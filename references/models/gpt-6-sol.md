# GPT-6 Sol and GPT-6.1 Sol

Optional handoff note, not a benchmark or a required assignment. Use only when
this model is actually available and selected or considered by the user. Source
IDs refer to [Sources](../sources.md); facts were consulted on 2026-09-29.

Two identities share this note. Record which one is actually configured; do not
carry facts from one to the other.

## Identity and positioning (Documented)

- `gpt-6-sol`: "Built to power complex coding and agentic workflows." Its API page
  points to GPT-6.1 Sol as the newer Sol model (S2).
- `gpt-6.1-sol`: "delivers near-Astra performance at a lower cost for complex
  coding, computer use, and professional work." (S3) Listed among Codex's
  recommended models (S7). OpenAI's selection guide: "Optimized and
  high-performing", for complex tasks where time and cost also matter; at medium
  effort, complex technical work; at extra high effort, polished deliverables and
  decisions from conflicting evidence (S16).

## Consider for (Guidance)

- Implementation that crosses modules or touches authorization, concurrency or
  data contracts, where a designed plan still needs judgment.
- Debugging with a partly understood cause; correction cycles after a review.
- Reviews and verification where the change is substantial but bounded.

## Fit less clear when (Guidance)

- Large volumes of simple, well-specified units, where a lighter configuration
  may meet the same criteria with fewer resources.
- The deepest investigations with no working hypothesis, where evidence may
  justify a more capable model or a narrower unit.

## Handoff adaptations (Guidance)

Carry decisions and reasons, actual entry points, invariants, non-goals and the
acceptance evidence expected. State what is already authorized and which checks
suffice, so the session does not re-ask or over-test.

## Resources and latency

- Documented: Codex credit rates for input and output are the same for both
  identities; cached input differs (S8). Estimated Plus-plan message ranges are
  published per identity (S8).
- Unknown: per-effort allowance consumption (U3).

## Effort by interface

- API, `gpt-6-sol`: none, low, medium (default), high, xhigh, max (S2).
- API, `gpt-6.1-sol`: low, medium (default), high, xhigh, max; no none (S3).
- Codex: GPT-6.1 Sol up to Max or Ultra depending on plan (S7). Check the client
  for GPT-6 Sol.

## Unknowns

- No primary evidence compares either identity at a given effort with GPT-6 Luna
  at a higher effort on the same phase.
