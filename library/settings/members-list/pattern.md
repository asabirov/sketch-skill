# Members list

Captured: 2026-11-22, from public pictures
Best for: a person who manages a shared account, such as a family or a small team, sees each member with a role and the last activity, invites a member with a role, decides on a request to join, and signs a member out of one device or of all devices. For the profile that other members see, use `profile/member-profile`.
Row opens: on the record's own page. Each row of the source ends with a chevron and opens the page of the person. The help text of the source says that this page shows the join date and the action that made the person join.
Related: `profile/member-profile`, the public page of a member. `settings/settings-modal`, a settings window that can hold this list for a shared workspace. `account/connected-apps`, a list of outside apps with a disconnect after a confirmation.

## States

The agent read 3 public pictures of the source and the text of 3 help pages. The pictures show the list of people, the list with 2 checked rows and the bar of actions, and the invite dialog. The help text names the filters, the pending status, the bulk actions and the confirmation of a remove. The source has no request to join in this list and no devices. The owner asked for both, so the agent drew them.

- `list`: the title with Invite at the right, a bar with a search and a Filter button, and a table. Each row has a check box, the picture, the name with the email below it, the role, the last activity and a chevron. A status word follows the name: "You" for the person who looks at the list, "Invited" for an invite that is not accepted yet, and "Asks to join" for a request that waits. The row of the person who looks at the list has no check box. Opens on: Members in the side list. The source shows the title, Invite, the search, the filter button, the check box, the picture, the name, the email, a word after the name ("Guest"), a type column, the last activity and the chevron. The "Invited" and "Asks to join" words are drawn. The help text of the source names a "Pending" type for an invite that is not accepted.
- `filter`: a popover below Filter with check boxes for each role and for each status. The rows that do not match go at once. Opens on: a click on Filter. The help text names the filter groups. The popover is drawn.
- `selected`: 2 rows are checked and marked. A filled bar floats at the foot of the screen. It names the count and has Copy emails, Change role with a chevron, Remove and a close button. Opens on: a check on a row. The source shows this filled bar with the count, Copy emails, 2 actions with a chevron, Remove and a close button.
- `bulk-role`: the menu of Change role is open above the bar. Each role has its icon, its name and one line about what it can do. Opens on: Change role in the bar. The source shows the chevron but no open menu, so the menu is drawn.
- `invite`: a dialog with 2 tabs at the top, Invite by email and Invite link, and a close button. The email tab has an email field for one or more emails, a role field that shows the icon of the role, one line that says the role applies after the person accepts, Cancel and Send invite. Send invite stays off until an email is typed, and a line beside it says so. The focus starts on Cancel. Opens on: Invite. The source shows this dialog with the 2 tabs, the close button, the email field, the field with an icon, Cancel and Send invite while it is off. The line that says why Send invite is off is drawn.
- `invite-link`: the link tab of the invite dialog. One line says that anyone with the link can ask to join, and that each request waits for approval. A switch turns the link on or off. The link has Copy link, and Reset link makes a new link. Opens on: the Invite link tab. The help text of the source names the switch, Copy link and Reset link. The layout is drawn. A request from the link shows in the list as "Asks to join".
- `invited`: the list with a new row for the invited email with the "Invited" word, and a toast that names the email. Opens on: Send invite. The source shows no such state.
- `member`: the page of a member. A back link, a head with the picture, the name, the email and Edit at the right, and a line below. On the left are the role field with the icon of the role, the devices with Sign out on each device, Sign out of all devices, and Remove with one line that says what Remove does. On the right are the facts: joined, joined by and last active. Opens on: a click on a name or a chevron. The source shows no picture of this page. Its help text names the join date and the action that made the person join. The devices, the sign-out actions, Edit and the layout are drawn.
- `edit`: a dialog on the member page with the name field, the email field, one line that says a new email takes effect after the member confirms it, Save and Cancel. The focus starts on the name field. Opens on: Edit on the member page. The source shows no such state.
- `sign-out`: a confirmation names the device and says that the member stays signed in on the other devices. It has Sign out and Cancel, and the focus starts on Cancel. Opens on: Sign out on a device. The source shows no such state.
- `signed-out`: the page without the device, and a toast that names the member and the device. Opens on: Sign out in the confirmation. The source shows no such state.
- `remove`: a confirmation names the member and says what stops. Remove member stays off until the check box "I understand that this cannot be undone" is on, and a line beside it says so. Opens on: Remove on the member page. The help text of the source names this check box and the Remove member button. The layout is drawn.
- `request`: the page of a request. The head has the "Asks to join" word. A box has the role asked for, the message of the person, a role field with icons for after the approval, Approve and Decline. The facts say when the person asked and where the request came from. Opens on: a click on a row with "Asks to join". The source shows no such state.
- `approved`: the list with the row of the new member without the "Asks to join" word, and a toast. Opens on: Approve. The source shows no such state.

## Transitions

The source gives only still pictures, so no value is measured. `transitions.json` is empty, because each change in the sketch shows at once.

- `list` to `filter`, and back. Trigger: a click on Filter, a click outside, or Escape. Moves: the popover shows and goes. 0 ms, none. estimated.
- `filter` and `list` search. Trigger: a check in the popover, or typing in the search. Moves: the rows that do not match go. 0 ms, none. estimated.
- `list` to `selected`, and back. Trigger: a check on a row, or the close button of the bar. Moves: the row is marked, and the bar shows at the foot with the count. 0 ms, none. estimated.
- `list` to `invite` to `invited`. Trigger: a click on Invite, then on Send invite. Moves: the dialog opens, then the new row and the toast show. 0 ms, none. estimated.
- `invite` to `invite-link`, and back. Trigger: a click on a tab, or the arrow keys. Moves: the panel of the tab shows. 0 ms, none. estimated.
- `selected` to `bulk-role`, and back. Trigger: a click on Change role, a role, a click outside, or Escape. Moves: the menu shows and goes. 0 ms, none. estimated.
- `list` to `member`, and back. Trigger: a click on a name or a chevron, or on the back link. Moves: the page content. 0 ms, none. estimated.
- `member` to `sign-out` to `signed-out`. Trigger: Sign out on a device, then Sign out in the confirmation. Moves: the confirmation opens, then the device row goes and the toast shows. 0 ms, none. estimated.
- `member` to `edit`, and back. Trigger: Edit, then Save, Cancel or Escape. Moves: the dialog opens, then Save closes it and shows a toast. 0 ms, none. estimated.
- `member` to `remove`. Trigger: Remove. Moves: the confirmation opens. 0 ms, none. estimated.
- `list` to `request` to `approved`. Trigger: a click on a row with "Asks to join", then Approve. Moves: the page content, then the list with the new member and the toast. 0 ms, none. estimated.

## Hard cases

- Empty invite: Send invite stays off until the email field has an email. A line beside the button says why, because the words of an off button are dim.
- Tabs of different size: the 2 tab panels share one area, so the dialog keeps its size and place when the tab changes. The line under the tabs is the only line of the dialog head.
- Invite link: a reset stops the old link at once. A request from the link always waits for approval, so a link that leaks adds no member by itself.
- Own row: the person who looks at the list cannot check or remove their own row. The row has no check box and shows "You".
- Last admin: not seen. Remove and a change of role stay off for the last admin, with one line that says why.
- Invite not accepted: the row shows the email in place of the name, "Invited", the role chosen in the invite and when the invite went. The page of an invite has Send again and Cancel invite in place of the devices. This page is not drawn.
- Request declined: the row goes, and a toast says that the person gets a message.
- Roles: the sketch uses 3 general roles, Admin, Member and Viewer, with a settings, a person and an eye icon. A product puts its own roles in their place.
- Lost device: Sign out on one device keeps the member signed in on the others. Sign out of all devices ends each session, also the session on the device in use, after one confirmation.
- No undo: Remove signs the member out of each device and ends the access. So the confirmation needs a check box, as the source does.
- No match: the search and the filter show one line that says no member matches.
- Long name and email: the name and the email wrap. The role and the last activity stay in their own columns. The chevron stays at the right.
- Keyboard: Tab goes to the check box, the name, then the chevron of each row. Escape closes the popover and each dialog, and the focus goes back to the button that opened it.
- Screen reader: each check box and each chevron has the name of the person in its label, such as "Select Mia Reyes" and "Open Mia Reyes".
- Narrow screen: at 390 px each row puts the check box at the left, the chevron at the right, and the role and the last activity on one line under the email. The facts of a member page go below the devices. The source shows only a wide window, so the phone width is drawn.
- Long list: the table scrolls with the page, and the bar of checked rows stays at the foot of the screen.
- Slow network: not seen.

## Notes

- The list keeps each person on one row with the 3 facts that an admin scans: who, which role, and when last active. Each special case is a word after the name, not a separate list. So an invite and a request show beside the members, and the filter finds them.
- Each decision about one person happens on the page of that person: the name and the email, the role, the devices, Remove, and Approve or Decline for a request. The list holds only the actions for many people at once.
- Each role field shows the icon of the role, and its menu gives one line about what each role can do. An admin then chooses a role without a separate help page.
- Keep these parts when the look changes: the status word after the name, the chevron that opens the person, the floating bar of actions for checked rows, the 2 tabs of the invite dialog, the role field with icons, Send invite that stays off until an email is typed, Edit on the person page, the devices on the person page with Sign out on each device, and a Remove confirmation with a check box.
- The pattern has no side list and no top bar. The product puts the page in its own frame, such as `settings/settings-modal`.
- Left out to make the pattern general: the side list of the admin area and the account switch, the back and forward arrows, the seat type pictures, the access column for paid credits, the billing group column and filter, the billing cycle, charge, last edit and workspace filters, the download of a file of members, the user groups tab, and the change workspace and change billing group actions.
- The role column of the source holds a paid seat type. The sketch uses a role in its place, because each product with members has roles.
- The sketch keeps no brand, no colour and no picture of the source. All words are sample content.
- The pictures of the source are not committed.
