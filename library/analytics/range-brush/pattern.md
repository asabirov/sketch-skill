# Range brush under a chart

Captured: 2026-11-25, recorded by an agent
Best for: any chart over time where a person sets the shown range by a drag, and needs to see where that range sits in the whole time.
Row opens: no rows.
Related: `analytics/filter-bar` holds the range button that names the same range. `analytics/cashflow-chart` is a chart that a brush can sit under.

## Scenarios

- See where the chosen range sits in the whole time, with a small copy of the data.
- See only the chosen months in the detail chart above.
- Make the range longer or shorter by a drag of one end.
- Move the whole range to earlier or later months by a drag of the frame.
- Move one end by one month with the keyboard.
- Check the dates of the range in the label, while the drag is still in progress.

## States

- `range`: a detail chart with a bar for each chosen month. Below it, the brush: a small bar for each of the 15 months and the month names, with a frame on the chosen range. A small filled label above the frame names its dates. Each end of the frame has a handle. The range button above names the same dates. Opens on: the address of the page.
- `end-moved`: one end is at a new month. The label and the range button give the new dates, and the detail chart shows the new months. Opens on: a drag of a handle, or an arrow key on a handle.
- `range-moved`: the whole frame is at earlier months, with the same length. The detail chart shows those months. Opens on: a drag of the frame.
- `handle-focus`: a handle has a focus ring. The Left and Right arrow keys move that end by one month. Opens on: the Tab key.
- `one-month`: the shortest range is one month. Near the right end, the label stands at the right of the frame. Opens on: a drag of a handle as far as the other handle.

## Transitions

- `range` to `end-moved`. Trigger: a drag of a handle. Moves: the frame follows the pointer with no motion of its own. When the pointer lets go, the frame snaps to the nearest whole month at once, and the detail chart changes at once. estimated, because the source did not take the drag of the agent.
- `range` to `range-moved`. Trigger: a drag of the frame. Moves: the same as a handle. estimated.
- `handle-focus` to `end-moved`. Trigger: an arrow key. Moves: nothing. The frame changes at once. The designer chose it. estimated.

## Hard cases

- One month: a handle cannot pass the other handle, so the range is at least one month.
- The ends of the time: the frame stops at the first and the last month.
- Today in the last month: the label says "today" in place of the last date.
- Narrow screen: at 390 px the source hides the bar and keeps only the range button. The sketch keeps the brush. Below 768 px it shows every third month name, and it hides the names beside each edge of the frame, so a handle never crosses a name, and the frame label names the range. With more than 6 months, the detail chart names every second month.
- Same scale: the detail chart and the brush use one scale, so a bar keeps its size when the range moves.
- Touch screen: each handle has a target of 44 px. The page does not scroll sideways during a drag.
- Keyboard: each handle is a slider with its value in words.

## Notes

- The brush answers "where is this range in time". The detail chart answers "what happened in it". The range button and its popover answer "which dates exactly". Keep both, and keep them in step.
- The label moves with the frame during the drag, so a person sees the dates before letting go.
- The snap to whole months keeps the data of the page at clean month ends.
- Left out, because only the source has them: the year marks above the months and the colour of the frame.
- The detail chart and the small copy of the data are not in the source. They make the bar a general brush that can sit under any chart over time.
