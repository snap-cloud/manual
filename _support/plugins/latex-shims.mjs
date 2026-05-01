// latex-shims.mjs
// Transforms unhandled / under-handled nodes into raw `latex` nodes
// so myst-to-tex emits exactly what we want.

// Minimal LaTeX special-character escaping for plain text contexts.
function escapeLatex(rawText) {
  return String(rawText)
    .replace(/\\/g, '\\textbackslash{}')
    .replace(/([&%$#_{}])/g, '\\$1')
    .replace(/~/g, '\\textasciitilde{}')
    .replace(/\^/g, '\\textasciicircum{}');
}

// Collect plain text from any subtree (good enough for kbd contents).
function gatherText(node) {
  if (node == null) return '';
  if (typeof node.value === 'string') return node.value;
  if (Array.isArray(node.children)) return node.children.map(gatherText).join('');
  return '';
}

const latexShimsTransform = {
  name: 'latex-shims',
  stage: 'document', // runs after parse + standard transforms, before export
  plugin: (_options, utils) => (tree) => {
    // 1. <kbd> -> keyboard node. Render as a framed monospace key.
    //    Swap to \keys{...} from the `menukeys` package if you prefer.
    utils.selectAll('keyboard', tree).forEach((keyboardNode) => {
      const keyText = escapeLatex(gatherText(keyboardNode));
      keyboardNode.type = 'latex';
      keyboardNode.value = `\\fbox{\\texttt{\\small ${keyText}}}`;
      delete keyboardNode.children;
    });

    // 2. :::{grid} -> grid node (with card/gridItem children).
    //    Simplest: unwrap into a `block`, which myst-to-tex passes through
    //    so children render sequentially. Replace with a multicol/minipage
    //    construction if you actually want columns.
    // utils.selectAll('grid', tree).forEach((gridNode) => {
    //   gridNode.type = 'block';
    //   // Optionally also flatten card wrappers inside the grid:
    //   (gridNode.children || []).forEach((child) => {
    //     if (child.type === 'card' || child.type === 'gridItem') {
    //       child.type = 'block';
    //     }
    //   });
    // });

    // 3. Image customization. Example: force every figure image to 0.8\linewidth
    //    and add a \centering. Tweak as needed; or replace entirely with a raw
    //    \includegraphics for full control.
    utils.selectAll('image', tree).forEach((imageNode) => {
      // Path A: just adjust attributes the default handler reads.
      imageNode.width = imageNode.width ?? '80%';
      imageNode.align = imageNode.align ?? 'center';

      // Path B (uncomment to fully override): emit raw LaTeX.
      // const url = imageNode.url ?? '';
      // imageNode.type = 'latex';
      // imageNode.value =
      //   `\\begin{center}\\includegraphics[width=0.8\\linewidth]{${url}}\\end{center}`;
      // delete imageNode.children;
    });
  },
};

const plugin = {
  name: 'LaTeX shims (kbd, grid, image)',
  transforms: [latexShimsTransform],
};

export default plugin;
