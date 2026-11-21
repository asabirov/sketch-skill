# Connected apps

Captured: 2026-11-21, from the signed-in web app, recorded by an agent in a browser
Best for: a signed-in reader sees each outside app that uses their account, with its access, the connect date and the last use, and disconnects one app after a confirmation. The list fits a phone and a desktop. For a short list of the clients of a workspace inside a settings window, use `account/oauth-consent`.
Row opens: a page of its own. The app name opens a page with the access of the app. The source opens such a page from the name.
Related: `account/oauth-consent`, the consent page that adds an app to this list, and a short list of clients in a settings window. `settings/settings-window`, the window form of settings. `navigation/user-menu`, the menu that opens the account pages.

## States

The agent recorded the list of the reader's own apps, the page of a connected app, the page of an app that is not connected, and each menu of these pages. The sketch follows the layout of these screens. It leaves out the catalog sections around the list. Each drawn part says so.

- `list`: a back link to the catalog, the title, and a bar with a search, a kind filter (All, Connectors, Skills), a filter button and an Add button. Below it are the heading Active and one row for each connected app. Each row has the app picture, the name with a verified mark, a line of what the app can do, and a line with the kind, the maker, the connect date and the last use. A More button is at the right of each row. A row with an arrow below the list opens the included parts. Opens on: Apps in the side list. The source shows the bar, the picture, the name, the mark, the kind, the maker, the More button and the Included row. The access line, the connect date and the last use are drawn, because the issue asks for them and the source shows none of them in the row.
- `menu`: the row menu is open below its More button, with one item, Disconnect. Opens on: a click on More. The source shows this menu with Disconnect only.
- `confirm`: a confirmation over the list names the app and says what stops. It has Disconnect and Cancel, and the focus starts on Cancel. Opens on: Disconnect in the row menu, in the menu of the app page, in the menu of the connector box, or in the account part of the box. The agent did not choose Disconnect in the source, because it would disconnect the owner's real app. So the confirmation is drawn.
- `disconnected`: the list without the app, and a toast that names it. Opens on: Disconnect in the confirmation. The source shows no such state.
- `empty`: one line says that no app uses the account, and that a new app shows after an add from the catalog. Opens on: the disconnect of the last app. The source shows no empty list.
- `app`: the page of one app. A head has the picture, the name, the maker with a short description, an Added badge and a More button, with a line below. On the left are the description and a Connectors box. The box has the connector name, Connected, a More button, an arrow that opens the details (address, tools, sign-in), and a part that says the account is connected, with Disconnect. On the right is a column of facts: developer with a Verified badge, safety and access, authorization, connected and last used. Opens on: the app name. The source shows each of these parts, except the connected date and the last use, which are drawn.

## Transitions

The agent read each transition in the signed-in browser. It started a recorder of `document.getAnimations()` before each click. The capture script was not used, because the page needs the owner's sign-in.

- `list` group-open. Trigger: a click on the Included row, or on the arrow of the connector box on `app`. Moves: the group grows to its full height. 200 ms, cubic-bezier(0.165, 0.84, 0.44, 1). measured.
- `list` group-open. Trigger: the same click. Moves: the arrow turns. 60 ms, cubic-bezier(0.4, 0, 0.2, 1). measured.
- `list` kind-filter. Trigger: a click on All, Connectors or Skills. Moves: the chosen mark slides to the new choice. 200 ms, cubic-bezier(0.32, 0.72, 0, 1). measured. The rows change at once. The sketch moves the mark at once.
- `list` to `menu`, and back. Trigger: a click on More, or Escape. Moves: the menu shows and goes. 0 ms, none. measured: the menu has no transition and no animation.
- `menu` to `confirm`. Trigger: a click on Disconnect. Moves: the confirmation opens. 0 ms, none. estimated.
- `confirm` to `disconnected`. Trigger: a click on Disconnect in the confirmation. Moves: the row goes, and the toast shows. 0 ms, none. estimated.
- `list` to `app`, and back. Trigger: a click on the app name, or on the back link. Moves: the page content. 0 ms, none. measured. While the page loads, the source shows grey blocks that fade in and out in 2000 ms, linear, with 90 ms between blocks. The sketch has no load state.

## Hard cases

- No undo: a disconnect ends the access at once. The app must be connected again. So each disconnect needs a confirmation, and the confirmation names the app and its access.
- Four ways to disconnect: the row menu, the menu of the app page, the menu of the connector box and its account part. Each one opens the same confirmation.
- Never used: an app that is connected but not used shows "Never used" in place of a last use.
- Maker: an app of a company and an app of a person both show a maker. A verified mark shows only for a checked maker. A reader decides on trust from this line.
- Failed disconnect: not seen. The row stays, and a message says that the app is still connected, with Try again.
- Keyboard: Tab goes to the app name, then to More. The arrow keys move in the menu. Escape closes the menu or the confirmation, and the focus goes back to the More button.
- Screen reader: each More button has the app name in its label, such as "More actions for Notes Sync". The verified mark has the label "Verified".
- Reduced motion: a group opens with no motion.
- Narrow screen: at 390 px the facts of a row wrap below the name. A long app name wraps, and the More button stays at the top right. On the app page, the badge and the More button go below the name, the facts column goes below the connector box, and each label of the details goes above its value. Each state fits at 320 px. The agent recorded only a wide window, so the phone width is drawn.
- Long list: not seen. The list scrolls with the page. The search and the kind filter above the list make a long list short.
- Slow network: the source shows grey blocks while a page loads, as Transitions says.

## Notes

- The 3 facts that the reader needs before a disconnect are the access, the connect date and the last use. The source shows the access only on the page of an app. The sketch puts a short line of what the app can do on each row, so that a reader can decide from the list.
- Keep these parts when the look changes: the bar above the list, the heading Active, the More button at the end of each row with Disconnect, the maker line with the verified mark, a confirmation that names the app, and a page of each app with its access facts.
- Left out as not essential: the catalog sections above and below the reader's apps, the items of the Add menu (upload, custom connector, create, marketplace), the items of the filter menu (verified, community), the related apps on the app page, the share button, the category, the listed date and the developer links. The Add and filter buttons stay, and each one shows a toast.
- The sketch keeps no brand, no colour and no picture of the source. All words are sample content.
- The pictures of the source are not committed.
