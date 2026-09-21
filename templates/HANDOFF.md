# HANDOFF template

Write the active handoff to `.dual-agent/HANDOFF.md`, then show the same content
in chat under **DUAL-AGENT HANDOFF**. Adapt the detail to task risk; write `none`
or `unknown` rather than inventing evidence. Keep objectives and constraints
specific while leaving room for the recipient's technical judgment.

```text
Current stage:
Source role: <architect | implementer>
Source model:
Target role: <architect | implementer | user>
Target model: <actual approved assignment, not an unapproved recommendation>
Task:
Repository state: <branch/revision and relevant uncommitted changes>
Objective:
Phase shape: <e.g. designed implementation | correction cycle | audit/investigation | review>
Recommended model for this phase: <available model matching required capabilities> — <why this tier fits the phase>
Capability/resource tradeoff: <brief reason; include known user constraints>
Recommended reasoning effort: <supported native value | client-default | verify-in-client>
Assignment vs recommendation: <matches assigned model | switch proposed, pending user approval>
Repository evidence: <observations and pointers; distinguish hypotheses>
Constraints:
Invariants:
Acceptance criteria:
Changes already made:
Tests/evidence already collected: <commands/checks, actual results, and what was not run>
Risks:
Open questions:
What the next agent should determine:
```

The model recommendation is required whenever the handoff starts work for another
agent (implementation, correction, investigation, review). Use the per-phase table
in `references/model-selection.md`. Keeping the previous model is valid when the phase still warrants it. For handoffs to the user that only ask for a
decision, write `Recommended model for this phase: not applicable`.

Known paths, symbols, and commands are useful evidence, not mandatory invented
fields. For test changes, identify the approved requirement that changed.
For a proposed model switch, state that approval is pending and preserve the
existing assignment until it is granted. When escalating or closing with
`Target role: user`, use `Target model: not applicable`.

For audit phases, also carry the actual program path/revision, unit, source
snapshot, scope and permission boundary, source/target session identity when known,
per-reader coverage pointer, next unread range or experiment, and `fixes authorized:
no`. First-pass work-starting handoffs carry only neutral evidence: do not include
scout suspicions, another reader's verdicts, or raw finding logs before both
readings are saved. Point to the recipient's own artifact and the neutral packet,
not to a bulk directory read. For verification after release, link both saved
reports and all candidate origins. A source session's private notes are not
automatically copied into the chat handoff. Recommend models as usual; do not
claim an unlaunched or unavailable participant has run.

In an independent-analysis round, provide neutral facts and questions only.
Do not include a hypothesis or solution that contaminates the recipient's first
analysis. Keep detailed logs in referenced files rather than inlining everything.
