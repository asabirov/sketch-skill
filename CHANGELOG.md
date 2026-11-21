# Changelog

## Unreleased

### Added

- Added the Chart category with 5 templates: monthly bars, a line over time, bars with a line, a sparkline in a table row and a stat with a small trend. Each template shows the current month to date and the projected months, and fits its periods without a scroll bar at 390 px and 1280 px.
- Added `references/charts.md` and one rule page for each chart template: when to use it, when not to use it, and how it fits many periods.
- Added the chart study `docs/studies/2026-11-21-chart-best-practices.md`, with a source for each practice.
- Added the chart classes to `assets/sketch.css`: `sketch-chart`, `sketch-plot`, `sketch-periods`, `sketch-line`, `sketch-tick` and `sketch-key`, with the `partial`, `projected` and `minor` states. A projected part of a sparkline is dashed.

## 0.15.0 — 2026-11-21

### Added

- Added the reusable pattern library and its pull request gate. The gate fails on a Source note or a web address in a library file. A name check runs in a private flow before a pattern reaches this repository.

### Changed

- Each sketch loads the kit from `assets/sketch.css` and `assets/sketch.js` instead of an inline copy.
- The kit draws the extra pattern icons. A pattern sets `window.sketchGlyphs` with the paths instead of drawing them itself.

## 0.14.0 — 2026-11-20

### Changed

- Replaced the README example with four sketches at four widths, made by `docs/render.py`.
- Added `docs/templates.md` with a picture, name and "Best for" line for each of the 43 templates.

## 0.13.0 — 2026-11-18

### Added

- First public version: the sketch kit, the template gallery, the 43 page templates and the drawing rules.
