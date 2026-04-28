#!/usr/bin/env python3
"""Convert LaTeX-style \\index{} entries to MyST/JupyterBook 2 {index}`` format.

Handles:
  - \\index{term}               → {index}`term`
  - \\index{main!sub}           → {index}`main; sub`  (sub-entries)
  - \\index{sortkey@display}    → {index}`display`    (@ sort key stripped)
  - \\index{*sort@display}      → {index}`display`    (* sort prefix stripped)
  - \\texttt{x}, $x$           → `x`   (code formatting)
  - \\textit{x}                → *x*  (italic)
  - Inline deduplication: word\\index{word} → {index}`word`
  - Nested braces in \\texttt{} handled correctly
  - ! inside "quoted strings" not treated as sub-entry separator

Usage:
    python convert_index.py path/to/file.md
    python convert_index.py path/to/directory/
    python convert_index.py "chapters/**/*.md"   # quote the glob!
    python convert_index.py file.md --apply      # write changes
"""

import re
import sys
import glob
import argparse
import readline
from pathlib import Path


def input_with_prefill(prompt: str, prefill: str = '') -> str:
    """Like input(), but with *prefill* pre-loaded for editing."""
    def hook() -> None:
        readline.insert_text(prefill)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    try:
        return input(prompt)
    finally:
        readline.set_pre_input_hook(None)


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
    # Process from innermost braces outward; iterate until stable
    for _ in range(5):
        prev = text
        text = re.sub(r'\\texttt\{([^{}]*)\}', r'`\1`', text)
        text = re.sub(r'\\textit\{([^{}]*)\}', r'*\1*', text)
        text = re.sub(r'\\textbf\{([^{}]*)\}', r'**\1**', text)
        text = re.sub(r'\\emph\{([^{}]*)\}',   r'*\1*', text)
        # strip remaining unknown \cmd{...} – keep contents
        text = re.sub(r'\\[a-zA-Z]+\{([^{}]*)\}', r'\1', text)
        if text == prev:
            break
    return text


def _expand_math_dollars(text: str) -> str:
    """Convert $term$ → `term` (inline math → inline code for index)."""
    # \$already handled; match un-escaped $...$
    return re.sub(r'\$([^$]+)\$', r'`\1`', text)


def _apply_simple_macros(text: str) -> str:
    for macro, replacement in SIMPLE_MACROS.items():
        text = text.replace(macro, replacement)
    return text


# ── Index term parsing ────────────────────────────────────────────────────────

def _split_on_bang_outside_quotes(s: str) -> tuple[str, str | None]:
    """Split s on first ! NOT inside double-quotes or backtick spans."""
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
    """Remove leading * (sort-first marker) or other leading punctuation sort tricks."""
    return part.lstrip('*').strip()


def _strip_sort_key(part: str) -> str:
    """Given 'sortkey@display', return display. With no @, return part itself."""
    if '@' in part:
        _sort, display = part.split('@', 1)
        return display.strip()
    return part.strip()


def convert_index_term(raw_term: str) -> tuple[str, bool]:
    """
    Convert a raw LaTeX index term to a MyST display string.

    Returns (myst_term, needs_review) where needs_review is True when the
    result may need manual inspection (e.g. contains backticks).
    """
    term = raw_term

    # Expand \\texttt{}, \\textit{}, etc. first (handles nested braces)
    term = _expand_braced_commands(term)
    # Convert $math$ → `code`
    term = _expand_math_dollars(term)
    # Simple macro replacements
    term = _apply_simple_macros(term)

    # Split on ! for sub-entries (ignoring ! inside quotes)
    main_part, sub_part = _split_on_bang_outside_quotes(term)

    # Strip leading sort-order markers (*)
    main_part = _strip_sort_prefix(main_part)
    # Strip sort@display from each part
    main_display = _strip_sort_key(main_part)

    if sub_part is not None:
        sub_part = _strip_sort_prefix(sub_part)
        sub_display = _strip_sort_key(sub_part)
        result = f'{main_display}; {sub_display}'
    else:
        result = main_display

    # Strip outer "double quotes" if the whole term is quoted
    result = result.strip()
    if result.startswith('"') and result.endswith('"'):
        result = result[1:-1].strip()

    # Flag only entries with unresolved LaTeX (stray braces or backslashes)
    needs_review = '{' in result or '}' in result or ('\\' in result and '\\' != result)
    return result, needs_review


def make_myst(term: str, display: str | None = None) -> str:
    """
    Produce a {index}`` role string.

    - Simple term, no display override: {index}`term`
    - Term with backtick code spans, or explicit display override:
        {index}``display text <index term>``
      Double-backtick role delimiters allow single backticks in the content.

    display — if provided, used as the inline text; term goes into <>.
              If None and term has backticks, display is derived by stripping them.
    """
    if display is None and '`' not in term:
        return f'{{index}}`{term}`'
    if display is None:
        # Derive plain display by stripping backtick spans
        display = re.sub(r'`', '', term)
        display = re.sub(r'\s+', ' ', display).strip()
    if '`' not in term:
        if normalize(display) == normalize(term):
            return f'{{index}}`{term}`'
        return f'{{index}}`{display} <{term}>`'
    return f'{{index}}``{display} <{term}>``'


# ── Brace-aware \\index{} extraction ─────────────────────────────────────────

def find_index_spans(line: str) -> list[tuple[int, int, str]]:
    """
    Locate all \\index{...} spans in *line*, handling nested braces.
    Returns list of (start, end, raw_term).
    """
    results = []
    i = 0
    while i < len(line):
        pos = line.find(r'\index{', i)
        if pos == -1:
            break
        # Walk forward counting braces
        depth = 0
        start = pos
        j = pos + len(r'\index')  # points at '{'
        term_start = j + 1
        while j < len(line):
            if line[j] == '{':
                depth += 1
            elif line[j] == '}':
                depth -= 1
                if depth == 0:
                    raw_term = line[term_start:j]
                    results.append((start, j + 1, raw_term))
                    i = j + 1
                    break
            j += 1
        else:
            # Unmatched brace – skip
            i = pos + 1
    return results


# ── Deduplication helpers ─────────────────────────────────────────────────────

def normalize(s: str) -> str:
    return re.sub(r'[^a-z0-9]', '', s.lower())


def _matching_word_suffix(prec_norm: list[str], term_norm: list[str]) -> int:
    """
    Return how many trailing words in *prec_norm* match *term_norm*.

    If term is longer than prec, return len(prec) when prec is a
    prefix of term (e.g. "Catch" matching "`catch` block").
    Returns 0 for no match.
    """
    n_p, n_t = len(prec_norm), len(term_norm)
    if not n_p or not n_t:
        return 0
    if n_t <= n_p:
        return n_t if prec_norm[-n_t:] == term_norm else 0
    else:
        return n_p if prec_norm == term_norm[:n_p] else 0


def find_preceding_span(text: str, match_start: int) -> tuple[str | None, int]:
    """
    Find the word/phrase immediately before match_start, possibly wrapped in
    inline formatting markers (``, *, **).
    Returns (word_for_compare, removal_start) where removal_start is the
    position in *text* to begin erasing (includes the opening format marker).
    Returns (None, -1) if nothing suitable found.
    """
    before = text[:match_start]
    WORDS = r"[\w\'\-/]+"
    PHRASE = rf'{WORDS}(?:[\s\-]+{WORDS}){{0,5}}'
    for pat, word_group in [
        (rf'(`{{1,2}})({PHRASE})\1\s*$', 2),    # `word`  or  ``word``
        (rf'(\*{{1,2}})({PHRASE})\1\s*$', 2),   # *word*  or  **word**
        (rf'(\b{PHRASE})\s*$', 1),               # plain word(s)
    ]:
        m = re.search(pat, before)
        if m:
            return m.group(word_group), m.start()
    return None, -1


# ── Word-boundary context helpers ────────────────────────────────────────────

N_WORDS = 3  # words of context to show / edit on each side


def _walk_back_words(text: str, pos: int, n: int) -> int:
    """Return start position after stepping back n word-spaces from pos."""
    count = 0
    i = pos - 1
    while i >= 0:
        if text[i] == ' ':
            count += 1
            if count >= n:
                return i + 1
        i -= 1
    return 0


def _walk_fwd_words(text: str, pos: int, n: int) -> int:
    """Return end position after stepping forward n word-spaces from pos."""
    count = 0
    i = pos
    while i < len(text):
        if text[i] == ' ':
            count += 1
            if count >= n:
                return i
        i += 1
    return len(text)


# ── Per-span proposal ─────────────────────────────────────────────────────────

class SpanProposal:
    """All data needed to display and optionally apply one \\index{} change."""
    __slots__ = ('myst', 'myst_term', 'actual_start', 'adj_end',
                 'base_new_offset', 'b_pre', 'b_mid', 'needs_review')

    def __init__(self, **kw: object) -> None:
        for k, v in kw.items():
            setattr(self, k, v)

    def after_ctx(self, result: str, role: str | None = None) -> tuple[str, str]:
        """
        Return (a_pre, a_role) for display: N words before the role, then the role.
        Operates on the proposed result (role not yet applied to result).
        """
        role = role or self.myst
        proposed = result[:self.actual_start] + role + result[self.adj_end:]
        a_start = _walk_back_words(proposed, self.actual_start, N_WORDS)
        return proposed[a_start:self.actual_start], role

    def edit_section(self, result: str) -> tuple[str, int, int]:
        """
        Return (section_text, sec_start, sec_end) in the proposed result:
        N words before + role + N words after — the region the user edits.
        """
        proposed, _ = self.apply(result)
        ins_end = self.actual_start + len(self.myst)
        sec_start = _walk_back_words(proposed, self.actual_start, N_WORDS)
        sec_end   = _walk_fwd_words(proposed, ins_end, N_WORDS)
        return proposed[sec_start:sec_end], sec_start, sec_end

    def apply(self, result: str, custom_myst: str | None = None) -> tuple[str, int]:
        """Apply (optionally with a custom role). Returns (new_result, new_offset)."""
        role = custom_myst if custom_myst is not None else self.myst
        new_result = result[:self.actual_start] + role + result[self.adj_end:]
        new_offset = self.base_new_offset + (len(role) - len(self.myst))
        return new_result, new_offset


def _compute_span(result: str, offset: int,
                  orig_start: int, orig_end: int, raw_term: str,
                  line: str) -> SpanProposal:
    """Compute the proposed replacement for one \\index{} span."""
    myst_term, needs_review = convert_index_term(raw_term)
    myst = make_myst(myst_term)

    adj_start = orig_start + offset
    adj_end = orig_end + offset
    actual_start = adj_start

    preceding, remove_start = find_preceding_span(result, adj_start)
    if preceding and remove_start >= 0:
        prec_words     = preceding.split()
        term_words_raw = myst_term.split()
        norm_prec_w = [normalize(w) for w in prec_words]
        norm_term_w = [normalize(w) for w in term_words_raw]

        # Require at least 3 non-punctuation chars in the term
        if len(normalize(myst_term)) >= 3:
            match_count = _matching_word_suffix(norm_prec_w, norm_term_w)
            if match_count > 0:
                # Is the preceding text wrapped in a formatting marker?
                is_formatted = result[remove_start] in ('`', '*')

                if is_formatted or match_count == len(prec_words):
                    # Remove the whole formatted span (or full plain match)
                    actual_start = remove_start
                else:
                    # Plain text: only remove the matching suffix words, keep prefix
                    suffix_text = ' '.join(prec_words[-match_count:])
                    suffix_pos  = preceding.rfind(suffix_text)
                    actual_start = remove_start + suffix_pos if suffix_pos >= 0 else adj_start

                matched_display = ' '.join(prec_words[-match_count:])
                if '`' in myst_term and normalize(matched_display) != normalize(myst_term):
                    myst = make_myst(myst_term, display=matched_display)
                else:
                    myst = make_myst(myst_term)

    # Before context: N words before the replaced span in the original line
    orig_actual = orig_start + (actual_start - adj_start)
    b_start = _walk_back_words(line, orig_actual, N_WORDS)
    b_pre = line[b_start:orig_actual]
    b_mid = line[orig_actual:orig_end]

    return SpanProposal(
        myst=myst,
        myst_term=myst_term,
        actual_start=actual_start,
        adj_end=adj_end,
        base_new_offset=offset + len(myst) - (adj_end - actual_start),
        b_pre=b_pre,
        b_mid=b_mid,
        needs_review=needs_review,
    )


# ── Line-level conversion (batch) ────────────────────────────────────────────

def convert_line(line: str) -> tuple[str, list[tuple[str, str, str, str, bool]]]:
    """Convert all \\index{} entries in *line* (non-interactive)."""
    spans = find_index_spans(line)
    if not spans:
        return line, []

    changes: list[tuple[str, str, str, str, bool]] = []
    result = line
    offset = 0

    for orig_start, orig_end, raw_term in spans:
        p = _compute_span(result, offset, orig_start, orig_end, raw_term, line)
        result, offset = p.apply(result)
        # After context: N words before role in updated result, then just the role
        ins_end = p.actual_start + len(p.myst)
        a_start = _walk_back_words(result, p.actual_start, N_WORDS)
        a_pre  = result[a_start:p.actual_start]
        a_role = result[p.actual_start:ins_end]
        changes.append((p.b_pre, p.b_mid, a_pre, a_role, p.needs_review))

    return result, changes


# ── Shared display ────────────────────────────────────────────────────────────

BOLD = '\033[1m'
DIM  = '\033[2m'
RESET = '\033[0m'


def _print_change(lineno: int, b_pre: str, b_mid: str,
                  a_pre: str, a_role: str, review: bool) -> None:
    marker = '  ⚠ REVIEW' if review else ''
    print(f'  L{lineno:<5} {b_pre}{BOLD}{b_mid}{RESET}')
    print(f'       → {a_pre}{BOLD}{a_role}{RESET}...{marker}')


# ── File processing ───────────────────────────────────────────────────────────

def process_file(filepath: Path, apply: bool, interactive: bool = False) -> int:
    text = filepath.read_text(encoding='utf-8')
    lines = text.splitlines(keepends=True)

    new_lines: list[str] = []
    all_changes: list[tuple[int, str, str, str, str, bool]] = []
    accepted = 0
    manual_edits = 0

    print(f'\n{"=" * 64}')
    print(f'File: {filepath}')
    print(f'{"=" * 64}')

    quit_all = False

    for lineno, line in enumerate(lines, 1):
        if r'\index{' not in line or quit_all:
            new_lines.append(line)
            continue

        stripped = line.rstrip('\n')
        ending = '\n' if line.endswith('\n') else ''

        if not interactive:
            new_line, changes = convert_line(stripped)
            new_lines.append(new_line + ending)
            for b_pre, b_mid, a_pre, a_role, review in changes:
                all_changes.append((lineno, b_pre, b_mid, a_pre, a_role, review))
        else:
            # Interactive: process each span individually
            result = stripped
            offset = 0
            for orig_start, orig_end, raw_term in find_index_spans(stripped):
                p = _compute_span(result, offset, orig_start, orig_end, raw_term, stripped)
                a_pre, a_role = p.after_ctx(result)
                _print_change(lineno, p.b_pre, p.b_mid, a_pre, a_role, p.needs_review)

                raw = input(f'  {DIM}[Enter=accept  e=edit  s=skip  q=quit]{RESET} ')
                print()

                if raw == 'q':
                    quit_all = True
                    break
                elif raw == 's':
                    print()
                    continue  # leave result unchanged for this span
                elif raw == 'e':
                    edited = input_with_prefill('  > ', p.myst).strip()
                    print()
                    if not edited:
                        continue  # blank → skip
                    custom = edited if edited != p.myst else None
                    if custom:
                        manual_edits += 1
                    result, offset = p.apply(result, custom_myst=custom or p.myst)
                    ins_end = p.actual_start + len(custom or p.myst)
                    a_s = _walk_back_words(result, p.actual_start, N_WORDS)
                    all_changes.append((lineno, p.b_pre, p.b_mid,
                                        result[a_s:p.actual_start],
                                        result[p.actual_start:ins_end],
                                        p.needs_review))
                    accepted += 1
                else:
                    # Enter or anything else → accept proposed
                    result, offset = p.apply(result)
                    all_changes.append((lineno, p.b_pre, p.b_mid, a_pre, a_role, p.needs_review))
                    accepted += 1

            new_lines.append(result + ending)

    if not interactive:
        count = len(all_changes)
        review_count = sum(1 for *_, r in all_changes if r)
        flag = f'  ⚠ {review_count} need review' if review_count else ''
        print(f'({count} conversion{"s" if count != 1 else ""}{flag})')
        for lineno, b_pre, b_mid, a_pre, a_role, review in all_changes:
            _print_change(lineno, b_pre, b_mid, a_pre, a_role, review)
        if not all_changes:
            print('  (nothing to convert)')
        if apply and count > 0:
            filepath.write_text(''.join(new_lines), encoding='utf-8')
            print('  -> Written.')
        return count
    else:
        print(f'  {accepted} accepted{f", {manual_edits} manually edited" if manual_edits else ""}.')
        if accepted > 0 or manual_edits > 0:
            filepath.write_text(''.join(new_lines), encoding='utf-8')
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
        description='Convert LaTeX \\index{} to MyST {index}`` entries',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument('paths', nargs='+',
                        help='File, directory, or glob pattern (quote globs!)')
    parser.add_argument('--apply', action='store_true',
                        help='Write changes to disk (default: dry run)')
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='Review each entry interactively; implies --apply')
    args = parser.parse_args()

    interactive = args.interactive
    apply = args.apply or interactive  # -i always writes accepted changes

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
        print('  Enter=accept  e=edit  s=skip  q=quit file\n')

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
