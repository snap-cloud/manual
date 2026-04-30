# Snap<em>!</em> Manual Style Guide

<!-- Editor Note: This document should be written using GitHub-flavored markdown,
  unlike the rest of the manual. -->

* Write UI elements inside quoted code blocks. e.g. ```"`Open`"```
* Monospaced text should use the CSS class `.mono` e.g. `{span .mono}[text here]`
* Do not put spaces around index entries. See [Indexes](#indexes) below.
* To write Snap! as stylized text write: `Snap<em>!</em>`
* Chapters are included at the top level of the repo, named 'NN-chapter.md'
  * This md file is the content for the chapter.
  * The `images/` folder contains images used in the manual, organized by chapter.
* The `appendix/` folder contains additional chapters, which are subfolders within the `appendix/` folder.
* The `blocks/` folder contains 1 markdown file per block, organized by palette.\
  * `blocks/<palette>/<selector>.md` is the reference for block with selector `x` in palette `palette`.
  * `blocks/<palette>/<selector>.yml` is the metadata for that block, which is used to render the block's help page. You should primarily edit these pages.
  * `blocks/images/` one image per block, named `block_x.png` where `x` is the block *selector*.
  * `blocks/help/` is the help screen for each block, named `selector.png`.


## Editing Section References

* Replace original text with a markdown link (e.g. `[text](url)`) with the section name but no page number
* Links should be formatted like the URL, e.g. `../chapter-name`

## Images

Some images do not need custom CSS classes, but images used as inline examples and those expeorted from Retina displays should have CSS classes applied.

* We have a few classes: `.image-4x`, `.image-2x`, `.image-3x`, and `.image-inline`
* The `-2x` class should be used for most retina-sized images.
* The `-inline` class should be used when you want to place an example within the rest of a paragraph.

Write markdown like this:

```md
![alt text](filename.png){.image-4x}
![alt text](filename.png){.image-inline}
![alt text](filename.png){.image-4x .image-inline} <!-- You probably don't need to combine these classes-->
```
### Linkining to Images

* Most images are contained within an `assets/` folder _within_ each chapter.
* If you are refercing an individual block image, try to reference `/blocks/images/block_x.png` to indicate it is a "standard" block used as a default.
* If an image is the exact same in multiple chapters, try to save it in the _chapter where it is first used_. Then reference that image as `[...](/01-.../assets/myimage.png)`

## Making new CSS classes

Add all CSS to the file `snap-manual.scss`. All "image" related CSS should be prefixed with `image-`
* If you need to make a generic generic class, call it something like what it used for
* If you need to make classes for a specific chapter include that, e.g. `image-ch3-...`
* Otherwise you can use `{style="..."}` to manually set the style of a single image

## Callouts
https://quarto.org/docs/authoring/callouts.html

You may want to replace images on text with a callout block.

```md
::: {.callout-tip}
## Tip with Title

This is an example of a callout with a title.
:::
```

---

# Indexes

The manual ships with an alphabetical index that's compiled into the PDF (and
will eventually be a search-friendly listing in the HTML). Index entries are
the most common annotation in the manual — most pages have several — and the
syntax is the place new contributors are most likely to get stuck.

> [!IMPORTANT]
> If something isn't indexed, it effectively isn't in the manual. Index
> *names* (blocks, menu options, dropdown values) and *ideas* (every
> significant word; e.g. both `lexical scope` and `scope, lexical`). People
> are indexed by family name only.

## Marking an index entry

The manual uses MyST's `index` role and directive. Both forms are
supported; prefer the role for entries that mark a specific word and the
directive when you want to attach several index terms to a paragraph or
figure without changing the visible text.

### Inline role (preferred for most entries)

The basic form puts an entry on whatever word you want indexed:

```md
This chapter describes the {index}`Scratch` features inherited by Snap!
```

Here "Scratch" both stays as visible text and becomes an index entry under
"Scratch".

To index something *under a different term* than the visible text, separate
the visible text and the index term with `<...>`:

```md
arrangement of {index}`regions <layout, window>` in the window
```

That displays "regions" but produces two index entries, **layout** and
**window**, both pointing at this page. Use `;` (semicolons) to express a
sub-entry hierarchy:

```md
{index}`hat block <block; hat>`
```

This produces "block, hat" (a sub-entry under "block") in the index.

### Block directive (for several terms at once)

When you want to attach index entries to a span of text without altering
the visible content, use the directive form:

```md
:::{index}
Snap! program
script
costume
block; command
:::
```

Each line is one entry. Sub-entries use `;` the same way as in the role
form.

### Avoid surrounding spaces

Don't put spaces between an index annotation and the word it's attached to:

```md
✅  the {index}`palette` area at the left edge
❌  the palette {index}`palette` area at the left edge
❌  the {index}`palette`  area at the left edge   (extra space inside the line)
```

## LaTeX `\index{...}` (legacy, **do not use**)

The original Word -> Markdown conversion used LaTeX's `\index{...}` syntax for index entries, which is not rendered by MyST but is still supported by our LaTeX template. When converting legacy entries, you may encounter this syntax. Here's how it compares to the MyST role:

| Goal | MyST | LaTeX |
| ---- | ---- | ----- |
| Simple entry on a word | <code>{index}\`palette\`</code> | `palette\index{palette}` |
| Different visible text vs. index term | <code>{index}\`regions &lt;layout&gt;\`</code> | `regions\index{layout}` |
| Multiple terms at one location | <code>{index}\`regions &lt;layout, window&gt;\`</code> | `regions\index{layout}\index{window}` |
| Sub-entry | <code>{index}\`hat block &lt;block; hat&gt;\`</code> | `hat block\index{block!hat}` |
| Sort key vs. display text | (use sub-entry form) | `\index{block name@$Block Name$ block}` |

LaTeX-specific quirks worth knowing about if you're reading or editing
existing entries:

* `!` denotes sub-entries (`\index{block!hat}`).
* `""` escapes special characters in the entry (e.g. `"!`).
* `@` separates a sort key from the displayed text. The form
  `\index{sortkey@entrytext}` is mostly used to keep block names in the
  right alphabetical position even when the display includes typesetting
  like math mode.
* See <https://en.wikibooks.org/wiki/LaTeX/Indexing> for the full reference.

When converting a legacy entry, prefer the MyST role and let the index term
do the heavy lifting via `<term>` rather than reaching for sort keys.

## How the index gets rendered

The index appears as the last chapter of the manual, [`manual-index.md`](../manual-index.md),
which calls `\printindex`. In the PDF build, our local LaTeX template
([`_latex-template/`](../_latex-template/)) runs `makeindex` with the
[`index-style.ist`](../_latex-template/index-style.ist) style file, which
produces the bold letter-group headings (A, B, C, …), small index entries,
and right-aligned page numbers. See
[`docs/latex.md`](./latex.md) for the full PDF pipeline.

---

# Brian's Guide for Writing the Word Manual

> [!NOTE]
> The specific notes on Word, PDF compilation and techical details no longer apple.
> The rest of the guide on writing style, punctation, goals, etc. are all still useful!

## SNAP! MANUAL STYLE GUIDE and editing tips

There are a lot of little details following this paragraph, but the most important thing is that the manual text should be correct, complete, unambiguous, and understandable by a teenager who has no idea how Snap! is implemented.  And well-indexed.

Fonts:
* Names of blocks and menu options: Tekton Pro Bold
* The name "Snap!": Candara, with the "!" in italics.  (Copy/paste it.)
* Computer text outside of Snap!: Courier
* Everything else: Baskerville

(If you're not careful, Word will put Times, Arial, or Helvetica in.  Don't let it.)  All 12 point except for headings, table of contents, and index.  (You should never have to change the size by hand; setting the style to, e.g., "Heading 1" will set the font, style, and size correctly.  And the TOC and Index take care of themselves.)

Note:  If you insert more than one word of Courier or Tekton Pro Bold in a text paragraph, carefully turn each space between words into Baskerville.  Also be careful about spaces or punctuation abutting a non-Baskerville word.  This sounds super finicky, but it looks terrible if you miss one.  This also means you can't select a word to change into a different font by double-clicking, because Word will include the trailing space in the selection.

Paragraphs:  We have two paragraph styles, Normal and "Indented oaragraph."  (Someday I'll get around to fixing the spelling.)  The names are a little confusing.  Word's automatic treatment of styles is more often correct with the names this way, even though indented is the really normal case.  So you should manually choose Indented (which will stay chosen until you change it), with two exceptions:  (1) The first paragraph after a heading (chapter, section, or subsection) should not be indented.  This is one of those mysterious book editor rules, not worth fighting.  (2) The text right after a displayed picture (in the context of pictures, "display" is the opposite of "run in with text"; it means the picture is on a line by itself) /may or may not/ be indented, depending on whether it is really a continuation of the paragraph interrupted by the display (not indented) or is starting a new topic (indented).

Imported pictures (mainly exported from Snap!):  They show up too big.  If you have a retina display, they show up WAY too big.  It's best if you shrink the picture to 50% or even 25% in Preview > Tools > Adjust size /before/ you import it into Word, to keep the .docx and .pdf files smaller.  Or, in Snap!, shift-click the Settings gear and uncheck "Enable retina display."  To shrink further, "Format Picture" > "Size" and try for 25% or 33% of the original size.  If the picture is a single block to be run in with text, try 20% or even 15%.  We are not trying for manual-wide consistency of sizes, in part because some very wide script pictures wouldn't fit unless we made everything tiny.  But, all else being equal, use the same size percentage within a text topic.  Alas, all else
/isn't/ equal, and the pictures Snap! makes aren't consistently scaled.  Make it look good.  If you try to resize a picture by grabbing its corner,
/don't forget to hold down the shift key!/  Whoever decided that Fun House Mirror should be the default made the second-worst mistake in computing history, after the creation of the Web.  (Lots of worse things have happened, but Facebook and friends aren't mistakes; they're just evil.)  But, back to the point, it's best to resize by number in Format Picture.

Displayed figures:  The manual is inconsistent between centering and left-justifying the picture.  It's ≈90% true that pictures of menus are left-justified while all other pictures (mostly blocks and results) are centered.  Let's try to stick to that.  If there are more than one picture in a display, select them all, click "Align or Distribute" > "Distribute horizontally," then decide how to align them vertically (typically Align Middle for syntactically unrelated pictures, but sometimes Align Top), then Group them.  The whole group should be "Text Wrap" > "Top and Bottom."  In "Format Picture" > "Layout" > "Advanced" you can set the top and bottom spacing to zero.

There is a special case of display alignment for pictures with a list as the shown result of an expression.  These pictures take a lot of vertical space, so in some cases they are aligned right, with a text paragraph in a text box to the left of the speech balloon but overlapping horizontally with the actual block.  See page 38 for two examples.

Pictures in line with text (typically a single block):  Text Wrap > Tight, then Format Picture > Layout > Advanced left space to zero, right space to 0.06 inches.  Then you can drag the block where it belongs in the text, but the fine positioning will require the cursor arrow keys.  Put spaces in the text left or right of the picture where syntactically appropriate, i.e., where you'd put a space left or right of a word.  To see why pictures taller than a single block are problematic in line, look at the second paragraph on page 7.  It's layed out correctly, with respect to its meaning, but it /looks/ screwy.  I should fix it.

Writing style:  Use exclamation points (other than in the name "Snap!") very sparingly; they should indicate danger, not enthusiasm.  Absolutely do not suggest that something is "fun" or "interesting," etc.  (But "more interesting" is okay when it means that you are giving a first, trivial example followed by an example that actually does something useful.)

First person:  Although the manual has two official authors, it's okay to use "I" when describing how you programmed something, e.g.,

>    the word “bark” is just an arbitrary name I made up

on page 9.  But when documenting a disagreement, use "Jens thinks..." and "Brian thinks...," not "I think..."  (We should try to minimize the need to document significant disagreements by resolving them!)  It's also okay to use "we" for uncontroversial choices, both about Snap! itself and about examples in the manual ("we used...").  But /do not/ use "we" for a putative group including yourself and the reader, as in "next we should..."  The reader is "you."

Second person:  Theoretically, "you" belongs in a tutorial, not in a reference manual.  But the distinction is somewhat blurred in this manual, which is more nearly a reference in the early chapters and more nearly a tutorial in the OOP ones.  But as early as page 9 we have

>    In text input slots, a space character is shown as a brown dot, so that
>    you can count the number of spaces between words, and in particular you
>    can tell the difference between an empty slot and one containing spaces.

This is all okay, even though the occasional professor user complains about it.

Index:  The hardest and most annoying part of writing the manual (not counting fighting with Microsoft and Adobe) is indexing (as for any nonfiction writing).  Make index entries for *names* (of blocks, of menu options, of dropdown input options) and for *ideas* (both "lexical scope" and "scope, lexical"; every significant word in the idea's name should have an index entry).  People's names are indexed only by family name.  If this is your first time, read the existing index to learn how entries are styled.  Make sure that the index entries have the correct fonts!  You can edit the text of the entry before you click "Mark" in the dialog.  The index should probably be two or three times its current size, given the manual's current contents.  If something isn't indexed, it effectively isn't in the manual.

Punctuation:  Trailing periods and commas go inside the quotation marks; other punctuation goes outside.  This is occasionally problematic when ending a sentence with a quoted name of a block, option, input value, etc.  I have very rarely put a period outside the closing quotation mark to avoid ambiguity, but I prefer to rephrase the sentence so that the quoted name isn't at the end.

Use parentheses instead of dashes, all else being equal, but try not to nest parentheses.  If you do use dashes, they have to be em dashes, not en dashes or double hyphens.  (If you are indicating a range of numbers, such as RGB values 0-255, that calls for an en dash.)  The subtraction operator is different from all of these.  If you're on a Mac, option-minus is en dash; option-shift-minus is em dash.

I tend to parenthesize too much, including several-sentence digressions, after which I forget the close paren.  If you find one of those, remove the open paren, probably.  Word changes " into curly quotes, and once in a rare while it gets confused about whether or not it's inside quoted text.  Keep an eye out.

Never (really, never) put a colon between a verb and its object, even if the object is a picture.  That is, you wouldn't say

>X   The higher order functions are: map, keep, and combine.

so you equally can't say "The higher order functions are:" followed by a picture of three blocks.  Instead, rephrase to avoid the need for the colon or to move the verb elsewhere in the sentence.

* There are three higher order functions:
* Here are the higher order functions:
* The next category of blocks is higher order functions.

That last alternative doesn't need a colon, although it wouldn't hurt.  (Note in passing that the subject of that last alternative is "category," not "blocks," so its verb is in the singular.)

Widows and orphans:  In this context, a "widow" is the last line of a paragraph, separated from the rest of the paragraph by a page break.  An "orphan" is the first line of a paragraph, or a heading line, separated from the following text by a page break.  Printers have used "widow" since forever; I never heard "orphan" until computer typesetting became a thing, probably because orphans are easy to fix: Insert a page break.  Fixing a widow, though, involves tiny tweaks to spacing, may involve changes to several previous pages, may involve changes to the actual text, and requires a sense of aesthetics.  If you solve either kind of problem with explicit page breaks, remember that the next change to the text of the manual may result in an almost-empty page downstream.  In particular, don't think about widows or orphans until you've finished typing in all of the text you're adding!

Short pages:  Always start a chapter (Word "Heading 1," identified by a Roman numeral) on a new page, no matter how short that makes the previous page.  (But if it's just a few lines, see if you can't squeeze some space out of the previous few pages.)  Starting a section (Word "Heading 2," identified by a capital letter) on a new page is optional, but I generally do it if the section would otherwise start on the last quarter of a page or so.  The same is true for subsections (Word "Heading 3," no identifier) but I'm less prone to putting page breaks before subsections.  Real book editors (i.e., human beings employed by publishing companies to edit books) get very uptight if facing pages (2n and 2n+1) aren't exactly the same height, but amateurs like us don't worry about that.

Another reason for a short page is that what comes next is a tall picture that won't fit at the bottom of the page.  This can be okay, but if the picture is only slightly too tall, try to make room by squeezing earlier pages.  If you do end up leaving a really significant empty space at the end of a page, try to make the immediately preceding text lead the reader to expect that the presentation of this topic isn't finished.

Scratch:  We officially think that the reader of the manual has used Scratch.  This affects us in two ways:  We barely mention the blocks that we share with them, and we sometimes explicitly compare the behaviors of Snap! and Scratch.  Try not to let the latter be understandable as /criticism/ of Scratch; our party line is that Scratch is ideal for its stated purpose, and our language is different because our goals are different.  Say that explicitly (but don't say "party line" of course) if there's any possibility of misunderstanding.  And there's nothing wrong with documenting a block we share with Scratch in detail if that'll help the narrative.


### HOW TO MAKE THE MANUAL:

Yes, this is a 22-step process.  :-(

0.  Change version number on the cover and at the top of page 5.  If there has been a really major change (e.g., hyperblocks), consider updating the picture on the cover.
1.  Save changes.
2.  Remake table of contents: Click on "Table of Contents" at the top of page 2, then choose Update, then choose one of the two options depending on whether you have changed, added, or deleted any headings.
3.  Carefully check every line of the Table of Contents!  Look for wrong fonts, missing labels (I, II, etc for level 1; A, B, etc for level 2; nothing for level 3), Chapter VII header at the top of the second column (if not, adjust spacing around chapters in the first column), Heading 2 letters restarting from A in each chapter.
4.  Edit Table of Contents: On page 2, insert a page break before Appendix A; change the text of II.E ("if you lose...") to boldface italic.  On page 3, insert a column break before Appendix B.  Manually fix the page number for the Index at the end of the ToC, which is not an official section (so it won't be numbered or lettered), so not automatically updated by Word.
5.  Save again.
6.  Scroll through the entire manual, looking for bad page breaks, mislabeled headings, and pictures out of place.  (Some old pictures that are run in with text were inserted into their pages by putting a bunch of spaces in the text, setting the picture's "Wrap Text" to "None," and manually positioning the picture.  These pictures will be out of place if the text on that page changes.  To fix them, move the picture out of the way; delete the extra spaces (keeping one before and/or one after where the picture belongs, depending on nearby punctuation; set the picture's "Wrap Text" to "Tight"; then position the picture where it belongs.  The last little bit of positioning should be done with the cursor arrow keys rather than with the mouse.  Finally, go to
	Format Picture > Layout > Advanced > Text Wrapping
and change the left distance to 0 and the right distance to 0.06 inches.)
7.  If you made changes, save again, then go back to step 2.
8.  Onward to the index!  Click inside the index; the entire thing will be selected in grey.  Now in the Word menu choose Insert > Index and Tables...  In the "Formats" menu, choose "Modern."  Then click OK.  Word will ask if you want to replace the selected index.  Say yes.
9.  Now edit the index.  First, delete the headings for punctuation characters (!, ., #, and ⚡).  Don't be afraid about the entire index still being selected in grey; you can select a subset of the index (such as a heading) within the big selection.  Next, delete the heading for the "fi" ligature, and the (second) "F" heading after it.  Scan through looking for widows and orphans, and try to fix them by adjusting spacing around individual headings.
10.  These issues are mostly fixed, but read the entire index looking for font problems.  If you find one, don't just fix it in the index; go back to the page indicated and fix the entry there.  (Click the ¶ button to make it visible.)
11.  Save again!
12.  Go to File > Page Setup and make sure it says "US Letter Borderless."  (It's in a submenu buried below "US Letter" in the main menu.)  Before you click OK, go up to the top where it says "Page Attributes," click, select "Microsoft Word," and make sure the "apply changes to" field says "whole document," not "current section."  If anything goes wrong later in the process, or if you take your eyes off the Word window for a second, Word will switch it back to "US Letter," so keep checking!
13.  To make sure this worked, instead of choosing "Save as..." and then saving as PDF, choose "Print," make sure the preview of the cover is borderless, and then choose "Save as PDF" down in the bottom left corner.  If the preview isn't borderless, click "Page setup" inside the Print dialog and repeat step 12 there.
14.  If Word pops up a dialog saying that a header or footer is outside the printable area, it means you looked away from the Word window for a second. Click "No" and go back to step 12.
15.  You now have a PDF; time to massage it.  If you're on a Mac, find the file "snap-manual-meta.workflow" and double click it.  Edit the Snap version number in the Title field, then click the Run button at the top right.  If you're not on a Mac, find something equivalent for your operating system and edit this file to add that information.  The goal is to change the PDF's metadata to get "Microsoft Word" out of the title.
16.  You're done with the required steps, but your PDF is 80Mb.  It would be nice to reduce that.  Fire up your virtual Windows machine and copy the PDF to its desktop.  (For me, the following steps crash Acrobat on my Mac.  That's why I have to shrink the PDF on my virtual PC.  If it works on your Mac, great!)
Also copy the file "Snap Manual Link Dictionary.ald" from the help folder of the repo onto your PC desktop.  You also need to have AutoBookmarker Pro installed on your PC.
17.  Open SnapManual.pdf in Acrobat.  Go through their extremely obnoxious login process.
18.  Choose "Action Wizard" from the Tools menu, then choose "Frobnicate Snap Manual" as the action to perform.  This will both reduce the size and make the links in the Table of Contents, the Index, and URLs active.
19.  Go eat dinner.
20.  Go eat breakfast.
21.  When it finally finishes, copy the file back to your Mac.  It should be reduced down to 60Mb or so. (Yes, that's still a lot.)


LONG TERM PROJECTS

* Find out what makes both the .docx and the .pdf so big, and fix it.
* Convert to TeXinfo. (Someone did this a long time back, but I was scared to try to deal with picture layout in TeX so didn't keep it up.)
* Systematically find and fix all the word-wrap-none pictures.
* Add a bazillion index entries.
* Tutorials, duh, real soon now.
* Make Jens read it carefully, fix any errors, and add any missing features, shortcuts, gotchas, etc.
* Get the line spacing consistent within a paragraph.
* Find all the hideous block pictures, especially the ones including results in speech balloons, and redo them.
