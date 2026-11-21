# Connected apps

Captured: 2026-11-21, from public pictures and help text
Best for: a signed-in reader sees each outside app that uses their account, with its access, the connect date and the last use, and takes the access back from one app or from all apps. The list fits a phone and a desktop. For a short list of the clients of a workspace inside a settings window, use `account/oauth-consent`.
Row opens: a page of its own. The app name opens a page with the full access of the app. The source help text says that the app name opens such a page.
Related: `account/oauth-consent`, the consent page that adds an app to this list, and a short list of clients in a settings window. `settings/settings-window`, the window form of settings. `navigation/user-menu`, the menu that opens Settings.

## States

The source picture shows the list at desktop width, with 2 apps. The help text names the row menu, Revoke, the confirmation and Revoke all. Each other state is drawn, and its line says so.

- `list`: the Settings page, with Connected apps chosen in the side list. A line gives the count of apps. Sort and Revoke all are at the right of that line. Each row has the app picture, the app name, the owner, a short access line, and a line with the connect date and the last use. A More button is at the top right of each row. Opens on: Connected apps in the side list of Settings. The picture shows this state with the name, the last use, the owner, Sort, Revoke all and the More button. The access line and the connect date are drawn, because the source shows them only on the page of the app or not at all.
- `menu`: the row menu of the first app is open below its More button. It has See the access and Revoke access. Opens on: a click on More. The help text names Revoke in this menu. See the access is drawn.
- `confirm`: a confirmation over the list names the app and says what stops. It has Revoke access and Cancel, and the focus starts on Cancel. Opens on: Revoke access in the row menu, or on the page of the app. The help text names a confirmation. Its words are drawn.
- `revoked`: the list without the app, with the new count, and a toast that names the app. Opens on: Revoke access in the confirmation. The source shows no such state.
- `confirm-all`: a confirmation over the list gives the count of apps and says that each app must ask again. It has Revoke all and Cancel. Opens on: Revoke all. The help text names Revoke all. The confirmation is drawn.
- `empty`: one line says that no app uses the account, and where a new app shows. Sort and Revoke all are off. A toast says that no app can use the account now. Opens on: Revoke all in its confirmation, or the revoke of the last app. The source shows no empty list.
- `app`: the page of one app, with a link back to the list, the app picture and name, the owner, the connect date, the last use, the website, a list of what the app can do, and Revoke access. Opens on: the app name, or See the access in the row menu. The help text says that this page shows the access of the app. The layout is drawn.

## Transitions

The capture is public pictures, so the agent read no transition from the source. `transitions.json` is empty, and each value is the designer's choice.

- `list` to `menu`. Trigger: a click on More. Moves: the menu opens below the button. 0 ms, none. estimated.
- `menu` to `confirm`, and `list` to `confirm-all`. Trigger: a click on Revoke access or Revoke all. Moves: the confirmation opens over the list. 0 ms, none. estimated.
- `confirm` to `revoked`, and `confirm-all` to `empty`. Trigger: a click on the revoke button in the confirmation. Moves: the row goes, and the toast shows. 0 ms, none. estimated.
- `list` to `app`, and back. Trigger: a click on the app name, or on the back link. Moves: the page content. 0 ms, none. estimated.

## Hard cases

- No undo: a revoke ends the access at once. The app must ask again. So each revoke needs a confirmation, and the confirmation names the app and its access.
- Revoke all: the confirmation gives the count of apps. Cancel has the first focus, so a quick Enter revokes nothing.
- Never used: an app that is connected but not used shows "Never used" in place of a last use.
- Rough last use: the source gives the last use as a span, such as "within the last week", not as a date. Keep the span, because an exact time tells more than the reader needs.
- Owner: an app of a person and an app of a company both show an owner. A reader decides on trust from this line.
- Failed revoke: not seen. The row stays, and a message says that the access is not revoked yet, with Try again.
- Keyboard: Tab goes to the app name, then to More. The arrow keys move in the menu. Escape closes the menu or the confirmation, and the focus goes back to the button that opened it.
- Screen reader: each More button has the app name in its label, such as "More actions for Notes Sync".
- Narrow screen: at 390 px the count line goes above Sort, and Revoke all goes to its own line. The facts of a row wrap below the name. A long app name wraps, and the More button stays at the top right. On the page of the app, each label goes above its value. Each state fits at 320 px. The picture shows only a wide window.
- Long list: not seen. The list scrolls with the page. Sort changes the order: Last used, Name or Connect date.
- Slow network: not seen. The list needs a load. A product shows the head of the list and empty rows while it loads.

## Notes

- The 3 facts that the reader needs before a revoke are the access, the connect date and the last use. The source shows the last use on the row, and the access only on the page of the app. The sketch puts a short access line on the row, so that a reader can decide from the list.
- Keep these parts when the look changes: the count above the list, Revoke all apart from the rows, the More button at the end of each row, the owner line, a confirmation that names the app, and a page of each app with its full access.
- The source has tabs above the list for 2 other kinds of apps. They are a different part, so the sketch leaves them out.
- The source marks Revoke all in red. The sketch has one ink, so Revoke all is a plain button.
- The sketch keeps no brand, no colour and no picture of the source. All words are sample content.
- The pictures of the source are not committed.
