#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
TEXT_FILES = [
    ROOT / "README.md",
    ROOT / "index.md",
    ROOT / "_config.yml",
    ROOT / "CURRENT_STATE.md",
    ROOT / "AGENTS.md",
    ROOT / "docs" / "agentic-first-buildout-plan.md",
    ROOT / "docs" / "heatmap-provenance.md",
    ROOT / "docs" / "historical-artifacts.md",
    ROOT / "docs" / "agentic-overhaul" / "2026-05-audit.md",
]
REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "index.md",
    ROOT / "_config.yml",
    ROOT / "Gemfile",
    ROOT / ".ruby-version",
    ROOT / "Figure2-Teeth_v4.1.pdf",
    ROOT / "oral-health-heatmap.png",
    ROOT / "assets" / "css" / "style.scss.css",
    ROOT / "scripts" / "validate_repo.py",
    ROOT / "scripts" / "render_heatmap.py",
    ROOT / "scripts" / "check_homepage.py",
    ROOT / "docs" / "agentic-first-buildout-plan.md",
    ROOT / "docs" / "heatmap-provenance.md",
    ROOT / "docs" / "historical-artifacts.md",
    ROOT / "CURRENT_STATE.md",
    ROOT / "AGENTS.md",
    ROOT / "docs" / "agentic-overhaul" / "2026-05-audit.md",
    ROOT / ".github" / "workflows" / "validate.yml",
]
FORBIDDEN_FILES = [ROOT / ".DS_Store", ROOT / "assets" / ".DS_Store"]


def is_external_target(target: str) -> bool:
    parsed = urlparse(target)
    return bool(parsed.scheme) or target.startswith("//")


def is_anchor(target: str) -> bool:
    return target.startswith("#")


def local_targets(text: str) -> list[str]:
    markdown_links = re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)
    html_attrs = re.findall(r"""(?:src|href)\s*=\s*["']([^"']+)["']""", text)
    return markdown_links + html_attrs


def check_required_files(errors: list[str]) -> None:
    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")


def check_forbidden_files(errors: list[str]) -> None:
    for path in FORBIDDEN_FILES:
        if path.exists():
            errors.append(f"Committed OS junk file should not exist: {path.relative_to(ROOT)}")


def check_config(errors: list[str]) -> None:
    config = (ROOT / "_config.yml").read_text(encoding="utf-8")
    if "theme: minima" not in config:
        errors.append("_config.yml should declare the GitHub Pages theme `minima`.")
    if "title:" not in config:
        errors.append("_config.yml should define a site title.")
    if "description:" not in config:
        errors.append("_config.yml should define a site description.")
    for entry in [
        "AGENTS.md",
        "CURRENT_STATE.md",
        "Figure2-Teeth_v4.1.pdf",
        "Gemfile",
        "Gemfile.lock",
        "README.CRAWL.md",
        "docs/",
        "scripts/",
        "vendor/",
    ]:
        if entry not in config:
            errors.append(f"_config.yml should exclude repo-only artifact `{entry}` from the public site.")


def check_index(errors: list[str]) -> None:
    index_text = (ROOT / "index.md").read_text(encoding="utf-8")
    if "<img" not in index_text:
        errors.append("index.md should embed the visualization image.")
    if 'alt="' not in index_text and "alt='" not in index_text:
        errors.append("index.md image should include alt text.")
    if "oral-health-heatmap.png" not in index_text:
        errors.append("index.md should reference oral-health-heatmap.png.")


def check_local_links(errors: list[str]) -> None:
    for path in TEXT_FILES:
        text = path.read_text(encoding="utf-8")
        for raw_target in local_targets(text):
            target = raw_target.strip()
            if not target or is_external_target(target) or is_anchor(target):
                continue
            normalized = target.split("#", 1)[0].split("?", 1)[0]
            if not normalized:
                continue
            candidate = (path.parent / normalized).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"{path.relative_to(ROOT)} references a path outside the repo: {raw_target}"
                )
                continue
            if not candidate.exists():
                errors.append(
                    f"{path.relative_to(ROOT)} references a missing local file: {raw_target}"
                )


def check_readme(warnings: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "python scripts/validate_repo.py" not in readme:
        warnings.append("README.md does not document the validation command.")
    if "bundle exec jekyll build" not in readme:
        warnings.append("README.md does not document the pinned local Jekyll build command.")
    if "python scripts/render_heatmap.py" not in readme:
        warnings.append("README.md does not document the heatmap regeneration command.")
    if "python scripts/check_homepage.py" not in readme:
        warnings.append("README.md does not document the homepage smoke test command.")
    if "Figure2-Teeth_v4.1.pdf" not in readme:
        warnings.append("README.md does not mention the committed heatmap source PDF.")
    if "docs/historical-artifacts.md" not in readme:
        warnings.append("README.md does not document the historical artifact policy.")
    if "README.CRAWL.md" not in readme:
        warnings.append("README.md does not mention the retained historical crawl snapshot.")
    crawl = ROOT / "README.CRAWL.md"
    if crawl.exists():
        crawl_text = crawl.read_text(encoding="utf-8")
        if "/Users/mschwar/" in crawl_text:
            warnings.append(
                "README.CRAWL.md contains a stale machine-local path and should not be treated as canonical repo documentation."
            )


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the repository structure and key content.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Run in check mode. Current validations are read-only, so this matches the default behavior.",
    )
    parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    check_required_files(errors)
    check_forbidden_files(errors)
    check_config(errors)
    check_index(errors)
    check_local_links(errors)
    check_readme(warnings)

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
    else:
        print("Validation passed.")

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
