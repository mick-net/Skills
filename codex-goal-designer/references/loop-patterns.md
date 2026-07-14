# Loop Patterns

Use this to choose the right loop shape before drafting a goal.

## Surfaces

| Surface | Use For | Avoid When |
| --- | --- | --- |
| Codex `/goal` | Active-thread persistence until a verifiable objective is met | Recurring timed work, vague quality goals, or work without a verifier |
| Codex automation | Scheduled or offline recurring work with results later | One active implementation task |
| Shell or `codex exec` loop | Operator-controlled CLI repetition with explicit caps | Risky writes, unclear stop conditions, or missing logging |
| Skill-generated `goal.md` | Portable design artifact before setting a goal | Tiny one-shot changes |

## Patterns

### Spec-To-Green

Use for implementation work with a known spec.

Contract: read spec, implement smallest slice, run tests/typecheck/lint, update specs if behavior changes, stop when all acceptance checks pass.

Pitfall: editing tests or widening scope to make the loop look green.

### Build-Test-Fix

Use for failing tests, CI, type errors, or lint failures.

Contract: reproduce failure, fix root cause, rerun focused check, then broader check.

Pitfall: increasing timeouts, skipping tests, or changing assertions without proving the product contract changed.

### PR Or CI Babysitting

Use when the user asks to open a PR and keep watching it.

Contract: push branch, watch checks, inspect exact failing jobs, fix related failures, rerun or wait until green, stop for unrelated or ambiguous failures.

Pitfall: claiming done after PR creation before CI completes.

### Production Error Sweep

Use for logs, Sentry, support queues, or bug inboxes.

Contract: classify actionable vs noise, reproduce actionable issues, add regression tests, fix, and report ignored noise separately.

Pitfall: chasing transient third-party noise or making broad speculative fixes.

### Quality Streak

Use when one green run is not enough.

Contract: run realistic scenarios repeatedly, fix new failures, reset streak on any new failure, stop only after N consecutive clean passes.

Pitfall: burning time without a wall-clock or iteration cap.

### Benchmark Hillclimb

Use for parser, retrieval, extraction, UI fidelity, or model-eval improvement.

Contract: baseline, one hypothesis per cycle, score dev, check sentinels/probe, occasionally check holdout, preserve log, stop on target or no-progress cap.

Pitfall: overfitting visible examples or treating a noisy judge as truth.

### Product Or UX Audit

Use for broad user-story testing and polish passes.

Contract: inventory stories, test each story, log issues, fix by severity, retest all touched flows, document remaining product decisions.

Pitfall: starting visual redesign before inventory and regression checks.

### Research Synthesis

Use for source-heavy investigation.

Contract: divide source collection into independent passes, require citations or file anchors, synthesize contradictions centrally, stop when coverage matrix is complete.

Pitfall: letting subagents provide uncited summaries.

### Human Approval Queue

Use when actions need judgment, external sending, deletion, payment, deploy, or policy decisions.

Contract: prepare proposed action, present evidence and options, wait for approval, continue only after explicit approval.

Pitfall: treating approval as a formality inside an autonomous loop.

## Parallel Agents

Use parallel agents when domains are genuinely independent:

- different failing test files with separate root causes
- separate source collections for research
- independent user stories in an audit
- separate platforms or repos with no shared write state

Do not use parallel agents when tasks edit the same files, depend on a shared diagnosis, require a single architecture decision, or touch production state.

Each agent needs: objective, scope, files/sources, forbidden actions, acceptance criteria, expected output, and budget. The coordinator owns integration and final verification.
