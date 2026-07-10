---
name: orchestrating-subagents
description: Use when a task requests Codex subagents, parallel agents, model-tier routing, Sol/Terra/Luna workers, or complex work has independent bounded tracks that may benefit from delegation.
---

# Orchestrating Subagents

Keep the root agent as lead. Own framing, shared interfaces, integration, risk decisions, and the final answer. Delegate only when speed, isolation, context separation, or independent verification outweigh coordination and token cost. Keep small, sequential, or tightly coupled work with one agent.

## Set the Quality Budget

- Critical security, auth, billing, tenancy, migration, and data-integrity work has no planned quality concession: keep judgment and integration on Sol and use fresh Sol verification.
- For substantive bounded coding, allow Terra max only when the target tolerates up to about 5% relative benchmark degradation and the task has a clear spec, disjoint ownership, and a strong test oracle.
- For deterministic mechanical work, use Luna medium only when an exact check—not model judgment—defines correctness.
- Treat benchmark cost and latency as routing evidence, not a guarantee for one repository. Verification decides whether delegated work is accepted.

## Route Work

| Profile / effort | Assign when |
| --- | --- |
| Root Sol / high | Default coding orchestration, architecture, shared contracts, integration, scope, and final judgment |
| Root Sol / xhigh | Exceptionally ambiguous architecture, long-horizon professional reasoning, or cross-boundary diagnosis needs more depth before execution |
| `sol_max_executor` / max | The hardest bounded implementation has critical security/data risk, a weak test oracle, or needs maximum single-agent coding depth |
| `sol_executor` / high | Complex bounded implementation or debugging needs Sol but not max |
| `terra_coder_max` / max | Substantive bounded coding has a clear spec, strong test oracle, and disjoint ownership |
| `terra_worker_high` / high | Routine one- or two-file change follows established patterns and has clear acceptance criteria |
| `terra_explorer` / medium | Read-heavy discovery, docs research, test triage, or evidence gathering |
| `luna_worker` / medium | Deterministic mechanical work has exact output and an exact check; no behavioral judgment |
| `sol_verifier` / high | Fresh integrated review covers high-risk or disputed work |
| `sol_max_verifier` / max | Fresh integrated review covers critical auth, security, billing, tenant isolation, migrations, or data integrity |

When exposed, confirm the root model and effort before dispatch. Do not claim near-Sol quality when a lower-tier root owns integration. Prefer Sol xhigh over max for broad ambiguous reasoning; reserve max for the hardest single-agent coding or critical verification. Do not push Terra or Luna to max to imitate Sol on broad or ambiguous work—escalate model tier earlier.

If the runtime cannot select a profile or model, delegate by task and report that the model was not pinned. Report requested and actual profile/effort when exposed. Never infer them.

Optional Codex agent profile templates live in `references/agent-profiles/`. To install them globally, copy those `.toml` files into `~/.codex/agents/` and merge `references/config-snippet.toml` into the relevant Codex config if you want the same Sol-high root default, depth limit, and concurrency guardrail.

## Parallelize by Dependency

Parallelize only when at least two work items are independent, any shared contract is already fixed, ownership is disjoint, coordination is cheaper than the saved wall time, and the added token or subscription usage is acceptable.

1. Prefer parallel read-heavy work: codebase exploration, independent test runs, triage, log analysis, documentation checks, and summarization.
2. Use dependency-aware waves for mixed work: parallel discovery; root contract checkpoint; parallel disjoint leaf implementation; root integration; integrated verification.
3. Keep unresolved schemas, shared types, central interfaces, migrations, and cross-cutting fixes on the root until their contract is stable.
4. Parallelize writes only with explicit owned and prohibited files. Run tests sequentially when they share databases, ports, build outputs, fixtures, or other mutable resources.
5. Keep noisy logs and intermediate exploration in child threads. Return concise findings with artifact references so the main thread retains requirements and decisions.
6. Use the fewest helpful agents. With four total slots, run at most three children while the root continues useful work; count automatic agents toward the limit and keep nesting at depth one.

## Prevent Double Fan-Out

If the parent/session is Ultra or automatic subagents are already active, treat that fan-out as the orchestration owner. Inspect active scopes and results; start no second broad manual fan-out. Keep depth one. Add only a narrowly missing role after a slot clears and evidence shows the existing fan-out does not cover it.

## Execute

1. Inspect instructions, specs, dirty state, and the execution path. Define success and identify shared files before dispatch.
2. Apply the dependency gate and choose sequential work or explicit waves before dispatch.
3. Give write-heavy workers disjoint file ownership; keep shared types, schemas, and integration with the root.
4. Send each worker a compact handoff containing:
   - objective and reason;
   - relevant files and evidence;
   - owned and prohibited files;
   - acceptance criteria and tests;
   - required return: findings, changed files, commands/results, assumptions, and blockers.
5. Delegate asynchronously and continue working. Require immediate messages when evidence invalidates the task, ownership overlaps, or a shared contract must change. Interrupt scope drift.
6. Review raw diffs, logs, tests, screenshots, or source references. Integrate results rather than pasting summaries blindly.
7. Allocate review by integrated risk, not worker count:
   - critical: one fresh `sol_max_verifier` on the integrated state;
   - high: one fresh `sol_verifier` on the integrated state; add task review only for a distinct cross-boundary risk;
   - normal substantive: root reviews diffs and tests; sample a Sol review only when uncertainty remains;
   - mechanical: exact check plus root review; no separate reviewer.
8. Run final checks across the integrated state. Record durable decisions, rejected alternatives, and verification gaps in the repo's specs, ADRs, plan, or traceable commit—not only in chat and not as duplicate memory.

## Escalate Once

- Luna → Terra high after any ambiguity, behavioral judgment, nondeterminism, or one failed exact check.
- Terra high/max → Sol high/max after one failed implementation or verification cycle, shared-contract discovery, scope expansion, a weak test oracle, or material security/data risk.
- Sol high → Sol xhigh for unresolved broad ambiguity; use max when the bounded task or critical verification benefits from maximum single-agent depth.
- Do not retry blindly at the same tier. Supply new evidence or escalate.

## Precedence over Superpowers SDD

This skill owns whether to delegate, profile and effort, parallel versus sequential execution, file ownership, and review intensity. `superpowers:subagent-driven-development` is an optional execution protocol only after a written plan when sequential per-task implementation and its review cost are justified. Use this skill alone for parallel disjoint work.

If SDD is invoked, reuse its compact task briefs, status reporting, diff packages, and durable ledger. Do not inherit reviewer-per-worker as a default, run nested SDD controllers under workers, or let workers commit independently unless isolated worktrees and explicit parent authority make that safe.

## Guardrails

- Do not fan out merely because slots exist.
- Do not let multiple agents edit the same files concurrently.
- Do not delegate destructive actions, user-only choices, or final integration authority.
- Do not let the maker be the only reviewer of high-risk work.
- Use `claude-fable-planner` only when the user requests it or an applicable policy warrants an expensive outside critique; it is an oracle, not a bulk executor.
