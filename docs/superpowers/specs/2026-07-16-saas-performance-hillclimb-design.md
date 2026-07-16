# SaaS Performance Hillclimb Skill Design

## Goal

Create a reusable `saas-performance-hillclimb` skill that helps Codex improve the speed of SaaS systems through controlled, evidence-backed experiments. Cover SQL queries, APIs and backend work, server-rendered pages, and browser/client performance. Optimize performance only; treat correctness, reliability, error rate, resource use, and cost as guardrails.

## Decisions

- Use one global skill with a shared experiment loop and progressively disclosed layer playbooks.
- Keep the skill stack-agnostic. Inspect and reuse each project's existing profiler, load-test harness, telemetry, performance budgets, and artifact conventions before adding generic tooling.
- Optimize one behavior class and one primary metric at a time.
- Separate cold-cache, warm-cache, concurrency, dataset-size, geographic, device, and network scenarios when they represent different user experiences.
- Prefer repeated baseline/candidate measurements and distributions over single runs or averages.
- Require correctness and holdout/sentinel protection before keeping an optimization.
- Keep the maintained source in `/Users/mickvermaat/Github/Skills/saas-performance-hillclimb`, index it in that repository's `README.md`, and publish the scoped commits to the `mick-net/Skills` remote.
- Install an identical complete copy in `/Users/mickvermaat/.codex/skills/saas-performance-hillclimb` so Codex discovers it globally.

## Alternatives Considered

### Separate skill per layer

This would make triggering precise but duplicate the experiment protocol and fragment cross-layer investigations. A slow page commonly spans browser, edge, application, and database work, so one routing skill is preferable.

### Generic benchmark-harness generator

This would maximize flexibility but encourage infrastructure work before bottleneck localization. The skill should reuse native project tooling first and provide a small fallback comparator only when no suitable comparison path exists.

## Skill Structure

```text
saas-performance-hillclimb/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── experiment-loop.md
│   ├── sql-performance.md
│   ├── api-and-server-performance.md
│   ├── web-client-performance.md
│   └── experiment-record.md
└── scripts/
    └── compare_samples.py
```

`SKILL.md` will contain the routing logic, universal loop, bottleneck taxonomy, keep/revert rules, and safety boundaries. The reference files will contain layer-specific measurement and diagnosis guidance. The Python script will compare simple numeric baseline and candidate sample files without replacing a project's established benchmark tooling.

## Experiment Contract

Before editing, record:

1. User-visible scenario and representative workload.
2. One primary performance metric and whether lower or higher is better.
3. Guardrails: output correctness, error rate, throughput, resource use, and any project-specific invariant.
4. Environment fingerprint: revision, runtime/config, dataset shape, cache state, concurrency, region/device/network profile, and relevant dependencies.
5. Warm-up and measurement protocol, repetition count, timeout, and stop conditions.
6. Optimization pack plus at least one holdout, sentinel, or adjacent workload.
7. A concrete hypothesis that names the suspected bottleneck and predicts an observable change.

Use existing project conventions for durable records. If none exist, use `docs/performance/experiments/YYYY-MM-DD-<slug>.md` and the template in `references/experiment-record.md`.

## Universal Loop

1. Orient in the owning repository and read performance-related specs, history, telemetry, and dirty-worktree state.
2. Reproduce the slow behavior and validate the benchmark harness itself.
3. Establish a repeated baseline under a controlled scenario.
4. Localize the bottleneck with the least invasive evidence source: timing breakdown, trace, query plan, profile, resource waterfall, or runtime profile.
5. Classify the bottleneck before choosing an edit surface.
6. Form one falsifiable hypothesis and change one main variable.
7. Rerun the same optimization and sentinel scenarios.
8. Compare distributions and diagnostics, not only a headline score.
9. Keep, revise, or revert. Record the evidence and the next most informative experiment.

## Bottleneck Taxonomy

- `measurement`: noisy, stale, saturated, non-representative, or incorrect harness.
- `database`: query plan, missing/selective index, excessive rows, N+1 work, lock/contention, connection pool, or transaction scope.
- `application`: CPU, allocations, serialization, algorithmic work, blocking I/O, or duplicated computation.
- `dependency`: downstream API, queue, storage, DNS, TLS, or third-party latency.
- `cache`: miss rate, invalidation, key shape, stampede, cold start, or cache masking.
- `network_edge`: redirects, payload size, compression, CDN, region, protocol, or connection setup.
- `server_render`: data waterfall, render/streaming boundary, TTFB, or hydration payload.
- `browser_load`: render-blocking resources, image/font loading, LCP discovery, bundle execution, or layout shifts.
- `browser_runtime`: long tasks, interaction handlers, rendering, memory, or main-thread contention.
- `capacity`: queueing, saturation, autoscaling, rate limits, or load-generator limits.

Match the experiment to the class. Do not add an index because an endpoint is slow until a query plan or trace implicates database work; do not optimize a Lighthouse score when field data identifies a different user bottleneck.

## Measurement and Comparison Rules

- Report sample count, median, and relevant tail percentiles. Include throughput and error rate for concurrent workloads.
- Treat one-run improvements as leads, not conclusions.
- Keep cache states explicit. Do not average cold and warm behavior into one number.
- Use paired or interleaved runs when environmental drift is likely and the project harness supports them.
- Predeclare a practically meaningful improvement threshold when possible; avoid keeping statistically visible but operationally irrelevant changes.
- Inspect raw samples and outliers. Do not assume latency is normally distributed.
- Confirm the load generator is not CPU, memory, connection, or network saturated.
- For browser work, use controlled lab runs for iteration and field/RUM data for real-user validation when available.

## Keep, Revert, and Escalate Rules

Keep a change only when:

- the primary metric improves by the predeclared meaningful amount or the evidence is otherwise clearly material;
- correctness and error guardrails pass;
- no meaningful holdout or sentinel regression appears;
- the suspected bottleneck diagnostic moves in the predicted direction; and
- the result survives enough repeated runs to distinguish it from ordinary noise.

Revert or reject a change when it merely shifts work to another layer, improves only an unrepresentative microbenchmark, depends on hidden cache warmth, harms tail latency or correctness, or cannot be reproduced. Mark ambiguous results as inconclusive and choose the next experiment that reduces uncertainty.

Escalate from a microbenchmark to component/load/E2E testing only after the narrower experiment shows signal. Validate promising changes against production-like data shape and concurrency before rollout.

## Safety Boundaries

- Treat production load testing, cache flushing, index creation, schema changes, configuration changes, and traffic shifts as state-changing operations that require explicit authority and a rollback path.
- Prefer read-only query plans first. Note that database `EXPLAIN ANALYZE` variants execute statements and can cause write side effects.
- Redact secrets and customer data from benchmark artifacts.
- Avoid benchmarking destructive endpoints unless the environment and fixture reset are explicitly controlled.
- Bound load, duration, concurrency, and abort thresholds before any shared or production-like test.
- Preserve unrelated dirty work and keep optimization commits scoped to validated changes.

## Comparison Script

`scripts/compare_samples.py` will accept baseline and candidate JSON files containing a metric name, direction, unit, and numeric samples. It will emit machine-readable JSON plus a concise text summary with sample count, median, p90, p95, p99, arithmetic mean, min/max, and candidate deltas. It will reject mismatched metric metadata, non-finite values, and underspecified inputs. The skill will direct Codex to prefer native tools such as k6, benchmark frameworks, tracing platforms, database plans, or Lighthouse CI when already present.

## Research Basis

- Google SRE recommends treating latency as a distribution and inspecting median and tail percentiles instead of relying on averages: <https://sre.google/sre-book/service-level-objectives/>.
- Grafana k6 supports percentile and error-rate thresholds and distinguishes protocol, browser, and hybrid workload testing: <https://grafana.com/docs/k6/latest/using-k6/thresholds/> and <https://grafana.com/docs/k6/latest/testing-guides/load-testing-websites/>.
- PostgreSQL documents plan inspection and warns that `EXPLAIN ANALYZE` executes the query: <https://www.postgresql.org/docs/current/using-explain.html>.
- Google distinguishes controlled lab measurements from real-user field distributions and recommends both for Core Web Vitals work: <https://web.dev/articles/lab-and-field-data-differences>.
- Lighthouse recommends multiple runs and aggregate values because individual results vary: <https://github.com/GoogleChrome/lighthouse/blob/main/docs/variability.md>.
- W3C Server Timing provides a standard way to expose backend timing components to browsers: <https://www.w3.org/TR/server-timing/>.
- OpenTelemetry's benchmark guidance recommends warm-up where relevant, repeated measurement, and reporting CPU/memory overhead: <https://opentelemetry.io/docs/specs/otel/performance-benchmark/>.

## Validation

1. Run the skill creator's `quick_validate.py` against the maintained source and global installation.
2. Test `compare_samples.py` with lower-is-better, higher-is-better, malformed, and mismatched inputs.
3. Verify source/install parity with `diff -rq` before publication.
4. Forward-test the skill on three independent synthetic prompts: a slow SQL-backed endpoint, a server-rendered page with high TTFB, and a client page with poor LCP/INP. Give validators only the skill and task artifacts, not the intended diagnosis.
5. Refine instructions if validators skip baselines, conflate cache states, optimize averages alone, or propose production-impacting tests without explicit authority.

## Out of Scope

- Reliability, cost, conversion, SEO content, accessibility, or security optimization as primary goals.
- Automatic production rollout or load generation.
- A universal observability stack or mandatory benchmark framework.
