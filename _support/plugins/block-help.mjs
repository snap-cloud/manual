import { readFileSync } from 'node:fs';
import yaml from 'js-yaml';

const blockHelp = {
  name: "block-help",
  arg: { type: String },
  run(data, vfile, ctx) {
    const yamlPath = vfile?.path?.replace(/\.md$/, '.yml');
    const partial = yaml.load(readFileSync(yamlPath, 'utf8')) ?? {};
    const {
      block_description = "No description",
      label = "Unknown block",
      selector = "unknown",
      help_screen = "default.png",
      example_images = [],
      example_projects = [],
    } = partial;
    const title = partial.title ?? label;

    const examples = example_images.length
      ? example_images.map(img => `![${img.description ?? "Example"}](${img.image})`).join("\n\n")
      : "No examples yet.";
    const projects = example_projects.length
      ? example_projects.map(p => `- [${p.title ?? "Untitled Project"}](${p.url ?? "#"})`).join("\n")
      : "No examples yet.";

    const md = `
${block_description}

![The "${title}" block](/blocks/images/block_${selector}.png)

![Help screen for the "${title}" block](../help/${help_screen})

## Example Images

${examples}

## Example Projects

${projects}
`;
    return ctx.parseMyst(md).children;
  },
};

export default { name: "Snap block help", directives: [blockHelp] };
