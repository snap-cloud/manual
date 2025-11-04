<!-- Dev Notes:
This partial is used to render all blocks.
We don't currently expost most of the 'metadata' about blocks, because not
a lot of it is written...

  block_description: Complete Me
  label: "create a clone of _"
  block_spec: "create a clone of %cln"
  help_screen: "createClone.png"
  selector: "createClone"
  type: command
  category: control
  arguments:
    - name: distance
      type: number
      default: 10
      description: The distance to move forward
  returns: None
-->

{{ block_description }}

![The "{{ label }}" block](/blocks/images/block_{{ selector }}.png)

![help screen for the block "{{ label }}"](../help/{{ help_screen }})

## Example Images

{{ #example_images }}
  ![{{ description }}]({{ image }})
{{ /example_images }}
{{ ^example_images }}
No examples yet.
{{ /example_images}}

## Example Projects

These example projects show the block in the context of a larger project. They will contain other blcoks, too.

{{ #example_projects }}
  * [{{ title }}]({{ url }})
{{ /example_projects }}
{{ ^example_projects }}
No examples yet.
{{ /example_projects}}

---

_Individual pages for each block are new. Most blocks don't yet additional links and images. If you have any questions, please post in the [Snap]{.snap} [forum](https://forum.snap.berkeley.edu/c/help/snap-help/49)._
