# Command acceptance scenarios

These are documentary decision cases for the Markdown instruction contract.
They are not a simulated command interpreter. Walk each case against
[Commands](../references/commands.md) and the linked workflow; record actual host
executions separately. The package check guards command/documentation consistency
and the presence of key constraints; it cannot prove an agent obeys them.

Use synthetic repositories and disposable state. For status and failed resume,
compare file hashes before and after a live execution, and inspect tool traces for
forbidden HANDOFF/ledger reads. For working routes verify actual role identity,
turn and handoff ordering, not just the final prose.

| Case | Input and setup | Required route / result | Allowed mutations |
|---|---|---|---|
| C01 | Bare invocation; no state or objective | Ask for objective; no invented task | None |
| C02 | Bare invocation; valid development state and matching Implementer turn | Resume the actual handoff/phase | Current phase only |
| C03 | Bare invocation; active audit reading | Audit resume with baseline and own coverage | Audit artifacts on owned turn |
| C04 | `Explain the module and propose a design`; no pairing | Bounded Architect understanding/plan; defer unused participant selection | Authorized design document only |
| C05 | `Add CSV export with tests`; substantive new task | Architect framing, Implementer build/test, independent review | Only after real assignment and owned turn |
| C06 | `plan Add CSV export` | Actionable design and criteria; stop before implementation | Authorized design/coordination only |
| C07 | `implement the agreed plan`; valid Implementer assignment and handoff | Verify assumptions, build/test; no redundant planning gate | Scoped implementation on owned turn |
| C08 | `implement`; another session owns the task | Report ownership; no reassignment from command name | None |
| C09 | `debug empty-file failure` | Diagnose/reproduce; report evidence and limits | Authorized probes/coordination, no repair |
| C10 | `debug empty-file failure and fix it`; matching turn | Evidence, Architect challenge, bounded repair and checks/review | Authorized fix phase only |
| C11 | `review`; current session authored the change | Fresh reviewer handoff or explicitly labelled self-review | Owned review handoff only; no fixes |
| C12 | `review src/import.py`; distinct reviewer | Actual diff/contracts and supported findings; open defects allowed in review delivery | Owned findings/coordination only |
| C13 | `resume`; no STATE or HANDOFF, chat remembers a plan | Report missing persisted task; do not reconstruct | None |
| C14 | `resume`; branch mismatch or interrupted inconsistent handoff | Preserve artifacts; reconcile before work | None until reconciled |
| C15 | `status`; another owner, ledger and HANDOFF contain sealed conclusions | Read metadata only; no findings and no claim process is running | None |
| C16 | `status`; no state, one persisted unpaired audit program | Neutral planned status with no audit coverage claimed | None |
| C17 | `audit the public API` | Repository-grounded preparation; equivalent to `audit plan` | Owned new audit program only |
| C18 | `audit run`; identified program, assignments and permissions clear | Audit execution without redundant approval; no repairs | Audit artifacts and authorized isolated probes |
| C19 | `audit run`; no program | Prepare program first; do not start full audit | Owned new audit program only |
| C20 | `audit --fix` or `--force` | Explain unsupported flag; no permission escalation | None |
| C21 | `implement export of audit logs` or a quoted filename containing audit | Development intent, not an audit campaign | Only authorized development phase |
| C22 | `statuz` or `status now` | Usage/clarification, no guessed command | None |
| C23 | `resume`; `turn: user` without a next-owner decision | Report pending decision; do not take the turn | None |
| C24 | `resume`; `task: none` or completed task | Report no active work/complete; no reopen | None |
| C25 | `implement fixes`; active audit state | Require explicitly scoped transition; preserve audit baseline/evidence | None until transition authorized and owned |
| C26 | `audit status`; multiple unpaired programs | Neutral ambiguity; do not bulk-read findings | None |
| C27 | `audit plan run scheduling` | Plan the scope named run scheduling, not execution | Owned new program only |
| C28 | `resume`; required fields valid and unknown optional metadata present | Preserve optional fields and actual assignments | Current owned phase only |

For every working case, also test wrong-turn denial and an existing unrelated
objective. No command bypasses STATE, trusted instructions, user authorization,
actual session identity or publish-turn-last. No command launches a second agent.
