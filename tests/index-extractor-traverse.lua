-- index-extractor-traverse.lua

function dump(o)
   if type(o) == 'table' then
      local s = '{ '
      for k,v in pairs(o) do
         if type(k) ~= 'number' then k = '"'..k..'"' end
         s = s .. '['..k..'] = ' .. dump(v) .. ','
      end
      return s .. '} '
   else
      return tostring(o)
   end
end

function traverse(elem)
    -- Print information about the current element
    print(string.format("Element type: %s", elem.t or "nil"))
    print(string.format("Element content: %s", dump(elem)))

    if elem.text then
        print(string.format("Text content: %s", elem.text))
    end

    -- If the element has content, traverse it
    if type(elem) == "table" then
        for k, v in pairs(elem) do
            if type(v) == "table" and v.t then  -- looks like a pandoc element
                traverse(v)
            elseif type(v) == "table" and #v > 0 then  -- array of elements
                for _, child in ipairs(v) do
                    if type(child) == "table" and child.t then
                        traverse(child)
                    end
                end
            end
        end
    end
end

-- Process every type of element
function Pandoc(doc)
    print("Starting document traversal...")
    traverse(doc)

    -- Return document unchanged
    return doc
end

-- Add handlers for specific element types we want to examine in detail
function Str(elem)
    print("String element: " .. elem.text)
    return elem
end

function RawInline(elem)
    print("RawInline element: " .. elem.format .. " - " .. elem.text)
    return elem
end

function RawBlock(elem)
    print("RawBlock element: " .. elem.format .. " - " .. elem.text)
    return elem
end

function Link(elem)
    print("Link element: " .. dump(elem))
    return elem
end

function Span(elem)
    print("Span element: " .. dump(elem))
    return elem
end

function Div(elem)
    print("Div element: " .. dump(elem))
    return elem
end
