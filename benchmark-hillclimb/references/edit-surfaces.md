# Edit Surfaces

## Usually Safe

- benchmark prompts and rubrics;
- tool descriptions and schemas;
- deterministic parsing or extraction bugs;
- retrieval diagnostics;
- context compression;
- report generation and comparison tooling;
- small, generic workflow skills.

## Higher Risk

- broad system-prompt rewrites;
- default model/provider changes;
- embedding/indexing changes without cache isolation;
- benchmark-specific answer formatting;
- hidden answer leakage;
- product behavior changes validated only on one case.

## Verification Pattern

For each change, record:

- baseline run;
- candidate run;
- target behavior;
- holdout/sentinel result;
- keep/revert decision;
- known remaining regressions.
