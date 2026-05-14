---
name: benchmark-hillclimb
description: Improve an AI agent, retrieval system, benchmark harness, or product workflow through trace-driven benchmark experiments. Use when analyzing failed evals, designing small experiment packs, comparing runs, researching retrieval or agent techniques, or improving prompts/tools without overfitting.
---

# Benchmark Hillclimb

Use benchmarks as product pressure tests, not scoreboards. Improve the system with evidence, one behavior class at a time.

## First Checks

1. Read the product or project context if the repo has one.
2. Inspect `git status --short` so local changes are known before interpreting results.
3. Read the relevant benchmark suite, case pack, previous report, and trace artifacts.
4. Inspect original source files before classifying a failure.
5. If the failure may be model-capability-bound, compare a default model with a stronger oracle model under the same tool and retrieval surface.
6. If repeated local experiments fail, do a short research intake from primary sources before editing.

## Experiment Loop

Use [references/experiment-loop.md](references/experiment-loop.md).

Default cadence:

1. Pick one behavior class.
2. Run a baseline on a small optimization pack and at least one holdout or sentinel pack.
3. Inspect traces and source documents.
4. Form one concrete hypothesis.
5. Make one focused change.
6. Rerun the same packs.
7. Compare baseline and candidate.
8. Keep only changes that improve the target behavior without meaningful regressions.
9. Append the hypothesis, run IDs, result, keep/revert decision, and links to an optimization log.

## Failure Classes

- `retrieval`: search returns empty, weak, or wrong candidates.
- `source_inspection`: candidates are found but the exact page, row, table, or section is not inspected.
- `multimodal`: extraction loses chart, table, layout, image, or page evidence.
- `reasoning`: evidence is available but the answer, math, unit, or selection is wrong.
- `context_efficiency`: tool outputs or prompts are too verbose, duplicated, or poorly shaped.
- `model_capability`: a weaker model fails while a stronger oracle succeeds under the same evidence surface.
- `tool_contract`: wrong path, args, schema, or deprecated tool use.
- `harness`: timeout, stale build, judge transport, readiness, or report bug.
- `data_quality`: benchmark source or gold answer is suspicious.

Match the edit to the failure class. Do not fix reasoning with indexing changes, or data-quality issues with prompt pressure.

## Allowed Edit Surfaces

See [references/edit-surfaces.md](references/edit-surfaces.md).

Prefer changes that make the product or agent generally better:

- prompt wording and output contracts;
- tool descriptions and schemas;
- deterministic tool behavior;
- context shaping and tool-result compression;
- indexing, preflight, retrieval, reranking, and diagnostics;
- benchmark harness, reports, comparison tooling, and case packs;
- generic skills or instructions that teach reusable workflow strategy.

## Anti-Overfitting Rules

- Ask: "If this exact case disappeared, would this still make the product better?"
- Require holdout or sentinel evidence before calling a change positive.
- Track regressions, not only net score.
- Prefer richer evidence access over answer-format coercion.
- Do not encode case IDs, hidden gold answers, or benchmark-specific answers into product behavior.
- Leave unclear experiments uncommitted or explicitly mark them as needing more data.

## Research Intake

Use research when trace evidence shows a repeated behavior class and obvious prompt/tool fixes have failed.

1. Start from the failure class and product need.
2. Search for primary sources such as papers, official docs, benchmark writeups, or implementation repos.
3. Summarize only what affects implementation: signal added, code surface, expected cost/latency, and which pack should detect the effect.
4. Turn the idea into one small experiment.
5. Record tested paper IDs, URLs, and keep/revert decisions.

Do not implement a paper because it is popular. Tie it to a trace-backed failure.
