# Oral Health Heatmap Provenance

The published heatmap is derived from the committed source figure PDF and a single rasterization step.

- Source figure: [Figure2-Teeth_v4.1.pdf](../Figure2-Teeth_v4.1.pdf)
- Published raster: [oral-health-heatmap.png](../oral-health-heatmap.png)
- Rebuild script: [scripts/render_heatmap.py](../scripts/render_heatmap.py)

## Rebuild Command

```bash
python scripts/render_heatmap.py
```

The source PDF is letter-sized and the rebuild path exports the image at 200 DPI. That reproduces the same 1700 x 2200 pixel image content as the committed PNG. PNG encoder metadata may differ between exporters, but the pixels match.
