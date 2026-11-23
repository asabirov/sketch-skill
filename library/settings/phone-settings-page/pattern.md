# Phone settings page

Captured: 2026-11-22, from public pictures
Best for: a phone app with about 15 settings, where a signed-in person opens Settings from the account button in the home bar and goes back with Back. Each choice applies at once, and a sign-out asks once more.
Row opens: on the record's own page
Related: `navigation/swipe-back` gives the drag back from a page. `settings/settings-window` is the settings of a desktop product. `settings/theme-switch-preview-cards` shows the appearance as cards with pictures.

## States

- `home`: the home screen of the app, with the title in the center and a round account button with the initials at the right of the bar. A plain box stands for its content. Opens on: Back in Settings. The source opens Settings from the account row at the foot of its side menu. The owner chose to leave the side menu out, so the account button is the designer's choice, not the source's.
- `settings`: Settings fills the screen. Its bar has Back at the left and the title "Settings" in the center. Under the bar, the email of the account, with the plan at the right. Then 4 groups with no names. A larger space separates them: the account (Profile, Billing), access (Security, Connected apps, Permissions), the look and the messages (Appearance, Language, Notifications) and the rest (Vibration, Privacy, Help). Log out is alone at the end, marked as the dangerous one. Each row has an icon at the left. A row that opens a page has a chevron at the right. A row with a choice shows its value and a down chevron. A row can have a second line, such as "2 connected". Opens on: a tap on the account button.
- `settings-labelled`: the same list, with a short label over each group: Account, Access, Preferences and More. It is Form `settings-labelled`, as the Notes say. The source shows no labels. Opens on: a tap on the account button, in a product that uses this form.
- `section`: the section of the row fills the screen. Its bar has Back at the left and the section name in the center. The sketch draws Privacy: a switch with a second line, a choice of two for the location (Ask each time, Always allow) and a delete action, marked as the dangerous one. A plain box with the name stands for each other section. The source shows no picture of an opened section. The sketch draws Privacy from the source's help text, with general words. Opens on: a tap on a row with a chevron.
- `appearance-card`: a card in the center of the screen, with the title "Appearance" and 3 rows: System, Light and Dark. Each row has an icon, and a tick marks the current choice. Everything under the card is dim. A tap on Light or Dark changes the look of the whole app at once. System follows the look of the device. Opens on: a tap on the Appearance row.
- `sign-out-confirm`: an alert in the center of the screen, with the title "Log out?" and two buttons at the right: Cancel and Log out. Log out is marked as the dangerous one. Everything under the alert is dim. The source asks this way on one of its two phone systems. Opens on: a tap on Log out.
- `signed-out`: the sign-in page. A plain box stands for it. Opens on: Log out in the alert.

## Transitions

- `home` to `settings`. Trigger: tap on the account button. Moves: the Settings page comes in from the right with `push-enter`. 350 ms, cubic-bezier(0.32, 0.72, 0, 1). estimated.
- `settings` to `home`. Trigger: tap on Back. Moves: the Settings page leaves to the right with `back-exit`. 350 ms, the same easing. estimated.
- `settings` to `section`. Trigger: tap on a row with a chevron. Moves: the section comes in from the right with `push-enter`, and the list moves 30% to the left with `push-exit`. 350 ms, cubic-bezier(0.32, 0.72, 0, 1). estimated.
- `section` to `settings`. Trigger: tap on Back. Moves: the section leaves to the right with `back-exit`, and the list comes back with `back-enter`. 350 ms, the same easing. estimated.
- `settings` to `appearance-card`. Trigger: tap on the Appearance row. Moves: the card grows from 90% and fades in with `card-in`, 200 ms, ease-out. The dim layer fades in with `scrim-in`, 300 ms. estimated.
- `appearance-card` to `settings`. Trigger: tap on a choice, or on the dim layer. Moves: the card fades out with `card-out`, 150 ms, ease-in. The dim layer fades out with `scrim-out`, 250 ms. The page takes the new look at once, and the row shows the new value. estimated.
- `settings` to `sign-out-confirm`. Trigger: tap on Log out. Moves: the alert grows from 90% and fades in with `card-in`, 200 ms, ease-out. The dim layer fades in with `scrim-in`, 300 ms. estimated.
- `sign-out-confirm` to `settings` or `signed-out`. Trigger: tap on Cancel or on the dim layer, or on Log out in the alert. Moves: the alert fades out with `card-out`, 150 ms, ease-in. The dim layer fades out with `scrim-out`, 250 ms. estimated.

The pictures give no durations and no easings. Each value above is the designer's choice for a phone app of this kind.

## Hard cases

- Free and paid plans: on a free plan, the source shows an upgrade card under the email. The sketch shows only the plan at the right of the email.
- Long email: the email stops with an ellipsis, and the plan stays at the right.
- Another phone system: one version of the source shows the value of a choice under its label, not at the right. It shows the appearance choice in the same card in the center. The sketch draws the sign out of this version. The other version asks with a small round pop-up just above the Log out row, with one Log out button, and a tap anywhere else keeps the person signed in. The owner did not like that pop-up.
- Appearance on the source's other version: the row shows its value with up and down chevrons. The pictures do not show the open choice there. The sketch uses the card, which the pictures show.
- Escape on a keyboard: the sketch closes the card, the alert, the section or Settings, in this order. The source shows no keyboard.
- Wide screen: the pictures show only phones. From 700 px, the home screen and Settings fill the window, and the list of Settings is at most 640 px wide. The card and the alert open in the center. This is the designer's choice.
- Back gesture: a drag from the left edge, or the system Back of the phone, does the same as Back. `navigation/swipe-back` draws the drag. This sketch draws only the Back button.
- Language: the row opens the same kind of card as Appearance, with the languages. The sketch does not draw it.
- Delete my data: the pictures show no confirmation. A product asks before it deletes, as Log out does.
- Reduced motion: each change shows its end at once.
- Empty, error and slow network: the source shows no such state.

## Notes

- Settings is a page of its own. Back takes the person to the home screen, where they opened it.
- Why no side menu: the source is a chat app. Its side menu is its main navigation, with the list of chats, and the account row at its foot opens Settings. The owner chose to leave the side menu out, because a product with no side menu could not use the pattern. A product that has a side menu can open Settings from an account row at its foot, as the source does.
- The groups have no names. With about 15 rows, space is enough to show the groups.
- Form `settings`: groups with no labels. Use it when each group has at most 4 rows, and the rows of a group clearly belong together.
- Form `settings-labelled`: a short label over each group. Use it when the list has more than 4 groups or more than 15 rows, or when a group mixes rows that a person does not expect together. The labels are optional. The source shows none.
- Each choice, such as the appearance, opens over the list and closes after one tap. The person never leaves the list for a choice.
- The sign-out asks once in an alert with Cancel and Log out, as the source does on one of its phone systems. Cancel, the dim layer and Escape keep the person signed in.
- Left out because only the source has it: the upgrade card, the rows for its tools, its voice and its shared links, the font style row, and the plan names. The sketch uses general rows that most signed-in apps have.
