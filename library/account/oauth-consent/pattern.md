# OAuth consent

Captured: 2026-11-16, from public pictures and a public video
Best for: a person lets an outside app act for their account, and later takes that right back in Settings.
Row opens: in place. The designer's choice: Disconnect in the row menu opens a confirmation over the list. The source shows no confirmation.
Related: `settings/settings-window`, the settings window that holds the list of connected clients.

## States

- `consent-request`: the product mark, the title "Connect with" the product, the app that asks, a workspace choice, the list of what the app can do, a full-width Continue, a full-width Cancel under it, and a trust note with the return address. Opens on: an app sends the person to the consent page. The source video shows this state at 00:46. The time limit and the line about Settings are drawn.
- `allowed`: a result that says the app is connected, with a way back to the app and a link to the connected clients. Opens on: Continue. The source shows a browser tab that loads and then returns to the app, with no page.
- `denied`: a result that says the app is not connected, with a way back to the app. Opens on: Cancel. The source shows no such state.
- `request-expired`: a message that the request has expired, with a way back to the app to start again. Opens on: a request that is opened after its time limit. The source shows no such state.
- `request-invalid`: a message that the request is not valid, with the reason, and no action that gives access. Opens on: a request that fails the check, such as a return address that does not match. The source shows no such state.
- `service-off`: a message that the product does not let apps connect now. Opens on: a request while connections are off. The source shows no such state.
- `app-return`: the app's own page, which shows the last result, a way to connect again and a way to open the product. The result is Connected, Not connected or The request expired. Opens on: Back to Notes Sync from `allowed`, `denied` or `request-expired`. The source video shows the app after the return at 00:56. Connect again opens a new `consent-request`.
- `product-home`: the product with its side menu, which holds Settings. Opens on: Open [Product] from `app-return`. The source pictures show no such page. It is drawn so that the person finds Settings later.
- `clients-list`: the settings window with Connected clients open. The window is a part of `settings/settings-window`, so the sketch draws it as a plain box with that name. A table lists each app with its maker, its access, when it was last used, and a menu button. Opens on: Settings, or Manage connected clients from `allowed`. The source shows My connected clients and Integrations in the Settings side menu, and a table with a menu on each row.
- `revoke-confirm`: a confirmation over the list that names the app and says what stops. Disconnect and Keep connected. Opens on: Disconnect in the row menu. The source menu has Disconnect and shows no confirmation.
- `client-revoked`: the list without the disconnected app, with a status line that names it. Opens on: Disconnect in the confirmation. The source shows no such state.
- `other-revoked`: the list without the other app, with a status line that names it. Opens on: Disconnect of Calendar Bridge while both apps are in the list. The source shows no such state.
- `clients-empty`: one sentence that says no client can use the account, and where a new client shows. Opens on: Disconnect of the last app. The source shows no empty list.

## Transitions

- `consent-request` to `allowed`. Trigger: click Continue. Moves: the request content. 180 ms, ease-out. estimated.
- `consent-request` to `denied`. Trigger: click Cancel. Moves: the request content. 180 ms, ease-out. estimated.
- Entry to `request-expired`. Trigger: open a request after its time ends. Moves: the request content. 180 ms, ease-out. estimated.
- Entry to `request-invalid`. Trigger: open a request that fails the check. Moves: the request content. 180 ms, ease-out. estimated.
- Entry to `service-off`. Trigger: open a request while connections are off. Moves: the request content. 180 ms, ease-out. estimated.
- `allowed`, `denied` or `request-expired` to `app-return`. Trigger: click Back to Notes Sync. Moves: the page content. 180 ms, ease-out. estimated.
- `app-return` to `product-home`. Trigger: click Open [Product]. Moves: the page content. 180 ms, ease-out. estimated.
- `product-home` or `allowed` to `clients-list`. Trigger: click Settings or Manage connected clients. Moves: the settings content. 180 ms, ease-out. estimated.
- `clients-list` to `revoke-confirm`. Trigger: click Disconnect in the row menu. Moves: the confirmation dialog. 160 ms, ease-out. estimated.
- `revoke-confirm` to `client-revoked`. Trigger: click Disconnect in the confirmation. Moves: the settings content. 180 ms, ease-out. estimated.
- `clients-list` to `other-revoked`. Trigger: click Disconnect in the confirmation of the other app. Moves: the settings content. 180 ms, ease-out. estimated.
- `client-revoked` or `other-revoked` to `clients-empty`. Trigger: disconnect the last app. Moves: the settings content. 180 ms, ease-out. estimated.

## Hard cases

- Cancel: not seen. Say that the app got no access, and send the person back to the app.
- Expired request: not seen. Say how long a request stays open, and send the person back to the app to start again. The app then opens a new request.
- Request that is not valid: not seen. Show the reason and no action that gives access.
- Connections that are off: not seen. Say that no access was given and when to try again.
- Empty list: not seen. Say in one sentence that no client can use the account.
- Many workspaces: the source puts the workspace in a choice above the list of access. The person must see which workspace the app gets before Continue.
- Long app name or long access list: not seen. Let the name wrap, and keep Continue and Cancel in view.
- 390 px screen: not seen. Keep one column. Each row of the table wraps. The settings window follows `settings/settings-window`.

## Notes

- Name the app, its maker, the account and the workspace before Continue. The person must see who gets access to what. Each result and Settings name the workspace that the person chose.
- Give Continue and Cancel the same width. Do not hide Cancel.
- Say in each result and each error whether access was given.
- Say on the consent page where the person can disconnect the app later.
- Put Settings in the side menu of the product, and Connected clients in the account group of Settings. The source names this item My connected apps. The sketch uses Connected clients, the name that the owner chose. A disconnected app stays out of the list until the person connects it again.
- Put Disconnect in a menu on each row, as the source does. Add a confirmation that names the app and says what stops. Keep connected is the safe action.
- The source menu also has Visit developer website and Contact support. The sketch leaves them out, because they leave the product.
