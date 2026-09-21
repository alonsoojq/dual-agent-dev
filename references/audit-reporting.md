# Audit reporting and evidence contract

The deliverable has two equal responsibilities: explain the system and distinguish
what was established from what remains unknown. A pile of defect tickets does
not satisfy an integral reading. A fully read unit with no identified defects
still gets a report. Use clear prose in the user's language unless requested
otherwise; paths, symbols and protocol vocabulary stay exact.

## Durable product

Follow the repository's documentation and confidentiality conventions. Suggested
layout when none exists: a directory under `docs/audits/<audit-id>/` with PROGRAM, an index, unit
reports, individual first-pass readings, coverage, and a findings/verification
trail. These are information responsibilities, not a demand to create a dozen
empty files: combine small ledgers or split large ones when it improves use.
Keep first-pass results isolated until both are saved; publish them durably after
release. `.dual-agent/` remains temporary coordination, not the only audit record.
Use version control for shareable reports where available. Private findings may
need a separately agreed durable location; do not publish sensitive evidence by
default. In non-Git workspaces, use durable files with snapshot identities and
state that they are not committed. Check ignore/tracking status where applicable
and distinguish "written" from "committed".

## Program

Use the AUDIT-PROGRAM template after reconnaissance. Fill its inventory, units,
contracts, proposed order, verification environment and acceptance criteria with
repository-derived evidence. The template is not a completed audit plan. Populate it from the actual target
and never present example content as inspected repository evidence.

Freeze an approved program revision for a reading round. Keep a neutral body for
first-pass readers. Any suspicions collected while preparing it belong in sealed
notes, not a "high-risk functions" handoff that biases subsequent discovery.

## Unit report

Start with one line saying baseline, report status, independence and what was
verified statically, executed, or not verified. Then give a one-screen orientation
map (use case → responsible file/symbol → inputs/outputs) and a small glossary of
terms actually used, including states and contract terms with examples.
Do not invent eight terms just to fill a quota.

Preserve these six information responsibilities:

1. **Identity and scope:** revision/snapshot, date, real author and verifier,
   included files, dependencies, exclusions and remaining work.
2. **What it does and how:** coherent main-path narrative, alternatives and
   significant branches, inputs/outputs, state, reads/writes, callers/consumers,
   external effects, rejection, failure, retry and recovery. Explain consequences,
   not a line-by-line translation of syntax. Where the caller is not yet read,
   distinguish the known reference from the unverified end-to-end claim.
3. **Evidence:** path, symbol, line range and baseline; static reasoning versus
   actual execution; concrete commands/results/environment and limitations.
   Describe correct behavior and guarantees as carefully as faults. Keep routine
   caveats here rather than interrupting every sentence of the behavior narrative;
   a limit that changes the actual guarantee also belongs in the description.
4. **Documents, uncertainty, understanding:** prior claims corroborated or
   contradicted, authority/age, gaps, and explicitly what was not understood.
   Assert historical reasons for design only with a historical source.
5. **Findings and disposition:** verified defects, pending hypotheses, refutations
   and duplicates as distinct classes; maintainability/design observations and
   contract decisions separately. Include true no-finding outcomes with scope.
6. **Coverage and continuity:** per-reader files and ranges read/unread, tests and
   data/query files where present, documentary claims compared, checks done/unrun
   and next action.

Use the AUDIT-UNIT template flexibly while retaining these information duties.
Headings can adapt to the system; don't force a stack, module taxonomy, table
schema, API shape or target implementation from this skill.

## Candidate and verified-defect record

Give each candidate a stable ID, origins and affected baseline. Record:

- **Location and rule:** file, symbol, lines, snapshot; the behavior expected and
  the actual source of the current contract/invariant.
- **Reachable scenario:** concrete inputs, state or event interleaving; how real
  guards, authorization, transactions and constraints permit it. A test-only
  helper that creates an unreachable state does not establish reachability.
- **Actual behavior and consequence:** what goes wrong and who/data/operation is
  affected. State a demonstrated behavior precisely, not as speculative rhetoric.
- **Verification:** executed reproduction, or a labelled static trace through
  code and applicable constraints with resolved preconditions; named independent verifier and
  evidence. A proposed test is a verification plan, not an executed test result.
- **Classification and next action:** status, severity, certainty/evidence basis,
  pending external facts, proposed correction/verification, remediation status.

Candidate states: `pending`, `confirmed`, `refuted`, `duplicate`. `confirmed`
requires resolved preconditions and independent verification under this program.
An author may label its first-pass record "demonstrated by author, not yet
independently verified"; never imply the peer's check already happened.

In an approved single-session fallback, preserve the label "demonstrated by author,
not independently verified" rather than fabricating a verifier or silently relaxing
`confirmed`. Completion may follow the explicitly amended independence criterion;
the report must continue to disclose the absent independent verification.

A `confirmed` item identifies evidence as `static` or `executed` (both if actually
present). `refuted` includes the counter-evidence; lack of environment/access
keeps it `pending`, not refuted. Duplicates retain their origin IDs and canonical
ID. Read-order contamination is an independence attribute, not defect severity.

Keep severity separate from confidence and from repair status. Reuse a documented
project severity scale; otherwise describe impact explicitly (money/data/access,
customer promise/functional correctness, or non-defect observation) before proposing
priority. No automatic severity derived from model certainty or number of votes.
Don't promote style, naming, missing tests alone, architecture preferences, or
harmless duplication to demonstrated defects. A contract ambiguity is a question.
A test/comment that falsely claims a concrete behavior can be an evidenced weakness,
but report the actual false assurance rather than equating all test gaps with bugs.

For comparisons/thresholds/ordering/repeated logic, inspect the opposite boundary
and analogous sites. List exactly which analogues were checked, not "all" after
one search. Judge tests by what their assertions prove, not their names.

The development STATE ledger keeps its existing states. After blind release, mirror
confirmed-but-unfixed and pending items as `open`, with their richer status and
report pointer; map refutations to `rejected` with evidence and duplicates to a
linked disposition. Use `resolved` only with a stated non-misleading reason; never
make "confirmed" mean "fixed". Do not put candidates in the shared ledger early.

## Documentation reconciliation

Classify each document as current normative contract, proposed design, implementation
description, or historical audit. Until checked against the baseline, call it
unverified, not false. Track document/section → claim → evidence → disposition.

Preserve correct parts of mixed documents. Mark obsolete architecture historically
in the new report and propose scoped updates; audit-only does not rewrite originals.
A current contract violated by code is not "outdated documentation" merely because
the code differs. Do not edit the contract to make the defect disappear.
For historical findings use: persists with evidence; repaired with evidence;
superseded by demonstrated system change; or unresolved. "Closed" in an old report
is not proof of repair. Link old and new IDs rather than inflating counts.

## Coverage and limitations

Track inventory membership independently from reading and verification. For each
reader: file/snapshot, assigned unit, total relevant ranges, ranges actually read,
ranges pending, understanding gaps, linked tests/data/docs and verification state.
Do not infer reading from a tool open, truncated output, search result, code graph,
large context window or self-reported percentage. Small complete files may use
"whole file at <hash>" after actual complete reading; large files need ranges.

Never merge A's 50% and B's other 50% into "two independent 100% reviews".
A secondary targeted review can be useful but must be labelled as such. Report
owned excluded files, inaccessible surfaces, non-text inspection methods, runtime
checks missing, external configuration limits and baseline drift explicitly.
Use case and absence checks supplement code reading: determine what should happen
for relevant unsupported input/failure journeys rather than assuming missing code
will reveal itself to a line scan. Source intended expectations or mark questions.

A completed report does not assert production safety, zero vulnerabilities, or
complete runtime verification. A partial report with exact remaining evidence
is preferable to inventing coverage or silently compressing an integral request.
