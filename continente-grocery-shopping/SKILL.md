---
name: continente-grocery-shopping
description: Search, compare, and add grocery and household products on Continente.pt using the browser tool. Use when the user wants help with Continente grocery shopping, favorites, product search, product comparison, ingredient/detail lookup, cart additions, or Portuguese product discovery from English requests. Especially useful when the user asks in English but the site should be searched in Portuguese (EU), when favorites should be checked first for likely matches, or when ambiguous product types need clarification before adding.
---

# Continente Grocery Shopping

Use the browser tool on `continente.pt` to search products, inspect favorites, compare options, and add chosen items to the shopping cart/list.

## Core rules

- Talk to the user in English.
- Search Continente using Portuguese (EU) terms.
- Prefer Continente brand options when value looks good, but still show relevant alternatives.
- Do not guess when a vague request maps to multiple plausible products; ask.
- Confirm adds by checking that the UI switches from `Comprar` / `Adicionar ao carrinho` to quantity controls.
- If login is required and credentials are not already available in trusted context or memory, ask the user to provide them in chat or store them in a private local file / environment-backed secret source before proceeding.
- This skill uses the browser tool, so a supported browser must be installed; Playwright browser support is recommended. See: https://docs.openclaw.ai/tools/browser#playwright-requirement

## Workflow

### 1) Choose the starting point

- If the user asks to **add a broad product they may already buy**, check favorites first.
- If the user asks to **discover, compare, or inspect products**, search the site directly.
- If the user gives a **specific product name or ID**, go straight to search or the product page.

For favorites-first behavior, add-confirmation rules, and tested repeat-purchase patterns, read [references/favorites-and-adds.md](references/favorites-and-adds.md).

### 2) Search in Portuguese, reply in English

Translate the user request into concise PT-PT terms, then filter results down to the relevant products.

For search-term examples, filtering guidance, reply formatting, and tested comparison patterns, read [references/lookup-patterns.md](references/lookup-patterns.md).

### 3) Ask before guessing

If multiple plausible products match, ask the shortest clarifying question that resolves the ambiguity.

### 4) Add and verify

Click the chosen product's add button and confirm success by checking for quantity controls.

## When to open product details

Open the product page when the user needs:
- ingredients
- nutrition
- product details/specs
- disambiguation between similar products
- confirmation that a search result is the right item

## Output style

Keep it concise and practical:
- lead with the answer
- show only the useful options
- include the Portuguese term briefly so the user learns it
- recommend one when appropriate
- ask only the minimum clarification needed
