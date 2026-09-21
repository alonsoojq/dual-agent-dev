# Architecture

## Stable core

The package is an instruction protocol. SKILL loads the command contract; workflow handles
development; audit/reporting handle examination; coordination owns transport;
templates describe artifacts. It does not add a scheduler, shell parser or lock
service. Architect and Implementer are coordination roles, independent of models.

The required STATE fields remain `task`, `branch`, `architect`, `implementer`,
`stage`, `turn`, `cycle`. Stages remain investigation, implementation, review,
correction, done. Turns remain architect, implementer, user. Publish turn last.
Optional audit metadata selects audit; `mode: single-agent` still means degraded
independence. Existing compatible active tasks need no reset.

Consumers are SKILL, coordination, workflow, audit, STATE/HANDOFF templates and
the behavioral scenarios. The package checker parses real example state blocks
and tests vocabulary against these contracts. Markdown remains the operational
format; there is no hidden runtime schema or new execution daemon.

## Public and private boundaries

| Information | Home | Why |
|---|---|---|
| Method, roles, evidence, turn ownership | Public skill | Shared behavior across projects |
| Personal roster, resource priorities, language | External user preferences | Survive skill replacement without a fork |
| Project contracts, commands, architecture | Repository context and existing project docs | Scoped facts that need local evidence |
| Sensitive project context | External private file or locally excluded root context | Does not enter public distribution |
| Explanatory audit reports and decisions | Agreed durable project/private docs | Remain useful after task close-out |
| Session progress, active handoff, scratch probes | Target `.dual-agent/` or isolated scratch | Temporary task coordination |
| Examples | Public examples/tests, explicitly inactive | Illustrate without pretending to describe a live repo |

The [format-1 configuration contract](configuration.md) is intentionally plain
Markdown. There is no executable override, deep merge, plugin registry or model
database. Defaults work without it. Context cannot overrule evidence or grant
permissions. New release versions keep format 1 until a deliberate migration.

## Evidence and independence

Two independent first passes, per-reader coverage, the union of findings,
independent verification and six report responsibilities prevent shared blind spots
from being mistaken for completed review.
Reconnaissance is factual input, never an exclusion authority. Prior conclusions
can leak through state, handoffs, broad diffs, chat history and project context;
neutral input and saved-before-reveal records address these paths procedurally.

A static trace with resolved reachable preconditions can demonstrate a defect.
Runtime behavior, external configuration and hardware behavior require their own
evidence. No detection does not establish safety. Design preferences remain
observations unless a supported contract is violated.

Audit and repair have different completion criteria. The former can report an
unfixed defect; the latter requires disposition of material findings and relevant
validation. An explicit scoped transition preserves the original evidence.
The audit program, not a language/framework checklist, defines the required scope.

## Capability and session identity

Roles describe responsibilities, not permanent provider assignments. Optional model
notes help construct a handoff; external preferences can name concrete models.
A model name does not authenticate a process. Distinct confirmed sessions establish
who authored, who reviewed and who currently owns the cooperative writing turn.

Planning can begin without choosing an unused collaborator. A work-starting handoff
requires an actual receiving assignment. This keeps entry lightweight without
simulating independent work or weakening ownership. Commands select intent; the
same state, role, handoff and review contracts govern every working route.

## Persistence and completion

`metadata.version` in SKILL is the product version source. Configuration format 1
and the STATE vocabulary are separate technical contracts. Unknown optional fields
survive updates, and external preferences are never rewritten by installation.

Close-out preserves useful evidence, checks consumers, verifies an external archive
and requires user review before deletion. Completion does not require deployment.
An audit can finish with unfixed defects; implementation needs disposition of its
material findings. A standalone review reports defects without silently fixing them.

The package adds no worktree, log, cache, scheduler, atomic lock or automatic agent
launcher. Its own ignore rules protect only this skill repository; target-project
exclusions require that project's authorized policy.
