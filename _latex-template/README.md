# Snap! Manual LaTeX Template

This directory is a locally vendored copy of MyST's [`plain_latex_book`][upstream]
template (the "common book" template), with adaptations for the Snap! Reference
Manual.

The template is referenced from the project's [`myst.yml`](../myst.yml) via the
`tex+pdf` export:

```yaml
exports:
  - format: tex+pdf
    template: ./_latex-template/
    output: output/snap-manual.pdf
```

The full PDF build process is documented in [`../docs/latex.md`](../docs/latex.md).

## Why a local copy?

Keeping a local copy lets us iterate on the LaTeX output (page geometry,
indexing, fonts, brand colors, etc.) without having to fork or pin a remote
template. It also means the `myst build --pdf` workflow runs from a known set
of files rather than fetching a template from `api.mystmd.org` at build time.

## Snap!-specific adaptations

The following changes have been made on top of the upstream `plain_latex_book`
template:

- KOMA-Script `scrbook` (instead of plain `book`) at 12pt, oneside.
- US Letter paper geometry with tighter Snap-style margins.
- `imakeidx` is loaded with `noautomatic`, which disables its shell-escape
  `makeindex` run and lets `latexmk` invoke `makeindex` instead. We pass
  `-s index-style.ist` via the bundled `latexmkrc`, so the rendered index
  uses our custom style (bold letter-group headings, small items,
  right-aligned page numbers). The index is also rendered in two columns
  via `imakeidx`'s `columns=2` option. `\printindex` itself is rendered
  by the [`manual-index.md`](../manual-index.md) chapter.
- Snap! brand colors (`snapblue`, `snaporange`) are defined for use in custom
  LaTeX content.
- A custom cover page (`\snapcoverpage`) replaces the default
  `\maketitle`: white left panel + blue right panel separated by a
  vertical dotted line, the Snap! logo + "Build Your Own Blocks"
  subtitle in the upper left, the version on the blue panel, an orange
  "Snap! Reference Manual" banner across the middle, the cover image of
  Snap! code below it, and the authors stacked in the lower right
  (sourced from `myst.yml`'s `authors:` list).
- Headings (`\chapter` ... `\subsection`) are restyled via `titlesec`:
  smaller fonts than the KOMA defaults and a thin horizontal rule
  beneath the heading text.
- `\includegraphics` is redefined to recognize the sentinel widths the
  [`latex-shims`](../_support/plugins/latex-shims.mjs) MyST plugin
  emits for inline images (`{inline ...}` role with `image-inline`,
  `image-inline-tall`, `image-1-5x`, `image-2x`, `image-3x`, or
  `image-4x` classes), and route them through `\snapinlineimgsize`,
  which renders them at a height proportional to the surrounding
  `\baselineskip` and raises them onto the text baseline. Plain
  `\includegraphics` calls (block images) fall through unchanged.
- `\kbd` macro renders a framed monospace key for `<kbd>` / `keyboard`
  nodes (also wired up by the latex-shims plugin).
- `snapgrid` environment + `\snapgriditem` macro render `:::{grid} N`
  directives as side-by-side minipages.

## Files

- `template.tex` &mdash; the jtex template. Special markers `[- IMPORTS -]`
  and `[- CONTENT -]` are filled in by MyST.
- `template.yml` &mdash; jtex template metadata (declared packages, doc
  fields, files to bundle).
- `index-style.ist` &mdash; `makeindex` style file applied by `latexmk`
  (see `latexmkrc`).
- `latexmkrc` &mdash; configures `latexmk`'s `$makeindex` so the style file
  above is actually used.
- `cover-image.png`, `snap-logo.png` &mdash; symlinks back to
  `../images/` so the cover-page `\includegraphics` calls resolve when
  `latexmk` runs from the temp build directory. The actual files live in
  `images/`; the symlinks here just make them visible to MyST's template
  bundler (see `template.yml`'s `files:` list).

## Updating from upstream

The upstream template is small. To pick up upstream changes, diff against:

```
https://github.com/myst-templates/plain_latex_book
```

and re-apply the Snap!-specific adaptations listed above.

[upstream]: https://github.com/myst-templates/plain_latex_book
