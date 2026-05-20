# Agent Instruction Guardrails

Use this during founder coaching/check-ins or when the user asks why the coding agent keeps overbuilding. Repo-level agent instructions can preserve a small solo-founder operating constraint even when this skill is not explicitly loaded.

Do not treat this as default file-editing permission. Inspect, report, and propose first. Edit only after explicit user approval.

## Files To Inspect

Look for:

- `AGENTS.md`
- nested `AGENTS.md` files in app/package folders
- `CLAUDE.md`
- `.cursor/rules/*.mdc`
- `.github/copilot-instructions.md`
- project docs imported by those files

Do not create all of these. Use the file type the repo already uses, or propose one small addition when no durable agent instruction file exists.

## When To Propose A Guardrail

Propose a repo-level solo-founder snippet when:

- The repo is a solo-founder product or SaaS/app business.
- The agent instructions only cover engineering mechanics and ignore product/revenue constraints.
- Recent work shows overbuilding, broad roadmaps, deep architecture, or hidden backend work without buyer/revenue proof.
- `/company/product.md`, `/company/product-marketing.md`, `/company/ideas/`, or coach logs show the product is early-stage or validation-constrained.
- The user asks for recurring coaching behavior across Codex, Claude Code, Cursor, or other agents.

Do not propose it for libraries, infrastructure-only repos, mature team repos, or short-lived experiments unless the user asks.

## What To Avoid

- Do not turn every bug fix, security fix, reliability issue, or already-validated implementation into a business debate.
- Do not paste the whole solo-founder-growth skill into `AGENTS.md` or `CLAUDE.md`.
- Do not add founder lore, biographies, generic motivation, or long 80/20 speeches.
- Do not weaken existing safety, test, security, release, or coding instructions.
- Do not make the agent hostile. It should be critical when scope or proof is weak, and execution-focused when work is necessary.

## Suggested Snippet

Use this as the default proposal. Keep it short and adapt the file name/tool wording to the repo.

```markdown
## Solo Founder Operating Mode

When work affects product direction, feature scope, roadmap, launch, pricing, onboarding, marketing, or growth:

- Prefer the smallest shippable or manual version that can create customer proof.
- Before expanding scope, identify the buyer, painful job, reachable channel, paid wedge, and next proof target.
- Push back on over-engineering when there is no evidence from users, revenue, activation, retention, support load, or distribution.
- Do not block necessary bug fixes, security work, reliability fixes, or already-validated revenue-moving implementation.
- Keep `/company/product.md`, `/company/product-marketing.md`, `/company/ideas/`, `/company/customers/`, and `/company/coach/` current when the work changes founder context.
```

## Cursor Rule Shape

For Cursor, prefer a project rule rather than bloating unrelated rules:

```markdown
---
description: Solo-founder product and growth guardrails
alwaysApply: false
---

Use when the user asks about product direction, feature scope, validation, pricing, launch, onboarding, marketing, or MRR growth.

- Prefer the smallest shippable or manual version that can create customer proof.
- Before expanding scope, identify buyer, painful job, reachable channel, paid wedge, and next proof target.
- Push back on over-engineering when there is no user, revenue, activation, retention, support, or distribution evidence.
- Do not block necessary bug fixes, security work, reliability fixes, or already-validated revenue-moving work.
- Update `/company` context when the work changes product truth, marketing truth, customer evidence, ideas, or coaching commitments.
```

## Output Shape

When reporting on agent instructions, keep it brief:

- `Found`: files inspected.
- `Gap`: missing or stale behavior, if any.
- `Risk`: why adding this could hurt if too broad.
- `Proposal`: exact snippet or file to update.
- `Approval needed`: yes. Never edit without it.
