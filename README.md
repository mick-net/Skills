# Public Codex Skills

Reusable, project-agnostic agent skills.

These skills use the common `SKILL.md` folder shape. Each skill is self-contained
in its own directory and can be installed into Codex, Claude Code, Cursor, or a
portable project-level `.agents/skills` folder.

## Quick Install

The existing GitHub URLs are stable. For example:

`https://github.com/mick-net/Skills/tree/master/solo-founder-growth`

### Codex

In Codex, ask:

```text
Install the skill from https://github.com/mick-net/Skills/tree/master/solo-founder-growth
```

Codex can use its built-in `skill-installer` to install GitHub skill paths into
`~/.codex/skills`.

### Claude Code

Claude Code skills live in either:

- `~/.claude/skills/<skill-name>` for personal skills.
- `.claude/skills/<skill-name>` for project skills committed to a repo.

You can ask Claude Code to install from the GitHub URL, but it should still be
doing the same mechanical work: copy the complete skill folder, including
`SKILL.md`, `references/`, `scripts/`, and any assets.

### Cursor

For Cursor, prefer a project-level install if your Cursor version supports
Agent Skills:

- `.cursor/skills/<skill-name>` for Cursor-specific installs.
- `.agents/skills/<skill-name>` when you want one checked-in copy shared across
  Cursor, Claude Code-compatible agents, Codex-style agents, and other tools
  that understand the common skills layout.

If your Cursor version does not discover `SKILL.md` folders, use the fallback in
[INSTALL.md](INSTALL.md): create a small `.cursor/rules/*.mdc` rule that points
Cursor to the checked-in skill folder.

See [INSTALL.md](INSTALL.md) for copy-paste commands and safer project-level
options.

## Skills

- `traceable-commit`: create narrow, decision-aware Git commits with real verification and provenance trailers.
- `benchmark-hillclimb`: improve AI agents or retrieval systems through trace-driven benchmark experiments.
- `marketing-use-case-pipeline`: turn real workflows into validated marketing use-case packs.
- `marketing-capture`: create real product screenshots and demo videos from deterministic scenarios.
- `continente-grocery-shopping`: existing grocery-shopping workflow skill.
- `solo-founder-growth`: coach solo SaaS/app founders toward MRR with scope, pricing, launch, and accountability playbooks.
- `gstack-office-hours`: pressure-test startup ideas with GStack-inspired YC-style forcing questions.
- `gstack-plan-ceo-review`: challenge implementation plans with GStack-inspired scope reduction and CEO review.

Each skill is self-contained in its own folder with a required `SKILL.md`.
