# API and Server Performance

Decompose request latency before changing application, dependency, capacity, or server-rendering code.

## Build a Timing Decomposition

Trace one representative request end to end and reconcile:

- client DNS, connection, TLS, redirects, upload, server wait, download, and retries;
- edge, gateway, queue, routing, authentication, rate-limit, and cache time;
- application queueing, middleware, handler, CPU, allocations, blocking I/O, serialization, compression, and logging;
- database, cache, storage, queue, and third-party dependency spans; and
- for SSR, server data waterfalls, render or streaming boundaries, flush time, hydration payload generation, and browser-visible TTFB.

Use consistent clocks and correlation identifiers. Record uninstrumented time instead of assigning it to the nearest span. Where exposure is safe, use the W3C [Server Timing](https://www.w3.org/TR/server-timing/) standard to surface named backend components to browser tooling without leaking secrets, tenant data, or internal topology.

## Localize with Traces and Profiles

1. Start with request traces and timing breakdowns to identify the dominant class and relevant tail behavior.
2. Use CPU, allocation, lock, event-loop, thread, or runtime profiles only after the request evidence implicates application work.
3. Inspect dependency latency distributions, retry and timeout behavior, connection reuse, payload size, and concurrency separately from local compute.
4. Measure serialization and compression with representative response shapes; include bytes transferred and CPU cost.
5. For SSR/TTFB, inspect both server traces and the browser waterfall. A low render duration does not rule out upstream data waterfalls, edge connection setup, buffering, or late streaming flushes.

Account for profiling and telemetry overhead. OpenTelemetry's [benchmark guidance](https://opentelemetry.io/docs/specs/otel/performance-benchmark/) recommends warm-up, repeated measurements, and reporting CPU and memory overhead.

## Shape Load Deliberately

- Distinguish arrival rate from fixed virtual users, open from closed models, steady state from spikes, and read from write or mixed workloads.
- Declare dataset and tenant mix, cache state, payload sizes, geographic path, think time, connection reuse, concurrency, duration, warm-up, timeout, and abort thresholds.
- Measure achieved request rate, latency distribution, errors, retries, queue depth, utilization, and saturation. Do not report a target request rate that the generator failed to achieve.
- Monitor the load generator's CPU, memory, connections, file descriptors, event loop, and network. Scale or distribute it before treating generator saturation as server capacity.
- Avoid destructive endpoints unless fixtures and reset behavior are controlled. Production or shared-environment tests require explicit authority and load bounds.

Grafana k6 documents [percentile and error-rate thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) and the tradeoffs among [protocol, browser, and hybrid website tests](https://grafana.com/docs/k6/latest/testing-guides/load-testing-websites/). Reuse the project's established harness before adding another.

## Test and Validate

State one prediction connecting a candidate to both a headline metric and a diagnostic, such as reduced serialization CPU, dependency span time, queue delay, or time to first streamed byte. Change one main variable, repeat the identical request and load shape, and run an adjacent route, payload, tenant shape, or concurrency level as the sentinel.

Keep a candidate only when its latency distribution or throughput clears the declared threshold, errors and correctness pass, the implicated span or profile moves as predicted, resource use stays within guardrails, and the sentinel does not regress. Reject changes that hide latency in a queue or cache, increase retry storms, improve average latency while harming tails, move work into the browser, or only succeed below representative load.

