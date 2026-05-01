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
    // console.log('img role data:', { url: data.body, alt, className, width, height, title });
    return [
      {
        type: 'image',
        url: data.body.trim(),
        alt,
        class: className || 'image-inline',
        width,
        height,
        title,
      },
    ];
  },
};

const plugin = {
  name: 'Inline image role',
  roles: [imgRole],
};

export default plugin;
