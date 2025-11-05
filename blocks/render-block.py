"""
Render the help page for a given block.

This script expects `yaml_data` to be defined, which should contain the metadata for the block.
"""
from IPython.display import Markdown, display

# import yaml

def render_block_markdown(yaml_data):
    """Generate markdown content from block YAML data"""

    # TODO: this is because we want to possible support quarto-partials.
    yaml_data = yaml_data.get('partial-data', {})
    description = yaml_data.get('block_description', 'No description')
    label = yaml_data.get('label', 'Unknown block')
    selector = yaml_data.get('selector', 'unknown')
    help_screen = yaml_data.get('help_screen', 'default.png')

    # Start building markdown
    markdown_content = []

    # Description
    markdown_content.append(description)
    markdown_content.append("")

    # Block image
    markdown_content.append(f'![The "{label}" block](/blocks/images/block_{selector}.png)')
    markdown_content.append("")

    # Help screen image
    markdown_content.append(f'![help screen for the block "{label}"](../help/{help_screen})')
    markdown_content.append("")

    # Example Images section
    markdown_content.append("## Example Images")
    markdown_content.append("")

    example_images = yaml_data.get('example_images', [])
    if example_images:
        for img in example_images:
            description = img.get('description', 'Example')
            image_path = img.get('image', '')
            markdown_content.append(f'![{description}]({image_path})')
    else:
        markdown_content.append("No examples yet.")

    markdown_content.append("")

    # Example Projects section
    markdown_content.append("## Example Projects")
    markdown_content.append("")
    markdown_content.append("These example projects show the block in the context of a larger project. They will contain other blocks, too.")
    markdown_content.append("")

    example_projects = yaml_data.get('example_projects', [])
    if example_projects:
        for project in example_projects:
            title = project.get('title', 'Untitled Project')
            url = project.get('url', '#')
            markdown_content.append(f'* [{title}]({url})')
    else:
        markdown_content.append("No examples yet.")

    markdown_content.append("")

    # Footer
    markdown_content.append("---")
    markdown_content.append("")
    markdown_content.append("_Individual pages for each block are new. Most blocks don't yet additional links and images. If you have any questions, please post in the {.snap}`Snap` [forum](https://forum.snap.berkeley.edu/c/help/snap-help/49)._")

    return "\n".join(markdown_content)

markdown_output = render_block_markdown(yaml_data)
# print(markdown_output)
display(Markdown(markdown_output))
