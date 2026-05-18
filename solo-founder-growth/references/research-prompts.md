# Research Prompts

Use this when the user asks for X, Grok, Google AI, Perplexity, or YouTube prompts to study solo founders.

## X Research Guardrails

Before turning a post into a tactic:

- Read the full thread, not just the isolated post.
- Check replies and quote-tweets for sarcasm, jokes, corrections, or community context.
- Separate literal advice from satire, memes, rage-bait, and motivational shorthand.
- Mark every lesson as `confirmed`, `inferred`, or `discarded`.
- Prefer repeated serious claims over one-off viral posts.
- Do not add a tactic to the skill if it only works because the founder already has a large audience, reputation, or unusual network.

## Universal Grok Prompt

```text
Research @HANDLE as a solo/bootstrapped founder. Use their X posts, replies, launch posts, revenue posts, interviews linked from X, and product pages.

Extract:
1. Their repeatable founder methods for marketing, simplicity, growth, pricing, product scope, and distribution.
2. 20 high-signal X posts with URLs, dates, and why each matters.
3. Their launch playbook: where they launched, how they wrote the launch post, what proof they used, and what CTA they used.
4. Their monetization playbook: pricing, free/paid boundary, one-time vs subscription, enterprise vs self-serve.
5. What a solo founder should copy.
6. What a solo founder should NOT copy.
7. How this differs from VC-backed startup advice.
8. Which posts are jokes/sarcasm/memes and should NOT be treated as advice.

Output as a tactical playbook, not biography. Be skeptical, read full thread context, and cite evidence.
```

## Comparison Prompt

```text
Compare @yasser_elsaid_, @levelsio, @marclou, @tdinh_me, @yongfook, @damengchen, @arvidkahl, @dannypostmaa, @dvassallo, and @IronBrands16 as solo/bootstrapped founders.

Create a distilled solo-founder skill/playbook with:
1. Shared principles.
2. Where they disagree.
3. Stage-specific tactics: pre-revenue, first $1K, first $10K MRR, $100K+/mo.
4. Marketing tactics that do not require a team.
5. Product simplicity rules.
6. Pricing rules.
7. Launch templates.
8. Anti-patterns and survivorship-bias warnings.
9. A 30-day action plan for a technical solo founder.
10. Any posts that are sarcastic or context-dependent and should be excluded.

Use X posts as evidence and include tweet URLs.
```

## Brutal Coach Prompt

```text
Act as a brutally direct solo-founder coach inspired by Pieter Levels, Jon Yongfook, Tony Dinh, Yasser Elsaid, Marc Lou, Damon Chen, Arvid Kahl, Danny Postma, Daniel Vassallo, and Iron Brands.

I am a technical founder. Audit whether I am overbuilding instead of validating, selling, and marketing.

Ask for or inspect:
1. Last 10 git commits or shipped changes.
2. Current product one-liner.
3. Pricing/checkout status.
4. Customer conversations from the last 14 days.
5. Marketing/content/outbound done in the last 14 days.
6. Current MRR, trials, activation, churn, and top support issues.

Give me:
- Hard read.
- What I am avoiding.
- What to stop building.
- What to ship/sell/ask by next week.
- The single metric that matters this week.
```

## X Search Patterns

Yasser:
- `from:yasser_elsaid_ Chatbase ARR`
- `from:yasser_elsaid_ pricing`
- `from:yasser_elsaid_ churn`
- `from:yasser_elsaid_ "self serve"`
- `from:yasser_elsaid_ "sales team"`
- `from:yasser_elsaid_ Shopify OR Vercel OR Stripe`

Pieter:
- `from:levelsio "12 startups"`
- `from:levelsio "paid validation"`
- `from:levelsio "PHP" OR "SQLite" OR "jQuery"`
- `from:levelsio PhotoAI revenue OR MRR`
- `from:levelsio RemoteOK revenue OR MRR`
- `from:levelsio "ship" "revenue"`

Marc:
- `from:marclou ShipFast launch`
- `from:marclou CodeFast "$" OR revenue`
- `from:marclou DataFast MRR OR "120 days"`
- `from:marclou TrustMRR`
- `from:marclou "Product Hunt"`
- `from:marclou "build in public"`

Tony:
- `from:tdinh_me TypingMind launch`
- `from:tdinh_me TypingMind revenue`
- `from:tdinh_me "one-time" OR "lifetime"`
- `from:tdinh_me "Product Hunt"`
- `from:tdinh_me "Black Magic" API`
- `from:tdinh_me "B2B" OR "enterprise"`

Jon:
- `from:yongfook Bannerbear MRR`
- `from:yongfook "50% coding" OR "50:50"`
- `from:yongfook "marketing"`
- `from:yongfook "free tools"`
- `from:yongfook "Jobs to be Done"`
- `from:yongfook "Charge More"`
- `from:yongfook "$1k MRR"`
- `from:yongfook "lifetime deals"`

Others:
- `from:damengchen Testimonial MRR`
- `from:arvidkahl FeedbackPanda MRR audience research`
- `from:dannypostmaa HeadshotPro revenue`
- `from:dannypostmaa Headlime sold`
- `from:dvassallo "1 net new customer"`
- `from:dvassallo "everything is marketing"`
- `from:IronBrands16 "first $1k"`
- `from:IronBrands16 "500k ARR"`

## Sarcasm Check Prompt

```text
Re-check these X posts before I treat them as founder advice.

For each URL:
1. Read the full thread and replies.
2. Decide whether it is literal advice, sarcasm, a joke, rage bait, or context-dependent.
3. If literal, extract the actual transferable tactic.
4. If not literal, say "discard" and explain why.
5. Return only tactics that a technical solo founder can safely apply.
```
