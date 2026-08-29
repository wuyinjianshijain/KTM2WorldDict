# `.agents/` — authoritative skills for every agent

`.agents/skills/` is the **only** place a project skill is edited. Everything
else is a link or a snapshot of it.

```
.agents/
  skills/<name>/SKILL.md          # portable: frontmatter + instructions
                references/*.md   # portable
                scripts/*         # portable
                agents/openai.yaml # Codex-only side-car (UI label, invocation policy)
  .claude-plugin/                 # optional: lets .agents/ be consumed as a Claude plugin
  link-claude-skills.ps1          # regenerates .claude/skills junctions
```

## How each agent reaches it

| Agent | Reads | Wiring |
| --- | --- | --- |
| Codex | `<repo>/.agents/skills/` | native, nothing to do |
| Claude Code | `<repo>/.claude/skills/` | one junction per skill, created by `link-claude-skills.ps1` |

Codex resolves the repo root by looking for `.git`, then reads `.agents/skills`.
It does **not** read `<repo>/.codex/skills`; its only other skill root is
`$CODEX_HOME/skills` (default `~/.codex/skills`), which is global, not per-repo.

Claude Code only scans `.claude/skills`. It refuses to follow a symlinked
*skills root*, but a session does follow symlinked *entries* inside that root —
hence one junction per skill rather than one for the whole tree.

## Adding or renaming a skill

1. Create or rename it under `.agents/skills/`.
2. Run:

   ```powershell
   .\.agents\link-claude-skills.ps1
   ```

Content edits need no re-run: junctions serve the live files.

Junctions are not stored in git, so re-run the script after a fresh clone.
`.claude/skills/` is generated — add it to `.gitignore` and never edit through it.

On macOS/Linux the equivalent is:

```bash
ln -s ../../.agents/skills/<name> .claude/skills/<name>
```

## Optional: consume `.agents/` as a Claude plugin instead

`.agents/.claude-plugin/` makes this directory a valid Claude Code plugin and
local marketplace, usable via `claude --plugin-dir .agents` or:

```
claude plugin marketplace add ./.agents --scope project
claude plugin install worlddict-skills@worlddict --scope project
```

Caveat: installing **copies** the tree into `~/.claude/plugins/cache/` at the
pinned `version`. Later edits to `.agents/skills/` are invisible until the
version in `plugin.json` is bumped and `claude plugin update worlddict-skills
--scope project` is run. Do not combine it with the junctions — the two would
register the same skill names twice.
