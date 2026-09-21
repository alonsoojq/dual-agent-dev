# Contributing

Keep changes tied to a demonstrated workflow need. Include the triggering request,
expected behavior, affected contract and validation evidence. Read
[architecture](references/architecture.md) before modifying state or handoffs.

Preserve active-task compatibility and update every affected consumer. Keep model
mapping optional, repository facts local, and evidence distinct from recommendations.
Use synthetic fixtures without secrets or private project data.

Run `python tests/check_package.py` and `python tests/test_package_policy.py`.
New public files require review and an entry in `tests/public-files.txt`.
Validate the actual directory/ZIP intended for publication in `--mode release`,
as described in [VALIDATION](VALIDATION.md); checkout success is insufficient.
For behavior changes, exercise relevant
development/audit scenarios and record whether evidence is structural, a fixture
walkthrough, or actual host execution. A passing text assertion is not a behavior
test. Do not claim unsupported host/model compatibility.

Command changes must update [the command contract](references/commands.md),
README examples and [command scenarios](tests/commands.md) together. Keep the
interface small; commands select intent without changing ownership or permissions.

Before proposing a release, inspect all distributable files for personal content,
private context, backups, session logs and credentials. The ignore file is not
proof of publish safety. Do not include active .dual-agent state in a contribution.
Contributions are distributed under the repository's [MIT license](LICENSE).
