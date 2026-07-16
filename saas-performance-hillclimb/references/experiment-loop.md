# Experiment Loop

Use this protocol for every layer. Preserve the repository's existing benchmark and artifact conventions when they are at least as rigorous.

## 1. Write the Measurement Contract

Before editing, record:

- the user-visible scenario and representative workload;
- one primary metric, its unit, direction, and a practically meaningful improvement threshold;
- correctness, error-rate, throughput, resource, cost, and project-specific guardrails;
- the revision, runtime and configuration, dependency versions, dataset shape and cardinality, cache state, concurrency, region, device, and network profile;
- setup, warm-up, repetition count, timeout, sampling, teardown, and abort conditions;
- the optimization workload plus at least one holdout, sentinel, or adjacent workload; and
- one falsifiable hypothesis naming the suspected bottleneck and its predicted metric and diagnostic changes.

Do not combine distinct cold-cache, warm-cache, concurrency, dataset-size, geographic, device, or network experiences into one benchmark.

## 2. Validate the Harness and Baseline

1. Reproduce the user-visible symptom without changing production state.
2. Confirm that fixtures, clocks, sampling, telemetry, and result parsing measure the intended path.
3. Confirm the load generator is not CPU, memory, connection, file-descriptor, or network saturated.
4. Run the declared warm-up, then collect repeated raw baseline samples. Interleave control runs when environmental drift is likely.
5. Record sample count, median, relevant tail percentiles, min/max, and outliers. For concurrent workloads, also record achieved throughput and error rate.

Latency is a distribution; do not substitute an average or one run for median and tail behavior. See Google SRE's [service level objectives guidance](https://sre.google/sre-book/service-level-objectives/) and OpenTelemetry's [performance benchmark guidance](https://opentelemetry.io/docs/specs/otel/performance-benchmark/) on repeated measurement, warm-up, and CPU or memory overhead.

## 3. Localize Before Editing

Choose the least invasive evidence source that can separate likely bottleneck classes:

- timing breakdown or distributed trace for request and dependency time;
- query plan and database wait evidence for database work;
- CPU, allocation, lock, event-loop, or runtime profile for application work;
- cache hit/miss and invalidation evidence for cache behavior;
- resource waterfall and browser performance trace for page load or runtime work; or
- queue, saturation, and utilization signals for capacity work.

Match clocks and request identifiers before comparing layers. Attribute unexplained time explicitly instead of forcing it into the nearest visible span.

## 4. Test One Variable

1. State one hypothesis: `Because <evidence>, changing <one variable> should improve <primary metric> by <threshold> and move <diagnostic> without violating <guardrails>.`
2. Make the smallest reversible candidate that tests it.
3. Re-run the exact baseline protocol and collect raw candidate samples.
4. Avoid opportunistic cleanup, unrelated refactors, or multiple optimization variables in the same candidate.

For load tests, encode percentile and error-rate abort criteria when supported; Grafana k6 documents [thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) for this purpose.

## 5. Validate the Sentinel

Repeat the holdout, sentinel, or adjacent workload under the same controlled conditions. Check that the candidate does not:

- shift time to another layer;
- improve the median while harming the relevant tail;
- reduce correctness, throughput, or reliability;
- depend on unrecorded cache warmth;
- raise CPU, memory, I/O, connection, or cost beyond guardrails; or
- regress a different data shape, concurrency level, route, device, or network profile.

## 6. Decide and Log

Keep the candidate only when it clears the practical threshold, all guardrails pass, the sentinel shows no meaningful regression, the diagnostic moves as predicted, and repeated runs rise above ordinary noise.

Otherwise:

- **Revise** when the evidence still supports the bottleneck but the candidate did not isolate it cleanly.
- **Revert** when the effect is unrepresentative, irreproducible, shifted elsewhere, cache-dependent, or guardrail-breaking.
- **Mark inconclusive** when noise or environment drift prevents a decision; choose the next experiment that most reduces uncertainty.

Log baseline and candidate samples or artifact paths, comparison statistics, trace or plan evidence, guardrail and sentinel results, the decision, rollback, remaining uncertainty, and the next experiment. Use the repository's convention; otherwise use `docs/performance/experiments/YYYY-MM-DD-<slug>.md` with [the experiment record](experiment-record.md).

