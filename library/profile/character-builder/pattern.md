# Avatar builder

Captured: 2026-11-11, recorded by an agent from the public frames. Frame time 00:00.00 is 0:20 of the video.
Best for: a mobile character or avatar builder where the user picks parts and sees the result at once, then saves to a profile. Use it for a profile avatar maker or a game character maker.
Row opens: no rows.

## States

Each state shows the avatar as built up to that point in the video. The times are estimated from the frames.

- `picker`: the icon tabs and the live preview. The header holds an X on the left and Done on the right. The preview shows the cat standing on a grey band with no circle. The cat body reaches the band's bottom edge. Below the preview is a row of nine part-type icon tabs: Fur and body, Expression, Ears, Glasses, Face details, Earrings, Whiskers, Headwear and Background. The chosen tab is underlined and lightly filled. Below the tabs, the Fur and body tab shows two lists with small headings: Fur color (a row of square colour swatches) and Body shape (a grid of two columns of body thumbnails). Opens on: the Create Avatar screen, video 0:28 to 0:29 (frame 00-08.50).
- `skin-tone`: the fur colour is black, the darkest swatch. The head and the body fill solid. The black swatch has a bold outline and a light fill. The source opens with this swatch already chosen; the frames show no colour pick. Opens on: the Create Avatar screen, video 0:28.5 (frame 00-08.50).
- `body`: the body shape changed to a large one. The preview shows a wider body. The large thumbnail is chosen. Opens on: pick a large body, video 0:38 to 0:39.
- `expression`: the expression changed to laughing. The preview shows a different mouth and eyes. Opens on: pick an expression, video 0:47 to 0:48.
- `hairstyle`: the ears changed to long ears. The preview shows tall ears. Opens on: pick long ears, video 0:50 to 0:51.
- `glasses-none`: the glasses set to none. The preview shows no glasses. The none choice is the first thumbnail, a crossed-out head. Opens on: pick none in Glasses, video 1:10.
- `face-details`: freckles added. The preview shows marks on the face. Opens on: pick a face detail, video 1:11 to 1:12.
- `earrings`: hoop earrings added. The preview shows the earrings. Opens on: pick earrings, video 1:13 to 1:14.
- `glasses`: round glasses with a glasses colour. The Glasses tab shows two lists with small headings: Glasses color (a row of square swatches) and Glasses (a grid of two columns of thumbnails). The round thumbnail and one colour swatch are chosen. Opens on: pick glasses and a glasses colour, video 1:21 to 1:22.
- `facial-hair`: whiskers added. The preview shows the whiskers. The Whiskers tab shows two lists: Whisker color and Whiskers. Opens on: pick whiskers, video 1:25 to 1:26.
- `headwear`: a beanie added with a headwear colour. The Headwear tab shows two lists: Headwear color and Headwear. The beanie thumbnail and one colour swatch are chosen. Opens on: pick headwear and its colour, video 1:44 to 1:45.
- `background`: the background colour fills the grey preview band. The dark swatch is chosen. Opens on: pick a background colour, video 2:04 to 2:05.
- `save`: the profile with the new avatar, after the loading screen. It shows a wide grey banner with the large avatar and a gear icon at the top right. Below the banner are the name with a flag, a handle line, a Joined line, Following and Followers links, an Add friends button with a share button, a Statistics heading with 2 by 2 tiles, and a bottom bar with 5 icons. Opens on: tap Done, video 2:18.

## Transitions

- any part pick. Trigger: tap a thumbnail or a swatch. Moves: the preview re-renders at once, no motion (0 ms). estimated from the frames; the re-render is shown at the pick of each part: video 0:38, 0:47, 0:50, 1:10, 1:11, 1:13, 1:21, 1:25, 1:44 and 2:04.
- any tab tap. Trigger: tap a part-type icon. Moves: the tab underlines and the lists below it change at once. Not a fixed duration. estimated.
- `picker` to `save`. Trigger: tap Done. Moves: a loading screen shows for about 10300 ms, then the profile opens. estimated from the source video, 2:06.5 to 2:16.9. The navigation motion itself is not seen in the frames.

## Hard cases

- None: Glasses, Face details, Earrings, Whiskers and Headwear each have a none choice, a crossed-out thumbnail. The creator picks none in Glasses at video 1:10, and adds Face details at 1:11, Earrings at 1:13 and Whiskers at 1:25.
- Empty pick: every part starts with a default, so there is no empty state.
- Long text: the profile name is the only long text and it wraps.
- Narrow screen and slow network: not seen.

## Notes

- Keep the live preview above the tabs, and update it at once on each pick.
- Keep the cat standing on the grey preview band with no circle, its body reaching the band's bottom edge.
- Keep the icon tab row. The chosen tab is underlined and lightly filled; the chosen tab in the source is blue and underlined.
- A tab can hold two lists, each with a small heading: Fur color swatches and Body shape thumbnails, Glasses color and Glasses, and so on.
- The sketch draws a round cat, while the source app draws a person. The source part names map to the cat: skin tone to fur colour, body to body shape, hairstyle to ears, and facial hair to whiskers.
- Most choices are avatar thumbnails in a grid of two columns. Colours are a row of square swatches. The chosen item has a bold outline and a light fill; in the source it has a blue outline and a light blue fill.
- Keep the save as one Done button in the header. The result is the profile with the new avatar, after a loading screen of about 10 seconds.
- The swatches and the thumbnails carry no text in the source; the list headings and the part-type icons are the only text. The sketch captions name each change in plain words.
- Not seen: the navigation motion from the builder to the profile, the none choice of Ears, a wrong save, and the exact colour names of the colour sub-pickers (Glasses color, Whisker color and Headwear color).
