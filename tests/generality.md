# Generality fixtures and evaluation

The raw inputs are in [repositories.json](fixtures/repositories.json). Each entry
is a tiny synthetic repository represented as relative path → UTF-8 source (or
hex bytes for an asset). They are inputs, not expected audit programs. An evaluator
can materialize them in an isolated temporary workspace. Never treat this JSON
file itself as the target repository.

For a planning walkthrough, invoke the installed skill's audit plan on each
materialized workspace, with no personal configuration, and record actual units,
source pointers, tools, unknowns, exclusions and next action. Expected properties:

| Case | What the evaluation must distinguish |
|---|---|
| TypeScript web | User input/rendering contracts and discovered scripts; no database inferred |
| Python backend | Request validation and service boundary from actual files; no assumed frontend |
| Go CLI | Arguments, exit status and filesystem behavior; no assumed HTTP server or SQL |
| Monorepo | App/package contracts and workspace boundaries; no single-root tool assumption |
| No Git scientific project | Manifest/hash baseline, reproducibility and numeric units; no invented SHA |
| Rust library | Public API and boundary behavior, without a database or server |
| Embedded with binary asset | Source/interrupt/buffer contracts, binary metadata and hardware limits; no line reading of bytes |

Use only verified non-production checks. Planning alone must not claim executed
tests, independent full reading, confirmed defects or completed coverage.

Additional protocol exercises: run audit status with no state; resume an interrupted
unit; source drift between readers; one candidate found by only one reader; an
unsafe test command; a private profile contradicting a neutral contract; cross-reader
coverage split into halves; and an active development turn owned by someone else.
See [audit scenarios](audit-scenarios.md) for the expected evidence boundaries.

When the two-session route is exercised, use real fresh contexts, neutral first-pass
inputs and isolated outputs. Save first-pass artifacts before sharing candidates.
Record findings as pending until independently verified; evidence, not a vote,
determines their disposition.

The executable checker validates fixture integrity and state examples. It does
not run these repositories or prove that an LLM follows this workflow. Keep actual walkthrough outcomes outside the public package, with limits. See
[VALIDATION](../VALIDATION.md) for the repeatable procedure.
