# Loss-Function Goals

Use this when the requested goal is an optimization run: benchmark hillclimb, parser fidelity, retrieval quality, UI matching, product distillation from public artifacts, generated-output quality, or any target where the agent could overfit a visible score.

## Four Parts

1. **Target:** the metric to improve, measured at the right resolution.
2. **Constraints:** time, money, allowed surfaces, methodology, capacity caps, and safety boundaries.
3. **Instruments:** commands or tools that measure every target and constraint.
4. **Forced entropy:** rules that prevent repeating the same local maximum.

## Required Design Steps

1. Baseline first. Run the current scorer or create a small honest baseline before editing.
2. Split evaluation when possible:
   - Dev inputs visible to the optimizer.
   - Dev answers hidden inside the scorer when feasible.
   - Holdout answers outside the optimizer's read surface.
   - Holdout feedback aggregate-only and used for acceptance.
3. Warn when the eval is small. If cases are few enough to enumerate, the goal must widen the set or add sentinel cases.
4. Score both failure directions. Retrieval needs precision and recall. UI matching needs pixel/layout checks plus semantic checks. Parsers need true positives, false positives, and span/page localization.
5. Add sentinel and anti-overfit cases. Include negatives, perturbations, and cases that punish shortcuts.
6. Cap shortcut artifacts. Name caps for keyword lists, regex lists, seed rows, fixture files, special-case branches, or hand-maintained maps.
7. Leak-audit feedback. A detailed miss list can become an answer key. Reduce feedback resolution or grow the eval when the feedback channel leaks too much.
8. Make constraints observable. A budget, capacity cap, or no-cheating rule without a checker is not a real constraint.
9. Keep a cycle log. Each cycle records hypothesis, expected failure mode, diagnostic, result, and next action before continuing.
10. Babysit cycle 1 for expensive or external-surface runs. Confirm the agent uses the instruments and respects boundaries before leaving it unattended.

## Goal Additions

Add this block to benchmark-style goals:

```text
Loss-function rules:
- Baseline before any edits and record it in [benchmark log].
- Optimize only after the inner spec/tests pass.
- Acceptance is measured on [holdout/scorer], not on visible examples alone.
- Do not read, print, commit, or infer hidden answers.
- Do not add eval-shaped fixtures, literal lookups, per-case branches, or uncapped keyword/regex maps.
- Run [lint/probe/status commands] each cycle.
- If score stalls for [N] cycles, switch hypothesis class before continuing.
- If the scorer, eval, or feedback channel appears gameable, stop and patch the loss function before patching product code.
```

## Common Cheats To Fence

- Hardcoding visible eval examples.
- Growing a keyword list from miss feedback.
- Returning everything to maximize recall.
- Returning one safe item to maximize precision.
- Editing the scorer, test, prompt, or goal instead of the product.
- Creating seed data that mirrors the eval.
- Using filenames, IDs, timestamps, or ordering artifacts as answer hints.
- Treating dev-set success as holdout success.
- Hiding failing cases behind retries or flaky-test skips.
- Spending beyond budget because the metric is still moving slightly.
