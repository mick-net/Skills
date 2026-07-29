---
name: converge-and-finish
description: Drive implementation toward risk-adjusted completion when tests, reviews, subagents, or hardening loops expand faster than user-visible progress. Use when a feature substantially works but Codex keeps reviewing, retesting, or fixing increasingly marginal edge cases; when validation effort dominates implementation; or when the user asks to converge, finish, ship, stop over-engineering, or bound review effort. Preserve strict treatment of security, authentication, tenancy, billing, data integrity, destructive migrations, credential exposure, and realistic production-scale performance.
---

# Converge and Finish

Finish the requested outcome with proportionate evidence. Optimize for a complete, safe vertical slice—not theoretical defect elimination.

## Re-anchor on the Outcome

1. Restate the original user-visible outcome and explicit acceptance criteria.
2. Identify the first incomplete path a real user must traverse.
3. Complete that path before adding more generic hardening, review, or test breadth.
4. Keep unrelated pre-existing issues outside the implementation unless they block the outcome or create material release risk.

Do not spend repeated hardening waves on one internal layer while the requested end-to-end path remains incomplete, except for a high-risk finding defined below.

## Triage Findings Independently

Treat reviewer severity as evidence, not authority. Evaluate each finding by likelihood, impact, reversibility, relation to the current change, and whether a realistic input or state can trigger it.

Fix now when at least one condition applies:

- The finding violates an explicit acceptance criterion.
- The current change introduced a reproducible user-facing regression.
- A realistic production path can cause security, authentication, tenancy, billing, data-integrity, credential-exposure, or destructive-migration harm.
- A realistic production workload can overload the database or service, exhaust a bounded resource, or create materially unacceptable latency.
- The defect blocks the primary vertical slice or its safe rollback.

Defer when all relevant evidence points to low release risk, such as:

- The state is impossible or has no credible producer under the documented contract.
- The input is outside the documented contract and no trust boundary requires defensive handling.
- The suggestion is speculative maintainability work without a demonstrated failure.
- More tests would duplicate existing evidence without covering a known gap.
- The issue is unrelated and pre-existing.
- The proposed expansion costs more than the risk reduction and can be handled independently later.

Record a concise reason for every deferred material finding. Never use this skill to dismiss plausible high-impact risk merely to finish faster.

## Use a Bounded Verification Budget

Apply this default budget unless explicit repository rules, acceptance criteria, or material risk require more:

1. Run focused tests while changing behavior.
2. Run the broader relevant suite once when the vertical slice is nearly complete.
3. Run the full required suite once at the final gate.
4. Do not rerun an unchanged suite against unchanged code.
5. Use at most one consolidated independent review, one fix wave, and one scoped re-review.
6. Add reviewer fan-out only for distinct high-risk boundaries; do not assign multiple generic reviewers to rediscover the same class of issues.
7. After the scoped re-review, extend the loop only for a new material blocker or a credible security, tenancy, billing, data-loss, migration, credential, or production-load risk.

Do not add fuzzing, mutation testing, property testing, exhaustive malformed-state tests, or broad lifecycle matrices unless the specification requires them or they reproduce a plausible failure relevant to the change.

When another optional workflow recommends more generic review rounds, use this bounded budget if this skill was explicitly invoked. Continue to obey higher-priority instructions and repository-specific safety gates.

## Run a Convergence Checkpoint

Run this checkpoint when any signal appears:

- Two review rounds have completed.
- Validation time or diff size has overtaken implementation work.
- The same internal layer remains under review while the user-visible path is incomplete.
- New findings are increasingly hypothetical, duplicated, or outside scope.
- Another review would repeat substantially unchanged evidence.

For each remaining item, answer:

1. Does it block the original user-visible goal?
2. Is the triggering state realistic?
3. Was it introduced by the current change?
4. Is the impact material and difficult to reverse?
5. Would another loop materially reduce release risk?
6. Can a targeted follow-up safely handle it?

Classify the item as `FIX NOW`, `DEFER`, or `STOP AND REPORT`. Then act on that classification instead of starting another open-ended review cycle.

## Preserve High-risk Exceptions

Do not apply the ordinary loop limit to unresolved credible risks involving:

- authorization, authentication, or tenant isolation;
- billing amounts, entitlements, or payment state;
- data loss, corruption, or destructive migrations;
- credential or private-data exposure;
- irreversible external side effects;
- realistic production-scale database or service overload.

For these boundaries, reduce uncertainty with the narrowest decisive test or independent review. Stop and report if the risk cannot be resolved within the authorized scope.

## Finish with an Honest Handoff

Report:

- the user-visible outcome completed;
- the focused and final verification actually run;
- any material blocker or unresolved high-risk concern;
- deferred follow-ups with the concrete reason they do not block this delivery;
- any verification gap without implying unearned confidence.

Do not manufacture cleanup work to make the handoff look perfect. Excellent engineering is risk-adjusted completion, not eliminating every theoretically possible defect.
