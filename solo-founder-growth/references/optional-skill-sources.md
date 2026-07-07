# Optional Skill Sources

Use this only when the agent suggests an external/deeper skill and the user or environment may not have it installed. `solo-founder-growth` must still work without these skills because the important solo-founder playbooks are embedded in this skill.

## Rule

- Do not block on missing optional skills.
- Use embedded references first.
- Suggest or install an external skill only when the bottleneck is specific and the user wants deeper structure.
- If a skill is unavailable, continue with the closest embedded playbook.

## This Skill Repo

Source:
- `https://github.com/mick-net/Skills`

Known bundled skills in this repo:
- `solo-founder-growth`
- `gstack-office-hours`
- `gstack-plan-ceo-review`

Use this repo when another agent needs the Codex-native solo-founder skill or the small GStack wrappers used by this setup.

## GStack

Source:
- `https://github.com/garrytan/gstack`

Relevant upstream skills:
- `office-hours`
- `plan-ceo-review`

Example install patterns, depending on agent/runtime:
- `npx skills add https://github.com/garrytan/gstack --skill office-hours`
- `npx skills add https://github.com/garrytan/gstack --skill plan-ceo-review`
- Full Claude Code setup is documented in the upstream repo.

Solo-founder usage:
- Use `office-hours` for idea/wedge pressure.
- Use `plan-ceo-review` for scope challenge after buyer/pain/paid-wedge/proof are clear.
- Prefer `references/gstack-playbooks.md` if GStack is not installed.

## Lenny Skills

Source:
- `https://github.com/RefoundAI/lenny-skills`

Relevant upstream skill names:
- `founder-sales`
- `conducting-user-interviews`
- `analyzing-user-feedback`
- `problem-definition`
- `scoping-cutting`
- `positioning-messaging`
- `launch-marketing`
- `content-marketing`
- `user-onboarding`
- `pricing-strategy`
- `retention-engagement`
- `product-led-sales`
- `competitive-analysis`
- `ai-evals`

Example install pattern:
- `npx skills add https://github.com/RefoundAI/lenny-skills --skill founder-sales`

Naming note:
- Some local Codex installs prefix these as `lenny-founder-sales`, `lenny-user-onboarding`, etc.
- Upstream install names usually omit the `lenny-` prefix.

Solo-founder usage:
- Use these for deeper structure only after applying the solo-founder filter.
- Avoid org-heavy or VC-scale parts unless the product is actually at that stage.
- Prefer `references/lenny-solo-playbooks.md` if Lenny skills are not installed.

## Minimalist Entrepreneur Skills

Source:
- `https://github.com/slavingia/skills`

Relevant skills:
- `find-community`
- `validate-idea`
- `mvp`
- `first-customers`
- `pricing`
- `marketing-plan`
- `grow-sustainably`
- `minimalist-review`

Example install patterns, depending on agent/runtime:
- `claude install-skill https://github.com/slavingia/skills`
- In Claude Code plugin mode, use the upstream plugin marketplace instructions.
- For other agents, copy only the needed skill folder or `SKILL.md` into the agent's skills directory.

Solo-founder usage:
- Use mostly for `still-building/prelaunch`, `launched/no revenue`, and `first paying customers / $1-$1k MRR`.
- `find-community`: no reachable community/channel.
- `validate-idea`: idea needs sell-before-build validation.
- `mvp`: scope must shrink to manual, no-code, or weekend-sized delivery.
- `first-customers`: next bottleneck is one-by-one sales.
- `pricing`: early paid boundary or first price.
- `marketing-plan`: use later, after real customers; do not use as a substitute for first sales.
- `grow-sustainably` and `minimalist-review`: useful for spending, hiring, or scope gut-checks.

## SEO / pSEO / Ads Deep Dives

Use external SEO, pSEO, AI-search, DataForSEO, or paid-ads skills only when:

- the search-demand gate in `seo-demand-validation.md` passes;
- the founder has a real page pattern, data source, tool, integration, example, template, or proof asset;
- the next bottleneck is implementation detail, not buyer proof;
- the user explicitly wants deeper SEO, AI-search, keyword-data, or paid-ads execution.

Useful deeper skills when installed:

- `seo-audit`: technical crawlability, indexation, on-page, schema, speed, sitemap, Search Console, and SEO health checks.
- `google-ai-seo-writing`: article/content briefs, people-first Google AI Search writing, non-commodity content, and avoiding AI-search hacks.
- `ai-seo`: AI search/AEO/GEO/LLMO diagnostics and source visibility when the product already has useful public assets.
- `dataforseo`: keyword volume, CPC, SERP, competitor, and backlink data via API when a data-backed decision is needed.
- `paid-ads`: small Google Ads or paid-channel validation tests when the founder has a clear query, promise, CTA, and conversion event.
- `schema-markup`: structured data only when it supports a real rich-result or product/business clarity use case.

Do not route to deeper SEO skills for pre-revenue founders who lack buyer, painful job, paid boundary, or reachable channel. Continue with `community-reachability.md`, `public-surface-onboarding.md`, warm outbound, or a manual paid offer instead.

## Portable Fallback

If none of these external skills are installed, use this order:

1. `community-reachability.md`
2. `gstack-playbooks.md`
3. `lenny-solo-playbooks.md`
4. `product-scope.md`
5. `public-surface-onboarding.md`
6. `metrics-growth-diagnosis.md`

Then give the user a `What to do now` and `What to do this week` plan.
