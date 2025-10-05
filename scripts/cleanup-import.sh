#!/usr/bin/env bash
#
# cleanup-import.sh
# Normalize filenames, archive old versions, and organize imported docs.
#
# Usage:
#   ./scripts/cleanup-import.sh <version> [--apply]
#
# Example:
#   ./scripts/cleanup-import.sh v1.5.2
#   ./scripts/cleanup-import.sh v1.5.2 --apply

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <version> [--apply]"
  exit 1
fi

VERSION="$1"
IMPORT_DIR="docs/imports/$VERSION"
ARCHIVE_DIR="docs/archive/$VERSION"
SOURCE_DIR="docs/source"
NEEDS_CONVERT_DIR="docs/needs-convert"
ASSETS_DIR="assets"

APPLY=false
if [[ "${2:-}" == "--apply" ]]; then
  APPLY=true
fi

run_cmd() {
  if $APPLY; then
    eval "$1"
  else
    echo "[DRY-RUN] $1"
  fi
}

echo "=== Cleanup Script for $VERSION ==="
echo "Import dir: $IMPORT_DIR"
echo "Apply mode: $APPLY"
echo

# 1) Normalize filenames (spaces → _, remove # and ?)
echo "--- Normalizing filenames ---"
shopt -s nullglob
for f in "$IMPORT_DIR"/*; do
  base=$(basename "$f")
  new=$(echo "$base" | sed 's/[[:space:]]/_/g; s/[#?]//g')
  if [[ "$base" != "$new" ]]; then
    run_cmd "mv \"$IMPORT_DIR/$base\" \"$IMPORT_DIR/$new\""
  fi
done

# 2) Archive old versions
echo "--- Archiving old versions ---"
mkdir -p "$ARCHIVE_DIR"
for d in "Old_versions" "Old versions"; do
  if [[ -d "$IMPORT_DIR/$d" ]]; then
    # Clean up hidden files like .DS_Store
    run_cmd "find \"$IMPORT_DIR/$d\" -name \".DS_Store\" -delete"
    # Move contents to archive
    run_cmd "mv \"$IMPORT_DIR/$d\"/* \"$ARCHIVE_DIR/\""
    # Remove the folder itself
    run_cmd "rm -rf \"$IMPORT_DIR/$d\""
  fi
done

# 3) Organize by type
echo "--- Organizing by type ---"
mkdir -p "$SOURCE_DIR" "$NEEDS_CONVERT_DIR" "$ASSETS_DIR"

# Pages → source
for f in "$IMPORT_DIR"/*.pages; do
  [[ -e "$f" ]] || continue
  run_cmd "mv \"$f\" \"$SOURCE_DIR/\""
done

# Docx → needs-convert
for f in "$IMPORT_DIR"/*.docx; do
  [[ -e "$f" ]] || continue
  run_cmd "mv \"$f\" \"$NEEDS_CONVERT_DIR/\""
  echo "[REMINDER] Convert $(basename "$f") to .pages and move into docs/source/"
done

# PDFs → assets
for f in "$IMPORT_DIR"/*.pdf; do
  [[ -e "$f" ]] || continue
  run_cmd "mv \"$f\" \"$ASSETS_DIR/\""
done

# 4) Large file check (>90MB)
echo "--- Large file check (>90MB) ---"
find . -type f -size +90M -print0 | xargs -0 ls -lh || true

echo
echo "=== Done. Rerun with --apply to make changes. ==="
