# Settings window

Captured: 2026-11-20, from still pictures of the app window and of its settings window
Best for: a product with at most 4 groups of settings, where one person changes a setting and goes back to their work. For more than 4 groups, or for settings of a shared workspace, use `settings/settings-modal`.
Row opens: no rows. The window holds settings, and it holds no records.
Related: `settings/settings-modal`, the second pattern of the same part, for a product with more than 4 groups of settings. `navigation/user-menu` and `navigation/foot-menu`, the menus whose settings row opens this window. `settings/notification-settings-by-event` and `settings/notification-settings-by-channel`, the notification settings that the notifications tab holds.

## States

- `closed`: the page of the product. 2 icon buttons at the head of the side list open the settings window: an account button and a settings button. Opens on: the page load, Escape, the close button of the window, or a press outside the window from 600 px.
- `general`: the settings window, open on the general tab, the first tab. The window has its title in the middle. Below the title, each tab is an icon above a word, and the chosen tab has a box. The general tab has 2 sample settings, each with its label at the left and its control at the right. Opens on: the settings button, or the general tab.
- `themes`: the themes tab, with one card for each theme in 2 columns. The chosen card has a thick border. Opens on: the themes tab.
- `notifications`: the notifications tab. The notification settings are a part of `settings/notification-settings-by-event` or `settings/notification-settings-by-channel`, so the sketch draws them as a plain box with these names. Opens on: the notifications tab. The source has no such tab.
- `account`: the account tab, the last tab, with the name, the email, a profile button and the sign-out button. Opens on: the account button, or the account tab. The source has a sync tab in this place, and it has no account.
- `signed-out`: the signed-out page. It is a part of `navigation/user-menu`, so the sketch draws it as a plain box with that name. Opens on: the sign-out button. The source shows no such state, because it has no sign-out.

Limit: the window has at most 4 tabs, and the general tab is the first tab. A product with more than 4 groups of settings uses `settings/settings-modal`.

## Transitions

The capture is still pictures, so the agent read no transition from the source. Each value is the designer's choice: the sketch plays the values of the menu of `navigation/user-menu`.

- `closed` to `general`. Trigger: click the settings button. Moves: the window goes from clear to solid. 35 ms, ease-out. estimated.
- `closed` to `general`. Trigger: the same click. Moves: the window grows from 98% of its size to its full size. 160 ms, cubic-bezier(0, 0, 0.2, 1). estimated.
- `closed` to `account`. Trigger: click the account button. Moves: the window goes from clear to solid. 35 ms, ease-out. estimated.
- `closed` to `account`. Trigger: the same click. Moves: the window grows from 98% of its size to its full size. 160 ms, cubic-bezier(0, 0, 0.2, 1). estimated.
- `general`, `themes`, `notifications` or `account` to `closed`. Trigger: press Escape, click the close button or press outside the window. Moves: the window goes to 98% of its size. 20 ms, feed. estimated.
- `general`, `themes`, `notifications` or `account` to `closed`. Trigger: the same action. Moves: after a delay of 20 ms, the window goes from solid to clear. 110 ms, cubic-bezier(0, 0, 0.2, 1). estimated.
- One tab to a different tab, such as `general` to `themes`. Trigger: click the tab, or press the Left Arrow or the Right Arrow key on the row of tabs. Moves: the part below the tabs changes at once. 0 ms, none. estimated.
- `account` to `signed-out`. Trigger: click the sign-out button. Moves: the page changes at once. 0 ms, none. estimated.

## Hard cases

The source is a desktop app. So each case below 1000 px is the designer's choice, and the source does not show it.

- More than 4 groups of settings: the window does not fit. The owner set the limit of 4 tabs. The head row has no overflow control, it does not scroll sideways and it does not wrap. A product with more groups uses `settings/settings-modal`, and this record draws no such layout.
- From 600 px: the window is in the middle of the screen, and it is at most 560 px wide.
- Below 600 px: the window fills the screen. The tabs share its width, the cards are in 1 column, and each label is above its control. No press outside the window is possible, so the close button and Escape close it.
- 320 px screen: the 4 tabs of the sketch fit in the head row.
- Short screen: the title and the tabs keep their place, and only the part below the tabs scrolls. The keyboard focus then scrolls the whole card and its focus ring into view.
- Keyboard: Escape closes the window, and the focus goes back to the button that opened it. The Left Arrow and the Right Arrow keys change the tab.
- Failed save: not seen. The sketch saves nothing. A theme choice shows a sample message.
- Slow network and failed load: not seen. The window shows no data that loads.

## Notes

- The source has no user menu and no sign-in of its own, because it syncs through the account of the computer. The controls nearest to a user menu are 2 icon buttons at the head of the side list, one for sync and one for preferences. Each button opens the settings window, and the sync button opens it on the sync tab, the last tab.
- The sketch has the same 2 buttons. The settings button opens the general tab, and the account button opens the account tab. A product can also open the window from the settings row of `navigation/user-menu` or of `navigation/foot-menu`.
- The source has 5 tabs: general, typography, themes, app icon and sync. Its general tab is the first tab, and its preferences button and its general tab have the same icon. The sketch has 4 tabs for the use case: general, themes, notifications and account.
- The owner's rule for each part: one part has one pattern. So this record draws the window, its tabs and its own sample settings. It draws the notification settings and the signed-out page as plain boxes.
- The 2 settings of the general tab are sample content. A product puts its own general settings there.
- The source draws each theme card in the colours of its theme. The sketch has one ink, so each card has a name and one line of words.
- The source has no sign-out and no profile. The profile button and the sign-out button on the account tab are the designer's choice.
- Keep these parts when the look changes: the general tab is the first tab, the window has at most 4 tabs, the title and the tabs keep their place, and the focus goes back to the button that opened the window.
- The sketch keeps no brand and no picture of the source. The member and all words are sample content.
- The pictures of the source are not committed.
