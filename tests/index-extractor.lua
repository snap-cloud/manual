-- index-extractor.lua
-- Extract index entries from Word documents through pandoc

local logging = require('logging')
local index_entries = {}

-- Helper function to print the type and content of elements for debugging
function dump(elem)
    print("Element type: " .. elem.t)
    if elem.text then
        print("Text content: " .. elem.text)
    end
end

function list_contains(list, item)
    for _, v in pairs(list) do
        if v == item then
            return true
        end
    end
    return false
end

function Span(elem, _text)
    if (elem.attr and list_contains(elem.attr.classes, "indexref")) then
        return " \\" .. 'index{' .. elem.attributes['entry'] .. "}"
    else
        if (not list_contains(elem.attr.classes, "anchor") and
            not list_contains(elem.attr.classes, "mark")) then
            logging.output("UNKNOWN SPAN FOUND")
            logging.output(elem)
        end
        return nil
    end
end

-- function RawInline(elem)
--     -- Print raw elements we find
--     print("Found RawInline:")
--     dump(elem)

--     if elem.format == "openxml" then
--         -- Look for w:r elements containing w:instrText
--         local xe = elem.text:match('w:instrText[^>]*>%s*XE%s*"([^"]+)"')
--         if xe then
--             print("Found index entry: " .. xe)
--             table.insert(index_entries, xe)
--         end
--     end
-- end

-- function RawBlock(elem)
--     -- Print raw elements we find
--     print("Found RawBlock:")
--     dump(elem)

--     if elem.format == "openxml" then
--         -- Look for w:r elements containing w:instrText
--         for text in elem.text:gmatch('<w:r.-<w:instrText.-XE%s*"([^"]+)".-</w:instrText>') do
--             print("Found index entry: " .. text)
--             table.insert(index_entries, text)
--         end
--     end
-- end

-- -- Final processing
-- function Pandoc(doc)
--     print("Total index entries found: " .. #index_entries)

--     -- Remove duplicates while preserving order
--     local seen = {}
--     local unique_entries = {}

--     for _, entry in ipairs(index_entries) do
--         if not seen[entry] then
--             seen[entry] = true
--             table.insert(unique_entries, entry)
--         end
--     end

--     -- Sort alphabetically
--     table.sort(unique_entries)

--     -- Create output
--     local blocks = {}
--     table.insert(blocks, pandoc.Header(1, pandoc.Str("Index Entries")))

--     for _, entry in ipairs(unique_entries) do
--         table.insert(blocks, pandoc.Para(pandoc.Str(entry)))
--     end

--     return pandoc.Pandoc(blocks)
-- end
