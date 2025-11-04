---
toc: false
partial-data:
  block_description: |
    The `for` block lets you make a loop with a new variable (`i`) that starts a 1 and increments by 1 value, up to 10.
  label: "for _ = _ to _ _"
  block_spec: "for %upvar = %n to %n %cla"
  help_screen: "doFor.png"
  selector: "doFor"
  type: command
  category: control
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
  #   - image: examples/control/for-example.png
  #     description: Move forward by 10 steps
  #   - image: move_forward.png
  #     description: Move forward by 10 steps
---

# `for _ = to` {.unnumbered .unlisted .pdf-only-unlisted}

<!-- {{< partial blocks/_block.qmd >}} -->
```{python}
#| echo: false
#| output: asis
import sys; sys.path.append('_support')
from block_renderer import render_block
render_block()
```
