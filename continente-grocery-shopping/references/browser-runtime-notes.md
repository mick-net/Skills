# Browser Runtime Notes

Use this only when Continente account pages behave differently from public product pages, especially when favorites, cart, checkout, or payment/account routes keep bouncing back to login wrappers.

## Browser requirement

This skill uses the browser tool and works better when a supported browser is installed with Playwright browser support.

Docs:
- https://docs.openclaw.ai/tools/browser#playwright-requirement

## What helped in this environment

The logged-in Continente flow became materially more reliable after the managed browser was adjusted to look more like a normal local browser:

- run headed instead of headless
- use a normal desktop window size (example: 1440x900)
- use a standard Chrome-on-Linux user agent instead of exposing `HeadlessChrome`
- use Portugal time zone (`Europe/Lisbon`)
- run Chromium in a way that supports headed mode inside the container (for example via Xvfb)

Observed good signs after the change:
- browser status reported `headless: false`
- user agent looked like normal Chrome instead of `HeadlessChrome`
- `webdriver` reported `false`
- time zone matched `Europe/Lisbon`
- public Continente search pages still loaded normally
- favorites/account login flow started working again

## What to infer

If public product pages work but logged-in account routes fail, treat it as a browser/session fingerprinting or fragile login-flow problem before assuming the site is fully down.

## Caveat

Locale emulation may still be imperfect (for example JS-visible language may remain `en-US`), but removing the obvious headless/browser-fingerprint signals can still be enough to fix the account flow.
