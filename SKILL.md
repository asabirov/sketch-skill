---
name: sketch
description: "Use when drawing a disposable one-ink UI sketch for a layout or interaction review, or when choosing a sketch template category. Covers the sketch kit, the 48 categorized templates, the chart rules, the template gallery and drawing rules. Not for the final look of a product, its UI kit or its design system and not for the tool that shows the sketch to a reviewer."
metadata:
  version: "0.17.0"
---

# Sketch

A sketch is a disposable page drawn with one marker. It shows layout and behaviour, and it cannot be mistaken for the built thing.

| Task | Read |
| --- | --- |
| Draw a sketch, or start one from a page template | [references/sketch-prototypes.md](references/sketch-prototypes.md) |
| Draw a chart, or choose a chart template | [references/charts.md](references/charts.md) |

The skill folder holds `assets/`, `templates/` and `references/`. Keep the installed skill unchanged. Copy a template to the project, edit it, then run `python3 "<skill-folder>/assets/sketch_inline.py" page.html > sketch.html` from the project folder.

## No sketch value is a design-system token

No sketch element or sketch value is a design-system token. This includes each colour, size, space, font, duration and easing. A sketch shows only layout and interaction. Its one ink and its kit are not a look.

Give sketch values to the designer as a proposal. The designer compares each value with the design system:

- If the design system has a token for the value, the screen uses that token.
- If the design system lacks the value, the designer proposes a design-system change for review. The value becomes a token only after the human approves it.

Never give a sketch value to a builder as a value to build.

## Start from a category

Before you draw a sketch, look in `library/` for a pattern that fits the screen. [docs/library.md](docs/library.md) lists each pattern with its "Best for" line. A name check runs in a private flow before a pattern reaches this repository.

Before you draw a sketch, choose the category that fits the screen. Then copy one template whose "Best for" line fits it. Read "Start from a template" in [references/sketch-prototypes.md](references/sketch-prototypes.md). Never start a sketch from an empty page.
