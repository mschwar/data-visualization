# AGENTS

## How To Orient In This Repo

Start with `CURRENT_STATE.md` for the current audit summary, then read `docs/agentic-first-buildout-plan.md` for the branch/PR/QA loop, then read `README.md` for the public-facing intent. The canonical site content lives in `index.md`, the site metadata lives in `_config.yml`, and the primary visualization asset is `oral-health-heatmap.png`.

## Canonical Source-Of-Truth Files

- `CURRENT_STATE.md`: current repository truth and known risks
- `docs/agentic-overhaul/2026-05-audit.md`: fuller audit, maturity scores, and backlog
- `README.md`: public overview of the project
- `index.md`: rendered GitHub Pages content
- `_config.yml`: site title, description, and theme config
- `Gemfile` and `.ruby-version`: pinned local Jekyll toolchain
- `assets/css/style.scss.css`: hand-authored site styling
- `oral-health-heatmap.png`: published visualization asset
- `Figure2-Teeth_v4.1.pdf`: committed source figure for the PNG
- `scripts/render_heatmap.py`: source-to-raster rebuild script
- `scripts/check_homepage.py`: homepage smoke test script
- `docs/heatmap-provenance.md`: provenance and rebuild notes

## Commands To Run Before And After Changes

Before changes:

- `git status --short`
- `python scripts/validate_repo.py`
- `python scripts/render_heatmap.py` if you touch the heatmap source artifact or rebuild notes
- `python scripts/check_homepage.py` if you touch the homepage render or nav

After changes:

- `python scripts/validate_repo.py`
- `bundle exec jekyll build`
- `git status --short`

The repo now pins the local Jekyll toolchain with `Gemfile` and `.ruby-version`. Do not claim build parity unless you have run the pinned build command successfully.

## Generated Vs. Hand-Authored Files

Hand-authored:

- `README.md`
- `index.md`
- `_config.yml`
- `Gemfile`
- `.ruby-version`
- `assets/css/style.scss.css`
- `CURRENT_STATE.md`
- `docs/agentic-overhaul/2026-05-audit.md`
- `AGENTS.md`
- `docs/heatmap-provenance.md`
- `docs/agentic-first-buildout-plan.md`
- `scripts/render_heatmap.py`
- `scripts/check_homepage.py`

Generated or historical artifact:

- `README.CRAWL.md`: historical crawl output with stale machine-local metadata; do not treat as canonical truth

## Data, Citation, And Provenance Rules

- Do not invent dataset provenance, participant counts, or publication claims beyond what is already supported in committed files.
- If you add provenance notes, tie them to already-present citation material or newly committed source artifacts.
- If the image can be regenerated, document the real pipeline; do not guess at unpublished steps.
- Keep the source PDF and rebuild script in sync with `oral-health-heatmap.png`.

## Accessibility And Documentation Expectations

- Preserve meaningful alt text for the main image and any future visual assets.
- Keep README and `CURRENT_STATE.md` aligned when commands or repo structure change.
- Favor small, explicit documentation updates over implied behavior.

## Safe-Change Rules

- Keep the repo lightweight; avoid introducing heavy tooling unless the site grows.
- Do not hand-edit generated artifacts if a real generator is introduced later.
- Prefer edits that preserve GitHub Pages compatibility.
- Avoid deleting historical artifacts unless their role is documented and the removal is clearly safe.

## Known Project-Specific Traps

- `README.CRAWL.md` includes stale machine-local paths and a directory count from another environment.
- The repo now pins the Jekyll toolchain, so local Pages rendering can be verified once Ruby is installed.
- The visualization image is committed, and the committed source PDF plus rebuild script provide the regeneration path.
