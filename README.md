# Tsimane Oral Health Heatmap: A Data Visualization Project

This repository showcases a data visualization project designed to represent the complete oral health status of the Tsimane population of Bolivia. The heatmap synthesizes over 32,000 data points from 1,176 individuals into a single, intuitive image, revealing complex patterns of dental health across age, sex, and anatomy.

This is a small GitHub Pages static site. The repo currently publishes one primary page (`index.md`) and one primary visualization asset (`oral-health-heatmap.png`).

The repo also pins a local GitHub Pages build path (`Gemfile` and `.ruby-version`) and keeps the committed source figure (`Figure2-Teeth_v4.1.pdf`) with a rebuild script in `scripts/render_heatmap.py`.

For the branch/PR/QA loop used by future agents, see `docs/agentic-first-buildout-plan.md`.

---

## ▶️ View the Live Project

The full project, including the visualization and detailed analysis, is best viewed on the live project page:

**[https://mschwar.github.io/data-visualization/](https://mschwar.github.io/data-visualization/)**

---

## About the Visualization

The heatmap displays the dental health of **1,176 individuals** (543 men and 633 women) from the Tsimane Health and Life History Project. Its purpose is to make a complex, multidimensional dataset immediately understandable by visualizing patterns of tooth decay and loss across:
*   **28 permanent teeth** (incisors, canines, premolars, and molars)
*   **Age groups** (ranging from 15-24 to 75+)
*   **Sex** (male and female)
*   **Anatomy** (upper and lower teeth)

A 5-point color scale indicates the health status of each tooth, from healthy (blue) to missing (red).

## Repository Contents

*   `index.md`: The main content file for the GitHub Pages site, written in Markdown.
*   `oral-health-heatmap.png`: The high-resolution image of the data visualization.
*   `_config.yml`: The configuration file that applies the visual theme to the GitHub Pages site.
*   `Figure2-Teeth_v4.1.pdf`: The committed source figure used to regenerate the PNG.
*   `Gemfile`: The pinned GitHub Pages and Ruby toolchain.
*   `.ruby-version`: The pinned Ruby runtime for local builds.
*   `scripts/validate_repo.py`: Lightweight repository validation for future contributors and agents.
*   `docs/agentic-first-buildout-plan.md`: Branch/PR/QA loop and feature sequencing guide.
*   `scripts/render_heatmap.py`: Rebuild script for the published heatmap PNG.
*   `scripts/check_homepage.py`: Smoke test for the rendered homepage HTML.
*   `docs/heatmap-provenance.md`: Source artifact and rebuild notes.

## Validate The Repo

Run:

```bash
python scripts/validate_repo.py
python scripts/check_homepage.py
```

This checks for required files, obvious broken local references, key site metadata, committed OS junk files, and the rendered homepage shape.

## Rebuild Locally

This repository pins Ruby 3.3.4 and `github-pages` 232, matching the current GitHub Pages dependency set. To rebuild the site and the heatmap locally:

```bash
bundle install
bundle exec jekyll build
bundle exec jekyll serve --baseurl=""
python scripts/render_heatmap.py
```

The heatmap PNG is regenerated from `Figure2-Teeth_v4.1.pdf` at 200 DPI. The rendered pixels match the published PNG; only PNG encoder metadata can differ.

## Publication Context

This visualization was created as part of the research published in:

> Trumble, B., Schwartz, M., et al. (2024). Poor Oral Health Is Associated With Inflammation, Aortic Valve Calcification, and Brain Volume Among Forager-Farmers. *The Journals of Gerontology*. [DOI: 10.1093/gerona/glae013](https://doi.org/10.1093/gerona/glae013)

---

Created by **Matthew Schwartz**.
