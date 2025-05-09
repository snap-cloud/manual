---
page-layout: full
margin-width: 1px
---

# All Snap<em>!</em> Blocks Reference {.unnumbered}

<!-- TODO: These images are missing:
reportNewCostumeSkewed
reportNewCostume
reportNewSoundFromSamples
changePenColorDimension
setPenColorDimension
reportPipe
doDefineBlock
doSetBlockAttribute
reportBlockAttribute
reportEnvironment
doSetSlot
reportMousePosition
reportVariadicMin
reportVariadicMax
reportAtan2
reportVariadicLessThan
reportVariadicEquals
reportVariadicGreaterThan
reportTextAttribute
reportCrossproduct
-->

| Block | Image | Type | Category | Is Primitive? |
| ----- | ----- | ---- | -------- | ------------- |
| [`move _ steps`](/blocks/motion/forward.html) | [![block 'move _ steps'](/blocks/images/block_forward.png)](/blocks/motion/forward.html) | command | motion | true |
| [`turn $clockwise _ degrees`](/blocks/motion/turn.html) | [![block 'turn $clockwise _ degrees'](/blocks/images/block_turn.png)](/blocks/motion/turn.html) | command | motion | true |
| [`turn $counterclockwise _ degrees`](/blocks/motion/turnLeft.html) | [![block 'turn $counterclockwise _ degrees'](/blocks/images/block_turnLeft.png)](/blocks/motion/turnLeft.html) | command | motion | true |
| [`point in direction _`](/blocks/motion/setHeading.html) | [![block 'point in direction _'](/blocks/images/block_setHeading.png)](/blocks/motion/setHeading.html) | command | motion | true |
| [`point towards _`](/blocks/motion/doFaceTowards.html) | [![block 'point towards _'](/blocks/images/block_doFaceTowards.png)](/blocks/motion/doFaceTowards.html) | command | motion | true |
| [`go to x: _ y: _`](/blocks/motion/gotoXY.html) | [![block 'go to x: _ y: _'](/blocks/images/block_gotoXY.png)](/blocks/motion/gotoXY.html) | command | motion | true |
| [`go to _`](/blocks/motion/doGotoObject.html) | [![block 'go to _'](/blocks/images/block_doGotoObject.png)](/blocks/motion/doGotoObject.html) | command | motion | true |
| [`glide _ secs to x: _ y: _`](/blocks/motion/doGlide.html) | [![block 'glide _ secs to x: _ y: _'](/blocks/images/block_doGlide.png)](/blocks/motion/doGlide.html) | command | motion | true |
| [`change x by _`](/blocks/motion/changeXPosition.html) | [![block 'change x by _'](/blocks/images/block_changeXPosition.png)](/blocks/motion/changeXPosition.html) | command | motion | true |
| [`set x to _`](/blocks/motion/setXPosition.html) | [![block 'set x to _'](/blocks/images/block_setXPosition.png)](/blocks/motion/setXPosition.html) | command | motion | true |
| [`change y by _`](/blocks/motion/changeYPosition.html) | [![block 'change y by _'](/blocks/images/block_changeYPosition.png)](/blocks/motion/changeYPosition.html) | command | motion | true |
| [`set y to _`](/blocks/motion/setYPosition.html) | [![block 'set y to _'](/blocks/images/block_setYPosition.png)](/blocks/motion/setYPosition.html) | command | motion | true |
| [`if on edge, bounce`](/blocks/motion/bounceOffEdge.html) | [![block 'if on edge, bounce'](/blocks/images/block_bounceOffEdge.png)](/blocks/motion/bounceOffEdge.html) | command | motion | true |
| [`position`](/blocks/motion/getPosition.html) | [![block 'position'](/blocks/images/block_getPosition.png)](/blocks/motion/getPosition.html) | reporter | motion | true |
| [`x position`](/blocks/motion/xPosition.html) | [![block 'x position'](/blocks/images/block_xPosition.png)](/blocks/motion/xPosition.html) | reporter | motion | true |
| [`y position`](/blocks/motion/yPosition.html) | [![block 'y position'](/blocks/images/block_yPosition.png)](/blocks/motion/yPosition.html) | reporter | motion | true |
| [`direction`](/blocks/motion/direction.html) | [![block 'direction'](/blocks/images/block_direction.png)](/blocks/motion/direction.html) | reporter | motion | true |
| [`switch to costume _`](/blocks/looks/doSwitchToCostume.html) | [![block 'switch to costume _'](/blocks/images/block_doSwitchToCostume.png)](/blocks/looks/doSwitchToCostume.html) | command | looks | true |
| [`next costume`](/blocks/looks/doWearNextCostume.html) | [![block 'next costume'](/blocks/images/block_doWearNextCostume.png)](/blocks/looks/doWearNextCostume.html) | command | looks | true |
| [`costume #`](/blocks/looks/getCostumeIdx.html) | [![block 'costume #'](/blocks/images/block_getCostumeIdx.png)](/blocks/looks/getCostumeIdx.html) | reporter | looks | true |
| [`say _ for _ secs`](/blocks/looks/doSayFor.html) | [![block 'say _ for _ secs'](/blocks/images/block_doSayFor.png)](/blocks/looks/doSayFor.html) | command | looks | true |
| [`say _`](/blocks/looks/bubble.html) | [![block 'say _'](/blocks/images/block_bubble.png)](/blocks/looks/bubble.html) | command | looks | true |
| [`think _ for _ secs`](/blocks/looks/doThinkFor.html) | [![block 'think _ for _ secs'](/blocks/images/block_doThinkFor.png)](/blocks/looks/doThinkFor.html) | command | looks | true |
| [`think _`](/blocks/looks/doThink.html) | [![block 'think _'](/blocks/images/block_doThink.png)](/blocks/looks/doThink.html) | command | looks | true |
| [`_ of costume _`](/blocks/looks/reportGetImageAttribute.html) | [![block '_ of costume _'](/blocks/images/block_reportGetImageAttribute.png)](/blocks/looks/reportGetImageAttribute.html) | reporter | looks | true |
| [`stretch _ x: _ y: _ %`](/blocks/looks/reportNewCostumeStretched.html) | [![block 'stretch _ x: _ y: _ %'](/blocks/images/block_reportNewCostumeStretched.png)](/blocks/looks/reportNewCostumeStretched.html) | reporter | looks | true |
| [`skew _ to _ degrees _ %`](/blocks/looks/reportNewCostumeSkewed.html) | no help screen | reporter | looks | true |
| [`new costume _ width _ height _`](/blocks/looks/reportNewCostume.html) | no help screen | reporter | looks | true |
| [`change _ effect by _`](/blocks/looks/changeEffect.html) | [![block 'change _ effect by _'](/blocks/images/block_changeEffect.png)](/blocks/looks/changeEffect.html) | command | looks | true |
| [`set _ effect to _`](/blocks/looks/setEffect.html) | [![block 'set _ effect to _'](/blocks/images/block_setEffect.png)](/blocks/looks/setEffect.html) | command | looks | true |
| [`clear graphic effects`](/blocks/looks/clearEffects.html) | [![block 'clear graphic effects'](/blocks/images/block_clearEffects.png)](/blocks/looks/clearEffects.html) | command | looks | true |
| [`_ effect`](/blocks/looks/getEffect.html) | [![block '_ effect'](/blocks/images/block_getEffect.png)](/blocks/looks/getEffect.html) | reporter | looks | true |
| [`change size by _`](/blocks/looks/changeScale.html) | [![block 'change size by _'](/blocks/images/block_changeScale.png)](/blocks/looks/changeScale.html) | command | looks | true |
| [`set size to _ %`](/blocks/looks/setScale.html) | [![block 'set size to _ %'](/blocks/images/block_setScale.png)](/blocks/looks/setScale.html) | command | looks | true |
| [`size`](/blocks/looks/getScale.html) | [![block 'size'](/blocks/images/block_getScale.png)](/blocks/looks/getScale.html) | reporter | looks | true |
| [`show`](/blocks/looks/show.html) | [![block 'show'](/blocks/images/block_show.png)](/blocks/looks/show.html) | command | looks | true |
| [`hide`](/blocks/looks/hide.html) | [![block 'hide'](/blocks/images/block_hide.png)](/blocks/looks/hide.html) | command | looks | true |
| [`shown?`](/blocks/looks/reportShown.html) | [![block 'shown?'](/blocks/images/block_reportShown.png)](/blocks/looks/reportShown.html) | predicate | looks | true |
| [`go to _ layer`](/blocks/looks/goToLayer.html) | [![block 'go to _ layer'](/blocks/images/block_goToLayer.png)](/blocks/looks/goToLayer.html) | command | looks | true |
| [`go back _ layers`](/blocks/looks/goBack.html) | [![block 'go back _ layers'](/blocks/images/block_goBack.png)](/blocks/looks/goBack.html) | command | looks | true |
| [`play sound _`](/blocks/sound/playSound.html) | [![block 'play sound _'](/blocks/images/block_playSound.png)](/blocks/sound/playSound.html) | command | sound | true |
| [`play sound _ until done`](/blocks/sound/doPlaySoundUntilDone.html) | [![block 'play sound _ until done'](/blocks/images/block_doPlaySoundUntilDone.png)](/blocks/sound/doPlaySoundUntilDone.html) | command | sound | true |
| [`stop all sounds`](/blocks/sound/doStopAllSounds.html) | [![block 'stop all sounds'](/blocks/images/block_doStopAllSounds.png)](/blocks/sound/doStopAllSounds.html) | command | sound | true |
| [`play sound _ at _ Hz`](/blocks/sound/doPlaySoundAtRate.html) | [![block 'play sound _ at _ Hz'](/blocks/images/block_doPlaySoundAtRate.png)](/blocks/sound/doPlaySoundAtRate.html) | command | sound | true |
| [`_ of sound _`](/blocks/sound/reportGetSoundAttribute.html) | [![block '_ of sound _'](/blocks/images/block_reportGetSoundAttribute.png)](/blocks/sound/reportGetSoundAttribute.html) | reporter | sound | true |
| [`new sound _ rate _ Hz`](/blocks/sound/reportNewSoundFromSamples.html) | no help screen | reporter | sound | true |
| [`rest for _ beats`](/blocks/sound/doRest.html) | [![block 'rest for _ beats'](/blocks/images/block_doRest.png)](/blocks/sound/doRest.html) | command | sound | true |
| [`play note _ for _ beats`](/blocks/sound/doPlayNote.html) | [![block 'play note _ for _ beats'](/blocks/images/block_doPlayNote.png)](/blocks/sound/doPlayNote.html) | command | sound | true |
| [`set instrument to _`](/blocks/sound/doSetInstrument.html) | [![block 'set instrument to _'](/blocks/images/block_doSetInstrument.png)](/blocks/sound/doSetInstrument.html) | command | sound | true |
| [`change tempo by _`](/blocks/sound/doChangeTempo.html) | [![block 'change tempo by _'](/blocks/images/block_doChangeTempo.png)](/blocks/sound/doChangeTempo.html) | command | sound | true |
| [`set tempo to _ bpm`](/blocks/sound/doSetTempo.html) | [![block 'set tempo to _ bpm'](/blocks/images/block_doSetTempo.png)](/blocks/sound/doSetTempo.html) | command | sound | true |
| [`tempo`](/blocks/sound/getTempo.html) | [![block 'tempo'](/blocks/images/block_getTempo.png)](/blocks/sound/getTempo.html) | reporter | sound | true |
| [`change volume by _`](/blocks/sound/changeVolume.html) | [![block 'change volume by _'](/blocks/images/block_changeVolume.png)](/blocks/sound/changeVolume.html) | command | sound | true |
| [`set volume to _ %`](/blocks/sound/setVolume.html) | [![block 'set volume to _ %'](/blocks/images/block_setVolume.png)](/blocks/sound/setVolume.html) | command | sound | true |
| [`volume`](/blocks/sound/getVolume.html) | [![block 'volume'](/blocks/images/block_getVolume.png)](/blocks/sound/getVolume.html) | reporter | sound | true |
| [`change balance by _`](/blocks/sound/changePan.html) | [![block 'change balance by _'](/blocks/images/block_changePan.png)](/blocks/sound/changePan.html) | command | sound | true |
| [`set balance to _`](/blocks/sound/setPan.html) | [![block 'set balance to _'](/blocks/images/block_setPan.png)](/blocks/sound/setPan.html) | command | sound | true |
| [`balance`](/blocks/sound/getPan.html) | [![block 'balance'](/blocks/images/block_getPan.png)](/blocks/sound/getPan.html) | reporter | sound | true |
| [`play frequency _ Hz`](/blocks/sound/playFreq.html) | [![block 'play frequency _ Hz'](/blocks/images/block_playFreq.png)](/blocks/sound/playFreq.html) | command | sound | true |
| [`stop frequency`](/blocks/sound/stopFreq.html) | [![block 'stop frequency'](/blocks/images/block_stopFreq.png)](/blocks/sound/stopFreq.html) | command | sound | true |
| [`clear`](/blocks/pen/clear.html) | [![block 'clear'](/blocks/images/block_clear.png)](/blocks/pen/clear.html) | command | pen | true |
| [`pen down`](/blocks/pen/down.html) | [![block 'pen down'](/blocks/images/block_down.png)](/blocks/pen/down.html) | command | pen | true |
| [`pen up`](/blocks/pen/up.html) | [![block 'pen up'](/blocks/images/block_up.png)](/blocks/pen/up.html) | command | pen | true |
| [`pen down?`](/blocks/pen/getPenDown.html) | [![block 'pen down?'](/blocks/images/block_getPenDown.png)](/blocks/pen/getPenDown.html) | predicate | pen | true |
| [`set pen color to _`](/blocks/pen/setColor.html) | [![block 'set pen color to _'](/blocks/images/block_setColor.png)](/blocks/pen/setColor.html) | command | pen | true |
| [`change pen _ by _`](/blocks/pen/changePenColorDimension.html) | no help screen | command | pen | true |
| [`set pen _ to _`](/blocks/pen/setPenColorDimension.html) | no help screen | command | pen | true |
| [`pen _`](/blocks/pen/getPenAttribute.html) | [![block 'pen _'](/blocks/images/block_getPenAttribute.png)](/blocks/pen/getPenAttribute.html) | reporter | pen | true |
| [`change pen size by _`](/blocks/pen/changeSize.html) | [![block 'change pen size by _'](/blocks/images/block_changeSize.png)](/blocks/pen/changeSize.html) | command | pen | true |
| [`set pen size to _`](/blocks/pen/setSize.html) | [![block 'set pen size to _'](/blocks/images/block_setSize.png)](/blocks/pen/setSize.html) | command | pen | true |
| [`stamp`](/blocks/pen/doStamp.html) | [![block 'stamp'](/blocks/images/block_doStamp.png)](/blocks/pen/doStamp.html) | command | pen | true |
| [`fill`](/blocks/pen/floodFill.html) | [![block 'fill'](/blocks/images/block_floodFill.png)](/blocks/pen/floodFill.html) | command | pen | true |
| [`write _ size _`](/blocks/pen/write.html) | [![block 'write _ size _'](/blocks/images/block_write.png)](/blocks/pen/write.html) | command | pen | true |
| [`pen trails`](/blocks/pen/reportPenTrailsAsCostume.html) | [![block 'pen trails'](/blocks/images/block_reportPenTrailsAsCostume.png)](/blocks/pen/reportPenTrailsAsCostume.html) | reporter | pen | true |
| [`paste on _`](/blocks/pen/doPasteOn.html) | [![block 'paste on _'](/blocks/images/block_doPasteOn.png)](/blocks/pen/doPasteOn.html) | command | pen | true |
| [`cut from _`](/blocks/pen/doCutFrom.html) | [![block 'cut from _'](/blocks/images/block_doCutFrom.png)](/blocks/pen/doCutFrom.html) | command | pen | true |
| [`broadcast _ _`](/blocks/control/doBroadcast.html) | [![block 'broadcast _ _'](/blocks/images/block_doBroadcast.png)](/blocks/control/doBroadcast.html) | command | control | true |
| [`broadcast _ _ and wait`](/blocks/control/doBroadcastAndWait.html) | [![block 'broadcast _ _ and wait'](/blocks/images/block_doBroadcastAndWait.png)](/blocks/control/doBroadcastAndWait.html) | command | control | true |
| [`wait _ secs`](/blocks/control/doWait.html) | [![block 'wait _ secs'](/blocks/images/block_doWait.png)](/blocks/control/doWait.html) | command | control | true |
| [`wait until _`](/blocks/control/doWaitUntil.html) | [![block 'wait until _'](/blocks/images/block_doWaitUntil.png)](/blocks/control/doWaitUntil.html) | command | control | true |
| [`forever _`](/blocks/control/doForever.html) | [![block 'forever _'](/blocks/images/block_doForever.png)](/blocks/control/doForever.html) | command | control | true |
| [`repeat _ _`](/blocks/control/doRepeat.html) | [![block 'repeat _ _'](/blocks/images/block_doRepeat.png)](/blocks/control/doRepeat.html) | command | control | true |
| [`repeat until _ _`](/blocks/control/doUntil.html) | [![block 'repeat until _ _'](/blocks/images/block_doUntil.png)](/blocks/control/doUntil.html) | command | control | true |
| [`for _ = _ to _ _`](/blocks/control/doFor.html) | [![block 'for _ = _ to _ _'](/blocks/images/block_doFor.png)](/blocks/control/doFor.html) | command | control | true |
| [`if _ _ _`](/blocks/control/doIf.html) | [![block 'if _ _ _'](/blocks/images/block_doIf.png)](/blocks/control/doIf.html) | command | control | true |
| [`if _ _ else _`](/blocks/control/doIfElse.html) | [![block 'if _ _ else _'](/blocks/images/block_doIfElse.png)](/blocks/control/doIfElse.html) | command | control | true |
| [`if _ then _ else _`](/blocks/control/reportIfElse.html) | [![block 'if _ then _ else _'](/blocks/images/block_reportIfElse.png)](/blocks/control/reportIfElse.html) | reporter | control | true |
| [`report _`](/blocks/control/doReport.html) | [![block 'report _'](/blocks/images/block_doReport.png)](/blocks/control/doReport.html) | command | control | true |
| [`stop _`](/blocks/control/doStopThis.html) | [![block 'stop _'](/blocks/images/block_doStopThis.png)](/blocks/control/doStopThis.html) | command | control | true |
| [`run _ _`](/blocks/control/doRun.html) | [![block 'run _ _'](/blocks/images/block_doRun.png)](/blocks/control/doRun.html) | command | control | true |
| [`launch _ _`](/blocks/control/fork.html) | [![block 'launch _ _'](/blocks/images/block_fork.png)](/blocks/control/fork.html) | command | control | true |
| [`call _ _`](/blocks/control/evaluate.html) | [![block 'call _ _'](/blocks/images/block_evaluate.png)](/blocks/control/evaluate.html) | reporter | control | true |
| [`pipe _ $arrowRight _`](/blocks/control/reportPipe.html) | no help screen | reporter | control | true |
| [`tell _ to _ _`](/blocks/control/doTellTo.html) | [![block 'tell _ to _ _'](/blocks/images/block_doTellTo.png)](/blocks/control/doTellTo.html) | command | control | true |
| [`ask _ for _ _`](/blocks/control/reportAskFor.html) | [![block 'ask _ for _ _'](/blocks/images/block_reportAskFor.png)](/blocks/control/reportAskFor.html) | reporter | control | true |
| [`create a clone of _`](/blocks/control/createClone.html) | [![block 'create a clone of _'](/blocks/images/block_createClone.png)](/blocks/control/createClone.html) | command | control | true |
| [`a new clone of _`](/blocks/control/newClone.html) | [![block 'a new clone of _'](/blocks/images/block_newClone.png)](/blocks/control/newClone.html) | reporter | control | true |
| [`delete this clone`](/blocks/control/removeClone.html) | [![block 'delete this clone'](/blocks/images/block_removeClone.png)](/blocks/control/removeClone.html) | command | control | true |
| [`pause all $pause`](/blocks/control/doPauseAll.html) | [![block 'pause all $pause'](/blocks/images/block_doPauseAll.png)](/blocks/control/doPauseAll.html) | command | control | true |
| [`switch to scene _ _`](/blocks/control/doSwitchToScene.html) | [![block 'switch to scene _ _'](/blocks/images/block_doSwitchToScene.png)](/blocks/control/doSwitchToScene.html) | command | control | true |
| [`define _ _ _`](/blocks/control/doDefineBlock.html) | no help screen | command | control | true |
| [`delete block _`](/blocks/control/doDeleteBlock.html) | [![block 'delete block _'](/blocks/images/block_doDeleteBlock.png)](/blocks/control/doDeleteBlock.html) | command | control | true |
| [`set _ of block _ to _`](/blocks/control/doSetBlockAttribute.html) | no help screen | command | control | true |
| [`_ of block _`](/blocks/control/reportBlockAttribute.html) | no help screen | reporter | control | true |
| [`this _`](/blocks/control/reportEnvironment.html) | no help screen | reporter | control | true |
| [`set slot _ to _`](/blocks/control/doSetSlot.html) | no help screen | command | control | true |
| [`touching _ ?`](/blocks/sensing/reportTouchingObject.html) | [![block 'touching _ ?'](/blocks/images/block_reportTouchingObject.png)](/blocks/sensing/reportTouchingObject.html) | predicate | sensing | true |
| [`touching _ ?`](/blocks/sensing/reportTouchingColor.html) | [![block 'touching _ ?'](/blocks/images/block_reportTouchingColor.png)](/blocks/sensing/reportTouchingColor.html) | predicate | sensing | true |
| [`color _ is touching _ ?`](/blocks/sensing/reportColorIsTouchingColor.html) | [![block 'color _ is touching _ ?'](/blocks/images/block_reportColorIsTouchingColor.png)](/blocks/sensing/reportColorIsTouchingColor.html) | predicate | sensing | true |
| [`ask _ and wait`](/blocks/sensing/doAsk.html) | [![block 'ask _ and wait'](/blocks/images/block_doAsk.png)](/blocks/sensing/doAsk.html) | command | sensing | true |
| [`answer`](/blocks/sensing/getLastAnswer.html) | [![block 'answer'](/blocks/images/block_getLastAnswer.png)](/blocks/sensing/getLastAnswer.html) | reporter | sensing | true |
| [`mouse position`](/blocks/sensing/reportMousePosition.html) | no help screen | reporter | sensing | true |
| [`mouse x`](/blocks/sensing/reportMouseX.html) | [![block 'mouse x'](/blocks/images/block_reportMouseX.png)](/blocks/sensing/reportMouseX.html) | reporter | sensing | true |
| [`mouse y`](/blocks/sensing/reportMouseY.html) | [![block 'mouse y'](/blocks/images/block_reportMouseY.png)](/blocks/sensing/reportMouseY.html) | reporter | sensing | true |
| [`mouse down?`](/blocks/sensing/reportMouseDown.html) | [![block 'mouse down?'](/blocks/images/block_reportMouseDown.png)](/blocks/sensing/reportMouseDown.html) | predicate | sensing | true |
| [`key _ pressed?`](/blocks/sensing/reportKeyPressed.html) | [![block 'key _ pressed?'](/blocks/images/block_reportKeyPressed.png)](/blocks/sensing/reportKeyPressed.html) | predicate | sensing | true |
| [`_ to _`](/blocks/sensing/reportRelationTo.html) | [![block '_ to _'](/blocks/images/block_reportRelationTo.png)](/blocks/sensing/reportRelationTo.html) | reporter | sensing | true |
| [`_ at _`](/blocks/sensing/reportAspect.html) | [![block '_ at _'](/blocks/images/block_reportAspect.png)](/blocks/sensing/reportAspect.html) | reporter | sensing | true |
| [`reset timer`](/blocks/sensing/doResetTimer.html) | [![block 'reset timer'](/blocks/images/block_doResetTimer.png)](/blocks/sensing/doResetTimer.html) | command | sensing | true |
| [`timer`](/blocks/sensing/getTimer.html) | [![block 'timer'](/blocks/images/block_getTimer.png)](/blocks/sensing/getTimer.html) | reporter | sensing | true |
| [`current _`](/blocks/sensing/reportDate.html) | [![block 'current _'](/blocks/images/block_reportDate.png)](/blocks/sensing/reportDate.html) | reporter | sensing | true |
| [`_ of _`](/blocks/sensing/reportAttributeOf.html) | [![block '_ of _'](/blocks/images/block_reportAttributeOf.png)](/blocks/sensing/reportAttributeOf.html) | reporter | sensing | true |
| [`my _`](/blocks/sensing/reportGet.html) | [![block 'my _'](/blocks/images/block_reportGet.png)](/blocks/sensing/reportGet.html) | reporter | sensing | true |
| [`object _`](/blocks/sensing/reportObject.html) | [![block 'object _'](/blocks/images/block_reportObject.png)](/blocks/sensing/reportObject.html) | reporter | sensing | true |
| [`url _`](/blocks/sensing/reportURL.html) | [![block 'url _'](/blocks/images/block_reportURL.png)](/blocks/sensing/reportURL.html) | reporter | sensing | true |
| [`microphone _`](/blocks/sensing/reportAudio.html) | [![block 'microphone _'](/blocks/images/block_reportAudio.png)](/blocks/sensing/reportAudio.html) | reporter | sensing | true |
| [`video _ on _`](/blocks/sensing/reportVideo.html) | [![block 'video _ on _'](/blocks/images/block_reportVideo.png)](/blocks/sensing/reportVideo.html) | reporter | sensing | true |
| [`set video transparency to _`](/blocks/sensing/doSetVideoTransparency.html) | [![block 'set video transparency to _'](/blocks/images/block_doSetVideoTransparency.png)](/blocks/sensing/doSetVideoTransparency.html) | command | sensing | true |
| [`is _ on?`](/blocks/sensing/reportGlobalFlag.html) | [![block 'is _ on?'](/blocks/images/block_reportGlobalFlag.png)](/blocks/sensing/reportGlobalFlag.html) | predicate | sensing | true |
| [`set _ to _`](/blocks/sensing/doSetGlobalFlag.html) | [![block 'set _ to _'](/blocks/images/block_doSetGlobalFlag.png)](/blocks/sensing/doSetGlobalFlag.html) | command | sensing | true |
| [`_`](/blocks/operators/reportVariadicSum.html) | [![block '_'](/blocks/images/block_reportVariadicSum.png)](/blocks/operators/reportVariadicSum.html) | reporter | operators | true |
| [`_ − _`](/blocks/operators/reportDifference.html) | [![block '_ − _'](/blocks/images/block_reportDifference.png)](/blocks/operators/reportDifference.html) | reporter | operators | true |
| [`_`](/blocks/operators/reportVariadicProduct.html) | [![block '_'](/blocks/images/block_reportVariadicProduct.png)](/blocks/operators/reportVariadicProduct.html) | reporter | operators | true |
| [`_ / _`](/blocks/operators/reportQuotient.html) | [![block '_ / _'](/blocks/images/block_reportQuotient.png)](/blocks/operators/reportQuotient.html) | reporter | operators | true |
| [`_ ^ _`](/blocks/operators/reportPower.html) | [![block '_ ^ _'](/blocks/images/block_reportPower.png)](/blocks/operators/reportPower.html) | reporter | operators | true |
| [`_ mod _`](/blocks/operators/reportModulus.html) | [![block '_ mod _'](/blocks/images/block_reportModulus.png)](/blocks/operators/reportModulus.html) | reporter | operators | true |
| [`_`](/blocks/operators/reportVariadicMin.html) | no help screen | reporter | operators | true |
| [`_`](/blocks/operators/reportVariadicMax.html) | no help screen | reporter | operators | true |
| [`round _`](/blocks/operators/reportRound.html) | [![block 'round _'](/blocks/images/block_reportRound.png)](/blocks/operators/reportRound.html) | reporter | operators | true |
| [`_ of _`](/blocks/operators/reportMonadic.html) | [![block '_ of _'](/blocks/images/block_reportMonadic.png)](/blocks/operators/reportMonadic.html) | reporter | operators | true |
| [`atan2 _ ÷ _`](/blocks/operators/reportAtan2.html) | no help screen | reporter | operators | true |
| [`pick random _ to _`](/blocks/operators/reportRandom.html) | [![block 'pick random _ to _'](/blocks/images/block_reportRandom.png)](/blocks/operators/reportRandom.html) | reporter | operators | true |
| [`_`](/blocks/operators/reportVariadicLessThan.html) | no help screen | predicate | operators | true |
| [`_`](/blocks/operators/reportVariadicEquals.html) | no help screen | predicate | operators | true |
| [`_`](/blocks/operators/reportVariadicGreaterThan.html) | no help screen | predicate | operators | true |
| [`_`](/blocks/operators/reportVariadicAnd.html) | [![block '_'](/blocks/images/block_reportVariadicAnd.png)](/blocks/operators/reportVariadicAnd.html) | predicate | operators | true |
| [`_`](/blocks/operators/reportVariadicOr.html) | [![block '_'](/blocks/images/block_reportVariadicOr.png)](/blocks/operators/reportVariadicOr.html) | predicate | operators | true |
| [`not _`](/blocks/operators/reportNot.html) | [![block 'not _'](/blocks/images/block_reportNot.png)](/blocks/operators/reportNot.html) | predicate | operators | true |
| [`_`](/blocks/operators/reportBoolean.html) | [![block '_'](/blocks/images/block_reportBoolean.png)](/blocks/operators/reportBoolean.html) | predicate | operators | true |
| [`join _`](/blocks/operators/reportJoinWords.html) | [![block 'join _'](/blocks/images/block_reportJoinWords.png)](/blocks/operators/reportJoinWords.html) | reporter | operators | true |
| [`split _ by _`](/blocks/operators/reportTextSplit.html) | [![block 'split _ by _'](/blocks/images/block_reportTextSplit.png)](/blocks/operators/reportTextSplit.html) | reporter | operators | true |
| [`letter _ of _`](/blocks/operators/reportLetter.html) | [![block 'letter _ of _'](/blocks/images/block_reportLetter.png)](/blocks/operators/reportLetter.html) | reporter | operators | true |
| [`_ of text _`](/blocks/operators/reportTextAttribute.html) | no help screen | reporter | operators | true |
| [`unicode of _`](/blocks/operators/reportUnicode.html) | [![block 'unicode of _'](/blocks/images/block_reportUnicode.png)](/blocks/operators/reportUnicode.html) | reporter | operators | true |
| [`unicode _ as letter`](/blocks/operators/reportUnicodeAsLetter.html) | [![block 'unicode _ as letter'](/blocks/images/block_reportUnicodeAsLetter.png)](/blocks/operators/reportUnicodeAsLetter.html) | reporter | operators | true |
| [`is _ a _ ?`](/blocks/operators/reportIsA.html) | [![block 'is _ a _ ?'](/blocks/images/block_reportIsA.png)](/blocks/operators/reportIsA.html) | predicate | operators | true |
| [`is _ ?`](/blocks/operators/reportVariadicIsIdentical.html) | [![block 'is _ ?'](/blocks/images/block_reportVariadicIsIdentical.png)](/blocks/operators/reportVariadicIsIdentical.html) | predicate | operators | true |
| [`JavaScript function ( _ ) { _ }`](/blocks/operators/reportJSFunction.html) | [![block 'JavaScript function ( _ ) { _ }'](/blocks/images/block_reportJSFunction.png)](/blocks/operators/reportJSFunction.html) | reporter | operators | true |
| [`blocks json`](/blocks/variables/reportGetVar.html) | [![block 'blocks json'](/blocks/images/block_reportGetVar.png)](/blocks/variables/reportGetVar.html) | reporter | variables | true |
| [`blocks list`](/blocks/variables/reportGetVar.html) | [![block 'blocks list'](/blocks/images/block_reportGetVar.png)](/blocks/variables/reportGetVar.html) | reporter | variables | true |
| [`blocks table md`](/blocks/variables/reportGetVar.html) | [![block 'blocks table md'](/blocks/images/block_reportGetVar.png)](/blocks/variables/reportGetVar.html) | reporter | variables | true |
| [`HEADER`](/blocks/variables/reportGetVar.html) | [![block 'HEADER'](/blocks/images/block_reportGetVar.png)](/blocks/variables/reportGetVar.html) | reporter | variables | true |
| [`missing screens`](/blocks/variables/reportGetVar.html) | [![block 'missing screens'](/blocks/images/block_reportGetVar.png)](/blocks/variables/reportGetVar.html) | reporter | variables | true |
| [`test-block`](/blocks/variables/reportGetVar.html) | [![block 'test-block'](/blocks/images/block_reportGetVar.png)](/blocks/variables/reportGetVar.html) | reporter | variables | true |
| [`set _ to _`](/blocks/variables/doSetVar.html) | [![block 'set _ to _'](/blocks/images/block_doSetVar.png)](/blocks/variables/doSetVar.html) | command | variables | true |
| [`change _ by _`](/blocks/variables/doChangeVar.html) | [![block 'change _ by _'](/blocks/images/block_doChangeVar.png)](/blocks/variables/doChangeVar.html) | command | variables | true |
| [`show variable _`](/blocks/variables/doShowVar.html) | [![block 'show variable _'](/blocks/images/block_doShowVar.png)](/blocks/variables/doShowVar.html) | command | variables | true |
| [`hide variable _`](/blocks/variables/doHideVar.html) | [![block 'hide variable _'](/blocks/images/block_doHideVar.png)](/blocks/variables/doHideVar.html) | command | variables | true |
| [`inherit _`](/blocks/variables/doDeleteAttr.html) | [![block 'inherit _'](/blocks/images/block_doDeleteAttr.png)](/blocks/variables/doDeleteAttr.html) | command | variables | true |
| [`list _`](/blocks/lists/reportNewList.html) | [![block 'list _'](/blocks/images/block_reportNewList.png)](/blocks/lists/reportNewList.html) | reporter | lists | true |
| [`numbers from _ to _`](/blocks/lists/reportNumbers.html) | [![block 'numbers from _ to _'](/blocks/images/block_reportNumbers.png)](/blocks/lists/reportNumbers.html) | reporter | lists | true |
| [`_ in front of _`](/blocks/lists/reportCONS.html) | [![block '_ in front of _'](/blocks/images/block_reportCONS.png)](/blocks/lists/reportCONS.html) | reporter | lists | true |
| [`item _ of _`](/blocks/lists/reportListItem.html) | [![block 'item _ of _'](/blocks/images/block_reportListItem.png)](/blocks/lists/reportListItem.html) | reporter | lists | true |
| [`all but first of _`](/blocks/lists/reportCDR.html) | [![block 'all but first of _'](/blocks/images/block_reportCDR.png)](/blocks/lists/reportCDR.html) | reporter | lists | true |
| [`_ of _`](/blocks/lists/reportListAttribute.html) | [![block '_ of _'](/blocks/images/block_reportListAttribute.png)](/blocks/lists/reportListAttribute.html) | reporter | lists | true |
| [`index of _ in _`](/blocks/lists/reportListIndex.html) | [![block 'index of _ in _'](/blocks/images/block_reportListIndex.png)](/blocks/lists/reportListIndex.html) | reporter | lists | true |
| [`_ contains _`](/blocks/lists/reportListContainsItem.html) | [![block '_ contains _'](/blocks/images/block_reportListContainsItem.png)](/blocks/lists/reportListContainsItem.html) | predicate | lists | true |
| [`is _ empty?`](/blocks/lists/reportListIsEmpty.html) | [![block 'is _ empty?'](/blocks/images/block_reportListIsEmpty.png)](/blocks/lists/reportListIsEmpty.html) | predicate | lists | true |
| [`map _ over _`](/blocks/lists/reportMap.html) | [![block 'map _ over _'](/blocks/images/block_reportMap.png)](/blocks/lists/reportMap.html) | reporter | lists | true |
| [`keep items _ from _`](/blocks/lists/reportKeep.html) | [![block 'keep items _ from _'](/blocks/images/block_reportKeep.png)](/blocks/lists/reportKeep.html) | reporter | lists | true |
| [`find first item _ in _`](/blocks/lists/reportFindFirst.html) | [![block 'find first item _ in _'](/blocks/images/block_reportFindFirst.png)](/blocks/lists/reportFindFirst.html) | reporter | lists | true |
| [`combine _ using _`](/blocks/lists/reportCombine.html) | [![block 'combine _ using _'](/blocks/images/block_reportCombine.png)](/blocks/lists/reportCombine.html) | reporter | lists | true |
| [`for each _ in _ _`](/blocks/lists/doForEach.html) | [![block 'for each _ in _ _'](/blocks/images/block_doForEach.png)](/blocks/lists/doForEach.html) | command | lists | true |
| [`add _ to _`](/blocks/lists/doAddToList.html) | [![block 'add _ to _'](/blocks/images/block_doAddToList.png)](/blocks/lists/doAddToList.html) | command | lists | true |
| [`delete _ of _`](/blocks/lists/doDeleteFromList.html) | [![block 'delete _ of _'](/blocks/images/block_doDeleteFromList.png)](/blocks/lists/doDeleteFromList.html) | command | lists | true |
| [`insert _ at _ of _`](/blocks/lists/doInsertInList.html) | [![block 'insert _ at _ of _'](/blocks/images/block_doInsertInList.png)](/blocks/lists/doInsertInList.html) | command | lists | true |
| [`replace item _ of _ with _`](/blocks/lists/doReplaceInList.html) | [![block 'replace item _ of _ with _'](/blocks/images/block_doReplaceInList.png)](/blocks/lists/doReplaceInList.html) | command | lists | true |
| [`append _`](/blocks/lists/reportConcatenatedLists.html) | [![block 'append _'](/blocks/images/block_reportConcatenatedLists.png)](/blocks/lists/reportConcatenatedLists.html) | reporter | lists | true |
| [`reshape _ to _`](/blocks/lists/reportReshape.html) | [![block 'reshape _ to _'](/blocks/images/block_reportReshape.png)](/blocks/lists/reportReshape.html) | reporter | lists | true |
| [`combinations _`](/blocks/lists/reportCrossproduct.html) | no help screen | reporter | lists | true |
