# Word Document Extraction

Most md files were created for doing:

```sh
pandoc --from docx SnapManual.docx --to [format] -o snap-manual-[format].md
```

Since there are a variety of formats, it's worth comparing them.

Things we can do:
* split by chapter / heading

TASKS:
* get image formatting better by default
* extract index info...

### Extracted docx:

```sh
unzip SnapManual.docx
xmllint --format word/document.xml > document_formatted.xml
```

### Word Doc Index info:
See this:

```sh
👉 grep 'w:instrText' document_formatted.xml
👉 grep 'w:instrText' document_formatted.xml | grep 'XE'
👉 grep 'w:instrText' word/document_formatted.xml | grep 'XE' | wc -l
    1161
```

Index entries are stored next to the place where the index should point to, with the format `XE "Index Entry text name"`.
Some entries seem to be spread across multiple XML entries...
