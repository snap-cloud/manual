/**
 * MyST transform: remove default center-alignment from .image-inline images.
 *
 * By default MyST sets align='center' on every image, which causes the React
 * renderer to inject `style="margin-left:auto;margin-right:auto"` as an inline
 * style — defeating any CSS override. Setting align to undefined produces no
 * inline margin style at all, leaving layout entirely to the stylesheet.
 */

const INLINE_CLASSES = new Set(['image-inline', 'image-inline-tall']);

function hasInlineClass(node) {
  const cls = node.class ?? '';
  return cls.split(/\s+/).some((c) => INLINE_CLASSES.has(c));
}

function walk(node, fn) {
  fn(node);
  if (node.children) node.children.forEach((child) => walk(child, fn));
}

// alert('hello');

const inlineImageAlignTransform = {
  name: 'inline-image-align',
  doc: 'Clear align on .image-inline/.image-inline-tall images to prevent margin:auto inline styles.',
  stage: 'document',
  plugin: () => (tree) => {
    walk(tree, (node) => {
      if (node.type === 'image' && hasInlineClass(node)) {
        console.log(node);
        node.align = '_';
      }
    });
  },
};

export default {
  name: 'snap-manual',
  transforms: [inlineImageAlignTransform],
};
