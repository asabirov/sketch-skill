# Sketch prototypes

Use these rules for disposable layout and interaction reviews. Keep the hierarchy and the meaningful content of the supplied screen. Simplify the details that are not decided yet.

A sketch is drawn with one marker. It has one ink and the bare page, and nothing else. It has no palette and no fill behind a drawn border, so the border sits on the page and not around a card. In the dark theme, the marker is the light stroke, and the page is the part that went dark. The purpose is that a sketch cannot be mistaken for the built thing. Also, every line on the sketch is a decision about layout, not about colour.

## One marker

Set up the sketch in this sequence from the project folder:

1. Copy `"<skill-folder>/templates/<category>/<name>.html"` to `page.html`.
2. Edit `page.html`. Do not edit the installed skill.
3. Run `python3 "<skill-folder>/assets/sketch_inline.py" page.html > sketch.html`.
4. Open `sketch.html`. It holds the CSS and JS from the skill.

After you add frames or icons by script, call `initSketch()`. Run step 3 again after each edit and after you copy an earlier sketch, so that the page holds the current kit.

`assets/sketch-gallery.html` shows components below in use. Copy markup from it. Do not draw your own version of a component that the library has.

Use these names:

- Layout: `sketch-stack` puts children in a column, `sketch-row` puts them in a wrapping row, and `sketch-spacer` pushes the rest of a row to the end. `sketch-muted` is secondary text.
- Region: `sketch-panel sketch-frame` draws an outline around a selected region.
- Actions: `sketch-button`, with `secondary` for an outlined button. `sketch-icon-button` with an `aria-label` is a 44px button that holds only an icon.
- Icons: `<i data-icon="name"></i>` becomes a line icon. The names are close, plus, minus, check, chevron-down, chevron-up, chevron-left, chevron-right, arrow-left, arrow-right, search, menu, more, edit, trash, sliders, settings, comment, user, home, bell, calendar, copy, link, upload, download, eye, filter, external, info, warning, image, send, smile and box. Use `smile` for a reaction and `box` for an order or a parcel.
- Fields: `<label class="sketch-field">Name <input class="sketch-input"></label>`. The same class goes on a `select` and a `textarea`. For a choice from a list, use `<select class="sketch-input">` and do not draw your own dropdown. Its open list is drawn as a `sketch-menu`. Where the browser supports `appearance: base-select`, `sketch.css` draws the list. In every other browser, `sketch.js` opens a `sketch-menu` listbox of the options. For an error, add `aria-invalid="true"` to the input and a `sketch-error` text that starts with "Error:".
- Choices: `sketch-choice` for a checkbox or a radio, `sketch-switch` for a checkbox with `role="switch"`, `sketch-segmented` for a radio group, and `sketch-chip` for a button with `aria-pressed`.
- Status: `sketch-badge` is an outlined word, and `sketch-badge strong` is a filled word.
- Tabs: `sketch-tabs` holds buttons with `role="tab"` and `aria-controls`. The script shows the selected panel and moves with the arrow keys.
- Table: `<div class="sketch-table-box"><table class="sketch-table">`. The box scrolls the table sideways on a narrow screen.
- Facts: `<dl class="sketch-facts">` holds `dt` and `dd` pairs, such as "Total" and "$48.00". The `dt` is muted.
- Thread: `sketch-thread` holds the messages as `p` elements. Add `own` to a message of the person who uses the screen.
- Avatar: `<span class="sketch-avatar" aria-hidden="true">TP</span>` shows initials in a circle for a person. Add `square` for a group. It can stand next to a message in an open conversation.
- Inbox row: `<li class="sketch-conversation">` in a `sketch-list`. Put its three children in this order: the avatar `span`, a `div` with the name link and a `p` with the last message, then a `div` with a `span` for the time and the unread count. The rules for the avatar and the time column need this order. The avatar `span` needs no `sketch-avatar` class. The message shows on one or two lines. The name and the names of a group wrap. For a subject or an order number, put a `span` between the link and the message, such as `<span><span class="sketch-muted">#1042</span> Wrong size</span>`. It shows on one line. Add `square` to the avatar for a group. The name link covers the row, and `aria-current` on it fills the row. For an unread row, put the count in a `sketch-badge strong` with `aria-hidden="true"`, and add the count to the link's `aria-label`, such as "Theo Park, 2 unread". The count makes the name bold. A read row has a regular name. The row has no chevron, because the whole row is its link.
- Inbox page: start from `templates/app-shell/sidebar.html`. It shows the app navigation as a tab bar on a phone and as a rail from 600 px. Replace its `<main class="sketch-main">` with `<main class="sketch-split panes" style="--split:min(380px,45%) minmax(0,1fr)">`. In it, put a section with the `sketch-list` of rows, then the open conversation in a section with `sketch-from-tablet`. So a phone shows the list first. End the conversation section with the reply `form`, and give the section `grid-template-rows` with a `1fr` row for the `sketch-thread`. With `panes`, the open column fills the screen at each width, so the reply form is at its foot. From 600 px, `panes` also scrolls each column on its own, and `--split` sets the columns. Add a second `data-state` for the open conversation on a phone. In it, put `sketch-from-tablet` on the list section, and put a `sketch-phone-only` Back link to the first state above the conversation. A link that is a direct child of a `sketch-split` column is a 44 px target, with its icon beside its words. `templates/conversation/channels.html` is for a team chat with channels, not for an Inbox.
- Picture: `sketch-placeholder` holds the name of a picture that is not decided.
- Theme: no class and no button. The library styles the dark theme from `html[data-theme="dark"]` (`assets/sketch.css`). When `<html>` has no `data-theme` at load, `assets/sketch.js` sets it from `?theme=light` or `?theme=dark` in the address. If the address has no such value, the script follows the system theme. The script never changes a value that the page or the address set.

Overlays fill their outline with the page, so the page under them does not show through:

- Popover: a `sketch-popover` with an `id`, and `data-sketch-popover="<id>"` on its trigger. It opens below the trigger and stays on the screen. If it is taller than the screen, it scrolls.
- Menu: a `sketch-menu` that holds `sketch-menu-item` buttons, opened the same way as a popover. The arrow keys move between the items.
- Dialog: a `<dialog class="sketch-dialog">` with an `id`, and `data-sketch-open="<id>"` on its trigger. Put `autofocus` on the safe action.
- Toast: `data-sketch-toast="<text>"` on a button, or `sketchToast(text)` in a script. Escape hides it.
- A popover, a menu and a dialog close on Escape and on a `data-sketch-close` button. A popover and a menu also close on a click outside them. Focus then goes back to the trigger.

A step of a flow is a `<section data-state="<id>">`. The address `#<id>` shows that section only. These ids name the states. In a state, add `data-open` to a popover, a menu or a dialog that must show open.

The stylesheet defines these variables:

- `--sketch-ink`
- `--sketch-page`
- `--sketch-muted`, which is the ink thinned
- `--sketch-wash`, which is the ink at a tenth, for a hover
- `--sketch-stroke`
- `--sketch-wobble`

Draw all of your own elements, such as charts, rules, markers and icons, with these variables and nothing else.

- Use crisp Geist or system typography. Use body text of 14–16px and compact headings. The one-marker rule is about the ink, not about the lettering. Do not use a handwriting font, a paper texture or scribbles.
- Use lightly irregular single SVG frames around useful regions. Do not use nested frames, decorative dividers or section numbering. Keep everything else quiet.
- Add no colour. Show the difference between states, series or warnings with words, with weight, with a filled shape against an outlined shape, or with texture. Never use a hue, because the sketch does not have one. Name every state explicitly in words. The human must not have to decode a mark.
- Leave surfaces unfilled. A card, a panel, a dialog or a chart is its drawn outline with the page showing through it. So no block of a second colour sits behind a border. A shape filled solid with the ink is the only emphasis available. Use it rarely.
- Make controls visibly clickable, with hover, pressed, disabled and keyboard-focus states. A hover rule outranks a state rule. So when you add a state that fills a control, also write the hover of that state, with its background and its text colour. Use real buttons and labelled inputs. Make each touch target at least 44px. A drawn checkbox or radio is an 18px mark. So wrap the mark and its words in a `sketch-choice` label, which is the 44px target.
- Explain the reason for a disabled control in text beside the control. A disabled button is dimmed together with the words in it. So a reason written in the button is the one line that the human cannot read.
- Follow `html[data-theme]`. A page sets it, and the library follows it. Do not add a theme button. Check both themes. The ink and the page swap, so read again anything that assumed a dark line on a light ground. Do not add a theme select menu.

## Page templates

Each `templates/<category>/<name>.html` file is one whole page. Its title is "[Screen]: [Variant]". The templates are in 22 categories:

- App shell, Home, Conversation and List hold the product structure.
- Catalog, Projects, Project, Search and Menu hold navigation screens.
- Settings, Landing, Notes, Detail, Form, Dashboard and Board hold common work screens.
- Checkout, Pricing, Sign in, Onboarding, Empty and Mobile hold focused flows.

Each file starts with a `<!-- Best for: ... -->` comment that says which product it fits.

The layout classes are at the end of `assets/sketch.css` (the block that starts with the `Page layouts` comment). They start at phone width and change at 600 px and at 1000 px. Set these variables in a `style` attribute:

- `sketch-grid`: `--phone`, `--tablet` and `--wide` are the number of columns at each width.
- `sketch-narrow`: `--width` is the largest width.
- `sketch-cols`: `--cols` is the columns from 1000 px. Add `flip` to put the first child last.
- `sketch-split`: `--split` is the columns from 1000 px. From 600 px to 999 px, the first column is 260 px. With `panes`, `--split` is the columns from 600 px, so give the first column a percentage limit, such as `min(380px,45%)`.

`sketch-from-tablet` and `sketch-from-desktop` hide a region below 600 px and below 1000 px. `sketch-until-desktop` hides a region from 1000 px. Below 1000 px, a `sketch-menu-button` opens and closes the `sketch-collapse` right after it. A `sketch-meter` holds one `<i>` with a `width` in percent, and draws a usage bar.

To start a sketch, choose a category and copy one template to the project. Then change the words and the rows. Run the inlining command before you open the sketch.

## Start from a template

A sketch that starts from an empty page becomes a stack of text. The human cannot approve the layout of a stack of text. So do these steps before you draw:

1. Write the product kind and the device in one line. Example: "A phone app. A kid sees a balance and a history. A parent adds money and sets a rate."
2. Choose the template whose "Best for" line fits each kind of screen.
3. For an app with more than one main screen, choose one template for the shell and one for each kind of screen. Example: the family money app above takes `templates/mobile/tab-bar.html` for the shell, `templates/dashboard/metrics.html` for the balance, `templates/list/table.html` for the history and `templates/form/single-column.html` for a money entry.
4. Copy the templates. Then change the words and the rows. Keep their layout classes.
5. If no template fits a screen, name the closest template and the reason in the review.

## Draw the product, not the task

- Use the real content of the product: names, amounts, dates and statuses. A heading names the thing on the screen, such as "Alex". It does not name the task, such as "See your money".
- Give each screen one main thing, and draw it largest. Put the other items in rows, a `sketch-table` or badges. Align numbers on the right, and give each amount its sign.
- Show how the person moves between screens: the shell, the tabs and the back links. Draw each row that opens something as a control, with a chevron. An Inbox row is the exception: the whole row is its link.
- When two roles see different screens, draw each role's own view. Show what differs between the views.
- If half of a phone screen is empty, check that the screen shows all that the person needs there.

## Keep the review tools out of the screen

Each state shows only what the person sees in the product.

- Do not draw a state switcher, a sample-data notice or a test control in a state. Send a `#state` link for each state.
- Draw an error as its own state. Do not add a button such as "Fail" to make the error.

`assets/sketch-pages.html` shows every template by category at 390, 820 and 1280 px, with the "Best for" line under each name. The gallery has no theme button. It follows `html[data-theme]` and opens each template again with `?theme=light` or `?theme=dark` when the theme changes.

## Interaction

Implement only the decision-critical paths. Include empty states, error states and a way back. Do not include inert controls that imply working behaviour. A dialog must support Escape and must return focus. Identify a simulated action in the toast that it shows, such as "Saved (sample)". Never connect a sketch action to a production write.

Use plain HTML, CSS and JavaScript. Do not use a framework, a drawing library or a font download. If the artifact is a single file, inline the copied CSS and JS, so relative asset links cannot break. Keep the decision context and the prior choices in the surrounding review, not in prototype labels.

Name each function, variable and constant that a page script defines in `snake_case`. Keep browser names and the kit names that `assets/sketch.js` defines, such as `sketchToast`, in their own form.

Send the single file with a `#state` link for each state that the human must see. Otherwise send an image or a video. Before you send the sketch, open it at iPad width and at 390 px in both themes. Then confirm the overflow, search and choice behaviour. Also confirm that a dialog returns focus.

Then inspect each state as the human sees it, and answer these questions:

1. Does the state use the layout classes of a template?
2. Is the main thing of the screen drawn largest?
3. Is each word the real content of the product?
4. Can the person see how to get to the next screen and back?
5. Is the frame free of review tools?
6. Can the human approve the layout, and not only the words?

If an answer is no, draw the state again before you send it.

## Where the colour comes back

A browser paints its own colours into a native control, and `color` does not reach most native controls. The stylesheet draws the button, the input, the checkbox and the radio. It also takes back a link and an autofilled field. It sets `accent-color`, which a range and a progress bar follow.

The rest is your task. A `meter` paints its value on its own vendor pseudo-element. So the `background` and the border that you set on the element do not reach the value. A native `dialog` arrives with a filled surface and a dark backdrop. `sketch-dialog` fills it with the page and makes the backdrop a wash of the page.

Build a bar from ordinary elements and the variables, and do not fight the control. Never put a `background` or a `box-shadow` on an outlined overlay. The outline is drawn inside the box, so a fill or a shadow shows past its corners. A control that nobody thought about is where the colour comes back. So, before you show the sketch, look at it in a browser.
