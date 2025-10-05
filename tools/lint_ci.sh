#!/usr/bin/env bash
ROOT="."
APPLY=false
for arg in "$@"; do
  case $arg in
    --root) shift; ROOT=$1 ;;
    --apply) APPLY=true ;;
  esac
done
if $APPLY; then
  python3 tools/lint_emstrainer_prompts.py "$ROOT" --backup
else
  python3 tools/lint_emstrainer_prompts.py "$ROOT" --dry-run --exit-nonzero-on-changes
fi
