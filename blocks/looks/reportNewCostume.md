---
toc: false
partial-data:
  block_description: Complete Me
  label: "new costume _ width _ height _"
  block_spec: "new costume %l width %dim height %dim"
  # help_screen: "reportNewCostume.png"
  help_screen: BLANK.png
  selector: "reportNewCostume"
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

# `New Costume` {.unnumbered .unlisted .pdf-only-unlisted}

<!-- {{< partial blocks/_block.qmd >}} -->
```{python}
#| echo: false
#| output: asis
import sys; sys.path.append('_support')
from block_renderer import render_block
render_block()
```
