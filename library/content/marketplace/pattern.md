# Marketplace

Captured: 2026-11-24, recorded by an agent
Best for: a person looks for an add-on for a product, searches and filters a large catalog, reads about one item and adds it to their account.
Row opens: on the record's own page
Related: `account/connected-apps` shows the add-ons that a person already has and disconnects one. `content/catalog-tabs` shows the records of one workspace. A marketplace shows what a person can add.

## States

- `home`: the title, a bar and the sections. The bar has a search field that takes the free width, a switch for the kind with 3 choices, and a Filter button. The first section, "Your add-ons", has full-width rows with a more button. Each other section has rows in two columns. Each section has its name on the left and Show all on the right. A row has the picture, the name with a verified mark, one line of text, and a muted line with the kind and the maker. A thin line stands below each row of the two columns. Opens on: the address of the marketplace.
- `row-hover`: the row gets a ground, and its Add button shows at the right. Opens on: hover on a row.
- `add-hover`: a tooltip above the Add button gives the action and the name of the item. Opens on: hover on the Add button.
- `kind`: the sections show only the rows of the chosen kind. The switch fills the chosen part, and the address keeps the kind. Opens on: a click on a kind.
- `filter`: a menu below the Filter button with Verified and Community. Opens on: a click on the Filter button.
- `search`: a list below the search field with at most 5 items. Each item has its name, its kind and its maker. The last line is See all results. The page under the list does not change. Opens on: typed words.
- `no-results`: the same list with one line, "No results". Opens on: typed words that fit no item.
- `results`: the start page with the results only. "Your add-ons" comes first with a count, then "More you can add" in two columns. A row of an unverified maker has a Community badge. The search field keeps the words. Opens on: See all results.
- `all`: a back link, the title, the same bar and one list in two columns, the most popular item first. Opens on: Show all of a section.
- `loading`: the list of `all` is dimmed while the page loads the items. Opens on: Show all, before the items are there.
- `item`: the page of one item. A back link, then a head with the picture, the name, the maker, a share button and Add. Below a line, the text, two example pictures and what the item can do are on the left. The facts are in a column on the right: the developer, the access, the authorization, the categories and the date. Related items are at the end. Opens on: a click on a row.
- `connect`: a dialog over the list, for an item with settings. It has a title with the name of the item, a close button, one line of text, 2 choices with a line of text each, a note, a line, and Cancel and Connect at the right. The first choice is made. Seen in a picture only. Opens on: Add, on an item with settings.
- `added`: the head of the item page shows Added in the place of Add. The source shows no such state, because the agent did not press Add in the source. Opens on: Connect in the dialog.

## Transitions

- `home` to `row-hover`. Trigger: hover on a row. Moves: the Add button fades in. 60 ms, cubic-bezier(0.4, 0, 0.2, 1). measured.
- `row-hover` to `add-hover`. Trigger: hover on the Add button. Moves: the tooltip fades in and grows (opacity and scale). 120 ms, cubic-bezier(0.32, 0.72, 0, 1). Measured duration and easing. The start scale of 0.96 is estimated.
- `home` to `kind`. Trigger: a click on a kind. Moves: nothing. The rows change at once. measured.
- `home` to `filter`. Trigger: a click on the Filter button. Moves: nothing was recorded. The menu shows at once. measured.
- `filter` to `home`. Trigger: Escape. Moves: the ring of the Filter button (box-shadow). 60 ms, cubic-bezier(0.165, 0.84, 0.44, 1). measured.
- `home` to `search`. Trigger: a click in the search field, then typed words. Moves: the ground and the ring of the field (background-color and box-shadow), 60 ms, cubic-bezier(0.4, 0, 0.2, 1). A spinner turns while the items load, 1000 ms for a turn, linear. measured.
- `search` to `results`. Trigger: a click on See all results. Moves: the sections appear with one animation. 120 ms, cubic-bezier(0.165, 0.84, 0.44, 1). Measured duration and easing. The fade from 0 is estimated.
- `home` to `all`, and back to `home`. Trigger: Show all, and the back link. Moves: the page appears with the same animation. 120 ms, cubic-bezier(0.165, 0.84, 0.44, 1). Measured duration and easing. The fade from 0 is estimated.
- `home` to `item`. Trigger: a click on a row. Moves: the pictures fade in. 500 ms, cubic-bezier(0.4, 0, 0.2, 1). The rest of the page shows at once. measured.
- `home` or `item` to `connect`. Trigger: Add, on an item with settings. Moves: nothing. A picture shows this state, so its motion is not known. The designer chose it. estimated.
- `connect` to `added`. Trigger: Connect. Moves: nothing. The designer chose it. estimated.

## Hard cases

- Empty: not seen. Each section without a row is hidden in the sketch.
- No match: the `no-results` state.
- Long text: the text of a row stays on one line and ends with an ellipsis.
- Slow network: a spinner turns in the search field. The old items of the search list fade after 500 ms (opacity 60 ms), and the sketch does not draw this. The list of `all` is dimmed, as in `loading`.
- Narrow screen: not captured. The sketch draws one column below 720 px, and the facts of the item go below its text. The designer chose it.
- Touch screen: not captured. The sketch always shows the Add button where no pointer can hover. The designer chose it.
- Failed load: not seen.

## Notes

- A row has one job, to open the page of the item. Add is a second, small control that shows on hover and on focus, so a long list stays quiet.
- The search shows a short list first and does not change the page. A person leaves the start page only with See all results.
- "Your add-ons" comes before the catalog, also in the results. So a person sees what they already have.
- Keep the maker and the verified mark on each row. They carry the trust of the marketplace.
- A choice in the Filter menu was not pressed in the source. The sketch hides the other rows, and a second click shows them again. The designer chose it.
- Left out, because only the source has them: the menu for more page actions, the menu that adds an item of the person's own, the section of workflows, the connection box of an item with its technical address, the arrows of the example pictures and the links of the maker.
- Some items have settings, such as the account to connect. Add opens the dialog for these items only. The other items are added at once.
- In the sketch, Add on an item without settings shows a short message. The source shows no such message, because the agent did not press Add.
- The frame of the product is left out. The product puts the page in its own frame.
