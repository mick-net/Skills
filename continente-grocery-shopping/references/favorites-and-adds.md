# Favorites And Adds

Use this file when the task is about repeat purchases, favorites-first matching, or adding items to the cart/list.

## Favorites-first rule

If the user asks to add a broad product they may already buy (`chicken`, `beef`, `eggs`, similar staples), check favorites first when that is likely helpful.

Search favorites using Portuguese names.

## Ambiguity rule

Do not guess when multiple plausible products match.

Ask a short clarifying question instead.

Example:
- `add chicken` may match multiple favorites such as `Bifes de Frango`, `Peito de Frango`, `Lombinhos de Frango`, `Bifes de Frango Extrafino`.

## Add confirmation rule

After clicking `Comprar` or `Adicionar ao carrinho`, confirm success by checking that quantity controls appear.

Tell the user the exact item added and the quantity.

## Useful site patterns

- Favorites: `https://www.continente.pt/conta/lista-produtos/?list=favorites`
- Search pattern: `https://www.continente.pt/pesquisa/?q=<term>&start=0&srule=Continente%2004&pmin=0.01`
- Product pages contain a useful trailing numeric ID in the slug.
- Logged-in favorites may expose raw IDs via `Wishlist-GetProductIds`, but prefer live site reads over storing giant static product lists.

## Tested example: chicken from favorites

Behavior that worked:
- inspect favorites for `frango`
- detect ambiguity when multiple chicken products exist
- ask which one the user wants
- add only after clarification
