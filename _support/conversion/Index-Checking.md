# Index Checking

`text-index.txt` represents a (manually) cleaned up C&P of the index from the most recent PDF.

* Each line is 1 index entry
* The `--` separates an entry from the origianl page it appeared on
* pages are separated by a `,`
* There is no formatting other than Unicode characters.
* A few entries like ⚡️ (lightning bolt) and the arrow right were manually cleaned up.
* Nested entries are separated by a `:` (e.g., `variable:global -- 14`)
  * These were manually cleaned up, to reflect the way they were (mostly) extracted from the original Word document.
* Normalized some spacing like "Snap !" to "Snap!".

From the _root of the repo_, you can run the following command to check the index:

```bash
ruby _support/conversion/index-check.rb
```
