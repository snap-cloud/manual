---
page-layout: full
---

# All [Snap!]{.snap} Blocks {.unnumbered}

<!--
The table below is currently generated from
the following Snap! project:
https://snap.berkeley.edu/snap/snap.html#present:Username=cycomachead&ProjectName=markdown%20blocks%20table
Run the two scripts, then copy the output of the `blocks table md` variable

Block images should be exported at 2X Zoom on a retina display.
(4X Zoom on a non-retina display.)
-->

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

<style>
/* In the markdown table this class is applied to the link */
.block-image-2x img {
  height: 55%;
}
</style>

<!-- This file should contain noting but markdown. -->
{{< include _raw_blocks_table.qmd >}}
: All Snap! Blocks {.blocks-table .table-striped .table-bordered .table-hover .table-responsive-sm .dataTable #sec-all-blocks}

<!--
Consider loaing the DataTables script and stylesheets from a CDN.
* We need some way to maitain the original order of the blocks.
* Consider a filter
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const table = document.querySelector('.blocks-table');
    if (table) {
      $(table).DataTable();
    }
  });
</script>
-->
