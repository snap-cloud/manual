#! /usr/bin/env ruby

INDEX_FILE = '_support/conversion/text-indext.txt'
CONTENT = '**/*.md'
ALL_CONTENT = Dir.glob(CONTENT).freeze

def parse_text_index_entries(file)
  entries = {}
  File.foreach(file) do |line|
    next if line.strip.empty?
    entry, pages = line.split('--', 2).map(&:strip)
    next unless entry && pages
    page_list = pages.split(',').map { |p| p.strip.to_i }
    entries[entry] = page_list
  end
  entries
end

def normalize_new_entry(entry)
  entry = entry.gsub(/[\s]+/, ' ') # Normalize whitespace
  entry = entry.strip.gsub(/['"`]/, '').gsub(/\n/, ' ')
  # Unescape LaTeX special characters
  entry = entry.gsub(/\\([#$%&*_{}])/,'\1')
  # puts "|" + entry + "|"
  entry
end

def extract_all_entries_from_content(md_files)
  entries = Hash.new { |h, k| h[k] = [] }
  md_files.each do |file|
    content = File.read(file)
    # This regex will match \index{...} even if ... contains newlines
    content.scan(/\\index\{((?:[^\}]|\n)+)\}/m).each do |match|
      entry = normalize_new_entry(match.first)
      normalized_name = file.sub(%r{\Acontent/}, '').sub(/\/index\.md\z/, '')
      entries[entry] << normalized_name
    end
  end
  entries
end

def compare_entries(original, new, aggressive_name_correction: false)
  if aggressive_name_correction
    original = original.transform_keys { |k| k.downcase.gsub(/[^a-z0-9\s]/i, '') }
    new = new.transform_keys { |k| k.downcase.gsub(/[^a-z0-9\s]/i, '') }
  end

  original_keys = original.keys.sort
  new_keys = new.keys.sort

  puts "Original index: #{original_keys.size} unique keys, #{original.values.flatten.size} total entries"
  puts "New index: #{new_keys.size} unique keys, #{new.values.flatten.size} total entries"
  puts

  missing_in_new = original_keys - new_keys
  puts "#{missing_in_new.size} Keys in original not found in new index:"
  puts missing_in_new.any? ? missing_in_new.map { |k| "|#{k}| -> (#{original[k].join(", ")})" }.join("\n") : "(none)"
  puts

  # Group missing keys by their original pages
  missing_in_new_grouped = missing_in_new.group_by { |k| original[k].first }
  missing_in_new_grouped = missing_in_new_grouped.sort.to_h
  puts "Page | Missing Terms"
  puts "-----|----------------"
  missing_in_new_grouped.each do |page, terms|
    puts "#{page.to_s.rjust(5)} | #{terms.join(", ")}"
  end

  puts "Keys with >1 entries in original and different count in new:"
  original.each do |key, orig_pages|
    if orig_pages.size > 1 && new[key] && new[key].size != orig_pages.size
      puts "#{key}: original=#{orig_pages.size}, new=#{new[key].size}"
      puts "  Pages in original: #{orig_pages.join(", ")}"
      puts "  Pages in new: #{new[key].join(", ")}"
    end
  end
end

orginal_entries = parse_text_index_entries(INDEX_FILE)
new_entries = extract_all_entries_from_content(ALL_CONTENT)

compare_entries(orginal_entries, new_entries)
puts "Comparison complete."
puts
puts "--" * 20
puts
