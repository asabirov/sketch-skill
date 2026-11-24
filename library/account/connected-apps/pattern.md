# Connected apps

Captured: 2026-11-21, from the signed-in web app, recorded by an agent in a browser
Best for: a signed-in reader sees each outside app that uses their account, with its access, the connect date and the last use, and disconnects one app after a confirmation. For a short list of the clients of a workspace inside a settings window, use `account/oauth-consent`.
Row opens: on the record's own page. The app name opens a page with the access of the app. The source opens such a page from the name.
Related: `account/oauth-consent`, the consent page that adds an app to this list, and a short list of clients in a settings window. `settings/settings-modal`, the window form of settings. `navigation/user-menu`, the menu that opens the account pages.

## States

The agent recorded the list of the reader's own apps, the page of a connected app, the page of an app that is not connected, and each menu of these pages. The source puts Disconnect in a row menu with one item. The owner chose a direct button, so the sketch has no row menu. The owner then asked for a general form. So the sketch keeps the layout of the source and only the parts that each product with connected apps needs. Notes lists the parts of the source that the sketch leaves out.

- `list`: the title, a bar with a search and Add app, and one row for each connected app. Each row has the app picture at the top left, the name with a verified mark, a line of what the app can do, and a line with the maker, the connect date and the last use. A Disconnect button is at the right of each row. Opens on: Connected apps in the side list. The source shows the bar, the picture, the name, the mark, the maker and a More button. The access line, the connect date and the last use are drawn, because the issue asks for them and the source shows none of them in the row. The Disconnect button is drawn in place of the More button.
- `confirm`: a confirmation over the list names the app and says what stops. It has Disconnect and Cancel, and the focus starts on Cancel. Opens on: Disconnect in the row, or Disconnect on the app page. The agent did not choose Disconnect in the source, because it would disconnect the owner's real app. So the confirmation is drawn.
- `disconnected`: the list without the app, and a toast that names it. Opens on: Disconnect in the confirmation. The source shows no such state.
- `empty`: one line says that no app uses the account, and that an app shows after a connect. The search goes, because there is nothing to search. Add app stays. Opens on: the disconnect of the last app. The source shows no empty list.
- `app`: the page of one app. A head has the picture, the name, the maker with a short description and a Connected badge, with a line below. On the left are the description, the list of what the app can do, and a box that says the account is connected, with Disconnect. On the right is a column of facts: developer with a Verified badge, where the app sends data, the connect date and the last use. Opens on: the app name. The source shows the head, the description, the box with Disconnect and the facts column. The access list, the connect date and the last use are drawn.

## Transitions

The agent read each transition in the signed-in browser. It started a recorder of `document.getAnimations()` before each click. The capture script was not used, because the page needs the owner's sign-in. `transitions.json` is empty, because each change that the sketch keeps shows at once.

- `list` search. Trigger: typing in the search. Moves: the rows that do not match go. 0 ms, none. measured on the URL filter of the source.
- `list` to `confirm`. Trigger: a click on Disconnect in the row. Moves: the confirmation opens. 0 ms, none. estimated.
- `confirm` to `disconnected`. Trigger: a click on Disconnect in the confirmation. Moves: the row goes, and the toast shows. 0 ms, none. estimated.
- `list` to `app`, and back. Trigger: a click on the app name, or on the back link. Moves: the page content. 0 ms, none. measured. While the page loads, the source shows grey blocks that fade in and out in 2000 ms, linear, with 90 ms between blocks. The sketch has no load state.

## Hard cases

- No undo: a disconnect ends the access at once. The app must be connected again. So each disconnect needs a confirmation, and the confirmation names the app and its access.
- Two ways to disconnect: the button in the row and the box on the app page. Each one opens the same confirmation.
- Never used: an app that is connected but not used shows "Never used" in place of a last use.
- Maker: an app of a company and an app of a person both show a maker. A verified mark shows only for a checked maker. A reader decides on trust from this line.
- Failed disconnect: not seen. The row stays, and a message says that the app is still connected, with Try again.
- No match: the search shows one line that says no connected app matches.
- Facts line: each fact is its own part. On a narrow screen a line breaks between facts, never inside one.
- Keyboard: Tab goes to the app name, then to Disconnect. Escape closes the confirmation, and the focus goes back to the Disconnect button.
- Screen reader: each Disconnect button has the app name in its label, such as "Disconnect Notes Sync". The verified mark has the label "Verified".
- Narrow screen: at 390 px the facts of a row wrap below the name. A long app name wraps, and the Disconnect button goes below the facts. On the app page, the badge goes below the name, and the facts column goes below the box. Each state fits at 320 px. The agent recorded only a wide window, so the phone width is drawn.
- Long list: not seen. The list scrolls with the page, and the search makes it short.
- Slow network: the source shows grey blocks while a page loads, as Transitions says.

## Notes

- The 3 facts that the reader needs before a disconnect are the access, the connect date and the last use. The source shows the access only on the page of an app. The sketch puts a short line of what the app can do on each row, so that a reader can decide from the list.
- A row with one action shows that action as a direct button. Use a row menu only when a row has more than one action.
- Keep these parts when the look changes: the Disconnect button of each row, the maker line with the verified mark, a confirmation that names the app, and a page of each app with its access facts.
- Left out to make the pattern general: the catalog sections around the list, the kind filter (all, connectors, skills), the filter menu (verified, community), the items of the Add menu, the group of included skills, the connector box with its address, tools and menu, the More menu of the app page, the related apps, the share button, the category, the listed date and the developer links. A product with more than one kind of app can add a kind filter above the list.
- Measured motions of the parts that are left out, as a proposal for a product that keeps them: a group opens in 200 ms, cubic-bezier(0.165, 0.84, 0.44, 1), and its arrow turns in 60 ms, cubic-bezier(0.4, 0, 0.2, 1). The chosen mark of the kind filter slides in 200 ms, cubic-bezier(0.32, 0.72, 0, 1).
- The sketch keeps no brand, no colour and no picture of the source. All words are sample content.
- The pictures of the source are not committed.
