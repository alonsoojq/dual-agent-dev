# Workflow reference

## Contents

- Roles and routes
- Independent analysis
- Review and findings
- Material risk
- Disagreement and stopping
- Single-agent fallback

## Audit-mode precedence

For an explicit `audit` route, use `references/audit.md`. It changes the deliverable
from implementation to documented understanding and verified findings. The generic
fix-before-done, diff-review and chosen-design rules below remain development rules,
not instructions to repair code during an audit. Audit execution also preserves
separate first-pass reports before comparison; a verifier who only reads another
agent's diagnosis has not performed an independent discovery pass.

## Roles and routes

Commands select the deliverable through [Commands](commands.md). Plan-only,
diagnosis-only and review-only requests stop at their requested output; the repair
and implementation-completion steps below apply only when implementation is in
scope. They do not silently widen an analysis request.

The Architect owns framing, constraints, system-level reasoning, design
tradeoffs, and review by default. The Implementer owns reproduction, repository
validation, implementation, tests, and necessary corrections by default.
Both may challenge assumptions. A handoff is a proposal, not unquestionable truth.

### Small change

Use one agent for low-risk copy, isolated styling, mechanical edits, and obvious
local fixes. Do not create coordination artifacts unless the user insists on a
two-agent process. A small diff does not establish low risk.

### Normal feature

Architect investigates the objective and produces a bounded implementation
handoff. Implementer verifies assumptions, builds, and tests. Architect reviews
the actual diff against the objective and invariants. Implementer addresses
valid findings and performs final checks. Stop when the criteria are met.

### Difficult bug

Implementer reproduces the failure, collects concrete evidence, and traces the
relevant data/control flow. Architect challenges the explanation and checks
system-level implications. Implementer fixes the supported cause and adds
appropriate regression coverage. A final architecture review is required when
material risk is involved; otherwise it is optional.

Reading another agent's diagnosis and challenging it is critical review, not
blind independent discovery. Use the independent route only when that distinction
matters; do not require it for every bug.

### Architectural refactor

Obtain independent analyses of the same objective, constraints, and neutral
evidence. Compare assumptions, complexity, migration risk, compatibility, and
testability. Select a direction before implementation. Product tradeoffs require
the user's decision; evidence may settle purely technical alternatives.

### Risky migration or structural change

Architect establishes invariants, migration boundaries, rollback concerns, and
acceptance criteria. Implementer validates those against the repository, changes
incrementally, and tests migration/regression behavior. Architect reviews the
architecture; Implementer resolves justified findings and verifies the result.

These are default sequences, not fixed implementation recipes. Record a justified
variation rather than adding unnecessary phases merely to follow a diagram.

## Independent analysis

This is a procedural read-order rule, not a security boundary or OS-enforced
information barrier. Shared files remain technically readable.

At the start of a round, archive prior per-task analysis files if needed; do not
delete unrelated user work. Put the current task and repository revision in each
analysis so an old result cannot masquerade as current evidence.

For development, each agent writes its own `.dual-agent/analysis-architect.md` or
`.dual-agent/analysis-implementer.md` before reading the other's analysis. Audit
mode uses per-unit/per-round saved artifacts and its additional neutral-handoff,
scout-findings and per-reader-coverage rules. Respect
the normal turn ownership even when writing scratch analyses. Use neutral
handoffs and avoid bulk reads that accidentally include the other analysis.

After both files exist for the same round, compare them on the active owner's
turn. Record the chosen direction and any remaining product decision in STATE.
Neither simultaneous execution nor a third agent is required.

If an agent reads the other solution early, label that contribution as influenced,
not independent. Do not claim to erase the influence by rewriting it. Record the
issue and either use ordinary cross-review or obtain a genuinely fresh session
when independent discovery is necessary. Involve the user if that changes scope.

## Review and findings

Reconstruct the objective from STATE and HANDOFF, inspect the diff and surrounding
code, and verify important assumptions independently. Review behavior, invariants,
regressions, and relevant tests. Do not invent a defect to justify the review.

Record each material finding with severity, concrete evidence, the affected
criterion/invariant, and a reproducible check when available. The ledger supports
`open`, `resolved`, and `rejected` plus `blocking`, `important`, and `optional`.
A clean review may record one concise "no material findings" entry.

The Implementer evaluates each finding: valid, already handled, unsupported,
outside scope, or optional. Resolve valid defects; reject unsupported findings
with evidence. An actual defect is not safely rejected merely because its fix
is inconvenient. Accepting product risk belongs to the user and must be explicit.

Do not weaken tests to conceal a regression. Updating tests is legitimate when an
approved behavior change invalidates old expectations; explain the contract change
and preserve meaningful coverage. Running one's own checks is always allowed and
expected; claiming those checks are independent review is not.

## Material risk

Require architecture-focused review for changes involving security boundaries,
authentication/authorization, destructive operations, data/schema migration,
public APIs or wire contracts, concurrency/shared state, money/billing/quotas,
or invariants spanning modules. The requirement applies to every model.

Read-only analysis of a risky area is not automatically permission to edit it.
A model's cyber capability rating does not establish production safety or grant
permission to perform offensive actions.

## Disagreement and stopping

Bound disagreement to at most two exchanges of reasoning. Resolve technical
claims with repository evidence, a reproduction, or a bounded experiment.
Escalate product/scope choices with the competing positions, not another audit.

One cycle is framing/investigation → implementation → review → correction.
Start at `cycle: 1`. Increment only for a new full cycle justified by new evidence
of a material correctness problem, regression, or broken invariant. Optional
cleanup, style preferences, or a model switch alone do not justify another cycle.

For implementation, finish when requested behavior and acceptance criteria are satisfied, relevant
checks have actually passed, and no material finding remains unresolved.
Document evidence-backed rejections and user-approved risk decisions. Optional
findings may remain. Set `stage: done`, then publish `turn: user` last.

If required validation is unavailable or fails for an unresolved reason, retain
the current stage and hand control to the user or appropriate role. Say what
was not tested; do not mark missing evidence as a pass.

## Single-agent fallback

For substantial tasks with only one available agent, retain STATE/HANDOFF and
record `mode: single-agent` in the optional metadata or Decisions. Put the same
model under both role fields. Separate investigation, implementation, and review;
prefer a fresh review session when available.

For a competing-design exercise, explicitly consider the strongest alternative,
but do not call that independent analysis. State the limitation. This fallback
is not a reason to create coordination files for a trivial one-agent edit.
