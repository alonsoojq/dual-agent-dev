# Evidence and source maintenance

Repository evidence supports project claims. Primary provider documentation and
actual client options support model/interface claims. Neither supports a universal
cross-model ranking without an appropriate evaluation.

Check time-sensitive model facts when needed:
context sizes, effort enums, prices, retirement dates and account entitlements
change. At the point of a model-dependent decision, inspect the client and consult
the selected provider's official documentation; record the page, date,
interface/version and exact claim supported. If unavailable, say unknown rather
than supplying an inherited value. A claim written in this package, or a URL next
to it, is a pointer to recheck, not a verification.

Separate documented facts, engineering recommendations and local observations.
A local outcome should retain task shape, real model/client/effort, checks and
limitations. Keep personal observations in external user/project context.
Generalize only the rule supported by evidence, not an anecdotal model stereotype.

Package validation is documented in [VALIDATION](../VALIDATION.md). Structural
checks, fixture walkthroughs and live session behavior are different evidence
types. A check of wording does not establish that an agent follows it.

## Evidence labels

Model notes and recommendations use four labels:

- **Documented** — stated by the provider on a page listed below, for the named
  model identity and interface, on the consultation date.
- **Guidance** — an engineering recommendation of this skill. It is conditional
  on the phase and can be overridden by evidence.
- **Local** — an observation or preference of a user or project. It belongs in
  external configuration, never in the public notes.
- **Unverified** — reported elsewhere or plausible, but not confirmed from a
  primary source. Never present it as fact.

## Verified provider pages

Consulted 2026-09-29. Each entry names the identity and interface the page covers.
A page for the API does not describe Codex, ChatGPT or Claude Code behavior unless
it says so, and vice versa.

| ID | Provider · identity · interface | Page | Claims used |
|---|---|---|---|
| S1 | OpenAI · `gpt-6-luna` · API | https://developers.openai.com/api/docs/models/gpt-6-luna | Positioning quote; `reasoning.effort` none, low, medium (default), high, xhigh, max; API price per token |
| S2 | OpenAI · `gpt-6-sol` · API | https://developers.openai.com/api/docs/models/gpt-6-sol | Positioning quote; effort none…max, default medium; page points to GPT-6.1 Sol as the newer Sol model |
| S3 | OpenAI · `gpt-6.1-sol` · API | https://developers.openai.com/api/docs/models/gpt-6.1-sol | Positioning quote; effort low…max (no none), default medium |
| S4 | OpenAI · `gpt-6-astra` · API | https://developers.openai.com/api/docs/models/gpt-6-astra | Positioning quote and use cases; effort low…max; no default stated |
| S5 | OpenAI · `gpt-5.6-sol` · API | https://developers.openai.com/api/docs/models/gpt-5.6-sol | Positioning quote; effort none…max, default medium |
| S6 | OpenAI · reasoning effort · API | https://developers.openai.com/api/docs/guides/reasoning | What each effort value is for; supported values and defaults are model-dependent; lower effort favors speed and fewer tokens |
| S7 | OpenAI · Codex models · Codex | https://learn.chatgpt.com/docs/models | Recommended Codex models (Astra, GPT-6.1 Sol, GPT-6 Luna); effort names; Luna up to Max, not Ultra; Ultra delegates to subagents; higher effort takes longer and uses more tokens |
| S8 | OpenAI · Codex pricing · Codex on ChatGPT plans | https://learn.chatgpt.com/docs/pricing | Estimated local messages per 5 hours per model and plan; credit rates per model; similar tasks can consume different amounts depending on model, context, reasoning, tool use, retrieval and caching |
| S9 | OpenAI · Codex changelog · Codex | https://learn.chatgpt.com/docs/changelog | GPT-6 Sol and Luna added 2026-09-25; GPT-6.1 Sol entry 2026-09-29 |
| S10 | Anthropic · model lineup · Claude API | https://platform.claude.com/docs/en/models/overview | Descriptions, default effort, relative latency and price for Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 4.5; Opus 5 and Opus 4.8 listed as legacy |
| S11 | Anthropic · effort parameter · Claude API | https://platform.claude.com/docs/en/build-with-claude/effort | Levels per model; per-model starting recommendations; effort is a behavioral signal, not a strict budget |
| S12 | Anthropic · `claude-opus-5` · Claude API | https://platform.claude.com/docs/en/models/opus-5/overview | Legacy status; migration suggestion to Opus 5.5; default effort high |
| S13 | Anthropic · `claude-opus-4-8` · Claude API | https://platform.claude.com/docs/en/models/opus-4-8/overview | Legacy status; migration suggestion to Opus 5.5; default effort high |
| S14 | Anthropic · effort in Claude Code · Claude Code | https://code.claude.com/docs/en/model-config | Levels and defaults per model in Claude Code; how to set effort; effort scale calibrated per model; switch models when effort is not enough; `max` may overthink |
| S16 | OpenAI · model selection · ChatGPT and Codex | https://learn.chatgpt.com/docs/model-selection | Roles of Luna, GPT-6.1 Sol and Astra; example tasks per model and effort; treat the guidance as a starting point and test on identical inputs for "the lightest setting that meets your quality bar" |
| S17 | OpenAI · `gpt-6-astra` guidance · API | https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra.md | Stronger results with fewer output tokens; more coherent than GPT-5.6 Sol on long tasks; more likely to ask for clarification; Astra and GPT-6.1 Sol do not accept none |
| S18 | Anthropic · `claude-opus-5-5` · Claude API | https://platform.claude.com/docs/en/models/opus-5-5/overview | Latest status, released 2026-09-22; adaptive thinking always on; default effort medium |
| S15 | Google · `gemini-3.8-flash` · Gemini API | https://ai.google.dev/gemini-api/docs/latest-model | Positioning quote; `thinking_level` low, medium (default), high; `minimal` rejected; more tokens on longer tasks by design |

## Unverified or unresolved on 2026-09-29

| ID | Claim | Status |
|---|---|---|
| U1 | GPT-5.3-Codex-Spark's current availability. Secondary sources report the research preview was retired in September 2026. | The API model page returned 404; the Codex changelog excerpt read did not mention it; S7 does not list it. Verify in the client. |
| U2 | GPT-6 Luna at higher effort matches older Sol-tier results at a fraction of the cost. | Reported by secondary sources citing the launch announcement; the announcement page could not be retrieved. Do not rely on it. |
| U3 | How much a given reasoning effort consumes of a ChatGPT plan allowance. | S8 says reasoning affects consumption but publishes no per-effort multiplier. Unknown. |
| U4 | Fast-mode multiplier. | S8 states 2x the Standard rate for purchased credits and Enterprise pay-as-you-go; other help-center pages may differ and were not retrievable. Check the page for the user's plan. |

When refreshing: re-read the page, update the claim and date, or move it to the
unresolved table. Remove a claim that no longer has a source instead of keeping it
by inertia.
