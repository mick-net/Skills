# Goal Template

Use this when drafting a copyable Codex `/goal` prompt or a durable `goal.md`. Replace every bracketed field with task-specific content. Delete sections that truly do not apply, but do not delete verification, budget, or stop conditions for long-running work.

## Copyable Prompt

```text
/goal [Concrete objective]

Context:
- Work surface: [repo/worktree/app/thread]
- Read first: [AGENTS.md, specs, key files, issues, logs, prior notes]
- Current assumptions: [known facts and assumptions to verify]

Scope:
- Allowed to touch: [files, directories, services, branches, APIs]
- Do not touch: [unrelated dirt, prod services, secrets, broad refactors, paid APIs]
- Non-goals: [adjacent work to avoid]

State:
- Keep durable progress in: [plan.md, LOG.md, task ledger, benchmark history, etc.]
- Record every cycle with: [hypothesis, action, verification, result, next step]

Iteration protocol:
1. Establish baseline and current state before editing.
2. Choose the smallest next change likely to move the goal.
3. Apply the change within the allowed surface.
4. Run the listed verification.
5. If verification fails, diagnose from evidence and continue only with a changed hypothesis.
6. If verification passes, check completion criteria before claiming done.

Verification:
- Required commands/checks: [exact command list]
- User-visible checks: [browser, UI, API, document, output artifact]
- Acceptance criteria: [pass/fail definition]
- Completion evidence: [files, screenshots, logs, CI runs, benchmark scores]

Budgets:
- Max iterations: [N]
- Wall-clock limit: [duration]
- Spend/token/API limit: [limit or none]
- Parallelism cap: [N agents/tasks] only for independent work

Stop and report when:
- Done: [all acceptance criteria met]
- Blocked: [missing credential, missing source, impossible test, needs decision]
- Budget exhausted: [iteration/time/spend cap]
- No progress: [same failure or no metric movement N times]
- Unsafe or ambiguous: [deploy, delete, purchase, external send, privacy/security tradeoff]

Parallel work:
- Spawn independent agents only for: [domains]
- Give each agent its own objective, files to inspect, acceptance criteria, and output contract.
- Integrate centrally and rerun the full verification before finalizing.

Final report:
- Summarize changes, evidence, commands run, failures handled, remaining risk, and exact artifacts.
- Do not claim completion without verification evidence.
```

## Prompt Review Checklist

- The outcome is measurable and not just "make it better."
- The agent has enough context sources to inspect before acting.
- The allowed and forbidden surfaces are explicit.
- Each acceptance criterion has a command, artifact, or reviewer.
- Budgets and stop reasons are concrete.
- Parallelism is capped and independent.
- The prompt says what to preserve across compaction or interruption.
- The prompt prevents common shortcuts such as editing tests to pass, hiding failures, hardcoding eval items, or widening scope.
