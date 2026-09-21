# STATE template — copy the body below to .dual-agent/STATE.md

Keep existing compatible state. Replace angle-bracket fields with known facts;
do not copy example identities or optional values as observations.

```text
task: <one-line objective>
branch: <dedicated branch, or none for non-git/already-isolated workspace>
architect: <user-approved model>
implementer: <user-approved model>
stage: investigation
turn: architect
cycle: 1

## Baseline
- <repository revision and relevant pre-existing dirty state, or unknown>

## Decisions
- <date> — <decision and evidence/authority>

## Findings ledger
- [open|resolved|rejected] (blocking|important|optional) <finding; evidence; disposition reason when applicable> — raised by <role> (<model>)
```

Only add a ledger entry when there is a real finding or review outcome; remove
the template line on initialization. For a review with no material findings, one
resolved optional entry is enough. Do not manufacture an issue to fill the ledger.

Optional fields, only when needed and known. Insert them in the initial metadata
block before `## Baseline`; preserve unknown optional fields in existing state:

```text
repository: <workspace identity, only when useful>
handoff_id: <shared transfer identifier, only when useful>
architect_instance: <confirmed session/terminal label>
implementer_instance: <confirmed session/terminal label>
architect_client: <client and version, when relevant>
implementer_client: <client and version, when relevant>
implementer_effort: <actually configured value; not merely a recommendation>
mode: single-agent
workflow: audit
audit_program: <actual path; audit only>
audit_phase: <planning | reading | verification | reporting | paused | complete>
audit_unit: <actual current unit, when applicable>
audit_baseline: <actual source snapshot identity>
```

Audit fields are optional and do not authorize implementation. Use `workflow:
audit` for the route, `stage: investigation` while reading and `stage: review`
while verifying/reporting. Keep rich evidence states in reports. During blind
reading, STATE/HANDOFF contain neutral progress only, not peer suspicions. A
plan-only draft without paired execution does not require STATE initialization.
Audit completion can leave confirmed unfixed defects, but not essential unverified
claims; see `references/audit.md` before setting `done`.

Use `mode: single-agent` only for the disclosed fallback. Initial ownership may
be assigned differently by the user. Publish `turn` changes last and set
`stage: done` plus `turn: user` only when completion conditions are satisfied.
