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
// 40% of \linewidth. Per-image overrides can be set in markdown:
//
//     ![alt](path){width=1.5in}
//     ![alt](path){width=30%}
//
// Inch widths are converted to a percentage of the assumed text width
// below (BLOCK_LINEWIDTH_INCHES) so they fall through the standard
// myst-to-tex `width=N\linewidth` path.
const BLOCK_DEFAULT_WIDTH = '40%';

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

    // 3. Image sizing.
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
  },
};

export default {
  name: 'LaTeX shims (kbd, grid, image)',
  transforms: [latexShimsTransform],
};
