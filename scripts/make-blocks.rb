require 'json'
require 'fileutils'

dest = 'blocks'
TEMPLATE = <<~TEMPLATE
---
readable_name: "{{ label }}"
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

# {{ label }} {.unnumbered}

{{< include ../_block.qmd >}}
TEMPLATE

def block_template(block)
  template = TEMPLATE.dup
  template.gsub!('{{ label }}', block['label'])
  template.gsub!('{{ selector }}', block['selector'])
  template.gsub!('{{ type }}', block['type'])
  template.gsub!('{{ category }}', block['category'])
  template.gsub!('{{ block_spec }}', block['block_spec'])

  template
end
blocks_json = JSON.parse(File.read('scripts/blocks.json'))

puts "Generating blocks... #{blocks_json.length} blocks"

blocks_json.each do |block|
  block_page = block_template(block)
  FileUtils.mkdir_p("#{dest}/#{block['category']}")
  File.open("#{dest}/#{block['category']}/#{block['selector']}.qmd", 'w') do |f|
    f.write(block_page)
  end
  puts "  - blocks/#{block['category']}/#{block['selector']}.qmd"
end
