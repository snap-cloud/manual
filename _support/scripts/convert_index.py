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
        # If there's a space immediately before and after the \index{}, keep only one.
        # Don't insert a space when the following character is punctuation.
        pre  = result[:start].rstrip(' ')
        post = result[end:].lstrip(' ')
        if pre and post and not post[:1] in '.,):_-;':
            result = pre + ' ' + post
        else:
            result = (pre + post).strip()

    return result, terms, review


def make_index_block(terms: list[str]) -> list[str]:
    """Return lines for a :::{{index}} directive (no trailing newlines)."""
    lines = [f':::{{index}} {terms[0]}']
    lines.extend(terms[1:])
    lines.append(':::')
    return lines


# ── File processing ───────────────────────────────────────────────────────────

def _collapse_multiline_index(lines: list[str]) -> list[str]:
    """Join lines where \\index{ is opened but not closed before EOL."""
    result = []
    buf: str | None = None
    for line in lines:
        if buf is not None:
            buf = buf.rstrip() + ' ' + line.lstrip()
            depth = buf.count('{') - buf.count('}')
            if depth <= 0:
                result.append(buf)
                buf = None
        else:
            depth_in_index = 0
            pos = 0
            in_index = False
            for m in re.finditer(r'\\index\{', line):
                in_index = True
                depth_in_index = 1
                for ch in line[m.end():]:
                    if ch == '{':
                        depth_in_index += 1
                    elif ch == '}':
                        depth_in_index -= 1
                        if depth_in_index == 0:
                            break
            if in_index and depth_in_index > 0:
                buf = line
            else:
                result.append(line)
    if buf is not None:
        result.append(buf)
    return result


def process_file(filepath: Path, apply: bool, interactive: bool = False) -> int:
    text = filepath.read_text(encoding='utf-8')
    orig_lines = _collapse_multiline_index(text.splitlines())

    print(f'\n{"=" * 64}')
    print(f'File: {filepath}')
    print(f'{"=" * 64}')

    in_code_fence = False

    # ── Pass 1: build clean_lines, collect changed-paragraph records ──────────
    # clean_lines has \index{} stripped from all paragraph text (no blocks added).
    # heading_indices records which positions in clean_lines are headings.

    clean_lines:    list[str]  = []
    heading_indices: list[int] = []

    para_orig:  list[str] = []
    para_clean: list[str] = []
    para_terms: list[str] = []
    para_start  = 1
    para_review = False

    changed_paras: list[dict] = []

    def flush_para() -> None:
        nonlocal para_start, para_review
        if not para_orig:
            return
        first_idx = len(clean_lines)
        clean_lines.extend(para_clean)
        if para_terms:
            changed_paras.append({
                'clean_idx': first_idx,
                'clean_len': len(para_clean),
                'terms':     list(para_terms),
                'orig':      list(para_orig),
                'clean':     list(para_clean),
                'review':    para_review,
                'lineno':    para_start,
            })
        para_orig.clear(); para_clean.clear(); para_terms.clear()
        para_start = 0; para_review = False

    for lineno, line in enumerate(orig_lines, 1):
        stripped = line.strip()

        if re.match(r'^(`{3,}|~{3,})', stripped):
            in_code_fence = not in_code_fence

        if not stripped and not in_code_fence:
            flush_para()
            clean_lines.append(line)
            continue

        if not para_orig:
            para_start = lineno

        if not in_code_fence and re.match(r'^#{1,6}\s', line):
            flush_para()
            heading_indices.append(len(clean_lines))
            clean_lines.append(line)
            continue

        if in_code_fence or r'\index{' not in line:
            para_orig.append(line)
            para_clean.append(line)
        else:
            clean, terms, review = strip_index_from_line(line)
            para_orig.append(line)
            para_clean.append(clean)
            for t in terms:
                if t not in para_terms:
                    para_terms.append(t)
            if review:
                para_review = True

    flush_para()

    change_count = len(changed_paras)

    if not change_count:
        print('  (nothing to convert)')
        print(f'\n(0 paragraphs with index entries)')
        return 0

    # ── Pass 2: interactive review (per paragraph) ────────────────────────────

    accepted_set: set[int] = set()
    quit_all = False

    if not interactive:
        for rec in changed_paras:
            rev_flag = '  ⚠ REVIEW' if rec['review'] else ''
            print(f'\n  L{rec["lineno"]}{rev_flag}')
            for ln in rec['orig']:
                print(f'    {DIM}{ln}{RESET}')
            print(f'    {DIM}→{RESET}')
            for ln in rec['clean']:
                print(f'    {ln}')
        accepted_set = set(range(change_count))
    else:
        for i, rec in enumerate(changed_paras):
            if quit_all:
                break
            rev_flag = '  ⚠ REVIEW' if rec['review'] else ''
            print(f'\n  L{rec["lineno"]}{rev_flag}')
            print(f'  {RED}BEFORE:{RESET}')
            for ln in rec['orig']:
                print(f'    {ln}')
            print(f'  {GREEN}AFTER:{RESET}')
            for ln in rec['clean']:
                print(f'    {ln}')
            raw = input(f'  {DIM}[Enter=accept  s=skip  q=quit]{RESET} ').strip()
            print()
            if raw == 'q':
                quit_all = True
            elif raw != 's':
                accepted_set.add(i)

    accepted_count = len(accepted_set)

    # Revert rejected paragraphs in clean_lines to their original text.
    for i, rec in enumerate(changed_paras):
        if i not in accepted_set:
            start = rec['clean_idx']
            for j, orig_ln in enumerate(rec['orig']):
                clean_lines[start + j] = orig_ln

    # ── Pass 3: assign accepted terms to their closest preceding heading ───────
    # heading_index -1 is a sentinel meaning "before the first heading".

    terms_at_heading: dict[int, list[str]] = {}

    for i, rec in enumerate(changed_paras):
        if i not in accepted_set:
            continue
        h_idx = -1
        for hi in heading_indices:
            if hi <= rec['clean_idx']:
                h_idx = hi
            else:
                break
        if h_idx not in terms_at_heading:
            terms_at_heading[h_idx] = []
        for t in rec['terms']:
            if t not in terms_at_heading[h_idx]:
                terms_at_heading[h_idx].append(t)

    # Show placement summary.
    if terms_at_heading:
        print(f'\n  Index blocks → before heading:')
        for h_idx in sorted(terms_at_heading):
            label = '(start of file)' if h_idx == -1 else clean_lines[h_idx].strip()
            print(f'    {BOLD}{label}{RESET}')
            for t in terms_at_heading[h_idx]:
                print(f'      {t}')

    # ── Pass 4: build output ──────────────────────────────────────────────────
    # Insert each block immediately before its heading (and before any MyST
    # cross-reference labels "(name)=" that must sit directly above the heading).

    new_lines: list[str] = []

    if -1 in terms_at_heading:
        new_lines.extend(make_index_block(terms_at_heading[-1]))
        new_lines.append('')

    for i, line in enumerate(clean_lines):
        if i in terms_at_heading:
            # Step back past any (label)= anchors already appended so the block
            # lands before them, keeping the label adjacent to its heading.
            labels: list[str] = []
            while new_lines and re.match(r'^\([^)]+\)=$', new_lines[-1].strip()):
                labels.insert(0, new_lines.pop())
            new_lines.extend(make_index_block(terms_at_heading[i]))
            new_lines.append('')
            new_lines.extend(labels)
        new_lines.append(line)

    # ── Write / report ────────────────────────────────────────────────────────

    if not interactive:
        if apply and accepted_count > 0:
            out = '\n'.join(new_lines)
            if text.endswith('\n') and not out.endswith('\n'):
                out += '\n'
            filepath.write_text(out, encoding='utf-8')
            print('  -> Written.')
        print(f'\n({change_count} paragraph{"s" if change_count != 1 else ""} with index entries)')
        return change_count
    else:
        print(f'  {accepted_count} accepted.')
        if accepted_count > 0:
            out = '\n'.join(new_lines)
            if text.endswith('\n') and not out.endswith('\n'):
                out += '\n'
            filepath.write_text(out, encoding='utf-8')
            print('  -> Written.')
        return accepted_count


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
