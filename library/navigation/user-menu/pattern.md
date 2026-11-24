# User menu

Captured: 2026-11-20, recorded by an agent
Best for: a team product where a signed-in member reaches their own account: who is signed in, their settings and the way out.
Row opens: no rows. The menu holds actions, and it holds no records.
Related: `navigation/foot-menu`, the same menu at the foot of the side list, with the name and the email of the member at its head. `settings/settings-modal`, the window that the settings row opens.

## States

- `closed`: the page of the product. The trigger of the menu is at the head of the side list. It shows a small picture, a name and a chevron. Opens on: the page load, Escape, a press outside the menu, or a click on the trigger while the menu shows.
- `menu-open`: the menu, open under the trigger and over the page. It has one row for each action. The first row opens the settings. One row has an arrow, and it opens a submenu. The sign-out row is apart from the other rows. Opens on: a click on the trigger.
- `theme-open`: the menu, with the submenu open beside its row. The submenu lists the choices, and the current choice has a check. Opens on: the pointer over the row that has the arrow. The submenu of the source lists the workspaces. The sketch lists the themes.
- `settings-open`: the page with the settings window over it. The window is a part of `settings/settings-modal`, so the sketch draws it as a plain box with that name. Opens on: the settings row. Escape or a press outside the box opens `closed`. The capture has no frame of the settings of the source.
- `signed-out`: a page that says the member is signed out, with one button to sign in again. Opens on: the sign-out row. The source shows no such state, because the capture did not sign out.

The trigger of the source shows the picture and the name of the workspace. The sketch shows the member, because the member opens the menu from their avatar.

## Transitions

The source moves the menu with a script that writes the style in each frame, and `document.getAnimations()` returns nothing for the menu. So the agent read the style of the menu in each frame, at 120 frames in one second. Each duration has an error of about 8 ms. Each easing is the standard curve nearest to the samples. So each duration and each delay is measured, and each easing is estimated.

- `closed` to `menu-open`. Trigger: click the trigger. Moves: the menu goes from clear to solid. 35 ms, ease-out. measured duration, estimated easing.
- `closed` to `menu-open`. Trigger: the same click. Moves: the menu grows from 98% of its size to its full size, from the corner next to the trigger. 160 ms, cubic-bezier(0, 0, 0.2, 1). measured duration, estimated easing.
- `menu-open` or `theme-open` to `closed`. Trigger: press Escape, press outside the menu or click the trigger. Moves: the menu goes to 98% of its size. 20 ms, linear. measured duration, estimated easing.
- `menu-open` or `theme-open` to `closed`. Trigger: the same action. Moves: after a delay of 20 ms, the menu goes from solid to clear. 110 ms, cubic-bezier(0, 0, 0.2, 1). measured delay and duration, estimated easing. The source removes the menu about 170 ms after the action.
- `menu-open` to `theme-open`. Trigger: the pointer goes over the row that has the arrow. Moves: the submenu shows at once beside its row. 0 ms, none. measured.
- `theme-open` to `menu-open`. Trigger: the pointer goes over a different row. Moves: the submenu goes at once. 0 ms, none. measured.
- `menu-open` to `settings-open`. Trigger: click the settings row. Moves: the menu goes and the box shows at once. 0 ms, none. estimated. The capture read no transition for this step. The motion of the window belongs to `settings/settings-modal`.
- `settings-open` to `closed`. Trigger: press Escape or press outside the box. Moves: the box goes at once. 0 ms, none. estimated.
- `menu-open` to `signed-out`. Trigger: click the sign-out row. Moves: the page changes at once. 0 ms, none. estimated. The capture did not sign out.

## Hard cases

- 390 px screen: the source hides the side list. A menu button shows the side list as a drawer over the page, and the trigger is in the drawer. So the menu needs 2 taps. The sketch keeps the trigger in the top bar, and the menu needs 1 tap.
- Drawer on a 390 px screen: the drawer goes out to the left in 360 to 445 ms. The 2 runs had few frames, so this range is not exact.
- Submenu on a 390 px screen: the submenu has no room beside its row. It shows over the rows of the menu.
- Many rows: when the member types while the menu shows, a field with the typed text shows at the top of the menu. The menu then shows only the rows that match. The sketch has 3 rows and draws no field.
- No match: the menu shows one line that says that no action matches.
- Who is signed in: the menu does not name the member. Only the submenu shows the email of the account, as a label at its top. `navigation/foot-menu` names the member at the head of the menu.
- Long name: the trigger cuts a long name with an ellipsis on one line.
- Keyboard: one press of Escape closes the submenu and the menu together. The focus goes back to the trigger.
- Slow network and failed load: not seen. The menu shows no data that loads.
- Sign out: not seen. The capture did not sign out, so it is not known if the source asks the member to confirm.

## Notes

- The owner's rule for this record: a pattern is general, and a product composes it with its own parts. So the sketch keeps only the parts that each product of this kind needs. It draws no part that belongs to one source.
- The owner's rule for each part: one part has one pattern. So this record draws the menu, and `settings/settings-modal` draws the settings window.
- The first row of the source opens its settings, as the first row of the sketch does. The source also has a row for the members and a row for its desktop app. These rows are the product's own, so the sketch draws none of them.
- The sketch has no profile row and no notification row. A product puts these parts behind the settings row, or it adds its own rows.
- The source shows the shortcut keys of a row at the right of the row. The sketch draws no shortcut keys. A product that has shortcut keys adds them.
- In the sketch, a click on the row that has the arrow and the Right Arrow key also open the submenu. The capture did not try them in the source.
- In the source, the words of a row that is a link change their colour in 150 ms, ease. The agent read this value with `document.getAnimations()`. The highlight of a row shows at once.
- The source draws a line between the groups of rows. The sketch uses space between the groups.
- Keep these parts when the look changes: one press of Escape closes all layers, the focus goes back to the trigger, and the sign-out row stays apart from the other rows.
- The sketch keeps no brand and no picture of the source. The member and all words are sample content.
- The frames of the source are not committed.
