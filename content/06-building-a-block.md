#  Building a Block

The first version of Snap*!* was called BYOB, for "Build Your Own Blocks
\\index{Build Your Own Blocks}." This was the first and is still the
most important capability we added to Scratch \\index{Scratch}. (The
name was changed because a few teachers have no sense of humor. ☹ You
pick your battles.) Scratch 2.0 and later also has a partial custom
block capability.

## Simple Blocks

In every palette, at or near the bottom, is a button labeled "Make a
block \\index{Make a block}." Also, floating near the top of the palette
is a plus sign. Also, the menu you get by right-clicking on the
background of the scripting area has a "make a block" option.

![](assets/chp-06-image501.png) <!-- width="2.2708333333333335in" height="2.3472222222222223in" -->Clicking any of these will display a
dialog window in which you choose the block's name, shape, and
palette/color. You also decide whether the block will be available to
all sprites, or only to the current sprite and its children.

In this dialog box, you can choose the block\'s palette, shape, and
name. With one exception, there is one color \\index{color of blocks}
per palette, e.g., all Motion blocks are blue. But the Variables palette
includes the orange variable-related blocks and the red list-related
blocks. Both colors are available, along with an "Other" option that
makes grey blocks in the Variables palette for blocks that don't fit any
category.

There are three block shapes \\index{shapes of blocks}, following a
convention that should be familiar to Scratch users: The
jigsaw-puzzle-piece shaped blocks \\index{jigsaw-piece blocks} are
Commands, and don't report a value. The oval blocks \\index{oval blocks}
are Reporters, and the hexagonal blocks \\index{hexagonal blocks} are
Predicates, which is the technical term for reporters that report
Boolean (true or false) values.

Suppose you want to make a block named "square" that draws a square. You
would choose Motion, Command, and type "square" into the name field.
When you click OK, you enter the Block Editor \\index{Block Editor}.
This works just like making a script in the sprite's scripting area,
except that the "hat" block at the top, instead of saying something like
"when I am clicked," has a picture of the block you're building. This
hat block \\index{hat block} is called the *prototype*
\\index{prototype} of your custom block.[^3] You drag blocks under the
hat to program your custom block, then click OK:

![](assets/chp-06-image502.png) <!-- width="4.210937226596675in" height="1.3364041994750657in" -->

![](assets/chp-06-image503.png) <!-- width="4.615555555555556in" height="3.647777777777778in" -->

Your block appears at the bottom of the Motion palette. Here's the block
and the result of using it:

###  Custom Blocks with Inputs

But suppose you want to be able to draw squares of different sizes.
Control-click or right-click on the block, choose "edit," and the Block
Editor \\index{Block Editor} will open. Notice the plus signs before and
after the word square in the prototype block. If you hover the mouse
over one, it lights up:

![](assets/chp-06-image508.png) <!-- width="3.4444444444444446in" height="2.7222222222222223in" -->

![](assets/chp-06-image509.png) <!-- width="2.5833333333333335in" height="1.6041666666666667in" -->Click on the plus on the right. You will
then see the "input name" dialog \\index{input name dialog}:

Type in the name "size" and click OK. There are other options in this
dialog; you can choose "title text \\index{title text}" if you want to
add words to the block name, so it can have text after an input slot,
like the "move ( ) steps" block. Or you can select a more extensive
dialog with a lot of options about your input name. But we'll leave that
for later. When you click OK, the new input appears in the block
prototype:

![](assets/chp-06-image510.png) <!-- width="1.4791666666666667in" height="1.4895833333333333in" -->You can now drag the orange variable down
into the script, then click okay:

![](assets/chp-06-image511.png) <!-- width="1.474724409448819in" height="1.495495406824147in" -->

![](assets/chp-06-image512.png) <!-- width="0.6979166666666666in" height="0.25in" -->Your block now appears in the Motion palette with an
input box: You can draw any size square by entering the length of its
side in the box and running the block as usual, by clicking it or by
putting it in a script.

### Editing Block Properties

![](assets/chp-06-image513.png) <!-- width="0.9993055555555556in" height="0.7604166666666666in" -->What if you change your mind about a
block's color (palette) or shape (command, reporter, predicate)? If you
click in the hat block at the top that holds the prototype, but not in
the prototype itself, you'll see a window in which you can change the
color, and *sometimes* the shape, namely, if the block is not used in
any script, whether in a scripting area or in another custom block.
(This includes a one-block script consisting of a copy of the new block
pulled out of the palette into the scripting area, seeing which made you
realize it's the wrong category. Just delete that copy (drag it back to
the palette) and then change the category.)

If you right-click/control-click the hat block, you get this menu:

Script pic \\index{script pic} exports a picture of the script. (Many of
the illustrations in this manual were made that way.) Translations
\\index{translations option} opens a window in which you can specify how
your block should be translated if the user chooses a language other
than the one in which you are programming. Block variables lets you
create a variant of script variables for this block: A script variable
is created when a block is called, and it disappears when that call
finishes. What if you want a variable that's local to this block, as a
script variable is, but doesn't disappear between invocations? That's a
block variable \\index{block variable}. If the definition of a block
includes a block variable, then every time that (custom) block is
dragged from the palette into a script, the block variable is created.
Every time *that copy* of the block is called, it uses the same block
variable, which preserves its value between calls. Other copies of the
block have their own block variables. The in palette checkbox determines
whether or not this block will be visible in the palette. It's normally
checked, but you may want to hide custom blocks if you're a curriculum
writer creating a Parsons problem. To unhide blocks, choose "Hide
blocks" from the File menu and uncheck the checkboxes. Edit does the
same thing as regular clicking, as described earlier.

## Recursion

![](assets/chp-06-image514.png) <!-- width="2.9652777777777777in" height="2.3631944444444444in" -->![](assets/chp-06-image515.png) <!-- width="1.9583333333333333in" height="2.3541666666666665in" -->![](assets/chp-06-image516.png) <!-- width="1.4236111111111112in" height="0.9118055555555555in" -->Since the new custom \\index{recursion}
block appears in its palette as soon as you *start* editing it, you can
write recursive blocks (blocks that call themselves) by dragging the
block into its own definition:

(If you added inputs to the block since opening the editor, click Apply
before finding the block in the palette, or drag the \\index{drag from
prototype}block from the top of the block editor rather than from the
palette.)

If recursion is new to you, here are a few brief hints: It's crucial
that the recursion have a *base case* \\index{base case}*,* that is,
some small(est) case that the block can handle without using recursion.
In this example, it's the case depth=0, for which the block does nothing
at all, because of the enclosing if. Without a base case, the recursion
would run forever, calling itself over and over.

Don't try to trace the exact sequence of steps that the computer follows
in a recursive program. Instead, imagine that inside the computer there
are many small people, and if Theresa is drawing a tree of size 100,
depth 6, she hires Tom to make a tree of size 70, depth 5, and later
hires Theo to make another tree of size 70, depth 5. Tom in turn hires
Tammy and Tallulah, and so on. Each little person \\index{little people}
has his or her own local variables size and depth, each with different
values.

You can also write recursive reporters \\index{reporters, recursive},
like this block to compute the factorial \\index{factorial} function:

Note the use of the report block \\index{report block}. When a reporter
block uses this block, the reporter finishes its work and reports the
value given; any further blocks in the script are not evaluated. Thus,
the if else block in the script above could have been just an if, with
the second report block below it instead of inside it, and the result
would be the same, because when the ﬁrst report is seen in the base
case, that finishes the block invocation, and the second report is
ignored. There is also a stop this block block \\index{stop block block}
that has a similar purpose, ending the block invocation early, for
command blocks. (By contrast, the stop this script block \\index{stop
script block} stops not only the current block invocation, but also the
entire toplevel script that called it.)

![](assets/chp-06-image521.png) <!-- width="4.291666666666667in" height="0.8645833333333334in" -->Here's a slightly more compact way to
write the factorial function:

For more on recursion, see *Thinking Recursively* \\index{Thinking
Recursively} by Eric Roberts \\index{Roberts, Eric}. (The original
edition is ISBN 978‑0471816522; a more recent *Thinking Recursively in
Java* is ISBN 978-0471701460.)

## Block Libraries

When you save a project (see Chapter II above), any custom blocks you've
made are saved with it. But sometimes you'd like to save a collection of
blocks that you expect to be useful in more than one project. Perhaps
your blocks implement a particular data structure (a stack, or a
dictionary, etc.), or they're the framework for building a multilevel
game. Such a collection of blocks is called a *block library.*

*\
*To create a block library, \\index{library:block} choose "Export
blocks..." from the File menu. You then see a window like this:

![](assets/chp-06-image522.png) <!-- width="2.0215277777777776in" height="2.7222222222222223in" -->The window shows all of your global custom
blocks. You can uncheck some of the checkboxes to select exactly which
blocks you want to include in your library. (You can right-click or
control-click on the export window for a menu that lets you check or
uncheck all the boxes at once.) Then press OK. An XML file containing
the blocks will appear in your Downloads location.

To import a block library, use the "Import..." command in the File menu,
or just drag the XML file into the Snap*!* window.

Several block libraries are included with Snap*!*; for details about
them, see page [25](#libraries-1).

## Custom blocks and Visible Stepping

Visible stepping \\index{visible stepping} normally treats a call to a
custom block as a single step. If you want to see stepping inside a
custom block you must take these steps *in order:*

1.  ![Macintosh
    HD:Users:bh:Desktop:pix:footprint-lit.png](media/image123.png) <!-- width="0.2916666666666667in"     height="0.16666666666666666in" -->Turn on Visible Stepping.

2.  Select "Edit" in the context menu(s) of the block(s) you want to
    examine.

3.  Then start the program.

The Block Editor windows you open in step 2 do not have full editing
capability. You can tell because there is only one "OK" button at the
bottom, not the usual three buttons. Use the button to close these
windows when done stepping.

