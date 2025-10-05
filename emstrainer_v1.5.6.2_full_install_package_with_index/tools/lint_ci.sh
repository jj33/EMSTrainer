#!/usr/bin/env bash
set -euo pipefail
ROOT="."
APPLY=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --root) ROOT="${2:-.}"; shift 2 ;;
    --apply) APPLY=1; shift ;;
    *) echo "Unknown arg: $1" >&2; exit 1 ;;
  esac
done
TARGET="$ROOT/prompts"
if [[ ! -d "$TARGET" ]]; then echo "prompts/ directory not found under $ROOT" >&2; exit 1; fi
if [[ $APPLY -eq 1 ]]; then
  python3 tools/lint_emstrainer_prompts.py "$TARGET" --backup
else
  python3 tools/lint_emstrainer_prompts.py "$TARGET" --dry-run --exit-nonzero-on-changes
fi
