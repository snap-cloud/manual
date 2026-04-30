# Block reference pages

> [!NOTE]
> _Individual pages for each block are new. Most blocks don't yet additional links and images. If you have any questions, please post in the Snap<em>!</em> [forum](https://forum.snap.berkeley.edu/c/help/snap-help/49)._

Each Snap! block has a one-page entry under this directory. A page is two
files sharing a basename:

- `<selector>.md` — prose, examples, anything page-specific
- `<selector>.yml` — structured metadata consumed by the `{block-help}` directive

Pages are organized by category: `blocks/<category>/<selector>.{md,yml}`.

## Authoring a new block page

1. Create `blocks/<category>/<selector>.yml` with the fields below.
2. Create `blocks/<category>/<selector>.md` with frontmatter and the
   `{block-help}` directive:

````markdown
   ---
   title: "when ⚑ clicked"
   ---

```{block-help}
```
````

3. Add the page to the table of contents (`myst.yml` or your TOC file).
4. Drop the block screenshot at `blocks/images/block_<selector>.png` and the
   help-screen image under `help/<help_screen>`.

The `{block-help}` directive auto-locates the sidecar by replacing the page's
`.md` extension with `.yml`. No argument is required in the common case.

## Sidecar YAML schema

Required fields:

| Field | Type | Notes |
|---|---|---|
| `selector` | string | Snap! internal selector; should match the filename |
| `label` | string | Human-readable block label, e.g. `"when $greenflag clicked"` |
| `block_spec` | string | Snap! block spec syntax |
| `block_description` | string | One- or two-sentence description |
| `help_screen` | string | Filename of the help-screen image under `help/` |
| `type` | string | `command`, `reporter`, `predicate`, `hat`, etc. |
| `category` | string | Should match the parent directory |

Optional fields:

| Field | Type | Notes |
|---|---|---|
| `arguments` | list | Each item: `name`, `type`, `default`, `description` |
| `returns` | string | Return type (`None` for command/hat blocks) |
| `example_images` | list | Each item: `image`, `description` |
| `example_projects` | list | Each item: `title`, `url` |

Example: see [`blocks/control/receiveGo.yml`](control/receiveGo.yml).

## What `{block-help}` renders

The directive reads the sidecar and emits, in order:

1. The block description as a paragraph.
2. The block screenshot (`/blocks/images/block_<selector>.png`).
3. The help-screen image (`../help/<help_screen>`).
4. An "Example Images" section (or "No examples yet.").
5. An "Example Projects" section (or "No examples yet.").

Output is renderer-agnostic MyST AST, so the same source produces both the
website and the LaTeX/PDF export.

## Common issues

- **Image path shows `block_unknown.png` in the build.** The plugin couldn't
  read the sidecar — check that `<selector>.yml` exists next to the `.md` and
  that `selector:` inside it is set.
- **"Cannot load sidecar" warning in build logs.** mystmd ran the plugin
  without a resolvable file path. Pass the selector explicitly as an argument:
  `` ```{block-help} <selector> ``. If this happens consistently, the
  `vfile.path` API has changed — see the maintenance notes below.
- **YAML parse errors.** Validate a single file with:

````bash
  python -c "import yaml; yaml.safe_load(open('blocks/control/receiveGo.yml'))"
````

## For maintainers

### Plugin

Implementation: [`plugins/block-help.mjs`](../plugins/block-help.mjs).
Registered in [`myst.yml`](../myst.yml) under `project.plugins`. Depends on
`js-yaml` (declared in the repo's `package.json`).

The plugin:

1. Locates the sidecar by taking `vfile.path` and replacing `.md` → `.yml`.
   If `vfile.path` is unavailable, it falls back to the directive's positional
   argument as a relative selector path.
2. Loads and parses the sidecar with `js-yaml`.
3. Returns a list of MyST AST nodes — paragraph, image, image, heading, list,
   heading, list — which mystmd routes to whichever renderer is active (HTML,
   LaTeX, Typst, DOCX). No format-specific branching in the plugin.

To add a new field to the rendered output: extend the destructuring block in
`run()`, then append the corresponding AST node(s) to the returned array. See
the [MyST AST spec](https://spec.myst.tools/spec/overview) for node shapes,
or the [JS plugin guide](https://mystmd.org/guide/javascript-plugins) for
context API.

### Migration

Sidecar files were extracted from inline `partial-data` frontmatter using
[`scripts/migrate_blocks.py`](../scripts/migrate_blocks.py). The script is
idempotent (skips files that no longer have `partial-data`) and should not
need to run again. Keep it in the repo as documentation of the original
layout and as a template if a similar refactor is needed for another field.

### Adding new categories

Categories are just directories under `blocks/`. The plugin doesn't enumerate
them — it only resolves a sidecar relative to the page being rendered — so a
new category needs no plugin change. Add the directory, add pages, and add
them to the TOC.



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

```
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
```
