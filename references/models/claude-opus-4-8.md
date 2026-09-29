# Claude Opus 4.8

Optional handoff note, not a benchmark or a required assignment. Use only when
this model is actually available and selected or considered by the user. Source
IDs refer to [Sources](../sources.md); facts were consulted on 2026-09-29.

## Identity and positioning (Documented)

- Anthropic API ID `claude-opus-4-8`. Legacy, still available; the provider
  suggests migrating to Claude Opus 5.5 (S13).
- Provider-reported behavior (S23): strengths in long-horizon agentic work and
  knowledge work; interprets instructions literally, especially at lower effort;
  spawns fewer subagents by default; better bug-finding than prior models, but
  review prompts that filter by severity lower what it reports.

## Consider for (Guidance)

- Work already running on it, or when a newer Opus is unavailable in the client.

## Fit less clear when (Guidance)

- Tasks relying on recent libraries or APIs: its reliable knowledge cutoff is
  older than the current lineup's (S13). Supply current library documentation.

## Handoff adaptations (Guidance)

Supply the same objective and evidence contract as for other models, plus
relevant library documentation where its knowledge may be stale.

- Put the task, intent and constraints in the first turn rather than across
  several (S23).
- State the scope of an instruction explicitly; it does not generalize one item's
  instruction to others (S23).
- If reasoning looks shallow on a hard item, raise effort rather than prompting
  around it (S23).
- For review, ask for every finding with severity and confidence, and filter
  afterwards (S23).

## Resources and latency

- Documented: API price per token on S13.
- Unknown: consumption on a given subscription plan.

## Effort by interface

- Claude API: low, medium, high (default), xhigh, max; for coding and agentic use
  the provider suggests starting at `xhigh` (S11).
- Claude Code: same levels, default high (S14).

## Unknowns

- Retirement timing beyond the provider's stated commitment; check S13.
