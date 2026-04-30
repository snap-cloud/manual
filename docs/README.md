# Snap! Manual &mdash; Developer Docs

This directory contains documentation for *contributing to* the Snap! manual.
For the manual itself, read it at <https://docs.snap.berkeley.edu/> or
download the [PDF](https://docs.snap.berkeley.edu/snap-manual.pdf).

## Contents

- **[STYLEGUIDE.md](./STYLEGUIDE.md)** &mdash; writing conventions, MyST/LaTeX
  syntax cheat sheet, indexing, cross-references, formatting rules.
- **[latex.md](./latex.md)** &mdash; how the PDF gets built (MyST &rarr;
  LaTeX &rarr; `latexmk`), the local LaTeX template at
  [`../_latex-template/`](../_latex-template/), and the GitHub Actions
  pipeline that publishes the PDF alongside the HTML site.

## See also

- [`../README.md`](../README.md) &mdash; project overview, install &
  build instructions, citation info.
- [`../_latex-template/README.md`](../_latex-template/README.md) &mdash;
  details of the vendored LaTeX template.
