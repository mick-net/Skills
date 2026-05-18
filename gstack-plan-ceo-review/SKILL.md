---
name: gstack-plan-ceo-review
description: Codex-native adaptation of Garry Tan's GStack /plan-ceo-review workflow. Use when the user has a feature/product plan and wants CEO-level scope challenge, alternatives, minimal viable vs ideal architecture tradeoffs, or a direct review before implementation. For solo founders, default to scope reduction unless demand evidence justifies expansion.
---

# GStack CEO Plan Review

This is a concise Codex adaptation of the public `garrytan/gstack` `/plan-ceo-review` workflow. Preserve the useful CEO-level review structure; do not import Claude-specific tooling, telemetry, or AskUserQuestion machinery.

## Solo-Founder Gate

Before using GStack-style planning, answer:

1. Who is the buyer?
2. What painful job are they doing today?
3. What is the smallest paid wedge?
4. What marketing or sales proof exists?
5. Would this work move MRR, activation, retention, or distribution?

If the answers are weak, stop and recommend validation before implementation.

## Default Mode

For solo founders, default to `SCOPE_REDUCTION`.

Use expansion only when:
- There is paid demand.
- Users already activate and retain.
- The feature clearly increases conversion, ARPA, retention, or distribution.
- The user explicitly asks for ambitious product strategy.

## Review Steps

1. Restate the plan in one sentence.
2. Name the user-visible outcome.
3. Identify the revenue or growth mechanism.
4. List assumptions that must be true.
5. Produce at least two approaches:
   - `Minimal viable`: fewest files, smallest diff, fastest learning.
   - `Ideal architecture`: best long-term trajectory if proof exists.
   - Optional `Do not build yet`: validate manually first.
6. Recommend one approach with a direct reason.
7. List what is explicitly out of scope.

## Scope Reduction Questions

- What is the absolute minimum that ships value to a user?
- What can be a follow-up?
- What can be manual this week?
- What can be mocked, faked, or done with existing tools?
- Which part creates payment, activation, retention, or distribution?
- Which part is just technical elegance?

## Output

Use:

- `CEO Read`: direct verdict on the plan.
- `Revenue Mechanism`: how this could affect MRR or learning.
- `Approaches`: 2-3 options with effort, risk, pros, cons.
- `Recommendation`: one chosen path.
- `Out Of Scope`: explicit cuts.
- `Next Check`: what evidence decides whether to expand later.

## When To Hand Off

- If the plan is still an idea, use `gstack-office-hours` first.
- If the issue is too many features, pair with `lenny-scoping-cutting`.
- If the problem is unclear, pair with `lenny-problem-definition`.
- If implementation starts, use normal repo/spec/test workflow.

Source inspiration: https://github.com/garrytan/gstack/tree/main/plan-ceo-review
