# Experiment Loop

## Baseline

Run the current system before editing. Save:

- command and environment;
- model/provider IDs;
- case IDs;
- run ID or report path;
- score and failure summary;
- trace paths.

## Hypothesis

Write one testable statement:

```text
If we change <surface>, then <behavior> should improve because <reason>.
```

## Candidate

Make the smallest change that tests the hypothesis.

## Compare

Compare baseline and candidate on the same cases. Include holdout or sentinel cases when possible.

## Decision

Use one of:

- `keep`: improves target behavior without meaningful regressions.
- `revert`: no improvement or regressions.
- `needs-more-data`: mixed result, unstable run, or weak evidence.

Append the result to an optimization log so future agents do not repeat failed experiments.
