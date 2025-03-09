-- Track the current file being processed
local current_file = ""
local current_title = ""

-- This runs at the start of each document
function Meta(meta)
  -- Get current file and title
  if PANDOC_STATE and PANDOC_STATE.input_files and #PANDOC_STATE.input_files > 0 then
    current_file = PANDOC_STATE.input_files[1]:gsub("%.qmd$", ".html")
  end

  if meta.title then
    current_title = pandoc.utils.stringify(meta.title)
  end

  -- Create or clear the file if this is the first document that's not the index
  if not current_file:match("index%.html$") then
    local file_exists = io.open("_index_entries.txt", "r")
    if file_exists then
      file_exists:close()
    else
      local new_file = io.open("_index_entries.txt", "w")
      if new_file then
        new_file:close()
      end
    end
  end

  return meta
end

-- Process spans with index attributes
function Span(el)
  if el.attributes.index or (el.classes and el.classes:includes("index")) then
    -- Get the term
    local term = el.attributes.index
    if not term and el.identifier then
      -- Handle #index:term format
      if el.identifier:match("^index:") then
        term = el.identifier:gsub("^index:", "")
      else
        term = el.identifier
      end
    end

    if term then
      -- Append entry to the index file
      local file = io.open("_index_entries.txt", "a")
      if file then
        file:write(term .. "|" .. current_file .. "|" .. current_title .. "\n")
        file:close()
      end

      -- Return empty span to hide the markup
      return pandoc.Span("")
    end
  end
  return el
end

-- Process LaTeX-style \index{} commands in RawInline elements
function RawInline(el)
  if el.format == "tex" or el.format == "latex" then
    -- Look for \index{term} pattern
    local term = el.text:match("\\index%{(.-)%}")

    if term then
      -- Append entry to the index file
      local file = io.open("_index_entries.txt", "a")
      if file then
        file:write(term .. "|" .. current_file .. "|" .. current_title .. "\n")
        file:close()
      end

      -- For HTML output, remove the index markup
      if FORMAT:match("html") then
        return pandoc.Span("")
      end
    end
  end
  return el
end

-- Process inline code blocks that might contain \index commands
function Code(el)
  -- Look for \index{term} pattern in code blocks
  local term = el.text:match("\\index%{(.-)%}")

  if term then
    -- Append entry to the index file
    local file = io.open("_index_entries.txt", "a")
    if file then
      file:write(term .. "|" .. current_file .. "|" .. current_title .. "\n")
      file:close()
    end

    -- For HTML output, we need to decide whether to keep the code block
    -- If it's just an index command, remove it; if it contains other code, keep it
    if FORMAT:match("html") and el.text:match("^\\index%{.+%}$") then
      return pandoc.Span("")
    end
  end

  return el
end

-- Process raw LaTeX blocks
function RawBlock(el)
  if el.format == "tex" or el.format == "latex" then
    -- Look for all \index{term} patterns in the block
    for term in el.text:gmatch("\\index%{(.-)%}") do
      -- Append entry to the index file
      local file = io.open("_index_entries.txt", "a")
      if file then
        file:write(term .. "|" .. current_file .. "|" .. current_title .. "\n")
        file:close()
      end
    end
  end
  return el
end

-- Process inline LaTeX written directly in markdown (not in code blocks)
function Str(el)
  -- Look for \index{term} pattern in regular text
  local term = el.text:match("\\index%{(.-)%}")

  if term then
    -- Append entry to the index file
    local file = io.open("_index_entries.txt", "a")
    if file then
      file:write(term .. "|" .. current_file .. "|" .. current_title .. "\n")
      file:close()
    end

    -- We don't modify the text here, as this would break LaTeX rendering
  end

  return el
end
