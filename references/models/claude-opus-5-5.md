# Claude Opus 5.5

Optional handoff note, not a benchmark or a required assignment. Use only when
this model is actually available and selected or considered by the user. Source
IDs refer to [Sources](../sources.md); facts were consulted on 2026-09-29.

## Identity and positioning (Documented)

- Anthropic API ID `claude-opus-5-5`: "For long-running agentic coding and knowledge
  work." Anthropic suggests starting with it for most workloads, and Claude Fable
  5.1 when evaluations at higher Opus 5.5 effort still fall short (S10). Latest
  Opus model, released 2026-09-22 (S18).
- Adaptive thinking is always on; effort is the main control of reasoning depth
  and cost (S11).

## Consider for (Guidance)

- Architecture framing, design consolidation and independent review, where
  system invariants and compatibility matter more than speed.
- Long agentic implementation sessions that must hold many contracts at once.

## Fit less clear when (Guidance)

- High-volume, well-specified units where a faster configuration meets the same
  criteria.
- Problems where its evaluations at higher effort still fall short; the provider
  points to Fable 5.1 for that case (S10).

## Handoff adaptations (Guidance)

For architecture or review, carry system constraints, compatibility invariants and
the acceptable change boundary, and let it review the actual implementation in
context. Exact signatures are needed only when a real contract requires them.

## Resources and latency

- Documented: moderate latency relative to the current Claude lineup; API price per
  token on S10.
- Unknown: consumption on a given subscription plan.

## Effort by interface

- Claude API: low, medium (default), high, xhigh, max. Do not carry settings over
  from an earlier model; the default is one level lower than Opus 5's (S11).
- Claude Code: same levels, default medium; the provider states its default
  matches or exceeds Opus 5 at `high` on its evaluations, and `max` may overthink
  (S14).

## Unknowns

- Relative performance against other providers' models on a given phase.
