# Company Context

Use this when the skill is operating inside a product repo. The repo's `/company` folder is the durable founder context layer.

## Folder Contract

Expected paths:

- `company/product.md`: product truth. What the app does, buyer, painful job, wedge, current stage, current constraints.
- `company/product-marketing.md`: positioning, ICP, channels, offers, proof points, launch/content notes.
- `company/public-surface.md` (optional): current landing page, onboarding, pricing, demo, and CTA audit notes.
- `company/metrics.md` (optional): lightweight current growth metrics and bottleneck notes.
- `company/customers/`: meeting transcripts, interview notes, support summaries, churn notes, testimonials.
- `company/coach/`: solo-founder-growth coach logs and weekly accountability.
- `company/ideas/`: raw ideas, feature concepts, market observations, and possible bets.

Do not assume every repo has all files. When missing, call out the gap and suggest the smallest useful file.

## Coach Log

Default log path:

`company/coach/solo-founder-growth-coach.md`

Append entries. Do not overwrite prior coaching history.

Use `scripts/log_coach_session.py --repo <repo> --summary <text-or-file>` to write entries.

Each coaching entry should include:

- Date.
- Repo path.
- Product wedge.
- Evidence inspected.
- Hard read.
- Recent work classification.
- Customer/marketing/revenue evidence.
- Idea gatekeeping decisions.
- Commitments before next check-in.

## Keep Product Context Current

During a coaching/check-in session, inspect:

- `company/product.md`
- `company/product-marketing.md`
- recent files under `company/customers/`
- recent files under `company/ideas/`
- existing `company/coach/solo-founder-growth-coach.md`

If product or marketing docs are stale, say exactly what changed and what should be updated.

For example:

- "The product doc still says X, but recent commits and positioning imply Y."
- "The marketing doc names broad ICPs but the customer notes only show traction with Z."
- "This feature appears in `company/ideas`, but I do not see buyer proof yet."

## Context Debt

Call out context debt when `/company` would mislead the next agent.

High-priority context debt:
- `company/product.md` has an outdated buyer, wedge, or product promise.
- `company/product-marketing.md` does not match the current ICP, channel, offer, or proof.
- The public website, onboarding flow, pricing page, or demo contradicts `company/product-marketing.md`.
- The product is launched but there is no current traffic, activation, revenue, search, or churn summary.
- Customer conversations happened but are not stored under `company/customers/`.
- `company/ideas/` contains implementation-ready-looking ideas without buyer/proof notes.
- The coach log has commitments but no follow-up status.

Output a short `Company Context Updates` section:

- `Update now`: files that should change before more product work.
- `Append later`: notes that can be added after the current task.
- `Missing evidence`: customer/marketing/revenue artifacts the repo lacks.

## Customer Evidence

Customer transcripts and notes belong in `company/customers/`.

Preferred naming:

`YYYY-MM-DD-customer-or-segment-topic.md`

Extract from transcripts:

- Buyer/user role.
- Current workaround.
- Pain language in the customer's own words.
- Trigger event.
- Budget or willingness to pay.
- Objections.
- Follow-up commitment.
- Product implications.

## Public Surface Evidence

Use `company/public-surface.md` when repeated landing/onboarding audits would help future agents. Keep it short and current.

Useful sections:

- Live URL or route.
- Current headline, subhead, CTA, and pricing entry point.
- Intended aha moment.
- Main proof shown publicly.
- Signup-to-activation path.
- Known conversion or activation metrics.
- Open public-surface gaps.

If the actual website is weaker than the internal positioning, say so directly and recommend a public-surface fix before more feature work.

## Metrics Evidence

Use `company/metrics.md` only when a short snapshot would help future agents avoid guessing.

Useful sections:

- Current MRR/revenue stage.
- Traffic source and volume.
- Signup, activation, trial, payment, and churn signals.
- Search impressions/clicks, indexed pages, backlinks, or rankings when SEO matters.
- Top funnel leak.
- Current growth bet.
- Data source and date.

Keep it concise. Do not create a metrics file just because a product exists; create it when the metric snapshot changes what to build, sell, fix, or cut.

## Ideas Gatekeeping

Treat `company/ideas/` as intake, not roadmap.

Before recommending implementation, require:

1. Buyer: who specifically wants this?
2. Painful job: what are they doing today?
3. Paid wedge: what is the smallest version worth paying for?
4. Proof: customer note, transcript, support issue, search demand, repeated request, payment, or pilot.
5. MRR path: how this changes conversion, ARPA, retention, activation, or distribution.
6. Scope: what can be manual, mocked, or deferred?

If evidence is missing, recommend validation work instead of implementation.

Promotion rule:
- `company/ideas/` item -> validation task -> customer/revenue/market proof -> scoped implementation.
- Do not skip straight from idea to build unless the evidence gate passes.

## Update Behavior

When the user asks for coaching:

- Log the coaching session by default when inside a repo.
- Recommend specific `/company` updates when stale context would mislead future agents.
- If context is stale and the user asked for a plan, include the exact proposed `/company` update in the answer.
- If the user asks to update docs, keep edits concise and append dated notes where possible.
- Do not rewrite customer transcripts.
- Do not promote an idea to implementation without passing the gate.
