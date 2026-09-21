# Validation and packaging

## Checkout versus actual publication

`tests/public-files.txt` is the reviewed list of required public files. An optional
root `.env.example` is allowed and scanned. No Git ignore rule selects publication
membership. New public files require explicit manifest review; unknown files fail
with `unlisted-public-file`. An ordinary name containing `env` is not an environment
violation, though it still needs manifest membership like any new public file.

Checkout mode permits recognized local artifacts: `.dual-agent/`, root repository
context, `.dual-agent-context.local.md`, `.mcp.json`, private environment files,
Git metadata, caches/dependencies, and known backup/temp/log suffixes. These are
excluded from its public snapshot without opening their contents. It does not
validate those files' safety or prove they are untracked. This exception is not
a permission to publish them. Arbitrary unlisted overrides are rejected rather
than silently classified as public. External user preferences stay outside the
checkout and are never discovered or copied by the checker/builder.

Release mode inspects every actual file in a supplied directory or ZIP. It rejects
private/temporary entries, missing/unknown public files, sensitive patterns, binary
or non-UTF-8 content, links/reparse points, unsafe/colliding archive paths and
encrypted entries. Private directory entries are rejected even when empty.
`.env`, `.env.local`, `.env.production`, `.env.development`, `.env.test` and other
private suffixes are forbidden at every depth, case-insensitively for portability.
Nested `.env.example` files are naming-policy exceptions but must be explicitly
listed in the manifest; only the root example is optional without a list edit.

Use a trusted checker to inspect a release; packaged Python files are treated
as data, not imported or executed. The scanner checks raw bytes before UTF-8
decoding or content-bearing assertions. Structural checks use a temporary snapshot
outside the source checkout. Current bounds are 8 MiB per file and 32 MiB total;
larger artifacts need a deliberate packaging-policy change, not silent omission.

## Reproducible commands

From the installed public skill root:

```text
python tests/check_package.py
python tests/test_package_policy.py
python tests/check_package.py --mode release --target .
python tests/check_package.py --build ../dual-agent-dev-release.zip
python tests/check_package.py --mode release --target ../dual-agent-dev-release.zip
```

Release validation of `.` is appropriate only for a clean distribution tree without
Git metadata or local artifacts. The builder uses the already validated public
snapshot; it never copies skipped local files and refuses to overwrite an existing
ZIP. Keep its output outside the checkout. On an I/O failure, no successful build
is claimed; inspect any incomplete output before retrying. Directory and ZIP
validation cover the same contents. ZIPs may have no wrapper or one
`dual-agent-dev...` wrapper directory.

For publishing a Git repository, validate an export of the exact commit you will
push, rather than treating the manifest-built ZIP as approval of that commit:

```text
git archive --format=zip --output=../publish-tree.zip HEAD
python tests/check_package.py --mode release --target ../publish-tree.zip
```

This includes tracked files regardless of `.gitignore`. A regression also exports
an isolated Git index tree containing a force-added private file and verifies its
rejection. Never use checkout mode to approve a commit or hand-built ZIP. These
checks cover the selected tree, not older Git history; review history separately
when publishing an existing repository. A directory without Git metadata has no commit history to validate. Test an
isolated Git export when preparing its first commit; validate the actual commit
export again before remote publication.

## Command and workflow validation

`python tests/check_package.py` also checks the command table, README examples,
links, state vocabulary and required permission/ownership boundaries against the
command contract. The Markdown decision cases in
[command scenarios](tests/commands.md) exercise default and natural-language entry,
unknown inputs, ownership, status, resume, review and audit dispatch. They are a
lightweight documentary check, not a runtime parser or proof of model behavior.

For changes to routing, walk each case against the final skill and record the
chosen route, allowed writes, stopping condition and supporting contract outside
the public package. For live forward tests use isolated repositories, real session
identities and authorized tools. Compare filesystem snapshots around status and
missing-state resume; record actual reads as well as writes when sealed reports
exist. Do not simulate an independent reviewer by renaming the author.

Retain the [development](tests/scenarios.md), [audit](tests/audit-scenarios.md) and
[generality](tests/generality.md) scenarios. The seven synthetic repository inputs
are [here](tests/fixtures/repositories.json); they are not production systems or
expected findings. Record what actually ran, including skipped/blocked checks.

## Evidence limits

Security regressions exercise redacted errors, environment-file policy, actual
publication membership, unsafe links, decode failures and build round trips.
Native filesystem symlink tests may be skipped when the host cannot create links;
ZIP link rejection is independently exercised. Pattern scanning cannot detect all
private prose or every secret format, so inspect every public file before release.

Passing structural checks or a documentary walkthrough does not prove live host
compliance, review independence, production safety or audit completeness. Keep
execution logs and temporary evaluation artifacts outside the public repository;
this document defines the repeatable validation policy.
