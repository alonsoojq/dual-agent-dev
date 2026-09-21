# Audit program template — adapt after repository reconnaissance

Do not copy these placeholders as observations. Produce the program in the user's
language and the project's chosen report location. This is a coverage/evidence
contract, not a template architecture or a mandate to edit target code.

The numbered sections below are information duties, not mandatory document length
or headings. For a small repository, combine them into a compact plan: actual
baseline/inventory, units/contracts, participants/permissions, verification/limits,
and completion/next action. Link the skill's protocol rather than restating its
generic rules. Retain every repository-specific fact, decision and boundary needed
to execute the plan; avoid boilerplate that outweighs the inspected system.

---

# Audit program — <actual repository / scope>

**Status:** planned, not executed. **Authority:** <request and approval state>.
**Baseline:** <actual SHA + dirty snapshot identity, or file-hash manifest>.
**Prepared by:** <real session/model, or explicitly unknown>. **Date:** <actual>.

## 1. Objective and boundaries

Explain the intended reading: integral system understanding, scoped module audit,
or another explicitly agreed scope. Record deliverables, normative constraints,
what is not authorized, and any current start gate. Old example start gates are
not inherited. No patches, historical-document edits, merges or deploys in audit.

## 2. What the repository actually contains

Summarize the observed stack, entry points, boundaries, data and state flows,
external effects and tests, with paths/symbols and snapshot evidence. Distinguish
reconnaissance observations from behavior that the audit still needs to establish.
Do not call a manifest or static graph a completed reading.

| Area / actual paths | Owned / generated / third-party / external | Evidence | Proposed scope and inspection method |
|---|---|---|---|
| <observed area> | <classification> | <snapshot and pointer> | <included or explicit proposed exclusion> |

Account for relevant untracked/ignored owned code, tests, fixtures, SQL/migrations,
scripts, configuration/CI, documentation, and non-text assets. Record secret
handling and inaccessible surfaces without values. Exclusions require agreement.

## 3. Reading units and order

Choose cohesive units from actual dependencies and responsibilities, not example
folder names. Explain why this order and why the first unit calibrates the method.
Priority determines order, not omission. No target defects/lines/folders per day.

| ID | Purpose / concrete members | Important dependencies / flows | Tests, data, docs | Order rationale | Required readers |
|---|---|---|---|---|---|
| <assigned unit> | <actual files/symbols> | <verified pointers / unresolved links> | <actual or missing> | <consequence/coupling/unknowns> | <approved sessions or unassigned> |

Use a linked exact membership inventory for large units; no ellipses hiding scope.
Define how newly discovered owned files and cross-unit dependencies are handled.

## 4. Current contracts and documentary inventory

Identify normative requirements and their authority. Record proposals, historical
audits and implementation descriptions separately. Preserve a neutral first-pass
packet: inventory earlier verdict-bearing reports by reference but defer reading
those verdicts until the independent analyses are saved. Never rewrite a contract
to conform to contradictory code. Mark ambiguous rules as decisions to resolve.

## 5. Participants, handoffs and independence

Record real or proposed participants, available clients/tools, quota constraints,
approved assignments and unknowns. Model recommendations are not invocations.

| Phase | Role/session and model | Assignment approved? | Inputs before first pass | Deliverable / verifier |
|---|---|---|---|---|
| Optional reconnaissance | <actual/proposed/unassigned> | <source> | Repository + neutral requirements | Factual map; suspicions held separately |
| Independent reader A | <actual/proposed/unassigned> | <source> | Same source snapshot + neutral packet | Own explanation, candidates, coverage |
| Independent reader B | <actual/proposed/unassigned> | <source> | Same source snapshot + neutral packet | Own explanation, candidates, coverage |
| Verification / consolidation | <actual/proposed/unassigned> | <source> | Both saved readings + candidate union | Evidence and report; no self-only verification |

Define save-before-reveal, identity/hash records, contamination handling, a neutral
handoff and an unavailable-participant fallback requiring disclosed approval.
Sequential sessions suffice. Keep the two-owner STATE schema; an auxiliary agent
uses an approved temporary role assignment, not a new turn value or shared writer.

## 6. Verification plan and safe environment

List commands/checks actually discovered, what each could establish, whether it
has already run, and its environment/side effects. Include normal, rejection,
retry, concurrency/event-order and partial-failure scenarios only as relevant.
A proposed scenario is not a finding. Do not invent execution results.

| Check / evidence route | Repository source | Property / reachable scenario | Environment, permissions, isolation | State |
|---|---|---|---|---|
| <actual check or proposed static investigation> | <path/symbol> | <question> | <verified/pending; external effects controlled> | <not run / actual result> |

Specify forbidden production effects, isolation/serialization of any mutable resources, how
scratch probes are kept off target production files, and unresolved dependencies.
Static and executed evidence must remain distinct.

## 7. Report product and evidence standard

Name the chosen durable destination, confidentiality boundary and actual
tracking/ignore status (or non-Git). Keep sensitive evidence in an agreed private
location; make only sanitized reports candidates for version control. Require an index, understandable unit reports, per-reader coverage,
original independent readings, and a durable finding/verification trail; combine
or split documents proportionately. Use the unit report's six responsibilities.

A defect requires location/rule, reachable wrong behavior, practical consequence,
and verification with resolved preconditions. Keep pending/refuted/duplicate and
non-defect observations separate. Severity, certainty and remediation are distinct.
No majority vote, defect quota, or treating non-detection as proof of correctness.

## 8. Calibration, sequencing and checkpoints

Select the actual first unit. Check demonstrated findings and whether a reader
can understand its main journey from the report. Record method adjustments without
recursive audits. Save while reading, by file/range and snapshot; one writer at a
time. Specify where unread ranges, gaps and next action survive context/quota loss.

## 9. Completion, pauses and changes

Define per-unit and whole-program completion: requested per-reader coverage,
required verification, documentary reconciliation, explanation, traceability and
no essential evidence gaps. An open confirmed defect can coexist with a completed
audit; unperformed essential verification cannot. Missing permissions or urgent
live risk pause work rather than authorizing fixes.

Describe how source changes invalidate affected evidence or trigger rebaselining.
Audit completion is not remediation completion. Corrections need separate scope,
authorization and the normal development/review route; link them to original
findings without rewriting history.

## 10. Decisions pending and next action

List actual unanswered scope/assignment/environment decisions, not generic questions
already answered. State the program path/revision to approve and the first safe
execution step. `audit run` may approve this identified plan; it does not approve
production writes. Do not claim any audit unit completed during reconnaissance.
