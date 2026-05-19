#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PDF = ROOT / "Figure2-Teeth_v4.1.pdf"
OUTPUT_PNG = ROOT / "oral-health-heatmap.png"
DPI = "200"


def render_heatmap() -> Path:
    if shutil.which("pdftoppm") is None:
        raise SystemExit("pdftoppm is required to rebuild oral-health-heatmap.png.")
    if not SOURCE_PDF.exists():
        raise SystemExit(f"Missing source PDF: {SOURCE_PDF.relative_to(ROOT)}")

    with tempfile.TemporaryDirectory() as tmpdir:
        prefix = Path(tmpdir) / OUTPUT_PNG.stem
        subprocess.run(
            [
                "pdftoppm",
                "-png",
                "-singlefile",
                "-r",
                DPI,
                str(SOURCE_PDF),
                str(prefix),
            ],
            check=True,
            cwd=ROOT,
        )
        rendered = prefix.with_suffix(".png")
        if not rendered.exists():
            raise SystemExit("pdftoppm did not create the expected PNG output.")
        shutil.copyfile(rendered, OUTPUT_PNG)

    return OUTPUT_PNG


def main() -> int:
    render_heatmap()
    print(
        f"Rendered {OUTPUT_PNG.relative_to(ROOT)} from {SOURCE_PDF.name} at {DPI} DPI."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
