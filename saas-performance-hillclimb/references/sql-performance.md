# SQL Performance

Diagnose query performance from the executed plan and representative workload before proposing schema or index changes.

## Establish the Scenario

- Capture the exact query shape, bind-parameter classes, returned rows, table and index cardinalities, data skew, database version and configuration, transaction state, cache state, and concurrency.
- Use production-like cardinality and value distributions. A fast plan on a tiny fixture or common value may conceal a slow plan for large tenants, rare values, or skewed joins.
- Separate client, pool, lock wait, planning, execution, transfer, and application-mapping time. Do not label total endpoint time as query time.
- Measure cold buffer/cache and warm buffer/cache behavior separately. Record database buffer hits/reads and operating-system or storage effects when available.

## Inspect the Plan First

1. Start with the database's read-only plan inspection and capture estimates, access paths, join order, filters, sorts, aggregates, and parallelism.
2. Compare estimated versus actual rows only in a safe environment where executing the statement is authorized.
3. Look for excessive rows scanned or discarded, repeated inner-loop execution, spills, poor selectivity, misestimates, N+1 queries, and work performed after a limiting predicate could have applied.
4. Correlate the plan with slow-query evidence, waits, locks, pool metrics, and a request trace before choosing the edit surface.

PostgreSQL's [plan inspection documentation](https://www.postgresql.org/docs/current/using-explain.html) explains plan nodes and explicitly notes that `EXPLAIN ANALYZE` executes the statement. Never use an executing plan variant on a write statement or shared production path without explicit authority, a transaction or fixture strategy that truly prevents side effects, and a rollback plan. Triggers, functions, locks, sequences, external effects, and long-running reads can still make analysis unsafe.

## Evaluate Candidate Fixes

- **Query shape:** remove unnecessary rows or columns, move selective predicates earlier when semantics allow, eliminate N+1 work, reduce repeated computation, and verify pagination or aggregation semantics.
- **Indexes:** require the plan and workload to justify key order, included columns, partial predicates, or expression indexes. Measure index size, build duration, write amplification, vacuum or maintenance impact, cache pressure, and insert/update/delete latency.
- **Statistics:** inspect stale or insufficient statistics and skew before forcing access paths. Validate changes against parameter classes and representative tenants.
- **Transactions and contention:** inspect lock waits, transaction age, isolation level, retry behavior, hot rows, and transaction scope. A faster query may not fix queueing behind a long transaction.
- **Connections:** inspect acquisition wait, pool size, database connection ceilings, timeouts, leaks, and per-connection memory. Increasing the pool can amplify saturation.
- **Caching:** distinguish database buffers, operating-system page cache, application/result cache, prepared-plan reuse, and proxy caches. Record which layer produced each hit or miss.

Change one main variable and rerun the same baseline protocol plus a sentinel query or write workload. For concurrent tests, confirm the load generator and connection pool are not the limiting resource.

## Keep or Revert

Keep a SQL optimization only when the primary user-visible or query metric clears the threshold, plan or wait evidence moves as predicted, correctness and row semantics match, representative parameter classes improve, and write/lock/pool sentinels stay within guardrails. Revert candidates that merely warm caches, trade read speed for unacceptable write cost, help one cardinality while harming another, increase contention, or cannot reproduce outside a microbenchmark.

