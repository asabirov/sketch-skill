# Flow chart

Captured: 2026-11-25, recorded by an agent
Best for: a report that shows where the money of a period came from and where it went, in one picture.
Row opens: no rows.
Related: `analytics/breakdown-table` lists the same sources and uses with their shares.

## Scenarios

- See the largest sources of the money in, and the largest uses, at one look.
- See how much of the money in the business kept.
- Check the amount and the share of one source or one use.
- Read a long list of sources without overlapping labels.

## States

- `flow`: the sources of the money in stand on the left, each with its name and amount. One bar for all the money in stands at the middle. The uses stand on the right, and the last one is the money that the business kept. A band joins each source and each use to the middle, and the width of a band is its amount. Opens on: the address of the page, or Flow in a chart switch.
- `band-picked`: one band is darker, the other bands fade, and a dark tooltip gives its name, its amount and its share of the money in. Opens on: the pointer or the keyboard focus on a band.
- `node-picked`: the same as `band-picked`, from the label of a source or a use. Opens on: the pointer on a label.
- `many-items`: the items too small for their own label go into one Other node on their side. Opens on: a range with many small sources or uses.
- `loading`: a pulsing block. Opens on: a new range or the first load.
- `empty`: one line of text and a way to the last 12 months, which shows `loading` and then the flow. The source shows no empty flow. Opens on: a range without money in or out.

## Transitions

- Any view to `flow`. Trigger: the chart shows. Moves: the chart fades in (opacity). 300 ms, ease-out. Measured for the change of view in the source. The source also fades in its labels and nodes in 180 ms, ease-out.
- `flow` to `band-picked`. Trigger: the pointer or the focus on a band. Moves: the other bands fade (opacity). 150 ms, ease-out. The source shows no hover on a band. estimated.
- `loading` to `flow`. Trigger: the data arrives. Moves: the block pulses (opacity) until then. 1000 ms, ease. measured.

## Hard cases

- Many small items: an item smaller than one line of label goes into Other. One small item alone stays itself.
- A use larger than all the money in, such as a loan payment from savings: the middle bar is the money in, so show the extra as its own source, such as "From savings".
- Negative kept amount: the business spent more than came in. The Kept node goes, and a "From savings" source takes its place on the left.
- Narrow screen: at 390 px each label takes 2 lines, the chart is taller, and the Other node takes the items that are smaller than 2 lines.
- Touch screen: a tap on a band or a label shows its tooltip. On a narrow screen, the tooltip shows below the chart, so it covers no label.
- Keyboard: each band takes the focus, and its label says its name, amount and share.

## Notes

- The middle bar makes the picture easy to read: everything on the left adds up to it, and everything on the right comes out of it.
- Keep the kept amount as the last use, so the picture also answers "how much did the business keep".
- The source groups the uses by recipient, with a second level for expenses and transfers. The sketch shows one level, because a sketch is about the layout.
- Left out, because only the source has them: the names of the source's customers and suppliers, and the colours of the bands.
