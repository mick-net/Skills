---
name: saas-performance-hillclimb
description: Run controlled, evidence-backed SaaS performance experiments across slow SQL queries, APIs, backend or server work, SSR and TTFB, page loads, Core Web Vitals, Lighthouse, LCP, INP, CLS, profiling, load tests, and performance regressions. Use when Codex must benchmark a slow user-visible path, localize its bottleneck, test one safe optimization against a repeated baseline, and protect correctness, reliability, resource, cost, and adjacent-workload guardrails.
---

# SaaS Performance Hillclimb

Improve one behavior class and one primary performance metric at a time. Treat correctness, reliability, error rate, throughput, resource use, cost, and project-specific invariants as guardrails, not optimization targets.

## First Checks

1. Identify the owning repository, production boundary, user-visible scenario, and existing performance tooling.
2. Read performance specs, experiment history, telemetry, and `git status --short` before interpreting measurements.
3. Reproduce the slow path without changing production state.
4. Define one primary metric, guardrails, environment fingerprint, cache state, data shape, concurrency, repetitions, and stop conditions.
5. Choose an optimization pack plus at least one holdout, sentinel, or adjacent workload.

Prefer the project's profilers, load-test harnesses, telemetry, performance budgets, and artifact conventions. Separate cold and warm cache, concurrency, dataset size, geography, device, and network profiles whenever they represent different user experiences.

## Classify the Bottleneck

Classify evidence before choosing an edit surface:

- `measurement`: noisy, stale, saturated, non-representative, or incorrect harness.
- `database`: query plan, missing or unselective index, excessive rows, N+1 work, locks, contention, connection pool, or transaction scope.
- `application`: CPU, allocations, serialization, algorithmic work, blocking I/O, or duplicated computation.
- `dependency`: downstream API, queue, storage, DNS, TLS, or third-party latency.
- `cache`: miss rate, invalidation, key shape, stampede, cold start, or cache masking.
- `network_edge`: redirects, payload size, compression, CDN, region, protocol, or connection setup.
- `server_render`: data waterfall, render or streaming boundary, TTFB, or hydration payload.
- `browser_load`: render-blocking resources, image or font loading, LCP discovery, bundle execution, or layout shifts.
- `browser_runtime`: long tasks, interaction handlers, rendering, memory, or main-thread contention.
- `capacity`: queueing, saturation, autoscaling, rate limits, or load-generator limits.

Do not infer database work from a slow endpoint without a plan or trace. Do not optimize a Lighthouse score when field data identifies a different user bottleneck.

## Run the Universal Loop

1. Orient in the owning repository and capture the scenario, contract, history, telemetry, and dirty-worktree state.
2. Reproduce the slow behavior and validate that the benchmark harness measures the intended path without saturating itself.
3. Establish repeated baseline samples under one controlled scenario. Report sample count, median, and relevant tail percentiles; add throughput and error rate for concurrent workloads.
4. Localize the bottleneck with the least invasive evidence: timing breakdown, trace, query plan, profile, resource waterfall, or runtime profile.
5. Classify the bottleneck and state one falsifiable hypothesis that predicts both a primary-metric change and a diagnostic change.
6. Change one main variable. Keep unrelated work intact and keep the candidate reversible.
7. Rerun the identical optimization and sentinel scenarios with the same warm-up, cache, data, concurrency, timeout, and repetition protocol.
8. Compare distributions, raw samples, outliers, diagnostics, guardrails, and the predeclared practical threshold. Treat a single run as a lead, not a conclusion.
9. Keep, revise, or revert the candidate. Record the evidence, decision, rollback, and next most informative experiment.

Use paired or interleaved runs when environmental drift is likely. Never average cold and warm behavior into one result. See [the complete experiment loop](references/experiment-loop.md) whenever defining or executing a baseline-versus-candidate experiment.

## Fallback Comparison Tool

Prefer project-native comparison tooling when it exists. Otherwise, save each sample set as `{"metric": "latency", "unit": "ms", "direction": "lower", "samples": [100, 110, 120]}` and run `python3 saas-performance-hillclimb/scripts/compare_samples.py BASELINE.json CANDIDATE.json --format text` (or use `--format json` for machine-readable output).

## Decide Whether to Keep the Change

Keep a change only when the primary metric improves materially, correctness and error guardrails pass, no meaningful holdout or sentinel regression appears, the implicated diagnostic moves as predicted, and repeated runs distinguish the result from ordinary noise.

Revert or reject a candidate that shifts work to another layer, improves only an unrepresentative microbenchmark, relies on hidden cache warmth, harms tail latency or correctness, or cannot be reproduced. Mark ambiguous results `inconclusive`; choose the next experiment that reduces uncertainty. Escalate from microbenchmark to component, load, or end-to-end testing only after the narrower experiment shows signal, then validate against production-like data shape and concurrency before rollout.

## Respect Safety Boundaries

- Treat production load testing, cache flushing, index creation, schema or configuration changes, and traffic shifts as state-changing operations requiring explicit authority and a rollback path.
- Prefer read-only query plans. Database `EXPLAIN ANALYZE` variants execute statements and may cause writes or other side effects.
- Redact secrets and customer data from measurements and artifacts.
- Avoid destructive endpoints unless fixtures and reset behavior are explicitly controlled.
- Bound load, duration, concurrency, and abort thresholds before shared or production-like tests.
- Preserve unrelated dirty work and scope commits to validated changes.

## Load the Relevant Playbook

- For query-plan, index, locking, pool, or database work, read [SQL performance](references/sql-performance.md).
- For API, backend, dependency, capacity, SSR, or TTFB work, read [API and server performance](references/api-and-server-performance.md).
- For page load, Lighthouse, LCP, INP, CLS, browser runtime, or SEO performance work, read [web client performance](references/web-client-performance.md).
- When the repository has no durable performance-record convention, copy [the experiment record](references/experiment-record.md) to `docs/performance/experiments/YYYY-MM-DD-<slug>.md` and keep it current.
