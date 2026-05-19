#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "_site" / "index.html"
EXPECTED_TITLE = "Oral Health Heatmap | Matthew Schwartz Data Visualization"
EXPECTED_HEADING = "Oral Health Heatmap"
EXPECTED_IMAGE_ALT = (
    "Heatmap of 28 permanent teeth for 1,176 Tsimane adults, colour-coded from healthy "
    "(blue) to missing (red)."
)


def load_html(source: str) -> str:
    parsed = urlparse(source)
    if parsed.scheme in {"http", "https"}:
        with urlopen(source) as response:  # nosec: trusted local QA target or live site URL
            return response.read().decode("utf-8")

    path = Path(source)
    if not path.is_absolute():
        path = (ROOT / path).resolve()
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8")


def normalize(html: str) -> str:
    return re.sub(r"\s+", " ", html)


def check_homepage(html: str) -> list[str]:
    text = normalize(html)
    errors: list[str] = []

    if EXPECTED_TITLE not in text:
        errors.append(f"missing page title: {EXPECTED_TITLE}")
    if f"<h1 class=\"page-heading\">{EXPECTED_HEADING}</h1>" not in text:
        errors.append(f"missing page heading: {EXPECTED_HEADING}")
    if 'class="heatmap"' not in text:
        errors.append("missing heatmap image class")
    if 'src="oral-health-heatmap.png"' not in text:
        errors.append("missing heatmap image source")
    if EXPECTED_IMAGE_ALT not in text:
        errors.append("missing heatmap alt text")
    download_link = re.search(
        r'<a\b[^>]*href="oral-health-heatmap\.png"[^>]*>',
        text,
    )
    if not download_link or "download" not in download_link.group(0):
        errors.append("missing download link for oral-health-heatmap.png")
    if "README.CRAWL.html" in text:
        errors.append("public homepage should not link to README.CRAWL.html")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke test the rendered homepage HTML.")
    parser.add_argument(
        "source",
        nargs="?",
        default=str(DEFAULT_SOURCE),
        help="Path or URL to the rendered homepage HTML.",
    )
    args = parser.parse_args()

    try:
        html = load_html(args.source)
    except FileNotFoundError as exc:
        print(f"Homepage HTML not found: {exc}", file=sys.stderr)
        return 1

    errors = check_homepage(html)
    if errors:
        print("Homepage smoke test failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Homepage smoke test passed for {args.source}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
