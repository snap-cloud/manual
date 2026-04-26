![Snap! Logo](./images/snap-logo.png)

# The Snap<em>!</em> Reference Manual
## [Read at docs.snap.berkeley.edu][website] ([Original PDF][original_pdf])

[![GitHub Pages](https://img.shields.io/badge/website-GitHub%20Pages-blue.svg)](https://docs.snap.berkeley.edu/)

[website]: https://docs.snap.berkeley.edu
[pdf]: https://docs.snap.berkeley.edu/snap-manual.pdf
[original_pdf]: ./SnapManual.pdf

The reference manual for the [Snap<em>!</em> programming language][snap]. ([GitHub][snap_gh])

[snap]: https://snap.berkeley.edu
[snap_gh]: https://github.com/jmoenig/snap/

> [!NOTE]
> The web manual is a "translation" of the original PDF, which was last largely updated for
> Snap<em>!</em> 8. We're first working on the making the web version readable, then we'll
> update the content to match recent Snap<em>!</em> releases.

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

**To build a PDF (requires LaTeX):**

```shell
myst build --pdf
```

### Quarto (legacy)

The original Quarto build system is preserved on the `quarto` branch.
The `quarto.yml` GitHub Actions workflow still targets that branch.

[quarto]: https://quarto.org/docs/

## Writing Style

Please read [`STYLEGUIDE.md`](./STYLEGUIDE.md)

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

The website is hosted on GitHub Pages, compiled by the `myst.yml` workflow and deployed to the `gh-pages` branch.

## License

AGPL, CC-BY-NC-SA
