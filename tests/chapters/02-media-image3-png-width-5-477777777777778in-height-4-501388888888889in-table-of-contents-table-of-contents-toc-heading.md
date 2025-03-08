# ![](assets/image3.png) <!-- width="5.477777777777778in" height="4.501388888888889in" --> Table of Contents {#table-of-contents .TOC-Heading}

Brian Harvey

Jens Mönig

I. Blocks, Scripts, and Sprites [5](#blocks-scripts-and-sprites)

Hat Blocks and Command Blocks [6](#hat-blocks-and-command-blocks)

A. Sprites and Parallelism [8](#sprites-and-parallelism)

Costumes and Sounds [8](#costumes-and-sounds)

Inter-Sprite Communication with Broadcast
[9](#inter-sprite-communication-with-broadcast)

B. Nesting Sprites: Anchors and Parts
[10](#nesting-sprites-anchors-and-parts)

C. Reporter Blocks and Expressions
[10](#reporter-blocks-and-expressions)

D. Predicates and Conditional Evaluation
[12](#predicates-and-conditional-evaluation)

E. Variables [13](#variables)

Global Variables [14](#global-variables)

Script Variables [15](#script-variables)

Renaming variables [15](#renaming-variables)

Transient variables [16](#transient-variables)

F. Debugging [17](#debugging)

The pause button [17](#the-pause-button)

Breakpoints: the pause all block [17](#breakpoints-the-pause-all-block)

Visible stepping [18](#visible-stepping)

G. Etcetera [18](#etcetera)

H. Libraries [25](#libraries)

II\. Saving and Loading Projects and Media
[37](#saving-and-loading-projects-and-media)

A. Local Storage [37](#local-storage)

B. Creating a Cloud Account [37](#creating-a-cloud-account)

C. Saving to the Cloud [38](#saving-to-the-cloud)

D. Loading Saved Projects [38](#loading-saved-projects)

E. **If you lose your project, do this first!**
[39](#if-you-lose-your-project-do-this-first)

F. Private and Public Projects [39](#private-and-public-projects)

III\. Building a Block [40](#building-a-block)

A. Simple Blocks [40](#simple-blocks)

Custom Blocks with Inputs [42](#custom-blocks-with-inputs)

Editing Block Properties [43](#editing-block-properties)

B. Recursion [43](#recursion)

C. Block Libraries [44](#block-libraries)

D. Custom blocks and Visible Stepping
[45](#custom-blocks-and-visible-stepping)

IV\. First class lists [46](#first-class-lists)

A. The list Block [46](#the-list-block)

B. Lists of Lists [47](#lists-of-lists)

C. Functional and Imperative List Programming
[48](#functional-and-imperative-list-programming)

D. Higher Order List Operations and Rings
[49](#higher-order-list-operations-and-rings)

E. Table View vs. List View [51](#table-view-vs.-list-view)

Comma-Separated Values [54](#comma-separated-values)

Multi-dimensional lists and JSON [54](#multi-dimensional-lists-and-json)

F. Hyperblocks [55](#hyperblocks)

V. Typed Inputs [59](#typed-inputs)

A. Scratch's Type Notation [59](#scratchs-type-notation)

B. The Snap! Input Type Dialog [59](#the-snap-input-type-dialog)

Procedure Types [60](#procedure-types)

Pulldown inputs
[61](#macintosh-hdusersbhdesktopgear-part.pngpulldown-inputs)

Input variants [63](#input-variants)

Prototype Hints [64](#prototype-hints)

Title Text and Symbols [64](#title-text-and-symbols)

VI\. Procedures as Data [65](#procedures-as-data)

A. Call and Run [65](#call-and-run)

Call/Run with inputs [65](#callrun-with-inputs)

Variables in Ring Slots [66](#variables-in-ring-slots)

B. Writing Higher Order Procedures
[66](#writing-higher-order-procedures)

Recursive Calls to Multiple-Input Blocks
[68](#recursive-calls-to-multiple-input-blocks)

C. Formal Parameters [69](#formal-parameters)

D. Procedures as Data [70](#procedures-as-data-1)

E. Special Forms [71](#special-forms)

Special Forms in Scratch [72](#special-forms-in-scratch)

VII\. Object Oriented Programming with Sprites
[73](#object-oriented-programming-with-sprites)

A. First Class Sprites [73](#first-class-sprites)

B. Permanent and Temporary Clones [74](#permanent-and-temporary-clones)

C. Sending Messages to Sprites [74](#sending-messages-to-sprites)

Polymorphism [75](#polymorphism)

D. Local State in Sprites: Variables and Attributes
[76](#local-state-in-sprites-variables-and-attributes)

E. Prototyping: Parents and Children
[76](#prototyping-parents-and-children)

F. Inheritance by Delegation [77](#inheritance-by-delegation)

G. List of attributes [78](#attrib.pnglist-of-attributes)

H. First Class Costumes and Sounds
[79](#first-class-costumes-and-sounds)

Media Computation with Costumes [79](#media-computation-with-costumes)

Media Computation with Sounds [82](#media-computation-with-sounds)

VIII\. OOP with Procedures [85](#oop-with-procedures)

A. Local State with Script Variables
[85](#local-state-with-script-variables)

B. Messages and Dispatch Procedures
[86](#messages-and-dispatch-procedures)

C. Inheritance via Delegation [87](#inheritance-via-delegation)

D. An Implementation of Prototyping OOP
[88](#an-implementation-of-prototyping-oop)

IX\. The Outside World [91](#the-outside-world)

A. The World Wide Web [91](#the-world-wide-web)

B. Hardware Devices [92](#hardware-devices)

C. Date and Time [92](#date-and-time)

X. Continuations [93](#continuations)

A. Continuation Passing Style [94](#continuation-passing-style)

B. Call/Run w/Continuation [97](#callrun-wcontinuation)

Nonlocal exit [99](#nonlocal-exit)

XI\. Metaprogramming [101](#metaprogramming)

A. Reading a block [101](#reading-a-block)

B. Writing a block [102](#writing-a-block)

C. Macros [105](#macros)

XII\. User Interface Elements [107](#user-interface-elements)

A. Tool Bar Features [107](#tool-bar-features)

The Snap*!* Logo Menu [107](#the-snap-logo-menu)

The File Menu [108](#the-file-menu)

The Cloud Menu [113](#the-cloud-menu)

The Settings Menu [114](#the-settings-menu)

Visible Stepping Controls [117](#visible-stepping-controls)

Stage Resizing Buttons [118](#stage-resizing-buttons)

Project Control Buttons [118](#project-control-buttons)

B. The Palette Area [119](#the-palette-area)

Buttons in the Palette [119](#buttons-in-the-palette)

Context Menus for Palette Blocks
[119](#context-menus-for-palette-blocks)

Context Menu for the Palette Background
[120](#context-menu-for-the-palette-background)

C. The Scripting Area [122](#the-scripting-area)

Sprite Appearance and Behavior Controls
[122](#sprite-appearance-and-behavior-controls)

Scripting Area Tabs [122](#scripting-area-tabs)

Scripts and Blocks Within Scripts
[122](#scripts-and-blocks-within-scripts)

Controls in the Costumes Tab [126](#controls-in-the-costumes-tab)

The Paint Editor [128](#the-paint-editor)

Controls in the Sounds Tab [130](#controls-in-the-sounds-tab)

D. Keyboard Editing [130](#keyboard-editing)

Starting and stopping the keyboard editor
[130](#starting-and-stopping-the-keyboard-editor)

Navigating in the keyboard editor
[130](#navigating-in-the-keyboard-editor)

Editing a script [131](#editing-a-script)

Running the selected script [132](#running-the-selected-script)

E. Controls on the Stage [132](#controls-on-the-stage)

Sprites [132](#sprites)

Variable watchers
[134](#macintosh-hdusersbhdesktopwatcher-menu.pngvariable-watchers)

The stage itself [135](#the-stage-itself)

F. The Sprite Corral and Sprite Creation Buttons
[135](#the-sprite-corral-and-sprite-creation-buttons)

G. Preloading a Project when Starting Snap!
[136](#preloading-a-project-when-starting-snap)

H. Mirror Sites [137](#mirror-sites)

Appendix A. Snap*!* color library [138](#appendix-a.-snap-color-library)

Introduction to Color [138](#introduction-to-color)

Crayons and Color Numbers [139](#crayons-and-color-numbers)

Perceptual Spaces: HSV and HSL [142](#perceptual-spaces-hsv-and-hsl)

Mixing Colors [144](#mixing-colors)

tl;dr [145](#tldr)

Subappendix: Geeky details on fair hue
[145](#subappendix-geeky-details-on-fair-hue)

Subappendix: Geeky details on color numbers
[146](#subappendix-geeky-details-on-color-numbers)

Appendix B. APL features [148](#appendix-b.-apl-features)

Boolean values [150](#boolean-values)

Scalar functions [150](#scalar-functions)

Mixed functions [151](#mixed-functions)

Higher order functions [157](#higher-order-functions)

Index ............................................................. 159

Copyright © 2020 Jens Mönig and Brian Harvey.

![Macintosh
HD:Users:bh:Desktop:cc.png](assets/image4.png) <!-- width="0.6111111111111112in" height="0.2152777777777778in" --> This work is licensed under a [Creative
Commons Attribution-NonCommercial-ShareAlike 4.0 International
License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

