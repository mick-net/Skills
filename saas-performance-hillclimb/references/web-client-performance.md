# Web Client Performance

Use controlled lab data to iterate and field or real-user monitoring data to validate actual user impact. Do not combine them into one distribution or expect them to match: Google explains the different populations and purposes in [lab and field data](https://web.dev/articles/lab-and-field-data-differences).

## Define the Page Scenario

Record the route and navigation type, revision, authenticated or anonymous state, content and data shape, cache and service-worker state, browser version, device and CPU profile, viewport, network latency and bandwidth, geography, extensions, and run count. Separate cold navigation, warm navigation, prerender, back-forward cache, and client-side route changes when they represent different experiences.

Run Lighthouse repeatedly under the same profile and aggregate results; individual scores vary because of network, CPU, page, and measurement noise. See Lighthouse's [variability guidance](https://github.com/GoogleChrome/lighthouse/blob/main/docs/variability.md). Preserve raw reports and traces, and diagnose from timings and artifacts rather than optimizing the composite score alone.

## Diagnose the Metric

### LCP and Page Load

- Identify the actual LCP element and when it is discovered, requested, received, decoded, and painted.
- Inspect redirects, DNS/connection/TLS, TTFB, HTML streaming, preload and priority, render-blocking CSS or scripts, image format and sizing, font behavior, cache status, resource contention, and late client-side discovery.
- Reconcile the browser waterfall with backend or Server Timing spans. A client resource change cannot fix server wait, and a fast TTFB cannot compensate for a late-discovered LCP resource.

### INP and Browser Runtime

- Capture representative interactions, including the relevant tail, and inspect input delay, handler duration, and presentation delay.
- Use the performance trace to find long tasks, JavaScript evaluation, synchronous work, framework rendering, style/layout, paint, garbage collection, and third-party contention.
- Confirm that deferring or splitting work does not move it onto the next interaction, harm correctness, or worsen an adjacent flow.

### CLS

- Inspect layout-shift clusters and their sources, not only the final score.
- Check missing image or embed dimensions, ad and consent slots, web-font swaps, injected content, animations, hydration mismatches, and late style changes.
- Verify the candidate across viewport sizes, content lengths, localization, and authenticated states.

## Inspect the Whole Waterfall

Record request count and bytes by type, initiator chains, priority, compression, caching, CDN behavior, third-party work, bundle parse and execute time, main-thread tasks, memory, and rendering. Test with the declared device and network profile; a desktop broadband result is not a mobile-field result. Confirm that the automation host itself is not CPU or network saturated.

For concurrent browser and protocol tests, choose the load shape deliberately. Grafana k6 documents when to use [protocol, browser, or hybrid testing](https://grafana.com/docs/k6/latest/testing-guides/load-testing-websites/) and how to enforce [thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/).

## Keep SEO Performance Scope Narrow

Treat crawl or rendering performance as in scope only when the task is specifically about delivery speed, renderability timing, or a performance metric. Do not turn a performance hillclimb into SEO content, metadata, conversion, or ranking optimization. Protect discoverability, rendered content, structured data, canonical behavior, and accessibility as correctness guardrails when performance edits touch them.

## Validate the Candidate

Change one main variable and repeat the identical lab profile. Compare distributions and raw traces, then validate the target metric in field/RUM data when available and statistically supportable. Run a sentinel route, interaction, viewport, device, or network profile. Keep only changes whose primary metric and predicted waterfall or main-thread diagnostic improve without regressions to correctness, other Core Web Vitals, resource use, or the sentinel.

