# dual-agent-dev v1.0.0

A repository-aware, resumable software-development skill for two coding agents.
It keeps design, implementation and independent review connected through explicit
ownership and durable handoffs, so work can continue across separate sessions
without relying on a shared conversation.

The **Architect** frames the problem, defines constraints and reviews the result.
The **Implementer** investigates, builds and tests. Both can challenge assumptions.
One session writes at a time. The same model can fill both roles in separate
sessions; a model name alone does not establish independence.

## Why use it?

Use it to understand a repository, design a change, implement an agreed task,
investigate a bug, make a bounded fix, or review another agent's work. Persistent
state makes interrupted work resumable; bounded ownership and explicit handoffs
reduce accidental overlap. Audit mode adds independent repository readings and
an evidence trail, with repairs handled as separate development work.

The usual flow is **frame → implement and test → independent review → correct
material findings → finish**. Difficult bugs begin with reproduction. Plans and
reviews can be requested on their own. Small low-risk work can use one agent;
substantial one-session work must disclose reduced independence.

## Installation

This is a local instruction skill, with no runtime service, API key or automatic
agent launcher. Install the complete `dual-agent-dev/` directory, including
`SKILL.md`, `references/` and `templates/`. Two actual sessions are needed for
independent implementation/review; manual handoffs between terminals are supported.
Python 3.9+ is needed only for the optional package checks.

| Host | Global installation directory | Invoke from your target repository |
|---|---|---|
| Codex CLI / IDE extension | `~/.agents/skills/dual-agent-dev/` | `$dual-agent-dev <task>` or select it with `/skills` |
| Claude Code, local sessions | `~/.claude/skills/dual-agent-dev/` | `/dual-agent-dev <task>` |

These paths and discovery mechanisms follow the official
[Codex skills documentation](https://learn.chatgpt.com/docs/build-skills) and
[Claude Code skills documentation](https://code.claude.com/docs/en/skills), checked
on September 21, 2026. Host installation conventions are verified; a complete
cross-host workflow test is not claimed. Other hosts are not documented as supported.

Download the release ZIP, extract it, then move its `dual-agent-dev` folder into
one of the directories above. For example, from the directory containing the ZIP
in PowerShell, for Codex:

```powershell
$skillParent = Join-Path $HOME '.agents/skills'
New-Item -ItemType Directory -Force -Path $skillParent | Out-Null
Expand-Archive -LiteralPath './dual-agent-dev-1.0.0.zip' -DestinationPath $skillParent
```

For Claude Code, set `$skillParent` to `Join-Path $HOME '.claude/skills'` instead.
On macOS/Linux, extract the same ZIP into `~/.agents/skills/` or `~/.claude/skills/`.
Use a fresh destination for first installation; see Updating for an existing copy.
Restart the host if discovery has not refreshed. Open your **target repository**
before invoking the skill; the installation directory is not the target.

Project-local installation is also possible under `.agents/skills/dual-agent-dev/`
for Codex or `.claude/skills/dual-agent-dev/` for Claude Code. Global installation
is preferable when using one copy across projects. Avoid duplicate installations
with the same name. Claude Code cloud/Cowork sessions do not read the local personal
skill directory; those integrations are outside this package's installation scope.

## Quick start

In Claude Code, start with a concrete outcome:

```text
/dual-agent-dev Add CSV export for the existing filtered results; include tests
```

In Codex, use the same arguments with its skill mention:

```text
$dual-agent-dev Add CSV export for the existing filtered results; include tests
```

The invoking agent checks repository instructions, current task state and relevant
code, then frames the work. If no collaborator is assigned, it can plan first and
asks for the receiving session only when the handoff needs one. You do not need to
pick roles or models before explaining the task. Open the second session in the
same target workspace, provide the published **DUAL-AGENT HANDOFF**, and invoke
`resume` there. The receiver verifies its assignment and turn before working.
Bring the implementation handoff back to the independent reviewer when ready.

For narrower requests:

```text
/dual-agent-dev plan Explain the import pipeline and design duplicate detection
/dual-agent-dev implement the agreed duplicate-detection plan
/dual-agent-dev debug CSV import fails on empty files; diagnose only
/dual-agent-dev debug CSV import fails on empty files; fix it and add a regression test
/dual-agent-dev review the implementation against the agreed import contract
/dual-agent-dev status
/dual-agent-dev resume
```

Replace `/dual-agent-dev` with `$dual-agent-dev` in Codex. These are prompt
instructions, not shell commands. Handoffs coordinate sessions; they do not launch them.

## Commands

The base invocation accepts ordinary task language. With no arguments it resumes
a valid active task; with no active task it asks what you want to do.

| Arguments after the skill name | Result |
|---|---|
| `<task>` | Route by intent and existing state; analysis stays analysis, explicit build/fix intent proceeds when permitted |
| `plan <task>` | Repository understanding, design and acceptance criteria; no implementation |
| `implement <task or plan>` | Use or complete framing, then assigned implementation, tests and independent review |
| `debug <problem>` | Diagnose first; repair only when requested or already authorized |
| `review [scope]` | Independent findings and validation gaps; no silent repairs |
| `resume` | Continue persisted state and handoff; never reconstruct a missing task from guesses |
| `status` | Read-only neutral progress and next action, including audit state |
| `audit [scope]` | Prepare an audit program |
| `audit plan [scope]` | Explicit audit preparation |
| `audit run [unit]` | Execute an identified program within its scope and permissions |
| `audit resume` | Continue the persisted audit phase and coverage |
| `audit status` | Read-only neutral audit progress |

There are no extra aliases. Unrecognized ordinary sentences remain task text;
unknown command-like tokens or unsupported flags get usage guidance without writes.
Use `audit plan <scope>` for a scope beginning with a reserved audit verb.
The [command contract](references/commands.md) defines dispatch and boundaries.
All commands preserve active ownership; none can take over another session's turn.

## Optional configuration

No configuration is required. Keep customization outside the installed skill:

| Content | Location |
|---|---|
| Personal language, model/capability and resource preferences | `$XDG_CONFIG_HOME/dual-agent-dev/preferences.md` when absolute; otherwise `~/.config/dual-agent-dev/preferences.md` |
| Shared project contracts and context | Target root `.dual-agent-context.md` |
| Private project context | External private file, or target root `.dual-agent-context.local.md` with verified local exclusion |
| Active task and handoff | Target root `.dual-agent/` |

The optional configuration contract is `config_version: 1`, independent of the
product version. Start with [preferences](examples/preferences.md) or
[repository context](examples/repository-context.md); see
[configuration](references/configuration.md) for discovery and precedence.
Specific model preferences are welcome but not required. Assignments depend on
available capabilities and real sessions, not a permanent vendor mapping.

## Audit mode

```text
/dual-agent-dev audit plan the public API and its consumers
/dual-agent-dev audit run
/dual-agent-dev audit status
```

Preparation inspects the actual repository and proposes units, contracts, baseline,
coverage and safe verification. `run` can approve that identified program when
assignments and permissions are clear; without a program it plans first.
Two independent readers examine the same scope and save initial conclusions before
seeing each other's findings. Reconnaissance cannot exclude unflagged code.
Agreement is not proof: repository evidence, tests and contracts resolve findings.

Reports separate hypotheses, demonstrated defects, static traces, executed checks
and unknown external configuration. A finished audit may contain **unfixed defects**;
missing essential evidence leaves it partial. Audit never silently repairs code.
Read the [audit protocol](references/audit.md) for the detailed guarantees.

## State and persistence

The target's `.dual-agent/STATE.md` records task, phase and ownership;
`HANDOFF.md` carries the next phase's evidence and acceptance criteria. Resume reads
these files and verifies repository, baseline, session and turn. Status reads only
neutral metadata and progress, without changing state or exposing sealed findings.

Keep runtime coordination out of version control unless the team explicitly wants
it committed. Shared project context and sanitized durable reports can be committed
after review; secrets and private context should not be. This repository's
`.gitignore` protects **this skill checkout only**. The skill never silently edits
a target repository's ignore rules. At close-out, useful evidence is preserved and
scratch work is archived before user-reviewed deletion. Updates do not reset tasks.

## Safety and permissions

Instructions, context and handoffs do not grant deployment, destructive-action or
external-system permissions. The host enforces access; the skill's single-writer
rule is cooperative, not an atomic lock or sandbox. Review checks before execution
and keep sensitive evidence private. See [SECURITY](SECURITY.md).

## Updating

Replace only the installed skill directory with a verified complete release, or
update a local source checkout after reviewing your changes. Keep external user
preferences, target-project context and `.dual-agent/` where they are. No private
edition, patch-after-update process or configuration migration is required.
For local checks, packaging and exact Git-export validation see
[VALIDATION](VALIDATION.md); contributors should read [CONTRIBUTING](CONTRIBUTING.md).
The product version source is `metadata.version` in [SKILL.md](SKILL.md).

## Limitations

LLM review is not formal verification. Runtime and environment-dependent bugs may
need execution; inaccessible external systems remain unknown. Separate sessions
reduce shared blind spots without eliminating them. Markdown cannot prevent a
non-cooperating process from writing or reading peer reports. The package does not
schedule agents or guarantee that every host/model follows the protocol.

Licensed under [MIT](LICENSE).
