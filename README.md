# The Snap_!_ Reference Manual
> by Brian Harvey, Jens Mönig

![Snap! Logo](./images/snap-logo.png)

## [Read the Manual][webiste] ([PDF - coming soon][pdf])

[webiste]: https://snap-cloud.github.io/snap-manual/
[pdf]: https://snap-cloud.github.io/snap-manual/snap-manual.pdf

The reference manual for the [Snap<em>!</em> programming language][sbe]. ([GitHub][snap_gh])

[sbe]: https://snap.berkeley.edu
[snap_gh]: https://github.com/jmoenig/snap/

## Authors
Brian Harvey & Jens Mönig

## Quarto

This version of the Snap! manual is built using [Quarto][quarto].

[quarto]: https://quarto.org/docs/

### Brief installation guide

You need:
* Quarto
* LaTeX

macOS:
```shell
brew install quarto
brew install mactex-no-gui
```

It is also recommended to install the [Quarto VSCode extension][quarto_vscode].
[quarto_vscode]: https://marketplace.visualstudio.com/items?itemName=quarto.quarto

### Building the book

**While writing content:**

```shell
quarto preview
```

This will automatically build the web version and display it in the browser.
Your webpage will automatically refresh as you save changes to files.

**To compile the PDF and final version:**

```shell
quarto render
```

### Hosting the book

The website is hosted on GitHub pages, compiled by the `quarto.yml` workflow.
The PDF is... TBD.

## Credits

## License
