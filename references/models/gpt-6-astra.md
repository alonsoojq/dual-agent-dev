# GPT-6 Astra

Optional handoff note, not a benchmark or a required assignment. Use only when
this model is actually available and selected or considered by the user. Source
IDs refer to [Sources](../sources.md); facts were consulted on 2026-09-29.

## Identity and positioning (Documented)

- OpenAI API ID `gpt-6-astra`: "Our most capable model for the most demanding
  work", for complex reasoning, coding, computer use, research and document
  creation (S4).
- OpenAI's selection guide: "State-of-the-art intelligence", for ambiguous
  problems, deep analysis and ambitious deliverables (S16). Its API guidance
  reports stronger results with substantially fewer output tokens and better
  coherence than GPT-5.6 Sol on long tasks, and notes it is more likely to ask for
  clarification where earlier models assumed (S17).
- Codex lists Astra as its flagship for complex end-to-end work (S7). OpenAI's
  reasoning guide suggests starting with it for most API reasoning workloads (S6);
  that is API guidance, not a rule for every phase of this workflow.

## Consider for (Guidance)

- Unknown root cause across coupled boundaries; competing hypotheses.
- Architecture decisions with migration or compatibility risk.
- Independent audit of a large unit, or a review where a miss is costly.

## Fit less clear when (Guidance)

- A later correction or implementation phase is already designed and bounded.
  Reassess phase fit instead of inheriting an investigation assignment.

## Handoff adaptations (Guidance)

For a deep investigation, carry observed behavior, competing hypotheses, source
boundaries and the evidence that would settle the question. Let repository
evidence revise the plan. State which decisions are already authorized and which
checks suffice, since it is more likely to ask for clarification (S17).

## Resources and latency

- Documented: the highest Codex credit rates and the narrowest estimated
  Plus-plan message range among the GPT-6 models listed (S8).
- Unknown: per-effort allowance consumption (U3).

## Effort by interface

- API: low, medium, high, xhigh, max; the model page states no default; `none` is
  not accepted (S4, S17).
- Codex: up to Max or Ultra depending on plan (S7).

## Unknowns

- No primary evidence of how much lighter configurations lose on a given phase.
  Compare on the actual phase when the difference matters.
