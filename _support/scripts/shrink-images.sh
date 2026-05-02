#!/usr/bin/env bash
# Halve the dimensions of every PNG/JPG under one or more directories.
#
# Used in CI between the HTML build and the PDF build: the HTML site
# ships at original resolution, and the PDF picks up the half-size
# copies so the output PDF lands at a reasonable file size without
# any post-build PDF rewrite.
#
# Usage:
#   shrink-images.sh <dir> [<dir>...]
#
# Honours $SHRINK_IMAGES_PERCENT (default 50) so the scale factor can
# be tuned without editing the script.
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <dir> [<dir>...]" >&2
  exit 2
fi

PCT="${SHRINK_IMAGES_PERCENT:-50}"

# ImageMagick 7 ships `magick`; older distros expose `mogrify` directly.
if command -v magick >/dev/null 2>&1; then
  MOGRIFY=(magick mogrify)
elif command -v mogrify >/dev/null 2>&1; then
  MOGRIFY=(mogrify)
else
  echo "error: ImageMagick (magick or mogrify) not found in PATH" >&2
  exit 1
fi

for dir in "$@"; do
  if [[ ! -d "$dir" ]]; then
    echo "warning: '$dir' is not a directory, skipping" >&2
    continue
  fi
  echo "Shrinking PNG/JPG under $dir to ${PCT}% ..."
  # `-resize 50%` always shrinks; we don't need the `>` modifier here.
  # xargs -P parallelises across cores; each mogrify call rewrites the
  # file in place (no -path so the original is replaced).
  find "$dir" -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' \) -print0 \
    | xargs -0 -r -n 32 -P 4 "${MOGRIFY[@]}" -resize "${PCT}%"
done
