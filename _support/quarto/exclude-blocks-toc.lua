-- exclude-blocks-toc.lua
-- Quarto Lua filter to adjust h1 headers in files under blocks/**

function Header(elem)
  -- if elem.level == 1 and FORMAT:match("latex") then
    local header_text = pandoc.utils.stringify(elem.content)

    -- Check if header has pdf-only-unlisted class
    for _, class in ipairs(elem.classes) do
      if class == "pdf-only-unlisted" and not FORMAT:match("latex") then
        io.stderr:write("Found pdf-only-unlisted class, removing from TOC: " .. header_text .. "\n")
        -- elem.attributes["-"] = ""

        -- Remove the original unlisted class so it doesn't appear in output
        local new_classes = {}
        for _, c in ipairs(elem.classes) do
          if c ~= "unlisted" then
            table.insert(new_classes, c)
          end
        end
        elem.classes = new_classes
        return elem
      end
    end
  -- end

  return elem
end
