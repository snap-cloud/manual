#!/usr/bin/env ruby
require 'fileutils'

# Split markdown file into individual files by h1 headers
split_dir = "chapters"
`mkdir -p #{split_dir}`

DOCX_MANUAL = "SnapManual.docx"
MD_OUTPUT = "SnapManual.md"

def pandoc
  `pandoc --from docx #{DOCX_MANUAL} --to commonmark --lua-filter index-extractor.lua -o #{MD_OUTPUT}`
end

def copy_files_to_content
  # this assumes this script is run from within ./tests/
  # Copy files to ../content, but skip 00, 01, and 02 chapters.
  Dir.glob('chapters/*').each do |file|
    next if File.basename(file) =~ /^(00|01|02)-/

    if File.directory?(file)
      FileUtils.cp_r(file, '../content/')
    else
      FileUtils.cp(file, '../content/')
    end
  end
end

def make_all_dirs
  `mkdir -p #{split_dir}/assets`
end

def chapter_file_name(heading, index)
  # Remove all other markdown formatting from the heading
  # Strip *, !, ![](.*), and {.*} from the heading
  heading = heading.gsub(/\*|!|\!\[.*?\]|\{.*?\}/, '')
  # Sanitize the heading to create a filename
  sanitized_heading = heading.downcase.gsub(/[^a-z0-9]+/, '-').gsub(/^-|-$/, '')
  sanitized_heading = sanitized_heading.split('-')[0..4].join('-')
  "#{split_dir}/#{format('%02d', index)}-#{sanitized_heading}.md"
end


def split_chapters
  # Read the markdown file
content = File.read(MD_OUTPUT)

# Split the content by h1 headers
chapters = content.split(/^# /)

images = {}

# Write each chapter to a separate file
chapters.each_with_index do |chapter, index|
  next if chapter.strip.empty?

  heading = chapter.lines.first.strip
  filename = chapter_file_name(heading, index)
  puts "Processing: #{index} - #{filename}"

  # Process the markdown content to clean things up.
  # Move the style attribute of an image tag to a comment after the image
  # {width="4.326388888888889in" height="2.689583333333333in"}
  chapter.gsub!(/(!\[.*?\]\(.*?\))\s*\{(.*?)\}/m) do
    "#{$1} <!-- #{$2.gsub(/\n/, ' ')} -->"
  end

  # Remove all the .smallcaps class from speific words/letters in markdown
  # e.g. [.*]{.smallcaps} -> .*
  chapter.gsub!(/\[(.*?)\]\{\.smallcaps\}/, '\1')

  # Replace \\index with \index
  chapter.gsub!(/\\index/, '\index')

  # Organize the image/media files
  # move images into a subdirectory organized by chapter, and rename them to `chp-xx-<original-name>`
  # but keep a map of the original names to the new names, in case they are referenced in a different chapter
  # then update the markdown to point to the new image locations
  chapter_images = chapter.scan(/\!\[.*?\]\(.*?\)/)
  chapter_images.each do |image|
    # extract the image name from the markdown
    image_name = image.match(/\!\[.*?\]\((.*?)\)/)[1]

    if images[image_name]
      chapter.gsub!(image_name, "assets/#{images[image_name]}")
      next
    end

    chapter_num = format('%02d', index)
    new_image_name = "chp-#{chapter_num}-#{File.basename(image_name)}"
    images[image_name] = new_image_name
    FileUtils.cp(image_name, "#{split_dir}/assets/#{new_image_name}")
    chapter.gsub!(image_name, "assets/#{new_image_name}")
  end

  File.write(filename, "# " + chapter)
end

def cleanup_chapter_md(source, image_index)

end

def full_conversion
  pandoc
  make_all_dirs
  split_chapters
  # Comment this out if you just want to rerun the script.
  copy_files_to_content
end

full_conversion
