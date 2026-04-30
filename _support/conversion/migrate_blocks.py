#!/usr/bin/env python3
"""
migrate_blocks.py — Move `partial-data` from each blocks/**/*.md frontmatter
into a sidecar at the same path with a .yml extension, and replace the old
Quarto partial+python invocation with `{block-help}`.

Idempotent. Defaults to dry-run; pass --apply to write changes.
"""
from __future__ import annotations
import argparse
import re
import sys
from io import StringIO
from pathlib import Path

from ruamel.yaml import YAML

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)

# The old Quarto partial-include + python block. Tweak if your sources differ.
OLD_BLOCK_RE = re.compile(
    r"<!--\s*\{\{<\s*partial\s+blocks/_block\.qmd\s*>\}\}\s*-->\s*"
    r"```\{python\}.*?```",
    re.DOTALL,
)

NEW_DIRECTIVE = "```{block-help}\n```"

def load_yaml() -> YAML:
    yaml = YAML(typ="rt")  # round-trip: keep comments + key order
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    return yaml

def split_frontmatter(text: str) -> tuple[str | None, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, text
    return match.group(1), text[match.end():]

def dump_yaml_str(yaml: YAML, data) -> str:
    buf = StringIO()
    yaml.dump(data, buf)
    return buf.getvalue()

def migrate_file(md_path: Path, yaml: YAML, apply: bool) -> str:
    text = md_path.read_text()
    fm_text, body = split_frontmatter(text)
    if fm_text is None:
        return f"skip    {md_path}: no frontmatter"

    fm = yaml.load(fm_text)
    if not fm or "partial-data" not in fm:
        return f"skip    {md_path}: no partial-data"

    partial = fm["partial-data"]
    declared_selector = partial.get("selector")
    file_basename = md_path.stem
    if declared_selector and declared_selector != file_basename:
        # Not necessarily an error, but worth flagging during migration.
        print(
            f"note    {md_path}: selector '{declared_selector}' "
            f"does not match filename '{file_basename}'",
            file=sys.stderr,
        )

    sidecar = md_path.with_suffix(".yml")
    if sidecar.exists():
        sidecar_action = "exists "
    else:
        sidecar_action = "write  "
        if apply:
            sidecar.write_text(dump_yaml_str(yaml, partial))

    # Strip partial-data from frontmatter.
    del fm["partial-data"]
    new_fm_text = dump_yaml_str(yaml, fm).rstrip() + "\n"
    new_body, n_subs = OLD_BLOCK_RE.subn(NEW_DIRECTIVE, body, count=1)
    new_text = f"---\n{new_fm_text}---\n{new_body}"

    if apply and new_text != text:
        md_path.write_text(new_text)

    changed = "changed" if new_text != text else "unchanged"
    sub_note = "" if n_subs else " (no old-block match)"
    return f"{sidecar_action} {md_path}  ->  {sidecar}  ({changed}{sub_note})"

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", default="blocks", help="root containing **/*.md")
    parser.add_argument("--apply", action="store_true",
                        help="write changes (default: dry-run)")
    args = parser.parse_args()

    src = Path(args.src)
    yaml = load_yaml()

    md_files = sorted(src.rglob("*.md"))
    if not md_files:
        print(f"no .md files under {src}", file=sys.stderr)
        return 1

    print(f"{'APPLY' if args.apply else 'DRY-RUN'}: {len(md_files)} files under {src}")
    for md_path in md_files:
        try:
            print(migrate_file(md_path, yaml, args.apply))
        except Exception as err:
            print(f"error  {md_path}: {err}", file=sys.stderr)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
