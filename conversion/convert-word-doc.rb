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

def chapter_folder_name(heading, index)
  # Remove all other markdown formatting from the heading
  # Strip *, !, ![](.*), and {.*} from the heading
  heading = heading.gsub(/\*|!|\!\[.*?\]|\{.*?\}/, '')
  # Strip everything aftera a latex command
  heading = heading.gsub(/\\.*$/, '')
  # Sanitize the heading to create a filename
  sanitized_heading = heading.downcase.gsub(/[^a-z0-9]+/, '-').gsub(/^-|-$/, '')
  sanitized_heading = sanitized_heading.split('-')[0..4].join('-')
  chapter_directoory = "#{format('%02d', index)}-#{sanitized_heading}"
  "#{OUTPUT_DIR}/#{chapter_directoory}"
end

def chapter_file_name(heading, index)
  "#{chapter_folder_name(heading, index)}/index.md"
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

    output_dir = chapter_folder_name(heading, index)
    filename = chapter_file_name(heading, index)
    puts "Processing: #{index} - #{filename}"

    # Arguments: chapter_content, chapter_number, output_dir, image_index
    chapter = cleanup_chapter_md(chapter, index, output_dir, image_index)

    FileUtils.mkdir_p(output_dir)
    File.write(filename, "# " + chapter)
  end
end

# This cleans up gfm, commonmark, and pandoc markdown
def cleanup_chapter_md(chapter, number, output_dir, image_index)
  chapter_num = format('%02d', number)

  # Move the style attribute of an image tag to a comment after the image
  # {width="4.326388888888889in" height="2.689583333333333in"}
  chapter.gsub!(/(!\[.*?\]\(.*?\))\s*\{(.*?)\}/m) do
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
  image_output_dir = "#{output_dir}/assets"
  FileUtils.mkdir_p(image_output_dir)

  chapter_images.each do |image|
    # extract the image name from the markdown
    image_name = image[0]
    # This only applies to about ~40 images in the entire manual
    # if image_index[image_name]
    #   # We are referencing an image that is in a different chapter.
    #   # Therefore the path needs to be adjusted some to work using the `content/` directory.
    #   new_image_path = image_index[image_name].gsub(/#{OUTPUT_DIR}\//, '../content/')
    #   puts "Image already exists: #{image_name} -> #{new_image_path}"
    #   chapter.gsub!(image_name, new_image_path)
    #   next
    # end

    new_image_name = "#{image_output_dir}/#{File.basename(image_name)}"
    html_image_path = "assets/#{File.basename(image_name)}"
    # image_index[image_name] = new_image_name
    FileUtils.cp(image_name, new_image_name)
    chapter.gsub!(image_name, html_image_path)
  end

    # Move the style attribute of an HTML image tag to a comment after the image
    chapter.gsub!(/(<img.*?src=["'].*?["'].*?>)\s*\{(.*?)\}/m) do
      "#{$1} <!-- #{$2.gsub(/\n/, ' ')} -->"
    end

    # Convert HTML-style image tags to markdown-style image tags
    chapter.gsub!(/<img.*?src=["'](.*?)["'](.*?)>/m) do
      image_path = $1
      "![#{File.basename(image_path)}](#{image_path}) <!-- #{$2.gsub(/\n/, ' ')} --> "
    end

    # Tidy LaTex Index tags to remove space before punctuation
    chapter.gsub!(/(\\index\{.*?})\s+([,\.;])/, '\1\2')
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
