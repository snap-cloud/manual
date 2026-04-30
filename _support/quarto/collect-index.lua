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
      -- TODO: Return an a name to link to the index entry
      return pandoc.Span("")
    end
  end
  return el
end

----

-- improved formatting for dumping tables and quarto's emulated pandoc nodes
function tdump (tbl, raw)

  local shouldPrint = function(k, _, innerTbl)
    -- when raw, print everything
    if raw then
      return true
    end
    if type(k) == "number" then
      return true
    end
    if string.sub(k, 1, 1) == "-" then
      return false
    end
    return true
  end

  local refs = {}
  local resultTable = {}

  -- https://www.lua.org/pil/19.3.html
  local pairsByKeys = function (t, f)
    local a = {}
    for n in pairs(t) do table.insert(a, n) end
    table.sort(a, f)
    local i = 0      -- iterator variable
    local iter = function ()   -- iterator function
      i = i + 1
      if a[i] == nil then return nil
      else return a[i], t[a[i]]
      end
    end
    return iter
  end

  local printInner = function(str)
    table.insert(resultTable, str)
  end

  local empty = function(tbl)
    for k, v in pairs(tbl) do
      return false
    end
    return true
  end

  -- sigh.
  -- https://stackoverflow.com/questions/48209461/global-and-local-recursive-functions-in-lua
  local inner
  inner = function(tbl, indent, doNotIndentType)
    local address = string.format("%p", tbl)
    local indentStr = string.rep(" ", indent)
    local closeBracket = indentStr .. "}\n"
    if refs[address] ~= nil then
      printInner(indentStr .. "(circular reference to " .. address .. ")\n")
      return
    end

    local isArray = tisarray(tbl)
    local isEmpty = empty(tbl)

    if type(tbl) == "table" or type(tbl) == "userdata" and tbl.is_emulated then
      local typeIndent = indentStr
      if doNotIndentType then
        typeIndent = ""
      end
      local endOfOpen = "\n"
      if isEmpty then
        endOfOpen = " <empty> }\n"
      end

      if tbl.is_emulated then
        printInner(typeIndent .. string.format("{ [quarto-emulated-ast:%s:%s]%s", tbl.t, address, endOfOpen))
      elseif tisarray(tbl) then
        printInner(typeIndent .. string.format("{ [array:%s]%s", address, endOfOpen))
      else
        printInner(typeIndent .. string.format("{ [table:%s]%s", address, endOfOpen))
      end
      if raw then
        printInner(indentStr .. " [metatable: " .. tostring(getmetatable(tbl)) .. "]\n")
      end
      if tbl.attr then
        printInner(indentStr .. "  attr: " .. tostring(tbl.attr) .. "\n")
      end
    end
    local empty = true
    local typesThenValues = function(a, b)
      local ta = type(a)
      local tb = type(b)
      if ta < tb then return true end
      if ta > tb then return false end
      return a < b
    end
    for k, v in pairsByKeys(tbl, typesThenValues) do
      if shouldPrint(k, v, tbl) then
        empty = false
        local formatting = indentStr .. "  " .. k .. ": "
        v = asLua(v)
        if type(v) == "table" or type(v) == "userdata" and v.is_emulated then
          printInner(formatting)
          refs[address] = true
          local indentBump = 2
          if string.len(k) < 3 then -- this does work when k is number
            indentBump = string.len(k) + 1
          end
          inner(v, indent+indentBump, true)
        elseif type(v) == 'boolean' then
          printInner(formatting .. tostring(v) .. "\n")
        elseif (v ~= nil) then
          printInner(formatting .. tostring(v) .. "\n")
        else
          printInner(formatting .. 'nil\n')
        end
      end
    end
    printInner(closeBracket)
  end

  inner(tbl, 0)
  print(table.concat(resultTable, ""))
end

function asLua(o)
  if type(o) ~= 'userdata' then
    return o
  end

  if rawequal(o, PANDOC_READER_OPTIONS) then
    return {
      abbreviations = o.abbreviations,
      columns = o.columns,
      default_image_extension = o.default_image_extension,
      extensions = o.extensions,
      indented_code_classes = o.indented_code_classes,
      standalone = o.standalone,
      strip_comments = o.strip_comments,
      tab_stop = o.tab_stop,
      track_changes = o.track_changes,
    }
  elseif rawequal(o, PANDOC_WRITER_OPTIONS) then
    return {
      cite_method = o.cite_method,
      columns = o.columns,
      dpi = o.dpi,
      email_obfuscation = o.email_obfuscation,
      epub_chapter_level = o.epub_chapter_level,
      epub_fonts = o.epub_fonts,
      epub_metadata = o.epub_metadata,
      epub_subdirectory = o.epub_subdirectory,
      extensions = o.extensions,
      highlight_style = o.highlight_style,
      html_math_method = o.html_math_method,
      html_q_tags = o.html_q_tags,
      identifier_prefix = o.identifier_prefix,
      incremental = o.incremental,
      listings = o.listings,
      number_offset = o.number_offset,
      number_sections = o.number_sections,
      prefer_ascii = o.prefer_ascii,
      reference_doc = o.reference_doc,
      reference_links = o.reference_links,
      reference_location = o.reference_location,
      section_divs = o.section_divs,
      setext_headers = o.setext_headers,
      slide_level = o.slide_level,
      tab_stop = o.tab_stop,
      table_of_contents = o.table_of_contents,
      template = o.template,
      toc_depth = o.toc_depth,
      top_level_division = o.top_level_division,
      variables = o.variables,
      wrap_text = o.wrap_text
    }
  end
  v = tostring(o)
  if string.find(v, "^pandoc CommonState") then
    return {
      input_files = o.input_files,
      output_file = o.output_file,
      log = o.log,
      request_headers = o.request_headers,
      resource_path = o.resource_path,
      source_url = o.source_url,
      user_data_dir = o.user_data_dir,
      trace = o.trace,
      verbosity = o.verbosity
    }
  elseif string.find(v, "^pandoc LogMessage") then
    return v
  end
  return o
end

-- dump an object to stdout
function dump(o, raw)

  o = asLua(o)
  if type(o) == 'table' or type(o) == 'userdata' and o.is_emulated then
    tdump(o, raw)
  else
    print(tostring(o) .. "\n")
  end
end

----


-- Process LaTeX-style \index{} commands in RawInline elements
-- TODO: how do we remove the space before the element.
function RawInline(el)
  if el.format == "tex" or el.format == "latex" then
    -- print('TEX DEUBG:   |' .. el.text .. '|')
    -- dump(el.content)
    -- Look for \s*\index{term} pattern
    local term = el.text:match("%s-\\index%{(.-)%}")

    if term then
      -- Append entry to the index file
      local file = io.open("_index_entries.txt", "a")
      if file then
        file:write(term .. "|" .. current_file .. "|" .. current_title .. "\n")
        file:close()
      end

      -- For HTML output, remove the index markup
      -- TODO: Return an anchor link to the index entry
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
  -- print('DEBUG STR el: |' .. el.text .. '|')
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
