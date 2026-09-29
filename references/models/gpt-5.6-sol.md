# GPT-5.6 Sol

Optional handoff note, not a benchmark or a required assignment. Use only when
this model is actually available and selected or considered by the user. Source
IDs refer to [Sources](../sources.md); facts were consulted on 2026-09-29.

## Identity and positioning (Documented)

- OpenAI API ID `gpt-5.6-sol`: "GPT-5.6 flagship model for complex professional
  work." (S5)
- Not among the recommended models on Codex's model page (S7); it may still appear
  in a client's picker.

## Consider for (Guidance)

- Implementing a designed slice, corrections and regressions, especially when the
  session already holds the relevant context and has been meeting its criteria.

## Fit less clear when (Guidance)

- Choosing it because it is older and assumed cheaper. On Codex credit rates it
  costs more per token than GPT-6 Sol, GPT-6.1 Sol and GPT-6 Luna (S8). Weigh a
  newer model for the phase unless local evidence favors this one.

## Handoff adaptations (Guidance)

Carry the decisions and their reasons, actual entry points, invariants, non-goals
and acceptance evidence. Ask it to verify the mechanisms the design assumes and to
report conflicts before building on them.

## Resources and latency

- Documented: Codex credit rates (S8). The Plus-plan message estimates on S8 do
  not list this model.
- Unknown: per-effort allowance consumption (U3).

## Effort by interface

- API: none, low, medium (default), high, xhigh, max (S5).
- Codex: verify in the client.

## Unknowns

- Current Codex plan coverage; check the client and the plan's own documentation.
