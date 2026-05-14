---
name: marketing-use-case-pipeline
description: Create reusable marketing use-case packs from real workflows. Use when researching a workflow, defining a source pack, generating synthetic workspaces, validating agent output, writing article briefs, or preparing screenshots/videos/blog posts without leaking private project details.
---

# Marketing Use-Case Pipeline

Turn a real workflow into a credible, reusable marketing use-case pack. Treat validation as the first goal and marketing production as the second.

## Core Rule

Do not create public claims from a scripted demo alone. Preserve enough evidence to prove the workflow, sources, and output are credible.

## Workflow

1. Define the pack: target persona, workflow, pain point, desired output, source-quality bar, and claim boundary.
2. Research the workflow and current pain points. Use official/public sources for regulated domains and record access dates.
3. Build a source-artifact plan. Prefer real downloadable public files. Capture useful web pages as clean PDFs when that is how a user would work with them.
4. Define the output contract before writing the scenario prompt. Include stable output filename, report title, likely sections, quality expectations, and optional short video labels.
5. Generate a realistic synthetic workspace with non-sensitive fictional files in natural formats such as PDF, DOCX, XLSX, Markdown, CSV, or images.
6. Decide whether an in-app or agent skill is appropriate. If yes, make it workflow guidance, not an answer key.
7. Run a baseline real-agent pass and, when relevant, a skill-assisted pass.
8. Preserve outputs and compact traces. Use traces as evidence for what the agent actually did.
9. Run output review and domain/workflow review from saved artifacts.
10. Decide: publish, iterate workspace, iterate prompt, revise/remove skill, promote to benchmark, or hand off to engineering.
11. Define the SEO-facing article brief before writing public content.
12. Only after review passes, create screenshots, videos, docs, or blog material.
13. Record reusable lessons in the pack README or reference notes.

## Public Brand And Copy

Choose the public brand before writing copy, overlays, file names, or article metadata.

- Use the niche brand for niche/domain use cases.
- Use the general product brand for general use cases.
- Keep visible brand names and spoken narration natural. If a written brand contains punctuation, write narration phonetically so text-to-speech does not read punctuation awkwardly.

## Output Contract

Each pack should define:

- `outputFile`: file the user asks the agent to create.
- `title`: visible report title.
- `sections`: expected section headings or aliases.
- `videoLabels`: optional short labels for captures or chapters.
- `reviewCriteria`: evidence-backed findings, caveats, missing-evidence calls, practical next actions, and source traceability.

The output contract is a shape, not an answer key.

## Blog And SEO Brief

Before writing a post, define:

- `reader`: who is searching and why.
- `problem`: the painful task.
- `targetQueries`: realistic buyer search phrases.
- `title`: human-readable promise tied to the query.
- `slug`: short and search-intent based.
- `description`: one sentence with workflow and outcome.
- `whatItSolves`: practical improvement.
- `termsToAvoidInTitle`: internal pipeline terms unless buyers use them.

End each post with a short "How <brand> can help" section tied to the specific workflow. Avoid overclaiming regulated, legal, medical, financial, or compliance outcomes.

## Artifact Retention

Commit the parts needed to recreate the asset:

- use-case README, research brief, workspace plan, output contract, article brief, rubrics, domain skill, non-sensitive generation scripts;
- public article Markdown/MDX and lightweight website metadata;
- video composition source, design notes, voiceover script text, and manifests.

Do not commit bulky or run-specific artifacts by default:

- raw recordings, rendered videos, generated audio, frame snapshots, temporary capture folders, traces from normal iterations, or source bookkeeping files that do not belong in the user-facing workspace.

Publish selected final media to object storage/CDN when needed and record public URL, source path, content type, checksum, and upload date.

## References

- Domain skill boundaries: [references/domain-skill-boundaries.md](references/domain-skill-boundaries.md)
- Trace review: [references/trace-review.md](references/trace-review.md)
