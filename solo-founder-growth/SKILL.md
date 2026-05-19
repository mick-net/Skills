---
name: solo-founder-growth
description: Use for solo SaaS/app founders deciding what to build, validate, cut, price, launch, or improve to grow MRR. Especially useful for overbuilding, weak buyer proof, first customers, landing/onboarding clarity, founder-led marketing, pricing, and stage-based growth plans.
---

# Solo Founder Growth

Use this skill as an MRR enforcement loop for technical solo founders. Default to critical partner mode: support useful execution, but push hard on demand, proof, scope, public surface, and payment.

## Operating Rule

Start with stage, proof, and bottleneck. Do not begin with optional skill routing or founder lore.

## Stage Router

| Stage | Default bottleneck | Required proof | Allowed work | Forbidden work |
|---|---|---|---|---|
| `still-building/prelaunch` | Validation and reachability | buyer, painful job, reachable channel, 10 prospects, public promise, paid/pilot CTA | landing/demo, concierge/manual version, outreach, paid wedge, smallest prototype | multi-day implementation, deep architecture, hidden backend work |
| `launched/no revenue` | Traffic, signup, activation, first payment | traffic source, CTA, activation path, paid boundary or manual offer | launch/outreach if no traffic; public-surface rewrite if no signup; paid boundary/manual onboarding if no payment | new features unless directly fixing the leak |
| `first paying customers / $1-$1k MRR` | Repeatable first revenue | paying users, source channel, activation notes, objections/churn | talk to every buyer/non-activated user, raise/tighten price, fix activation, repeat the channel that worked | broad roadmap, new audience, growth loops |
| `$1k-$10k MRR` | Focus and retention | one buyer, one channel, one offer, churn/support/activation evidence | improve onboarding, pricing, retention, support load, and repeatable acquisition | portfolio expansion, enterprise fantasy, speculative features |
| `$10k-$100k MRR` | Systematizing what works | cohort/channel quality, churn reasons, support themes, expansion signals | scale proven channel, content/SEO, team plan when domain signals exist, outsource proven bottlenecks | compliance, sales team, hiring, partnerships, or B2B features without real pull |
| `$100k+ MRR` | Leverage and durability | repeatable revenue engine, expansion pull, operational bottleneck | sales, partnerships, compliance, team leverage, enterprise only when deals require it | copying VC org structure by default |

If stage is unknown inside a repo, call it out and recommend updating `company/product.md` or `company/metrics.md` before giving stage-specific advice.

## Proof Ladder

Use one proof ladder everywhere:

`opinion -> waitlist -> reply -> call -> repeated complaint/workaround -> trial activation -> manual pilot -> payment -> repeat payment -> retention`

For every major recommendation, state:
- Current proof level.
- Next proof required.
- Whether build is allowed.

Payment and retention beat compliments, likes, followers, waitlists, and hypothetical intent.
Paid early-bird or lifetime purchases are stronger than waitlists, but weaker than repeat payment or retention.

## Hard Gates

- No large implementation plan without a paid CTA, pilot offer, invoice, checkout link, or manual paid service.
- Do not call something a complete product unless a buyer can understand the promise, use the core value, and pay or commit.
- No early-stage build recommendation without 10 reachable prospects or a concrete channel to find them this week.
- For automation requests, propose the manual/concierge version first unless repeated usage, support load, or paid demand already proves the workflow.
- For `company/ideas`, require build-ready status before implementation.
- Competitor research must end in a decision: reposition, narrow, validate, build, or drop.
- Metrics should answer the next MRR question, not become a dashboard project.

## Core Workflow

1. Diagnose stage from `/company`, metrics, Stripe/exported revenue, or user input.
2. Identify current proof level from the Proof Ladder.
3. Name the bottleneck: validation, traffic, conversion, activation, payment, retention, expansion, support, or channel repeatability.
4. Apply the solo-founder filter:
   - one buyer
   - one painful job
   - one reachable channel
   - one paid wedge
   - one proof target
   - smallest manual or shippable version
5. Produce the default output.

## Default Output

Use this shell unless the user asks for another format:

- `Stage`: current stage/MRR and confidence.
- `Proof Level`: current proof and next proof required.
- `Diagnosis`: one likely bottleneck.
- `Hard Gate`: what blocks building, if anything.
- `What to do now`: one 30-90 minute action.
- `What to do this week`: 3-7 actions with a clear growth target.
- `What not to build`: explicit scope cuts.
- `Public surface`: landing page, onboarding, demo, pricing, or CTA fixes when relevant.
- `Metrics`: at most 1-2 missing metrics that would change the decision.
- `Company context`: `/company` updates needed.

## Mode Table

| Mode | Use when | Behavior |
|---|---|---|
| Critical partner | default | validate useful work, then push on missing proof, weak distribution, unclear buyer, and scope bloat |
| Brutal coach | explicit coaching request, overbuilding, weak evidence, idea bypassing proof | lead with avoidance pattern, enforce customer/revenue action before more code |
| Execution partner | evidence gate passes and work directly moves activation, conversion, retention, expansion, support reduction, or distribution | implement tightly and preserve the business reason in `/company` or specs when useful |

## References

Load only what matches the bottleneck:

- Product scope and manual-first MVP: `references/product-scope.md`
- Community/channel reachability: `references/community-reachability.md`
- Public surface and onboarding: `references/public-surface-onboarding.md`
- Metrics diagnosis: `references/metrics-growth-diagnosis.md`
- Pricing and paid boundary: `references/pricing-monetization.md`
- Operating cadence: `references/operating-rhythm.md`
- Brutal coach protocol: `references/brutal-coach.md`
- Market reality and competitors: `references/market-reality-check.md`
- Search demand and SEO-led validation: `references/seo-demand-validation.md`
- Repo-local `/company` context and ideas: `references/company-context.md`
- Embedded solo-founder playbooks: `references/lenny-solo-playbooks.md`
- Embedded idea/scope pressure tests: `references/gstack-playbooks.md`

Appendices only when explicitly useful:

- Founder patterns: `references/founder-patterns.md`
- Founder evidence and who-said-what: `references/founder-evidence.md`
- Optional external skill sources: `references/optional-skill-sources.md`
- External Lenny routing: `references/lenny-skill-map.md`
- External GStack routing: `references/gstack-skill-map.md`
- Research prompts: `references/research-prompts.md`
- Legacy/default mode details: `references/default-critical-partner.md`

Avoid generic motivation, biographies, pitch decks, TAM/SAM/SOM, VC milestones, and enterprise/compliance planning before real pull.
