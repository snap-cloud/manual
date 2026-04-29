#!/usr/bin/env python3
"""Convert LaTeX-style \\index{} entries to MyST/JupyterBook 2 {index} directive blocks.

For each paragraph containing \\index{} entries:
  - Removes them from the inline text
  - Inserts a :::{{index}} ... ::: block immediately after the paragraph

Multiple entries appear on separate lines within the block:
    :::{{index}} first term
    second term
    third term
    :::

Handles:
  - \\index{term}               → term in block
  - \\index{main!sub}           → main; sub
  - \\index{sortkey@display}    → display  (@ sort key stripped)
  - \\index{*sort@display}      → display  (* sort prefix stripped)
  - \\texttt{x}, $x$           → `x`
  - \\textit{x}                → *x*

Usage:
    python convert_index.py path/to/file.md
    python convert_index.py path/to/directory/
    python convert_index.py "chapters/**/*.md"   # quote the glob!
    python convert_index.py file.md --apply      # write changes
    python convert_index.py file.md -i           # review paragraph by paragraph
"""

import re
import sys
import glob
import argparse
from pathlib import Path


BOLD  = '\033[1m'
DIM   = '\033[2m'
GREEN = '\033[32m'
RED   = '\033[31m'
RESET = '\033[0m'


# ── LaTeX macro expansions ────────────────────────────────────────────────────

SIMPLE_MACROS = {
    r'\textbackslash': '\\',
    r'\textasciitilde': '~',
    r'\textasciicircum': '^',
    r'\textunderscore': '_',
    r'\textbar': '|',
    r'\textless': '<',
    r'\textgreater': '>',
    r'\&': '&',
    r'\%': '%',
    r'\$': '$',
    r'\#': '#',
    r'\!': '!',
    r'\,': ' ',
}


def _expand_braced_commands(text: str) -> str:
    """Expand \\texttt{x} → `x`, \\textit{x} → *x*, \\textbf{x} → **x**."""
    for _ in range(5):
        prev = text
        text = re.sub(r'\\texttt\{([^{}]*)\}', r'`\1`', text)
        text = re.sub(r'\\textit\{([^{}]*)\}', r'*\1*', text)
        text = re.sub(r'\\textbf\{([^{}]*)\}', r'**\1**', text)
        text = re.sub(r'\\emph\{([^{}]*)\}',   r'*\1*', text)
        text = re.sub(r'\\[a-zA-Z]+\{([^{}]*)\}', r'\1', text)
        if text == prev:
            break
    return text


def _expand_math_dollars(text: str) -> str:
    return re.sub(r'\$([^$]+)\$', r'`\1`', text)


def _apply_simple_macros(text: str) -> str:
    for macro, replacement in SIMPLE_MACROS.items():
        text = text.replace(macro, replacement)
    return text


# ── Index term parsing ────────────────────────────────────────────────────────

def _split_on_bang_outside_quotes(s: str) -> tuple[str, str | None]:
    in_dquotes = False
    in_backticks = False
    for i, ch in enumerate(s):
        if ch == '"':
            in_dquotes = not in_dquotes
        elif ch == '`' and not in_dquotes:
            in_backticks = not in_backticks
        elif ch == '!' and not in_dquotes and not in_backticks:
            return s[:i], s[i + 1:]
    return s, None


def _strip_sort_prefix(part: str) -> str:
    return part.lstrip('*').strip()


def _strip_sort_key(part: str) -> str:
    if '@' in part:
        _sort, display = part.split('@', 1)
        return display.strip()
    return part.strip()


def convert_index_term(raw_term: str) -> tuple[str, bool]:
    """Convert a raw LaTeX index term to a plain MyST string."""
    term = _expand_braced_commands(raw_term)
    term = _expand_math_dollars(term)
    term = _apply_simple_macros(term)

    main_part, sub_part = _split_on_bang_outside_quotes(term)
    main_part = _strip_sort_prefix(main_part)
    main_display = _strip_sort_key(main_part)

    if sub_part is not None:
        sub_part = _strip_sort_prefix(sub_part)
        sub_display = _strip_sort_key(sub_part)
        result = f'{main_display}; {sub_display}'
    else:
        result = main_display

    result = result.strip()
    if result.startswith('"') and result.endswith('"'):
        result = result[1:-1].strip()

    needs_review = '{' in result or '}' in result or ('\\' in result and result != '\\')
    return result, needs_review


# ── Index extraction ──────────────────────────────────────────────────────────

def find_index_spans(line: str) -> list[tuple[int, int, str]]:
    """Locate all \\index{...} spans, handling nested braces."""
    results = []
    i = 0
    while i < len(line):
        pos = line.find(r'\index{', i)
        if pos == -1:
            break
        depth = 0
        j = pos + len(r'\index')
        term_start = j + 1
        while j < len(line):
            if line[j] == '{':
                depth += 1
            elif line[j] == '}':
                depth -= 1
                if depth == 0:
                    results.append((pos, j + 1, line[term_start:j]))
                    i = j + 1
                    break
            j += 1
        else:
            i = pos + 1
    return results


def strip_index_from_line(line: str) -> tuple[str, list[str], bool]:
    """
    Remove all \\index{} from line.
    Returns (clean_line, terms, needs_review).
    """
    spans = find_index_spans(line)
    if not spans:
        return line, [], False

    terms = []
    result = line
    review = False
    for start, end, raw_term in reversed(spans):
        term, term_review = convert_index_term(raw_term)
        terms.insert(0, term)
        review = review or term_review
        result = result[:start] + result[end:]

    result = re.sub(r'  +', ' ', result).rstrip()
    return result, terms, review


def make_index_block(terms: list[str]) -> list[str]:
    """Return lines for a :::{{index}} directive (no trailing newlines)."""
    lines = [f':::{{index}} {terms[0]}']
    lines.extend(terms[1:])
    lines.append(':::')
    return lines


# ── File processing ───────────────────────────────────────────────────────────

def process_file(filepath: Path, apply: bool, interactive: bool = False) -> int:
    text = filepath.read_text(encoding='utf-8')
    orig_lines = text.splitlines()

    print(f'\n{"=" * 64}')
    print(f'File: {filepath}')
    print(f'{"=" * 64}')

    in_code_fence = False

    # Paragraph-level buffers
    para_orig:  list[str] = []
    para_new:   list[str] = []
    para_terms: list[str] = []
    para_start  = 1
    para_review = False

    new_lines:  list[str] = []
    change_count = 0
    accepted = 0
    quit_all = False

    def flush_para(next_lineno: int) -> None:
        nonlocal change_count, accepted, quit_all
        if not para_orig:
            return

        if not para_terms or quit_all:
            new_lines.extend(para_orig)
            return

        block = make_index_block(para_terms)
        change_count += 1

        if not interactive:
            rev_flag = '  ⚠ REVIEW' if para_review else ''
            print(f'\n  L{para_start}{rev_flag}')
            for ln in para_orig:
                print(f'    {DIM}{ln}{RESET}')
            print(f'    {DIM}→{RESET}')
            for ln in para_new:
                print(f'    {ln}')
            for ln in block:
                print(f'    {BOLD}{ln}{RESET}')
            new_lines.extend(para_new)
            new_lines.extend(block)
        else:
            rev_flag = '  ⚠ REVIEW' if para_review else ''
            print(f'\n  L{para_start}{rev_flag}')
            print(f'  {RED}BEFORE:{RESET}')
            for ln in para_orig:
                print(f'    {ln}')
            print(f'  {GREEN}AFTER:{RESET}')
            for ln in para_new:
                print(f'    {ln}')
            for ln in block:
                print(f'    {BOLD}{ln}{RESET}')

            raw = input(f'  {DIM}[Enter=accept  s=skip  q=quit]{RESET} ').strip()
            print()

            if raw == 'q':
                quit_all = True
                new_lines.extend(para_orig)
            elif raw == 's':
                new_lines.extend(para_orig)
            else:
                new_lines.extend(para_new)
                new_lines.extend(block)
                accepted += 1

    def reset_para() -> None:
        para_orig.clear()
        para_new.clear()
        para_terms.clear()
        nonlocal para_start, para_review
        para_start = 0
        para_review = False

    for lineno, line in enumerate(orig_lines, 1):
        stripped = line.strip()

        # Track fenced code blocks
        if re.match(r'^(`{3,}|~{3,})', stripped):
            in_code_fence = not in_code_fence

        if not stripped and not in_code_fence:
            # Blank line → end of paragraph
            flush_para(lineno)
            reset_para()
            new_lines.append(line)
            continue

        if not para_orig:
            para_start = lineno

        if in_code_fence or r'\index{' not in line:
            para_orig.append(line)
            para_new.append(line)
        else:
            clean, terms, review = strip_index_from_line(line)
            para_orig.append(line)
            para_new.append(clean)
            for t in terms:
                if t not in para_terms:
                    para_terms.append(t)
            if review:
                para_review = True

    # Flush final paragraph (no trailing blank line)
    flush_para(len(orig_lines) + 1)

    if not interactive:
        count = change_count
        rev_count = 0  # already printed inline
        if not count:
            print('  (nothing to convert)')
        print(f'\n({count} paragraph{"s" if count != 1 else ""} with index entries)')
        if apply and count > 0:
            out = '\n'.join(new_lines)
            if text.endswith('\n') and not out.endswith('\n'):
                out += '\n'
            filepath.write_text(out, encoding='utf-8')
            print('  -> Written.')
        return count
    else:
        print(f'  {accepted} accepted.')
        if accepted > 0:
            out = '\n'.join(new_lines)
            if text.endswith('\n') and not out.endswith('\n'):
                out += '\n'
            filepath.write_text(out, encoding='utf-8')
            print('  -> Written.')
        return accepted


# ── File discovery ────────────────────────────────────────────────────────────

def collect_files(args: list[str]) -> list[Path]:
    files: list[Path] = []
    for arg in args:
        p = Path(arg)
        if p.is_file():
            files.append(p)
        elif p.is_dir():
            files.extend(sorted(p.rglob('*.md')))
        else:
            matched = glob.glob(arg, recursive=True)
            files.extend(Path(f) for f in sorted(matched)
                         if Path(f).is_file() and f.endswith('.md'))
    seen: set[Path] = set()
    unique: list[Path] = []
    for f in files:
        resolved = f.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(f)
    return unique


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description='Convert LaTeX \\index{} to MyST :::{{index}} directive blocks',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument('paths', nargs='+',
                        help='File, directory, or glob pattern (quote globs!)')
    parser.add_argument('--apply', action='store_true',
                        help='Write changes to disk (default: dry run)')
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='Review each paragraph interactively; implies --apply')
    args = parser.parse_args()

    interactive = args.interactive
    apply = args.apply or interactive

    files = collect_files(args.paths)
    if not files:
        print('No .md files found.', file=sys.stderr)
        sys.exit(1)

    if interactive:
        mode = 'INTERACTIVE'
    elif apply:
        mode = 'APPLY'
    else:
        mode = 'DRY RUN'
    print(f'Mode: {mode} | Files: {len(files)}')
    if interactive:
        print('  Enter=accept  s=skip  q=quit file\n')

    total = 0
    file_counts: dict[Path, int] = {}

    for fp in files:
        n = process_file(fp, apply=apply, interactive=interactive)
        if n:
            file_counts[fp] = n
            total += n

    print(f'\n{"=" * 64}')
    print('SUMMARY')
    print(f'{"=" * 64}')
    print(f'Files scanned:          {len(files)}')
    print(f'Files with conversions: {len(file_counts)}')
    print(f'Total {"accepted" if interactive else "conversions"}:{" " * 9}{total}')
    if file_counts:
        print()
        print('Per-file breakdown (sorted by count):')
        for fp, n in sorted(file_counts.items(), key=lambda x: -x[1]):
            print(f'  {n:4d}  {fp}')
    if not apply and total:
        print(f'\nRe-run with --apply to write changes.')


if __name__ == '__main__':
    main()
