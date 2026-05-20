#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/install-skill.sh <skill-name> <target> [project-root]

Targets:
  codex   -> ~/.codex/skills/<skill-name>
  claude  -> ~/.claude/skills/<skill-name>
  cursor  -> <project-root>/.cursor/skills/<skill-name>
  agents  -> <project-root>/.agents/skills/<skill-name>

Examples:
  scripts/install-skill.sh solo-founder-growth codex
  scripts/install-skill.sh solo-founder-growth claude
  scripts/install-skill.sh solo-founder-growth cursor /path/to/project
  scripts/install-skill.sh solo-founder-growth agents /path/to/project
EOF
}

if [[ $# -lt 2 || $# -gt 3 ]]; then
  usage
  exit 2
fi

skill_name="$1"
target="$2"
project_root="${3:-$PWD}"
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_dir="$repo_root/$skill_name"

if [[ ! -f "$source_dir/SKILL.md" ]]; then
  echo "Skill not found: $source_dir/SKILL.md" >&2
  exit 1
fi

case "$target" in
  codex)
    dest_base="$HOME/.codex/skills"
    ;;
  claude)
    dest_base="$HOME/.claude/skills"
    ;;
  cursor)
    dest_base="$project_root/.cursor/skills"
    ;;
  agents)
    dest_base="$project_root/.agents/skills"
    ;;
  *)
    echo "Unknown target: $target" >&2
    usage
    exit 2
    ;;
esac

dest_dir="$dest_base/$skill_name"

if [[ -e "$dest_dir" ]]; then
  echo "Destination already exists: $dest_dir" >&2
  echo "Remove it first or install under a different name." >&2
  exit 1
fi

mkdir -p "$dest_base"
cp -R "$source_dir" "$dest_dir"

echo "Installed $skill_name -> $dest_dir"
