-- Stylize "Snap!" (and friends like "SciSnap!") consistently across formats.
--
-- Source convention (preferred): `[Snap!]{.snap}` (a Pandoc inline span).
-- Legacy convention (still supported): `` {.snap}`Snap` `` (an inline code span).
--
-- The filter normalizes any `Span` or `Code` element with the `.snap` class so
-- that the trailing "!" is rendered in italics, while the leading text (e.g.
-- "Snap", "SciSnap") is emitted as-is. The actual character "!" is kept in the
-- document text — not added via CSS `::after` — so that headings, the sidebar,
-- the TOC, the page `<title>`, and search all see "Snap!".

local function is_emph_bang(elem)
  if elem.t ~= 'Emph' then return false end
  if #elem.content ~= 1 then return false end
  local inner = elem.content[1]
  return inner.t == 'Str' and inner.text == '!'
end

local function strip_trailing_bang(inlines)
  local n = #inlines
  if n == 0 then return inlines end
  local last = inlines[n]
  -- Already in canonical form: ends with Emph("!"). Strip so we can re-add it.
  if is_emph_bang(last) then
    inlines:remove(n)
    return inlines
  end
  if last.t ~= 'Str' then return inlines end
  local text = last.text
  if text:sub(-1) ~= '!' then return inlines end
  if #text == 1 then
    inlines:remove(n)
  else
    inlines[n] = pandoc.Str(text:sub(1, -2))
  end
  return inlines
end

local function render_snap(inlines)
  inlines = strip_trailing_bang(inlines)
  if FORMAT:match('latex') then
    local prefix = pandoc.utils.stringify(inlines)
    return pandoc.RawInline('latex', prefix .. '\\textit{!}')
  end
  inlines:insert(pandoc.Emph(pandoc.Inlines({ pandoc.Str('!') })))
  return inlines
end

function Span(elem)
  if not elem.classes:includes('snap') then return nil end
  local rendered = render_snap(elem.content)
  if FORMAT:match('latex') then
    return rendered
  end
  elem.content = rendered
  return elem
end

function Code(elem)
  if not elem.classes:includes('snap') then return nil end
  local content = pandoc.Inlines({ pandoc.Str(elem.text) })
  local rendered = render_snap(content)
  if FORMAT:match('latex') then
    return rendered
  end
  return pandoc.Span(rendered, pandoc.Attr('', { 'snap' }))
end

function Image(img)
  -- The image-2x class is styled via CSS in HTML; only rewrite it for LaTeX.
  if not FORMAT:match('latex') then return nil end
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
