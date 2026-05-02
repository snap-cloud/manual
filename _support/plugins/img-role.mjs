const imgRole = {
  name: 'inline',
  doc: 'Inline image with optional CSS class, width, height, and title.',
  body: {
    type: String,
    doc: 'The image URL or path.',
    required: true,
  },
  options: {
    alt: { type: String, doc: 'Alt text for accessibility.', required: true },
    class: { type: String, doc: 'CSS class(es).' },
    width: { type: String, doc: 'CSS width, e.g. 200px or 50%.' },
    height: { type: String, doc: 'CSS height.' },
    title: { type: String, doc: 'Tooltip / title attribute.' },
  },
  run(data) {
    const { alt, class: className, width, height, title } = data.options ?? {};
    return [
      {
        type: 'image',
        url: data.body.trim(),
        alt,
        class: className || 'image-inline',
        width:,
        height,
        title,
      },
    ];
  },
};

// Block image role — same shape as `inline`, but defaults to *no* class
// (so the latex-shims plugin treats it as a block image and lets the
// `width` flow through to \includegraphics). MyST doesn't parse the
// `![alt](url){width=...}` shortcut on images, so authors use this to
// override the default block width per-image:
//
//     {img alt="..." width="1.5in"}`./path/to/img.png`
//     {img alt="..." width="40%"}`./path/to/img.png`
//
// Inch widths are converted to a percentage of \linewidth by the
// latex-shims plugin before they reach myst-to-tex.
const blockImgRole = {
  name: 'img',
  doc: 'Block image with optional CSS class, width, height, and title.',
  body: {
    type: String,
    doc: 'The image URL or path.',
    required: true,
  },
  options: {
    alt: { type: String, doc: 'Alt text for accessibility.', required: true },
    class: { type: String, doc: 'CSS class(es).' },
    width: { type: String, doc: 'CSS width, e.g. 200px, 50%, or 1.5in.' },
    height: { type: String, doc: 'CSS height.' },
    title: { type: String, doc: 'Tooltip / title attribute.' },
  },
  run(data) {
    const { alt, class: className, width, height, title } = data.options ?? {};
    return [
      {
        type: 'image',
        url: data.body.trim(),
        alt,
        class: className,
        width,
        height,
        title,
      },
    ];
  },
};

const plugin = {
  name: 'Snap image roles',
  roles: [imgRole, blockImgRole],
};

export default plugin;
