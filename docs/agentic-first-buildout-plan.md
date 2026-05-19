# Agentic-First Buildout Plan

This repository is best advanced in a two-prompt loop:

1. Prompt A: create one feature branch, implement exactly one feature, commit, and push.
2. Prompt B: QA that same branch in the browser or with an explicit non-UI check, update docs, commit, push, and merge.

## Operating Contract

- One feature equals one branch equals one PR.
- Each branch must be independently mergeable.
- Each feature must have a single verification path:
  - Browser verification for UI-facing work.
  - An explicit non-UI command for infrastructure, docs, or render-only work.
- The next agent must be able to continue from repository files alone.
- Every feature branch must update the handoff notes in `CURRENT_STATE.md`.
- Every PR must include:
  - What changed.
  - How it was verified.
  - What docs were updated.
  - What the next feature is.

## Feature Packet Template

Use this structure for every branch:

- Branch name: `feat/<short-slug>`
- Scope: one feature only
- Verification: one command or one browser session
- Docs: update the relevant source-of-truth docs
- Handoff: add a short "Next" note to `CURRENT_STATE.md`
- PR body: include verification evidence and the next feature pointer

## Buildout Sequence

The baseline reproducibility work is already in place:

- Pinned Jekyll/Ruby toolchain
- Source PDF and heatmap regeneration script
- Public-site exclusions for repo-only files
- CI validation plus local repo validation

Start the remaining buildout here:

### 1. Browser smoke test for the home page

- Status: merged to main.
- Goal: add a browser-driven verification path that opens the local site, checks the title, the main heatmap image, the download link, and the image alt text.
- Merge boundary: the test harness and its docs only.
- Verification: browser screenshot or a scripted browser run against the local preview.
- Why first: it gives every later feature a stable visual baseline.

### 2. Responsive polish pass

- Status: merged to main.
- Goal: harden the layout for mobile and small laptop widths without changing content.
- Merge boundary: CSS and minimal markup only.
- Verification: browser screenshots at desktop and mobile breakpoints.
- Why second: it keeps later content changes from conflating with layout regressions.

### 3. Historical artifact governance

- Status: next.
- Goal: decide the final treatment of `README.CRAWL.md` and any other historical artifacts.
- Merge boundary: docs and navigation only.
- Verification: non-UI validation plus live site check that the artifact is not surfaced publicly.
- Why third: it resolves repo hygiene after the public experience is stable.

### 4. Provenance refinement

- Goal: tighten the provenance story around the source PDF, the published PNG, and any constraints on regeneration.
- Merge boundary: documentation only.
- Verification: non-UI link/file validation.
- Why fourth: it depends on the regeneration path already being committed.

### 5. Deployment check or badge

- Goal: add a lightweight live-deploy indicator or a Pages verification step if the repo still needs one.
- Merge boundary: CI/docs only.
- Verification: explicit non-UI command or GitHub Actions status.
- Why last: deployment checks are most useful after the content and verification paths are stable.

## Handoff Rules

- Keep the plan discoverable by updating `CURRENT_STATE.md` when the next feature changes.
- Avoid mixing two features into one PR, even if they are related.
- If a feature needs both browser and non-UI verification, split it until each PR has one primary verification mode.
- If a later branch depends on an earlier branch, merge the earlier branch first and update the plan doc.
