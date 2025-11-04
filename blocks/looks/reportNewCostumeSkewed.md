---
toc: false
partial-data:
  block_description: Complete Me
  label: "skew _ to _ degrees _ %"
  block_spec: "skew %cst to %dir degrees %n %"
  # help_screen: "reportNewCostumeSkewed.png"
  help_screen: BLANK.png
  selector: reportNewCostumeSkewed
  type: reporter
  category: looks
  arguments:
    - name: distance
      type: number
      default: 10
      description: The distance to move forward
  returns: None
  # example_projects:
  #   - title: Example Project 1
  #     url: https://example.com/project1
  #   - title: Example Project 1
  #     url: https://example.com/project1
  # example_images:
  #   - image: move_forward.png
  #     description: Move forward by 10 steps
  #   - image: move_forward.png
  #     description: Move forward by 10 steps
---

# `Skew Costume by Degrees` {.unnumbered .unlisted .pdf-only-unlisted}

<!-- {{< partial blocks/_block.qmd >}} -->
```{python}
#| echo: false
#| output: asis
import sys; sys.path.append('_support')
from block_renderer import render_block
render_block()
```
