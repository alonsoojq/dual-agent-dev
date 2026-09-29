# Maintenance

Keep the development protocol stable and model advice replaceable. Read
[architecture and compatibility](architecture.md) before changing a contract.
Trace consumers in SKILL, references, templates, examples and tests; update them
together. Preserve active project state and external personal configuration.

After a change, run `python tests/check_package.py`,
`python tests/test_package_policy.py` and the relevant
[development](../tests/scenarios.md), [audit](../tests/audit-scenarios.md) and
[generality](../tests/generality.md) scenarios. Keep evaluation records outside the public package; do not pre-fill model-behavior
passes. [VALIDATION](../VALIDATION.md) documents the reproducible procedure.

Treat SKILL's `metadata.version` as the product version source; check the README
and initial changelog against it. Keep versions out of runtime prose. Use
[configuration format 1](configuration.md) independently of the release number.
Unknown optional state fields survive updates; incompatible changes need a
documented migration and preservation test.

Review the actual distribution, not merely files unignored by Git. Remove generated
caches, session artifacts, backups and private context. Preserve necessary recovery
copies outside the checkout. Check relative links and source provenance.
Update the reviewed `tests/public-files.txt` when public membership changes.
Validate the actual release directory/ZIP, not only the checkout; use the
commands and Git-export distinction in [VALIDATION](../VALIDATION.md).
The package has no automatic spawning, permission enforcement or background worker.

Refresh model advice only when an actual decision requires it, using
[the evidence rules](sources.md): re-read the provider page, update the claim and
its consultation date in the source register, and keep the notes' shared
structure. A new note needs a manifest entry and an index link. Do not add dashboards, dynamic catalogs or a
new orchestration service solely to keep optional recommendations current.
