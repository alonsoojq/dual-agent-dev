# Unit audit report template — preserve information, adapt presentation

Produce in the user's language. Use for an independent first pass or a consolidated
report; label which. A first pass cannot contain a peer verification not yet done.
Replace unknowns honestly; remove empty example rows rather than inventing facts.

---

# <Actual unit ID/name> — <independent reading A/B or consolidated audit>

**Baseline/snapshot:** <actual>. **Status:** <partial / ready for peer verification / complete>.
**Evidence:** <read/static/executed/not verified>. **Independence:** <actual status>.
**Author / verifier:** <real identities, or not yet assigned/performed>. **Date:** <actual>.

## Orientation map

| Use case | Responsible file / symbol | Input → output / effect |
|---|---|---|
| <actual journey> | <actual pointer> | <observed behavior> |

## Terms used here

Define relevant domain, contract and state vocabulary with short examples.
No fixed glossary length and no unexplained local abbreviations.

## 1. Identity and scope

Record unit membership, source revision/dirty state, approved readers, dependencies,
known callers and unverified callers, explicit exclusions, prior related reports
and limits. Refer to the exact file inventory if too long to repeat.

## 2. What the unit does and how

Write a readable end-to-end account of the main journey, then meaningful branches:
state transitions, reads/writes, effects, consumers, rejection, failure, retries
and recovery. Explain responsibilities by file/symbol and the consequences of
choices; do not translate every line of syntax. Describe working behavior even
when no defect is found. Note actual guarantee limits where they change behavior.

## 3. Evidence and verification

| Claim / behavior | Path, symbol, lines, baseline | Read/static trace/executed evidence | Result and limits |
|---|---|---|---|
| <specific claim> | <source pointer> | <what actually happened> | <supported / unresolved, why> |

Keep execution commands, environment, input/state, results and unrun checks
traceable. A static trace is not a passing test. Mention pre-existing failures,
side-effect isolation, redaction, and probes kept separate from target code.

## 4. Prior documents and what remains unclear

| Document/section and authority | Claim | Current evidence | Disposition / required decision |
|---|---|---|---|
| <actual source> | <source claim> | <current trace> | <corroborated / partial / historical / pending> |

Name what was not understood. Distinguish absent evidence from false statements;
current contracts from historical descriptions. Do not invent historical reasons
or silently "correct" the original documents under audit-only permissions.

## 5. Findings and disposition

For each real candidate, record:

- ID, originating sessions and related/duplicate IDs.
- Path/symbol/lines and snapshot; violated contract and its source.
- Concrete reachable scenario and why actual guards allow it.
- Actual wrong behavior and practical consequence.
- Evidence, independent verifier and verification state: pending / confirmed /
  refuted / duplicate; static versus executed for confirmed findings.
- Severity/impact separately from certainty; dissent and external unknowns.
- Opposite boundary / analogous-site checks and what the existing tests assert.
- Remediation status and next action; proposal only unless separately authorized.

Separate defects, pending hypotheses, refutations, contract questions, and optional
design/maintainability observations. With no demonstrated defect, state the limited
no-finding outcome. A singleton demonstrated finding is not removed by voting.
In a blind first pass, omit peer findings and mark own claims awaiting verification.

## 6. Coverage and continuity

| Reader/session | File + snapshot | Read ranges / total | Unread ranges or understanding gaps | Related tests/data/docs and checks |
|---|---|---|---|---|
| <actual reader> | <actual file> | <observed reading> | <actual gaps / none> | <actual pointers and state> |

Summarize each required reader separately, then verification coverage. Indexing,
opening or searching a file does not prove integral reading. Report excluded and
non-text inventory items without fake line counts.

**Next action:** <actual file/range, experiment, decision, or unit completion>.
**Overall audit effect:** <partial / unit complete; program status remains separate>.
**Unfixed findings:** <IDs/status, even when the audit report is complete>.

For consolidated output, link both saved first-pass reports and their integrity
identifiers; preserve their original contents and append later supplements.
