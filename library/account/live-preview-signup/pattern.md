# Sign-up and first-run onboarding

Captured: 2026-11-09, recorded by an agent
Best for: the sign-up of a team product, where each answer can show its result at once. Use it when a new team names its workspace, says what it uses the product for, and takes its first steps in the app.
Row opens: in place. A row of the plan offer opens its body under the row.
Related: `account/email-code-signup`, a sign-up with an emailed code and a paged onboarding.

## States

- `workspace-name`: step 1 of 3. One field for the workspace name, with a counter of the characters that remain (50 when empty). On the right, a live preview of the app shows the typed name, or "Your workspace" when the field is empty. Next stays disabled while the field is empty. Opens on: Create a workspace.
- `your-name`: step 2 of 3. One field for your name and an optional photo. The preview lights up your name in the direct messages list, with the tag "you". Opens on: Next.
- `invite`: step 3 of 3. One field for teammate emails. The preview lights up a "Your teammate" row and dims the other parts. A secondary button skips the step. Opens on: Next.
- `skip-confirm`: a small dialog "Skip without inviting?" with a skip button and a back button. Opens on: the skip button.
- `welcome-use`: a modal card over the app, with decorative corner shapes. It asks what the product is for, with three cards (work, education, other). The card needs Next. Opens on: the skip confirmation.
- `welcome-familiar`: the same card asks how well the user knows the product. A click on an answer goes on at once, with no Next. Opens on: Next in `welcome-use`.
- `welcome-goals`: the same card shows a checklist of goals and one "Get started" button. Opens on: an answer in `welcome-familiar`.
- `upsell`: a full-screen plan offer with an accordion of features. Each open row shows its own picture. Escape or Close goes on to the app. Opens on: Get started.
- `first-channel`: the app with a welcome header, three action cards (start from a template, connect your apps, invite teammates) and an empty message list. A checklist card at the bottom of the sidebar says "5 tasks remaining" and shows only the next task. Opens on: closing `upsell`.
- `welcome-email`: a general welcome email by the owner's choice. A narrow column holds a logo, a "Welcome to [Product], <name>" heading, the workspace name and its address, one "Open your workspace" button, a numbered list of three first steps, a help line and a footer. The source email had more parts: an avatar across a card edge, two invite rows with an invite link, a "Better together" box with three columns and a row of social icons. No transition measured. Opens on: "Check your email" in `first-channel`.
- `task-dialog`: a dialog that configures the channel, with the name, a counter, the topic and Confirm. Opens on: the task in the checklist card.
- `task-done`: the checklist card shows the done tick, the plant icon grows one stage, the count goes down by one, and the next task takes the place of the done one. Opens on: Confirm in `task-dialog`.

## Transitions

- `workspace-name` to `your-name`. Trigger: click Next. Moves: the filled progress pill colour. 300 ms, ease-in-out. measured.
- `your-name` to `invite`. Trigger: click Next. Moves: the preview section heading colour as the highlight moves. 100 ms, ease-out. measured.
- any field, focus. Trigger: focus. Moves: the field border colour and the focus ring shadow. 80 ms, ease-out. measured.
- any button, hover and press. Trigger: pointer. Moves: the background, border and text colour. 80 ms, cubic-bezier(0.36, 0.19, 0.29, 1). measured.
- `welcome-use` to `welcome-familiar` to `welcome-goals`. Trigger: Next, or a click on an answer. Moves: the new question content fades in after the old one leaves. Opacity 500 ms, 150 ms delay, linear. measured.
- `welcome-goals` to `upsell`. Trigger: click Get started. Moves: the plan page fades in (opacity 500 ms, linear). The header fades in with a spring curve (opacity 700 ms, a linear() spring that reaches 0.95 at about 50 %). The rows fade in one after the other (opacity 160 ms, ease-out, delays 0, 50 and 100 ms). measured.
- `upsell`, row open. Trigger: click a row. Moves: the row body grows from grid-template-rows 0fr to 1fr. 300 ms, linear. measured.
- `first-channel`, action card hover. Trigger: pointer. Moves: the card transform. 300 ms, ease. measured.
- `task-dialog` open and close. Trigger: click the task, or Cancel or Confirm. Moves: nothing. The dialog and the overlay show at once (0 ms). measured.
- `task-dialog` to `task-done`. Trigger: click Confirm. Moves: the checkbox fills (background and border colour 160 ms, cubic-bezier(0.36, 0.19, 0.29, 1)). The tick pops (opacity 0 to 1, scale 0.4 to 1.25 at 70 % to 1, 240 ms, linear). The old plant fades out (opacity 1 to 0, scale 1 to 0.8, 200 ms, linear). The new plant grows (opacity 0 to 1, scale 0.7 to 1.15 at 60 % to 1, 240 ms, 80 ms delay, linear). measured.
- cookie banner, close. Trigger: click Reject. Moves: opacity to 0 in 400 ms, linear, then visibility hidden after a 400 ms delay. measured. The sketch leaves the banner out by the owner's choice.

## Hard cases

- Empty field: Next stays disabled. The preview shows the placeholder name.
- Long text: the counter shows the characters that remain. The workspace name has a limit of 50 characters, and the channel name a limit of 80.
- Wrong channel name: the help text under the field says lower case, no spaces, no full stops, and at most 80 characters. The error state was not seen.
- Skip: each optional step has a skip action with a confirmation, so the user can always go on.
- Narrow screen and slow network: not seen.

## Notes

- Keep the live preview. Each answer changes the preview at once, and the preview lights up only the part that the current step changes.
- Keep one question on each screen, with a step count of three.
- An answer that is a single choice goes on at once. A checklist needs a button.
- Keep the first-run checklist small. It shows only the next task, and it says how many remain.
- Keep the reward small and fast: a tick pop and a growing plant, less than 350 ms in total.
- The style stays quiet. Field and button feedback is 80 ms. Only the reward and the plan page use a scale or a spring.
- Not seen: the email code step, the photo upload, and the invite with real emails. The test did not send invites.
