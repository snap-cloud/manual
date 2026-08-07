# Manual Content Audit — vs. Snap! 12.0.6 (August 2026)

This audit compares the current manual content (a conversion of the Snap! 8.0 PDF,
August 2022) against the Snap! source and `HISTORY.md` at
[jmoenig/snap](https://github.com/jmoenig/snap) **v12.0.6 (2026-06-08)**.
Every finding below was verified against the Snap! source tree (file references are
to the Snap! repo unless prefixed with a manual chapter filename).

Scope: common features that typical users and teachers encounter. Obscure
extensions and cosmetic UI-styling drift in screenshots are excluded, except where
a screenshot depicts blocks/menus that no longer exist.

## Release timeline (git tag dates)

| Version | Released | Headlines relevant to the manual |
|---|---|---|
| 8.0.0 | 2022-08-04 | Manual baseline |
| 8.1.0 | 2023-02-01 | Lists as dictionaries; `pipe` becomes a Control primitive |
| 8.2.0 | 2023-03-01 | `and`/`or` and comparisons become variadic; `distribution` selector |
| 9.0.0 | 2023-07-18 | Variadic `if`/else-if; `this` reporter; call/cc & run/cc removed from palette; `uniques`/`sorted`/`shuffled`; case-sensitivity setting; static slots & separators; generate puzzle |
| 9.1.0 | 2023-12-05 | `min`/`max`/`atan2` in Operators palette; stage `say`/`write`; `text` list selector |
| 9.2.0 | 2024-01-11 | Hyperized `item of`; NumPy-style dimension matching; kernel convolutions |
| 10.0.0 | 2024-07-24 | "Blocks all the way" (editable primitives); color slots; palette rearranging; LISP syntax; metaprogramming expansion; performer mode; libraries search |
| 10.1.0 | 2024-10-11 | OOP 2.0 data objects; bright/dark themes + flat design toggle; input groups; Continuations library |
| 10.2.0 | 2024-11-08 | Scriptable dropdowns; Sprite Method API library; block-instance variables |
| 10.3.0 | 2024-12-05 | Custom hat blocks; generic `when` hat gets *event* semantics by default |
| 10.4.0 | 2025-01-22 | "Quicksteps" scheduling (warp/turbo largely obsolete); float `pick random` |
| 10.5.0 | 2025-02-28 | Mobile Device Sensors library |
| 10.6.0 | 2025-03-14 | Speech recognition in TTS library |
| 11.0.0 | 2025-08-29 | **First-class colors**; `request` reporter; Neural Networks library; Object slot → Color slot |
| 12.0.0 | 2026-05-29 | Magnification/zoom; templates & tutorials; settings menu → submenus; unringed blocks as data; custom data types & type enforcement; super-calls; custom category rename/recolor |

---

# Part A — Verifiably wrong or out of date

Ordered by priority.

## HIGH

### A1. Chapter 10 teaches removed blocks as "primitives" (whole chapter framing)
`10-continuations.md:188-255` — "Snap! provides a **primitive** mechanism for
capturing continuations" (`call w/continuation`, `run w/continuation`), and
`10-continuations.md:269-346` present `catch`/`throw` the same way.
`doCallCC`/`reportCallCC` were **removed from the palette in 9.0.0 (2023-07-18)**
(HISTORY.md: "RUN/CC and CALL/CC primitives have been deprecated and removed from
the palette"); in v12.0.6 they are `dev: true`, dev-mode-only (`src/objects.js`
~L1339-1352, palette push inside `if (devMode)` ~L4043). The user-facing
replacements are the **Continuations library** (`libraries/continuations_module.xml`,
added 10.1.0, 2024-10-11) and the iteration/composition library (`catch`/`throw`),
whose blocks are spelled "…**with** continuation", not "w/continuation".
A reader following the chapter will not find any of these blocks in the palette.
The modern palette-native mechanism, `this (continuation)` (9.0.0), is never
mentioned (see B9).

### A2. Chapter 7 names the wrong block for reporter messages
`07-object-oriented-programming-with-sprites.md:178` — "…or the `say ( )` block
(for reporter messages)." The block is **`ask ( ) for ( )`** (`src/objects.js:1371-1381`,
spec `ask %spr for %repRing %inputs`); `say` is the speech-balloon Looks block.
Lines 193-208 also repeatedly call it "`ask ( ) and wait`", which is actually the
unrelated Sensing block that prompts the user. This misleads on the chapter's
central mechanism. (Likely a conversion error rather than a Snap! change, which
makes it worth fixing first.)

### A3. Chapter 12's Settings-menu section describes a menu that no longer exists
`12-user-interface-elements.md:428-663` documents a flat checkbox list (three
groups), with screenshot `image1009.png`. Since **12.0.0 (2026-05-29)** the menu
opens with five submenus — `Language…`, `Looks…`, `Editor…`, `Project…`,
`Accessibility…` — followed by "Temporary Settings" (`src/gui.js` `settingsMenu`
~L4629-4807). Items moved: Zoom/Fade blocks → Looks; Stage size, Flat line ends,
Thread safe scripts, Codification, Single palette, HSL pen color, Log pen vectors →
Project; Long form input dialog, Plain prototype labels, Clicking sound → Editor.
Only Turbo, Performer mode, JS extensions, Extension blocks, Input sliders,
Visible stepping, Case sensitivity, Microphone remain top-level. This is the
manual's primary reference for every preference; none can currently be found where
it says.

### A4. Chapter 5's input-type dialog is wrong: `Object` slot is gone, `Color` exists, grid rearranged
`05-typed-inputs.md:18-19,27-29,50-71,106-113` (+ images `image659/660.png`) —
"The first row contains … Object, Text, and List… The second row … Number, Any,
Boolean". Current dialog (`src/byob.js` `createSlotTypeButtons` ~L4871-4882,
layout `fixSlotsLayout` ~L5137-5174): Row 1 **Any, Number, List**; Row 2 **Color,
Text, Boolean**; Rows 3-4 procedures. `Object` was **replaced by `Color`** in
**11.0.0 (2025-08-29)** (HISTORY.md: "replaced 'Object' type input slot with
'Color'… 'Object' is now in the 'special slots' menu"), and `Any` was moved to
top-left in **12.0.0**. The chapter's row/column rationale and the Object-type
walkthrough (`05:190-196`) no longer match the UI.

### A5. Chapter 3: "There are three block shapes" — there are four
`03-building-a-block.md:49-55` (and dialog image `image501.png`). The Make-a-block
dialog has a fourth shape, **Event Hat** (`src/byob.js` `createTypeButtons`
~L3140-3180), since custom hat blocks in **10.3.0 (2024-12-05)**. Similarly
`11-metaprogramming.md:108` "The type is command, reporter, or predicate" — the
metaprogramming type attribute now includes `hat` (`src/threads.js` ~L8630, L9164).

### A6. Chapter 1: `min`, `max`, `atan2` described as hidden relabel-only blocks
`01-blocks-scripts-and-sprites.md:1034-1039` — "These *hidden* blocks can be found
with the relabel option…". They have been **visible Operators-palette primitives
since 9.1.0 (2023-12-05)** (`src/objects.js` palette push ~L4116-4122; HISTORY.md
"added 'min', 'max' and 'atan2' reporters to the OPERATORS palette"). The adjacent
claim that ≤ ≥ ≠ are relabel-only is still correct.

### A7. Colors are now a built-in first-class data type, not a library feature
- `appendix/a-snap-color-library.md:12-16` — "The Colors and Crayons library …
  also establishes colors as a first class data type."
- `01-blocks-scripts-and-sprites.md:1667-1671` — the library "is intended as a
  more powerful replacement for the primitive `set pen` block, including first
  class color support."

Since **11.0.0 (2025-08-29)** `color` is an immutable primitive type with Pen
palette primitives: `color ( )` (`reportColor`, `src/objects.js:1102`),
`( ) of color ( )` (L1109), `new color hue…` (L1117), first-class-color pen setters
(L965-986), `color` in `is a ?` (L16739), color readouts in watchers/balloons.
Additionally, the library named **"Colors"** today (`libraries/colors_module.xml`)
is a new, simplified 4-block library (mix / darker-lighter / shift / transition);
the appendix documents the legacy library now called **"Colors and Crayons"**
(still shipped as `libraries/colors.xml`). Appendix A needs reframing around the
primitive color type and the new library.

### A8. Chapter 1: generic `when ⬡` hat described with obsolete default semantics
`01-blocks-scripts-and-sprites.md:87` (footnote) describes continuous
condition-polling semantics. Since **10.3.0 (2024-12-05)** the palette block is
`receiveConditionEvent` with **event semantics** (fires on state change); the old
"condition" behavior is a relabel variant marked with an infinity symbol
(`src/objects.js:1149-1158`, ~L3984, relabel pairing ~L3119; HISTORY.md 10.3.0).

## MEDIUM

### A9. Chapter 4: `length of`-family dropdown list is materially incomplete
`04-first-class-lists.md:636-680` enumerates length, rank, dimensions, flatten,
columns, reverse, lines, csv, json. The current menu (`src/blocks.js:504-527`)
also has **uniques, distribution, sorted, shuffled, text** (8.2.0 → 9.1.0;
implementations `src/threads.js:2518-2636`). The section reads as an exhaustive
list, so the five omissions look like nonexistence.

### A10. Chapter 1: `pipe` presented as library-only
`01-blocks-scripts-and-sprites.md:1468-1472`. `pipe` has been a **Control-palette
primitive since 8.1.0 (2023-02-01)** (`src/objects.js:1492-1504`, palette ~L4012).

### A11. Chapter 1: variadic-reporters library rationale is stale
`01-blocks-scripts-and-sprites.md:1651-1659` — the library is said to exist because
primitive `and`/`or` "take exactly two inputs". `and`/`or` and all comparison
operators have been **variadic (and hyper) since 8.2.0 (2023-03-01)**
(`src/objects.js:1835-1889`; the variadic-reporters library itself was removed in
8.2).

### A12. Chapter 11: `definition of` restriction and set-shorthand semantics
`11-metaprogramming.md:21-22` — "takes a custom block … as input"; since
**10.0.0 (2024-07-24)** it also reports primitive definitions ("blocks all the
way", `src/threads.js:8584-8603`). `11:110-113` — the non-list shorthand for
`set (slots/defaults/menus) of` now applies the value to **all** slots, not only
single-input blocks (10.0.0; `src/threads.js:9332-9374`).

### A13. Chapter 9: `url` block protocol-fallback claim
`09-the-outside-world.md:62-64` — "tries HTTPS and then, if that fails, HTTP."
`Process.reportURL` (`src/threads.js:4687-4700`) prepends the **page's own
protocol** (https on snap.berkeley.edu) and never falls back to http. (Behavior
dates to the v4.1 http→url rename; wrong since before the 8.0 baseline.)

### A14. Chapter 9: hardware-device story is stale
`09-the-outside-world.md:90-113` — presents a local-HTTP-server helper program as
the only mechanism, listing NXT/Wiimote/Leap-era drivers. Snap! now ships
Web-Serial/Web-Bluetooth based libraries: MicroBlocks + BLE (10.0.0),
**S4A Connector** for Firmata/Arduino and **websockets** (both 11.0.0, 2025-08-29)
(`libraries/microblocks.xml`, `s4aConn.xml`, `websockets.xml`).

### A15. Chapter 7: `my ( )` attribute list is incomplete
`07-object-oriented-programming-with-sprites.md:442-477` — missing `scripts`,
`solutions` (9.0.0), `costume` (singular), `rotation style`
(`src/blocks.js` `gettablesMenu` ~L12117-12158).

### A16. Chapter 12: palette context menu for custom blocks
`12-user-interface-elements.md:794-827` — omits `space above`, `move up`,
`move down` (palette rearranging/grouping, **10.0.0**; `src/byob.js:2007-2066`).

### A17. Chapter 1: `( ) at ( )` aspect menu
`01-blocks-scripts-and-sprites.md:967-974` — "first five items… ('RGBA' reports a
list)". Menu is now color, hue, saturation, brightness, transparency, **r-g-b-a**,
sprites — six color entries, first one reporting a first-class color (11.0.0;
`src/blocks.js:785-798`).

### A18. Appendix B: hyperblock dimension-matching rule predates 9.2.0
`appendix/b-apl-features.md:69-79` — since **9.2.0 (2024-01-11)** dyadic
hyperblocks zip dimensions **backwards, NumPy-style** (HISTORY.md 9.2.0), and
`item of` is itself hyperized with automatic zero-padding.

### A19. Chapter 3: prototype-hat context menu & category model
`03-building-a-block.md:133-154` — menu now also offers `selector…`, `condition`,
`return data type…`, `enforce types`, `export…` (`src/byob.js:1835-1927`;
10.0.0/10.3.0/12.0.0). `03:41-47` — custom categories can be created and, since
**12.0.0**, renamed/recolored, so "one color per palette + Other" is no longer the
whole model.

## LOW

- `05-typed-inputs.md:75-84` (footnote 5): wide "landscape" text slots were removed
  in **12.0.0** (`src/blocks.js:337-339`, HISTORY.md "removed landscape orientation
  of text-input slots").
- `04-first-class-lists.md:585-589`: `reshape` first input is Any-type since 9.0.0,
  and with no dimensions it reports a **scalar**, not an empty list
  (`src/lists.js:842-843`).
- `01-blocks-scripts-and-sprites.md:1203-1204`: `length of text` is now
  `(length ▾) of text` with lower/upper-case options (9.0.0;
  `src/objects.js:1941-1947`).
- `01-blocks-scripts-and-sprites.md:950` (image): "this script" is now the general
  `this ( )` reporter (9.0.0).
- `10-continuations.md:188`: label spelling "w/continuation" vs. the actual
  "with continuation" library blocks.
- `11-metaprogramming.md:133-136`: "maybe someday we'll have translations…
  for custom category names" — custom categories are renameable (12.0.0) and a
  `translations` attribute selector exists (8.1.0).

---

# Part B — Missing from the manual

Ordered by priority (how often a typical user/teacher hits it).

## HIGH

1. **Variadic `if` / else-if** (9.0.0, 2023-07-18). Core control flow; Chapter 1's
   conditionals section still shows only fixed `if`/`if else`.
2. **First-class colors** (11.0.0, 2025-08-29). The `color ( )`, `new color hue…`,
   `( ) of color ( )` primitives, color slots, `color` in `is a ?`, pen color
   attribute, and the new 4-block "Colors" library. Touches Chapters 1, 5, and
   Appendix A. (`src/objects.js:1102-1120`)
3. **Lists as dictionaries** (8.1.0, 2023-02-01). `item [key] of` for JSON fields /
   CSV columns (`src/lists.js:335-374`, `src/threads.js:2478`). The lists chapter
   never mentions it — the highest-priority gap in Chapter 4.
4. **OOP 2.0 data objects** (10.1.0, 2024-10-11). List-dictionary objects with
   prototypical inheritance via a `…` parent entry, `this (object)`, the OOP
   library, plus **super-calls** via a ring index in `item of` (12.0.0)
   (`src/threads.js:2463-2484`; `libraries/OOP_module.xml`). Chapter 8 hand-builds
   exactly this system with no pointer to the built-in one.
5. **"Blocks all the way" / editable primitives** (10.0.0, 2024-07-24). Right-click
   any primitive → `edit…` opens its Snap!-language definition; `Restore
   primitives` in the project menu (10.1.0). Chapter 3 and Chapter 12 predate the
   whole model. (Footnote in `04:130` already alludes to it — the only mention in
   the manual.)
6. **New list selectors**: `uniques`, `distribution`, `sorted`, `shuffled`, `text`
   (8.2.0–9.1.0) — see A9. Also index-slot dropdowns `last / random / all / parent`
   on `item`/`delete`/`insert` (`src/blocks.js:471-492`).
7. **Custom hat blocks + Events library** (10.3.0, 2024-12-05), including
   event-vs-condition semantics — relevant to Chapters 1, 3, 11.
8. **Settings & UI features** (Chapter 12): Magnification dialog & zoom gestures
   (12.0.0); bright/dark themes + flat design (10.1.0); performer mode (10.0.0);
   case sensitivity (9.0.0); "blocks only" and "hide empty categories" (12.0.0);
   green flag turning **red on script error** (12.0.0); tab icons and corral "+"
   buttons (12.0.0); libraries-browser search (10.0.0); `Export pen trails`
   (svg/embroidery, 10.0.0), `Generate puzzle` (9.0.0), templates & tutorials
   (12.0.0) in the project menu.
9. **`this ( )` introspection reporter** (9.0.0; `inputs` 9.2.0, `object` 10.1.0)
   — Chapters 6, 9, 10; `this (continuation)` is the modern basis of Chapter 10,
   and the chapter must say the catch/throw & call/cc blocks now come from the
   **Continuations** / iteration-composition libraries.
10. **Libraries appendix is an empty stub** (`appendix/libraries/index.md` says
    "Coming soon!") while v12.0.6 ships ~60 user-facing libraries. New since the
    baseline include: Neural Networks (11.0), Continuations (10.1), OOP (10.1),
    Sprite Method API (10.2), Events (10.3), Tiles & Arcs (9.0), Metaprogramming &
    Code-to-Blocks & Writing-and-formatting & Embroidery & MicroBlocks/BLE (10.0),
    Mobile Device Sensors (10.5), speech recognition in TTS (10.6), S4A Connector &
    WebSockets (11.0), Tables, Shapes, Draw Paths, Tutorials, Edge AI vision (12.0).
    Removed/absorbed: variadic reporters (8.2), multibranched conditional (9.0),
    "remove duplicates" from list utilities (9.0), old Streams → Streams 2.0 (10.0).

## MEDIUM

11. **`request ( )` reporter** (11.0.0) — broadcast-and-wait that collects replies
    (`src/objects.js:1178-1184`); Chapters 1 and 7 messaging sections.
12. **Custom-block slot machinery** (Chapter 5): variadic-slot options
    (`separator…`, `defaults…`, `initial/min/max slots`, `collapse/expand`,
    `group…` — 9.0.0/10.1.0; `src/byob.js:5268-5320`); static/irreplaceable slots
    (9.0.0); scriptable dropdown menus & slot-edit hat blocks (10.2.0);
    `parameter` slot type and variadic upvars (12.0.0); type enforcement
    (`return data type…`, `enforce types`, 12.0.0).
13. **`a new clone of (Turtle sprite)`** (10.0.0; stage-capable 11.0.0) — fresh
    temporary sprites inheriting nothing (`src/blocks.js:11978-11989`); Chapter 7.
14. **Sprite Method API library** (10.2.0) — dot-notation OOP; Chapters 7/8.
15. **Unringed blocks as data** (12.0.0) — CALL/RUN of bare expressions, the
    `expression` attribute selector; Chapters 6 and 11.
16. **Metaprogramming growth** (Chapter 11): the attribute getter/setter menus have
    ~tripled (`primitive`, `comment`, `global?`, `selector`, `slots`, `editables`,
    `replaceables`, `separators`, `collapses`, `expands`, `initial/min/max slots`,
    `translations`, `strict`, `answer`; `src/blocks.js:930-991`), the
    Metaprogramming library (10.0.0), DEFINE behavior changes (10.0.0), LISP text
    syntax round-tripping (10.0.0), slot-type numbers 13-21.
17. **Hyperized `call`** (9.0.0) and **RUN-as-ignore** (11.0.0) — Chapter 6.
18. **`sigmoid (σ)`** in monadic operators (11.0.0), **stage `say`/`write`**
    (9.1.0), **`(paint) on (surface)`** pen primitive (12.0.0) — Chapter 1.
19. **Extensions mechanism** (Chapter 9): Extension-blocks setting, `src_load`,
    `docs/Extensions.md`; websockets (11.0.0).
20. **Chapter 2**: the unsaved-changes confirm dialog / backup-and-restore flow
    (reworked in the 10.0 cycle); project templates (12.0.0).

## LOW

21. "Quicksteps" scheduling making warp/turbo largely obsolete (10.4.0);
    `pick random` reporting floats when an input has a decimal point (10.4.0);
    matrix-kernel convolutions (9.2.0, Chapter 4/Appendix B); balloon/watcher
    copy-to-clipboard and scrolling (10.0.0/12.0.0); block-instance variables
    already partially covered in Chapter 3; piano-widget octave switching (10.0.0).

---

## Verification caveats

- HISTORY.md (9.0.0) records a "with" infix for JOIN/APPEND/COMBINATIONS, but in
  the v12.0.6 source no such infix exists on `%words`/`%lists`
  (`src/blocks.js:1293-1302`) — apparently reverted. The manual makes no claim
  either way; no action needed.
- Negative-index list slicing exists in the source only as experimental code
  explicitly excluded from production `item of` (`src/lists.js:546-613`); it
  should not be documented.
- Chapter 2's save/load flow, Chapter 6's ring/call/run semantics, Chapter 1's
  eight-palette structure, the ≤/≥/≠ relabel claim, and the File-menu item list
  were all checked and are still accurate.
