# Create a chat with an avatar

Captured: 2026-11-20, recorded by an agent
Best for: a phone app where a person makes a new chat and gives it an avatar that tells it apart from the other chats.
Row opens: no rows. Create opens the page of the new chat. The sketch shows the new chat above the list in place of the page.
Related: `chat/create-a-chat-initials` draws the avatar from the initials of the name. `chat/create-a-chat-picture` uses a picture as the avatar. `sheets/bottom-sheet` draws the sheet. `chat/chat-list` draws the list.

## States

- `closed`: the chat list with a New chat button at the top right. No sheet shows. A plain box stands for the list. Opens on: Cancel, Close, a press outside the sheet, Escape, or the release of a long drag.
- `empty`: a sheet with a large preview of the avatar, a Name field, a grid of 10 shapes, 8 colour swatches, and Cancel and Create. The first shape and the first colour are chosen. Create is quiet and not in use. Opens on: tap on the New chat button.
- `filled`: the field has a name, and the preview shows the chosen shape and colour. Create is in use. Opens on: the first character in the Name field.
- `name-taken`: a message below the field says that a chat has this name. The field has a thick line and the focus. Opens on: Create with a name that the list has. The source shows this message in the validation message of the browser.
- `created`: the sheet is closed. The new chat shows above the list, with its avatar. Opens on: Create with a new name. The source opens the page of the new chat and shows no such list.

## Transitions

- `closed` to `empty`. Trigger: tap on the New chat button. Moves: the sheet rises from below the screen, with the animation `directory-enter`. 520 ms, linear(0 0%, 0.009 1.05%, 0.035 2.1%, 0.141 4.4%, 0.281 6.7%, 0.723 12.9%, 0.938 16.7%, 1.017 18.6%, 1.077 20.5%, 1.121 22.4%, 1.149 24.3%, 1.159 25.7%, 1.163 27.1%, 1.161 28.5%, 1.154 29.9%, 1.129 32.8%, 1.051 39.6%, 1.017 43.1%, 0.991 47.05%, 0.977 51%, 0.974 53.8%, 0.975 57.1%, 0.997 69.8%, 1.003 76.9%, 1 100%). measured.
- `closed` to `empty`. Trigger: the same tap. Moves: the scrim shows, with the animation `scrim-enter`. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured.
- `empty` to `filled`. Trigger: the first character in the Name field. Moves: the `background-color` and the `color` of the Create button, from quiet to full. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured. The preview changes at once on each choice.
- `filled` to `name-taken`. Trigger: tap on Create. Moves: while the finger is down, the button shrinks to `scale(0.96)` and its `background-color` changes. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured. The message shows at once.
- `filled` to `created`. Trigger: tap on Create. Moves: the same press on the button. Then the sheet leaves at once, and the scrim fades out with the animation `scrim-exit`. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured.
- An open sheet to `closed`. Trigger: tap on Cancel or Close, a press outside the sheet, or Escape. Moves: the same `scrim-exit`. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured.

## Hard cases

- No name: Create is not in use until the field has a character that is not a space. The source sends "Enter a name." to the browser's validation message if the form is sent with no name.
- Name in use: the source sends "Use a different name." to the browser's validation message. The sketch shows a message below the field, which each browser draws the same.
- Long name: the field takes at most 80 characters.
- Cancel with a name in the field: the source closes the sheet and asks no question. The next sheet is empty.
- Tall content: the sheet stops 48 px below the top of the screen, and the choices scroll. The head and the two buttons do not move.
- Keyboard: the shapes are one group of choices, and the colours are a second group. The arrow keys move in a group.
- Wide screen: from 736 px, the source shows the sheet as a dialog in the centre, with no grab handle.
- Error and slow network: the source shows no such state. Create is immediate in the source.

## Notes

- The preview is large and at the top. Each choice changes it at once, so the person sees the result before Create.
- The avatar starts with a shape and a colour. Thus a name alone is sufficient, and the choices are an option.
- The sheet is that of `sheets/bottom-sheet`. Cancel is at the left of the bottom, and Create is at the right.
- The sketch has one ink. Each colour swatch of the source is drawn as a tint or a texture of that ink.
- The sketch leaves out the faces on the source shapes. Its shapes are plain: circle, square, diamond, hexagon, octagon, shield, cross, triangle, leaf and star.
- The source makes a new assistant and opens its chat after Create. The sketch makes a chat, and shows it above the list.
- The chat list is in `chat/chat-list`. The sketch draws it as a plain box.
