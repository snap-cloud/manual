#!/usr/bin/env python3
"""Regenerate the variant PDF exports inside `myst.yml` from `toc.yml`.

The Snap! manual ships three PDF variants:

* `snap-manual.pdf`              — full manual, built directly from `toc.yml`.
* `snap-manual-no-blocks-ref.pdf` — full manual minus the "Blocks" branch.
* `snap-blocks-ref.pdf`          — only the "Blocks" branch (plus the index).

The two filtered variants are configured via per-export `articles:` lists in
`myst.yml`. The lists are deterministic functions of `toc.yml`, so this
script regenerates them in place between two sentinel comments:

    # === BEGIN GENERATED PDF VARIANTS ===
    ...
    # === END GENERATED PDF VARIANTS ===

Run after any change to `toc.yml`:

    python3 _support/scripts/generate-pdf-exports.py
"""

from __future__ import annotations

import io
import sys
from pathlib import Path
from typing import Iterable

import yaml

ROOT = Path(__file__).resolve().parents[2]
TOC = ROOT / "toc.yml"
MYST_YML = ROOT / "myst.yml"

BLOCKS_TITLE = "Blocks"
INDEX_FILE = "manual-index.md"

BEGIN_MARK = "  # === BEGIN GENERATED PDF VARIANTS ==="
END_MARK = "  # === END GENERATED PDF VARIANTS ==="


def flatten(entries: Iterable[dict], level: int = 0) -> list[dict]:
    """Flatten a nested toc tree into a flat list with `level:` annotations."""
    out: list[dict] = []
    for entry in entries:
        title = entry.get("title")
        file = entry.get("file")
        children = entry.get("children")
        item: dict = {}
        if title is not None:
            item["title"] = title
        if file is not None:
            item["file"] = file
        if level > 0:
            item["level"] = level
        if item:
            out.append(item)
        if children:
            out.extend(flatten(children, level + 1))
    return out


def main() -> int:
    with TOC.open() as fh:
        toc = yaml.safe_load(fh)

    project_toc = toc["project"]["toc"]

    blocks_entry = None
    other_entries = []
    for entry in project_toc:
        if entry.get("title") == BLOCKS_TITLE:
            blocks_entry = entry
        elif entry.get("file") == INDEX_FILE:
            continue  # appended manually below
        else:
            other_entries.append(entry)
    if blocks_entry is None:
        print(f"error: could not find '{BLOCKS_TITLE}' branch in {TOC}", file=sys.stderr)
        return 1

    # No-blocks variant: everything except the Blocks branch, plus the index.
    no_blocks = flatten(other_entries) + [{"file": INDEX_FILE}]

    # Blocks-only variant: just the Blocks branch (rooted at level 0), plus
    # the index. We expose the Blocks subtree's *children* directly so the
    # palette parts (Motion Blocks, Looks Blocks, …) sit at the top level.
    blocks_only = flatten(blocks_entry.get("children", [])) + [{"file": INDEX_FILE}]

    block = render_variants(no_blocks, blocks_only)
    if not patch_myst_yml(block):
        return 1

    print(f"updated {MYST_YML} ({len(no_blocks)} + {len(blocks_only)} articles)")
    return 0


def render_variants(no_blocks: list[dict], blocks_only: list[dict]) -> str:
    """Render the two PDF-variant exports as a YAML snippet for myst.yml."""
    out = io.StringIO()
    out.write("  - format: tex+pdf\n")
    out.write("    title: Snap\\textit{!} Reference Manual (without block reference)\n")
    out.write("    template: ./_latex-template/\n")
    out.write("    output: output/snap-manual-no-blocks-ref.pdf\n")
    out.write("    articles:\n")
    out.write(_indent(_dump(no_blocks), 6))
    out.write("  - format: tex+pdf\n")
    out.write("    title: Snap\\textit{!} Blocks Reference\n")
    out.write("    template: ./_latex-template/\n")
    out.write("    output: output/snap-blocks-ref.pdf\n")
    out.write("    articles:\n")
    out.write(_indent(_dump(blocks_only), 6))
    return out.getvalue()


def patch_myst_yml(block: str) -> bool:
    """Replace the content between the sentinel markers in myst.yml."""
    text = MYST_YML.read_text()
    lines = text.splitlines(keepends=True)
    try:
        begin = next(i for i, line in enumerate(lines) if line.rstrip() == BEGIN_MARK.rstrip())
        end = next(i for i, line in enumerate(lines) if line.rstrip() == END_MARK.rstrip())
    except StopIteration:
        print(
            f"error: could not find both sentinel markers in {MYST_YML}.\n"
            f"  Add these lines inside the `exports:` list:\n"
            f"  {BEGIN_MARK}\n"
            f"  {END_MARK}",
            file=sys.stderr,
        )
        return False
    if end <= begin:
        print(f"error: END marker comes before BEGIN marker in {MYST_YML}", file=sys.stderr)
        return False
    new_lines = lines[: begin + 1] + [block] + lines[end:]
    MYST_YML.write_text("".join(new_lines))
    return True


def _dump(items: list[dict]) -> str:
    return yaml.safe_dump(items, default_flow_style=False, sort_keys=False, allow_unicode=True)


def _indent(text: str, spaces: int) -> str:
    pad = " " * spaces
    return "".join(pad + line if line.strip() else line for line in text.splitlines(keepends=True))


if __name__ == "__main__":
    sys.exit(main())
