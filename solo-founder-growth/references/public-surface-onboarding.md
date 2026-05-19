# Public Surface And Onboarding

Use this when the product has, needs, or should have a landing page, website, app-store page, demo, pricing page, signup flow, checkout flow, or first-run onboarding. Internal clarity in `/company` does not count until buyers can understand and act on it.

## When To Run

Run this audit when:

- The user is building features but there is no clear public page or CTA.
- The landing page explains features instead of buyer outcomes.
- The product has traffic but weak signup, trial, checkout, or activation.
- The founder asks for marketing, launch, positioning, demo, onboarding, or MRR growth.
- `/company/product-marketing.md` is clearer than the actual website.

## Sources To Inspect

Inside a repo, inspect:

- Public routes and app routes: `app/`, `pages/`, `src/routes/`, `src/app/`, `public/`.
- Landing, pricing, docs, examples, demo, changelog, and onboarding components.
- README and screenshots if the site is not obvious.
- Analytics notes, PostHog events, funnels, or session recordings when present.
- `company/product.md` and `company/product-marketing.md` for intended promise.

If the site is live and current facts matter, open or browse it. If competitors matter, combine with `market-reality-check.md`.

## Landing Page Tests

The first screen should answer in seconds:

1. Who is this for?
2. What painful job does it solve?
3. What outcome will I get?
4. Why believe this?
5. What should I do next?

Fail conditions:

- Headline says what the product is, not what the buyer gets.
- Copy uses technical implementation language before buyer value.
- CTA is vague: "learn more", "get started" without a clear reason.
- Demo does not show the aha moment quickly.
- Benefits are hidden below feature lists.
- Pricing, free/paid boundary, or next step is unclear.
- No proof: no screenshot, result, customer language, metric, example, or founder credibility.

## Onboarding Tests

The first product session should:

- Show the fastest path to first value.
- Remove setup that can be deferred.
- Use sample data, templates, import, or guided defaults when empty state blocks value.
- Explain one action at a time.
- Ask for payment, setup, or integration only when the value is understood.
- Give the user a visible success moment.

Fail conditions:

- User lands in an empty dashboard with no next action.
- Product requires configuration before showing value.
- Onboarding teaches the UI instead of getting a result.
- The user cannot tell whether the product worked.
- Activation depends on documentation instead of product flow.

## Copy Rewrite Rules

Translate technical copy into buyer copy:

- Feature: "RAG over PDFs" -> Benefit: "answer questions from your policy docs without searching folders."
- Feature: "multi-provider LLM routing" -> Benefit: "keep working when one AI provider is slow, expensive, or blocked."
- Feature: "webhook automation" -> Benefit: "send the finished report to the tool your team already uses."

Keep one technical line only when it builds trust for a technical buyer.

## Skill Routing

Use embedded checks first. Load or suggest deeper skills only when useful:

- `lenny-positioning-messaging`: unclear one-liner, buyer, promise, or homepage copy.
- `lenny-user-onboarding`: signup-to-activation problems.
- `lenny-launch-marketing`: launch page, Product Hunt, beta, waitlist, or feature announcement.
- `lenny-content-marketing`: SEO/tutorial/free-tool content.
- `frontend-skill`: visual execution of a landing page or app surface.
- `product-marketing-context`: create or refresh durable positioning context.
- `analytics-tracking` or `posthog`: instrument landing, signup, activation, and payment events.

Keep the solo-founder filter in control: do not turn this into a brand exercise before buyer proof.

## Output

Use:

- `Public Surface Diagnosis`: the conversion or clarity bottleneck.
- `Aha Moment`: what the buyer should understand or experience first.
- `Rewrite`: headline, subhead, CTA, and proof block when useful.
- `Onboarding Fixes`: smallest changes that reduce time to value.
- `Missing Proof`: customer quote, screenshot, demo, metric, example, or comparison needed.
- `Do Not Build Yet`: features that should wait until the public surface converts.
- `Next Action`: one change to ship or test this week.
