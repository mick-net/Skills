---
name: marketing-capture
description: Create or refresh real product marketing screenshots and demo videos from deterministic browser, desktop, or app scenarios. Use after a use-case pack is credible enough to record and when assets must be reused in docs, blog posts, landing pages, or launch material.
---

# Marketing Capture

Use this skill for real product marketing assets. Prefer deterministic app captures over generated mock UI when the marketing claim depends on real behavior.

If the use case, source corpus, synthetic workspace, output rubric, or review loop is still being designed, use a marketing use-case pipeline first.

## Inputs To Read

Look for project-local equivalents of:

- product/design language;
- asset hosting or CDN notes;
- visual demo harness docs;
- relevant docs/blog/landing-page files;
- the use-case pack README, output contract, and review report.

## Capture Workflow

1. Smoke-run the scenario without video after changing scenario logic.
2. Run the full capture command at the final viewport/resolution.
3. For publishable real-agent captures, preserve the generated output and compact trace.
4. Run output or domain review when claims are specialized or regulated.
5. Decide next action from review evidence before changing app behavior.
6. For clean static screenshots, rerun with cursor, teaching overlays, and debug UI disabled.
7. Inspect screenshots and video before using them.
8. Copy selected final assets to stable local filenames for review.
9. Upload selected public assets to object storage/CDN if the website should not bundle them.
10. Verify public URLs.
11. Reference verified URLs in public pages.
12. Run the docs/site build after content changes.

## Video Guidance

For polished public videos, prefer two stages:

1. Record a clean raw app video with few or no in-app instruction bubbles.
2. Use a video composition tool to add a marketing cover, chapter overlays, captions, voiceover, targeted zooms, and background music.

Preserve a timeline artifact when possible. It should include prompt typing, send, follow/open events, write start/end, and checkpoint timings. Use it for narration timing instead of guessing from trace order.

Keep the default view zoomed out so viewers understand the whole app. Use restrained, steady zooms only for specific beats. If zooming beyond roughly 1.15-1.25x, record above final delivery resolution and render down to the final size.

Prefer segmented voiceover clips over one continuous narration track:

- opening cover;
- prompt typing;
- agent source inspection;
- generated output;
- closing value statement.

## Capture Hygiene

- Do not capture private customer data, credentials, inboxes, or personal workspaces.
- Keep visible prompts natural. Prefer file tags or friendly names over internal paths when the UI supports it.
- Hide pipeline manifests, traces, fixture metadata, and source bookkeeping outside the visible demo workspace.
- Instruction bubbles should explain the user's workflow, not the harness.
- Keep overlays readable at final video size.
- Use a real model or real backend for publishable workflow evidence when the claim depends on authentic behavior.
- Keep raw recordings and final rendered video out of git unless there is a deliberate publication reason.

## Asset Publishing

For public sites, large videos should usually live on object storage/CDN rather than in the website repository.

Record an asset manifest with:

- source path;
- storage key;
- public URL;
- MIME type;
- checksum;
- upload date;
- verification status.

Do not print or commit secrets. Check for required environment variables before declaring publishing blocked.
