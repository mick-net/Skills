---
name: gstack-office-hours
description: Codex-native adaptation of Garry Tan's GStack /office-hours idea-validation workflow. Use when the user has a product idea, feature idea, startup concept, side project, or asks whether something is worth building. Pressure-test demand reality, status quo, desperate specificity, narrowest paid wedge, observable user behavior, and future-fit before planning or coding.
---

# GStack Office Hours

This is a concise Codex adaptation of the public `garrytan/gstack` `/office-hours` workflow. Preserve the useful YC-style forcing questions; do not import Claude-specific tooling, telemetry, or routing behavior.

## Default Mode

Use startup mode unless the user explicitly says this is just for learning, fun, open source, or a hackathon.

Startup mode is direct:
- Seek evidence of demand, not enthusiasm.
- Reduce the idea to the narrowest paid wedge.
- Challenge vague personas, vague pain, and future-tense buyer claims.
- End with a build / do-not-build / validate-first recommendation.

When inside a repo, inspect `/company` context before asking questions:
- `company/product.md`
- `company/product-marketing.md`
- `company/ideas/`
- `company/customers/`
- `company/coach/solo-founder-growth-coach.md`

If the idea comes from `company/ideas`, treat it as intake, not roadmap.

## Six Forcing Questions

Ask or answer these with the evidence available:

1. **Buyer**: Who is the specific buyer or user by role, situation, and urgency?
2. **Status quo**: What are they doing today without this product?
3. **Pain**: What makes the current way expensive, slow, risky, embarrassing, or painful?
4. **Desperate specificity**: Which subgroup has the problem badly enough to act now?
5. **Smallest paid wedge**: What is the smallest version someone could pay for this week?
6. **Observation**: What behavior proves demand: payment, repeated use, workaround, manual process, public complaint, support ticket, search volume, or committed pilot?

## Solo-Founder Bias

Prefer:
- Paid pilot over waitlist.
- Manual service over speculative platform.
- One narrow buyer over broad market.
- Public demo over private polishing.
- Stripe/payment/invoice over "interested" feedback.

Flag:
- "Everyone could use this."
- "Once it has all features..."
- "I'll build the platform first."
- "People said it sounds cool."
- "The tech is the moat" before customer proof.

## Output

Use:

- `Hard Read`: whether the idea has demand evidence or is still wishful.
- `Narrowest Buyer`: who to target first.
- `Status Quo`: what they do now.
- `Smallest Paid Wedge`: what to sell or demo this week.
- `Validation Task`: the next 1-3 actions before more building.
- `Decision`: build now, validate first, cut scope, or drop.
- `Company Update`: what should be appended to `/company`.

## When To Hand Off

- If the idea passes demand checks and needs implementation scope, suggest `gstack-plan-ceo-review`.
- If the user needs sales/outreach, suggest `lenny-founder-sales`.
- If the user needs interviews, suggest `lenny-conducting-user-interviews`.
- If the user is overbuilding, suggest `solo-founder-growth` brutal coach mode.

Source inspiration: https://github.com/garrytan/gstack/tree/main/office-hours
