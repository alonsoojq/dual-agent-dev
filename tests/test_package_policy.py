"""Synthetic regression cases for safe diagnostics and the actual publish set."""
import contextlib
import io
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import traceback
import unittest
from unittest import mock
import warnings
import zipfile

sys.dont_write_bytecode = True
import package_policy as policy
import check_package as checker

CHECKER = policy.PACKAGE_ROOT / 'tests' / 'check_package.py'


def fake_token():
    # Construct at runtime so the public test source contains no matching literal.
    return 'gh' + 'p_' + 'FAKE_SECRET_TEST_ONLY_' + 'A' * 12


class PublicationRegressions(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='dual-agent-policy-test-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / 'checkout'
        for name in policy.public_files():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((policy.PACKAGE_ROOT / name).read_bytes())

    def put(self, name, data=b'APP_MODE=synthetic\n'):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def rejected(self, target=None, category=None):
        with self.assertRaises(policy.PackageError) as caught:
            policy.load_package(target or self.root, 'release')
        if category:
            self.assertTrue('category=' + category in str(caught.exception), 'wrong safe error category')
        return caught.exception

    def run_checker(self, *args):
        return subprocess.run([sys.executable, '-B', str(CHECKER), *map(str, args)],
                              capture_output=True, text=True, encoding='utf-8')

    def make_zip(self, additions=None, prefix='dual-agent-dev/'):
        path = self.base / 'release.zip'
        with zipfile.ZipFile(path, 'w') as archive:
            for name in policy.public_files():
                archive.writestr(prefix + name, (self.root / name).read_bytes())
            for name, data in (additions or {}).items():
                archive.writestr(prefix + name, data)
        return path

    def test_sensitive_match_fails_without_any_stream_or_exception_value(self):
        token = fake_token()
        self.put('README.md', b'# Example\n' + token.encode() + b'\n')
        streams = [io.StringIO() for _ in range(3)]

        class FailingCheck(unittest.TestCase):
            def runTest(inner):
                policy.load_package(self.root, 'release')

        with contextlib.redirect_stdout(streams[0]), contextlib.redirect_stderr(streams[1]):
            result = unittest.TextTestRunner(stream=streams[2]).run(FailingCheck())
        self.assertFalse(result.wasSuccessful())
        output = ''.join(stream.getvalue() for stream in streams)
        self.assertTrue(token not in output, 'synthetic match leaked through unittest')
        self.assertIn('github-token', output)
        self.assertIn('README.md', output)
        self.assertIn('line=2', output)
        error = self.rejected(category='github-token')
        self.assertTrue(token not in str(error), 'exception contains matched value')
        self.assertTrue(token not in repr(error), 'exception repr contains matched value')
        process = self.run_checker('--mode', 'release', '--target', self.root)
        self.assertEqual(process.returncode, 1)
        self.assertTrue(token not in process.stdout + process.stderr, 'CLI leaked matched value')

    def test_sensitive_filename_is_redacted(self):
        token = fake_token()
        self.put(token + '.md')
        process = self.run_checker('--mode', 'release', '--target', self.root)
        self.assertEqual(process.returncode, 1)
        self.assertTrue(token not in process.stdout + process.stderr, 'filename leaked matched value')
        self.assertIn('redacted-github-token', process.stderr)

    def test_environment_names_in_real_distribution(self):
        for name in ('.env', '.env.local', '.env.production', '.env.development',
                     '.env.test', '.env.custom', 'nested/.env.local', '.ENV.LOCAL'):
            with self.subTest(name=name):
                path = self.put(name)
                self.rejected(category='private-environment')
                path.unlink()

    def test_environment_example_is_allowed_but_still_scanned(self):
        path = self.put('.env.example')
        self.assertIn('.env.example', policy.load_package(self.root, 'release'))
        nested = 'examples/.env.example'
        self.put(nested)
        with mock.patch.object(policy, 'public_files', return_value=policy.public_files() | {nested}):
            self.assertIn(nested, policy.load_package(self.root, 'release'))
        (self.root / nested).unlink()
        path.write_bytes(fake_token().encode())
        self.rejected(category='github-token')

    def test_incidental_env_name_has_no_environment_rejection(self):
        for name in ('environment.md', 'docs/env-guide.md', 'tools/env.py', 'env.local'):
            self.assertIsNone(policy.publication_issue(name))
            path = self.put(name)
            with mock.patch.object(policy, 'public_files', return_value=policy.public_files() | {name}):
                self.assertIn(name, policy.load_package(self.root, 'release'))
            path.unlink()

    def test_local_configuration_allowed_only_in_checkout(self):
        self.put('.dual-agent-context.local.md', fake_token().encode())
        files = policy.load_package(self.root, 'checkout')
        self.assertNotIn('.dual-agent-context.local.md', files)
        self.rejected(category='private-configuration')

    def test_local_state_backups_and_caches_are_never_distributed(self):
        for name in ('.dual-agent/STATE.md', 'nested/.dual-agent/HANDOFF.md',
                     'tests/__pycache__/module.pyc', 'README.md.bak-local', 'notes.tmp',
                     'trace.log', '.mcp.json'):
            with self.subTest(name=name):
                path = self.put(name)
                self.assertNotIn(name, policy.load_package(self.root, 'checkout'))
                self.rejected()
                path.unlink()
                # Remove only this fixture's newly empty directories.
                parent = path.parent
                while parent != self.root and not any(parent.iterdir()):
                    parent.rmdir()
                    parent = parent.parent

    def test_unlisted_files_require_publication_review(self):
        for name in ('STATE.md', 'local-overrides.md', 'unknown.bin'):
            with self.subTest(name=name):
                path = self.put(name)
                self.rejected(category='unlisted-public-file')
                path.unlink()

    def test_reference_walk_never_reads_outside_the_package(self):
        outside = self.base / 'outside.md'
        outside.write_text(fake_token(), encoding='utf-8')
        skill = self.root / 'SKILL.md'
        skill.write_text(skill.read_text(encoding='utf-8') + '\n[external](../outside.md)\n', encoding='utf-8')
        original_read = Path.read_text
        reads = []

        def record_read(path, *args, **kwargs):
            reads.append(path.resolve())
            if path.resolve() == outside.resolve():
                self.fail('reference walk attempted to read outside the package')
            return original_read(path, *args, **kwargs)

        with mock.patch.object(checker, 'ROOT', self.root), mock.patch.object(Path, 'read_text', record_read):
            checker.PackageChecks('test_runtime_references_reachable').test_runtime_references_reachable()
            with self.assertRaises(AssertionError):
                checker.PackageChecks('test_local_links_and_anchors').test_local_links_and_anchors()
        self.assertNotIn(outside.resolve(), reads)

    def test_binary_and_invalid_utf8_fail_safely(self):
        for data, category in ((b'\x00abc', 'binary-content'), (b'\xffabc', 'non-utf8-content')):
            with self.subTest(category=category):
                self.put('README.md', data)
                error = self.rejected(category=category)
                output = ''.join(traceback.format_exception(type(error), error, error.__traceback__))
                self.assertNotIn('UnicodeDecodeError', output)
                self.assertNotIn('abc', output)

    def test_sensitive_bytes_are_not_lost_to_decode_errors(self):
        self.put('README.md', b'\xff\x00' + fake_token().encode())
        error = self.rejected(category='github-token')
        self.assertTrue(fake_token() not in str(error), 'binary secret leaked')

    def test_file_and_directory_symlinks_not_followed(self):
        outside = self.base / 'outside'
        outside.mkdir()
        for directory in (False, True):
            link = self.root / ('linked-dir' if directory else 'linked-file')
            try:
                link.symlink_to(outside if directory else outside / 'missing', target_is_directory=directory)
            except OSError:
                self.skipTest('Host does not permit filesystem symlink creation; ZIP links tested separately')
            self.rejected(category='symlink-or-reparse-point')
            link.unlink()

    def test_clean_zip_and_directory_contain_the_same_bytes(self):
        expected = policy.load_package(self.root, 'release')
        self.assertEqual(policy.load_package(self.make_zip(), 'release'), expected)
        self.assertEqual(policy.load_package(self.make_zip(prefix=''), 'release'), expected)

    def test_private_file_manually_added_to_zip_is_rejected(self):
        for name in ('.env.local', '.dual-agent-context.local.md', '.dual-agent/STATE.md', '.git/config'):
            with self.subTest(name=name):
                self.rejected(self.make_zip({name: b'synthetic'}))

    def test_zip_traversal_duplicates_links_and_empty_private_directory(self):
        for name, category in (('../outside.md', 'unsafe-path'),
                               ('control\nname.md', 'unsafe-path'),
                               ('README.md', 'duplicate-or-case-collision'),
                               ('readme.md', 'duplicate-or-case-collision'),
                               ('.dual-agent/', 'local-artifact')):
            with self.subTest(name=name), warnings.catch_warnings():
                warnings.simplefilter('ignore', UserWarning)
                self.rejected(self.make_zip({name: b''}), category)
        path = self.make_zip()
        with zipfile.ZipFile(path, 'a') as archive:
            info = zipfile.ZipInfo('dual-agent-dev/link')
            info.create_system = 3
            info.external_attr = (stat.S_IFLNK | 0o777) << 16
            archive.writestr(info, '../outside')
        self.rejected(path, 'symlink-or-special-zip-entry')

    def test_zip_wrapper_link_is_not_silently_skipped(self):
        path = self.make_zip()
        with zipfile.ZipFile(path, 'a') as archive:
            info = zipfile.ZipInfo('dual-agent-dev/')
            info.create_system = 3
            info.external_attr = (stat.S_IFLNK | 0o777) << 16
            archive.writestr(info, '../outside')
        self.rejected(path, 'symlink-or-special-zip-entry')

    @unittest.skipUnless(shutil.which('git'), 'Git is unavailable')
    def test_private_file_in_git_index_is_rejected_in_export(self):
        self.put('.dual-agent-context.local.md')
        for arguments in (['init', '--quiet'], ['-c', 'core.autocrlf=false', 'add', '--force', '.']):
            result = subprocess.run(['git', '-C', str(self.root), *arguments], capture_output=True)
            self.assertEqual(result.returncode, 0, 'fixture Git setup failed')
        tree = subprocess.run(['git', '-C', str(self.root), 'write-tree'], capture_output=True, text=True)
        self.assertEqual(tree.returncode, 0, 'fixture Git index export failed')
        path = self.base / 'index.zip'
        result = subprocess.run(['git', '-C', str(self.root), 'archive', '--format=zip',
                                 '--output=' + str(path), tree.stdout.strip()], capture_output=True)
        self.assertEqual(result.returncode, 0, 'fixture Git archive failed')
        self.rejected(path, 'private-configuration')

    def test_cli_build_excludes_local_files_and_does_not_overwrite(self):
        self.put('.dual-agent-context.local.md', fake_token().encode())
        output = self.base / 'release.zip'
        build = self.run_checker('--target', self.root, '--build', output)
        self.assertEqual(build.returncode, 0, 'build failed; inspect with sanitized checker')
        files = policy.load_package(output, 'release')
        self.assertNotIn('.dual-agent-context.local.md', files)
        verify = self.run_checker('--mode', 'release', '--target', output)
        self.assertEqual(verify.returncode, 0, 'release check failed')
        original = output.read_bytes()
        repeat = self.run_checker('--target', self.root, '--build', output)
        self.assertEqual(repeat.returncode, 1)
        self.assertTrue(output.read_bytes() == original, 'existing archive changed')
        self.assertTrue(fake_token() not in build.stdout + build.stderr + verify.stdout + verify.stderr)


if __name__ == '__main__':
    unittest.main(verbosity=2)
