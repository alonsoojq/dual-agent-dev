# Optional configuration (format 1)

The public skill works with no configuration. Configuration is Markdown read by
the host agent, not executable code, a shell include, or an automatic model router.
Use small documents with `config_version: 1` as the first line.

## Discover and apply

1. Find the target repository/workspace root from the user and actual filesystem.
   Read applicable trusted project instructions through the host's normal rules.
   Do not assume the skill installation directory is the target.
2. For user preferences, read `$XDG_CONFIG_HOME/dual-agent-dev/preferences.md`
   if XDG_CONFIG_HOME is an absolute path; otherwise use
   `~/.config/dual-agent-dev/preferences.md`. Here `~` is the current user's
   home directory (also on Windows). A user may explicitly supply another file.
   Do not search unrelated home directories or create defaults just to initialize.
3. At the target root, optionally read `.dual-agent-context.md` (shareable project
   context) and `.dual-agent-context.local.md` (private project context). No
   recursive profile search, inheritance engine or required folder taxonomy.
4. Follow explicit context links only when relevant to this task. Resolve relative
   links against the containing configuration file. Preserve scope conditions on
   user-level project links; confirm repository identity before applying them.
   Read contracts, not verdict-bearing historical reports, before a blind pass.
5. Record which sources influenced the task, without copying personal content into
   public reports. Missing optional files are normal. If a present file cannot be
   read, disclose the unavailable context and proceed only where it is immaterial.

User preferences can name a model roster, capability-to-model preferences, language,
resource priorities and archive destination. Project context can identify components,
contract documents, verified test commands, external dependencies, report conventions
and safety boundaries. Facts need repository pointers and must be rechecked where
they affect correctness; a listed command is not execution permission.

For advisory preferences, precedence is explicit current user instruction, private
project context, shared project context, user preferences, then skill defaults.
This does not override host instruction priority or authoritative repository
contracts. A personal preference cannot silently invalidate a team contract.
Resolve material conflicts with evidence or the user. Active STATE assignments
remain in force until an authorized transfer; a configuration change is not a
model switch or permission to take the turn.

Read known format-1 fields/prose; preserve unknown content when editing. For an
unsupported future config version, report it and use compatible public defaults
for independent work; resolve any decision that depends on the unread semantics.
Never silently migrate or overwrite private configuration during a skill update.

## Privacy and persistence

Prefer external user configuration for personal material: it is outside the skill
checkout and survives replacing or updating that checkout. A project can use its
normal private documentation instead of duplicating domain context into a profile.
The skill only needs pointers. Never store credentials in any of these documents.

The shared project file is intended for version control after content review.
Before creating the local variant, check that its exact path is not already tracked.
For Git repositories, add the exact root rule `/.dual-agent-context.local.md` to
the repository's existing ignore policy or local Git exclude file when authorized,
and verify with `git check-ignore` and `git ls-files`. The skill's own .gitignore
does not protect a different target repository. If the file is already tracked,
ignoring it will not remove it from history: preserve it and resolve removal with
the user. Use external configuration if safe local exclusion is unavailable.
For non-Git workspaces, use external private configuration and keep it outside
any folder packaged or shared with collaborators.

Never copy private profiles into generated reports, examples or a release archive.
Do not auto-commit reports. Inspect the actual publish set, including tracked files,
rather than trusting ignore rules. Ignore rules are accident prevention, not access
control or secret removal.

## Examples and updates

Copy/adapt only the needed fields from [user preferences](../examples/preferences.md)
or [repository context](../examples/repository-context.md). These are illustrative,
not already-approved assignments or discovered project facts.

Updating the public skill replaces methodology, references and templates only.
It does not replace external preferences, project context, reports or
`.dual-agent/STATE.md`. Format 1 remains supported independently of the package's
version; any future incompatible format must have a documented migration preserving
the old file. No second skill, fork, global environment mutation or post-update
copy step is needed.
