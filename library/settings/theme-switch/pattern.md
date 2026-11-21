# Theme switch

Captured: 2026-11-21, recorded by an agent
Best for: a signed-in reader chooses how the product looks, as one short setting among other preferences. The choice applies at once, with no Save button. For a product that gives the look its own section and shows what each choice looks like, use `settings/theme-switch-preview-cards`.
Row opens: no rows. The page holds settings, and it holds no records.
Related: `settings/theme-switch-preview-cards`, the second pattern of the same part, with a picture of each choice. `navigation/user-menu`, the menu whose Preferences row opens this page, and whose theme submenu is a shorter form of this choice. `settings/settings-modal` and `settings/settings-window`, the settings windows whose theme tab holds cards with words.

## States

The recording shows the control in the settings menu of the signed-out page of the source. The source shows its signed-in Preferences page only after a sign-in, so the agent did not record it. The control, its order, its icons and its behaviour come from the recording. The Preferences page around the control is drawn.

- `system`: the Preferences page. An Appearance group has a Theme row, with its name and one line about it at the left, and the control at the right. The control is 3 icon buttons in one row: Light (a sun), Dark (a moon) and System (a half-filled circle), in this order. The chosen button is filled. System is chosen, so the page looks like the device. A Language row and a plain box for the notification settings follow. Opens on: the Preferences row of the account menu. The source opens its menu from a settings button at the head of the page, and System is chosen at the first visit.
- `light`: Light is chosen. The page changes to its light look at once. Opens on: a click on the Light button.
- `dark`: Dark is chosen. The page changes to its dark look at once. Opens on: a click on the Dark button.

## Transitions

The capture script recorded the source, and it read no transition when the theme changed. So `transitions.json` is empty.

- `system`, `light` or `dark` to another of these states. Trigger: a click on a button, or an arrow key on the control. Moves: the fill goes to the chosen button, and the page changes its look. 0 ms, none. measured.
- The menu of the source opens and closes with a fade and a small move in 120 ms. This record has no menu, so it does not keep these values. The menu is a part of `navigation/user-menu`.

## Hard cases

- No Save button: the choice applies and stays at once. The source keeps the choice on the device of the signed-out reader. A product with accounts keeps it on the account, so the choice follows the reader to each device. The sketch saves nothing.
- Failed save: not seen. A product that saves the choice on the account keeps the new look on the device, and it tries the save again later.
- System and the device: when the device changes between light and dark, a page on System changes with it at once. A page on Light or Dark does not change.
- First visit: the source chooses System. Keep System as the first value.
- Icons without words: each button has its name as its label and as its tip. A screen reader reads "Theme", then the name of each button and whether it is chosen.
- Keyboard: Tab goes to the chosen button. The arrow keys move the choice, and the look changes with each move. Not seen in the source, which uses menu items.
- Narrow screen: at 390 px the control stays at the right of the name. Below 360 px it goes below the name. Each state fits at 320 px.
- Long name or long line: the words wrap, and the control keeps its place.
- Slow network: not seen. The choice needs no load.

## Notes

- The source puts the control in a menu. The owner asked for a Preferences page, so this record puts the same control in a settings row. The control, its order and its instant change come from the source.
- Keep these parts when the look changes: the 3 choices in the order Light, Dark, System, a name and a tip on each icon, System as the first value, and no Save button.
- The source also has a Language row and a Feedback row in its menu. The sketch keeps a Language row as sample content, and it leaves out Feedback.
- The sketch keeps no brand and no picture of the source. All words are sample content.
- The frames of the recording are not committed.
