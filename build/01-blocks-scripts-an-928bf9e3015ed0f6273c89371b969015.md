---
---

:::{index}
Scratch
:::

(sec-ch01)=
# 1. Blocks, Scripts, and Sprites

This chapter describes the Snap<em>!</em> features inherited from Scratch; experienced Scratch users can skip to @sec-sprites-parallelism.

Snap<em>!</em> is a programming language—a notation in which you can tell a
computer what you want it to do. Unlike most programming languages,
though, Snap<em>!</em> is a *visual* language; instead of writing a program
using the keyboard, the Snap<em>!</em> programmer uses the same drag-and-drop
interface familiar to computer users.

Start Snap<em>!</em>. You should see the following
arrangement of {index}`regions <layout, window>` in the window:

{img alt="An annotated screenshot of blank Snap! editor" width="4.5in"}`images/12-user-interface-elements/snap-ide-annotated.png`

(The proportions of these areas may be different, depending on the size
and shape of your browser window.)

A Snap<em>!</em> program consists of one or more
*scripts,* each of which is made of *blocks.* Here’s a typical script:
:::{index}
Snap! program
script
:::

(fig-draw-square)=
{img alt="image6.png" width="1.48in"}`images/01-blocks-scripts-and-sprites/image6.png`

The five {index}`blocks <block>` that make up this script have three different colors,
corresponding to three of the eight *palettes* in which blocks
can be found. The {index}`palette` area at the left edge of the
window shows one palette at a time, chosen with the eight buttons just
above the palette area. In this script, the gold blocks are from the
Control palette; the green block is from the Pen palette; and the blue
blocks are from the Motion palette. A script is assembled by dragging
blocks from a palette into the {index}`scripting area`
in the middle part of the window. Blocks snap together (hence the name
Snap<em>!</em> for the language) when you drag a block so that its indentation
is near the tab of the one above it:

(fig-snapping-blocks)=
::::{grid} 2

:::{grid-item}
{img alt="image7.png" width="2.25in"}`images/01-blocks-scripts-and-sprites/image7.png`
:::

:::{grid-item}
{img alt="image8.png" width="2.21in"}`images/01-blocks-scripts-and-sprites/image8.png`
:::
::::

The white horizontal line is a signal that if you let go of the green
block it will snap into the tab of the gold one.

:::{index}
green flag
single: flag, green
tool bar
stage
sprite
:::
## Hat Blocks and Command Blocks
At the top of the script is a *hat* block, which indicates when the
script should be carried out. Hat block names typically start with the
word “when”; in the square-drawing example in @fig-draw-square, the script should
be run when the green flag near the right end of the
Snap<em>!</em> tool bar is clicked. (The Snap<em>!</em> tool bar is
part of the Snap<em>!</em> window, not the same as the browser’s or operating
system’s menu bar.) A script isn’t required to have a
{index}`hat block <block; hat>`, but if not, then the script will be run only if the
user clicks on the script itself. A script can’t have more than one hat
block, and the hat block can be used only at the top of the script; its
distinctive shape is meant to remind you of
that.[^1]

<!-- TODO: Different CSS for an inline hat block? -->

[^1]: One of the hat blocks, the {index}`generic hat block <hat block; generic>` “when anything” block {inline alt="generic when hat block"}`images/01-blocks-scripts-and-sprites/image10`, is subtly different from the others. When the stop sign is clicked, or when a project or sprite is loaded, this block doesn’t test whether the condition in its hexagonal input slot is true, so the script beneath it will not run, until some *other* script in the project runs (because, for example, you click the green flag). When {index}`generic when` blocks are disabled, the stop sign {index}`stop sign, square` will be squarewill be {index}`square <square stop sign>` instead of octagonal.


The other blocks in our example script are *command* blocks. Each {index}`command block`
corresponds to an action that Snap<em>!</em> already knows how to carry out.
For example, the block {inline alt="image9.png"}`./blocks/images/block_forward` tells the sprite (the arrowhead shape on the _stage_ at the right end of the window) to
move ten steps (a step is a very small unit of distance) in the
direction in which the arrowhead is pointing. We’ll see shortly that
there can be more than one sprite, and that each sprite has its own
scripts. Also, a sprite doesn’t have to look like an arrowhead, but can
have any picture as a *costume.* The shape of the
move block is meant to remind you of a Lego™ brick; a {index}`script` is a stack of blocks. (The word “block” denotes both the graphical shape on the screen and the procedure,
the action, that the block carries out.)

:::{index} stack of blocks
procedure
costume
block; command
:::

The number 10 in the `move` block above is called an *input* to the block. By
clicking on the white oval, you can type any number in place of the 10.
The sample script on the previous page uses 100 as the input value. We’ll see later that inputs can have non-oval
shapes that accept values other than numbers. We’ll also see that you
can compute input values, instead of typing a particular value into the
oval. A block can have more than one input slot. For example, the `glide`
block located about halfway down the Motion palette has three inputs.
:::{index} input
:::

Most command blocks have that brick shape, but some, like the `repeat`
block in the sample script, are *C‑shaped.* Most
C-shaped blocks are found
in the {index}`Control palette`. The slot inside the C
shape is a special kind of input slot that accepts a *script* as the
input.

:::{index} repeat block
block; C-shaped
C-shaped block
:::

::::{grid} 4

:::{grid-item}
In the sample script
:::

:::{grid-item}
{img alt="image6.png" width="1.48in"}`images/01-blocks-scripts-and-sprites/image6.png`
:::

:::{grid-item}
the `repeat` block has two inputs: the number 4 and the script
:::

:::{grid-item}
{img alt="image11.png" width="1.41in"}`images/01-blocks-scripts-and-sprites/image11.png`
:::
::::

C-shaped blocks can be put in a script in two ways. If you see a white
line and let go, the block will be inserted into the script like any
command block:

::::{grid} 2

:::{grid-item}
{img alt="image12.png" width="5.70in"}`images/01-blocks-scripts-and-sprites/image12.png`
:::

:::{grid-item}
{img alt="image13.png" width="5.70in"}`images/01-blocks-scripts-and-sprites/image13.png`
:::
::::

<!-- Note until images are cleaned up 12 and 14 were identical, 13 and 15 were identical. -->

But if you see an orange halo and let go, the block will *wrap* around
the haloed blocks:

::::{grid} 2

:::{grid-item}
{img alt="image16.png" width="5.50in"}`images/01-blocks-scripts-and-sprites/image16.png`
:::

:::{grid-item}
{img alt="image17.png" width="5.50in"}`images/01-blocks-scripts-and-sprites/image17.png`
:::
::::

The halo will always extend from the cursor position to the bottom of
the script:

::::{grid} 2

:::{grid-item}
{img alt="image18.png"}`images/01-blocks-scripts-and-sprites/image18.png`
:::

:::{grid-item}
{img alt="image19.png"}`images/01-blocks-scripts-and-sprites/image19.png`
:::
::::

If you want only some of those blocks, after wrapping you can grab the
first block you don’t want wrapped, pull it down, and snap it under the
C-shaped block.

For “E-shaped” blocks with more than one C-shaped slot, only the first slot
will wrap around existing blocks in a script, and only if that C-shaped
slot is empty before wrapping. (You can fill the other slots by dragging
blocks into the desired slot.)

{img alt="image24.png" width="2.31in"}`images/01-blocks-scripts-and-sprites/image24.png`

:::{index} new sprite button
sprite corral
parallelism
:::
(sec-sprites-parallelism)=
## Sprites and Parallelism

Just below the stage is the “new sprite button”
{inline alt="image25.png"}`images/01-blocks-scripts-and-sprites/image25`. Click the button to add a new sprite to the stage. The new
sprite will appear in a random position on the stage, with a random
color, but always facing to the right.

Each sprite has its own scripts. To see the scripts for a particular
sprite in the scripting area, click on the picture of that sprite in the
*sprite corral* in the bottom right corner of the
window. Try putting one of the following scripts in each sprite’s
scripting area:

::::{grid} 2

:::{grid-item}
{img alt="image26.png" width="1.55in"}`images/01-blocks-scripts-and-sprites/image26.png`
:::

:::{grid-item}
{img alt="image27.png" width="1.54in"}`images/01-blocks-scripts-and-sprites/image27.png`
:::
::::

When you click the green flag, you should see one sprite rotate while
the other moves back and forth. This experiment illustrates the way
different scripts can run in parallel. The turning and the moving happen
together. Parallelism can be seen with multiple
scripts of a single sprite also. Try this example:

::::{grid} 2

:::{grid-item}
{img alt="image28.png" width="1.73in"}`images/01-blocks-scripts-and-sprites/image28.png`
:::

:::{grid-item}
{img alt="image29.png" width="1.73in"}`images/01-blocks-scripts-and-sprites/image29.png`
:::
::::

When you click the green flag, the sprite should move back and forth

When you press the space key, the sprite should move forever in a
circle, because the move and turn blocks are run in parallel. (To stop
the program, click the red {index}`stop sign` at the right end
of the tool bar.)

:::{index} jukebox
`play sound` block
costume
Costumes tab
playing sounds
single: Church, Alonzo
wardrobe
Turtle costume
Alonzo
procedures as data
Scratch
:::

### Costumes and Sounds
To change the appearance of a sprite, paint or import a new *costume* for it. To paint a costume, click on the Costumes tab above the
scripting area, and click the paint button {inline alt="image32.png"}`images/01-blocks-scripts-and-sprites/image32.png` The *Paint Editor* that
appears is explained in @sec-the-paint-editor. There are three
ways to import a costume. First select the desired sprite in the sprite
corral. Then, one way is to click on the file icon in the tool bar,
then choose {inline alt="image30.png"}`images/01-blocks-scripts-and-sprites/image30` the “`Costumes…`” menu item. You will see a list of costumes
from the public media library, and can choose one. The second way, for a
costume stored on your own computer, is to click on the file icon and
choose the “Import…” menu item. You can then select a file in any
picture format (PNG, JPEG, etc.) supported by your browser. The third
way is quicker if the file you want is visible on the desktop: Just drag
the file onto the Snap<em>!</em> window. In any of these cases, the scripting
area will be replaced by something like this:

{img alt="image31.png" width="1.77in"}`images/01-blocks-scripts-and-sprites/image31.png`

Just above this part of the window is a set of three tabs: Scripts,
Costumes, and Sounds. You’ll see that the Costumes
tab is now selected. In this view, the sprite’s *wardrobe*,
you can choose whether the sprite should wear its
Turtle costume or its Alonzo costume. (Alonzo, the Snap<em>!</em> mascot, is named after Alonzo Church, a
mathematician who invented the idea of procedures as data, the most important way in which Snap<em>!</em> is
different from Scratch.) You can give a sprite as many
costumes as you like, and then choose which it will wear either by
clicking in its wardrobe or by using the {inline alt="image35.png"}`./blocks/images/block_doSwitchToCostume` or {inline alt="Next Costume"}`./blocks/images/block_doWearNextCostume` block in a script.
(Every costume has a number as well as a name. The `next` costume block
selects the next costume by number; after the highest-numbered costume it
switches to costume 1. The Turtle, costume 0, is never chosen by next
costume.) The Turtle costume is the only one that
changes color to match a change in the sprite’s pen color.

::: {.callout-tip}
{inline alt="Switch to costumer (() - 1)"}`images/01-blocks-scripts-and-sprites/image33.png` switches to the *previous* costume, wrapping like `next costume`.
:::
<!-- Protip: {inline alt="Switch to costumer (() - 1)"}`images/01-blocks-scripts-and-sprites/image33` switches to the *previous* costume, wrapping like `next costume`.
-->

In addition to its costumes, a sprite can have *sounds;* the equivalent for sounds of the sprite’s wardrobe is called its *jukebox.* Sound files can be imported in any format (WAV, OGG, MP3, etc.) supported by your browser. Two blocks accomplish the task of playing sounds. If you would like a script to continue running while the sound is playing, use the block {inline alt="image39.png"}`images/01-blocks-scripts-and-sprites/image39.png`. In contrast, you can use the block {inline alt="image38.png"}`images/01-blocks-scripts-and-sprites/image38.png` to wait for the sound's completion before continuing the rest of the script.

:::{index} `broadcast and wait` block
`broadcast` block
:::
(sec-broadcast)=
### Inter-Sprite Communication with Broadcast

Earlier we saw an example of two sprites moving at the same time. In a
more interesting program, though, the sprites on stage will *interact*
to tell a story, play a game, etc. Often one sprite will have to tell
another sprite to run a script. Here’s a simple example:

(fig-broadcast-dog)=
::::{grid} 4
:::{grid-item}
{img alt="image41.png" width="0.57in"}`images/01-blocks-scripts-and-sprites/image41.png`
:::

:::{grid-item}
{img alt="image42.png" width="2.78in"}`images/01-blocks-scripts-and-sprites/image42.png`
:::

:::{grid-item}
{img alt="image43.png" width="1.24in"}`images/01-blocks-scripts-and-sprites/image43.png`
:::

:::{grid-item}
{img alt="image44.png" width="1.52in"}`images/01-blocks-scripts-and-sprites/image44.png`
:::
::::


In the block {inline alt="image40.png"}`images/01-blocks-scripts-and-sprites/image40`, the word “bark” is just an arbitrary name I made up. When you
click on the downward arrowhead in that input slot, one of the choices
(the only choice, the first time) is “new,” which then prompts you to
enter a name for the new broadcast. When this block is run, the chosen
message is sent to *every* sprite, which is why the block is called
“broadcast.” (But if you click the right arrow after the message name,
the block becomes {inline alt="image45.png"}`images/01-blocks-scripts-and-sprites/image45`, and you can change it to {inline alt="image46.png"}`images/01-blocks-scripts-and-sprites/image46` to send the message just to one sprite.) In this program, though, only one sprite has a script to
run when that broadcast is sent, namely the dog. Because the boy’s
script uses `broadcast and wait` rather
than just broadcast, the boy doesn’t go on to his next say block until
the dog’s script finishes. That’s why the two sprites take turns
talking, instead of both talking at once. In @sec-ch07 you’ll see a more flexible
way to send a message to a specific sprite using the tell and ask
blocks.

Notice, by the way, that the say block’s first input slot is rectangular
rather than oval. This means the input can be any text string, not only
a number. In {index}`text input` slots, a space character is
shown as a {index}`brown dot`, so that you can count the
number of spaces between words, and in particular you can tell the
difference between an empty slot and one containing spaces. The brown
dots are *not* shown on the stage if the text is displayed.

The stage has its own scripting area. It can be selected by clicking on
the Stage icon at the left of the sprite corral. Unlike a sprite,
though, the stage can’t move. Instead of costumes, it has *backgrounds:*
pictures that fill the entire stage area. The sprites appear in front of
the current background. In a complicated project, it’s often convenient
to use a script in the stage’s scripting area as the overall director of
the action.

:::{index} backgrounds
Nesting Sprites
anchor
parts (of nested sprite)
synchronous rotation
dangling rotation
:::

(nesting-sprites-anchors-and-parts)=
## Nesting Sprites: Anchors and Parts

Sometimes it’s desirable to make a sort of “super-sprite” composed of
pieces that can move together but can also be separately articulated.
The classic example is a person’s body made up of a torso, limbs, and a
head. Snap<em>!</em> allows one sprite to be designated as the *anchor*
of the combined shape, with other sprites as its *parts.*

To set up sprite nesting, drag the sprite corral icon of a *part* sprite
onto the stage display (not the sprite corral icon!) of the desired
*anchor* sprite. The precise place where you let go of the mouse button
will be the attachment point of the part on the anchor.
:::{index} sprite nesting
:::

Sprite nesting is shown in the sprite corral icons of both anchors and parts:

{img alt="image47.png" width="1.63056in"}`images/01-blocks-scripts-and-sprites/image47.png`

In this illustration, it is desired to animate Alonzo’s arm. (The arm has
been colored green in this picture to make the relationship of the two
sprites clearer, but in a real project they’d be the same color,
probably.) Sprite, representing Alonzo’s body, is the anchor; Sprite(2)
is the arm. The icon for the anchor shows small images of up to three
attached parts at the bottom. The icon for each part shows a small image
of the anchor in its top left corner, and a *synchronous*
 *dangling rotation* *flag* in the top right corner. In its initial, synchronous
setting, as shown above, it means that the when the anchor sprite
rotates, the part sprite also rotates as well as revolving around the
anchor. When clicked, it changes from a circular arrow to a straight
arrow, and indicates that when the anchor sprite rotates, the part
sprite revolves around it, but does not rotate, keeping its original
orientation. (The part can also be rotated separately, using its turn
blocks.) Any change in the position or size of the anchor is always
extended to its parts. Also, cloning the anchor (see Section @sec-permanent-and-temporary-clones)
will also clone all its parts.

<!-- TODO: Figure w/caption -->
{img alt="image56.png" width="1.44in"}`images/01-blocks-scripts-and-sprites/image56.png`

{img alt="image48.png" width="4.88in"}`images/01-blocks-scripts-and-sprites/image48.png`

{img alt="image49.png" width="4.88in"}`images/01-blocks-scripts-and-sprites/image49.png`

*Top: turning the part: the green arm. Bottom: turning the anchor, with
the arm synchronous (left) and dangling (right).*

:::{index} zebra coloring
expression
halo
block; reporter
`reporter` block
:::
## Reporter Blocks and Expressions

So far, we’ve used two kinds of blocks: hat blocks
and command blocks. Another kind is the *reporter* block, which has an oval shape: {inline alt="image66.png"}`images/01-blocks-scripts-and-sprites/image66.png`. It’s called a “reporter” because
when it’s run, instead of carrying out an action, it reports a value
that can be used as an input to another block. If you drag a {inline alt="image65.png"}`images/01-blocks-scripts-and-sprites/image65` reporter into the scripting area by itself and click on it, the value it reports
will appear in a speech balloon next to the block:

When you drag a reporter block over another block’s input slot, a white
“halo” appears around that input slot, analogous to the
white line that appears when snapping command blocks together:

{img alt="image67.png" width="1.47in"}`images/01-blocks-scripts-and-sprites/image67.png`

Don’t drop the input over a *red* halo:
{img alt="image71.png" width="2.11111in"}`images/01-blocks-scripts-and-sprites/image71.png`

That’s used for a purpose explained in @sec-recursive-calls-to-multiple-input-blocks.

Here’s a simple script that uses a reporter block:

{img alt="image72.png" width="2.11111in"}`images/01-blocks-scripts-and-sprites/image72.png`

Here the `x position` reporter provides the first input to the say block.
(The sprite’s {index}`x position` is its horizontal position,
how far left (negative values) or right (positive values) it is compared
to the center of the stage. Similarly, the {index}`y position`
is measured vertically, in steps above (positive) or below (negative)
the center.)

You can do arithmetic using reporters in the Operators palette:
:::{index} arithmetic
:::

{img alt="image73.png" width="2.11111in"}`images/01-blocks-scripts-and-sprites/image73.png`

The `round` block rounds 35.3905… to 35, and the `+` block adds 100 to that.
(By the way, the `round` block is in the Operators palette, just like `+`,
but in this script it’s a lighter color with black lettering because
Snap<em>!</em> alternates light and dark versions of the palette colors when a
block is nested inside another block from the same palette:

{img alt="image80.png" width="4.85417in"}`images/01-blocks-scripts-and-sprites/image80.png`

This aid to readability is called *zebra coloring.*
A reporter block with its inputs, maybe including other reporter
blocks, such as {inline alt="image81.png"}`images/01-blocks-scripts-and-sprites/image81.png` <!--  width="1.91667in" -->, is called an *expression.*

:::{index} block; predicate
`Predicate` block
hexagonal shape
`repeat until` block
animation
`if` block
reporter `if` block\
Boolean
Boole, George
:::
(sec-predicates-and-conditional-evaluation)=
## Predicates and Conditional Evaluation

Most reporters report either a number, like {inline alt="image82.png"}`./blocks/images/block_reportVariadicSum`,
or a text string, like {inline alt="image83.png"}`./blocks/images/block_reportJoinWords`.
A *predicate* is a special kind of reporter that
always reports true or false. Predicates have a
hexagonal shape: {inline alt="image85.png"}`./blocks/images/block_reportMouseDown`

The special shape is a reminder that predicates don’t generally make sense
in an input slot of blocks that are expecting a number or text. You
wouldn’t say {inline alt="image84.png"}`images/01-blocks-scripts-and-sprites/image84.png`, although (as you can see from the picture) Snap<em>!</em> lets you do it if you really want. Instead, you normally use predicates in
special hexagonal input slots like this one:

{img alt="image86.png" class="image-2x"}`./blocks/images/block_doIf.png`

The C-shaped `if` block runs its input script if (and only
if) the expression in its hexagonal input reports true.

{img alt="image87.png" width="1.59in"}`images/01-blocks-scripts-and-sprites/image87.png`

A really useful block in animations runs its input script *repeatedly* until a predicate
is satisfied:
{img alt="image89.png" width="2.29in"}`images/01-blocks-scripts-and-sprites/image89.png`

If, while working on a project, you want to omit temporarily some commands
in a script, but you don’t want to forget where they belong, you can say

{img alt="image88.png" width="2.28194in"}`images/01-blocks-scripts-and-sprites/image88.png`

Sometimes you want to take the same action whether some condition is
true or false, but with a different input value. For this purpose you
can use the *reporter* `if` block:

{img alt="image90.png" width="4.20833in"}`images/01-blocks-scripts-and-sprites/image90.png`

The technical term for a true or false value is a “Boolean”
value; it has a capital B because it’s named after a person, George
Boole, who developed the mathematical theory of
Boolean values. Don’t get confused; a hexagonal block is a *predicate,*
but the value it reports is a *Boolean.*

Another quibble about vocabulary: Many programming languages reserve the
name “procedure” for Commands (that carry out an
action) and use the name “function” for Reporters and Predicates. In
this manual, a *procedure* is any computational capability, including
those that report values and those that don’t. Commands, Reporters, and
Predicates are all procedures. The words “a Procedure type” are
shorthand for “Command type, Reporter type, or Predicate type.”
:::{index} procedure
:::

If you want to put a *constant* Boolean value in a hexagonal slot
instead of a predicate-based expression, hover the mouse over the block
and click on the control that appears:
:::{index} Boolean constant
:::

{inline alt="image91.png"}`images/01-blocks-scripts-and-sprites/image91` <!--  width="1.375in" --> {inline alt="image92.png"}`images/01-blocks-scripts-and-sprites/image92` <!--  width="1.375in" -->


:::{index} `for` block
variable
squiral
:::
## Variables

Try this script:

{img alt="image93.png" width="1.58333in"}`images/01-blocks-scripts-and-sprites/image93.png`

The input to the move block is an orange oval. To get it there, drag the
orange oval that’s part of the `for` block:

{img alt="image94.png" width="1.88542in"}`images/01-blocks-scripts-and-sprites/image94.png`

The {index}`orange oval` is a *variable:* a symbol that
represents a value. (I took this screenshot before changing the second
number input to the `for` block from the default 10 to 200, and before
dragging in a `turn` block.)
`For` runs its script input repeatedly, just
like `repeat`, but before each repetition it sets the variable
<var>i</var> to a number starting with its first numeric input,
adding 1 for each repetition, until it reaches the second numeric input.
In this case, there will be 200 repetitions, first with <var>i</var>=1, then with
<var>i</var>=2, then <var>i</var>=3, and so on until <var>i</var>=200 for the final repetition. The result
is that each move draws a longer and longer line segment, and that’s why
the picture you see is a kind of spiral. (If you try again with a turn
of 90 degrees instead of 92, you’ll see why this picture is called a
“squiral.”)

The variable <var>i</var> is created by the `for` block, and it can only be used in the
script inside the block’s C-slot. (By the way, if you don’t like the
name <var>i</var>, you can change it by clicking on the orange oval without
dragging it, which will pop up a dialog window in which you can enter a
different name:

{img alt="image95.png" width="3.1875in"}`images/01-blocks-scripts-and-sprites/image95.png`

“<var>I</var>” isn’t a very descriptive name; you might prefer “length” to indicate
its purpose in the script. “<var>I</var>” is traditional because mathematicians
tend to use letters between <var>i</var> and <var>n</var> to represent integer values, but in
programming languages we don’t have to restrict ourselves to
single-letter variable names.)

:::{index} variable watcher
:::

:::{index} variable; global
global variable
Make a variable
`set` block
sprite-local variable
Delete a variable
watcher
:::
### Global Variables

You can create variables “by hand” that aren’t limited to being used
within a single block. At the top of the Variables palette, click the
“Make a variable” button:

{img alt="image97.png" width="2.05208in"}`images/01-blocks-scripts-and-sprites/image97.png`

This will bring up a dialog window in which you can give your variable a
name:

{img alt="image96.png" width="3.1875in"}`images/01-blocks-scripts-and-sprites/image96.png`

The dialog also gives you a choice to make the variable available to all
sprites (which is almost always what you want) or to make it visible
only in the current sprite. You’d do that
if you’re going to give several sprites individual variables *with the
same name,* so that you can share a script between sprites (by dragging
it from the current sprite’s scripting area to the picture of another
sprite in the sprite corral), and the different sprites will do slightly
different things when running that script because each has a different
value for that variable name.

If you give your variable the name “name” then the Variables palette will
look like this:

{img alt="image98.png" width="1.65833in"}`images/01-blocks-scripts-and-sprites/image98.png`

There’s now a “Delete a variable” button, and there’s
an orange oval with the variable name in it, just like the orange oval
in the for block. You can drag the variable into any script in the
scripting area. Next to the oval is a checkbox, initially checked. When
it’s checked, you’ll also see a *variable watcher* on the stage: {inline alt="image99.png" width="1.04167in"}`images/01-blocks-scripts-and-sprites/image99.png`


When you give the variable a value, the orange box in its watcher
will display the value.

How *do* you give it a value? You use the `set` block:

{img alt="image100.png" width="1.92708in"}`images/01-blocks-scripts-and-sprites/image100.png`

Note that you *don’t* drag the variable’s oval into the `set` block! You
click on the downarrow in the first input slot, and you get a menu of
all the available variable names.

If you do choose “For this sprite only”
when creating a variable, its block in the palette looks like this: {inline alt="image101.png" width="0.65833in"}`images/01-blocks-scripts-and-sprites/image101.png`
:::{index} For this sprite only
:::

The *location*-pin icon is a bit of a pun on a sprite-*local* variable. It’s shown only in the palette.
:::{index} location-pin
variable; sprite-local
:::

### Script Variables

In the name example above, our project is going to carry on an
interaction with the user, and we want to remember
their name throughout the project. That’s a good example of a situation
in which a *global* variable (the kind you make
with the “Make a variable” button) is appropriate. Another common
example is a variable called “score” in a game project. But sometimes
you only need a variable temporarily,
during the running of a particular script. In that case you can use the
script variables block to make the
variable:
:::{index} interaction
global variable
variable; script-local
`script variables` block
:::

{img alt="image105.png" width="2.08333in"}`images/01-blocks-scripts-and-sprites/image105.png`

As in the `for` block, you can click on an orange oval in the script
variables block without dragging to change its name. You can also make
more than one temporary variable by clicking on the right arrow at the
end of the block to add another variable oval:

{img alt="image106.png" width="2.08333in"}`images/01-blocks-scripts-and-sprites/image106.png`

:::{index} Renaming variables
:::
### Renaming variables

There are several reasons why you might want to change the name of a
variable:

1.  It has a default name, such as the <var>a</var> in script variables or the
    <var>i</var> in the `for` block.

2.  It conflicts with another name, such as a global variable, that you
    want to use in the same script.

3.  You just decide a different name would be more self-documenting.

In the first and third case, you probably want to change the name
everywhere it appears in that script, or even in all scripts. In the
second case, if you’ve already used both variables in the script before
realizing that they have the same name, you’ll want to look at each
instance separately to decide which ones to rename. Both of these
operations are possible by right-clicking or control-clicking on a
variable oval.

If you right-click on an
orange oval in a context in which the variable is *used,* then you are
able to rename just that one orange oval:

{img alt="image104.png" width="2.08333in"}`images/01-blocks-scripts-and-sprites/image104.png`

If you right-click on the
place where the variable is *defined* (a script variables block, the
orange oval for a global variable in the Variables palette, or an orange
oval that’s built into a block such as the “i” in for), then you are
given two renaming options, “rename” and “rename all.” If you choose
“rename,” then the name is changed only in that one orange oval, as in
the previous case:

{img alt="image103.png" width="2.08333in"}`images/01-blocks-scripts-and-sprites/image103.png`

But if you choose “rename all,” then the name will be changed throughout the scope of the variable
(the script for a script variable, or everywhere for a global variable):

:::{index} variable; transient
memory
:::
### Transient variables

So far we’ve talked about variables with numeric values, or with short text strings such as
someone’s name. But there’s no limit to the amount of information you
can put in a variable; in Chapter IV you’ll see how to use *lists* to
collect many values in one data structure, and in Chapter VIII you’ll
see how to read information from web sites.

{img alt="image102.png" width="2.08333in"}`images/01-blocks-scripts-and-sprites/image102.png`

When you use these capabilities, your project may take up a lot of memory in
the computer. If you get close to the amount of memory available to
Snap<em>!</em>, then it may become impossible to save your project. (Extra
space is needed temporarily to convert from Snap<em>!</em>’s internal
representation to the form in which projects are exported or saved.) If
your program reads a lot of data from the outside world that will still
be available when you use it next, you might want to have values
containing a lot of data removed from memory before saving the project.
To do this, right-click or control-click on the orange oval in the
Variables palette, to see this menu:

{img alt="image114.png" width="1.29in"}`images/01-blocks-scripts-and-sprites/image114.png`

You already know about the rename options, and "help…" displays a help
screen about variables in general. Here we’re interested in the check
box next to transient. If you check it, this variable’s value will not
be saved when you save your project. Of course, you’ll have to ensure
that when your project is loaded, it recreates the needed value and sets
the variable to it.

:::{index} debugging
:::
## Debugging

Snap<em>!</em> provides several tools to help you debug a program. They center
around the idea of *pausing* the running of a script partway through, so
that you can examine the values of variables.

:::{index} button; pause
`hide variable` block
:::
### The pause button

The simplest way to pause a program is manually, by clicking the pause button {inline alt="image116.png"}`images/01-blocks-scripts-and-sprites/image116.png` <!-- width="0.29167in" -->
in the top right corner of the window. While the program is paused, you
can run other scripts by clicking on them, show variables on stage with
the checkbox next to the variable in the Variables palette or with the
`show variable` block, and do all the other
things you can generally do, including modifying the paused scripts by
adding or removing blocks. The {inline alt="image115.png"}`images/01-blocks-scripts-and-sprites/image115.png`
button changes shape too and clicking it again resumes the paused scripts.

:::{index} breakpoint
`pause all` block
conditional breakpoint
:::
(sec-pause-all)=
### Breakpoints: the `pause all` block

The pause button is great if your program seems to be in an infinite loop,
but more often you’ll want
to set a *breakpoint,* a particular point in a script at which you want
to pause. The {inline alt="image117.png"}`./blocks/images/block_doPauseAll` block, near the bottom of the Control palette, can be
inserted in a script to pause when it is run. So, for example, if your
program is getting an error message in a particular block, you could use
`pause all` just before that block to look at the values of variables just
before the error happens.

The `pause all` block turns bright cyan while paused. Also, during the pause, you can right-click on
a running script and the menu that appears will give you the option to
show watchers for temporary variables of the script:

{img alt="image118.png" width="1.88in"}`images/01-blocks-scripts-and-sprites/image118.png`

But what if the block with the error is run many times in a loop, and it
only errors when a particular condition is true — for example, when the value of some
variable is negative, which shouldn’t ever happen. In the iteration
library (see @sec-libraries for more about how to use
libraries) is a breakpoint block that lets you set a *conditional*
breakpoint, and automatically display the relevant variables before pausing. Here’s a sample use of it:

:::{index} hide variable block
`show variable` block
hide and show primitives
:::
### Hide and show variables
{img alt="image119.png" width="1.19444in"}`images/01-blocks-scripts-and-sprites/image119.png`

(In this contrived example, variable <var>zot</var> comes from outside the script but is relevant to its
behavior.) When you continue (with the pause button), the temporary
variable watchers are removed by this breakpoint block before resuming
the script. The breakpoint block isn’t magic; you could alternatively
just put a `pause all` inside an `if`.[^2]

[^2]: The hide variable and show variable block s can also be used to hide and show primitives in the palette.
The pulldown menu doesn’t include primitive blocks, but there’s a generally useful
technique to give a block input values it wasn’t expecting using run or
call: {inline alt="image120.png"}`images/01-blocks-scripts-and-sprites/image120.png`.

In order to use a block as an input this way, you must explicitly put a
ring around it, by right-clicking on it and choosing ringify. More about
rings in @sec-ch06.

:::{index} single stepping
visible stepping
button; visible stepping
visible stepping button
:::
### Visible stepping

Sometimes you’re not exactly sure where the error is, or you don’t
understand how the program got there. To understand better, you’d
like to watch the program as it runs, at human speed rather than
at computer speed. You can do this by
clicking the *visible stepping* button ({inline alt="image121.png"}`images/01-blocks-scripts-and-sprites/image121.png`), <!-- width="0.3in" --> before running a script or
while the script is paused. The button will light up ({inline alt="image123.png"}`images/01-blocks-scripts-and-sprites/image123.png`) <!-- width="0.3in" --> and a speed
control slider {inline alt="image122.png"}`images/01-blocks-scripts-and-sprites/image122.png` <!-- width="0.54563in" --> will appear in the toolbar. When you start or continue
the script, its blocks and input slots will light up cyan one at a time:

{img alt="image124.png" width="0.54563in"}`images/01-blocks-scripts-and-sprites/image124.png`

In this simple example, the inputs to the blocks are constant values,
but if an input were a more complicated expression involving several
reporter blocks, each of those would light up as they are called. Note
that the input to a block is evaluated before the block itself is
called, so, for example, the 100 lights up before the move.

The speed of stepping is controlled by the slider. If you move the
slider all the way to the left, the speed is zero, the pause button
turns into a step button {inline alt="image134.png"}`images/01-blocks-scripts-and-sprites/image134.png`,
and the script takes a single step each time you push it. The name for this is *single stepping.*
:::{index} slider; stepping speed
:::

If several scripts that are visible in the scripting area are running at
the same time, all of them are stepped in parallel. However, consider
the case of two repeat loops with different numbers of blocks. While not
stepping, each script goes through a complete cycle of its loop in each
display cycle, despite the difference in the length of a cycle. In order
to ensure that the visible result of a program on the stage is the same
when stepped as when not stepped, the shorter script will wait at the
bottom of its loop for the longer script to catch up.

When we talk about custom blocks in @sec-ch03, we’ll have more to say
about visible stepping as it affects those blocks.

:::{index} `pen trails` block
`if else` reporter block
index variable
`script variables` block
newline character
:::
## Etcetera

This manual doesn’t (yet) explain every block in detail. There are many more
motion blocks, sound blocks, costume and graphics effects blocks, and so
on. If you would like to find information on specific blocks, go to @sec-all-blocks. You can also learn what they all do by experimentation, and by
reading the “help screens” that you can get by right-clicking or
control-clicking a block and selecting “`help…`” from the menu that
appears. If you forget what palette (color) a block is, but you remember
at least part of its name, type {keyboard}`control-F` and enter the name in the text block that appears in the palette area.


:::{index} pen vectors block
`write` block
`for` block
local variables
false
`false` block
`true` block
true
graphics effect
JavaScript
pen down? block
at\` block
screen pixel
RGBA option
`is \_ a \_ ?` block
stage blocks
type
`set flag` block
`split` block
:::
(sec-primitives-not-in-scratch)=
Here are some of the primitive blocks that don’t exist in Scratch:

{inline alt="image135.png"}`images/01-blocks-scripts-and-sprites/image135.png` reports, a new costume consisting of everything that’s drawn on the stage by any sprite. Right-clicking the block in the scripting area gives the option to change it to {inline alt="image136.png"}`images/01-blocks-scripts-and-sprites/image136.png` if vector logging is enabled. See [Log pen vectors](#sec-para-log-pen-vectors).

{inline alt="image137.png"}`images/01-blocks-scripts-and-sprites/image137.png` Print
characters in the given point size on the stage, at
the sprite’s position and in its direction. The sprite moves to the end
of the text. (That’s not always what you want, but you can save the
sprite’s position before using it, and sometimes you need to know how
big the text turned out to be, in turtle steps.) If the pen is down, the
text will be underlined.

{inline alt="image138.png"}`images/01-blocks-scripts-and-sprites/image138`
Takes a sprite as input. Like stamp except that the costume is stamped onto the selected sprite instead of onto the stage. (Does nothing if the current sprite doesn’t overlap the chosen sprite.)

{inline alt="image139.png"}`images/01-blocks-scripts-and-sprites/image139`
Takes a sprite as input. Erases from that sprite’s costume the area that overlaps with the current sprite’s costume. (Does not affect the costume in the chosen sprite’s wardrobe, only the copy currently visible.)

{inline alt="image142.png"}`images/01-blocks-scripts-and-sprites/image142` See the "generic when" hat block described in footnote [^1].

{inline alt="image141.png"}`images/01-blocks-scripts-and-sprites/image141` See @sec-pause-all.

{inline alt="image140.png" class="tall"}`images/01-blocks-scripts-and-sprites/image140` Runs only this script until finished. In the Control palette even though it’s gray.

{inline alt="image143.png"}`images/01-blocks-scripts-and-sprites/image143` <!--  width="1.71in" --> Reporter version of the `if/else` primitive command block. Only one of the two branches is evaluated, depending on the value of the first input.

{inline alt="image144.png"}`images/01-blocks-scripts-and-sprites/image144` <!--  width="1.83in" --> Looping block like `repeat` but with an index variable.

{inline alt="image145.png"}`images/01-blocks-scripts-and-sprites/image145` <!--  width="1.37986in" alt="Graphical user interface, application, logo Description automatically generated" / --> Declare local variables in a script.

{inline alt="image148.png"}`images/01-blocks-scripts-and-sprites/image148` See @sec-ch09.

{inline alt="image146.png"}`images/01-blocks-scripts-and-sprites/image146` reports the value of a graphics effect.

{inline alt="image147.png"}`images/01-blocks-scripts-and-sprites/image147` Constant true or false value. See @sec-predicates-and-conditional-evaluation.

{inline alt="image149.png" class="image-2x"}`images/01-blocks-scripts-and-sprites/image149.png`

{inline alt="image153.png"}`images/01-blocks-scripts-and-sprites/image153` Create a primitive using JavaScript. (This block is disabled by default; the user must check “Javascript extensions” in the setting menu *each time* a project is loaded.)

::::{grid} 2

:::{grid-item}
{inline alt="image150.png" class="image-1-5x"}`images/01-blocks-scripts-and-sprites/image150.png`
:::

:::{grid-item}
The `at` block lets you examine the screen pixel directly behind the rotation center of a sprite,
the mouse, or an arbitrary (x,y) coordinate pair dropped onto the second
menu slot. The first five items of the left menu let you examine the
color visible at the position. (The "RGBA" option
reports a list.) The "sprites" option reports a list of all sprites,
including this one, any point of which overlaps this sprite's rotation
center (behind or in front). This is a hyperblock with respect to its
second input.
:::
::::

<!-- This needs 2 columns ??? -->
::::{grid} 2

:::{grid-item}
{inline alt="image154.png" class="image-1-5x"}`images/01-blocks-scripts-and-sprites/image154.png`
:::
:::{grid-item}
Checks the data type of a value.
:::
::::

<!-- These two need to be remade as text -->
::::{grid} 2

:::{grid-item}
{inline alt="image151.png" class="image-1-5x"}`images/01-blocks-scripts-and-sprites/image151.png`
:::
:::{grid-item}
{inline alt="image152.png" class="image-1-5x"}`images/01-blocks-scripts-and-sprites/image152.png`
:::
::::

:::{index} whitespace
carriage return character
CSV format
JSON format
:::

(sec-split-block)=
::::{grid} 2
:::{grid-item}
{inline alt="image155.png" class="image-2x"}`images/01-blocks-scripts-and-sprites/image155.png`
:::

:::{grid-item}
Turn the text into a list, using the second input as the delimiter between items. The default
delimiter, indicated by the brown dot in the input slot, is a single
space character. "Letter" puts each character of the text in its own
list item. "Word" puts each word in an item. ( Words
are separated by any number of consecutive space, tab, carriage return,
or newline characters.) "Line" is a newline character (0xa); "tab" is a {index}`tab character` (0x9);
"cr" is a carriage return (0xd). "Csv" and "json" split formatted text
into lists of lists; see @sec-csv. "Blocks"
takes a script as the first input, reporting a list structure
representing the structure of the script. See Chapter XI.
:::
::::

{inline alt="image170.png"}`images/01-blocks-scripts-and-sprites/image170` For lists,
reports true only if its two input values are the
very same list, so changing an item in one of them is visible in the
other. (For `=`, lists that look the same are the same.) For text strings,
uses case-sensitive comparison, unlike `=`, which is case-independent.
:::{index} identical to
:::

{inline alt="image171.png"}`images/01-blocks-scripts-and-sprites/image171` These *hidden* blocks can be found with the relabel option
 of any dyadic arithmetic block. They’re hidden
partly because writing them in Snap<em>!</em> is a good, pretty easy
programming exercise. Note: the two inputs to `atan2`
are Δ*x* and Δ*y* in that order, because we measure angles clockwise
from north. `max` /index{max block} and `min` /index{min block} are *variadic;* by clicking the arrowhead, you
can provide additional inputs.
:::{index} relabel option
`atan2` block
:::

{inline alt="image177.png"}`images/01-blocks-scripts-and-sprites/image177` {inline alt="image178.png"}`images/01-blocks-scripts-and-sprites/image178` {inline alt="image179.png"}`images/01-blocks-scripts-and-sprites/image179`

Similarly, these hidden predicates can be found by relabeling the relational predicates.
:::{index} `≤` block
:::

### Metaprogramming (see @sec-ch11)

{img alt="image172.png" width="0.88in"}`images/01-blocks-scripts-and-sprites/image172.png`

These blocks support *metaprogramming,* which means manipulating blocks
and scripts as data. This is not the same as manipulating procedures
(see @sec-ch06), which are what the blocks *mean;* in metaprogramming
the actual blocks, what you see on the screen, are the data. This
capability is new in version 8.0.

:::{index} broadcast block
of block (operators)
:::

### First class list blocks (see @sec-ch04):

<!-- TODO: welp. this needs to be remade -->
{img alt="image173.png" width="0.85in"}`images/01-blocks-scripts-and-sprites/image173.png`

`Numbers from` will
count up or down.
:::{index} numbers from block
:::

{inline alt="image224.png"}`images/01-blocks-scripts-and-sprites/image224` {inline alt="image225.png"}`images/01-blocks-scripts-and-sprites/image225`
report the sprite or mouse position as a two-item
vector (x,y).
:::{index} position block
:::

**First class procedure blocks (see @sec-ch06):**
 {img alt="image226.png" width="5.99in"}`images/01-blocks-scripts-and-sprites/image226.png`

**First class continuation blocks (see @sec-ch10):**
 {img alt="image227.png" width="5.99in"}`images/01-blocks-scripts-and-sprites/image227.png`

**First class sprite, costume, and sound blocks (see @sec-ch07):**

 {img alt="image228.png" width="5.99in"}`images/01-blocks-scripts-and-sprites/image228.png`

 {img alt="image229.png" width="5.99in"}`images/01-blocks-scripts-and-sprites/image229.png`

Object is a hyperblock.

**Scenes:**

{inline alt="image280.png" class="image-2x"}`images/01-blocks-scripts-and-sprites/image280.png`

The major new feature of version 7.0 is *scenes:* A project can include
within it sub-projects, called scenes, each with its own stage, sprites,
scripts, and so on. This block makes another scene active, replacing the
current one.
:::{index} scenes
:::

Nothing is automatically shared between scenes: no sprites, no blocks,
no variables. But the old scene can send a message to the new one, to
start it running, with optional payload as in broadcast (See @sec-broadcast).

{inline alt="image282.png" class="image-4x"}`images/01-blocks-scripts-and-sprites/image282.png`

In particular, you can say

{inline alt="image281.png" class="image-4x"}`images/01-blocks-scripts-and-sprites/image281.png`

if the new scene expects to be started with a green flag signal.

***These aren’t new blocks but they have a new feature:***
These accept two-item (x,y) lists
 as input, and have extended menus (also
including other sprites):
:::{index} points as inputs
two-item (x,y) lists
`to` block
:::

{img alt="image283.png" width="3.13in"}`images/01-blocks-scripts-and-sprites/image283.png`

“Center” means the center of the stage, the
point at (0,0). “Direction” is in the point in direction sense, the
direction that would leave this sprite pointing toward another sprite,
the mouse, or the center. “Ray length” is the distance from the center
of this sprite to the nearest point on the other sprite, in the current
direction.
:::{index} center of the stage
:::

{inline alt="image284.png" class="image-4x"}`images/01-blocks-scripts-and-sprites/image284.png`
The {index}`\`stop\` block<`stop` block>` has two extra menu choices. `Stop this block` is used inside the definition of a custom block to stop just this
invocation of this custom block and continue the script that called it.
`Stop all` but this script is good at the end of a game to stop all the
game pieces from moving around, but keep running this script to provide
the user’s final score. The last two menu choices add a tab at the
bottom of the block because the current script can continue after it.

{inline alt="image285.png" class="image-2x"}`images/01-blocks-scripts-and-sprites/image285.png`
The new “pen trails” option is true if the sprite is touching any drawn
or stamped ink on the stage. Also, `touching` will
not detect hidden sprites, but a hidden sprite can use it to detect
visible sprites.
:::{index} touching block
:::

{inline alt="image305.png"}`images/01-blocks-scripts-and-sprites/image305` <!--  width="2.43333in" --> The `video on` block has a {index}`snap option` that takes a
snapshot and reports it as a costume. It is hyperized with respect to its second input.
:::{index} video block
:::

::::{grid} 2

:::{grid-item}
{inline alt="image306.png"}`images/01-blocks-scripts-and-sprites/image306`
:::

:::{grid-item}
{inline alt="image304.png"}`images/01-blocks-scripts-and-sprites/image304` The "neg" option is a monadic negation operator
, equivalent to "lg" is log<sub>2</sub>.
"id" is the identity function, which reports its input. "sign" reports 1
for positive input, 0 for zero input, or -1 for negative input.

:::
::::
:::{index} neg option
`length of text` block
negation operator
`set background` block
:::

<!--::: {.callout-tip} -->
<!-- ## Two Different Length Of Blocks -->

The {inline alt="length of text block"}`./blocks/images/block_reportTextAttribute` name was changed to clarify it is different from {inline alt="length of text block"}`./blocks/images/block_reportListAttribute`
<!--::: -->

{img alt="image308.png" width="1.42in"}`images/01-blocks-scripts-and-sprites/image308.png`

`+` and `×` are *variadic*: they take two or more inputs. If
you drop a list on the arrowheads, the block name
changes to `sum` or `product`.

::::{grid} 2

:::{grid-item}
{img alt="image309.png"}`images/01-blocks-scripts-and-sprites/image309.png`
:::

:::{grid-item}
Extended mouse interaction events, sensing
clicking, dragging, hovering, etc. The "stopped" option triggers when
all scripts are stopped, as with the stop button; it is useful for
robots whose hardware interface must be told to turn off motors. A `when I am stopped` script can run only for a
limited time.
:::
::::
:::{index} when I am block
when I am stopped script
:::

(para-broadcast)=
::::{grid} 2

:::{grid-item}
{img alt="image310.png"}`images/01-blocks-scripts-and-sprites/image310.png`
:::

:::{grid-item}
{index}`Extended broadcast`: Click the right arrowhead to direct the message to a single sprite or the stage. Click again to add any value as a payload to the message.
:::
::::

::::{grid} 2
:::{grid-item}
{inline alt="image311.png" class="image-4x"}`images/01-blocks-scripts-and-sprites/image311.png`
:::

:::{grid-item}
Extended `when I receive`: Click the right
arrowhead to expose a script variable (click on it to change its name,
like any script variable) that will be set to the data of a matching
broadcast. If the first input is set to "any message," then the data
variable will be set to the message, if no payload is included with the
broadcast, or to a two-item list containing the message and the payload.
:::
::::
:::{index} when I receive block
:::

{inline alt="image312.png" class="image-2x"}`images/01-blocks-scripts-and-sprites/image312.png`

::::{grid} 2
:::{grid-item}
{inline alt="image355.png" class="image-2x"}`images/01-blocks-scripts-and-sprites/image355.png`
:::

:::{grid-item}
If the input is set to “any key,” then a right arrowhead appears:
{inline alt="image357.png" class="image-inline-tall"}`images/01-blocks-scripts-and-sprites/image357.png` and if you click it,
a script variable key is created whose value is the key that was
pressed. (If the key is one that’ represented in the input menu by a
word or phrase, e.g., “enter” or “up arrow,” then the value of key
will be that word or phrase, *except for* the space character, which
is represented as itself in key.)

{img alt="image356.png" class="image-4x" width="2.25in"}`images/01-blocks-scripts-and-sprites/image356.png`
:::
::::

The RGB(A) option accepts a single number, which
is a grayscale value 0-255; a two-number list, grayscale plus opacity
0-255; a three-item RGB list, or a four-item RGBA list.
:::{index} set pen block
:::

<!-- TODO: Images like this should have index entries defined after this image. -->
(sec-pen-hue-block-options)=
{img alt="image358.png" width="2.41in"}`images/01-blocks-scripts-and-sprites/image358.png`

:::{index} `of` block (sensing)
`ask and wait` block
:::

(sec-ask-lists)=
### Using Lists with the Ask Block
These ask features and more in the Menus
library.

{img alt="image359.png" width="0.60in"}`images/01-blocks-scripts-and-sprites/image359.png`

{img alt="image360.png" width="2.25in"}`images/01-blocks-scripts-and-sprites/image360.png`

{img alt="image361.png" width="2.25in"}`images/01-blocks-scripts-and-sprites/image361.png`

{img alt="image362.png" width="4.55in"}`images/01-blocks-scripts-and-sprites/image362.png`

::::{grid} 2
:::{grid-item}
{img alt="image363.png" class="image-2x"}`images/01-blocks-scripts-and-sprites/image363.png`
:::

:::{grid-item}
(sec-image-list-of-attributes)=
The `of` block has an extended menu of
attributes of a sprite. Position reports an (x,y) vector. Size reports
the percentage of normal size, as controlled by the set size block in
the Looks category. Left, right, etc. report the stage coordinates of
the corresponding edge of the sprite's bounding box. Variables reports a
list of the names of all variables in scope (global, sprite-local, and
script variables if the right input is a script.)
:::
::::

:::{index} `for` block
`item 1 of stream` block
`all but first of stream` block
`letter (1) of (world)` block
visual representation of a sentence
`bar chart` block
conditional library
conditional library; multiple-branch
`setting` block
infinite precision integer library
Libraries… option
:::

(sec-libraries)=
## Libraries

There are several collections of useful procedures that aren’t Snap<em>!</em>
primitives, but are provided as libraries. To include a library in your
project, choose the Libraries… option in the
file ({inline alt="file menu icon"}`images/01-blocks-scripts-and-sprites/image384`) menu.


{img alt="The import libraries dialog" width="3.27in"}`images/01-blocks-scripts-and-sprites/image385.png`

<!-- TODO: This is out of date. It is somewhat redudant with chapter 12. -->
The library menu is divided into five broad categories. The first is,
broadly, utilities: blocks that might well be primitives. They might be
useful in all kinds of projects.

The second category is blocks related to media computation: ones that
help in dealing with costumes and sounds (a/k/a Jens libraries). There
is some overlap with “big data” libraries, for dealing with large lists
of lists.

The third category is, roughly, specific to non-media applications
(a/k/a Brian libraries). Three of them are imports from other
programming languages: words and sentences from Logo, array functions
from APL, and streams from Scheme. Most of the others are to meet the
needs of the BJC curriculum.

The fourth category is major packages (extensions) provided by users.

The fifth category provides support for hardware devices such as robots,
through general interfaces, replacing specific hardware libraries in
versions before 7.0.

When you click on the one-line description of a library, you are shown
the actual blocks in the library and a longer explanation of its
purpose. You can browse the libraries to find one that will satisfy your
needs.

The libraries and their contents may change, but as of this writing the
{index}`list library` has these blocks:

{img alt="image387.png" class="image-1-5x"}`images/01-blocks-scripts-and-sprites/image387.png`

(The lightning bolt (⚡️) before the name in several of these
blocks means that they use compiled HOFs or JavaScript primitives to achieve
optimal speed. They are officially considered experimental.) `Remove duplicates from` reports a list in
which no two items are equal. The `sort` block takes a
list and a two-input comparison predicate, such as `<`, and reports a
list with the items sorted according to that comparison. The `assoc` block
is for looking up a key in an *association list:* a
list of two-item lists. In each two-item list, the first is a *key* and
the second is a *value.* The inputs are a key and an association list;
the block reports the first key-value pair whose key is equal to the
input key.
:::{index} ⚡️ (lightning bolt)
`remove duplicates from` block
`sort` block
`assoc` block
dictionary
association list
:::

`For each item` is a variant of the primitive
version that provides a \# variable containing the
position in the input list of the currently considered item. `Multimap`
 is a version of `map` that allows multiple list
inputs, in which case the mapping function must take as many inputs as
there are lists; it will be called with all the first items, all the
second items, and so on. `Zip` takes any number of lists as inputs; it
reports a list of lists: all the first items, all the second items, and
so on. The `no-name` identity function reports its input.
:::{index} `for each item` block
`#` variable
`multimap` block
:::

`Sentence` and `sentence ➔ list`
 are borrowed from the [word and sentence library](#word-and-sentence-library) to serve as a variant of append that accepts non-lists
as inputs. `Printable` takes a list structure of any depth as input and
reports a compact representation of the list as a text string.
:::{index} `sentence` block
`sentence ➔ list` block
:::

The iteration, {index}`composition library` has these
blocks:

{img alt="image388.png" width="1.68889in"}`images/01-blocks-scripts-and-sprites/image388.png`
{img alt="image389.png" width="1.04444in"}`images/01-blocks-scripts-and-sprites/image389.png`

`Catch` and `throw` provide a nonlocal exit facility. You can drag the tag from a `catch` block to a `throw` inside
its C-slot, and the throw will then jump directly out to the matching
catch without doing anything in between.
:::{index} `catch` block
`throw` block
:::

`If do and pause all` is for setting a
breakpoint while debugging code. The idea is to put show variable blocks
for local variables in the C-slot; the watchers will be deleted when the
user continues from the pause.
:::{index} `if do and pause all` block
:::

`Ignore` is used when you need to call a reporter but
you don’t care about the value it reports. (For example, you are writing
a script to time how long the reporter takes.)
:::{index} `ignore` block
:::

The `cascade` blocks take an initial value and call
a function repeatedly on that value, *f*(*f*(*f*(*f*…(*x*)))).
:::{index} cascade blocks
:::

The `compose` block takes two functions and reports
the function *f*(*g*(*x*)).
:::{index} `compose` block
:::

The first three repeat blocks are variants of the primitive `repeat until` block,
giving all four combinations of whether the first test happens before or
after the first repetition, and whether the condition must be true or
false to continue repeating. The last repeat block is like the `repeat`
primitive, but makes the number of repetitions so far available to the
repeated script. The next two blocks are variations on `for`: the first allows an explicit step instead of using ±1, and the
second allows any values, not just numbers; inside the script you say {inline alt="image390.png"}`images/01-blocks-scripts-and-sprites/image390` <!-- width="3.15278in" -->
replacing the grey block in the picture with an expression to give the next
desired value for the loop index.
:::{index} repeat blocks
:::

`Pipe` allows reordering a nested composition with a left-to-right one:
:::{index} `pipe` block
:::

{img alt="image392.png" width="3.70972in"}`images/01-blocks-scripts-and-sprites/image392.png` {img alt="image391.png" width="3.44097in"}`images/01-blocks-scripts-and-sprites/image391.png`


:::{index}
stream list
`in front of stream` block
`map over stream` block
`show stream` block
`Stream` block
`sieve` block
`Stream with numbers from` block
:::
(sec-stream-library)=
The {index}`stream library` has these blocks:

{img alt="image393.png" width="3.16111in"}`images/01-blocks-scripts-and-sprites/image393.png`

*Streams* are a special kind of list whose items are not computed until they are needed. This makes
certain computations more efficient, and also allows the creation of
lists with infinitely many items, such as a list of all the positive
integers. The first five blocks are stream versions of the list blocks.

`in front of`, `item 1 of`, `all but first of`, `map`, and `keep`. `Show stream`
 takes a stream and a number as inputs, and
reports an ordinary list of the first *n* items of the stream. `Stream`
 is like the primitive list; it makes a finite
stream from explicit items. `Sieve` is an example
block that takes as input the stream of integers starting with 2 and
reports the stream of all the prime numbers. `Stream with numbers from` is
 like the numbers from block for
lists, except that there is no endpoint; it reports an infinite stream
of numbers.


:::{index} sentence library
`word ➔ list` block
:::
(word-and-sentence-library)=
The **word and sentence library** has these blocks:

<!-- TODO: Index Entries for all these blocks -->
{img alt="image394.png" width="1.68in"}`images/01-blocks-scripts-and-sprites/image394.png`

This library has the goal of recreating the Logo approach to handling text:
A text isn’t best viewed as a string of characters, but rather as a *sentence*, made of *words*,
each of which is a string of *letters.* With a few specialized
exceptions, this is why people put text into computers: The text is
sentences of natural (i.e., human) language, and the emphasis is on
words as constitutive of sentences. You barely notice the letters of the
words, and you don’t notice the spaces between them at all, unless
you’re proof-reading. (Even then: Proofreading is *diffciult,* because
you see what you expect to see, what will make the snetence make sense,
rather than the misspelling in front of of your eyes.) Internally, Logo
stores a sentence as a list of words, and a word as a string of letters.

:::{index} `all but first` blocks
:::

Inexplicably, the designers of Scratch chose to abandon that tradition,
and to focus on the representation of text as a string of characters.
The one vestige of the {index}`Logo tradition` from which
Scratch developed is the block named "`letter (1) of (world)`", rather than "`character (1) of (world)`". Snap<em>!</em> inherits its text handling from Scratch.

In Logo, the visual representation of a sentence (a list of words) looks like a natural
language sentence: a string of words with spaces between them. In
Snap<em>!</em>, the visual representation of a list looks nothing at all like
natural language. On the other hand, representing a sentence as a string
means that the program must continually re-parse the text on every
operation, looking for spaces, treating multiple consecutive spaces as
one, and so on. Also, it’s more convenient to treat a sentence as a list
of words rather than a string of words because in the former case you
can use the higher order functions `map`, `keep`, and `combine` on them. This
library attempts to be agnostic as to the internal representation of
sentences. The sentence selectors accept any combination of lists and
strings; there are two sentence constructors, one to make a string (join
words) and one to make a list (sentence).

The selector names come from Logo, and should be self-explanatory.
However, because in a block language you don’t have to type the block
name, instead of the terse butfirst or the cryptic bf we spell out “all
but first of” and include “word” or “sentence” to indicate the intended
domain. There’s no first letter of block because `letter 1 of` serves that
need. `Join words` (the sentence-as-string constructor) is like the
primitive `join` except that it puts a space in the reported value between
each of the inputs. `Sentence` (the List-colored sentence-as-list
constructor) accepts any number of inputs, which can be words,
sentences-as-lists, or sentences-as-strings. (If inputs are lists of
lists, only one level of flattening is done.) `Sentence` reports a list of
words; there will be no empty words or words containing spaces. The four
blocks with right-arrows in their names
convert back and forth between text strings (words or sentences) and
lists. (Splitting a word into a list of letters is unusual unless you’re
a linguist investigating orthography.) `Printable`
takes a list (including a deep list) of words as input and reports a
text string in which parentheses are used to show the structure, as in
Lisp/Scheme.

:::{index} list ➔ sentence block
`printable` block
pixels library
:::

:::{index} `snap` block
:::

(sec-pixels-library)=
The **pixels library** has one block:

{img alt="image395.png" width="0.8in" class="image-2x"}`images/01-blocks-scripts-and-sprites/image395.png`

Costumes are first class data in Snap<em>!</em>. Most of the processing of
costume data is done by primitive blocks in the Looks category. (See page
@sec-media-computation-with-costumes).) This library provides Snap<em>!</em>,
which takes a picture using your computer’s camera and reports it as a costume.

The bar charts library has these blocks:
:::{index} bar charts library
:::

{img alt="image396.png" width="3.43056in"}`images/01-blocks-scripts-and-sprites/image396.png`

`Bar chart of table` takes a table (typically from a CSV data set) as input and
reports a summary of the table grouped by the field in the specified
column number. The remaining three inputs are used only if the field
values are numbers, in which case they can be grouped into buckets
(e.g., decades, centuries, etc.). Those inputs specify the smallest and
largest values of interest and, most importantly, the width of a bucket
(10 for decades, 100 for centuries). If the field isn't numeric, leave
these three inputs empty or set them to zero. Each string value of the
field is its own bucket, and they appear sorted alphabetically.

`Bar chart of table` reports a new table with three columns. The first column
contains the bucket name or smallest number. The second column contains
a nonnegative integer that says how many records in the input table fall
into this bucket. The third column is a subtable containing the actual
records from the original table that fall into the bucket. `Plot bar chart`
 takes the table reported by bar chart
and graphs it on the stage, with axes labelled appropriately. The
remaining blocks are helpers for those.
:::{index} plot bar chart block
:::

If your buckets aren't of constant width, or you want to group by some
function of more than one field, load the "Frequency Distribution
Analysis" library instead.

The multi-branched conditional library has these blocks:

{img alt="image397.png" width="1.85in"}`images/01-blocks-scripts-and-sprites/image397.png`

The `catch` and `throw` blocks duplicate ones in the iteration library, and are
included because they are used to implement the others. The `cases: if/then` block
 sets up a multi-branch conditional, similar to cond
in Lisp or switch in C -family
languages. The first branch is built into the cases block; it consists
of a Boolean test in the first hexagonal slot and an action script, in
the C-slot, to be run if the test reports true. The remaining branches
go in the variadic hexagonal input at the end; each branch consists of
an `else if` block, which includes the Boolean test
and the corresponding action script, except possibly for the last
branch, which can use the unconditional {index}`\`else\` block<`else` block>`.
As in other languages, once a branch succeeds, no other branches are
tested.
:::{index} cases block
cond in Lisp
switch in C
`else if` block
:::

:::{index} variadic library
`sum` block
`all of` block
`any of` block
:::
### The Variadic Library

The variadic library has these blocks:

{img alt="image398.png" width="1.19653in"}`images/01-blocks-scripts-and-sprites/image398.png`

These are versions of the associative
operators `and`, and `or` that take any number of inputs
instead of exactly two inputs. As with any variadic input,
you can also drop a list of values onto the arrowheads
instead of providing the inputs one at a time
As of version 8.0, the arithmetic operators sum, product, minimum, and
maximum are no longer included, because the primitive operators `+` `x`,
`min`, and `max` are themselves variadic.

:::{index} `set pen` block
HSL color
X11/W3C color names
`color from` block
`from color` block
:::
### The Color and Crayons Library
The colors and {index}`crayons library` has these blocks:

It is intended as a more powerful replacement for the primitive `set pen`
block, including *first class color* support; `HSL color` specification as a better alternative to the HSV
that Snap<em>!</em> inherits from JavaScript; a “{index}`fair hue`”
scale that compensates for the eye’s grouping a wide range of light
frequencies as green while labelling mere slivers as orange or yellow;
the `X11/W3C standard color names`; `RGB in
hexadecimal`; a linear color scale (as in the old days, but better) based
on fair hues and including shades (darker colors) and grayscale. Another
linear scale is a curated set of 100 “crayons,” explained further on the
next page.

{img alt="image412.png" width="1.13333in"}`images/01-blocks-scripts-and-sprites/image412.png`

Colors are created by the {inline alt="image414.png"}`images/01-blocks-scripts-and-sprites/image414` <!--  width="0.95in" --> block (for direct user selection), the `color from`
to specify a color numerically, or by {inline alt="image413.png"}`images/01-blocks-scripts-and-sprites/image413` <!-- width="1.13333in" -->, which
reports the color currently in use by the pen. The `from color` block
reports names or numbers associated with a color:

{inline alt="image411.png" class="image-4x"}`images/01-blocks-scripts-and-sprites/image411.png` <!--  width="0.95in" -->

Colors can be created from other colors:
{img alt="image415.png" width="4.83333in"}`images/01-blocks-scripts-and-sprites/image415.png`
:::{index} mix colors block
:::

The three blocks with pen in their names are improved versions of
primitive Pen blocks. In principle `set pen`, for
example, could be implemented using a (hypothetical) `set pen` to color
composed with the `color from` block, but in fact `set pen` benefits from
knowing how the pen color was set in its previous invocation, so it’s
implemented separately from `color from`. Details in Appendix A.

The recommended way to choose a color is from one of two linear scales: the
continuous *color numbers* and the discrete *crayons:*

{img alt="image416.png" width="7.5in"}`images/01-blocks-scripts-and-sprites/image416.png`

{img alt="image417.png" width="7.5in"}`images/01-blocks-scripts-and-sprites/image417.png`

{index}`Color numbers` are based on *fair hues,* a modification
of the spectrum (rainbow) hue scale that devotes less space to green and
more to orange and yellow, as well as promoting brown to a real color.
Here is the normal hue scale, for reference:

{img alt="image418.png" width="4in"}`images/01-blocks-scripts-and-sprites/image418.png`

Here is the fair hue scale:

{img alt="image419.png" width="4in"}`images/01-blocks-scripts-and-sprites/image419.png`

Here is the color number scale:

{img alt="image416.png" width="5in"}`images/01-blocks-scripts-and-sprites/image416.png`

(The picture is wider so that pure spectral colors line up with the fair
hue scale.)

 And
here are the 100 crayons:
:::{index} crayons
:::

{img alt="image417.png" width="5in"}`images/01-blocks-scripts-and-sprites/image417.png`

The `color from` block, for example, provides different pulldown menus
depending on which scale you choose:

{img alt="image410.png" width="2.41667in"}`images/01-blocks-scripts-and-sprites/image410.png`

 You can also
type the crayon name:

{img alt="image420.png" width="2.41667in"}`images/01-blocks-scripts-and-sprites/image420.png`

There are many scales:

{img alt="image427.png" width="4.29167in"}`images/01-blocks-scripts-and-sprites/image427.png`

The white slot at the end of some of the blocks has two purposes. It can
be used to add a transparency to a color (0=opaque,
100=transparent):
:::{index} transparency
:::

{img alt="image428.png" width="4.29167in"}`images/01-blocks-scripts-and-sprites/image428.png`

or it can be expanded to enter three or four numbers for a vector
directly into the block, so these are equivalent:

{img alt="image429.png" width="4.29167in"}`images/01-blocks-scripts-and-sprites/image429.png`

But note that a transparency number in a four-number RGBA vector is on
the scale 255=opaque, 0=transparent, so the following are *not*
equivalent:

{img alt="image430.png"}`images/01-blocks-scripts-and-sprites/image430.png`

`Set pen crayon to` provides the equivalent of a box of 100 crayons. They
are divided into color groups, so the menu in the set pen crayon to
input slot has submenus. The colors are
chosen so that starting
from crayon 0, `change pen crayon by` 10 rotates through an interesting,
basic set of ten colors:
:::{index} set pen to crayon block
:::

{img alt="image440.png" width="4.37in"}`images/01-blocks-scripts-and-sprites/image440.png`

Using `change pen crayon by` 5 instead gives ten more colors, for a total of 20:

{img alt="image441.png" width="4.36in"}`images/01-blocks-scripts-and-sprites/image441.png`

(Why didn’t we use the colors of the 100-crayon Crayola™ box? A few
reasons, one of which is that some Crayola colors aren’t representable
on RGB screens. Some year when you have nothing else to do, look up
“color space” on Wikipedia. Also “crayon.” Oh, it’s deliberate that
`change pen crayon by` 5 doesn’t include white, since that’s the usual
stage background color. White is crayon 14.) Note that crayon 43 is
“Variables”; all the standard block colors are included.

See Appendix A (@sec-crayons-and-color-numbers) for more information.

The **crayon library** has only the crayon features,
without the rest of the colors package.
:::{index} crayon library
:::

{img alt="image442.png" width="1.51in"}`images/01-blocks-scripts-and-sprites/image442.png`

The catch errors library has these blocks:
:::{index} catch errors library
:::

{img alt="image444.png" width="3.04in"}`images/01-blocks-scripts-and-sprites/image444.png`

The `safely try` block
 allows you to handle errors that happen when
your program is run within the program, instead of stopping the script
with a red halo and an obscure error message. The block runs the script
in its first C-slot. If it finishes without an error, nothing else
happens. But if an error happens, the code in the second C-slot is run.
While that second script is running, the variable {inline alt="image443.png"}`images/01-blocks-scripts-and-sprites/image443.png` <!-- width="0.43056in" --> contains the text of
the error message that would have been displayed if you weren’t catching
the error. The {index}`\`error\` block<`error` block>` is sort of the opposite:
it lets your program *generate* an error message, which will be
displayed with a red halo unless it is caught by `safely try`. `Safely try reporting` is the reporter version of `safely try`.
:::{index} safely try block
:::

The text costumes library has only two
blocks:
:::{index} text costume library
:::

 {img alt="image446.png" width="1.92in"}`images/01-blocks-scripts-and-sprites/image446.png`
 {inline alt="image447.png" class="image-4x"}`images/01-blocks-scripts-and-sprites/image447.png` <!-- width="3.25972in" -->

`Costume from text`
reports a costume that can be used with
the `switch to costume` block to make a
button:
:::{index} costume from text block
:::

{img alt="image445.png" width="0.53472in"}`images/01-blocks-scripts-and-sprites/image445.png`

`Costume with background` reports a
costume made from another costume by coloring its background, taking a
color input like the `set pen color to RGB(A)` block and a number of
turtle steps of padding around the original costume. These two blocks
work together to make even better buttons:
:::{index} costume with background block
:::

{img alt="image448.png" width="5.51in"}`images/01-blocks-scripts-and-sprites/image448.png`

The text to speech library has these
blocks:
:::{index} speech synthesis library
:::

{img alt="image449.png" width="2.275in"}`images/01-blocks-scripts-and-sprites/image449.png`

This library
interfaces with a capability in up-to-date browsers, so it might not
work for you. It works best if the accent matches
the text!
:::{index} speak block
:::

The {index}`parallelization library` contains
these blocks:

{img alt="image450.png" width="1.17986in"}`images/01-blocks-scripts-and-sprites/image450.png`

The two `do in parallel`blocks
 take any number of scripts as inputs.
Those scripts will be run in parallel, like ordinary independent scripts
in the scripting area. `The do in parallel and wait` version waits until all of those
scripts have finished before continuing the script below the block.
:::{index} do in parallel block
:::

The create variables library
 has these blocks:
:::{index} variables library
`does var exist` block
:::

{img alt="image451.png" width="1.37778in"}`images/01-blocks-scripts-and-sprites/image451.png`

These blocks allow a program to perform the same operation as the
button, making global, sprite local, or script variables, but allowing
the program to compute the variable name(s). It can also set and find
the values of these variables, show and hide their stage watchers,
delete them, and find out if they already exist.

The getters and setters library has these
blocks:
:::{index} getter/setter library
:::

{img alt="image452.png" width="1.875in"}`images/01-blocks-scripts-and-sprites/image452.png`

The purpose of this library is to allow program access to the settings controlled by user interface
elements, such as the settings menu {inline alt="image453.png"}`images/01-blocks-scripts-and-sprites/image453.png`. The `setting` block reports a setting; the `set flag` block sets
yes-or-no options that have checkboxes in the user interface, while the
`set value` block controls settings with numeric
or text values, such as project name.
:::{index} set flag block
`set value` block
:::

Certain settings are ordinarily remembered on a per-user basis, such as
the “zoom blocks” value. But when these settings are changed by this
library, the change is in effect only while the project using the
library is loaded. No permanent changes are made. Note: this library has
not been converted for version 7.0, so you’ll have to enable Javascript
extensions to use it.

The bignums, rationals, complex \#s library has these blocks:
:::{index} library; infinite precision integers
:::

{img alt="image454.png" width="1.88in"}`images/01-blocks-scripts-and-sprites/image454.png`

The `USE BIGNUMS` block takes a Boolean input, to turn
the infinite precision feature on or off. When on, all of the arithmetic
operators are redefined to accept and report integers of any number of
digits (limited only by the memory of your computer) and, in fact, the
entire Scheme numeric tower, with exact rationals and with complex
numbers. The `Scheme number` block has a list
of functions applicable to Scheme numbers, including subtype predicates
such as rational? and infinite?, and selectors such as numerator and
real-part.
:::{index} BIGNUMS block
`Scheme number` block
:::

<!-- I cannot figure out an index format that compiles this... -->
The `!` block computes the factorial function, useful to test whether bignums are turned on. Without bignums:
:::{index} `!` block, block; !
factorial
:::

{img alt="image455.png" width="0.29167in"}`images/01-blocks-scripts-and-sprites/image455.png`

With bignums:

{img alt="image456.png" width="0.29167in"}`images/01-blocks-scripts-and-sprites/image456.png`

The 375-digit value of 200! isn’t readable on this page, but if you
right-click on the block and choose “result pic,” you can open the
resulting picture in a browser window and scroll through it. (These
values end with a bunch of zero digits. That’s not roundoff error; the
prime factors of 100! and 200! include many copies of 2 and 5.) The
block with no name is a way to enter things
like 3/4 and 4+7i into numeric input slots by converting the slot to Any
type.
:::{index} block with no name
:::

The strings, multi-line input library
provides these blocks:
:::{index} string processing library
case-independent comparisons block
:::

{img alt="image463.png" width="3.9375in"}`images/01-blocks-scripts-and-sprites/image463.png`

All of these could be written in Snap<em>!</em> itself, but these are implemented
using the corresponding JavaScript library functions directly, so they
run fast. They can be used, for example, in scraping data from a web
site. The command use case-independent comparisons applies only to this
library. The {index}`\`multiline\` block<`multiline` block>` accepts and reports
a text input that can include newline characters.

The {index}`animation library` has these blocks:

{img alt="image464.png" width="4.0125in"}`images/01-blocks-scripts-and-sprites/image464.png`

Despite the name, this isn’t only about graphics; you can animate the values
of a variable, or anything else that’s expressed numerically.


The central idea of this library is an *easing function* *,* a
reporter whose domain and range are real numbers between 0 and 1
inclusive. The function represents what fraction of the “distance” (in
quotes because it might be any numeric value, such as temperature in a
simulation of weather) from here to there should be covered in what
fraction of the time. A {index}`linear easing` function
means steady progression. A quadratic easing function means starting
slowly and accelerating. (Note that, since it’s a requirement that
*f*(0)=0 and *f*(1)=1, there is only one linear easing function,
*f*(*x*)=*x*, and similarly for other categories.) The {inline alt="image465.png"}`images/01-blocks-scripts-and-sprites/image465.png` block reports some of the common easing functions.
:::{index} easing function
:::

The two Motion blocks in this library animate a sprite. `Glide` always animates
the sprite’s motion. `Animate's` first pulldown menu input allows you to
animate horizontal or vertical motion, but will also animate the
sprite’s direction or size. The `animate setter` block in
Control lets you animate any numeric quantity with any easing function.
The getter and setter inputs are best explained by example:
:::{index} animate block
:::

{img alt="image466.png" width="4.63194in"}`images/01-blocks-scripts-and-sprites/image466.png`

is equivalent to

{img alt="image467.png" width="3.40972in"}`images/01-blocks-scripts-and-sprites/image467.png`

The other blocks in the library are helpers for these four.

The serial ports library contains these
blocks:
:::{index} serial-ports library
:::

{img alt="image468.png" width="1.73264in"}`images/01-blocks-scripts-and-sprites/image468.png`

It is used to allow hardware developers to control devices such as robots
that are connected to your computer via a serial port.

The {index}`frequency distribution analysis library` has these blocks:

{img alt="image469.png" width="4.02708in"}`images/01-blocks-scripts-and-sprites/image469.png`

This is a collection of tools for analyzing large data sets and plotting
histogram s of how often some value is found in some
column of the table holding the data.
:::{index} histogram
:::

For more information go here:

https://tinyurl.com/jens-data

The audio comp library includes these
blocks:
:::{index} sound manipulation library
:::

{img alt="image470.png" width="3.54167in"}`images/01-blocks-scripts-and-sprites/image470.png`

This library takes a sound,
one that you record or one from our collection of sounds, and
manipulates it by systematically changing the intensity of the samples
in the sound and by changing the sampling rate at which the sound is
reproduced. Many of the blocks are helpers for the `plot sound` block,
used to plot the waveform of a sound. The `play sound` (primitive) block plays a sound. \_\_ `Hz for`
 reports a sine wave as a list of samples.
:::{index} plot sound block
`play` block
`Hz for` block
:::

The web services library has these blocks:
:::{index} web services library
:::

{img alt="image471.png" width="3.41in"}`images/01-blocks-scripts-and-sprites/image471.png`

The first block is a generalization of the primitive
{index}`\`url\` block<`url` block>`, allowing more control over the various
options in web requests:
`GET`, `POST`, `PUT`, and `DELETE`, and fine control over the content of the
message sent to the server. {index}`Current location block` reports your latitude and longitude. The {index}`Listify block` takes some text in JSON format (see @multi-dimensional-lists-and-json) and converts it to a structured
list. `Value at key` looks up a key-value pair
in a (listified) JSON dictionary. The `key:value:` block
 is just a constructor for an abstract data
type used with the other blocks
:::{index} value at key block
single: `key\:value\:` block
:::

The {index}`database library` contains these blocks:

{img alt="image472.png" width="2.26in"}`images/01-blocks-scripts-and-sprites/image472.png`

It is used to keep data that persist from one Snap<em>!</em> session
to the next, if you use the same browser and the same login.

The world {index}`map library` has these blocks:

{img alt="image473.png" width="2.44236in"}`images/01-blocks-scripts-and-sprites/image473.png`

Using any of the command blocks puts a map on the screen, in a layer in front of the stage’s
background but behind the pen trails layer (which is in turn behind all
the sprites). The first block asks your browser for your current
physical location, for which you may be asked to give permission. The
next two blocks get and set the map’s zoom amount; the default zoom of
10 ﬁts from San Francisco not quite down to Palo Alto on the screen. A
zoom of 1 ﬁts almost the entire world. A zoom of 3 fits the United
States; a zoom of 5 ﬁts Germany. The zoom can be changed in half steps,
i.e., 5.5 is different from 5, but 5.25 isn’t.

The next five blocks convert between stage coordinates (pixels) and
Earth coordinates (latitude and longitude). The change by x: y: block
shifts the map relative to the stage. The distance to block measures the
map distance (in meters) between two sprites. The three reporters with
current in their names find *your* actual location, again supposing that
geolocation is enabled on your device. Update redraws the map; as
costume reports the visible section of the map as a costume. `Set style`
allows things like satellite pictures.

The {index}`APL primitives library` contains these blocks:

{img alt="image474.png" width="5.73in"}`images/01-blocks-scripts-and-sprites/image474.png`

{img alt="image475.png" width="6.45in"}`images/01-blocks-scripts-and-sprites/image475.png`

For more information about APL, see @sec-apl-features).

The **list comprehension library** has one block, `zip`:
:::{index} list comprehension library
:::

{img alt="image476.png" width="1.20in"}`images/01-blocks-scripts-and-sprites/image476.png`

Its first input is a function of two inputs. The two Any-type inputs are
deep lists (lists of lists of…) interpreted as trees, and the function
is called with every possible combination of a leaf node of the first
tree and a leaf node of the second tree. But instead of taking atoms
(non-lists) as the leaves, `zip` allows the leaves of each tree to be
vectors (one-dimensional lists), matrices (two-dimensional lists), etc.
The Number-type inputs specify the leaf dimension for each tree, so the
function input might be called with a vector from the first tree and an
atom from the second tree.

The **bitwise library** provides bitwise
logic functions; each bit of
the reported value is the result of applying the corresponding Boolean
function to the corresponding bits of the input(s). The Boolean
functions are `not for ¬`, ` and for ∧`, ` or for ∨`, and `xor (exclusive or) for
⊻`. The remaining functions shift their first input left or right by the
number of bits given by the second input. `\<\<` is left shift, `\>\>` is
arithmetic right shift (shifting in one bits from the left), and `\>\>\>`
is logical right shift (shifting in zero bits from the left). If you
don’t already know what these mean, find a tutorial online.
:::{index} bitwise library
:::

{img alt="image477.png" width="0.89in"}`images/01-blocks-scripts-and-sprites/image477.png`

The **MQTT library** supports the Message Queuing
Telemetry Transport protocol, for connecting with IOT devices. See
<https://mqtt.org/> for more information.
:::{index} MQTT library, library; MQTTqq
:::

{img alt="image487.png" width="3.55in"}`images/01-blocks-scripts-and-sprites/image487.png`

The **Signada library** allows you to control a
microBit or similar device that works with the Signada MicroBlocks
project.
:::{index} Signada library
:::

{img alt="image488.png" width="1.23in"}`images/01-blocks-scripts-and-sprites/image488.png`

The **menus library** provides the ability to
display hierarchical menus on the stage, using the ask block’s ability
to take lists as inputs. See @sec-ask-lists.
:::{index} menus library
:::

:::{index}
library; SciSnap
library; TuneScope
SciSnap! library
TuneScope library
:::

### Extensions Libraries
{img alt="image486.png" width="3.39in"}`images/01-blocks-scripts-and-sprites/image486.png`

The **SciSnap<em>!</em> library** and the
**TuneScope library** are too big to discuss here and are
documented sepa, library; MQTTqqrately at
<http://emu-online.de/ProgrammingWithSciSnap.pdf> and
<https://maketolearn.org/creating-art-animations-and-music/>
respectively.
