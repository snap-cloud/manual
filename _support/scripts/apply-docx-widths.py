#!/usr/bin/env python3
"""Backport docx-derived image widths into plain ``![](path)`` markdown images.

The original `convert-word-doc.rb` pipeline strips Pandoc's
``{width="Xin" height="Yin"}`` attributes from images during the
docx → markdown conversion (it moves them into non-functional HTML
comments or drops them entirely). As a result, plain block images in
the chapter `.md` files fall through to the latex-shims default of
30 % of \\linewidth — too small for editor screenshots that were
~5 in. wide in the docx, and too large for ~1 in. block icons.

This script harvests the original widths from the docx-as-markdown
export at ``_support/conversion/SnapManual.md`` and re-attaches them
to the chapter markdown by rewriting plain block images as the
project-local ``{img}`` role (see ``_support/plugins/img-role.mjs``).
The latex-shims plugin's ``normalizeWidth`` already converts ``Xin``
widths to a percentage of \\linewidth, so the role works through the
existing pipeline without further changes.

Usage::

    cd /path/to/manual
    python3 _support/scripts/apply-docx-widths.py

The script is idempotent: images that already use ``{img}``,
``{inline}``, or any other role are left alone.

Heuristics:
- Only touches block images whose entire line is ``![alt](url)``
  (with optional title and trailing HTML comment).
- Skips images whose URL doesn't look like a docx-extracted
  ``imageNN.png`` (no entry in the width map).
- For images reused at multiple sizes in the docx, picks the largest
  recorded width (smaller copies are usually inline thumbnails that
  belong on the inline-role path anyway).
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DOCX = REPO / "_support" / "conversion" / "SnapManual.docx"

DOCX_IMG = re.compile(
    r"!\[[^\]]*\]\([^)]*?(image\d+)\.png\)\{width=\"([\d.]+)in\""
)


def extract_docx_markdown() -> str:
    """Return the docx contents as Pandoc-flavoured markdown.

    Uses the same `pandoc --from docx --to markdown` conversion as
    ``convert-word-doc.rb`` so the resulting image attributes line up
    with what that script sees, but keeps everything in a temp dir to
    avoid leaving generated files in the tree.
    """
    if not DOCX.exists():
        sys.exit(f"Missing {DOCX} — nothing to harvest widths from.")
    if shutil.which("pandoc") is None:
        sys.exit(
            "pandoc not found on PATH. Install pandoc (the same tool the "
            "convert-word-doc.rb pipeline relies on) and re-run."
        )
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "SnapManual.md"
        subprocess.run(
            [
                "pandoc",
                "--from",
                "docx",
                str(DOCX),
                "--to",
                "markdown",
                "--wrap=none",
                "-o",
                str(out),
            ],
            check=True,
            cwd=tmp,
        )
        return out.read_text(encoding="utf-8")


def build_docx_width_map() -> dict[str, float]:
    text = extract_docx_markdown()
    widths: dict[str, float] = {}
    for m in DOCX_IMG.finditer(text):
        name, width = m.group(1), float(m.group(2))
        if name not in widths or width > widths[name]:
            widths[name] = width
    return widths


PLAIN_BLOCK_IMG = re.compile(
    r"^(?P<indent>[ \t]*)"
    r"!\[(?P<alt>[^\]]*)\]"
    r"\((?P<url>[^)\s]+)(?:\s+\"(?P<title>[^\"]*)\")?\)"
    r"(?P<trailing>[ \t]*(?:<!--[^>]*-->[ \t]*)?)$",
    re.MULTILINE,
)
URL_IMAGE_NN = re.compile(r"/(image\d+)\.(?:png|jpg|jpeg|gif)$", re.IGNORECASE)


def quote(value: str) -> str:
    return value.replace('"', '\\"')


def apply_widths(md_path: Path, widths: dict[str, float]) -> int:
    text = md_path.read_text(encoding="utf-8")
    changed = 0

    def repl(m: re.Match) -> str:
        nonlocal changed
        url = m.group("url")
        url_match = URL_IMAGE_NN.search(url)
        if not url_match:
            return m.group(0)
        image_name = url_match.group(1)
        width = widths.get(image_name)
        if width is None or width <= 0:
            return m.group(0)
        alt = m.group("alt") or image_name
        title = m.group("title")
        opts = [f'alt="{quote(alt)}"', f'width="{width:.2f}in"']
        if title:
            opts.append(f'title="{quote(title)}"')
        changed += 1
        return f'{m.group("indent")}{{img {" ".join(opts)}}}`{url}`'

    new_text = PLAIN_BLOCK_IMG.sub(repl, text)
    if changed:
        md_path.write_text(new_text, encoding="utf-8")
    return changed


def main() -> None:
    widths = build_docx_width_map()
    print(f"Loaded {len(widths)} docx image widths.", file=sys.stderr)
    targets = sorted(REPO.glob("[0-9][0-9]-*.md")) + sorted(
        REPO.glob("appendix/*.md")
    )
    total = 0
    for md in targets:
        n = apply_widths(md, widths)
        if n:
            print(f"  {md.relative_to(REPO)}: {n} image widths set")
        total += n
    print(f"Total updated: {total}", file=sys.stderr)


if __name__ == "__main__":
    main()
