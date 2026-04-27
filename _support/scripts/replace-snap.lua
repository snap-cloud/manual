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

  -- Apply pdf-width as width for LaTeX/PDF output only.
  -- This filter is only loaded for PDF builds (see _quarto.yml).
  local pdf_width = img.attributes['pdf-width']
  if pdf_width then
    img.attributes['pdf-width'] = nil
    img.attributes['width'] = pdf_width
    return img
  end
end
