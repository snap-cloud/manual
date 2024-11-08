# Blocks, Scripts, and Sprites

This chapter describes the Snap<em>!</em> features inherited from Scratch;
experienced Scratch users can skip to Section B.

Snap<em>!</em> is a programming language---a notation in which you can tell a
computer what you want it to do. Unlike most programming languages,
though, Snap<em>!</em> is a *visual* language; instead of writing a program
using the keyboard, the Snap<em>!</em> programmer uses the same drag-and-drop
interface familiar to computer users.

Start Snap<em>!</em>. You should see the following arrangement of regions in the window:

<img src="/content/assets/images/image5.png" style="width:415px; height:258px">

(The proportions of these areas may be different, depending on the size
and shape of your browser window.)


A Snap<em>!</em> program consists of one or more *scripts,* each of which is made of *blocks.* Here's a typical script:

<img src="/content/assets/images/image6.png" style="width:142px; height:130px">


The five blocks that make up this script have three different colors, corresponding to three of the eight *palettes* in which blocks can be found. The palette area at the left edge of the window shows one palette at a time, chosen with the eight buttons just above the palette area. In this script, the gold blocks are from the Control palette; the green block is from the Pen palette; and
the blue blocks are from the Motion palette. A script is assembled by dragging blocks from a palette into the *scripting area* in the middle part of the window. Blocks snap together (hence the name Snap<em>!</em> for the language) when you drag a block so that its indentation is near the tab of the one above it:

<img src="/content/assets/images/image7.png" style="width:216px; height:141px">
<img src="/content/assets/images/image8.png" style="width:212px; height:109px">

The white horizontal line is a signal that if you let go of the green
block it will snap into the tab of the gold one.

### Hat Blocks and Command Blocks

At the top of the script is a *hat* block, which indicates when the
script should be carried out. Hat block names typically start with the
word "when"; in the square-drawing example on page 5, the script should
be run when the green flag near the right end of the Snap<em>!</em> tool bar is
clicked. (The Snap<em>!</em> tool bar is part of the Snap<em>!</em> window, not the
same as the browser's or operating system's menu bar.) A script isn't
required to have a hat block, but if not, then the script will be run
only if the user clicks on the script itself. A script can't have more
than one hat block, and the hat block can be used only at the top of the
script; its distinctive shape is meant to remind you of that.[^1]


The other blocks in our example script are *command* blocks. Each command block corresponds to an action that Snap<em>!</em> already knows how to carry out. For example, the <img src="/content/assets/images/image9.png" style="width:112px; height:24px"> block tells the sprite (the arrowhead shape on the *stage* at the right end of the window) to move ten steps (a step is a very small unit of distance) in the direction in which the arrowhead is pointing. We'll see shortly that there can be more than one sprite, and that each sprite has its own scripts. Also, a sprite doesn't have to look like an arrowhead, but can have any picture as a *costume.* The shape of the move block is meant to remind you of a
Lego™ brick; a script is a stack of blocks. (The word "block" denotes
both the graphical shape on the screen and the procedure, the action,
that the block carries out.)


The number 10 in the move block above is called an *input* to the block. By clicking on the white oval, you can type any number in place of the 10. The sample script on the previous page uses 100 as the input value. We'll see later that inputs can have non-oval shapes that accept values other than numbers. We'll also see that you can compute input values, instead of typing a particular value into the oval. A block can have more than one input slot. For example,
the glide block located about halfway down the Motion palette has three
inputs.

Most command blocks have that brick shape, but some, like the repeat
block in the sample script, are *C‑shaped.* Most C-shaped blocks are
found in the Control palette. The slot inside the C shape is a special
kind of input slot that accepts a *script* as the input.


In the sample script

<img src="/content/assets/images/image6.png" style="width:600px; height:130px">

C-shaped blocks can be put in a script in
two ways. If you see a white line and let go, the block will be inserted
into the script like any command block:

<img src="/content/assets/images/image12.png" style="width:547px; height:139px">

But if you see an orange halo and let go,
the block will *wrap* around the haloed blocks:

<img src="/content/assets/images/image16.png" style="width:550px; height:123px">

The halo will always extend from the
cursor position to the bottom of the script:

<img src="/content/assets/images/image20.png" style="width:550px; height:124px">

If you want only some of those blocks, after wrapping you can grab the
first block you don't want wrapped, pull it down, and snap it under the
C-shaped block.

For "E-shaped" blocks with more than one
C-shaped slot, only the first slot will wrap around existing blocks in a
script, and only if that C-shaped slot is empty before wrapping. (You
can fill the other slots by dragging blocks into the desired slot.)

<img src="/content/assets/images/image24.png" style="width:222px; height:131px">

<!--<img src="/content/assets/images/image25.png" style="width:33px; height:23px">
-->

<em>One of the hat blocks, the generic “when anything” <img src="/content/assets/images/image10.png" style="width:105px; height:34px">block, is subtly different from the others. When the stop sign is clicked, or when a project or sprite is loaded, this block doesn’t test whether the condition in its hexagonal input slot is true, so the script beneath it will not run, until some other script in the project runs (because, for example, you click the green flag). When generic when blocks are disabled, the stop sign will be square instead of octagonal.</em>