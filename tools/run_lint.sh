#!/usr/bin/env bash
set -euo pipefail

# Usage examples:
#   bash tools/run_lint.sh . --dry-run
#   bash tools/run_lint.sh . --backup
#   bash tools/run_lint.sh                # defaults to ./prompts dry-run

ROOT_DIR="${1:-.}"
# If first arg is a flag, default ROOT_DIR to current directory
if [[ "$ROOT_DIR" == --* ]]; then
  ROOT_DIR="."
else
  shift || true
fi

TARGET_DIR="$ROOT_DIR/prompts"

if [[ ! -d "$TARGET_DIR" ]]; then
  echo "prompts/ directory not found under $ROOT_DIR" >&2
  exit 1
fi

# Default to --dry-run if no flags were provided
if [[ $# -eq 0 ]]; then
  set -- --dry-run
fi

python3 "$(dirname "$0")/lint_emstrainer_prompts.py" "$TARGET_DIR" "$@"
