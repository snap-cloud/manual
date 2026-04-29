function Span(elem)
  if elem.classes:includes('snap') and #elem.content == 1 then
    local str = elem.content[1]
    if str.t == 'Str' and str.text == 'Snap' then
      return pandoc.RawInline('latex', 'Snap\\textit{!}')
    end
  end
end

function Image(img)
  if img.classes:includes('image-2x') then
    for i, class in ipairs(img.classes) do
      if class == 'image-2x' then
        table.remove(img.classes, i)
        break
      end
    end
    img.attributes['width'] = '50%'
    return img
  end
end
