# Performance Experiment Record

Copy this template into the repository's established performance artifact location. If none exists, use `docs/performance/experiments/YYYY-MM-DD-<slug>.md`. Update it during the experiment rather than reconstructing intent afterward.

```markdown
# <Experiment title>

- Date:
- Owner:
- Status: proposed | running | kept | reverted | inconclusive
- Revision / branch:
- Related spec, issue, trace, or commit:

## Scenario

- User-visible behavior:
- Exact workload and entry point:
- Representative data shape / cardinality / tenant class:
- Optimization pack:
- Holdout, sentinel, or adjacent workload:

## Measurement Contract

- Primary metric:
- Unit and direction (lower or higher is better):
- Practically meaningful threshold:
- Correctness guardrails:
- Error / reliability guardrails:
- Throughput guardrail:
- CPU / memory / I/O / connection guardrails:
- Cost or project-specific guardrails:
- Warm-up, repetitions, timeout, sampling, and stop conditions:

## Environment Fingerprint

- Revision and dirty-worktree state:
- Runtime, build, configuration, and dependency versions:
- Host / container / database characteristics:
- Dataset and fixture version:
- Cache and buffer state:
- Concurrency and load shape:
- Region / edge / dependency path:
- Browser, device, viewport, CPU, and network profile:
- Load-generator resource state:

## Baseline

- Command or procedure:
- Raw sample / report paths:
- Sample count:
- Median and relevant tail percentiles:
- Throughput and error rate, if concurrent:
- Resource use:
- Outliers and noise notes:

## Localization Evidence

- Timing decomposition, trace, plan, profile, waterfall, or wait evidence:
- Bottleneck class:
- Artifact links / identifiers:
- Remaining unexplained time:

## Hypothesis

Because <evidence>, changing <one variable> should improve <primary metric> by <threshold> and move <diagnostic> without violating <guardrails>.

## Candidate

- One main variable changed:
- Diff / configuration:
- Reversibility:
- Candidate raw sample / report paths:
- Sample count:
- Median and relevant tail percentiles:
- Throughput and error rate, if concurrent:
- Resource use:
- Diagnostic change:

## Holdout / Sentinel Result

- Workload:
- Baseline versus candidate:
- Correctness and guardrail results:
- Regressions or shifted work:

## Decision

- Decision: keep | revise | revert | inconclusive
- Evidence against the practical threshold:
- Reproducibility / noise assessment:
- Why this decision follows from the hypothesis and guardrails:
- Remaining uncertainty:

## Rollback

- Exact rollback procedure:
- State or data restoration required:
- Verification after rollback:

## Next Experiment

- Next most informative hypothesis:
- Why it reduces uncertainty:
- Required authority or safety boundary:
```

For interpretation, preserve latency distributions and tails as recommended by Google SRE's [service level objectives guidance](https://sre.google/sre-book/service-level-objectives/). For concurrent tests, preserve declared percentile and error-rate criteria such as Grafana k6 [thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/). For profiler or telemetry experiments, record warm-up, repetition, and CPU or memory overhead following OpenTelemetry's [benchmark guidance](https://opentelemetry.io/docs/specs/otel/performance-benchmark/).
