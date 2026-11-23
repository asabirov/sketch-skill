# Theme switch with preview cards

Captured: 2026-11-21, from public pictures
Best for: a signed-in reader chooses how the product looks in a section of its own, and sees a small picture of each choice before choosing. The choice applies at once, with no Save button. For a product that has the look only as a short choice in its account menu, use the theme submenu of `navigation/user-menu`.
Row opens: no rows. The page holds settings, and it holds no records.
Related: `navigation/user-menu`, the menu whose Preferences row opens this page, with a theme submenu of its own. `settings/settings-modal`, the settings window whose theme tab holds cards with words and no picture.

## States

The pictures show the Color mode group of the source with Match system chosen. The help text names the path to the group and the 3 choices. Each other state is drawn, and its line says so.

- `system`: the Preferences page, on its Appearance section. A Color mode heading is above 3 cards in one row: Light, Match system and Dark, in this order. Each card is a small picture of a message box in that look, with the name of the choice below the card. The Match system picture is light in its left half and dark in its right half. The chosen card has a ring. Below the group, a plain box stands for the other settings of the look. Opens on: the Preferences row of the account menu, then the Appearance section. The help text says that the reader opens the account menu at the foot of the side list, then Settings, then Appearance. The pictures show this state.
- `light`: the Light card has the ring. The page changes to its light look at once. Opens on: a click on the Light card. The pictures show no such state.
- `dark`: the Dark card has the ring. The page changes to its dark look at once. Opens on: a click on the Dark card. The pictures show no such state.

## Transitions

The capture is public pictures, so the agent read no transition from the source. `transitions.json` is empty, and each value is the designer's choice.

- `system`, `light` or `dark` to another of these states. Trigger: a click on a card, or an arrow key in the group. Moves: the ring goes to the chosen card, and the page changes its look. 0 ms, none. estimated.

## Hard cases

- No Save button: the help text names no Save button, and the pictures show none. So the choice applies at once. The sketch saves nothing.
- Failed save: not seen. A product that saves the choice on the account keeps the new look on the device, and it tries the save again later.
- Match system and the device: when the device changes between light and dark, a page on Match system changes with it at once. A page on Light or Dark does not change.
- The picture in each theme: the Light card keeps the light look and the Dark card keeps the dark look, also when the page itself is dark. Do not let the pictures follow the theme of the page.
- Keyboard: Tab goes to the chosen card. The arrow keys move the choice, and the look changes with each move. The focus ring is outside the ring of the chosen card. Not seen in the source.
- Screen reader: the pictures are hidden from it. It reads "Color mode", then the name of each card and whether it is chosen.
- Narrow screen: at 390 px the 3 cards share the width, and the pictures get smaller. Below 360 px the cards are in one column. Each state fits at 320 px. The pictures show only a wide window.
- Long name: the name below a card wraps, and the cards keep the same width.
- Slow network: not seen. The choice needs no load.

## Notes

- A picture of each choice lets a reader who does not know the words "light" and "dark" choose by eye. Keep a real piece of the product in each picture, such as its message box.
- Keep these parts when the look changes: the 3 choices in the order Light, Match system, Dark, a picture that keeps its own look in each theme, the half-and-half picture for Match system, and no Save button.
- The source has a second group below Color mode, for the font of the text, with 3 cards of the same form. It is a different setting, so the sketch draws it as a plain box. A product can use the same card form for it.
- The source has a different look for its message box and a blue ring. The sketch has one ink, so the ring is thick ink.
- The sketch keeps no brand, no colour and no picture of the source. All words are sample content.
- The pictures of the source are not committed.
