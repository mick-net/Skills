# Embedded GStack-Style Playbooks

Use these embedded workflows before loading external GStack skills. They are Codex-native, solo-founder filtered, and aware of `/company` context.

## Company Context First

When inside a repo, inspect before asking basic questions:

- `company/product.md`
- `company/product-marketing.md`
- `company/ideas/`
- `company/customers/`
- `company/coach/solo-founder-growth-coach.md`

If the answer is already in `/company`, use it and note whether it appears stale.

## Office Hours: Idea/Wedge Validation

Use when the user has an idea, feature concept, side project, or `company/ideas` item.

Questions:

1. Who is the specific buyer by role, situation, and urgency?
2. What are they doing today without this?
3. What makes the current way expensive, slow, risky, embarrassing, or painful?
4. Which subgroup has the problem badly enough to act now?
5. What is the smallest version someone could pay for this week?
6. What behavior proves demand: payment, repeated use, workaround, public complaint, search demand, support issue, or committed pilot?

Output:

- `Hard Read`
- `Narrowest Buyer`
- `Status Quo`
- `Smallest Paid Wedge`
- `Validation Task`
- `Decision`: build now, validate first, cut scope, or drop
- `Company Update`: what should be appended to `/company`

## CEO Plan Review: Scope Challenge

Use after the idea has some evidence and the user has a plan.

Gate:

1. Who is the buyer?
2. What painful job are they doing today?
3. What is the smallest paid wedge?
4. What marketing or sales proof exists?
5. Would this work move MRR, activation, retention, distribution, or support load?

If weak, return to Office Hours or founder-sales/customer-interview work.

Default for solo founders: `SCOPE_REDUCTION`.

Review:

- Restate the plan in one sentence.
- Name the user-visible outcome.
- Identify the revenue or growth mechanism.
- List assumptions that must be true.
- Produce options:
  - `Minimal viable`: fewest files, smallest diff, fastest learning.
  - `Ideal architecture`: only if proof exists.
  - `Do not build yet`: manual validation first.
- Recommend one.
- List out-of-scope items.

Output:

- `CEO Read`
- `Revenue Mechanism`
- `Approaches`
- `Recommendation`
- `Out Of Scope`
- `Next Check`
- `Company Update`
