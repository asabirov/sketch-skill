# Changelog

## 0.16.0 — 2026-11-21

### Added

- A Chart category for report pages. Before, the kit had only the small bars and trends of the dashboard page, with no projection and no rule for when to use them. Now there are 5 chart templates: monthly bars, a line over time, bars against a plan, a trend in each table row, and key numbers with a small trend.
- Each chart shows the current month to date and the projected months. So a reader does not take an incomplete month for a fall.
- No chart scrolls inside itself, on a phone or on a desktop. A scroll bar inside a chart hides periods and is hard to use.
- Each chart has a rule page that says when to use it and when not to, so that a designer picks the right chart.
- The charts follow real product charts that the owner chose. A dated study gives a source for each chart practice.
- Each chart gives all its values to screen readers.

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
