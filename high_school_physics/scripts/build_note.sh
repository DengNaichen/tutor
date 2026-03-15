#!/usr/bin/env bash

set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: scripts/build_note.sh path/to/file.tex" >&2
  exit 1
fi

src="$1"

if [ ! -f "$src" ]; then
  echo "File not found: $src" >&2
  exit 1
fi

src_dir="$(cd "$(dirname "$src")" && pwd)"
src_name="$(basename "$src")"
src_base="${src_name%.tex}"
src_abs="$src_dir/$src_name"

case "$src_abs" in
  */source/*)
    unit_root="${src_abs%%/source/*}"
    rel_path="${src_abs#"$unit_root/source/"}"
    ;;
  *)
    echo "Expected a .tex file inside a unit's source/ directory: $src" >&2
    exit 1
    ;;
esac

out_path="$unit_root/pdf/${rel_path%.tex}.pdf"
out_dir="$(dirname "$out_path")"

mkdir -p "$out_dir"

tmp_dir="$(mktemp -d "${TMPDIR:-/tmp}/latex-build.XXXXXX")"
cleanup() {
  rm -rf "$tmp_dir"
}
trap cleanup EXIT

(
  cd "$src_dir"
  latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir="$tmp_dir" "$src_name"
)

cp "$tmp_dir/$src_base.pdf" "$out_path"
echo "Built $out_path"
