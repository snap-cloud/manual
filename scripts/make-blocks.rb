require 'json'
require 'fileutils'

dest = 'blocks'
TEMPLATE = <<~TEMPLATE
---
block_description: Complete Me
label: "{{ label }}"
block_spec: "{{ block_spec }}"
help_screen: "{{ selector }}.png"
selector: "{{ selector }}"
type: {{ type }}
category: {{ category }}
arguments:
  - name: distance
    type: number
    default: 10
    description: The distance to move forward
returns: None
exmaple_projects:
  - title: Example Project 1
    url: https://example.com/project1
  - title: Example Project 1
    url: https://example.com/project1
example_images:
  - image: move_forward.png
    description: Move forward by 10 steps
  - image: move_forward.png
    description: Move forward by 10 steps
---

# {{ title }} {.unnumbered}

{{< include ../_block.qmd >}}
TEMPLATE

SYMBOL_MAP = {
  "$greenflag": "<img src=\"/images/greenflag.png\" alt=\"Green Flag\" class=\"icon\" />",
  "$clockwise": "↻",
  "$counterclockwise": "↺",
  "$arrowRight": "→",
  "$pause": "⏸",
}

def title(label)
  # Remove ":" from the label which seems to cause issues with YAML
  label.gsub(':', '').gsub('_', '').capitalize
  # Replace $symbols with their HTML equivalents
  SYMBOL_MAP.each do |symbol, html|
    label.gsub!(symbol.to_s, html)
  end
  label
end

def block_template(block)
  template = TEMPLATE.dup
  template.gsub!('{{ label }}', block['label'])
  template.gsub!('{{ title }}', title(block['label']))
  template.gsub!('{{ selector }}', block['selector'])
  template.gsub!('{{ type }}', block['type'])
  template.gsub!('{{ category }}', block['category'])
  template.gsub!('{{ block_spec }}', block['block_spec'])

  template
end

# This file is exported from this Snap! project:
# https://snap.berkeley.edu/versions/dev/snap.html#present:Username=cycomachead&ProjectName=markdown%20blocks%20table
blocks_json = JSON.parse(File.read('scripts/blocks.json'))

puts "Generating blocks... #{blocks_json.length} blocks"

all_custom_labels = []

blocks_json.each do |block|
  block_page = block_template(block)
  # All $words in the label
  block['label'].scan(/\$[a-zA-Z0-9_]+/).each do |custom_label|
    all_custom_labels << custom_label
  end
  FileUtils.mkdir_p("#{dest}/#{block['category']}")
  # TODO: Figure out how to merge existing files
  # File.open("#{dest}/#{block['category']}/#{block['selector']}.qmd", 'a') do |f|
  #   f.write(block_page)
  # end
  File.open("#{dest}/#{block['category']}/#{block['selector']}.qmd", 'w') do |f|
    f.write(block_page)
  end
  puts "  - blocks/#{block['category']}/#{block['selector']}.qmd"
end

all_custom_labels.uniq!
puts "Found #{all_custom_labels.length} custom labels"
puts "Custom labels:\n#{all_custom_labels.join("\n")}"
