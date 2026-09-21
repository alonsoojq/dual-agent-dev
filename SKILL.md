---
name: dual-agent-dev
description: Coordinate explicitly requested dual-agent software development through planning, implementation, debugging, independent review and persisted handoffs. Resume tasks, inspect status, or plan and run repository-grounded audits. Do not activate for ordinary coding, model comparisons, or edits to this skill itself.
license: MIT
metadata:
  version: "1.0.0"
---

# Dual-Agent Development Workflow

Coordinate two engineering collaborators, normally in separate sessions or
terminals. The Architect frames the problem and reviews; the Implementer
investigates, builds, and validates. Either can investigate or challenge a plan.
The objective is independent judgment, not duplicate work or extra ceremony.

## Configuration before initialization

Read [Configuration](references/configuration.md) on entry to discover optional
user preferences and repository context. Missing files mean use this skill's defaults.
Configuration supplies preferences and sourced context; it does not grant execution
permissions, replace a valid active assignment, or weaken evidence/independence.
For `status` and `audit status`, inspect only neutral progress and configuration locations needed
to locate the program; keep sealed findings and unnecessary private data out of output.

## Command dispatch — before initialization

Editing or discussing this skill is artifact work, not execution of its workflow.
For an actual invocation, interpret the user's invocation arguments as task text,
never as shell commands. Hosts may append arguments to the skill or provide them
in the user's prompt. Do not require a particular
placeholder expansion or invent an executable named `dual-agent-dev`.

Read [Commands](references/commands.md) for every invocation before initializing
or changing state. It is the authoritative command contract: natural-language task
or no arguments, `plan`, `implement`, `debug`, `review`, `resume`, `status`, and
`audit` with `plan`, `run`, `resume`, `status`. These route into the shared workflow;
they never override ownership, permissions, active scope or independent review.
Dispatch observational status before reading a handoff or findings ledger.

For any audit route, first read [Audit mode](references/audit.md). It supplies the
mode-specific initialization, evidence, and completion rules. In particular:
planning does not require selecting an unused Implementer; `audit` never grants
production-code edits, fixes, merges, or deployments; confirmed open defects do
not by themselves prevent completion of a properly evidenced audit report.
All shared-state ownership, user authorization, and preservation rules still apply.
When active STATE has `workflow: audit`, a bare skill invocation or continuation
uses the audit reference even without an `audit` argument. A new development
objective requires an explicit transition, not silently leaving audit-only mode.
Never replace an active development task with an audit task without authorization.

## Operating contract

- The user owns scope, product decisions, and model selection. Recommendations
  do not authorize switching models, changing global settings, or spawning agents.
- **Every handoff that starts work for another agent carries a task-fit model
  recommendation for that phase.** Choose an available model whose capability
  matches the phase's risk and unknowns; never default to the previously used model
  just because it was used before. Use the user's actual cost, latency or quota
  constraints when supplied. The user approves or overrides; the Architect decides
  what to recommend.
- Handoffs convey objectives, evidence, constraints, invariants, and acceptance
  criteria. Let the recipient determine the implementation. Exact steps or file
  boundaries are justified by the task, not by stereotypes about a model.
- Inspect repository evidence; do not treat a prior agent's plan as ground truth.
  Distinguish observations, hypotheses, recommendations, and unverified claims.
- One writer at a time. `.dual-agent/STATE.md` records the current owner; it is
  a cooperative turn protocol, not an operating-system mutex.
- Author and independent reviewer should be separate sessions. The same model
  can fill both roles in different sessions; model name alone is not identity.
- Every implementer validates its own work. That is not a substitute for an
  independent review when the change warrants one. Never weaken a test merely
  to make it pass; legitimate requirement-driven test changes need justification.
- Protect existing user edits, secrets, and unrelated code. Do not deploy, perform
  destructive actions, or expand permissions without the required authorization.
- Stop when acceptance criteria and proportionate validation are satisfied.
  Implementation requires disposition of material findings; audit mode requires its
  coverage/evidence/reporting contract, not repairs. Do not manufacture another audit.

## Load only the material needed

Read this file first. Resolve the paths below relative to the skill directory,
not the target repository. Do not load every reference or model profile at once.

| Situation | Read |
|---|---|
| Starting or resuming any coordinated task | [Coordination](references/coordination.md) |
| Planning, running, resuming, or reporting an audit | [Audit mode](references/audit.md) |
| Creating a repository-specific audit program | [Audit program template](templates/AUDIT-PROGRAM.md) |
| Reading a unit or verifying/consolidating audit evidence | [Audit reporting](references/audit-reporting.md) and [Unit report template](templates/AUDIT-UNIT.md) |
| Understanding the public/private boundary and design rationale | [Architecture](references/architecture.md) |
| Checking audit behavior after an edit | [Audit regression scenarios](tests/audit-scenarios.md) |
| Choosing a route, investigation, review, disagreement, or completion | Relevant section of [Workflow](references/workflow.md) |
| Selecting a model, recommending one for the next phase, effort, or a switch | [Model selection](references/model-selection.md) plus the relevant profile |
| Creating shared state | [STATE template](templates/STATE.md) |
| Publishing a handoff | [HANDOFF template](templates/HANDOFF.md) |
| Verifying a model claim or refreshing the skill | [Sources](references/sources.md) and [Maintenance](references/maintenance.md) |
| Checking this skill after edits | [Regression scenarios](tests/scenarios.md) |

Roles describe needed capabilities. Optional model notes are replaceable handoff
advice, not a required roster or proof of access. Check client-reported availability,
effort options and effective context before making a concrete assignment.

## Entry and initialization

First distinguish executing this workflow from discussing or editing it.
A request to improve this skill does not itself start a dual-agent task.

**Existing task:** `status` and `audit status` use the read-only metadata-first exception in
the audit reference. For other resumptions, read `.dual-agent/STATE.md` and the
active handoff. Confirm that the task, repository, branch, role/session, stage,
and turn match this work.
Resume without asking for model selection again when the assignment is clear.
Do not take the turn merely because you use the listed model. If another agent
owns it, stop work; status may still report read-only. If `turn: user`,
wait for the user's decision before resuming a work phase.

**New task:** if no objective was supplied, ask for it without inventing a task.
Otherwise classify the requested work from the information already supplied.
For a small, obvious, low-risk change, recommend one agent and avoid creating
`.dual-agent/`. If the user expressly wants two agents anyway, honor that choice.
Do not run model-selection ceremony for a task that will not use this workflow.

For a new **development** task (audit has its own initialization):

1. Inspect repository identity, trusted instructions, dirty state and relevant
   contracts. The invoking session frames the task as Architect by default;
   `implement` does not silently reassign it as Implementer. Report unknown model
   identity honestly. No participant interview is needed for bounded analysis,
   design or a neutral investigation packet.
2. Reuse explicit session assignments and authorized local preferences. At the
   first work-starting handoff, recommend the required capability and an available
   model when known. Ask only for a missing receiving-session assignment or an
   actual switch; a preference alone is not an assignment. No automatic spawning.
3. Create coordinated STATE only when the pairing is established, or when the
   disclosed single-session fallback is accepted. Before then, deliver a bounded
   plan/reproduction packet in chat or an authorized durable document, naming
   unassigned participants honestly. Do not invent a second agent or resume state.
4. Record real assignments with the state template, distinguishing same-model
   sessions, and establish the branch/workspace safely. Use the requested route
   and hand off once acceptance criteria are actionable; do not repeat planning
   or approval already completed. The Implementer verifies and executes the handoff.

An incomplete, stale, or ambiguous state is a coordination issue to resolve,
not permission to reset files or invent the missing decisions.

## Task routing at a glance

| Task | Starting route |
|---|---|
| Small, obvious, low-risk edit | One agent; no coordination files by default |
| Explicit audit mode | Repository-grounded program → independent reading → evidence verification → durable reports; no fixes |
| Normal feature | Architect framing → Implementer build/test → Architect review → necessary corrections |
| Difficult bug | Implementer reproduction/evidence → Architect challenge → Implementer fix/regression checks |
| Architectural refactor | Independent analyses from neutral evidence → choose direction → implement/review |
| Risky migration or structural change | Invariants/rollback → incremental implementation → architecture review → verification |

Detailed ownership, independence, review, and stopping rules live in the
[workflow reference](references/workflow.md). Risk is not measured by file count:
a one-line billing, authorization, or concurrency change can be material.

## Running a phase

Read the active state before acting. Work only within the current phase and
approved scope. Confirm repository assumptions and preserve existing behavior
outside the objective. Use the selected model's profile to tune context and
validation, not to impose an arbitrary implementation recipe.

Use the findings ledger for actionable issues. Include evidence and severity;
accept, fix, or reject each material finding with a reason. Optional improvements
are not a reason to reopen completed work. Technical disputes should be resolved
with evidence or a small experiment; scope disputes belong to the user.

If capability, context, or quota makes the selected model unsuitable, recommend
a switch with the reason and tradeoff. Preserve the handoff and await approval.
Do not silently substitute another model or treat more quota as more capability.
If an agent runs out of quota mid-phase, preserve its uncommitted work outside the
repository before anyone else writes, and let the user choose who continues.

## Publishing a handoff

Write `.dual-agent/HANDOFF.md` from the template. Include the task/repository
identity, verified evidence, constraints, acceptance criteria, checks actually
run, unresolved risks, and the next decision. State the actual target model;
keep any suggested replacement separate and explicitly advisory.

**Model recommendation for the next phase (required when the handoff starts work).**
Classify the phase with the routing table in [Model selection](references/model-selection.md),
name the recommended available model and effort, explain the capability/resource
tradeoff briefly, and say whether it matches the currently assigned
model or proposes a switch pending approval. A correction cycle, a review, and the
original implementation are different phases and may warrant different models.
Keeping the same model is valid when it remains appropriate; explain the fit.

Recommend a provider-native effort value only when supported by the actual
client. Otherwise use `client-default` or `verify-in-client`; never invent an
API parameter. Include a short rationale rather than a universal maximum.

In audit blind-reading phases, shared state and handoff updates contain neutral
progress only; detailed candidates remain in the reader's separate saved artifact
until both readings are frozen, as specified in the audit reference.

Finish all state, ledger, and handoff updates before changing `turn`. Publish
the turn change last, then stop editing. End the chat reply with the same active
handoff under **DUAL-AGENT HANDOFF**, so the user can carry it to the other session.

For blind independent analysis, the handoff must remain neutral and omit your
proposed solution until both analyses are saved.

## Completion and degraded mode

The following implementation-completion rule applies to implementation work.
Plan-only, diagnosis-only and review-only requests finish at the deliverable in
[Commands](references/commands.md); they do not claim the implementation is done.
Audit mode uses the completion contract in [Audit mode](references/audit.md): distinguish a
finished examination from a repaired system. A plan-only delivery is not a
completed audit, and missing required evidence is never a pass.

Set `stage: done` and `turn: user` when the stopping conditions are met. Summarize
what changed, validation actually performed, and remaining optional limitations.
Blocked required checks or unresolved material risks mean the task is not done.

For audit work, preserve the program, individual readings, verification trail,
and coverage in the agreed durable report location before close-out.
An approved program awaiting more units is still active; never archive its active
coordination away merely because one report or planning session finished.

**Close-out: leave `.dual-agent/` empty of finished work.** When a task is done
(acceptance satisfied or explicitly abandoned; a deploy is not required), and before starting the next one:

1. Preserve useful decisions, sanitized evidence and reusable tools in the agreed
   durable destination. Use versioned project docs when appropriate; sensitive
   evidence may require a private location. In a non-Git workspace, use a durable
   directory and distinguish local preservation from version control.
2. Inventory the folder with the user: what stays (only artifacts of a program still
   active, named explicitly), what moves, what goes. Check nothing in code, tests,
   scripts or config reads the folder.
3. Archive the rest outside the repository (the project's history folder, or ask
   where), verify the archive lists exactly those files, then delete them.
4. Reset STATE to `task: none`, `stage: done` / `turn: user` and HANDOFF to a
   short "no active task" note; record the archive path in Decisions and the project
   handoff notes.

Never delete without the user's review in that session, never delete another
agent's uncommitted work, and never treat the archive as a substitute for evidence
the team needs in the repository.

If only one session is available for substantial work, use the documented
single-agent fallback and disclose reduced independence. A fresh session helps
separate review from authorship; relabeling the same reasoning does not.
