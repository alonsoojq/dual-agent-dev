# GPT-6 Luna

Optional handoff note, not a benchmark or a required assignment. Use only when
this model is actually available and selected or considered by the user. Source
IDs refer to [Sources](../sources.md); facts were consulted on 2026-09-29.

## Identity and positioning (Documented)

- OpenAI API ID `gpt-6-luna`. Provider description: "Our most efficient model for
  focused, high-volume tasks." (S1)
- Listed among Codex's recommended models (S7); added to Codex on 2026-09-25 (S9).
- OpenAI's selection guide: "Smart and efficient", for scoped tasks, triage and
  frequent automations; at low effort, fine-grained edits and simple extraction;
  at extra high effort, finding context across apps and solving constrained
  problems (S16).

## Consider for (Guidance)

- Designed implementation and correction cycles with explicit decisions,
  invariants and acceptance checks.
- Repetitive work across many units of the same shape, where a lighter
  configuration that holds quality saves the most.
- Factual reconnaissance whose output another phase verifies.

## Fit less clear when (Guidance)

- The root cause is unknown and spans coupled components.
- A miss is expensive and the phase is the last line of defense: security or
  authorization review, irreversible migrations, architecture decisions.

This is not a statement that it cannot do these; no primary evidence covers them.
Pilot it on a bounded unit, or pair it with a stronger independent review.

## Handoff adaptations (Guidance)

State decisions with their reasons, the invariants, non-goals and acceptance
checks. Name the entry points found so far without prescribing the code. Ask it to
report design conflicts rather than resolve them silently. For repeated units,
keep one evidence and report schema so results consolidate without guessing what
was examined.

## Resources and latency

- Documented: the lowest Codex credit rates among the GPT-6 models listed, and the
  widest estimated Plus-plan message range (S8). Higher effort takes longer and
  uses more tokens (S7).
- Unknown: per-effort allowance consumption (U3); whether it finishes a given
  phase at `max` with fewer total resources than a Sol model at `high`. See the
  worked comparison in [model selection](../model-selection.md#effort-or-model).

## Effort by interface

- API: none, low, medium (default), high, xhigh, max (S1).
- Codex: up to Max; Ultra is not offered for Luna (S7).
- Guidance: start at the level the phase difficulty suggests; raise it on the
  reassessment signals; treat `max` as a choice to justify, not a default.

## Unknowns

- U2: secondary sources claim Luna at higher effort matches older Sol-tier results
  at a fraction of the cost. Unverified; do not rely on it.
