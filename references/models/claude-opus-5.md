# Claude Opus 5

Optional handoff note, not a benchmark or a required assignment. Use only when
this model is actually available and selected or considered by the user. Source
IDs refer to [Sources](../sources.md); facts were consulted on 2026-09-29.

## Identity and positioning (Documented)

- Anthropic API ID `claude-opus-5`. Legacy, still available; the provider suggests
  migrating to Claude Opus 5.5 (S12).

## Consider for (Guidance)

- Architecture or review assignments already running on it, where continuity of
  context outweighs a switch.

## Fit less clear when (Guidance)

- Starting a new phase where Claude Opus 5.5 is available; the provider's own
  migration advice applies (S12).

## Handoff adaptations (Guidance)

For architecture or review, carry system constraints, compatibility invariants and
the acceptable change boundary. Review the actual implementation and its context.

## Resources and latency

- Documented: API price per token on S12.
- Unknown: consumption on a given subscription plan.

## Effort by interface

- Claude API: low, medium, high (default), xhigh, max; the provider suggests
  starting at `high` and adjusting by evaluation (S11, S12).
- Claude Code: same levels, default high (S14).

## Unknowns

- Retirement timing beyond the provider's stated commitment; check S12.
