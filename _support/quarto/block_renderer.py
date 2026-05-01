"""
Render the help page for a given block.

# print(dir(get_ipython()))

* In the PDF version we don't want to render "duplicate" figcaptions,
and the images shouldn't be too large.
* The website will be the fully accessible version.
"""

import yaml
import os
# from IPython.display import Markdown, display

def get_block_data(filename=None):
    """Extract partial-data from current Quarto file"""
    if not filename:
        filename = os.environ.get('QUARTO_DOCUMENT_FILE')
        filepath = os.environ.get('QUARTO_DOCUMENT_PATH')
        filename = os.path.join(filepath, filename)

    with open(filename, 'r') as f:
        content = f.read()

    # Find the first # line and extract the title.
    # This is specific to block files.
    title = None
    for line in content.splitlines():
        if line.startswith('# '):
            title = line[2:].strip()
            # remove everything after {
            title = title.split('{')[0].strip()
            # remove `'s
            title = title.replace('`', '').strip()
            break

    if content.startswith('---'):
        yaml_end = content.find('\n---', 4)
        if yaml_end != -1:
            yaml_str = content[4:yaml_end]
            full_yaml = yaml.safe_load(yaml_str)
            full_yaml['title'] = title
            return full_yaml
    return {}

def render_block_markdown(yaml_data):
    """Generate markdown content from block YAML data"""

    # TODO: this is because we want to possible support quarto-partials.
    yaml_data = yaml_data.get('partial-data', {})
    description = yaml_data.get('block_description', 'No description')
    label = yaml_data.get('label', 'Unknown block')
    selector = yaml_data.get('selector', 'unknown')
    help_screen = yaml_data.get('help_screen', 'default.png')

    block_title = yaml_data.get('title', label)

    example_images = yaml_data.get('example_images', [])
    example_images_md = []
    if example_images:
        for img in example_images:
            description = img.get('description', 'Example')
            image_path = img.get('image', '')
            example_images_md.append(f'![{description}]({image_path})')
    else:
        example_images_md.append("No examples yet.")

    example_projects = yaml_data.get('example_projects', [])
    example_projects_md = []
    if example_projects:
        example_projects_md.append("""
These example projects show the block in the context of a larger project. These projects will contain other blocks, too.

        """)
        for project in example_projects:
            proj_title = project.get('title', 'Untitled Project')
            url = project.get('url', '#')
            example_projects_md.append(f'* [{proj_title}]({url})')
    else:
        example_projects_md.append("No examples yet.")

    example_images_md = '\n'.join(example_images_md)
    example_projects_md = '\n'.join(example_projects_md)
    no_index = ''
    _html_visible = '{.content-visible when-format="html"}'
    _pdf_visible = '{.content-visible when-format="pdf"}'
    small_image = '{height=15pt}'
    max_width = '{width=85% max-height=50vh}'
    return f'''
{description}

::: {_html_visible}
![The "{block_title}" block](/blocks/images/block_{selector}.png)
:::

::: {_pdf_visible}
![](/blocks/images/block_{selector}.png){small_image}
:::

::: {_html_visible}
![help screen for the block "{block_title}"](../help/{help_screen})
:::

::: {_pdf_visible}
![](../help/{help_screen}){max_width}
:::

## Example Images{no_index}
{example_images_md}

## Example Projects{no_index}
{example_projects_md}
    '''

def render_block():
    """Main function to render block from current file"""
    yaml_data = get_block_data()
    markdown_output = render_block_markdown(yaml_data)
    print(markdown_output)

"""
THIS BREAKS RENDERING -- no idea why.

::: {_html_visible}
---
<em>Individual pages for each block are new. Most blocks don't yet additional links and images. If you have any questions, please post in the <a href="https://forum.snap.berkeley.edu/c/help/snap-help/49"><span class="snap">Snap</span> forum</a>.</em>
:::

::: {_pdf_visible}
:::
"""
