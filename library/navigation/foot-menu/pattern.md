# Foot menu

Captured: 2026-11-20, from one still picture of the signed-in page at 1280 px
Best for: a team product where a signed-in member checks which account is signed in, then reaches their settings and the way out.
Row opens: no rows. The menu holds actions, and it holds no records.
Related: `navigation/user-menu`, the same menu at the head of the side list, with no name and no email in the menu. It also draws the signed-out page. `settings/settings-window`, the window that the settings row opens.

## States

- `closed`: the page of the product. The trigger of the menu is at the foot of the side list. It shows the picture and the name of the member. Opens on: the page load, Escape, a press outside the menu, or a click on the trigger while the menu shows.
- `menu-open`: the menu, open above the trigger and over the page. Its head shows the name and the email of the member. Its rows are a settings row, a help row, a Theme row with an arrow, a line and the sign-out row. Each row has an icon. Opens on: a click on the trigger.
- `theme-open`: the menu, with the submenu open beside the Theme row. The menu opens up, so the submenu also opens up from its row. The submenu lists the themes, and the current theme has a check. Opens on: the pointer over the Theme row. The picture of the source shows no theme row and no such state.
- `settings-open`: the page with the settings window over it. The window is a part of `settings/settings-window`, so the sketch draws it as a plain box with that name. Opens on: the settings row. Escape or a press outside the box opens `closed`. The picture of the source shows no such state.
- `signed-out`: the signed-out page. It is a part of `navigation/user-menu`, so the sketch draws it as a plain box with that name. Opens on: the sign-out row. The picture of the source shows no such state.

## Transitions

The capture is one still picture, so the agent read no transition from the source. Each value is an estimate: the sketch plays the values of `navigation/user-menu`.

- `closed` to `menu-open`. Trigger: click the trigger. Moves: the menu goes from clear to solid. 35 ms, ease-out. estimated.
- `closed` to `menu-open`. Trigger: the same click. Moves: the menu grows from 98% of its size to its full size, from the corner next to the trigger. 160 ms, cubic-bezier(0, 0, 0.2, 1). estimated.
- `menu-open` or `theme-open` to `closed`. Trigger: press Escape, press outside the menu or click the trigger. Moves: the menu goes to 98% of its size. 20 ms, linear. estimated.
- `menu-open` or `theme-open` to `closed`. Trigger: the same action. Moves: after a delay of 20 ms, the menu goes from solid to clear. 110 ms, cubic-bezier(0, 0, 0.2, 1). estimated.
- `menu-open` to `theme-open`. Trigger: the pointer goes over the Theme row. Moves: the submenu shows at once beside its row. 0 ms, none. estimated.
- `theme-open` to `menu-open`. Trigger: the pointer goes over a different row. Moves: the submenu goes at once. 0 ms, none. estimated.
- `menu-open` to `settings-open`. Trigger: click the settings row. Moves: the menu goes and the box shows at once. 0 ms, none. estimated. The motion of the window belongs to `settings/settings-window`.
- `settings-open` to `closed`. Trigger: press Escape or press outside the box. Moves: the box goes at once. 0 ms, none. estimated.
- `menu-open` to `signed-out`. Trigger: click the sign-out row. Moves: the page changes at once. 0 ms, none. estimated.

## Hard cases

The picture of the source is 1280 px wide. So each case below 1000 px is the designer's choice, and the source does not show it.

- Below 1000 px: the side list is a tab bar. The trigger is the last tab of the tab bar, with the picture above the first name.
- Submenu from 600 to 999 px: the menu is at the right edge of the screen, so the submenu has no room at the right. It shows at the left of the menu.
- Submenu below 600 px: the submenu has no room beside its row. It shows over the rows of the menu.
- Long name: not seen. The sketch cuts a long name on the trigger with an ellipsis on one line. In the head of the menu, a long name or a long email goes to the next line.
- Keyboard: not seen. In the sketch, one press of Escape closes the submenu and the menu together, and the focus goes back to the trigger.
- Slow network and failed load: not seen. The menu shows no data that loads.
- Sign out: not seen. It is not known if the source asks the member to confirm.

## Notes

- The owner's rule for this record: a pattern is general, and a product composes it with its own parts. So the sketch keeps only the parts that each product of this kind needs. A product adds its own rows between the head and the Theme row.
- The owner's rule for each part: one part has one pattern. So this record draws the menu. `settings/settings-window` draws the settings window, and `navigation/user-menu` draws the signed-out page. The profile and the notification settings are behind the settings row.
- The menu of the source also has a dashboard row, an invite row and an upgrade row, and its help row opens a submenu. An icon button stands beside its trigger. These parts are the product's own, so the sketch draws none of them.
- The picture of the source shows no theme row. The owner asked for a theme choice, and then for a submenu as in `navigation/user-menu`. The sketch puts the Theme row before the line.
- The coordinator of this capture read the entry of the menu in the source with `document.getAnimations()`: 2 animations, 120 ms, linear. The agent of this record did not read this value, so `transitions.json` does not have it.
- In the sketch, a click on the Theme row and the Right Arrow key also open the submenu.
- Keep these parts when the look changes: the head of the menu names the member, one press of Escape closes all layers, the focus goes back to the trigger, and the sign-out row stays apart from the other rows.
- The sketch keeps no brand and no picture of the source. The member and all words are sample content.
- The picture of the source is not committed.
