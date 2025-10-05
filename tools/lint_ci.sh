#!/usr/bin/env bash
set -euo pipefail

# One-shot CI linter for EMSTrainer
# - Dry-run by default and fails (exit 2) if changes are needed
# - Use --apply to auto-fix with backups and exit 0
# - Use --root <path> to set repo root (default: .)

ROOT="."
APPLY=0

# Parse args
while [[ $# -gt 0 ]]; do
  case "$1" in
    --root)
      ROOT="${2:-.}"
      shift 2
      ;;
    --apply)
      APPLY=1
      shift
      ;;
    *)
      echo "Unknown argument: $1" >&2
      echo "Usage: $0 [--root <path>] [--apply]" >&2
      exit 1
      ;;
  esac
done

TARGET="$ROOT/prompts"
if [[ ! -d "$TARGET" ]]; then
  echo "prompts/ directory not found under $ROOT" >&2
  exit 1
fi

if [[ $APPLY -eq 1 ]]; then
  echo "[CI Lint] Applying fixes with backup to: $TARGET"
  python3 "$(dirname "$0")/lint_emstrainer_prompts.py" "$TARGET" --backup
  echo "[CI Lint] Fixes applied."
  exit 0
else
  echo "[CI Lint] Dry-run (no changes) scanning: $TARGET"
  # Exit code 2 if changes needed
  python3 "$(dirname "$0")/lint_emstrainer_prompts.py" "$TARGET" --dry-run --exit-nonzero-on-changes
fi
