# Acknowledgements {#acknowledgements .TOC-Heading}

We have been extremely lucky in our mentors. Jens cut his
teeth in the company of the Smalltalk pioneers: Alan Kay \[\]{.index
#Kay-Alan} , Dan Ingalls \[\]{.index #Ingalls-Dan} , and the rest of the
gang who invented personal computing and object oriented programming in
the great days of Xerox PARC \[\]{.index #Xerox-PARC} . He worked with
John Maloney \[\]{.index #Maloney-John} , of the MIT \[\]{.index
#Massachusetts-Institute-of-Technology} Scratch Team \[\]{.index
#Scratch-Team} , who developed the Morphic \[\]{.index #Morphic}
graphics framework that's still at the heart of Snap*!*.

***The brilliant design of Scratch, from the Lifelong Kindergarten
Group*** \[\]{.index #Lifelong-Kindergarten-Group} ***at the MIT Media
Lab*** \[\]{.index #Media-Lab} ***, is crucial to* Snap*!. Our earlier
version, BYOB, was a direct modification of the Scratch source code.*
Snap*! is a complete rewrite, but its code structure and its user
interface remain deeply indebted to Scratch. And the Scratch Team, who
could have seen us as rivals, have been entirely supportive and
welcoming to us.***

Brian grew up at the MIT and Stanford Artificial Intelligence Labs
\[\]{.index #MIT-Artificial-Intelligence-Lab} , learning from Lisp
inventor John McCarthy \[\]{.index #-McCarthy-John} , Scheme \[\]{.index
#Scheme} inventors Gerald J. Sussman \[\]{.index #Sussman-Gerald-J.} and
Guy Steele \[\]{.index #Steele-Guy} , and the authors of the world's
best computer science book, *Structure and Interpretation of Computer
Programs* \[\]{.index
#Structure-and-Interpretation-of-Computer-Programs} *,* Hal Abelson
\[\]{.index #Abelson-Hal} and Gerald J. Sussman with Julie Sussman
\[\]{.index #Sussman-Julie} , among many other heroes of computer
science. (Brian was also lucky enough, while in high school, to meet
Kenneth Iverson \[\]{.index #Iverson-Kenneth-E.} , the inventor of APL
\[\]{.index #APL} .)

***In the glory days of the MIT Logo Lab, we used to say, "Logo is Lisp
disguised as BASIC." Now, with its first class procedures, lexical
scope, and first class continuations,* Snap*! is Scheme disguised as
Scratch.***

Four people have made such massive contributions to the implementation
of Snap*!* that we have officially declared them members of the team:
Michael Ball \[\]{.index #Ball-Michael} and Bernat Romagosa, in addition
to contributions throughout the project, have primary responsibility for
the web site and cloud storage \[\]{.index #Romagosa-Bernat} . Joan
Guillén i Pelegay \[\]{.index #Guillén-i-Pelegay-Joan} has contributed
very careful and wise analysis of outstanding issues, including help in
taming the management of translations to non-English languages. Jadga
Hügle \[\]{.index #Huegle-Jadga} , has energetically contributed to
online mini-courses about Snap*!* and leading workshops for kids and for
adults. Jens, Jadga, and Bernat are paid to work on Snap*!* by SAP,
which also supports our computing needs.

We have been fortunate to get to know an amazing group of brilliant
middle school(!) and high school students through the Scratch Advanced
Topics forum, several of whom (since grown up) have contributed code to
Snap*!*: Kartik Chandra \[\]{.index #Chandra-Kartik} , Nathan Dinsmore
\[\]{.index #Dinsmore-Nathan} , Connor Hudson \[\]{.index
#Hudson-Connor} , Ian Reynolds \[\]{.index #Reynolds-Ian} , and Deborah
Servilla \[\]{.index #Servilla-Deborah} . Many more have contributed
ideas and alpha-testing bug reports. UC Berkeley students who've
contributed code include Achal Dave \[\]{.index #Dave-Achal} . Kyle
Hotchkiss \[\]{.index #Hotchkiss.-Kyle} , Ivan Motyashov \[\]{.index
#Motyashov-Ivan} , and Yuan Yuan \[\]{.index #Yuan-Yuan} . Contributors
of translations are too numerous to list here, but they're in the
"About..." box in Snap*!* itself.

This material is based upon work supported in part by the National
Science Foundation under Grants No. 1138596, 1143566, and
1441075; and in part by MioSoft, Arduino.org, SAP, and YC Research. Any
opinions, findings, and conclusions or recommendations expressed in this
material are those of the author(s) and do not necessarily reflect the
views of the National Science Foundation or other funders.

[\
]{.smallcaps}**[Snap*!* Reference Manual]{.underline}**

**Version 8.0**

Snap*!* (formerly BYOB) is an extended reimplementation of Scratch
([https://scratch.mit.edu]{.underline}) that allows you to Build Your
Own Blocks. It also features ﬁrst class lists, ﬁrst class procedures,
first class sprites, first class costumes, first class sounds, and first
class continuations. These added capabilities make it suitable for a
serious introduction to computer science for high school or college
students.

In this manual we sometimes make reference to Scratch, e.g., to explain
how some Snap*!* feature extends something familiar in Scratch. It's
very helpful to have some experience with Scratch before reading this
manual, but not essential.

To run Snap*!*, open a browser window and connect to
https://snap.berkeley.edu/run. The Snap*!* community web site at
https://snap.berkeley.edu is not part of this manual's scope.

