---
name: codex-goal-designer
description: Design, refine, and review Codex /goal prompts and long-running goal-loop instructions. Use when the user asks to write a goal prompt, use Codex /goal, create a long-running autonomous task, design a loop or loss function, run benchmark hillclimbs, coordinate parallel agents, or turn a vague request into a bounded objective with verification, budgets, state artifacts, and stop conditions.
---

# Codex Goal Designer

Design the goal before setting it. Codex `/goal` keeps a persistent target attached to the active thread, but it does not make a vague objective measurable, bounded, or safe. Use this skill to turn a request into a goal contract that Codex can execute or that the user can paste into `/goal`.

Do not set a live goal automatically unless the user explicitly asks to set or run it. If the user asks for a goal prompt, emit the prompt or a `goal.md` style artifact instead.

Before drafting or setting a goal, ask the user targeted questions for information that is still missing. Ask only for the minimum information needed to proceed safely: blockers, required constraints, and decisions that would materially change the goal, scope, verification, or stop conditions. Do not turn the interaction into a full requirements interview; use reasonable assumptions for details that are not blockers or big decisions, and state those assumptions in the resulting goal contract.

## Decision

- Use a normal task plan, not `/goal`, when the work is small, single-turn, and has obvious verification.
- Use a Codex goal prompt when the work needs repeated inspect-act-verify cycles, CI babysitting, broad audits, batch fixes, long-running implementation, or continuation after compaction.
- Use an automation, scheduler, or shell loop when the user needs recurring time-based work or offline monitoring. `/goal` alone is for an active thread objective.
- Use the loss-function path when the task optimizes against an eval set, benchmark, reference product, public artifact, quality score, or hidden expected-output examples.
- Use a companion oracle only when cheap local evidence is not enough. Prefer `$claude-fable-planner` for expensive architecture, high-blast-radius planning, or deep review, not for routine goal wording.

## Workflow

1. Inspect before drafting. Check the active repo/worktree, `AGENTS.md`, relevant `/specs`, existing tests, scripts, logs, evals, CI commands, dirty state, and relevant memories. For credentials, check presence only and never print secrets.
2. Classify the loop type: spec-to-green implementation, build-test-fix, PR/CI babysitting, production error sweep, benchmark hillclimb, product/UX audit, research synthesis, maintenance sweep, or human-approval queue.
3. Define the goal contract: objective, non-goals, allowed surfaces, forbidden surfaces, state artifacts, acceptance criteria, progress signal, budget, stop reasons, and reporting format.
4. Add instruments. Every constraint needs a way to observe it: test command, scorer, lint, status command, spend check, time log, browser check, CI check, or human approval gate. If no instrument exists, call that out instead of pretending the loop can self-verify.
5. Add stop guards: max iterations, wall-clock budget, cost/token budget when relevant, no-progress threshold, repeated-failure threshold, approval-required actions, and risky external actions that must stop for the user.
6. Route parallel work conservatively. Dispatch subagents only for independent tasks with no shared edit state, give each one a scoped objective and acceptance criteria, cap the count, then integrate and verify centrally. Do not translate "as many agents as needed" into unbounded fanout.
7. Emit or set the goal. If the user asked for a prompt, produce a copyable `/goal ...` prompt or `goal.md`. If the user explicitly asked to set the goal in the current thread and the goal tool is available, set it only after the contract is specific enough.

## Goal Requirements

Every serious goal prompt should include:

- **Outcome:** the concrete end state.
- **Scope:** repo, worktree, files, systems, APIs, and data that may be touched.
- **Non-goals:** tempting adjacent work that must stay out.
- **State:** durable files such as `plan.md`, `LOG.md`, task ledger, evidence table, benchmark history, or checkpoint commits.
- **Iteration protocol:** what to do each cycle, what to inspect first, and how to choose the next step.
- **Verification:** exact commands or checks that prove progress and completion.
- **Budgets:** max iterations, wall-clock, spend, tool calls, or batch size.
- **Stop conditions:** done, blocked, needs user input, budget exhausted, no progress, unsafe action, or ambiguous tradeoff.
- **Reporting:** what to summarize, including evidence paths, commands run, failures, remaining risk, and next action.

Read `references/goal-template.md` when drafting a reusable prompt or a `goal.md` artifact.

## Loss-Function Goals

For benchmark, parser, retrieval, product-distillation, UI-clone, or quality-score work, design an optimization target rather than only a spec. Read `references/loss-function-goals.md` before emitting the goal.

Required additions:

- Baseline before edits.
- Eval split with visible inputs and hidden answers where possible.
- Holdout-only acceptance when overfitting is plausible.
- Mechanical scorer at the right resolution, not a vague self-judge.
- Constraints on shortcut artifacts such as keyword lists, seed data, special cases, regex sets, and generated fixtures.
- Leak audit for every feedback channel.
- Per-cycle log with hypothesis, expected failure mode, diagnostic, result, and next change.
- Forced entropy rule when the score stalls: the next cycle must try a materially different hypothesis, not the same knob harder.

## Companion Skills

- Use `$ai-harness-engineering` when the question is really about building or improving a harness, scorer, durable state, or loop controller.
- Use `$dispatching-parallel-agents` or the active platform's equivalent when two or more independent domains can be researched or fixed concurrently.
- Use `$claude-fable-planner` only after cheap evidence gathering when the remaining decision is expensive, ambiguous, or high blast radius.
- Use the repo's traceable commit or review workflow when the goal includes committing, opening a PR, or babysitting CI.

Do not make companion skills mandatory in the generated prompt. Name when to use them and why, so the executing agent can apply the platform's current skill rules.

## Pattern Reference

Read `references/loop-patterns.md` when the user asks what kind of loop to run, when the request mixes `/goal`, loops, routines, or parallel agents, or when you need a starting shape for the goal.

When answering the user, be direct about whether `/goal` is actually the right surface. Sometimes the best answer is "do not use `/goal`; make a test, run a normal patch, or create an automation."
