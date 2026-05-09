---
---

:::{index} devices
sensors
robots
World Wide Web
:::

(sec-ch09)=
# 9. The Outside World

The facilities discussed so far are fine for projects that take place
entirely on your computer’s screen. But you may want to write programs
that interact with physical devices (sensors
or robots) or with the World Wide Web. For these purposes Snap<em>!</em> provides a
single primitive block:

{img alt="report URL block 'snap.berkeley.edu'"}`blocks/images/block_reportURL.png`

This might not seem like enough, but in fact it can be used to build the
desired capabilities.

:::{index} URL
Uniform Resource Locator
HTML
HTML (HyperText Markup Language)
HTTPS
HTTP
CORS
Cross-Origin Resource Sharing
:::

## The World Wide Web

The input to the {index}`url block` is the URL (Uniform
Resource Locator) of a web page. The
block reports the body of the Web server’s response (minus HTTP header),
*without interpretation.* This means that in most cases the response is
a description of the page in HTML (HyperText Markup Language)
notation. Often, especially for commercial web sites, the actual
information you’re trying to find on
the page is actually at another URL included in the reported HTML. The
Web page is typically a very long text string, and so the primitive
{index}`split block` is useful to get the text in a
manageable form, namely, as a list of lines:

<!-- TODO: Shrink an image like this in the PDF so more stuff fits on the previous page... -->
{img alt="image871.png" width="6.52in"}`images/09-the-outside-world/image871.png`

The second input to split is the character to be used to separate the
text string into a list of lines, or one of a set of common cases (such
as line, which separates on carriage return and/or newline characters).

This might be a good place for a reminder that list-view watchers scroll
through only 100 items at a time. The downarrow near the bottom right
corner of the speech balloon in the picture presents a menu of
hundred-item ranges. (This may seem unnecessary, since the scroll bar
should allow for any number of items, but doing it this way makes
Snap<em>!</em> much faster.) In table view, the entire list is included.

If you include a protocol name in the input to the url block (such as
`http://` or `https://`), that protocol will be used. If not, the block
first tries HTTPS and then, if that fails, HTTP.

A security restriction in JavaScript limits the ability of one web site
to initiate communication with another site. There is an official
workaround for this limitation called the CORS protocol
(Cross-Origin Resource Sharing),
but the *target* site has to allow snap.berkeley.edu explicitly, and of
course most don’t. To get around this problem, you can use third-party
sites (“{index}`cors proxies`”) that are not limited by
JavaScript and that forward your requests.

<!-- TODO: Note that you must trust the CORS proxy that you use not to steal your data or modify the responses. -->

:::{index} devices
robots
Lego NXT
Finch
Hummingbird
Nintendo
Wiimote
Leap Motion
Arduino
Super-Awesome Sylvia
Water Color Bot
:::

## Hardware Devices

Another JavaScript security restriction prevents Snap<em>!</em> from having
direct access to devices connected to your computer,
such as sensors and robots. (Mobile devices such as
smartphones may also have useful devices built in, such as
accelerometers and GPS receivers.) The url block is also used to
interface Snap<em>!</em> with these external capabilities.

The idea is that you run a separate program that both interfaces with
the device and provides a local HTTP server that Snap<em>!</em> can use to make
requests to the device. *Unlike* Snap<em>!</em> *itself, these programs have
access to anything on your computer, so you have to trust the author of
the software!* Our web site, snap.berkeley.edu, provides links to
drivers for several devices, including, at this writing, the Lego NXT,
Finch, Hummingbird, and {index}`Parallax S2` robots; the Nintendo
Wiimote and Leap Motion sensors, the Arduino microcomputer, and
Super-Awesome Sylvia ’s Water Color Bot. The same server technique can be used for
access to third party software libraries, such as the speech synthesis
package linked on our web site.

Most of these packages require some expertise to install; the links are
to source code repositories. This situation will improve with time.

:::{index} current block
current date or time
date
time
:::

## Date and Time

The current block in the Sensing palette can be used to find
out the current date or time. Each call to
this block reports one component of the date or time,
so you will probably combine several calls, like this:

{img alt="image872.png" width="5.31in"}`images/09-the-outside-world/image872.png`

for Americans, or like this:

{img alt="image873.png" width="5.31in"}`images/09-the-outside-world/image873.png`

for Europeans.
