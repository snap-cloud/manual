![Snap! Logo](./images/snap-logo.png)

# The Snap<em>!</em> Reference Manual
## [Read online at docs.snap.berkeley.edu][website] &middot; [Download the PDF][pdf]

[![GitHub Pages](https://img.shields.io/badge/website-GitHub%20Pages-blue.svg)](https://docs.snap.berkeley.edu/)

The latest production build of the manual is published from `main` to
GitHub Pages on every push:

| Format | URL |
| ------ | --- |
| HTML site | <https://docs.snap.berkeley.edu/> |
| PDF | <https://docs.snap.berkeley.edu/snap-manual.pdf> |
| Original Snap! 8 PDF (legacy reference) | <https://snap.berkeley.edu/snap/help/SnapManual.pdf> |

For PRs, an unmerged-but-built copy of the PDF is attached to each CI run as
a GitHub Actions artifact (kept for 10 days). See ["Previewing the PDF for a
PR"](#previewing-the-pdf-for-a-pr) below.

[website]: https://docs.snap.berkeley.edu
[pdf]: https://docs.snap.berkeley.edu/snap-manual.pdf
[legacy_pdf]: https://snap.berkeley.edu/snap/help/SnapManual.pdf

The reference manual for the [Snap<em>!</em> programming language][snap]. ([GitHub][snap_gh])

[snap]: https://snap.berkeley.edu
[snap_gh]: https://github.com/jmoenig/snap/

> [!NOTE]
> The web manual is a "translation" of the [original PDF][legacy_pdf], which
> was last largely updated for Snap<em>!</em> 8. We're first working on
> making the web version readable, then we'll update the content to match
> recent Snap<em>!</em> releases.

## Citing Snap! and the Snap! Manual

To cite the _manual_ specifically:

DOI: https://doi.org/10.5281/zenodo.16892852

```
Harvey, B., & Mönig, J. (2022). Snap! Reference Manual. Zenodo. https://doi.org/10.5281/zenodo.16892852
```

```bibtex
@book{harvey_2022_16892853,
  author       = {Harvey, Brian and
                  Mönig, Jens},
  title        = {Snap! Reference Manual},
  publisher    = {Zenodo},
  year         = 2022,
  month        = aug,
  doi          = {10.5281/zenodo.16892852},
  url          = {https://doi.org/10.5281/zenodo.16892852},
}
```
To cite Snap<em>!</em> in general, please use the following citation:

DOI: https://doi.org/10.5281/zenodo.15460068

```
Mönig, J., & Harvey, B. (2025). Snap! (latest). Zenodo. https://doi.org/10.5281/zenodo.15460068
```

```bibtex
@software{monig_2025_15460069,
  author       = {Mönig, Jens and
                  Harvey, Brian},
  title        = {Snap!},
  month        = may,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {latest},
  doi          = {10.5281/zenodo.15460068},
  url          = {https://doi.org/10.5281/zenodo.15460068},
}
```

These DOI's always point to the latest version of the manual and Snap! software, respectively. You can visit Zenodo to cite a specific version if you need to.

## Authors
Brian Harvey, Jens Mönig, Michael Ball, Jadge Hügle, Victoria Phelps, Mary Fries

## Jupyter Book 2 (MyST)

This version of the Snap! manual is built using [Jupyter Book 2][jb2] via [MyST Markdown][myst].

[jb2]: https://jupyterbook.org
[myst]: https://mystmd.org

### Installation

You need [Node.js][nodejs] (v18+) to install MyST:

```shell
npm install -g mystmd
```

[nodejs]: https://nodejs.org

macOS (via Homebrew):
```shell
brew install node
npm install -g mystmd
```

It is also recommended to install the [MyST VSCode extension][myst_vscode].

[myst_vscode]: https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight

### Building the book

**While writing content (live preview):**

```shell
myst start
```

This builds the web version and opens it in the browser.
The page reloads automatically as you save changes.

**To build the final HTML:**

```shell
myst build --html
```

Output is placed in `_build/html/`.

**To build a PDF (requires a TeX Live install):**

```shell
myst build --pdf
```

The PDF is written to `output/snap-manual.pdf`. See
[`docs/latex.md`](./docs/latex.md) for details on the PDF pipeline and the
local LaTeX template at [`_latex-template/`](./_latex-template/).

## Writing Style

Please read [`docs/STYLEGUIDE.md`](./docs/STYLEGUIDE.md). Other developer
docs live in [`docs/`](./docs/).

## VSCode and Editing

Install the [MyST VSCode extension][myst_vscode] for syntax highlighting and live preview.

## Document Conversion
If you are making large updates to the md structure, it may be worth working on the script to convert the Word document to markdown.
The script assumes you have `pandoc` installed and available in your path.

```
cd _support/conversion
ruby convert-word-doc.rb
```

## Published Book

The website is hosted on GitHub Pages at [docs.snap.berkeley.edu][website].
On every push to `main`, the [`myst.yml`](./.github/workflows/myst.yml)
workflow builds both the HTML site and the PDF (`snap-manual.pdf`), then
publishes them together to the `gh-pages` branch. The PDF is therefore
available at [`/snap-manual.pdf`][pdf] on the published site.

### Previewing the PDF for a PR

The same workflow also runs on pull requests. It does **not** publish to
`gh-pages`, but it does attach the freshly built `snap-manual.pdf` to the
workflow run as a GitHub Actions artifact named `snap-manual-pdf` with a
10-day retention.

To grab the PR's PDF:

1. Open the PR on GitHub and click **Checks** &rarr; **Deploy MyST /
   Jupyter Book to GitHub Pages**.
2. On the run page, scroll to the **Artifacts** section at the bottom.
3. Download `snap-manual-pdf` &mdash; it expands to `snap-manual.pdf`.

Or from the CLI:

```shell
gh run download --name snap-manual-pdf --repo snap-cloud/manual
```

## License

AGPL, CC-BY-NC-SA
