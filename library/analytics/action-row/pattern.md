# Action row with a More menu

Captured: 2026-11-25, recorded by an agent
Best for: the top of an overview page, where a person starts the most common jobs of the product without a menu.
Row opens: no rows.
Related: `analytics/summary-card` holds one direct action for one part of the product. `analytics/balance-card` is often the first card below this row.

## Scenarios

- Start the most common job with one click on the filled main action.
- Start a less common job from an outlined action.
- On a narrow screen, reach the actions that do not fit through More.
- Change the page, such as its cards, from the page action at the right end.

## States

- `actions`: one filled main action, 4 outlined actions with an icon each, and a page action at the right end. Opens on: the address of the page.
- `more-open`: in a narrower space, the row keeps the actions that fit. More holds the others, in the same order. Opens on: a click on More.
- `narrow`: at about 360 px, the row holds only the main action, More and the page action. Opens on: a narrow screen or a narrow column.
- `narrow-more`: More lists all 4 outlined actions. Opens on: a click on More in the `narrow` state.
- `action-started`: the action opens its own form. The sketch shows a line of text in its place. Opens on: a click on an action.

## Transitions

- `actions` to `more-open`. Trigger: a click on More. Moves: nothing. The menu shows at once. measured.
- `actions` to `narrow`. Trigger: the width changes. Moves: nothing. The actions move into More at once. estimated.

## Hard cases

- Long labels: the row measures the real widths, so a long label moves more actions into More.
- One action only: the row shows no More.
- Translation: the order stays the same in More, so a person finds an action in the same place.
- Touch screen: each button has a target of 44 px.
- Narrow screen: the source shows only the main action and More at 390 px. The sketch uses the same rule at every width, not only on a phone.

## Notes

- Only the main action is filled, so the eye finds the main job first. The main action never goes into More.
- The row moves actions into More from the end. Put the actions in the order of use.
- The page action, such as Customize, is not a job. It stays apart, at the right end.
- Left out, because only the source has them: the names of the source's own jobs and its icons.
