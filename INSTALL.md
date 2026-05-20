# Installing Skills

This repository keeps every skill at the top level:

```text
<skill-name>/SKILL.md
<skill-name>/references/...
<skill-name>/scripts/...
```

Do not move or flatten a skill when installing it. Copy the whole folder.

## Install From This Repo

If you have cloned this repository locally:

```bash
./scripts/install-skill.sh solo-founder-growth codex
./scripts/install-skill.sh solo-founder-growth claude
./scripts/install-skill.sh solo-founder-growth cursor
./scripts/install-skill.sh solo-founder-growth agents /path/to/your/project
```

Targets:

- `codex`: installs to `~/.codex/skills/<skill-name>`
- `claude`: installs to `~/.claude/skills/<skill-name>`
- `cursor`: installs to `.cursor/skills/<skill-name>` in the current project
- `agents`: installs to `.agents/skills/<skill-name>` in the current project

The `agents` target is the most portable project-level option when multiple
coding agents work in the same repository.

## Codex

Use Codex's built-in skill installer:

```text
Install the skill from https://github.com/mick-net/Skills/tree/master/solo-founder-growth
```

Manual install:

```bash
git clone https://github.com/mick-net/Skills.git /tmp/mick-net-skills
mkdir -p ~/.codex/skills
cp -R /tmp/mick-net-skills/solo-founder-growth ~/.codex/skills/
```

Restart Codex after installing new skills.

## Claude Code

Claude Code supports personal and project skills:

```bash
# Personal install
git clone https://github.com/mick-net/Skills.git /tmp/mick-net-skills
mkdir -p ~/.claude/skills
cp -R /tmp/mick-net-skills/solo-founder-growth ~/.claude/skills/
```

```bash
# Project install, run from your project root
git clone https://github.com/mick-net/Skills.git /tmp/mick-net-skills
mkdir -p .claude/skills
cp -R /tmp/mick-net-skills/solo-founder-growth .claude/skills/
```

You can also ask Claude Code:

```text
Install the skill at https://github.com/mick-net/Skills/tree/master/solo-founder-growth into ~/.claude/skills/solo-founder-growth. Copy the whole folder and preserve references and scripts.
```

Review third-party skills before trusting a workspace. Skills are instructions
for an agent, and some skills may ask the agent to run tools.

## Cursor

If your Cursor version supports Agent Skills, install the full folder into one
of these project locations:

```bash
# Cursor-specific
git clone https://github.com/mick-net/Skills.git /tmp/mick-net-skills
mkdir -p .cursor/skills
cp -R /tmp/mick-net-skills/solo-founder-growth .cursor/skills/
```

```bash
# Portable across multiple agents
git clone https://github.com/mick-net/Skills.git /tmp/mick-net-skills
mkdir -p .agents/skills
cp -R /tmp/mick-net-skills/solo-founder-growth .agents/skills/
```

If Cursor does not discover `SKILL.md` folders in your setup, use a rule
fallback:

```bash
mkdir -p .cursor/rules
cat > .cursor/rules/solo-founder-growth.mdc <<'EOF'
---
description: Use for solo SaaS/app founder coaching, validation, pricing, launch, MRR growth, and scope reduction.
alwaysApply: false
---

When the user asks for solo-founder growth, validation, pricing, launch,
marketing, or MRR advice, read and follow:

- .agents/skills/solo-founder-growth/SKILL.md
- .cursor/skills/solo-founder-growth/SKILL.md
- .claude/skills/solo-founder-growth/SKILL.md

Use whichever path exists. If none exists, ask the user to install the full
skill folder first.
EOF
```

This fallback is less robust than native skill discovery because Cursor rules
are regular context instructions, not a guaranteed progressive skill loader.

## Can I Just Ask My Agent To Install It?

Usually yes, if the agent has shell and filesystem access.

Use this prompt:

```text
Install the skill from https://github.com/mick-net/Skills/tree/master/solo-founder-growth.

For Codex, install to ~/.codex/skills/solo-founder-growth.
For Claude Code, install to ~/.claude/skills/solo-founder-growth unless I ask for a project install.
For Cursor, prefer .agents/skills/solo-founder-growth in the current repo; if native skills are not supported, add a small .cursor/rules fallback that points to the skill.

Copy the complete folder. Do not paste only SKILL.md, because the skill relies on references and scripts.
```

Check the result:

```bash
find ~/.codex/skills/solo-founder-growth -maxdepth 2 -type f
find ~/.claude/skills/solo-founder-growth -maxdepth 2 -type f
find .agents/skills/solo-founder-growth -maxdepth 2 -type f
find .cursor/skills/solo-founder-growth -maxdepth 2 -type f
```

