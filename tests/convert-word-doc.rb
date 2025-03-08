#!/usr/bin/env ruby

DOCX_MANUAL = "SnapManual.docx"
MD_OUTPUT = "SnapManual.md"

# Convert Word document to markdown
`pandoc --from docx #{DOCX_MANUAL} --to markdown --lua-filter index-extractor.lua -o #{MD_OUTPUT}`

# Split markdown file into individual files by h1 headers
split_dir = "chapters"
`mkdir -p #{split_dir}`
require 'fileutils'

# Read the markdown file
content = File.read(MD_OUTPUT)

# Split the content by h1 headers
chapters = content.split(/^# /)

# Write each chapter to a separate file
chapters.each_with_index do |chapter, index|
  next if chapter.strip.empty?

  heading = chapter.lines.first.strip

  # Process the markdown content to clean things up.
  # Move the style attribute of an image tag to a comment after the image
  # {width="4.326388888888889in" height="2.689583333333333in"}
  chapter.gsub!(/(!\[.*?\]\(.*?\))\s*\{(.*?)\}/m) do
    "#{$1} <!-- #{$2.gsub(/\n/, ' ')} -->"
  end

  # Replace the `media/` with 'assets/' in the image paths
  chapter.gsub!(/\(media\//, '(assets/')

  # Remove all the .smallcaps class from speific words/letters in markdown
  # e.g. [.*]{.smallcaps} -> .*
  chapter.gsub!(/\[(.*?)\]\{\.smallcaps\}/, '\1')

  # Sanitize the heading to create a filename
  sanitized_heading = heading.downcase.gsub(/[^a-z0-9]+/, '-').gsub(/^-|-$/, '')
  filename = "#{split_dir}/#{format('%02d', index)}-#{sanitized_heading}.md"
  File.write(filename, "# " + chapter)
end
