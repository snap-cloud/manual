-- index-extractor.lua
-- Extract index entries from Word documents through pandoc

local logging = require('logging')
local index_entries = {}

-- Handle both block and inline raw elements
function RawInline(elem)
    logging.output('RAW INLINE: ' .. elem.text)
    print('RAW INLINE: ' .. elem.text)
    if elem.format == "openxml" then
        print('\t OXML')
        -- Look for index entry markers in the Word XML
        local xe = elem.text:match('instrText[^>]*>%s*XE%s*"([^"]+)"')
        if xe then
            table.insert(index_entries, xe)
        end
    end
end

function RawBlock(elem)
    print('RAW: ' .. elem.text)
    if elem.format == "openxml" then
        print('\t OXML')
        -- Look for index entry markers in the Word XML
        for xe in elem.text:gmatch('instrText[^>]*>%s*XE%s*"([^"]+)"') do
            table.insert(index_entries, xe)
        end
    end
end

-- Final processing
function Pandoc(doc)
    -- Remove duplicates while preserving order
    local seen = {}
    local unique_entries = {}

    for _, entry in ipairs(index_entries) do
        print(entry)
        table.insert(unique_entries, entry)
        if not seen[entry] then
            seen[entry] = true
        end
    end

    -- Sort alphabetically
    table.sort(unique_entries)

    -- Create output
    local blocks = {}
    table.insert(blocks, pandoc.Header(1, pandoc.Str("Index Entries")))

    -- Add each entry as a paragraph
    for _, entry in ipairs(unique_entries) do
        table.insert(blocks, pandoc.Para(pandoc.Str(entry)))
    end

    return pandoc.Pandoc(blocks)
end
