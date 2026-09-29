# Claude Opus 4.8

Optional handoff note, not a benchmark or a required assignment. Use only when
this model is actually available and selected or considered by the user. Source
IDs refer to [Sources](../sources.md); facts were consulted on 2026-09-29.

## Identity and positioning (Documented)

- Anthropic API ID `claude-opus-4-8`. Legacy, still available; the provider
  suggests migrating to Claude Opus 5.5 (S13).

## Consider for (Guidance)

- Work already running on it, or when a newer Opus is unavailable in the client.

## Fit less clear when (Guidance)

- Tasks relying on recent libraries or APIs: its reliable knowledge cutoff is
  older than the current lineup's (S13). Supply current library documentation.

## Handoff adaptations (Guidance)

Supply the same objective and evidence contract as for other models, plus
relevant library documentation where its knowledge may be stale.

## Resources and latency

- Documented: API price per token on S13.
- Unknown: consumption on a given subscription plan.

## Effort by interface

- Claude API: low, medium, high (default), xhigh, max; for coding and agentic use
  the provider suggests starting at `xhigh` (S11).
- Claude Code: same levels, default high (S14).

## Unknowns

- Retirement timing beyond the provider's stated commitment; check S13.
