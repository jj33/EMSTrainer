#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="${1:-.}"
if [[ "$ROOT_DIR" != "." ]]; then shift || true; fi
TARGET_DIR="$ROOT_DIR/prompts"
if [[ ! -d "$TARGET_DIR" ]]; then
  echo "prompts/ directory not found under $ROOT_DIR" >&2
  exit 1
fi
if [[ $# -eq 0 ]]; then set -- --dry-run; fi
python3 tools/lint_emstrainer_prompts.py "$TARGET_DIR" "$@"
