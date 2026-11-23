# Settings

Captured: 2026-11-23, recorded by an agent from the public source code of the desktop app
Best for: a desktop work app with many groups of settings, where a person leaves the work for a time to find, change and check settings, then goes back to the work.
Row opens: no rows. The page holds settings, and it holds no records.
Related: `settings/settings-modal` shows a similar list of sections in a modal over the page, and the page stays in view below it. This record replaces the whole window. These parts sit inside this page, and the sketch draws each as a dashed box with its name: `settings/theme-switch-preview-cards` is the theme choice, and `settings/notification-settings-by-event` and `settings/notification-settings-by-channel` are the notification choices.

## States

The source is the public code of the app, read on 2026-11-23. It gives the layout, the states and the style values. The agent did not open the app on the screen. Each state that the code does not show is drawn, and its line says so.

- `general`: the settings page fills the window, in place of the work page. A column at the left, 280 px wide, has a "Back to app" button at the top, a search field below it, and the list of sections in named groups. Each section is a row with an icon and a name. The row of the open section has a fill and bold words. A bar at the top of the right side has the name of the open section and a close button. Below the bar, the right side shows only the open section: its title, one line about it, and its settings in groups. The title of a group is above the group, outside its outline. Each setting is a row, with a line between 2 rows: its name and one line about it at the left, and its control at the right. The right side is at most 784 px wide, in the middle of the space. Opens on: the page load, or the General row. In a product, the settings button of the app and Cmd+, open this page. The work page of the app is not a part of this record, so "Back to app", the close button and Escape show a note in the sketch. The search field has the focus when the page opens.
- `general-more`: the "More options" row at the foot of a group is open in place, and it shows 2 more settings under it, with an indent. Its arrow turns from right to down. Opens on: the "More options" row. The source has such rows in many sections.
- `appearance`: the Appearance section. Its Theme group is a dashed box that names `settings/theme-switch-preview-cards`, because that record draws the theme choice. The Text group has the UI zoom and the font size. A change takes effect at once, with no save button. Opens on: the Appearance row. The source has a choice of 3 theme words here.
- `account`: the Account section, for a person who is signed in. A group shows the avatar, the name and the email of the person, a "Signed in" word, and a "Sign out" button at the right. A second group lists what the account includes. Opens on: the Account row.
- `sign-out-confirm`: a confirmation over the settings page asks "Sign out?", with the buttons Cancel and Sign out. Cancel has the focus. Opens on: the "Sign out" button.
- `signed-out`: the Account section for a person who is not signed in. The group says "Not signed in", with one line about what the account gives, and a "Sign in" button at the right. Opens on: the Sign out button of the confirmation.
- `search-results`: the left column shows the settings that have the words of the search field, in place of the groups of sections. Each result shows the name of the setting and its place, such as "Interface / Appearance". The first result has a fill, so Enter opens it. The arrow keys move the fill. The right side keeps the open section. Opens on: words in the search field that a setting has.
- `search-empty`: the left column shows one line, which says that no setting has the words. The right side shows a dashed box with the same words. Opens on: words in the search field that no setting has.
- `sections`: below 600 px, the left column fills the screen. Opens on: the "Sections" button in the bar of a section, on a phone. The source shows no such state, because its window is at least 600 px wide. From 600 px, this state shows the same page as `general`.

## Transitions

The source code names each style value, so the agent read each value from the code and not from the screen. The capture script did not record the app. So each value is estimated. The page itself has no transition: it replaces the work page at once.

- The work page of the app to `general`, and back. Trigger: the settings button or Cmd+,, and "Back to app", the close button or Escape. Moves: one page replaces the other at once. 0 ms, none. estimated. The sketch has no work page, so it shows a note in place of the way back.
- One section to a different section, such as `general` to `appearance`. Trigger: click the row of the section. Moves: the fill of the section row changes, background-color 150 ms, cubic-bezier(0.4, 0, 0.2, 1). The right side changes at once. estimated.
- `general` to `general-more`, and back. Trigger: click the "More options" row. Moves: the arrow of the row turns 90 degrees, transform 150 ms, cubic-bezier(0.4, 0, 0.2, 1). The 2 settings show at once. estimated.
- `account` to `sign-out-confirm`. Trigger: click "Sign out". Moves: the confirmation goes from clear to solid and grows from 95% of its size to its full size, animation 200 ms, ease. The page below it goes pale, animation 150 ms, ease. estimated.
- `sign-out-confirm` to `account` or `signed-out`. Trigger: Cancel, Escape, or the Sign out button. Moves: the confirmation goes clear and goes to 95% of its size, animation 200 ms, ease. The pale layer goes clear, animation 150 ms, ease. estimated.
- A section to `search-results` or `search-empty`. Trigger: type in the search field. Moves: the left column changes at once. The fill of a result changes, background-color 150 ms, cubic-bezier(0.4, 0, 0.2, 1). estimated.
- `search-results` to the section of a result. Trigger: click the result or press Enter. Moves: the right side shows the section at once, and the search field keeps its words. estimated.
- `search-results` or `search-empty` to the section that was open. Trigger: clear the search field, or press Escape in it. Moves: the groups of sections show again at once. 0 ms, none. estimated.

## Hard cases

- Escape with words in the search field: the first Escape clears the words, and it does not close the settings. A second Escape closes the settings. Seen in the source.
- A change that is not saved: some settings have their own save step. When the person leaves the settings before that step, the source asks to keep or discard the change. The sketch has no such setting, because each of its changes takes effect at once.
- Many sections: the source lists about 40 sections in 8 groups, and a group for the projects of the person. The left column scrolls on its own, and the right side keeps its place. The sketch has 6 sections in 3 groups.
- Many settings in one section: the right side scrolls on its own, below the bar. The bar keeps its place, so the close button stays in view. A stable gutter keeps the content in place when the scroll bar comes and goes. Seen in the source.
- A narrow window, 600 to 999 px: the left column keeps its 280 px, and the right side gets narrow. In a few sections of the source, the title gets smaller and its line goes under the title, across the full width. The sketch does this in each section. The source window is at least 600 px wide.
- Below 600 px: the source has no such window. The sketch shows the open section in the full width. A "Sections" button in the bar opens the `sections` state, and a click on a section row opens that section. A control that is wider than a switch goes under the name of its setting. This is the designer's choice.
- Long name of a section or a setting: the name in the left column is cut with an ellipsis. On the right side, the name goes to a second line, and the control keeps its place.
- Keyboard: the Tab key goes from "Back to app" to the search field, then to the sections, then to the close button and the settings. In the search field, the up and down arrows move the fill in the results, and Enter opens the result with the fill.
- Sign out: the source asks before it signs out. Not signed in, the section shows a sign-in button in place of the account.
- Slow network and failed load: the source shows "Checking account status" while it reads the account. The sketch draws no such state.

## Notes

- This record replaces the whole window, so the settings get the full height and width. Keep the "Back to app" button at the top of the left column, and the close button at the top of the right side. Each one goes back to the work.
- The bar of the right side and the top of the left column have the same height, so their bottom lines meet in one line.
- Only the open section shows on the right side. The page does not scroll through all sections.
- The source has parts that only that app needs: a setup checklist row at the top of the left column, a list of the projects of the person, a choice of the computer that the settings apply to, badges on some section rows, and an app icon choice. The sketch leaves them out.
- The source gives one animation name to the confirmation and to its pale layer. This record names the layer `enter_layer` and `exit_layer`, so that `compare` tells the 2 apart.
- The 6 sections and their settings are sample content. A product puts its own sections in its own groups.
- The owner's rule for each part: one part has one pattern. So this record draws no theme choice and no notification choices. Each is a dashed box with the name of the pattern that draws it.
