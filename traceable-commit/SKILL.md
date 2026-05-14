---
name: traceable-commit
description: Stage only the files related to the current task, split unrelated work into scoped commits, and create decision-aware Git commit messages with real verification and provenance trailers. Use when committing changes in repositories that need durable context for future maintainers or agents.
---

# Traceable Commit

Create commits that preserve the reasoning behind a change, not only the diff.

## Core Rule

Commit only the files that belong to the current task. Do not stage the whole worktree by default.

## Workflow

1. Inspect `git status --short`.
2. Bound the commit scope from the user request, current task, and files changed in this session.
3. If files are already staged, inspect `git diff --cached --stat` and `git diff --cached` before trusting the staged set.
4. Split unrelated work into separate commits when changes have different purpose, risk, verification, or rollout story.
5. Check whether the change affects durable behavior, APIs, storage, security, operations, or user workflows. If so, update or reference the relevant spec, plan, ADR, or issue.
6. Stage the narrow slice.
7. Inspect the staged diff.
8. Commit with a message that explains why the change exists, how it works, and what was verified.
9. Run `git status --short` again and report leftover unstaged changes.

## Commit Message Shape

```text
<type>: <short outcome>

Why:
- <reason, decision, or user-visible problem>

How:
- <implementation shape>

Verification:
- <commands or checks actually run>

Spec: <path>
Plan: <path>
ADR: <path>
Issue: #123
Decision: DEC-001
Initiated-by: user|agent|shared
Implemented-by: codex
```

Omit sections and trailers that do not apply. Never invent specs, issues, decisions, or verification.

## Scope Rules

- Keep behavior changes and their matching spec updates together when they describe the same slice.
- Commit docs-only provenance updates separately when they cover broader future work.
- Use selective staging when one file contains clearly separate hunks.
- Stop and ask when scope is genuinely ambiguous and committing unrelated work is likely.
- Do not revert or clean up unrelated local changes.

## Provenance

Prefer references that future maintainers can actually open:

- `Spec:` for product or behavior contracts.
- `Plan:` for implementation plans or decision logs.
- `ADR:` for architectural decisions.
- `Issue:` only when present in the request, branch, or repo artifacts.
- `Decision:` only for real decision IDs in a referenced plan or ADR.

Use actor trailers consistently:

- `Initiated-by: user` when the user asked for the outcome.
- `Initiated-by: shared` when direction was materially shaped through discussion.
- `Initiated-by: agent` for agent-initiated cleanup or follow-up.
- `Implemented-by: codex` when Codex produced the implementation.

## References

- Trailer schema: [references/trailer-schema.md](references/trailer-schema.md)
- Commit template: [assets/commit-template.txt](assets/commit-template.txt)
