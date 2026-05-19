# Oral Health Heatmap Provenance

The published heatmap in this repository is reproducible from the committed source figure PDF through a single rasterization step.

- Source figure available in this repo: [Figure2-Teeth_v4.1.pdf](../Figure2-Teeth_v4.1.pdf)
- Published raster available in this repo: [oral-health-heatmap.png](../oral-health-heatmap.png)
- Rebuild script available in this repo: [scripts/render_heatmap.py](../scripts/render_heatmap.py)

## Provenance Boundary

This repository does not currently publish the raw or analysis-ready source dataset behind the original heatmap. The committed PDF is the earliest source artifact available here.

That means this repo supports figure-to-PNG regeneration, not full data-to-figure regeneration. Do not claim that the complete underlying dataset or statistical pipeline is reproducible from this repository unless those materials are added later.

## Rebuild Command

```bash
python scripts/render_heatmap.py
```

The source PDF is letter-sized and the rebuild path exports the image at 200 DPI. That reproduces the same 1700 x 2200 pixel image content as the committed PNG. PNG encoder metadata may differ between exporters, but the pixels match.

## Current Local Rebuild Blocker

On this Windows environment, `python scripts/render_heatmap.py` is currently blocked by MiKTeX `pdftoppm` permission errors while writing log/temp output under `AppData\Local`. The script and source artifact remain committed, but local verification of the rebuild command requires either a working `pdftoppm` installation or a future script change that routes temporary output through a known writable repo-local path.
