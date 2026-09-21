"""Read-only publication policy; no Git ignore rules or target code execution."""
from pathlib import Path, PurePosixPath
import os
import re
import stat
import zipfile

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = PACKAGE_ROOT / 'tests' / 'public-files.txt'
MAX_FILE_BYTES = 8 * 1024 * 1024
MAX_TOTAL_BYTES = 32 * 1024 * 1024
PATTERNS = (
    ('machine-path', rb'[A-Z]:[\\/](?:Users|home)[\\/][A-Za-z0-9_.-]+'),
    ('machine-path', rb'/(?:Users|home)/[A-Za-z0-9_.-]+/'),
    ('private-key', rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    ('github-token', rb'\b(?:ghp|github_pat)_[A-Za-z0-9_]{30,}\b'),
    ('aws-access-key', rb'\bAKIA[A-Z0-9]{16}\b'),
)


class PackageError(ValueError):
    """Contains only a controlled category, redacted relative path and location."""


def safe_path(name):
    data = str(name).encode('utf-8', errors='backslashreplace')
    for category, pattern in PATTERNS:
        data = re.sub(pattern, ('[redacted-' + category + ']').encode(), data)
    # Escape control characters so filenames cannot inject terminal/log lines.
    return ascii(data.decode('utf-8', errors='replace'))


def reject(category, name, line=None):
    location = '' if line is None else '; line=' + str(line)
    raise PackageError('category=' + category + '; file=' + safe_path(name) + location) from None


def scan_sensitive(name, data):
    """Never expose a Match or quote data in an exception."""
    for category, pattern in PATTERNS:
        match = re.search(pattern, data)
        if match is not None:
            reject(category, name, data[:match.start()].count(b'\n') + 1)


def publication_issue(name):
    parts = PurePosixPath(name).parts
    lower = [part.lower() for part in parts]
    if any(p == '.env' or (p.startswith('.env.') and p != '.env.example') for p in lower):
        return 'private-environment'
    if any(p in {'.git', '.dual-agent', '__pycache__', 'node_modules'} for p in lower):
        return 'local-artifact'
    if any(p in {'.mcp.json', '.dual-agent-context.local.md'} for p in lower):
        return 'private-configuration'
    if any(re.search(r'(\.bak(?:-|$)|\.py[cod]$|~$|\.tmp$|\.sw[op]$|\.log$)', p) for p in lower):
        return 'temporary-or-backup'
    return None


def local_only(name):
    # Explicit package policy, independent of ignored/tracked Git status.
    return publication_issue(name) is not None or name == '.dual-agent-context.md'


def check_name(name):
    path = PurePosixPath(name)
    if (not name or path.is_absolute() or '\\' in name or ':' in name
            or any(ord(character) < 32 or ord(character) == 127 for character in name)
            or any(p in {'', '.', '..'} for p in name.split('/'))):
        reject('unsafe-path', name)
    scan_sensitive(name, name.encode('utf-8'))


def public_files():
    try:
        data = MANIFEST.read_bytes()
        scan_sensitive('tests/public-files.txt', data)
        names = data.decode('utf-8').splitlines()
    except (OSError, UnicodeError):
        raise PackageError('category=unreadable-manifest; file=tests/public-files.txt') from None
    names = [name for name in names if name and not name.startswith('#')]
    if len(set(names)) != len(names):
        reject('duplicate-manifest-entry', 'tests/public-files.txt')
    for name in names:
        check_name(name)
        if publication_issue(name):
            reject('private-manifest-entry', name)
    return set(names)


def is_link(path):
    info = path.lstat()
    return stat.S_ISLNK(info.st_mode) or bool(
        getattr(info, 'st_file_attributes', 0) & getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0))


def directory_entries(root, mode):
    def walk(directory, prefix=''):
        for entry in sorted(os.scandir(directory), key=lambda item: item.name):
            name = prefix + entry.name
            if mode == 'checkout' and local_only(name):
                continue  # Do not open private local content or follow its links.
            check_name(name)
            issue = publication_issue(name)
            if issue:
                reject(issue, name)
            path = Path(entry.path)
            if is_link(path):
                reject('symlink-or-reparse-point', name)
            if entry.is_dir(follow_symlinks=False):
                yield from walk(path, name + '/')
            elif entry.is_file(follow_symlinks=False):
                if entry.stat(follow_symlinks=False).st_size > MAX_FILE_BYTES:
                    reject('file-too-large', name)
                yield name, path.read_bytes()
            else:
                reject('unsupported-file-type', name)
    yield from walk(root)


def zip_entries(source):
    # Inspect bytes in place. Never extract paths or execute packaged Python.
    with zipfile.ZipFile(source) as archive:
        entries = archive.infolist()
        for item in entries:
            if item.orig_filename != item.filename:
                reject('unsafe-path', '<archive-entry>')
        raw_names = [item.filename.rstrip('/') for item in entries]
        for name in raw_names:
            check_name(name)
        # Accept an unwrapped tree or one conventional skill/release directory.
        prefix = ''
        if 'SKILL.md' not in raw_names:
            roots = {name.split('/')[0] for name in raw_names}
            if len(roots) != 1 or not next(iter(roots)).startswith('dual-agent-dev'):
                reject('zip-root', '<archive>')
            prefix = next(iter(roots)) + '/'
        seen = set()
        total = 0
        for item in entries:
            raw = item.filename.rstrip('/')
            kind = stat.S_IFMT(item.external_attr >> 16)
            if kind not in (0, stat.S_IFREG, stat.S_IFDIR):
                reject('symlink-or-special-zip-entry', raw)
            if (kind == stat.S_IFDIR and not item.is_dir()) or (kind == stat.S_IFREG and item.is_dir()):
                reject('inconsistent-zip-entry-type', raw)
            if item.flag_bits & 1:
                reject('encrypted-entry', raw)
            name = raw[len(prefix):] if raw.startswith(prefix) else raw
            if item.is_dir() and raw == prefix.rstrip('/'):
                continue
            check_name(name)
            key = name.casefold()
            if key in seen:
                reject('duplicate-or-case-collision', name)
            seen.add(key)
            issue = publication_issue(name)
            if issue:
                reject(issue, name)
            if item.is_dir():
                continue
            total += item.file_size
            if item.file_size > MAX_FILE_BYTES or total > MAX_TOTAL_BYTES:
                reject('archive-too-large', name)
            yield name, archive.read(item)


def load_package(source, mode='checkout'):
    """Return an immutable-by-convention byte snapshot before structural tests."""
    if mode not in {'checkout', 'release'}:
        raise ValueError('Unknown validation mode')
    source = Path(source)
    try:
        if is_link(source):
            reject('symlink-or-reparse-point', '<target>')
        if source.is_dir():
            entries = directory_entries(source, mode)
        elif mode == 'release':
            entries = zip_entries(source)
        else:
            reject('checkout-requires-directory', '<target>')
        required = public_files()
        allowed = required | {'.env.example'}
        result, seen = {}, set()
        total = 0
        for name, data in entries:
            if name.casefold() in seen:
                reject('duplicate-or-case-collision', name)
            seen.add(name.casefold())
            if name not in allowed:
                reject('unlisted-public-file', name)
            total += len(data)
            if total > MAX_TOTAL_BYTES:
                reject('package-too-large', '<target>')
            scan_sensitive(name, data)
            if b'\x00' in data:
                reject('binary-content', name)
            try:
                data.decode('utf-8')
            except UnicodeDecodeError:
                reject('non-utf8-content', name)
            result[name] = data
        for missing in sorted(required - result.keys()):
            reject('missing-public-file', missing)
        return result
    except PackageError:
        raise
    except (OSError, ValueError, RuntimeError, zipfile.BadZipFile, NotImplementedError):
        # Never echo exception text: OS/ZIP errors can include content or paths.
        raise PackageError('category=unreadable-package; file=<target>') from None
