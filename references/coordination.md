# Shared state and transport

## Contents

- Files and ownership
- Identity and initialization
- State schema
- Publishing and recovery
- Model changes and compatibility

## Files and ownership

Cross-agent state lives in `.dual-agent/` at the repository root. The skill's
references and templates stay in its installation directory. Persistent context
and user preferences live outside this scratch area; see [Configuration](configuration.md). Do not copy the
whole skill into the per-task state folder.

Use STATE.md as the coordination authority and HANDOFF.md as the current
transfer of context. The two development analysis files exist only for independent-analysis
rounds. Audit mode uses unit/round-scoped individual readings in its approved
report/scratch locations; see `references/audit.md`. The next agent sees only written/shared material, not the previous chat.

Keep `.dual-agent/` out of version control unless the user/team wants the trail
committed. Follow existing ignore policy; changing `.gitignore` is itself a
repository edit requiring user authorization and the current owner. Never silently
edit a target repository's ignore rules; this skill checkout's .gitignore cannot
protect files in another repository. Never put credentials in state.

`.dual-agent/` is a working area, not a history. Between tasks it holds only STATE,
HANDOFF and artifacts of programs that are still active (for example a method document
for an ongoing multi-slice audit, or a design blocked on an external dependency). Name
task-scoped files with the task identifier so the close-out can find them, write logs
and experiment scripts there only while the task runs, and follow the close-out in
SKILL.md when the task is done: evidence and useful tools to the agreed durable
location, the rest archived outside the repository and deleted after user review.

Use an agreed dedicated branch. For a non-git workspace or an already isolated
worktree, `branch: none` is acceptable. Check for existing user changes before
changing branches; never reset, stash, delete, or overwrite them without approval.

`turn` is a cooperative ownership record, not an atomic lock. Do not modify the
shared working tree, STATE, HANDOFF, or analysis files while another role owns the
turn. All writers must follow the same protocol; this package adds no background
watcher, lock daemon, automatic spawning, or concurrent editing service.

If true concurrent work is needed, agree on isolated workspaces and coordination
before proceeding. Merely changing a Markdown field cannot prevent write races.

## Identity and initialization

Use the `architect:` and `implementer:` model-name fields.
They describe assignments, not authenticated process identities.

When two separate sessions use the same model, add optional `architect_instance:`
and `implementer_instance:` labels, such as `terminal-a` and `terminal-b`, confirmed
by the user or trustworthy launch context. Do not invent session identifiers.
A fresh session must know its assigned role; matching a model name is insufficient.
The disclosed one-session fallback does not require fictitious second-session labels.

Before resuming, match the task, repository/branch, stage, and turn. Read the
active handoff and check its target role. If identity or task context conflicts,
ask the user rather than guessing. Do not restart initialization for an already
valid assignment just because a new session loaded the skill.

For a new task, bounded repository understanding, planning and a neutral
investigation packet can precede collaborator selection. Create coordinated STATE
only once actual participants are assigned (or the disclosed fallback is accepted).
Deliver an unpaired plan in chat or an authorized durable document; do not invent
participants or STATE. Before the first work-starting transfer, resolve only the
missing recipient assignment. Audit planning follows the same unpaired principle.
Ownership still prohibits repurposing an active task or writing on another turn.

An explicit new task after completion may initialize fresh state after preserving
the prior trail according to the user's policy and establishing the actual pairing.
Never repurpose an in-progress task or discard its handoff silently.

## State schema

Use the STATE template. Required fields and values:

| Field | Meaning |
|---|---|
| `task` | Current objective; do not silently reuse a completed task |
| `branch` | Dedicated branch name, or `none` for the cases above |
| `architect`, `implementer` | User-approved model assignments |
| `stage` | `investigation`, `implementation`, `review`, `correction`, or `done` |
| `turn` | `architect`, `implementer`, or `user` |
| `cycle` | Full-cycle number, initially 1 |

Optional metadata can record instance labels, client, effort actually configured,
mode, or a revision identifier when useful. Audit mode adds optional `workflow:
audit`, `audit_program`, `audit_phase`, `audit_unit`, and `audit_baseline`, not new
required fields or new `stage`/`turn` values. `mode: single-agent` retains its
original meaning. Audit participant assignments and prior first-pass identities
stay traceable in the program; an approved auxiliary model temporarily occupies
an existing role rather than becoming a third writer. Do not add placeholders for unknown
configuration and then treat them as observed facts.

Decisions are dated and appended in order. Findings record status, severity,
evidence, author, and the disposition reason. During an audit's blind first pass,
keep suspicions out of the shared ledger and handoff; save them in the reader's
separate artifact until both readings are frozen. After release, mirror them
with the existing ledger states and links to the richer audit evidence status. Keep a concise baseline note with
the repository revision and pre-existing dirty state when that affects review.
Do not require a new commit just to have a handoff.

`turn: user` pauses both agents. Resume only after a user decision, with an
explicit assignment of the next owner. A proposed model switch does not itself
change the current agent or transfer ownership.

## Publishing and recovery

Before a phase, read STATE and confirm ownership. Before publishing:

1. Update phase results, decisions, findings, and stage while retaining your turn.
2. Finish HANDOFF, including task/branch identity and honest validation status.
3. Re-read STATE to detect an unexpected ownership change. If it changed, stop
   and reconcile with the user; do not overwrite another agent's state.
4. Change `turn` last, then stop editing and show the same handoff in chat.

This ordering reduces incomplete handoffs but is not crash-proof transactional
storage. If a write was interrupted, a branch changed, or HANDOFF disagrees with
STATE, preserve the artifacts and reconcile before editing project code. Do not
interpret mismatched files as permission to take over.

Across machines, the user carries the state, handoff, and relevant code revision
or diff. The receiver verifies that the task and code snapshot match. An old
HANDOFF must not be used against an unrelated or newer tree without checking.

Context compaction or a new session is not evidence that state is current. Re-read
files and the relevant code. Keep pointers to detailed logs instead of pasting an
entire long conversation into the next agent's input.

Optional `repository` and `handoff_id` fields can bind the state to a workspace
and transfer when cross-machine ambiguity makes them useful. Older files without
them remain valid: use Baseline and HANDOFF to verify identity. Unknown optional
fields must survive updates. Unknown workflow/stage values require reconciliation,
not a guessed development route. The templates are Markdown contracts, not YAML
files; only the initial key/value block is metadata.

## Model changes and compatibility

A model recommendation is advisory. Explain the task reason, access requirements,
and expected quality/latency/quota tradeoff. Obtain approval, preserve the active state,
then update the affected model assignment and Decisions on the authorized turn.

Changing the Implementer model between phases is normal, not an exception: an audit,
its correction cycles, and a review can each warrant a different available model. Every
handoff that starts work carries a per-phase recommendation (see the HANDOFF
template). `implementer:` in STATE always names the currently approved model; record
the switch as a dated Decision when the user approves it.

If an agent exhausts its allowance mid-phase, do not write over its uncommitted work.
Back it up outside the repository, record where, and let the user decide who
continues; the continuing session reviews the partial work against the design first.
Record the actual receiving session; do not claim the running process changed
because a file changed. Never silently edit global client configuration.

Before moving to a smaller-context model, prepare a focused handoff with required
contracts, evidence, and file pointers. Do not assume the old session fits or that
context is transferred automatically.

The skill package version is independent of the state format. Development state
without optional workflow metadata remains valid. Audit state requires a reader
that understands `workflow: audit`; never treat it as ordinary development.
Preserve required fields and unknown optional content. Add instance/configuration
details only when needed and known. Leave valid active task state intact when
updating the skill; no bulk migration is needed.
