# Changelog

## Unreleased

### Added

- The pattern `analytics/account-list`: Account list card. A card on an overview page that compares the money in a few accounts, pots or wallets, and opens one of them.
- The pattern `analytics/action-row`: Action row with a More menu. The top of an overview page, where a person starts the most common jobs of the product without a menu.
- The pattern `analytics/balance-card`: Balance card. A person opens a money product to see how much money the business has now, and how the total moved over a period that they choose.
## 0.24.0 — 2026-11-24

### Added

- The pattern `chat/channel-thread-panel`. A message of a channel shows a card of its thread. The thread opens in a panel at the right of the channel, and the channel keeps its place. Below 1000 px the thread takes the place of the channel, and on a phone a drag from the left edge goes back.
- The kit part `sketch-split-handle`: a handle on the line between 2 columns of a `sketch-split`. A drag, the arrow keys, Home and End change the width of a column, and a double click gives the start width. Each column keeps its `--pane-min`, and the browser keeps the width for the next visit. `references/sketch-prototypes.md` shows an example.
- The kit part `sketch-slide-in`: a panel that slides in from the right edge in 300 ms each time it shows. With reduced motion, it shows at once.

### Changed

- The kit draws the `bell` icon with a body that gets wide at its foot and a round clapper under it. Before, the clapper was a flat line under a dome, and the icon did not look like a bell. The `bell-off` and `bell-ring` icons of 7 patterns use the same body.

## 0.23.0 — 2026-11-24

### Added

- The pattern `content/marketplace`. A start page with sections of add-ons in two columns, a search with a short list, a kind switch, a filter menu, a results page, a full list and the page of one item. A dialog for an item with settings.

## 0.22.0 — 2026-11-24

### Changed

- `account/connected-apps` and `account/oauth-consent`: each row shows Disconnect as a direct button. A row menu is used only when a row has more than one action. The `menu` state of `account/connected-apps` is gone.

## 0.21.0 — 2026-11-24

### Added

- The pattern `settings/settings`. The settings page fills the window in place of the work, with a column of sections at the left and one open section at the right, a search, and an account with sign out. The theme choice and the notification choices are dashed boxes that name the patterns that draw them.

### Removed

- The pattern `settings/phone-settings-page`. The owner did not like it (#30).
- The pattern `settings/settings-window`. `settings/settings-modal` covers the same part, and the patterns that named the settings window now name the settings modal.

### Changed

- The kit draws a `select` or a `button` with the class `sketch-input` at most 320px wide. Before, a dropdown filled the full line, such as the role dropdown of `settings/members-list`. A text field still fills the line.
- The kit puts an icon in a line of words on the middle of the words. Before, the icon sat too high, such as the check before "Included".

## 0.20.0 — 2026-11-23

### Added

- The pattern `settings/phone-settings-page`. A signed-in person opens Settings from their account on a phone and goes back with Back. Each row with a chevron opens its own section, each choice applies at once, and a sign-out asks once more. The sketch has an optional labelled form and a wide layout from 700 px.

### Fixed

- `README.md` and `docs/library.md` say 70 patterns. Pull requests #22 and #27 each raised the count from 68 to 69, so the count was one too low.

## 0.19.0 — 2026-11-23

### Added

- The pattern `content/document-match`. A person matches a bank transaction with an invoice, then checks each value that the product read from the invoice against the document. The document zooms to the value of each step and marks it. A value that differs from the document shows both values, with one button to use the document value. A summary and an edit screen come before the confirmation. On a phone, a bar at the foot opens the document in a drawer, and a down arrow closes it.

### Fixed

- `README.md` and `docs/library.md` say 69 patterns. Two pattern pull requests each raised the count from 67 to 68, so the count was one too low.

## 0.18.0 — 2026-11-22

### Added

- The pattern `settings/members-list`. A person who manages a shared account sees each member with a role and the last activity. The person invites a member by email or by link, decides on a request to join, edits a member, and signs a member out of one device or of all devices. Remove needs a check box. The sketch uses 3 general roles: Admin, Member and Viewer.
- 2 fills in the sketch kit. `.sketch-ground` sets one side of a split area apart. `.sketch-accent` makes the block that needs a decision stand out without a frame.
- `docs/library.md` lists each library pattern with its "Best for" line. A test fails when this list or the counts in `README.md` do not match `library/`.

## 0.17.0 — 2026-11-21

### Added

- The pattern `settings/theme-switch-preview-cards`. A reader chooses how the product looks on a page of its own, and sees a small picture of each choice first. The choice applies at once, with no Save button.
- The pattern `account/connected-apps`. A reader sees each outside app that uses their account, with its access, the connect date and the last use. The reader disconnects one app after a confirmation. The pattern fits a phone and a desktop.

## 0.16.0 — 2026-11-21

### Added

- A Chart category for report pages. Before, the kit had only the small bars and trends of the dashboard page, with no projection and no rule for when to use them. Now there are 5 chart templates: monthly bars, a line over time, bars against a plan, a trend in each table row, and key numbers with a small trend.
- Each chart shows the current month to date and the projected months. So a reader does not take an incomplete month for a fall.
- No chart scrolls inside itself, on a phone or on a desktop. A scroll bar inside a chart hides periods and is hard to use.
- Each chart has a rule page that says when to use it and when not to, so that a designer picks the right chart.
- The charts follow real product charts that the owner chose. A dated study gives a source for each chart practice.
- Each chart gives all its values to screen readers.

## 0.15.0 — 2026-11-21

### Added

- Added the reusable pattern library and its pull request gate. The gate fails on a Source note or a web address in a library file. A name check runs in a private flow before a pattern reaches this repository.

### Changed

- Each sketch loads the kit from `assets/sketch.css` and `assets/sketch.js` instead of an inline copy.
- The kit draws the extra pattern icons. A pattern sets `window.sketchGlyphs` with the paths instead of drawing them itself.

## 0.14.0 — 2026-11-20

### Changed

- Replaced the README example with four sketches at four widths, made by `docs/render.py`.
- Added `docs/templates.md` with a picture, name and "Best for" line for each of the 43 templates.

## 0.13.0 — 2026-11-18

### Added

- First public version: the sketch kit, the template gallery, the 43 page templates and the drawing rules.
