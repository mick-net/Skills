# GStack Skill Map

Use this when a solo-founder task could benefit from GStack-style workflows. GStack is an execution/planning accelerator, not the founder strategy layer. Prefer the embedded workflows in `references/gstack-playbooks.md`; use external `gstack-*` skills only when the user explicitly invokes them or wants that workflow isolated.

If these skills are missing, keep using the embedded playbooks. For source/install pointers, see `references/optional-skill-sources.md`.

## Gate Before GStack

Use GStack-style workflows only after answering:

1. Who is the buyer?
2. What painful job are they doing today?
3. What is the smallest paid wedge?
4. What marketing/sales proof exists?
5. Would this work move MRR, activation, retention, or distribution?

If these answers are weak, stay in `solo-founder-growth`, `gstack-office-hours`, `lenny-founder-sales`, or `lenny-conducting-user-interviews` before engineering planning.

When inside a repo, inspect `/company` context before asking these questions.

## Routing

- Idea validation -> use embedded Office Hours in `references/gstack-playbooks.md`; optionally suggest `gstack-office-hours`.
- Scope challenge -> use embedded CEO Plan Review in `references/gstack-playbooks.md`; optionally suggest `gstack-plan-ceo-review`, but default to `SCOPE_REDUCTION`.

## How GStack Overlaps Lenny

### `gstack-office-hours`

Overlaps:
- `lenny-problem-definition`
- `lenny-conducting-user-interviews`
- `lenny-startup-ideation`
- `lenny-working-backwards`

Best use:
- Fast, blunt pressure-test before code.
- Good when the user has an idea but no proof.
- Better than Lenny when the founder needs direct challenge and narrowest paid wedge.

Lenny is better when:
- The user needs interview scripts or deeper customer discovery.
- The user needs structured problem framing without YC-style pressure.

### `gstack-plan-ceo-review`

Overlaps:
- `lenny-scoping-cutting`
- `lenny-prioritizing-roadmap`
- `lenny-working-backwards`
- `lenny-product-led-sales` when scope touches PLG expansion.

Best use:
- Reviewing a concrete implementation plan.
- Forcing alternatives: minimal viable vs ideal architecture vs do-not-build-yet.
- Cutting scope before an engineering sprint.

Lenny is better when:
- The problem is mostly product process or roadmap prioritization.
- There are many stakeholder/customer signals to rank.
- The user needs less "CEO taste" and more methodical framework.

## Recommendation For This User

Default hierarchy:

1. `solo-founder-growth`: operating system and brutal coach.
2. Embedded GStack Office Hours: idea/wedge pressure test.
3. `lenny-founder-sales` or `lenny-conducting-user-interviews`: get buyer evidence.
4. Embedded GStack CEO Plan Review: review/cut implementation scope after evidence.
5. `lenny-scoping-cutting`: extra depth if scope is still bloated.

Blunt rule:
If there is no buyer, no painful job, no paid wedge, and no marketing/sales proof, `gstack-plan-ceo-review` is premature. Use `gstack-office-hours` or sales/interview skills first.
