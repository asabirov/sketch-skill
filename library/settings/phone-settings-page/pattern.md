# Phone settings page

Captured: 2026-11-22, from public pictures
Best for: a phone chat app with about 15 settings, where a signed-in person opens Settings from their account and goes back with Back. Each choice applies at once, and a sign-out asks once more.
Row opens: on the record's own page
Related: `settings/phone-settings-sheet` opens Settings as a sheet over the chat, with a name on each group and a pull-down menu for the appearance. `navigation/swipe-back` gives the drag back from a page. `settings/settings-window` is the settings of a desktop product.

## States

- `chat`: the chat, with the menu button at the top left. A plain box stands for the chat. Opens on: a tap on the dim layer beside the side menu.
- `drawer`: the side menu covers 82% of the width from the left. A plain box stands for the chats. The account row is at the foot: the avatar, the name and a settings icon. The chat shows dim at the right. Opens on: a tap on the menu button, or Back in Settings.
- `settings`: Settings fills the screen. Its bar has Back at the left and the title "Settings" in the center. Under the bar, the email of the account, with the plan at the right. Then 4 groups with no names. Space and a thin line separate them: the account (Profile, Billing), what the assistant can use (Tools, Connected apps, Permissions), the look and the voice (Appearance, Speech language, Notifications) and the rest (Haptic feedback, Privacy, Shared links). Log out is alone at the end. Each row has an icon at the left. A row that opens a page has a chevron at the right. A row with a choice shows its value and a down chevron. A row can have a second line, such as "2 connected". Opens on: a tap on the account row.
- `section`: one section, here Privacy, fills the screen. Its bar has Back at the left and the section name in the center. It has a switch with a second line, a choice of two (Ask each time, Always allow) and a delete action, marked as the dangerous one. The source shows no picture of an opened section. The sketch draws it from the source's help text.
- `appearance-card`: a card in the center of the screen, with the title "Appearance" and 3 rows: System, Light and Dark. Each row has an icon, and a tick marks the current choice. Everything under the card is dim. Opens on: a tap on the Appearance row.
- `sign-out-confirm`: a small round pop-up opens just above the Log out row. It holds one button: Log out. Nothing else goes dim. Opens on: a tap on Log out.
- `signed-out`: the sign-in page. A plain box stands for it. Opens on: Log out in the pop-up.

## Transitions

- `chat` to `drawer`. Trigger: tap on the menu button. Moves: the side menu comes in from the left with `drawer-in`, and the dim layer fades in with `scrim-in`. 300 ms, cubic-bezier(0.2, 0, 0, 1) for the side menu and linear for the dim layer. estimated.
- `drawer` to `chat`. Trigger: tap on the dim layer. Moves: the side menu leaves to the left with `drawer-out`, and the dim layer fades out with `scrim-out`. 250 ms, the same easings. estimated.
- `drawer` to `settings`. Trigger: tap on the account row. Moves: the Settings page comes in from the right with `push-enter`, 350 ms, cubic-bezier(0.32, 0.72, 0, 1). The side menu leaves with `drawer-out`, and the dim layer fades out with `scrim-out`, 250 ms. estimated.
- `settings` to `drawer`. Trigger: tap on Back. Moves: the Settings page leaves to the right with `back-exit`, 350 ms. The side menu comes back with `drawer-in`, and the dim layer with `scrim-in`, 300 ms. estimated. The source shows no picture of this change. The designer chose the side menu as the screen that Back shows.
- `settings` to `section`. Trigger: tap on a row with a chevron. Moves: the section comes in from the right with `push-enter`, and the list moves 30% to the left with `push-exit`. 350 ms, cubic-bezier(0.32, 0.72, 0, 1). estimated.
- `section` to `settings`. Trigger: tap on Back. Moves: the section leaves to the right with `back-exit`, and the list comes back with `back-enter`. 350 ms, the same easing. estimated.
- `settings` to `appearance-card`. Trigger: tap on the Appearance row. Moves: the card grows from 90% and fades in with `card-in`, 200 ms, ease-out. The dim layer fades in with `scrim-in`, 300 ms. estimated.
- `appearance-card` to `settings`. Trigger: tap on a choice, or on the dim layer. Moves: the card fades out with `card-out`, 150 ms, ease-in. The dim layer fades out with `scrim-out`, 250 ms. The page takes the new look at once, and the row shows the new value. estimated.
- `settings` to `sign-out-confirm`. Trigger: tap on Log out. Moves: the pop-up grows from 60% at its bottom center and fades in with `popover-in`. 250 ms, cubic-bezier(0.2, 0, 0, 1). estimated.
- `sign-out-confirm` to `settings` or `signed-out`. Trigger: tap outside the pop-up, or on Log out in it. Moves: the pop-up shrinks to 90% and fades out with `popover-out`. 150 ms, ease-in. estimated.

The pictures give no durations and no easings. Each value above is the designer's choice for a phone app of this kind.

## Hard cases

- Free and paid plans: on a free plan, the source shows an upgrade card under the email. The sketch shows only the plan at the right of the email.
- Long email: the email stops with an ellipsis, and the plan stays at the right.
- Another phone system: one version of the source shows the value of a choice under its label, not at the right. It shows the appearance choice in the same card in the center. Its Log out row is marked as dangerous, and it asks in an alert in the center with Cancel and Log out.
- Appearance on the source's other version: the row shows its value with up and down chevrons. The pictures do not show the open choice there. The sketch uses the card, which the pictures show.
- Escape on a keyboard: the sketch closes the card, the pop-up, the section, Settings or the side menu, in this order. The source shows no keyboard.
- Wide screen: the pictures show only phones. From 700 px, the sketch keeps the side menu open at the left and hides the menu button. Settings fills the place of the chat, beside the side menu, and its list is at most 640 px wide. Back shows the chat again. This is the designer's choice.
- Reduced motion: each change shows its end at once.
- Empty, error and slow network: the source shows no such state.

## Notes

- Settings is a page of its own. Back takes the person to the side menu, where they opened it.
- The groups have no names. With about 15 rows, space and a line are enough to show the groups.
- Each choice, such as the appearance, opens over the list and closes after one tap. The person never leaves the list for a choice.
- The sign-out asks with one small button next to the row. A second tap at the same place signs out, and a tap anywhere else keeps the person signed in.
- Left out because only the source has it: the upgrade card, the source's own names for its tools and connected apps, the font style row, and the plan names.
