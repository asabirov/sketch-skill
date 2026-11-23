# Settings modal

Captured: 2026-11-20, from public pictures
Best for: a product with more than 4 groups of settings, where a person finds one setting of their account or of a shared workspace.
Row opens: no rows. The modal holds settings, and it holds no records.
Related: `navigation/user-menu` and `navigation/foot-menu`, the menus whose settings row can open this modal. `settings/notification-settings-by-event` and `settings/notification-settings-by-channel`, the notification settings that the notifications section holds.

## States

The pictures show the modal on 3 sections: the notifications section, the account section below a confirmation, and an analytics section. Each state that the pictures do not show is drawn, and its line says so.

- `closed`: the page of the product. A settings button at the head of the side list opens the modal. Opens on: the page load, Escape, the close button of the modal, or a press outside the modal from 600 px. The pictures show the page only below the open modal.
- `account`: the modal, open over the page on the first section, My account. The modal is large, and the page below it is pale. A left column has a search field and the list of sections in 2 groups, Account and Workspace. Each section is a row with an icon and a name. The row of the open section has a light fill and bold words. The right side shows the title of the open section and its settings. Each setting is a row, with its name and one line about it at the left and its control at the right. A close button is at the top of the right side. Opens on: the settings button, or the My account row. The pictures show this section only below a confirmation, so its 3 settings are drawn. The help text names a name, an email and a two-step sign-in.
- `preferences`: the Preferences section, with 3 settings that each have a list field. Opens on: the Preferences row. The pictures show no such section. The help text names the section and its list field for the language. The other 2 settings are sample content.
- `notifications`: the Notifications section. The notification settings are a part of `settings/notification-settings-by-event` or `settings/notification-settings-by-channel`, so the sketch draws them as a plain box with these names. Opens on: the Notifications row. The pictures show this section with its switches.
- `general`: the General section of the Workspace group, with a text field, a switch and a list field. Opens on: the General row. The pictures show no such section. The help text names the workspace name and the switch for page analytics. The week start is sample content.
- `security`: the Security section of the Workspace group, with 3 switches. Opens on: the Security row. The pictures show no such section. The help text names the section and a setting for each of these 3 subjects.
- `search-results`: the left column shows the settings that have the words of the search field, in place of the list of sections. Each result shows the name of the setting and its place, such as "Workspace / General". The right side keeps the open section. Opens on: words in the search field that a setting has. The pictures show no such state. The help text describes it.
- `search-empty`: the left column shows one line, which says that no setting has the words. Opens on: words in the search field that no setting has. The source shows no empty state.

## Transitions

The capture is public pictures, so the agent read no transition from the source. Each value is the designer's choice: the sketch plays the values of the menu of `navigation/user-menu`.

- `closed` to `account`. Trigger: click the settings button. Moves: the modal goes from clear to solid. 35 ms, ease-out. estimated.
- `closed` to `account`. Trigger: the same click. Moves: the modal grows from 98% of its size to its full size. 160 ms, cubic-bezier(0, 0, 0.2, 1). estimated.
- An open state to `closed`. Trigger: press Escape, click the close button or press outside the modal. Moves: the modal goes to 98% of its size. 20 ms, linear. estimated.
- An open state to `closed`. Trigger: the same action. Moves: after a delay of 20 ms, the modal goes from solid to clear. 110 ms, cubic-bezier(0, 0, 0.2, 1). estimated.
- One section to a different section, such as `account` to `general`. Trigger: click the row of the section. Below 600 px, choose the section in the list field. Moves: the right side changes at once. 0 ms, none. estimated.
- A section to `search-results` or `search-empty`. Trigger: type in the search field. Moves: the left column changes at once. 0 ms, none. estimated.
- `search-results` to the section of a result. Trigger: click the result. Moves: the right side shows the section at once. 0 ms, none. estimated. The row of the setting then has a light fill for 2000 ms. The help text says that the source marks the setting "briefly", so this time is estimated.
- `search-results` or `search-empty` to the section that was open. Trigger: clear the search field, or press Escape in it. Moves: the list of sections shows again at once. 0 ms, none. estimated.

## Hard cases

The pictures show the modal only in a wide window. So each case below 1000 px is the designer's choice, unless its line names the source.

- Size, from 600 px: the modal is in the middle of the screen. In the pictures, it takes about 92% of the width and 87% of the height of the window, and the left column takes about 22% of the modal. Each of these values is estimated. In the sketch, the modal is at most 1040 px wide and 720 px high, and the left column is 200 to 260 px wide.
- Many sections: the source lists about 20 sections. Its left column scrolls on its own, and the right side keeps its place. The sketch has 5 sections, and its left column scrolls in the same way on a short screen.
- Many settings in one section: in the source, the right side scrolls on its own. In the sketch, the title of the section keeps its place and the rows below it scroll. So no words go below the close button.
- A member who is not an owner: the help text says that the member sees only the settings that they can change. The sketch draws the view of an owner.
- Search: the help text says that the search reads the name of a setting, its description and the name of its section. It also says that some settings are not in the search yet. The sketch reads the same 3 parts of its sample settings.
- A setting with a button: the source has rows whose control is a button, such as the button that changes the email. The button opens a form or a confirmation over the modal. The sketch draws no such row.
- A dangerous setting: the source opens a confirmation over the modal, and the modal stays below it. The person types their email to confirm. The sketch draws no such setting.
- A section with its own tabs: the analytics section of the source has a row of tabs below its title. The sketch draws no such section.
- Below 600 px: the modal fills the screen. A head row has the name of the modal and the close button. A list field with the 2 groups replaces the list of sections, and the open section is below it. A text field or a list field is below the name of its setting, and a switch stays at the right. The results of a search take the place of the list field and of the open section. The source differs: its phone app shows the settings as one page with a Done button, and the help text says that many workspace settings are not in the phone app.
- 320 px screen: each state fits, and no words are cut.
- Long name of a section or of a setting: the name goes to a second line, and the control keeps its place.
- Keyboard: the Tab key goes from the close button to the search field, then to the sections, then to the settings. Escape closes the modal, and the focus goes back to the settings button. In a search field with words, Escape first clears the words. After a click on a result, the focus is on the control of the setting. Not seen in the source.
- Browser history: each section has its own address, so the Back button goes to the section before. A search changes the address in place, so it adds no step. Not seen in the source.
- Failed save: not seen. The pictures show no save button, so each change takes effect at once. The sketch saves nothing.
- Slow network and failed load: not seen. The modal shows no data that loads.

## Notes

- The help text says that a Settings row in the side list of the source opens the modal. The sketch has a settings button at the head of the side list. A product can also open the modal from the settings row of `navigation/user-menu` or of `navigation/foot-menu`.
- The source shows the name and the email of the member below the Account label. The sketch leaves them out, because its My account section shows them.
- The left column of the source has a light grey fill. The sketch has one ink, so a line divides the 2 parts.
- The 5 sections and their 12 settings are sample content. A product puts its own sections in its own groups.
- The owner's rule for each part: one part has one pattern. So this record draws the modal, its list of sections, its search and its own sample settings. It draws the notification settings as a plain box.
- Keep these parts when the look changes: the name of each group, the list of sections that stays on the screen from 600 px, the place in each search result, and the focus that goes back to the button that opened the modal.
- The sketch keeps no brand and no picture of the source. The member and all words are sample content.
- The pictures of the source are not committed.
