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

## Recommendation at each work-starting handoff

Name the phase, required capabilities, available recommended model, supported effort,
brief resource/capability tradeoff, validation and escalation condition. Keep the
actual approved assignment separate. For a user-only decision, recommendation can
be not applicable. Keep the same model when it fits; reassess when the task changes.

Use optional [configuration](configuration.md) to tailor candidate order and
personal cost/latency/quota priorities. Those are local constraints, not vendor
measurements. With no preferences, use confirmed availability and task evidence;
ask only for a missing participant/model choice. Do not fabricate a universal
"cheapest", "best" or mandatory model menu.

Unknown root cause, coupled state, inadequate context or repeated failed hypotheses
can justify deeper reasoning or a smaller coherent unit. Resize units without
silently reducing approved audit coverage. Missing credentials or a broken test
environment are not necessarily model limitations. Preserve partial work before
reassignment; confirm the former writer stopped.

## Effort and context

Recommend a provider-native value only when the actual client exposes it.
Otherwise use `client-default` or `verify-in-client`. A requested "deep review"
does not imply a particular API parameter. Record actual configured effort
separately from advice. Maximum effort is not mandatory.

API context limits, effective session context, subscription allowances and API
prices are distinct. Verify current facts at the point of use. Estimate total
task work including tools, retries and review; do not invent subscription
consumption from API price or treat token throughput as correctness.

## Optional notes for existing model users

Read only the note for a model selected or seriously considered. These notes retain
useful handoff adaptations without fixing the architecture to a dated catalog.
They deliberately make no current availability, pricing, limit or benchmark claims.

- [GPT-5.6 Sol](models/gpt-5.6-sol.md)
- [GPT-6 Astra](models/gpt-6-astra.md)
- [Claude Opus 5](models/claude-opus-5.md)
- [Claude Opus 4.8](models/claude-opus-4-8.md)
- [Gemini 3.8 Flash](models/gemini-3.8-flash.md)
- [GPT-5.3-Codex-Spark](models/gpt-5.3-codex-spark.md)

The same generic contract applies to unlisted or renamed models. Consult
[Sources](sources.md) before adding factual model claims.
