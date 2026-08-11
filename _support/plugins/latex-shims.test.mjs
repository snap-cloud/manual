// Unit tests for the index-entry rewriting in latex-shims.mjs.
//
// Run with `npm test` (Node's built-in test runner; no extra deps).
//
// These cover the makeindex quoting rules, which are easy to get wrong
// because `!` is both our sub-entry separator (added by myst-to-tex,
// after this transform runs) and a literal character in Snap!'s own
// name — the term most likely to be looked up in this manual.

import test from 'node:test';
import assert from 'node:assert/strict';

import { quoteForMakeindex, rewriteIndexEntry } from './latex-shims.mjs';

test('quoteForMakeindex escapes every makeindex control character', () => {
  assert.equal(quoteForMakeindex('Snap! program'), 'Snap"! program');
  assert.equal(quoteForMakeindex('a@b'), 'a"@b');
  assert.equal(quoteForMakeindex('a|b'), 'a"|b');
  assert.equal(quoteForMakeindex('a"b'), 'a""b');
});

test('plain entries with a literal ! are quoted, not split', () => {
  // Without quoting these reach \index{...} as sub-entry separators:
  // makeindex reads \index{Snap! program} as "Snap" -> "program".
  assert.equal(rewriteIndexEntry('Snap! program'), 'Snap"! program');
  assert.equal(rewriteIndexEntry('SciSnap!'), 'SciSnap"!');
  assert.equal(rewriteIndexEntry('SciSnap! library'), 'SciSnap"! library');
  assert.equal(rewriteIndexEntry('starting Snap!'), 'starting Snap"!');
  assert.equal(rewriteIndexEntry('source files for Snap!'), 'source files for Snap"!');
});

test('a bare ! sub-entry survives as a literal', () => {
  // The `!` block in chapter 1: the sub-entry is the character itself.
  assert.equal(rewriteIndexEntry('!'), '"!');
});

test('plain entries without control characters are left alone', () => {
  assert.equal(rewriteIndexEntry('palette'), 'palette');
  assert.equal(rewriteIndexEntry('hat block'), 'hat block');
  assert.equal(rewriteIndexEntry('Ball, Michael'), 'Ball, Michael');
});

test('trailing backslashes are still stripped', () => {
  assert.equal(rewriteIndexEntry('hat block\\'), 'hat block');
  assert.equal(rewriteIndexEntry('hat block\\\\  '), 'hat block');
});

test('code spans still become \\texttt with a plain sort key', () => {
  assert.equal(rewriteIndexEntry('`set`'), 'set@\\texttt{set}');
  assert.equal(
    rewriteIndexEntry('`Snap! website` option'),
    'Snap"! website option@\\texttt{Snap"! website} option',
  );
});

test('symbols keep their ASCII sort key and TeX display', () => {
  assert.equal(rewriteIndexEntry('⚡'), 'lightning bolt@\\snaplightning{}');
  assert.equal(
    rewriteIndexEntry('sentence ➔ list'),
    'sentence arrow list@sentence \\textrightarrow{} list',
  );
});

test('non-string entries pass through untouched', () => {
  assert.equal(rewriteIndexEntry(undefined), undefined);
  assert.equal(rewriteIndexEntry(null), null);
});
