# Capability-based model selection

Choose from models actually exposed by the client or confirmed by the user.
There is no mandatory vendor, roster or model generation. An explicit assignment
wins over a recommendation; a new model needs no package edit to participate.

## Phase fit

| Capability needed | Evidence to consider | Handoff and validation |
|---|---|---|
| Reconnaissance | Can inventory actual files, tools, entry points and dependencies | Factual map; no permission to limit later readers' scope |
| Implementation | Can use the repository's language/toolchain and preserve contracts | Designed outcome, invariants, relevant tests and acceptance |
| Deep reasoning | Can resolve unknown behavior across coupled boundaries | Competing hypotheses, source traces and bounded experiments |
| Independent audit | Distinct session, neutral context, enough capability for the full assigned unit | Own explanation, candidates and per-reader coverage before release |
| Verification | Can check reachable preconditions and evaluate test assertions | Static/executed evidence, counter-evidence and remaining unknowns |
| Architecture review | Can evaluate system invariants, compatibility and migration risk | Actual diff/contracts, consequence and rollback checks |

These capabilities can belong to the same model. Independence comes from actual
sessions and read order, not branding. Different providers are optional and may
introduce data-sharing constraints; obtain the required authorization before
transmitting code. If only one session exists, disclose the fallback.

## The unit of recommendation

Recommend a **configuration**: model, effort and interface together (for example
an API, Codex, Claude Code or another client). The same model can expose different
effort values, defaults, tools and billing in different interfaces, and the same
effort name can mean different depth on different models. A recommendation covers
one phase, not the whole task, and stays separate from the approved assignment.

## Reading the phase

Weigh these together; none decides alone.

| Factor | Pushes toward more depth or capability | Allows a lighter configuration |
|---|---|---|
| Scope and clarity | Open-ended goal, design still moving | Decided design, named acceptance checks |
| Ambiguity | Unknown root cause, conflicting evidence | Reproduced symptom with known cause |
| Coupling | State or contracts shared across components | Change confined to one module |
| Risk | Security, authorization, money, data loss, irreversible steps | Reversible, well-tested surface |
| Context | Must hold many files or long history at once | Focused handoff fits comfortably |
| Volume | One hard decision | Many similar units with the same shape |
| Interface | Needed tools only in a specific client | Tools available wherever it runs |
| Constraints | — | User-stated cost, latency or quota priority |

Constraints come from the user or their configuration. Do not infer them.

## Choosing the move

Before recommending, pick the move that addresses the phase:

- **Keep** the configuration when the previous phase met its criteria and the
  next phase has a similar shape.
- **Adjust effort** when the model covered the unit but reasoned shallowly or,
  conversely, spent far more than the phase needed.
- **Improve context** when failures trace to missing contracts, files or
  decisions. More effort or a bigger model does not supply missing facts.
- **Split** into coherent units when the work exceeds what one session can hold
  or when independent parts can be verified separately. Never shrink approved
  audit coverage to make a unit fit.
- **Propose another model** when evidence points to a capability gap that effort
  and context did not close, or when a lighter model is likely to meet the same
  acceptance criteria with fewer total resources.

There is no standing rule such as "always maximum effort", "smallest model
first" or "top model for anything important". Each is sometimes right; justify it
by the phase.

### Effort or model

Effort buys more deliberation, tool use and verification within one model's
capability; it does not add knowledge or skills the model lacks. Effort scales
are calibrated per model, so the same level name does not represent the same
depth across models (Documented for Claude Code, S14; do not assume otherwise for
other providers without evidence). One provider advises switching models when
effort is not enough (S14).

A lighter model at a high effort can be a real alternative to a heavier model at
a moderate effort for well-specified work; one provider's own selection guide pairs
its lightest model at a high effort with constrained problems and advises testing
on identical inputs for the lightest setting that meets the quality bar (S16). It
can also lose: more tokens per
attempt, more retries, more review findings to correct. Decide with evidence:
run both on a representative bounded unit with identical acceptance criteria,
and compare first-pass acceptance, corrections needed and resources actually
consumed. Record the outcome as a local observation, not as a package fact.

**Worked comparison — GPT-6 Luna at `max` versus GPT-6 Sol at `high` in Codex.**
What is documented (S1, S2, S7, S8, S16): both identities accept both values; Codex
lists Luna up to Max; Codex credit rates per token for Luna are much lower than
for GPT-6 Sol; the Plus plan's estimated message ranges are far wider for Luna.
What is not documented: how many tokens either uses on a given task at those
efforts, how often each needs a retry, or any per-effort allowance multiplier
(U3). A per-token rate ratio is therefore not a per-task cost ratio, and neither
is a quality claim. Guidance: for a bounded, well-specified phase under a stated
quota priority, Luna at a high effort is a reasonable candidate to try; for
unknown-cause debugging, a costly-to-miss review or a design decision, prefer the
configuration with better evidence for that phase shape, and reassess with the
signals below. No winner is assumed.

## Effort: depth versus accepted values

Think in conceptual depth first — light, standard, deep, maximum — then map it to
a value the actual model and interface accept. Documented examples, consulted
2026-09-29:

| Interface | Values | Source |
|---|---|---|
| OpenAI API | model-dependent subset of none, low, medium, high, xhigh, max | S1–S6 |
| Codex | low, medium, high, xhigh (Extra High), max; Ultra delegates to subagents and is plan-dependent; Luna stops at Max | S7 |
| Claude API | low, medium, high, xhigh, max; defaults differ per model | S11 |
| Claude Code | same names; per-model defaults; `/effort`, `--effort`, settings | S14 |
| Gemini API (3.8 Flash) | `thinking_level` low, medium, high; no max | S15 |

- Do not translate labels across providers, models or clients. An API parameter
  is not a Codex or Claude Code setting, and vice versa.
- Several providers state that higher effort takes longer and uses more tokens
  (S6, S7, S11); one warns `max` may overthink and should be tested before broad
  use (S14). Maximum is never the default recommendation.
- When the client's options are unknown, write `verify-in-client` or
  `client-default`. Never invent a value.
- Record the recommended effort separately from the effort actually configured
  (STATE's optional effort field holds the configured one).

## Resources and efficiency

Keep these distinct: API price per token; subscription allowance or credits;
rate limits; latency; and the total resources to finish the phase, which include
tokens across attempts, tool calls, retries, corrections and review.

- Never derive subscription consumption from API prices. Use the plan's own
  documentation, and say unknown where it is silent (S8, U3).
- Provider words such as "efficient" or "affordable" describe positioning, not a
  guaranteed saving on a given account or task.
- Under a quota priority, prefer the configuration most likely to finish the
  phase with the fewest total resources, counting likely retries, not merely the
  lowest rate per token.
- Build no cost estimator or benchmark suite for a recommendation. A brief,
  honest tradeoff is enough.

## Reassessment signals

Signals that the configuration may not fit:

- the same question produces repeatedly failing hypotheses;
- stated invariants are lost or violated between turns;
- the session cannot cover its assigned unit (skipped or truncated reading);
- reasoning is shallow on items the handoff marked as hard;
- review repeatedly finds classes of defect the phase was meant to prevent.

Not configuration signals: missing permissions, a broken environment, tool or
network outages, missing credentials, flaky tests or incomplete requirements.
Fix or escalate those first; switching models will not help. A provider safeguard
declining a legitimate task is a routing fact, not a capability signal: record it
and reassign with the user's approval; never reword the request to evade it.

On a real signal, choose the cheapest move from the list above that addresses the
observed cause. Preserve partial work before any reassignment and confirm the
former writer stopped.

## In the handoff

Keep it short: the configuration (model · effort · interface), one line on why it
fits this phase, and one observable condition to reconsider. Keep the actual
approved assignment separate; for a user-only decision, write not applicable.
Use optional [configuration](configuration.md) to apply personal cost, latency or
quota priorities; they are local constraints, not vendor measurements. With no
preferences, use confirmed availability and task evidence, and ask only for a
missing participant or model choice.

API context limits, effective session context, subscription allowances and prices
are distinct. Verify current facts at the point of use, following the
[evidence rules](sources.md).

## Optional model notes

Read only the note for a model selected or seriously considered. Notes share one
structure so they can be compared: documented identity and positioning; phases
to consider it for; where its fit is less clear; handoff adaptations; resources
and latency; effort by interface; unknowns. A section is left short rather than
filled with a plausible guess. Guidance that applies to every model lives here,
not in the notes.

- [GPT-6 Astra](models/gpt-6-astra.md)
- [GPT-6 Sol and GPT-6.1 Sol](models/gpt-6-sol.md)
- [GPT-6 Luna](models/gpt-6-luna.md)
- [GPT-5.6 Sol](models/gpt-5.6-sol.md)
- [Claude Opus 5.5](models/claude-opus-5-5.md)
- [Claude Opus 5](models/claude-opus-5.md)
- [Claude Opus 4.8](models/claude-opus-4-8.md)
- [Gemini 3.8 Flash](models/gemini-3.8-flash.md)
- [GPT-5.3-Codex-Spark](models/gpt-5.3-codex-spark.md)

The same generic contract applies to unlisted or renamed models. Consult
[Sources](sources.md) before adding factual model claims.
