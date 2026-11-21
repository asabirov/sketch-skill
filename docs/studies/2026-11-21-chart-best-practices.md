# Chart best practices for sketch templates

Date: 21 November 2026. Question: which practices must a chart template of this kit follow? The question comes from [issue #8](https://github.com/asabirov/sketch-skill/issues/8). The owner rejected the Finance charts because of the bars and because of the scroll bar inside a chart.

The agent read each source on 21 November 2026. Each quote below is from that source.

## Practices with a source

| # | Practice | Source and quote |
| --- | --- | --- |
| 1 | Use bars to compare a total for each period. Use a line to follow a level over time. | NN/g, [Choosing chart types](https://www.nngroup.com/articles/choosing-chart-types/): "bar charts make it easy for people to quickly and accurately perceive the differences between values." Also: "If you want to show a data trend over time, a line chart will work better than a bar chart." |
| 2 | Put time on the horizontal axis, from left to right. | Zebra BI, [IBCS guide](https://zebrabi.com/ibcs/): "You should always put time series on the horizontal axis." |
| 3 | Show an actual value as a solid shape and a projected value as a hatched shape. | Zebra BI, [IBCS guide](https://zebrabi.com/ibcs/): "we use a solid fill with actual values, an outline with the plan and a hatched pattern for the forecast." |
| 4 | Start the value axis of a bar chart at zero. A line chart can use a range that does not start at zero, if the range has meaning. | Apple, [Human Interface Guidelines: Charts](https://developer.apple.com/design/human-interface-guidelines/charts): "bar charts can work well when you use zero for the lower bound of the Y axis, because doing so lets people visually compare the relative heights of individual bars". The same page gives a heart rate chart as the example where zero "could obscure important differences". |
| 5 | Use few grid lines. | Apple, [Human Interface Guidelines: Charts](https://developer.apple.com/design/human-interface-guidelines/charts): "Too many grid lines can be visually overwhelming, distracting people from the data; too few grid lines can make it difficult to estimate a mark's value." |
| 6 | Combine a bar and a line only when this makes the chart clearer. | Apple, [Human Interface Guidelines: Charts](https://developer.apple.com/design/human-interface-guidelines/charts): "Consider combining mark types when it adds clarity to your chart." |
| 7 | Do not give a chart a second value axis. Show the bar and the line in one unit. | Datawrapper, [Why not to use two axes](https://www.datawrapper.de/blog/dualaxis/): "A general audience is indeed likely to misread dual-axis charts". |
| 8 | Draw a sparkline at the size of a word, next to the numbers that it explains. | Edward Tufte, [Sparkline theory and practice](https://www.edwardtufte.com/notebook/sparkline-theory-and-practice-edward-tufte/): "A sparkline is a small intense, simple, word-sized graphic with typographic resolution." |
| 9 | Never show a difference with colour alone. Name each mark in words, in a key or in a label. | W3C, [Understanding WCAG 2.2: Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html): "Color is not used as the only visual means of conveying information". |
| 10 | Give each chart a short text summary and the data in text. | W3C, [Complex images tutorial](https://www.w3.org/WAI/tutorials/images/complex/): "The second part is the long description – a textual representation of the essential information conveyed by the image." |
| 11 | Do not scroll inside a chart. Fit the periods to the width. | The owner, in the result round of [apliteni/apliteni-ui#841](https://github.com/apliteni/apliteni-ui/issues/841), as quoted in issue #8: "scroll loooks ugly and should be avoided in charts". Datawrapper, [Chart types guide](https://www.datawrapper.de/blog/chart-types-guide), gives a related point: "A bar chart is often a safer pick for small screens than a column chart, since it grows vertically rather than horizontally." |

## Decisions in the templates without an outside source

The agent found no source for these points. They are decisions of this kit.

- A projected part of a line is dashed. A line cannot be hatched, so the dash is the line form of practice 3.
- The current period that is not complete shows its actual value to date as a solid part, and its projected rest as a hatched part on top. So the bar has the full projected height, and the solid part stays comparable with the earlier months.
- A change in the current period compares the value to date with the earlier period at the same day. A full earlier month against a part of this month always looks like a fall.
- To fit many periods, the bars get narrower. Below 600 px, only the first period and the current period keep a label, as status pages label only the ends of a long row of bars. Each other label has the class `minor`, and `assets/sketch.css:418` hides it below 600 px. See `templates/chart/monthly-bars.html:41`. The number of periods that fit is in the rule page of each template.

## What the agent could not check

- The IBCS standard itself (ISO 24896). Its pages on ibcs.com do not show the rule text without a sign-in or a download. Practices 2 and 3 cite Zebra BI, a vendor that explains the standard.
- A source that says to label lines directly in place of a legend. The templates use a key in words, which practice 9 requires.
