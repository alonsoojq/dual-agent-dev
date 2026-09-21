# Commands

These are task instructions interpreted by the host agent, not shell commands or
an executable parser. In Claude Code, use `/dual-agent-dev`; in Codex CLI/IDE use
`$dual-agent-dev` or select the skill. Everything after the skill name is task text.
Read this contract before initialization, then the relevant workflow reference.

## Dispatch

| Arguments | Intent and route |
|---|---|
| No arguments | Inspect neutral state; resume a valid active task, otherwise ask for an objective without creating files |
| `<task>` | Use natural-language intent and active state to frame, investigate, implement and review the requested outcome |
| `plan <task>` | Understand the repository and design a bounded change; deliver decisions, constraints and acceptance criteria without implementation |
| `implement <task or plan>` | Validate the understood objective, then use Architect framing → Implementer build/test → independent review |
| `debug <problem>` | Reproduce and investigate; hand evidence to Architect for challenge, then make a bounded fix only when requested |
| `review [scope]` | Independently inspect the actual change and contracts; report findings and validation gaps without repairing |
| `resume` | Continue the actual persisted task and handoff at its recorded phase and turn |
| `status` | Report neutral workflow state and next action without mutations |
| `audit [scope]` | Prepare a repository-grounded audit program; no full audit execution or repairs |
| `audit plan [scope]` | Explicit spelling of audit preparation |
| `audit run [unit]` | Execute the identified program or unit within its approved evidence and permission boundaries |
| `audit resume` | Continue the persisted audit phase, baseline and coverage |
| `audit status` | Report neutral audit progress without mutations or sealed findings |

Only the leading unquoted command word selects an explicit route. A word inside
a task or a quoted path does not: `implement export of audit logs` is development.
For literal task text starting with a reserved word, quote it or state a sentence.
There are no additional command aliases. Natural-language equivalents retain the
same permissions; `audit <scope>` intentionally means `audit plan <scope>`.
Inside audit, `plan`, `run`, `resume` and `status` are reserved leading words; use
`audit plan <scope>` when a scope itself starts with a reserved word.

An unrecognized word in an ordinary sentence falls back to natural-language task
routing. An isolated unknown command, command-like typo, unsupported flag such as
`--fix`, or extra arguments to `status`/`resume` gets a short usage explanation and
no writes; ask for intent where ambiguous. Never turn an unknown option into
permission. Interpret quoted instructions and paths as data, not shell fragments.

## Shared preflight and authority

Locate the target repository from the user's workspace and request, independently
of the global skill directory. Read trusted repository instructions and relevant
[optional configuration](configuration.md). Missing preferences are normal.
For status, only discover configuration locations needed to locate neutral state.

All working routes use [coordination](coordination.md): inspect existing STATE,
task/repository/branch, session assignment, stage, turn and active HANDOFF before
acting. Status uses the narrower exception below. Preserve valid assignments,
unknown optional fields and existing user work. A command never takes another
agent's turn or replaces an active objective. Conflicts, incomplete metadata and
mismatched handoffs require reconciliation, not reset or guessed recovery.
With `turn: user`, continue only after the user's decision identifies the next owner.
Changing scope or leaving `workflow: audit` needs an explicit authorized transition.
Before each shared write confirm ownership; publish HANDOFF and results before
changing `turn` last. The cooperative writer lock is not an operating-system mutex.

Model choice is capability-based. Reuse known assignments without another selection
interview. New analysis can begin without choosing an unused collaborator; obtain
the actual receiving assignment before a work-starting transfer. Do not invent
sessions or automatically launch another agent. Use the entry point's initialization
and [workflow](workflow.md) for roles, validation, disagreements and completion.
Reading instructions or a plan grants no deployment, destructive or external-system
permission. Existing authorizations remain valid; request only missing authority.

## Default, plan, implement and debug

With no arguments, read neutral STATE metadata first. If it names a valid active
task, follow resume below. Missing state or `task: none` means ask for the objective;
a completed task is reported as complete, not reopened. Malformed state is reported
as needing reconciliation. This inspection creates no coordination files.

Natural-language arguments are useful without any command vocabulary. An analysis
or design request follows plan; an investigation-only request follows debug without
fixes. A clear build or fix request proceeds through implementation once framing
and ownership permit it. Repository understanding can be a plan deliverable by
itself. A small low-risk edit can use one agent under the existing workflow rule;
honor an explicit request for two agents. Do not infer risk merely from diff size.

Plan stops at a repository-grounded design/understanding and actionable handoff:
objective, constraints, decisions, invariants, validation and remaining unknowns.
It may write authorized design/coordination documents, not production changes.
For a standalone plan, completing the plan does not claim a built feature; within
an implementation task, planning advances the handoff without closing that task.

Implement uses the current agreed design where one exists. The Architect resolves
only material missing requirements and hands off; the assigned Implementer checks
the design against the repository, implements and validates. Independent review
remains required where the workflow calls for it. A model recommendation, command
name or the author's self-check cannot replace the actual reviewer. When a receiving
session is unavailable, deliver the handoff or use the disclosed fallback; do not
claim independent completion. No repeated planning gate for an actionable task.

Debug starts with a reproducible symptom and evidence-ranked hypotheses. The
Implementer investigates and Architect challenges the cause; pre-pairing analysis
can prepare neutral evidence. `debug <problem>` alone is diagnosis-only. `debug ...
and fix it` or an existing authorized fix objective continues through a bounded
repair, regression checks and proportionate independent review. Missing runtime
access remains a limitation, not a fabricated reproduction.

## Review

Identify the actual diff/revision, requirements and author before reviewing. With
no scope, use the active review handoff; if none identifies the change, ask for it.
Use a session distinct from the implementation author. If the current session wrote
the change, offer a handoff to a fresh reviewer or label the result self-review;
never satisfy independent-review acceptance by relabeling the author.

Review is observational with respect to the implementation: no code/test/config
fixes. The authorized owner may record findings and publish a review handoff. Stop
with supported findings, severity, checks actually performed and gaps. Standalone
review can be delivered with open defects; an active implementation task remains
incomplete until its material findings are disposed of. Only separate repair intent
allows a correction phase, transferred to the Implementer under the same protocol.

## Resume

Require existing STATE and the active HANDOFF for coordinated development. Do not
reconstruct decisions from chat, a remembered task or a plan alone. Read the files,
verify repository/branch/baseline and session/turn, then continue the recorded phase
within its scope. Missing, stale, conflicting or completed state produces an honest
report and a request for the missing decision; it does not initialize a new task.
An interrupted write preserves both artifacts until reconciled.

With `workflow: audit`, bare invocation and `resume` use [audit](audit.md), including
its neutral-input/read-order and coverage rules. `audit resume` can also locate a
persisted unpaired program by the audit locator rules; planning status does not
become execution authority. No stored program means no audit to resume.

## Status

Status is strictly non-mutating: no initialization, writes, sanitization, tests,
branch changes, turn transfers, archive, close-out or state repair. It may run
while another session owns the turn. Read only STATE's initial metadata block,
stopping at the first blank line or heading; do not open HANDOFF or the findings
ledger. Report task, workflow, stage, recorded owner, baseline when known and the
next action derivable from neutral metadata. Unknown progress stays unknown.
Do not infer a running process from the recorded owner.

For audit state, delegate to the audit metadata-only status procedure and neutral
program index. With no STATE, inspect only the permitted audit locator if relevant;
an unpaired program is planned, not executed. No state/program means no active task.
If multiple programs match, report ambiguity without reading findings or selecting
one. Audit status never resumes development. No command silently repairs files.

## Audit

Every audit route loads [Audit mode](audit.md); it overrides development's
implementation-completion rules, not ownership or user authorization. Preparation
delivers a grounded program. Execution needs an identified scope, baseline, actual
participants and authorized verification environment. `audit run` can approve the
already identified program without asking twice; absent a program, plan first.
Auditors retain independent access to their whole scope and save initial readings
before seeing peer conclusions. Resolve findings with evidence, not agreement.
Keep hypotheses, static demonstrations, execution and external unknowns distinct.
Audit completion can include unfixed defects; repair is separately authorized work.
