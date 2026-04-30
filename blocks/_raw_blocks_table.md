| Block | Text Label | Type | Category | Lisp |
| ----- | ---------- | ---- | -------- | ---- |
| [![block 'move _ steps'](/blocks/images/block_forward.png)](/blocks/motion/forward.html) | [`move _ steps`](/blocks/motion/forward.html) | command | motion | `(move 10)` |
| [![block 'turn $clockwise _ degrees'](/blocks/images/block_turn.png)](/blocks/motion/turn.html) | [`turn $clockwise _ degrees`](/blocks/motion/turn.html) | command | motion | `(right 15)` |
| [![block 'turn $counterclockwise _ degrees'](/blocks/images/block_turnLeft.png)](/blocks/motion/turnLeft.html) | [`turn $counterclockwise _ degrees`](/blocks/motion/turnLeft.html) | command | motion | `(left 15)` |
| [![block 'point in direction _'](/blocks/images/block_setHeading.png)](/blocks/motion/setHeading.html) | [`point in direction _`](/blocks/motion/setHeading.html) | command | motion | `(head 90)` |
| [![block 'point towards _'](/blocks/images/block_doFaceTowards.png)](/blocks/motion/doFaceTowards.html) | [`point towards _`](/blocks/motion/doFaceTowards.html) | command | motion | `(face [mouse-pointer])` |
| [![block 'go to x: _ y: _'](/blocks/images/block_gotoXY.png)](/blocks/motion/gotoXY.html) | [`go to x: _ y: _`](/blocks/motion/gotoXY.html) | command | motion | `(go 0 0)` |
| [![block 'go to _'](/blocks/images/block_doGotoObject.png)](/blocks/motion/doGotoObject.html) | [`go to _`](/blocks/motion/doGotoObject.html) | command | motion | `(goto "[random position]")` |
| [![block 'glide _ secs to x: _ y: _'](/blocks/images/block_doGlide.png)](/blocks/motion/doGlide.html) | [`glide _ secs to x: _ y: _`](/blocks/motion/doGlide.html) | command | motion | `(glide 1 0 0)` |
| [![block 'change x by _'](/blocks/images/block_changeXPosition.png)](/blocks/motion/changeXPosition.html) | [`change x by _`](/blocks/motion/changeXPosition.html) | command | motion | `(+x 10)` |
| [![block 'set x to _'](/blocks/images/block_setXPosition.png)](/blocks/motion/setXPosition.html) | [`set x to _`](/blocks/motion/setXPosition.html) | command | motion | `(x= 0)` |
| [![block 'change y by _'](/blocks/images/block_changeYPosition.png)](/blocks/motion/changeYPosition.html) | [`change y by _`](/blocks/motion/changeYPosition.html) | command | motion | `(+y 10)` |
| [![block 'set y to _'](/blocks/images/block_setYPosition.png)](/blocks/motion/setYPosition.html) | [`set y to _`](/blocks/motion/setYPosition.html) | command | motion | `(y= 0)` |
| [![block 'if on edge, bounce'](/blocks/images/block_bounceOffEdge.png)](/blocks/motion/bounceOffEdge.html) | [`if on edge, bounce`](/blocks/motion/bounceOffEdge.html) | command | motion | `(bounce)` |
| [![block 'position'](/blocks/images/block_getPosition.png)](/blocks/motion/getPosition.html) | [`position`](/blocks/motion/getPosition.html) | reporter | motion | `(pos)` |
| [![block 'x position'](/blocks/images/block_xPosition.png)](/blocks/motion/xPosition.html) | [`x position`](/blocks/motion/xPosition.html) | reporter | motion | `(x)` |
| [![block 'y position'](/blocks/images/block_yPosition.png)](/blocks/motion/yPosition.html) | [`y position`](/blocks/motion/yPosition.html) | reporter | motion | `(y)` |
| [![block 'direction'](/blocks/images/block_direction.png)](/blocks/motion/direction.html) | [`direction`](/blocks/motion/direction.html) | reporter | motion | `(dir)` |
| [![block 'switch to costume _'](/blocks/images/block_doSwitchToCostume.png)](/blocks/looks/doSwitchToCostume.html) | [`switch to costume _`](/blocks/looks/doSwitchToCostume.html) | command | looks | `(wear nil)` |
| [![block 'next costume'](/blocks/images/block_doWearNextCostume.png)](/blocks/looks/doWearNextCostume.html) | [`next costume`](/blocks/looks/doWearNextCostume.html) | command | looks | `(next)` |
| [![block 'costume #'](/blocks/images/block_getCostumeIdx.png)](/blocks/looks/getCostumeIdx.html) | [`costume #`](/blocks/looks/getCostumeIdx.html) | reporter | looks | `(costume#)` |
| [![block 'say _ for _ secs'](/blocks/images/block_doSayFor.png)](/blocks/looks/doSayFor.html) | [`say _ for _ secs`](/blocks/looks/doSayFor.html) | command | looks | `(sayFor Hello! 2)` |
| [![block 'say _'](/blocks/images/block_bubble.png)](/blocks/looks/bubble.html) | [`say _`](/blocks/looks/bubble.html) | command | looks | `(say Hello!)` |
| [![block 'think _ for _ secs'](/blocks/images/block_doThinkFor.png)](/blocks/looks/doThinkFor.html) | [`think _ for _ secs`](/blocks/looks/doThinkFor.html) | command | looks | `(thinkFor Hmm... 2)` |
| [![block 'think _'](/blocks/images/block_doThink.png)](/blocks/looks/doThink.html) | [`think _`](/blocks/looks/doThink.html) | command | looks | `(think Hmm...)` |
| [![block '_ of costume _'](/blocks/images/block_reportGetImageAttribute.png)](/blocks/looks/reportGetImageAttribute.html) | [`_ of costume _`](/blocks/looks/reportGetImageAttribute.html) | reporter | looks | `(costume [width] [current])` |
| [![block 'stretch _ x: _ y: _ %'](/blocks/images/block_reportNewCostumeStretched.png)](/blocks/looks/reportNewCostumeStretched.html) | [`stretch _ x: _ y: _ %`](/blocks/looks/reportNewCostumeStretched.html) | reporter | looks | `(stretch [current] 100 50)` |
| [![block 'skew _ to _ degrees _ %'](/blocks/images/block_reportNewCostumeSkewed.png)](/blocks/looks/reportNewCostumeSkewed.html) | [`skew _ to _ degrees _ %`](/blocks/looks/reportNewCostumeSkewed.html) | reporter | looks | `(skew [current] 0 50)` |
| [![block 'new costume _ width _ height _'](/blocks/images/block_reportNewCostume.png)](/blocks/looks/reportNewCostume.html) | [`new costume _ width _ height _`](/blocks/looks/reportNewCostume.html) | reporter | looks | `(newCostume nil nil nil)` |
| [![block 'change _ effect by _'](/blocks/images/block_changeEffect.png)](/blocks/looks/changeEffect.html) | [`change _ effect by _`](/blocks/looks/changeEffect.html) | command | looks | `(+effect [ghost] 25)` |
| [![block 'set _ effect to _'](/blocks/images/block_setEffect.png)](/blocks/looks/setEffect.html) | [`set _ effect to _`](/blocks/looks/setEffect.html) | command | looks | `(effect= [ghost] 0)` |
| [![block 'clear graphic effects'](/blocks/images/block_clearEffects.png)](/blocks/looks/clearEffects.html) | [`clear graphic effects`](/blocks/looks/clearEffects.html) | command | looks | `(clearEffects)` |
| [![block '_ effect'](/blocks/images/block_getEffect.png)](/blocks/looks/getEffect.html) | [`_ effect`](/blocks/looks/getEffect.html) | reporter | looks | `(effect [ghost])` |
| [![block 'change size by _'](/blocks/images/block_changeScale.png)](/blocks/looks/changeScale.html) | [`change size by _`](/blocks/looks/changeScale.html) | command | looks | `(+size 10)` |
| [![block 'set size to _ %'](/blocks/images/block_setScale.png)](/blocks/looks/setScale.html) | [`set size to _ %`](/blocks/looks/setScale.html) | command | looks | `(size= 100)` |
| [![block 'size'](/blocks/images/block_getScale.png)](/blocks/looks/getScale.html) | [`size`](/blocks/looks/getScale.html) | reporter | looks | `(size)` |
| [![block 'show'](/blocks/images/block_show.png)](/blocks/looks/show.html) | [`show`](/blocks/looks/show.html) | command | looks | `(show)` |
| [![block 'hide'](/blocks/images/block_hide.png)](/blocks/looks/hide.html) | [`hide`](/blocks/looks/hide.html) | command | looks | `(hide)` |
| [![block 'shown?'](/blocks/images/block_reportShown.png)](/blocks/looks/reportShown.html) | [`shown?`](/blocks/looks/reportShown.html) | predicate | looks | `(shown)` |
| [![block 'go to _ layer'](/blocks/images/block_goToLayer.png)](/blocks/looks/goToLayer.html) | [`go to _ layer`](/blocks/looks/goToLayer.html) | command | looks | `(layer [front])` |
| [![block 'go back _ layers'](/blocks/images/block_goBack.png)](/blocks/looks/goBack.html) | [`go back _ layers`](/blocks/looks/goBack.html) | command | looks | `(back 1)` |
| [![block 'play sound _'](/blocks/images/block_playSound.png)](/blocks/sound/playSound.html) | [`play sound _`](/blocks/sound/playSound.html) | command | sound | `(play nil)` |
| [![block 'play sound _ until done'](/blocks/images/block_doPlaySoundUntilDone.png)](/blocks/sound/doPlaySoundUntilDone.html) | [`play sound _ until done`](/blocks/sound/doPlaySoundUntilDone.html) | command | sound | `(playAll nil)` |
| [![block 'stop all sounds'](/blocks/images/block_doStopAllSounds.png)](/blocks/sound/doStopAllSounds.html) | [`stop all sounds`](/blocks/sound/doStopAllSounds.html) | command | sound | `(stopSounds)` |
| [![block 'play sound _ at _ Hz'](/blocks/images/block_doPlaySoundAtRate.png)](/blocks/sound/doPlaySoundAtRate.html) | [`play sound _ at _ Hz`](/blocks/sound/doPlaySoundAtRate.html) | command | sound | `(playAt nil 44100)` |
| [![block '_ of sound _'](/blocks/images/block_reportGetSoundAttribute.png)](/blocks/sound/reportGetSoundAttribute.html) | [`_ of sound _`](/blocks/sound/reportGetSoundAttribute.html) | reporter | sound | `(sound [duration] nil)` |
| [![block 'new sound _ rate _ Hz'](/blocks/images/block_reportNewSoundFromSamples.png)](/blocks/sound/reportNewSoundFromSamples.html) | [`new sound _ rate _ Hz`](/blocks/sound/reportNewSoundFromSamples.html) | reporter | sound | `(newSound nil 44100)` |
| [![block 'rest for _ beats'](/blocks/images/block_doRest.png)](/blocks/sound/doRest.html) | [`rest for _ beats`](/blocks/sound/doRest.html) | command | sound | `(rest 0.2)` |
| [![block 'play note _ for _ beats'](/blocks/images/block_doPlayNote.png)](/blocks/sound/doPlayNote.html) | [`play note _ for _ beats`](/blocks/sound/doPlayNote.html) | command | sound | `(note 60 0.5)` |
| [![block 'set instrument to _'](/blocks/images/block_doSetInstrument.png)](/blocks/sound/doSetInstrument.html) | [`set instrument to _`](/blocks/sound/doSetInstrument.html) | command | sound | `(instrument 1)` |
| [![block 'change tempo by _'](/blocks/images/block_doChangeTempo.png)](/blocks/sound/doChangeTempo.html) | [`change tempo by _`](/blocks/sound/doChangeTempo.html) | command | sound | `(+tempo 20)` |
| [![block 'set tempo to _ bpm'](/blocks/images/block_doSetTempo.png)](/blocks/sound/doSetTempo.html) | [`set tempo to _ bpm`](/blocks/sound/doSetTempo.html) | command | sound | `(tempo= 60)` |
| [![block 'tempo'](/blocks/images/block_getTempo.png)](/blocks/sound/getTempo.html) | [`tempo`](/blocks/sound/getTempo.html) | reporter | sound | `(tempo)` |
| [![block 'change volume by _'](/blocks/images/block_changeVolume.png)](/blocks/sound/changeVolume.html) | [`change volume by _`](/blocks/sound/changeVolume.html) | command | sound | `(+vol 10)` |
| [![block 'set volume to _ %'](/blocks/images/block_setVolume.png)](/blocks/sound/setVolume.html) | [`set volume to _ %`](/blocks/sound/setVolume.html) | command | sound | `(vol= 100)` |
| [![block 'volume'](/blocks/images/block_getVolume.png)](/blocks/sound/getVolume.html) | [`volume`](/blocks/sound/getVolume.html) | reporter | sound | `(vol)` |
| [![block 'change balance by _'](/blocks/images/block_changePan.png)](/blocks/sound/changePan.html) | [`change balance by _`](/blocks/sound/changePan.html) | command | sound | `(+pan 10)` |
| [![block 'set balance to _'](/blocks/images/block_setPan.png)](/blocks/sound/setPan.html) | [`set balance to _`](/blocks/sound/setPan.html) | command | sound | `(pan= 0)` |
| [![block 'balance'](/blocks/images/block_getPan.png)](/blocks/sound/getPan.html) | [`balance`](/blocks/sound/getPan.html) | reporter | sound | `(pan)` |
| [![block 'play frequency _ Hz'](/blocks/images/block_playFreq.png)](/blocks/sound/playFreq.html) | [`play frequency _ Hz`](/blocks/sound/playFreq.html) | command | sound | `(freq 440)` |
| [![block 'stop frequency'](/blocks/images/block_stopFreq.png)](/blocks/sound/stopFreq.html) | [`stop frequency`](/blocks/sound/stopFreq.html) | command | sound | `(stopFreq)` |
| [![block 'clear'](/blocks/images/block_clear.png)](/blocks/pen/clear.html) | [`clear`](/blocks/pen/clear.html) | command | pen | `(clear)` |
| [![block 'pen down'](/blocks/images/block_down.png)](/blocks/pen/down.html) | [`pen down`](/blocks/pen/down.html) | command | pen | `(down)` |
| [![block 'pen up'](/blocks/images/block_up.png)](/blocks/pen/up.html) | [`pen up`](/blocks/pen/up.html) | command | pen | `(up)` |
| [![block 'pen down?'](/blocks/images/block_getPenDown.png)](/blocks/pen/getPenDown.html) | [`pen down?`](/blocks/pen/getPenDown.html) | predicate | pen | `(down?)` |
| [![block 'set pen color to _'](/blocks/images/block_setColor.png)](/blocks/pen/setColor.html) | [`set pen color to _`](/blocks/pen/setColor.html) | command | pen | `(setColor "rgba(145,26,68,1)")` |
| [![block 'change pen _ by _'](/blocks/images/block_changePenColorDimension.png)](/blocks/pen/changePenColorDimension.html) | [`change pen _ by _`](/blocks/pen/changePenColorDimension.html) | command | pen | `(+pen [hue] 10)` |
| [![block 'set pen _ to _'](/blocks/images/block_setPenColorDimension.png)](/blocks/pen/setPenColorDimension.html) | [`set pen _ to _`](/blocks/pen/setPenColorDimension.html) | command | pen | `(pen= [hue] 50)` |
| [![block 'pen _'](/blocks/images/block_getPenAttribute.png)](/blocks/pen/getPenAttribute.html) | [`pen _`](/blocks/pen/getPenAttribute.html) | reporter | pen | `(pen [hue])` |
| [![block 'change pen size by _'](/blocks/images/block_changeSize.png)](/blocks/pen/changeSize.html) | [`change pen size by _`](/blocks/pen/changeSize.html) | command | pen | `(+penSize 1)` |
| [![block 'set pen size to _'](/blocks/images/block_setSize.png)](/blocks/pen/setSize.html) | [`set pen size to _`](/blocks/pen/setSize.html) | command | pen | `(penSize= 1)` |
| [![block 'stamp'](/blocks/images/block_doStamp.png)](/blocks/pen/doStamp.html) | [`stamp`](/blocks/pen/doStamp.html) | command | pen | `(stamp)` |
| [![block 'fill'](/blocks/images/block_floodFill.png)](/blocks/pen/floodFill.html) | [`fill`](/blocks/pen/floodFill.html) | command | pen | `(fill)` |
| [![block 'write _ size _'](/blocks/images/block_write.png)](/blocks/pen/write.html) | [`write _ size _`](/blocks/pen/write.html) | command | pen | `(write Hello! 12)` |
| [![block 'pen trails'](/blocks/images/block_reportPenTrailsAsCostume.png)](/blocks/pen/reportPenTrailsAsCostume.html) | [`pen trails`](/blocks/pen/reportPenTrailsAsCostume.html) | reporter | pen | `(trails)` |
| [![block 'paste on _'](/blocks/images/block_doPasteOn.png)](/blocks/pen/doPasteOn.html) | [`paste on _`](/blocks/pen/doPasteOn.html) | command | pen | `(paste nil)` |
| [![block 'cut from _'](/blocks/images/block_doCutFrom.png)](/blocks/pen/doCutFrom.html) | [`cut from _`](/blocks/pen/doCutFrom.html) | command | pen | `(cut nil)` |
| [![block 'broadcast _ _'](/blocks/images/block_doBroadcast.png)](/blocks/control/doBroadcast.html) | [`broadcast _ _`](/blocks/control/doBroadcast.html) | command | control | `(send nil)` |
| [![block 'broadcast _ _ and wait'](/blocks/images/block_doBroadcastAndWait.png)](/blocks/control/doBroadcastAndWait.html) | [`broadcast _ _ and wait`](/blocks/control/doBroadcastAndWait.html) | command | control | `(sendAll nil)` |
| [![block 'wait _ secs'](/blocks/images/block_doWait.png)](/blocks/control/doWait.html) | [`wait _ secs`](/blocks/control/doWait.html) | command | control | `(wait 1)` |
| [![block 'wait until _'](/blocks/images/block_doWaitUntil.png)](/blocks/control/doWaitUntil.html) | [`wait until _`](/blocks/control/doWaitUntil.html) | command | control | `(waitUntil nil)` |
| [![block 'forever _'](/blocks/images/block_doForever.png)](/blocks/control/doForever.html) | [`forever _`](/blocks/control/doForever.html) | command | control | `(forever nil)` |
| [![block 'repeat _ _'](/blocks/images/block_doRepeat.png)](/blocks/control/doRepeat.html) | [`repeat _ _`](/blocks/control/doRepeat.html) | command | control | `(repeat 10 nil)` |
| [![block 'repeat until _ _'](/blocks/images/block_doUntil.png)](/blocks/control/doUntil.html) | [`repeat until _ _`](/blocks/control/doUntil.html) | command | control | `(until nil nil)` |
| [![block 'for _ = _ to _ _'](/blocks/images/block_doFor.png)](/blocks/control/doFor.html) | [`for _ = _ to _ _`](/blocks/control/doFor.html) | command | control | `(for i 1 10 nil)` |
| [![block 'if _ _ _'](/blocks/images/block_doIf.png)](/blocks/control/doIf.html) | [`if _ _ _`](/blocks/control/doIf.html) | command | control | `(if nil nil)` |
| [![block 'if _ _ else _'](/blocks/images/block_doIfElse.png)](/blocks/control/doIfElse.html) | [`if _ _ else _`](/blocks/control/doIfElse.html) | command | control | `(ifElse nil nil nil)` |
| [![block 'if _ then _ else _'](/blocks/images/block_reportIfElse.png)](/blocks/control/reportIfElse.html) | [`if _ then _ else _`](/blocks/control/reportIfElse.html) | reporter | control | `(ifThen nil nil nil)` |
| [![block 'report _'](/blocks/images/block_doReport.png)](/blocks/control/doReport.html) | [`report _`](/blocks/control/doReport.html) | command | control | `(report nil)` |
| [![block 'stop _'](/blocks/images/block_doStopThis.png)](/blocks/control/doStopThis.html) | [`stop _`](/blocks/control/doStopThis.html) | command | control | `(stop [all])` |
| [![block 'run _ _'](/blocks/images/block_doRun.png)](/blocks/control/doRun.html) | [`run _ _`](/blocks/control/doRun.html) | command | control | `(run nil)` |
| [![block 'launch _ _'](/blocks/images/block_fork.png)](/blocks/control/fork.html) | [`launch _ _`](/blocks/control/fork.html) | command | control | `(fork nil)` |
| [![block 'call _ _'](/blocks/images/block_evaluate.png)](/blocks/control/evaluate.html) | [`call _ _`](/blocks/control/evaluate.html) | reporter | control | `(call nil)` |
| [![block 'pipe _ $arrowRight _'](/blocks/images/block_reportPipe.png)](/blocks/control/reportPipe.html) | [`pipe _ $arrowRight _`](/blocks/control/reportPipe.html) | reporter | control | `(pipe nil nil)` |
| [![block 'tell _ to _ _'](/blocks/images/block_doTellTo.png)](/blocks/control/doTellTo.html) | [`tell _ to _ _`](/blocks/control/doTellTo.html) | command | control | `(tell nil nil)` |
| [![block 'ask _ for _ _'](/blocks/images/block_reportAskFor.png)](/blocks/control/reportAskFor.html) | [`ask _ for _ _`](/blocks/control/reportAskFor.html) | reporter | control | `(ask nil nil)` |
| [![block 'create a clone of _'](/blocks/images/block_createClone.png)](/blocks/control/createClone.html) | [`create a clone of _`](/blocks/control/createClone.html) | command | control | `(clone [myself])` |
| [![block 'a new clone of _'](/blocks/images/block_newClone.png)](/blocks/control/newClone.html) | [`a new clone of _`](/blocks/control/newClone.html) | reporter | control | `(newClone [myself])` |
| [![block 'delete this clone'](/blocks/images/block_removeClone.png)](/blocks/control/removeClone.html) | [`delete this clone`](/blocks/control/removeClone.html) | command | control | `(removeClone)` |
| [![block 'pause all $pause'](/blocks/images/block_doPauseAll.png)](/blocks/control/doPauseAll.html) | [`pause all $pause`](/blocks/control/doPauseAll.html) | command | control | `(pause)` |
| [![block 'switch to scene _ _'](/blocks/images/block_doSwitchToScene.png)](/blocks/control/doSwitchToScene.html) | [`switch to scene _ _`](/blocks/control/doSwitchToScene.html) | command | control | `(scene [next])` |
| [![block 'define _ _ _'](/blocks/images/block_doDefineBlock.png)](/blocks/control/doDefineBlock.html) | [`define _ _ _`](/blocks/control/doDefineBlock.html) | command | control | `(define block nil nil)` |
| [![block 'delete block _'](/blocks/images/block_doDeleteBlock.png)](/blocks/control/doDeleteBlock.html) | [`delete block _`](/blocks/control/doDeleteBlock.html) | command | control | `(deleteBlock nil)` |
| [![block 'set _ of block _ to _'](/blocks/images/block_doSetBlockAttribute.png)](/blocks/control/doSetBlockAttribute.html) | [`set _ of block _ to _`](/blocks/control/doSetBlockAttribute.html) | command | control | `(setBlock [label] nil nil)` |
| [![block '_ of block _'](/blocks/images/block_reportBlockAttribute.png)](/blocks/control/reportBlockAttribute.html) | [`_ of block _`](/blocks/control/reportBlockAttribute.html) | reporter | control | `(block [definition] nil)` |
| [![block 'this _'](/blocks/images/block_reportEnvironment.png)](/blocks/control/reportEnvironment.html) | [`this _`](/blocks/control/reportEnvironment.html) | reporter | control | `(this [script])` |
| [![block 'set slot _ to _'](/blocks/images/block_doSetSlot.png)](/blocks/control/doSetSlot.html) | [`set slot _ to _`](/blocks/control/doSetSlot.html) | command | control | `(doSetSlot nil nil)` |
| [![block 'touching _ ?'](/blocks/images/block_reportTouchingObject.png)](/blocks/sensing/reportTouchingObject.html) | [`touching _ ?`](/blocks/sensing/reportTouchingObject.html) | predicate | sensing | `(touch [mouse-pointer])` |
| [![block 'touching _ ?'](/blocks/images/block_reportTouchingColor.png)](/blocks/sensing/reportTouchingColor.html) | [`touching _ ?`](/blocks/sensing/reportTouchingColor.html) | predicate | sensing | `(touchColor "rgba(145,26,68,1)")` |
| [![block 'color _ is touching _ ?'](/blocks/images/block_reportColorIsTouchingColor.png)](/blocks/sensing/reportColorIsTouchingColor.html) | [`color _ is touching _ ?`](/blocks/sensing/reportColorIsTouchingColor.html) | predicate | sensing | `(colorTouch "rgba(145,26,68,1)" "rgba(145,26,68,1)")` |
| [![block 'ask _ and wait'](/blocks/images/block_doAsk.png)](/blocks/sensing/doAsk.html) | [`ask _ and wait`](/blocks/sensing/doAsk.html) | command | sensing | `(doAsk "what's your name?")` |
| [![block 'answer'](/blocks/images/block_getLastAnswer.png)](/blocks/sensing/getLastAnswer.html) | [`answer`](/blocks/sensing/getLastAnswer.html) | reporter | sensing | `(answer)` |
| [![block 'mouse position'](/blocks/images/block_reportMousePosition.png)](/blocks/sensing/reportMousePosition.html) | [`mouse position`](/blocks/sensing/reportMousePosition.html) | reporter | sensing | `(mouse)` |
| [![block 'mouse x'](/blocks/images/block_reportMouseX.png)](/blocks/sensing/reportMouseX.html) | [`mouse x`](/blocks/sensing/reportMouseX.html) | reporter | sensing | `(mouseX)` |
| [![block 'mouse y'](/blocks/images/block_reportMouseY.png)](/blocks/sensing/reportMouseY.html) | [`mouse y`](/blocks/sensing/reportMouseY.html) | reporter | sensing | `(mouseY)` |
| [![block 'mouse down?'](/blocks/images/block_reportMouseDown.png)](/blocks/sensing/reportMouseDown.html) | [`mouse down?`](/blocks/sensing/reportMouseDown.html) | predicate | sensing | `(mouseDown)` |
| [![block 'key _ pressed?'](/blocks/images/block_reportKeyPressed.png)](/blocks/sensing/reportKeyPressed.html) | [`key _ pressed?`](/blocks/sensing/reportKeyPressed.html) | predicate | sensing | `(key [space])` |
| [![block '_ to _'](/blocks/images/block_reportRelationTo.png)](/blocks/sensing/reportRelationTo.html) | [`_ to _`](/blocks/sensing/reportRelationTo.html) | reporter | sensing | `(relation [distance] [mouse-pointer])` |
| [![block '_ at _'](/blocks/images/block_reportAspect.png)](/blocks/sensing/reportAspect.html) | [`_ at _`](/blocks/sensing/reportAspect.html) | reporter | sensing | `(aspect [hue] [mouse-pointer])` |
| [![block 'reset timer'](/blocks/images/block_doResetTimer.png)](/blocks/sensing/doResetTimer.html) | [`reset timer`](/blocks/sensing/doResetTimer.html) | command | sensing | `(resetTimer)` |
| [![block 'timer'](/blocks/images/block_getTimer.png)](/blocks/sensing/getTimer.html) | [`timer`](/blocks/sensing/getTimer.html) | reporter | sensing | `(timer)` |
| [![block 'current _'](/blocks/images/block_reportDate.png)](/blocks/sensing/reportDate.html) | [`current _`](/blocks/sensing/reportDate.html) | reporter | sensing | `(current [date])` |
| [![block '_ of _'](/blocks/images/block_reportAttributeOf.png)](/blocks/sensing/reportAttributeOf.html) | [`_ of _`](/blocks/sensing/reportAttributeOf.html) | reporter | sensing | `(attribute "[costume #]" nil)` |
| [![block 'my _'](/blocks/images/block_reportGet.png)](/blocks/sensing/reportGet.html) | [`my _`](/blocks/sensing/reportGet.html) | reporter | sensing | `(my [neighbors])` |
| [![block 'object _'](/blocks/images/block_reportObject.png)](/blocks/sensing/reportObject.html) | [`object _`](/blocks/sensing/reportObject.html) | reporter | sensing | `(object [myself])` |
| [![block 'url _'](/blocks/images/block_reportURL.png)](/blocks/sensing/reportURL.html) | [`url _`](/blocks/sensing/reportURL.html) | reporter | sensing | `(url snap.berkeley.edu)` |
| [![block 'microphone _'](/blocks/images/block_reportAudio.png)](/blocks/sensing/reportAudio.html) | [`microphone _`](/blocks/sensing/reportAudio.html) | reporter | sensing | `(audio [volume])` |
| [![block 'video _ on _'](/blocks/images/block_reportVideo.png)](/blocks/sensing/reportVideo.html) | [`video _ on _`](/blocks/sensing/reportVideo.html) | reporter | sensing | `(video [motion] [myself])` |
| [![block 'set video transparency to _'](/blocks/images/block_doSetVideoTransparency.png)](/blocks/sensing/doSetVideoTransparency.html) | [`set video transparency to _`](/blocks/sensing/doSetVideoTransparency.html) | command | sensing | `(transparency 50)` |
| [![block 'is _ on?'](/blocks/images/block_reportGlobalFlag.png)](/blocks/sensing/reportGlobalFlag.html) | [`is _ on?`](/blocks/sensing/reportGlobalFlag.html) | predicate | sensing | `(global "[turbo mode]")` |
| [![block 'set _ to _'](/blocks/images/block_doSetGlobalFlag.png)](/blocks/sensing/doSetGlobalFlag.html) | [`set _ to _`](/blocks/sensing/doSetGlobalFlag.html) | command | sensing | `(global= "[video capture]" nil)` |
| [![block '_'](/blocks/images/block_reportVariadicSum.png)](/blocks/operators/reportVariadicSum.html) | [`_`](/blocks/operators/reportVariadicSum.html) | reporter | operators | `(+ nil nil)` |
| [![block '_ − _'](/blocks/images/block_reportDifference.png)](/blocks/operators/reportDifference.html) | [`_ − _`](/blocks/operators/reportDifference.html) | reporter | operators | `(- nil nil)` |
| [![block '_'](/blocks/images/block_reportVariadicProduct.png)](/blocks/operators/reportVariadicProduct.html) | [`_`](/blocks/operators/reportVariadicProduct.html) | reporter | operators | `(* nil nil)` |
| [![block '_ / _'](/blocks/images/block_reportQuotient.png)](/blocks/operators/reportQuotient.html) | [`_ / _`](/blocks/operators/reportQuotient.html) | reporter | operators | `(/ nil nil)` |
| [![block '_ ^ _'](/blocks/images/block_reportPower.png)](/blocks/operators/reportPower.html) | [`_ ^ _`](/blocks/operators/reportPower.html) | reporter | operators | `(^ nil nil)` |
| [![block '_ mod _'](/blocks/images/block_reportModulus.png)](/blocks/operators/reportModulus.html) | [`_ mod _`](/blocks/operators/reportModulus.html) | reporter | operators | `(mod nil nil)` |
| [![block '_'](/blocks/images/block_reportVariadicMin.png)](/blocks/operators/reportVariadicMin.html) | [`_`](/blocks/operators/reportVariadicMin.html) | reporter | operators | `(min nil nil)` |
| [![block '_'](/blocks/images/block_reportVariadicMax.png)](/blocks/operators/reportVariadicMax.html) | [`_`](/blocks/operators/reportVariadicMax.html) | reporter | operators | `(max nil nil)` |
| [![block 'round _'](/blocks/images/block_reportRound.png)](/blocks/operators/reportRound.html) | [`round _`](/blocks/operators/reportRound.html) | reporter | operators | `(round nil)` |
| [![block '_ of _'](/blocks/images/block_reportMonadic.png)](/blocks/operators/reportMonadic.html) | [`_ of _`](/blocks/operators/reportMonadic.html) | reporter | operators | `(fn [sqrt] 10)` |
| [![block 'atan2 _ ÷ _'](/blocks/images/block_reportAtan2.png)](/blocks/operators/reportAtan2.html) | [`atan2 _ ÷ _`](/blocks/operators/reportAtan2.html) | reporter | operators | `(atan2 nil nil)` |
| [![block 'pick random _ to _'](/blocks/images/block_reportRandom.png)](/blocks/operators/reportRandom.html) | [`pick random _ to _`](/blocks/operators/reportRandom.html) | reporter | operators | `(rand 1 10)` |
| [![block '_'](/blocks/images/block_reportVariadicLessThan.png)](/blocks/operators/reportVariadicLessThan.html) | [`_`](/blocks/operators/reportVariadicLessThan.html) | predicate | operators | `(< nil nil)` |
| [![block '_'](/blocks/images/block_reportVariadicEquals.png)](/blocks/operators/reportVariadicEquals.html) | [`_`](/blocks/operators/reportVariadicEquals.html) | predicate | operators | `(= nil nil)` |
| [![block '_'](/blocks/images/block_reportVariadicGreaterThan.png)](/blocks/operators/reportVariadicGreaterThan.html) | [`_`](/blocks/operators/reportVariadicGreaterThan.html) | predicate | operators | `(> nil nil)` |
| [![block '_'](/blocks/images/block_reportVariadicAnd.png)](/blocks/operators/reportVariadicAnd.html) | [`_`](/blocks/operators/reportVariadicAnd.html) | predicate | operators | `(and nil nil)` |
| [![block '_'](/blocks/images/block_reportVariadicOr.png)](/blocks/operators/reportVariadicOr.html) | [`_`](/blocks/operators/reportVariadicOr.html) | predicate | operators | `(or nil nil)` |
| [![block 'not _'](/blocks/images/block_reportNot.png)](/blocks/operators/reportNot.html) | [`not _`](/blocks/operators/reportNot.html) | predicate | operators | `(not nil)` |
| [![block '_'](/blocks/images/block_reportBoolean.png)](/blocks/operators/reportBoolean.html) | [`_`](/blocks/operators/reportBoolean.html) | predicate | operators | `(bool t)` |
| [![block 'join _'](/blocks/images/block_reportJoinWords.png)](/blocks/operators/reportJoinWords.html) | [`join _`](/blocks/operators/reportJoinWords.html) | reporter | operators | `(join "hello " world)` |
| [![block 'split _ by _'](/blocks/images/block_reportTextSplit.png)](/blocks/operators/reportTextSplit.html) | [`split _ by _`](/blocks/operators/reportTextSplit.html) | reporter | operators | `(split "hello world" " ")` |
| [![block 'letter _ of _'](/blocks/images/block_reportLetter.png)](/blocks/operators/reportLetter.html) | [`letter _ of _`](/blocks/operators/reportLetter.html) | reporter | operators | `(letter 1 world)` |
| [![block '_ of text _'](/blocks/images/block_reportTextAttribute.png)](/blocks/operators/reportTextAttribute.html) | [`_ of text _`](/blocks/operators/reportTextAttribute.html) | reporter | operators | `(text [length] world)` |
| [![block 'unicode of _'](/blocks/images/block_reportUnicode.png)](/blocks/operators/reportUnicode.html) | [`unicode of _`](/blocks/operators/reportUnicode.html) | reporter | operators | `(unicode a)` |
| [![block 'unicode _ as letter'](/blocks/images/block_reportUnicodeAsLetter.png)](/blocks/operators/reportUnicodeAsLetter.html) | [`unicode _ as letter`](/blocks/operators/reportUnicodeAsLetter.html) | reporter | operators | `(toLetter 65)` |
| [![block 'is _ a _ ?'](/blocks/images/block_reportIsA.png)](/blocks/operators/reportIsA.html) | [`is _ a _ ?`](/blocks/operators/reportIsA.html) | predicate | operators | `(is 5 [number])` |
| [![block 'is _ ?'](/blocks/images/block_reportVariadicIsIdentical.png)](/blocks/operators/reportVariadicIsIdentical.html) | [`is _ ?`](/blocks/operators/reportVariadicIsIdentical.html) | predicate | operators | `(same nil nil)` |
| [![block 'JavaScript function ( _ ) { _ }'](/blocks/images/block_reportJSFunction.png)](/blocks/operators/reportJSFunction.html) | [`JavaScript function ( _ ) { _ }`](/blocks/operators/reportJSFunction.html) | reporter | operators | `(js nil nil)` |
| [![block 'set _ to _'](/blocks/images/block_doSetVar.png)](/blocks/variables/doSetVar.html) | [`set _ to _`](/blocks/variables/doSetVar.html) | command | variables | `(set nil 0)` |
| [![block 'change _ by _'](/blocks/images/block_doChangeVar.png)](/blocks/variables/doChangeVar.html) | [`change _ by _`](/blocks/variables/doChangeVar.html) | command | variables | `(+= nil 1)` |
| [![block 'show variable _'](/blocks/images/block_doShowVar.png)](/blocks/variables/doShowVar.html) | [`show variable _`](/blocks/variables/doShowVar.html) | command | variables | `(showVar nil)` |
| [![block 'hide variable _'](/blocks/images/block_doHideVar.png)](/blocks/variables/doHideVar.html) | [`hide variable _`](/blocks/variables/doHideVar.html) | command | variables | `(hideVar nil)` |
| [![block 'inherit _'](/blocks/images/block_doDeleteAttr.png)](/blocks/variables/doDeleteAttr.html) | [`inherit _`](/blocks/variables/doDeleteAttr.html) | command | variables | `(inherit nil)` |
| [![block 'list _'](/blocks/images/block_reportNewList.png)](/blocks/lists/reportNewList.html) | [`list _`](/blocks/lists/reportNewList.html) | reporter | lists | `(list nil)` |
| [![block 'numbers from _ to _'](/blocks/images/block_reportNumbers.png)](/blocks/lists/reportNumbers.html) | [`numbers from _ to _`](/blocks/lists/reportNumbers.html) | reporter | lists | `(range 1 10)` |
| [![block '_ in front of _'](/blocks/images/block_reportCONS.png)](/blocks/lists/reportCONS.html) | [`_ in front of _`](/blocks/lists/reportCONS.html) | reporter | lists | `(cons nil nil)` |
| [![block 'item _ of _'](/blocks/images/block_reportListItem.png)](/blocks/lists/reportListItem.html) | [`item _ of _`](/blocks/lists/reportListItem.html) | reporter | lists | `(item 1 nil)` |
| [![block 'all but first of _'](/blocks/images/block_reportCDR.png)](/blocks/lists/reportCDR.html) | [`all but first of _`](/blocks/lists/reportCDR.html) | reporter | lists | `(cdr nil)` |
| [![block '_ of _'](/blocks/images/block_reportListAttribute.png)](/blocks/lists/reportListAttribute.html) | [`_ of _`](/blocks/lists/reportListAttribute.html) | reporter | lists | `(data [length] nil)` |
| [![block 'index of _ in _'](/blocks/images/block_reportListIndex.png)](/blocks/lists/reportListIndex.html) | [`index of _ in _`](/blocks/lists/reportListIndex.html) | reporter | lists | `(# thing nil)` |
| [![block '_ contains _'](/blocks/images/block_reportListContainsItem.png)](/blocks/lists/reportListContainsItem.html) | [`_ contains _`](/blocks/lists/reportListContainsItem.html) | predicate | lists | `(contains nil thing)` |
| [![block 'is _ empty?'](/blocks/images/block_reportListIsEmpty.png)](/blocks/lists/reportListIsEmpty.html) | [`is _ empty?`](/blocks/lists/reportListIsEmpty.html) | predicate | lists | `(empty nil)` |
| [![block 'map _ over _'](/blocks/images/block_reportMap.png)](/blocks/lists/reportMap.html) | [`map _ over _`](/blocks/lists/reportMap.html) | reporter | lists | `(map nil nil)` |
| [![block 'keep items _ from _'](/blocks/images/block_reportKeep.png)](/blocks/lists/reportKeep.html) | [`keep items _ from _`](/blocks/lists/reportKeep.html) | reporter | lists | `(keep nil nil)` |
| [![block 'find first item _ in _'](/blocks/images/block_reportFindFirst.png)](/blocks/lists/reportFindFirst.html) | [`find first item _ in _`](/blocks/lists/reportFindFirst.html) | reporter | lists | `(find nil nil)` |
| [![block 'combine _ using _'](/blocks/images/block_reportCombine.png)](/blocks/lists/reportCombine.html) | [`combine _ using _`](/blocks/lists/reportCombine.html) | reporter | lists | `(combine nil nil)` |
| [![block 'for each _ in _ _'](/blocks/images/block_doForEach.png)](/blocks/lists/doForEach.html) | [`for each _ in _ _`](/blocks/lists/doForEach.html) | command | lists | `(forEach item nil nil)` |
| [![block 'add _ to _'](/blocks/images/block_doAddToList.png)](/blocks/lists/doAddToList.html) | [`add _ to _`](/blocks/lists/doAddToList.html) | command | lists | `(add thing nil)` |
| [![block 'delete _ of _'](/blocks/images/block_doDeleteFromList.png)](/blocks/lists/doDeleteFromList.html) | [`delete _ of _`](/blocks/lists/doDeleteFromList.html) | command | lists | `(del 1 nil)` |
| [![block 'insert _ at _ of _'](/blocks/images/block_doInsertInList.png)](/blocks/lists/doInsertInList.html) | [`insert _ at _ of _`](/blocks/lists/doInsertInList.html) | command | lists | `(ins thing 1 nil)` |
| [![block 'replace item _ of _ with _'](/blocks/images/block_doReplaceInList.png)](/blocks/lists/doReplaceInList.html) | [`replace item _ of _ with _`](/blocks/lists/doReplaceInList.html) | command | lists | `(put 1 nil thing)` |
| [![block 'append _'](/blocks/images/block_reportConcatenatedLists.png)](/blocks/lists/reportConcatenatedLists.html) | [`append _`](/blocks/lists/reportConcatenatedLists.html) | reporter | lists | `(append nil nil)` |
| [![block 'reshape _ to _'](/blocks/images/block_reportReshape.png)](/blocks/lists/reportReshape.html) | [`reshape _ to _`](/blocks/lists/reportReshape.html) | reporter | lists | `(reshape nil 4 3)` |
| [![block 'combinations _'](/blocks/images/block_reportCrossproduct.png)](/blocks/lists/reportCrossproduct.html) | [`combinations _`](/blocks/lists/reportCrossproduct.html) | reporter | lists | `(combinations nil nil)` |
