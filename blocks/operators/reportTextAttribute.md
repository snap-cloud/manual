---
toc: false
partial-data:
  block_description: Complete Me
  label: "_ of text _"
  block_spec: "%ta of text %s"
  # help_screen: "reportTextAttribute.png"
  # keep the next line here until we have a good image so it shows when searching for missing screens.
  # help_screen: BLANK.png
  help_screen: reportStringSize.png
  selector: "reportTextAttribute"
  type: reporter
  category: operators
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

# `Attribute of Text` {.unnumbered .unlisted .pdf-only-unlisted}

<!-- {{< partial blocks/_block.qmd >}} -->
```{python}
#| echo: false
#| output: asis
import sys; sys.path.append('_support')
from block_renderer import render_block
render_block()
```
