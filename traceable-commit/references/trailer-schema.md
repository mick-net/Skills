# Trailer Schema

Use only trailers that are true and useful.

## Supported Trailers

- `Spec: <repo-relative path>`
- `Plan: <repo-relative path>`
- `ADR: <repo-relative path>`
- `Issue: #<number>` or `Issue: <URL>`
- `Decision: <ID>`
- `Initiated-by: user|agent|shared`
- `Implemented-by: codex`

## Rules

- Omit missing trailers.
- Use repo-relative paths for local artifacts.
- Use one trailer per line.
- Use one `Decision:` line per decision ID.
- Do not use trailers as decoration. Each trailer should point to evidence that explains the commit.
- Actor values must be exactly `user`, `agent`, or `shared`.

## Parseable Decision Log Format

When plans include decision IDs, prefer this format:

```markdown
## Decision Log

- DEC-001: Chose <decision> because <reason>.
- DEC-002: Deferred <decision> until <condition>.
```

Only reference decisions that exist in the referenced artifact.
