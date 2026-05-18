#!/usr/bin/env python3
"""Append a solo-founder coaching entry to a repo-local log."""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path
import subprocess
import sys


def git_root(path: Path) -> Path | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(path), "rev-parse", "--show-toplevel"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return Path(result.stdout.strip())


def read_summary(args: argparse.Namespace) -> str:
    if args.summary_file:
        return Path(args.summary_file).read_text(encoding="utf-8").strip()
    if args.summary:
        return args.summary.strip()
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    raise SystemExit("Provide --summary, --summary-file, or stdin.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".", help="Repository path. Defaults to cwd.")
    parser.add_argument("--summary", help="Markdown summary text to append.")
    parser.add_argument("--summary-file", help="File containing markdown summary to append.")
    parser.add_argument(
        "--log-path",
        help="Optional log path. Defaults to <repo>/.codex/solo-founder-growth-coach.md.",
    )
    args = parser.parse_args()

    repo_input = Path(args.repo).expanduser().resolve()
    root = git_root(repo_input) or repo_input
    summary = read_summary(args)
    if not summary:
        raise SystemExit("Summary is empty.")

    log_path = Path(args.log_path).expanduser().resolve() if args.log_path else root / ".codex" / "solo-founder-growth-coach.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    today = dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    entry = f"\n\n## {today}\n\nRepo: `{root}`\n\n{summary}\n"

    if not log_path.exists():
        log_path.write_text("# Solo Founder Growth Coach Log\n", encoding="utf-8")
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(entry)

    print(log_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
