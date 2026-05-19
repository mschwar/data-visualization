# Current State

Audit date: 2026-05-19

## Purpose

This repository is a small GitHub Pages static site that publishes a single oral-health heatmap and explanatory narrative for the Tsimane population of Bolivia. The site is centered on one visualization asset (`oral-health-heatmap.png`), one page of written interpretation (`index.md`), and lightweight Jekyll/Minima configuration for deployment through GitHub Pages.

## Confirmed Working Pieces

- Core content files exist: `README.md`, `index.md`, `_config.yml`, `oral-health-heatmap.png`, and `assets/css/style.scss.css`.
- The site content includes descriptive alt text for the primary visualization.
- A committed `Gemfile` and `.ruby-version` pin the GitHub Pages toolchain for local builds.
- `Figure2-Teeth_v4.1.pdf` and `scripts/render_heatmap.py` provide a reproducible source-to-raster path for `oral-health-heatmap.png`.
- `scripts/check_homepage.py` provides a non-UI smoke test for the rendered homepage.
- A repo-local validation command now checks required files, local links, key config values, and tracked OS junk.
- The live GitHub Pages deployment returned HTTP 200 and served the expected page content in this session.

## QA Evidence

- A local homepage QA snapshot passed `python scripts/check_homepage.py` and was then captured at desktop and mobile widths in a browser-rendered view.
- The browser captures showed the heatmap image, page heading, and download link in the expected positions with no visible layout regressions.

## Existing Commands

| Command | Purpose | Result |
| --- | --- | --- |
| `python scripts/validate_repo.py` | Repo validation | Pass with warning about stale `README.CRAWL.md` |
| `python scripts/render_heatmap.py` | Heatmap rebuild | Produces the published 1700 x 2200 PNG from the committed PDF source at 200 DPI |
| `python scripts/check_homepage.py` | Homepage smoke test | Verifies the rendered homepage title, heading, heatmap image, alt text, download link, and the absence of README.CRAWL.html |
| `Invoke-WebRequest https://mschwar.github.io/data-visualization/` | Live site verification | 200 OK |
| `bundle exec jekyll build` | Local Jekyll build | Not run in this environment because Ruby was unavailable at audit time |

The pinned build path is now committed in-repo, so local build instructions are canonical even though this environment did not have Ruby installed when the audit started.

## Important Files And Directories

- `README.md`: public-facing repo overview and live site link
- `index.md`: main GitHub Pages content page
- `_config.yml`: GitHub Pages/Jekyll site metadata
- `assets/css/style.scss.css`: hand-authored theme overrides
- `oral-health-heatmap.png`: primary visualization asset
- `Figure2-Teeth_v4.1.pdf`: source PDF for the published heatmap
- `scripts/render_heatmap.py`: reproducible heatmap rebuild script
- `scripts/check_homepage.py`: homepage smoke test script
- `docs/heatmap-provenance.md`: provenance notes and rebuild command
- `scripts/validate_repo.py`: lightweight validation spine
- `docs/agentic-overhaul/2026-05-audit.md`: detailed audit and backlog
- `AGENTS.md`: contributor and agent operating guide

## Stale Or Conflicting Docs And Metadata

- `README.CRAWL.md` contains a machine-local path (`/Users/mschwar/...`) and a historical directory crawl snapshot. It is useful as a historical artifact only and should not be treated as canonical documentation.
- The repo now references a pinned local Ruby/Jekyll toolchain, so local build instructions are canonical from the repo itself.

## Known Risks

- Local GitHub Pages rendering is not reproducible from committed tooling in the current environment.
- Local build execution still depends on having Ruby installed on the host.
- The historical source dataset that fed the original figure is still not published in this repo.
- `README.CRAWL.md` remains as a historical artifact but is excluded from the public site.

## Immediate Next Moves

1. Implement the responsive polish pass in `feat/responsive-polish`, focusing on mobile and small-laptop typography and spacing without changing content.
2. Keep `scripts/render_heatmap.py` and `Figure2-Teeth_v4.1.pdf` in sync if the figure changes.
3. Run `python scripts/check_homepage.py` against `_site/index.html` after a local build if you need a homepage smoke check.
