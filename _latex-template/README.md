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
  right-aligned page numbers). `\printindex` itself is rendered by the
  [`manual-index.md`](../manual-index.md) chapter.
- Snap! brand colors (`snapblue`, `snaporange`) are defined for use in custom
  LaTeX content.

## Files

- `template.tex` &mdash; the jtex template. Special markers `[- IMPORTS -]`
  and `[- CONTENT -]` are filled in by MyST.
- `template.yml` &mdash; jtex template metadata (declared packages, doc
  fields, files to bundle).
- `index-style.ist` &mdash; `makeindex` style file applied by `latexmk`
  (see `latexmkrc`).
- `latexmkrc` &mdash; configures `latexmk`'s `$makeindex` so the style file
  above is actually used.

## Updating from upstream

The upstream template is small. To pick up upstream changes, diff against:

```
https://github.com/myst-templates/plain_latex_book
```

and re-apply the Snap!-specific adaptations listed above.

[upstream]: https://github.com/myst-templates/plain_latex_book
