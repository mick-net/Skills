# Metrics Growth Diagnosis

Use this when a product is launched, has traffic, has signups, has revenue, or the founder asks how to grow MRR. Keep this lightweight. Metrics should answer the next business question, not become another engineering project.

## Principle

First identify the current stage/MRR. Then ask for the smallest metric set that explains the bottleneck:

1. Are people finding it?
2. Do they understand it?
3. Do they reach value?
4. Do they pay?
5. Do they stay?
6. Can the channel repeat?

If the product has no traffic and no customers, do not over-instrument. Push the founder toward the earliest shippable prototype, selling, launching, outreach, or public proof.

When revenue exists, reduce the business to the simple revenue equation before adding dashboards:

`revenue capacity ~= customers acquired per period * average retention duration * average price`

Then pick one operational metric for the current lever:

- Acquisition: qualified conversations, demos, trials, signups from the main channel, or calls booked.
- Retention: activation success, useful outputs delivered, repeat usage, support themes, churn reasons, or time to first value.
- Price/ARPA: plan mix, close rate by price, expansion requests, refund reasons, support load per plan, or gross margin.

Do not optimize all three at once. If every metric improves but revenue still falls, inspect the work directly: sales calls, support tickets, onboarding sessions, failed jobs, and customer outcomes. Numbers can hide quality decay.

## Useful Data Sources

Use whatever the environment can access. In Codex, this may be skills/plugins. In Claude Code, Cursor, or other agents, this may be MCP servers, API docs, CLI tools, exports, screenshots, CSVs, or pasted metrics.

- Revenue: Stripe or payment exports for MRR, new MRR, churn, failed payments, ARPA, plan mix, trial-to-paid.
- Traffic: Google Analytics, Plausible, Simple Analytics, server logs, Vercel/Cloudflare analytics.
- Product analytics: PostHog or similar for funnels, activation, retention, cohorts, feature use.
- Search: Google Search Console, Ahrefs/Semrush, rank trackers, indexed pages, backlinks, query impressions.
- UX friction: Microsoft Clarity, PostHog Replay, Sentry Replay, session recordings, heatmaps.
- Reliability: Sentry/errors/performance logs when bugs block activation or retention.
- Qualitative: customer calls, support tickets, churn notes, sales objections, onboarding replies.

Do not hardcode one vendor. Prefer whatever is already installed and trusted.

## Stage Diagnosis

### Still Building / Prelaunch

Look for:
- Earliest shippable prototype.
- Landing page or demo.
- Buyer list and reachable community/channel.
- Paid wedge, Stripe button, waitlist, pilot ask, or manual service offer.
- 5-10 real buyer conversations.

Default action:
- Ship the smallest demo/prototype that makes the painful job obvious.
- Add a CTA that asks for payment, a pilot, a call, or a concrete commitment.
- Use `community-reachability.md` if the founder cannot name 10 reachable prospects.
- Talk to buyers before adding technical depth.

Avoid:
- Deep architecture.
- Complex analytics.
- Building invisible backend capability before there is a public promise.

### Launched / No Revenue

Look for:
- Traffic source and volume.
- Landing-page conversion.
- Signup or reply rate.
- First activation.
- Payment attempt, pilot, or sales-call ask.

Default action:
- If no traffic: launch harder, do outreach, publish proof, or seed SEO pages.
- If traffic but no signup: fix public surface, promise, proof, CTA.
- If signups but no payment: add/tighten paid boundary and manually onboard.

Avoid:
- Treating "launched" as success.
- Adding features before someone tries to pay.

### First Paying Customers / $1 To $1k MRR

Look for:
- Traffic or audience source.
- Reachable community/channel.
- Number of real buyer conversations.
- Landing page visits and signups.
- Payments or serious purchase intent.
- Manual pilots, demos, or replies.

Default action:
- If no traffic: launch, outreach, community, or SEO seed pages.
- If traffic but no signup: fix positioning, CTA, proof, and demo.
- If signups but no payment: ask for money, simplify pricing, add trust, or manually onboard.
- Make first $1k MRR the goal, not launch count or feature count.

Avoid:
- Complex dashboards.
- Attribution modeling.
- Deep cohort work before there are cohorts.

### $1k To $10k MRR

Find the bottleneck:
- No traffic: distribution, SEO, backlinks, partnerships, marketplace, or content problem.
- Traffic but weak signup: CRO, copy, public surface, trust, proof, pricing-page problem.
- Signup but weak activation: onboarding, empty state, setup burden, unclear aha moment.
- Activation but weak payment: packaging, urgency, free/paid boundary, objection, payment friction.
- Payment but churn: product value, repeat use, reliability, support, wrong buyer, weak onboarding.

Default action:
- Fix the narrowest leaking step.
- Keep one main channel and one main buyer until growth repeats.
- Talk to every churned, non-activated, and high-intent user before adding features.
- Check whether pricing is too low for the support burden.

### $10k To $100k MRR

Use deeper metrics:
- Cohort retention and expansion.
- Channel quality by paid conversion, not visits.
- Product-qualified leads and high-intent accounts.
- Churn reasons and support themes.
- SEO page performance and backlink gaps.
- Reliability or performance issues that hit valuable users.

Default action:
- Systematize the channel that already works.
- Add pricing/packaging or team/B2B expansion only when signals exist.
- Improve onboarding and retention before adding broad features.
- Track founder load, delivery quality, margin, and customer concentration alongside MRR; a growing high-touch business can still be fragile.

## Routing To Existing Skills

Load or suggest only when the bottleneck is clear:

- `stripe` plugin or Stripe exports: revenue, subscriptions, churn, failed payments, plan mix.
- `sentry` plugin or `sentry` skill: production errors, performance, replay-backed failures.
- `posthog` skill: funnels, activation, retention, cohorts, feature usage.
- `analytics-tracking` skill: missing event instrumentation.
- `seo-audit`, `ai-seo`, `schema-markup`, `google-ai-seo-writing`: search visibility, SEO pages, schema, AI search.
- `lenny-user-onboarding`: activation and first-value problems.
- `lenny-pricing-strategy`: pricing, packaging, free/paid boundary.
- `lenny-retention-engagement`: churn, repeat use, habit, engagement.
- `lenny-content-marketing`: SEO/content channel.
- `public-surface-onboarding.md`: landing page, demo, CTA, pricing page, onboarding clarity.

If no tool access exists, ask for a pasted summary or export. Do not block the diagnosis on perfect integrations.

## Output

Use:

- `MRR Stage`: still-building/prelaunch, launched/no revenue, first paying customers / $1-$1k, $1k-$10k, $10k-$100k, $100k+, or unclear.
- `Metric Evidence`: what was inspected and what it suggests.
- `Likely Bottleneck`: traffic, conversion, activation, payment, retention, expansion, or channel repeatability.
- `Missing Data`: at most 1-2 metrics that would change the decision.
- `What To Do Now`: the next 30-90 minute action.
- `Recommended Move`: the smallest action likely to move MRR.
- `Do Not Do`: dashboard/integration/work that is not needed yet.
