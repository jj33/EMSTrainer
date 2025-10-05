#!/usr/bin/env bash
ROOT=${1:-.}
shift || true
python3 tools/lint_emstrainer_prompts.py "$ROOT" "$@"
