#!/usr/bin/env ruby
require 'fileutils'

# Split markdown file into individual files by h1 headers
OUTPUT_DIR = "chapters"
DOCX_MANUAL = "SnapManual.docx"
MD_OUTPUT = "SnapManual.md"

def pandoc
  `pandoc --from docx #{DOCX_MANUAL} --to commonmark --lua-filter index-extractor.lua -o #{MD_OUTPUT}`
end

def copy_files_to_content
  # this assumes this script is run from within ./conversion/
  Dir.glob('chapters/*').each do |file|
    if File.directory?(file)
      FileUtils.cp_r(file, '../content/')
    else
      FileUtils.cp(file, '../content/')
    end
  end
end

def make_all_dirs
  `mkdir -p #{OUTPUT_DIR}`
  `rm #{OUTPUT_DIR}/*.md`
  `mkdir -p #{OUTPUT_DIR}/assets`
end

def chapter_file_name(heading, index)
  # Remove all other markdown formatting from the heading
  # Strip *, !, ![](.*), and {.*} from the heading
  heading = heading.gsub(/\*|!|\!\[.*?\]|\{.*?\}/, '')
  # Strip everything aftera a latex command
  heading = heading.gsub(/\\.*$/, '')
  # Sanitize the heading to create a filename
  sanitized_heading = heading.downcase.gsub(/[^a-z0-9]+/, '-').gsub(/^-|-$/, '')
  sanitized_heading = sanitized_heading.split('-')[0..4].join('-')
  chapter_directoory = "#{format('%02d', index)}-#{sanitized_heading}"
  # Create the directory for the chapter
  `mkdir -p #{OUTPUT_DIR}/#{chapter_directoory}`
  "#{OUTPUT_DIR}/#{chapter_directoory}/index.md"
end


def split_chapters
  # Read the markdown file
  content = File.read(MD_OUTPUT)

  # Split the content by h1 headers
  chapters = content.split(/^# /)

  # Track image file names and where they were first used
  image_index = {}

  # Write each chapter to a separate file
  chapters.each_with_index do |chapter, index|
    # This is simply a hack because the first 3 "#" in the markdown conversion aren't usable content
    next if index < 3
    next if chapter.strip.empty?

    # Index - 3 so that chapter 0 is "acknowledgements"
    index -= 3
    heading = chapter.lines.first.strip
    filename = chapter_file_name(heading, index)
    puts "Processing: #{index} - #{filename}"

    chapter = cleanup_chapter_md(chapter, index, image_index)

    File.write(filename, "# " + chapter)
  end
end

# This cleans up gfm, commonmark, and pandoc markdown
def cleanup_chapter_md(chapter, number, image_index)
  chapter_num = format('%02d', number)

  # Move the style attribute of an image tag to a comment after the image
  # {width="4.326388888888889in" height="2.689583333333333in"}
  chapter.gsub!(/(!\[.*?\]\(.*?\))\s*\{(.*?)\}/m) do
    "#{$1} <!-- #{$2.gsub(/\n/, ' ')} -->"
  end
  # Move the style attribute of an HTML image tag to a comment after the image
  chapter.gsub!(/(<img.*?src=["'].*?["'].*?>)\s*\{(.*?)\}/m) do
    "#{$1} <!-- #{$2.gsub(/\n/, ' ')} -->"
  end

  # Remove all the .smallcaps class from speific words/letters in markdown
  # e.g. [.*]{.smallcaps} -> .*
  chapter.gsub!(/\[(.*?)\]\{\.smallcaps\}/, '\1')
  # Remove html formatted smallcaps
  chapter.gsub!(/<span class="smallcaps">(.*?)<\/span>/, '\1')

  # Replace \\index with \index
  chapter.gsub!(/\\index/, '\index')

  # Organize the image/media files
  # move images into a subdirectory organized by chapter, and rename them to `chp-xx-<original-name>`
  # but keep a map of the original names to the new names, in case they are referenced in a different chapter
  # then update the markdown to point to the new image locations
  # chapter_images = chapter.scan(/\!\[.*?\]\(.*?\)/)
  chapter_images = chapter.scan(/<img.*?src=["'](.*?)["'].*?>/m)
  chapter_images.each do |image|
    # extract the image name from the markdown
    image_name = image[0]

    if image_index[image_name]
      chapter.gsub!(image_name, "assets/#{image_index[image_name]}")
      next
    end

    new_image_name = "chp-#{chapter_num}-#{File.basename(image_name)}"
    image_index[image_name] = new_image_name
    FileUtils.cp(image_name, "#{OUTPUT_DIR}/assets/#{new_image_name}")
    chapter.gsub!(image_name, "assets/#{new_image_name}")
  end

  chapter
end

def full_conversion
  pandoc
  make_all_dirs
  split_chapters
  # Comment this out if you just want to rerun the script.
  copy_files_to_content
end

full_conversion
