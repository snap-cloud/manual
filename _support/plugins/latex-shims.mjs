// latex-shims.mjs
// Adapt the MyST AST so that the LaTeX export produces the rendering we want
// for inline images, block images, :::{grid} layouts, and <kbd> elements.
//
// The myst-to-tex image renderer only honours `node.url` and `node.width`
// (rendered as `\includegraphics[width=X\linewidth]{url}`). To express
// inline (line-height-scaled, raised) images and block images at a smaller
// width without forking myst-to-tex, we set sentinel widths here and pair
// them with a redefinition of \includegraphics in the LaTeX preamble (see
// `_latex-template/template.tex`). The cached image URL is filled in by
// MyST after this transform runs, so the macro receives the resolved path.
//
// MyST runs document-stage transforms once per export pipeline, but the
// AST mutations these transforms perform (sentinel widths, kbd -> raw
// LaTeX, grid -> raw `\snapgrid` env) are LaTeX-specific and would
// shrink images to 0.001px and erase grid/kbd content in the HTML
// build. We therefore gate every transform on the build flag in
// `process.argv`, applying the transforms only when MyST is invoked
// for `--pdf`, `--tex`, `--typst`, or `--all`. HTML / site / docx
// builds see the AST untouched.

const TEX_BUILD_FLAGS = new Set(['--pdf', '--tex', '-a', '--all']);
const isLatexBuild = process.argv.some((arg) => TEX_BUILD_FLAGS.has(arg));

// Width sentinels used to communicate the desired rendering to the
// custom \includegraphics defined in the LaTeX preamble. These values
// are unlikely to occur as real image widths and the preamble decodes
// them into the right \snapinline*img macro.
const SENTINEL_WIDTHS = {
  'image-inline':       0.001,  // ~1.5 baseline (default inline icon)
  'image-inline-tall':  0.002,  // ~2.4 baselines (taller hat blocks etc.)
  'image-1-5x':         0.003,  // ~1.7 baselines
  'image-2x':           0.004,  // ~2.0 baselines
  'image-3x':           0.005,  // ~2.5 baselines
  'image-4x':           0.006,  // ~3.0 baselines
};

// Block images that don't carry their own `width` attribute default to
// 30% of \linewidth. Per-image overrides can be set in markdown:
//
//     ![alt](path){width=1.5in}
//     ![alt](path){width=30%}
//
// Inch widths are converted to a percentage of the assumed text width
// below (BLOCK_LINEWIDTH_INCHES) so they fall through the standard
// myst-to-tex `width=N\linewidth` path.
const BLOCK_DEFAULT_WIDTH = '30%';

// Linewidth in inches assumed when converting `Xin` widths to a
// percentage of \linewidth. With 8.5"-wide US Letter and 0.5" margins
// (see template.tex's `\usepackage{geometry}`), \linewidth ≈ 7.5in.
const BLOCK_LINEWIDTH_INCHES = 7.5;

// Convert a width attribute that ends in `in` (inches) to a percentage
// string. Anything else passes through unchanged.
function normalizeWidth(width) {
  if (typeof width !== 'string') return width;
  const m = width.match(/^([\d.]+)\s*in$/i);
  if (!m) return width;
  const inches = parseFloat(m[1]);
  if (!Number.isFinite(inches)) return width;
  const pct = (inches / BLOCK_LINEWIDTH_INCHES) * 100;
  return `${pct.toFixed(2)}%`;
}

// Minimal LaTeX special-character escaping for plain text (used by kbd).
function escapeLatex(rawText) {
  return String(rawText)
    .replace(/\\/g, '\\textbackslash{}')
    .replace(/([&%$#_{}])/g, '\\$1')
    .replace(/~/g, '\\textasciitilde{}')
    .replace(/\^/g, '\\textasciicircum{}');
}

function gatherText(node) {
  if (node == null) return '';
  if (typeof node.value === 'string') return node.value;
  if (Array.isArray(node.children)) return node.children.map(gatherText).join('');
  return '';
}

function classList(node) {
  const cls = node?.class ?? '';
  return cls.split(/\s+/).filter(Boolean);
}

// If an image carries one of the inline-style classes, return the
// corresponding sentinel width. Otherwise return null. We test the
// most specific classes first so e.g. `image-inline-tall` wins over
// the generic `image-inline`.
const INLINE_CLASS_PRIORITY = [
  'image-inline-tall',
  'image-inline',
  'image-4x',
  'image-3x',
  'image-2x',
  'image-1-5x',
];

function inlineSentinel(node) {
  const cls = classList(node);
  for (const className of INLINE_CLASS_PRIORITY) {
    if (cls.includes(className)) return SENTINEL_WIDTHS[className];
  }
  return null;
}

// Walk a subtree and apply `fn` to every image node found.
function walkImages(root, fn) {
  if (!root) return;
  if (Array.isArray(root)) {
    root.forEach((c) => walkImages(c, fn));
    return;
  }
  if (root.type === 'image') fn(root);
  if (root.children) walkImages(root.children, fn);
}

// Apply `fn` to every node in the tree (mutating in place). Unlike
// walkImages this visits every node type, not just images.
function walkAll(node, fn) {
  if (!node) return;
  if (Array.isArray(node)) {
    node.forEach((c) => walkAll(c, fn));
    return;
  }
  fn(node);
  if (Array.isArray(node.children)) walkAll(node.children, fn);
}

// makeindex treats `! @ " |` as control characters; literal occurrences
// inside an \index{...} argument must be prefixed with `"` (the default
// quote char) so makeindex doesn't try to split them into sub-entries
// or alternate-rendering markers.
function quoteForMakeindex(s) {
  return s.replace(/(["@!|])/g, '"$1');
}

// Convert a single index entry string so that runs of `code` render as
// \texttt{...} in the printed index, while still sorting on the plain
// text. We rewrite the string into makeindex's `sort@display` form,
// which tells makeindex to alphabetize on the part before the `@` but
// typeset the part after it. Without this, leading backticks would
// sort the entry under "Symbols" and render as curly quotes.
//
// `⚡` (and the variation-selector form `⚡️`) is similarly recoded so
// it sorts under "lightning bolt" and is typeset via \snaplightning,
// which is defined in the preamble (the body font has no glyph for
// ⚡, so passing it through verbatim renders as a missing-glyph box).

// Symbol-to-ASCII map used when building the makeindex sort key for an
// entry that contains non-ASCII characters. makeindex is byte-oriented
// and treats every UTF-8 lead byte (0x80-0xFF) as the same alphabet
// "letter" group, so an entry like "≤ block" creates a singleton group
// whose heading is the partial UTF-8 sequence of ≤. LuaTeX then chokes
// reading the .ind file ("String contains an invalid utf-8 sequence"),
// which leaves \textbf{ unclosed and ends the index `multicols` early.
// Translating known symbols to a stable ASCII name in the sort key
// keeps the printed display untouched while putting the entry in a
// real letter group.
const INDEX_SORT_REPLACEMENTS = [
  [/⚡️?/g, 'lightning bolt'],
  [/≤/g, 'less or equal'],
  [/≥/g, 'greater or equal'],
  [/➔/g, 'arrow'],
  [/…/g, '...'],
  [/[“”]/g, '"'],
  [/[‘’]/g, "'"],
  [/—/g, '-'],
  [/–/g, '-'],
];

function asciiSortKey(value) {
  let out = value;
  for (const [re, rep] of INDEX_SORT_REPLACEMENTS) out = out.replace(re, rep);
  // Strip anything still outside ASCII so makeindex sorts on a clean
  // single-byte string. Collapse whitespace introduced by the replacement.
  out = out.replace(/[^\x20-\x7e]/g, '').replace(/\s+/g, ' ').trim();
  return out;
}

function rewriteIndexEntry(value) {
  if (typeof value !== 'string') return value;
  // Trailing backslashes on index entries (sometimes left over from
  // markdown line-continuation syntax in the source) would escape the
  // closing brace of \index{...} when written to LaTeX. Strip them
  // unconditionally — there's never a legitimate use for them inside
  // an index term.
  value = value.replace(/\\+\s*$/, '').trim();
  const hasCode = value.includes('`');
  const hasNonAscii = /[^\x00-\x7f]/.test(value);
  if (!hasCode && !hasNonAscii) return value;
  // Display: `set` -> \texttt{set}; ⚡ (with optional VS-16) -> \snaplightning{}.
  // # / % / & are parameter / comment / tab-alignment characters in LaTeX
  // and would break the .ind file makeindex emits if left bare inside the
  // \texttt{...} group. _ is already typically escaped by myst upstream
  // but we double-escape defensively.
  // Display-side rewrites: render `code` as \texttt{...}; map symbols
  // that have no glyph in the body font (Source Serif Pro) to a TeX
  // command that does — \snaplightning{} for ⚡, \textrightarrow{} for
  // the ➔ found in block names like `sentence ➔ list`. Without these
  // the .ind file would render a missing-glyph box for those symbols.
  const display = quoteForMakeindex(
    value
      .replace(/`([^`]+)`/g, (_m, code) =>
        `\\texttt{${code.replace(/(?<!\\)([#%&_])/g, '\\$1')}}`,
      )
      .replace(/⚡️?/g, '\\snaplightning{}')
      .replace(/➔/g, '\\textrightarrow{}'),
  );
  // Sort key: drop formatting markers, translate known symbols to ASCII
  // names so they alphabetize sensibly, and strip anything else outside
  // ASCII so makeindex doesn't make a bogus single-byte letter group.
  const sort = quoteForMakeindex(
    asciiSortKey(value.replace(/`/g, '')),
  );
  return `${sort}@${display}`;
}

// Symbols that have no glyph in the body fonts (Source Serif Pro,
// Latin Modern Mono) and therefore render as a missing-character box
// in the PDF. Each entry maps the source character (with an optional
// trailing variation selector U+FE0F) to a TeX command that renders
// something visually equivalent in any body font.
const BODY_SYMBOL_MAP = [
  { re: /⚡️?/g, tex: '\\snaplightning{}' },
  { re: /➔/g,    tex: '\\textrightarrow{}' },
];

const BODY_SYMBOL_RE = new RegExp(
  BODY_SYMBOL_MAP.map((s) => s.re.source).join('|'),
  'g',
);

// Replace symbols that have no body-font glyph inside a text node with
// raw TeX commands. Returns either null (no change), or an array of
// replacement nodes when a symbol appears in the middle of a string.
function expandSymbolsInTextNode(node) {
  if (node.type !== 'text' || typeof node.value !== 'string') return null;
  if (!BODY_SYMBOL_RE.test(node.value)) return null;
  // BODY_SYMBOL_RE is global; reset state before splitting per-symbol.
  BODY_SYMBOL_RE.lastIndex = 0;
  const out = [];
  let cursor = 0;
  for (const m of node.value.matchAll(BODY_SYMBOL_RE)) {
    if (m.index > cursor) {
      out.push({ type: 'text', value: node.value.slice(cursor, m.index) });
    }
    const matched = m[0];
    const entry = BODY_SYMBOL_MAP.find((s) => {
      s.re.lastIndex = 0;
      return s.re.test(matched);
    });
    out.push({ type: 'raw', lang: 'tex', tex: entry?.tex ?? matched });
    cursor = m.index + matched.length;
  }
  if (cursor < node.value.length) {
    out.push({ type: 'text', value: node.value.slice(cursor) });
  }
  return out;
}

function rewriteSymbolsInChildren(parent) {
  if (!Array.isArray(parent.children)) return;
  for (let i = 0; i < parent.children.length; i++) {
    const replacement = expandSymbolsInTextNode(parent.children[i]);
    if (replacement) {
      parent.children.splice(i, 1, ...replacement);
      i += replacement.length - 1;
    }
  }
}

const latexShimsTransform = {
  name: 'latex-shims',
  stage: 'document',
  plugin: (_options, utils) => (tree) => {
    // Skip transforms entirely on non-LaTeX builds: the mutations below
    // (sentinel widths, raw-tex grid/kbd nodes) would degrade the HTML
    // and Typst renders.
    if (!isLatexBuild) return;
    // 1. <kbd> -> \kbd{...} (defined in the LaTeX preamble).
    utils.selectAll('keyboard', tree).forEach((node) => {
      const keyText = escapeLatex(gatherText(node));
      node.type = 'raw';
      node.lang = 'tex';
      node.tex = `\\kbd{${keyText}}`;
      delete node.children;
    });

    // 2. :::{grid} N -> a snapgrid environment with one snapgriditem per child.
    //    We keep the children as `block` nodes so their content (including
    //    images) is still rendered by the standard handlers.
    utils.selectAll('grid', tree).forEach((gridNode) => {
      // myst stores the column count in `columns`. It's an array of
      // breakpoint counts ([sm, md, lg, xl]) or a single-element array.
      // We want the largest count (used at full-page breakpoints in
      // print).
      const rawCols = Array.isArray(gridNode.columns)
        ? gridNode.columns[gridNode.columns.length - 1]
        : (gridNode.columns ?? gridNode.argument ?? 2);
      const ncols = Math.max(1, parseInt(rawCols, 10) || 2);
      // Leave a small gap between columns; minipages use a fraction of \linewidth.
      const colWidth = (1 / ncols - 0.01).toFixed(3);

      const items = (gridNode.children || []).filter(
        (c) => c.type === 'gridItem' || c.type === 'grid-item' || c.type === 'card',
      );

      // Each `raw` node is concatenated verbatim into the output by
      // myst-to-tex (no separator), so trailing `%` here would swallow
      // whatever follows. Use explicit `\n` instead.
      const newChildren = [{ type: 'raw', lang: 'tex', tex: '\n\\begin{snapgrid}\n' }];
      items.forEach((item, idx) => {
        // Within a grid, images should fill the column rather than
        // shrinking to BLOCK_DEFAULT_WIDTH, so flag them with a sentinel.
        walkImages(item, (img) => {
          if (inlineSentinel(img) == null) {
            img.width = '100%';
            img._snapInGrid = true;
          }
        });
        newChildren.push({
          type: 'raw',
          lang: 'tex',
          tex: `\\snapgriditem{${colWidth}}{`,
        });
        newChildren.push({ type: 'block', children: item.children || [] });
        const last = idx === items.length - 1;
        newChildren.push({
          type: 'raw',
          lang: 'tex',
          tex: last ? '}\n' : '}\\snapgridsep\n',
        });
      });
      newChildren.push({ type: 'raw', lang: 'tex', tex: '\\end{snapgrid}\n' });

      gridNode.type = 'block';
      gridNode.children = newChildren;
    });

    // 3. Index entries: rewrite `code` and ⚡ inside index entries into
    //    a makeindex sort@display string so the printed index uses
    //    \texttt{...} / \snaplightning instead of literal backticks
    //    or missing-glyph boxes (and so the entries sort properly).
    walkAll(tree, (node) => {
      if (!Array.isArray(node.indexEntries)) return;
      node.indexEntries.forEach((ie) => {
        if (typeof ie?.entry === 'string') {
          ie.entry = rewriteIndexEntry(ie.entry);
        }
        if (ie?.subEntry && typeof ie.subEntry.value === 'string') {
          ie.subEntry.value = rewriteIndexEntry(ie.subEntry.value);
        }
      });
    });

    // 4. Body-font symbol substitutions. Source Serif Pro and Latin
    //    Modern Mono have no glyph for the ⚡ and ➔ symbols Snap! uses
    //    in block names, so we splice in raw-TeX nodes wherever they
    //    appear. Index-entry strings were already handled above.
    walkAll(tree, (node) => rewriteSymbolsInChildren(node));

    // 5. Image sizing.
    //    Inline images get a sentinel width that the custom \includegraphics
    //    redefinition in the preamble decodes back into a height-based,
    //    raisebox'd \includegraphics. Block images that have no explicit
    //    width get our reduced default (BLOCK_DEFAULT_WIDTH); explicit
    //    `Xin` widths from markdown attrs are converted to percentages.
    utils.selectAll('image', tree).forEach((imageNode) => {
      const sentinel = inlineSentinel(imageNode);
      if (sentinel != null) {
        imageNode.width = sentinel;
        imageNode.align = undefined;
      } else if (imageNode._snapInGrid) {
        // Already set to 100% above.
      } else if (imageNode.width == null) {
        imageNode.width = BLOCK_DEFAULT_WIDTH;
      } else {
        imageNode.width = normalizeWidth(imageNode.width);
      }
    });

    // 6. Keep inline images inline. myst-to-tex closes EVERY image node
    //    with a blank line (a forced \par in TeX), so an inline image
    //    mid-sentence would split its paragraph and put a line break
    //    after the image. We can't stop the serializer from emitting the
    //    blank line without forking myst-to-tex, but we can defuse it:
    //    bracket each inline image with raw-TeX siblings
    //    (\snapinlineopen / \snapinlineclose, defined in template.tex)
    //    that scope a no-op \par around the image. A genuine paragraph
    //    end still breaks normally because it is serialized after the
    //    closing marker. Nodes are tagged so re-runs of this transform
    //    (one per export pipeline) don't wrap twice.
    walkAll(tree, (node) => {
      if (!Array.isArray(node.children)) return;
      for (let i = 0; i < node.children.length; i++) {
        const child = node.children[i];
        if (child?.type !== 'image' || child._snapInlineWrapped) continue;
        if (inlineSentinel(child) == null) continue;
        child._snapInlineWrapped = true;
        node.children.splice(i, 0, {
          type: 'raw',
          lang: 'tex',
          tex: '\\snapinlineopen{}',
        });
        node.children.splice(i + 2, 0, {
          type: 'raw',
          lang: 'tex',
          tex: '\\snapinlineclose{}',
        });
        i += 2;
      }
    });
  },
};

export default {
  name: 'LaTeX shims (kbd, grid, image, index, lightning)',
  transforms: [latexShimsTransform],
};
