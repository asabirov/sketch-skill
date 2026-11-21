# Agent rules

## Keep the lists up to date

When a pull request adds, removes or renames a pattern in `library/`, update these in the same pull request:

- `docs/library.md`: one row for each pattern, with its "Best for" line, and the pattern and category counts.
- The "Pattern library" section of `README.md`: the pattern and category counts, and the row of each category.

When a pull request adds, removes or renames a template in `templates/`, update these in the same pull request:

- The template counts in `SKILL.md`, `README.md` and `docs/templates.md`.
- The "Template categories" table of `README.md`.
- The entry and the picture of the template in `docs/templates.md`. Run `python3 docs/render.py` to refresh the pictures.

`tests/test_library_index.py` fails when `docs/library.md` or the `README.md` counts do not match `library/`.
