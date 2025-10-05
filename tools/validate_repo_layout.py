#!/usr/bin/env python3
"""
Validate local repo layout against expected file paths for EMSTrainer v1.5.6.1
Usage:
  python3 tools/validate_repo_layout.py
Exits with code 1 if any required paths are missing; 0 otherwise.
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
EXPECTED_PATH = BASE / 'tools' / 'expected_layout_v1.5.6.1.json'

try:
    with EXPECTED_PATH.open('r', encoding='utf-8') as f:
        expected = json.load(f)
except FileNotFoundError:
    print(f"ERROR: Expected layout file not found: {EXPECTED_PATH}")
    sys.exit(2)

missing = []
unexpected = []

# Check required files
for folder, files in expected.items():
    if folder == 'root':
        for fn in files:
            p = BASE / fn
            if not p.exists():
                missing.append(str(fn))
    else:
        for fn in files:
            p = BASE / folder / fn
            if not p.exists():
                missing.append(str(Path(folder) / fn))

# Scan for unexpected files (informational):
# restrict to prompts/assets/schemas; allow extra instructor JSON files in assets and any extra docs
critical_dirs = {'prompts', 'assets', 'schemas'}
for d in critical_dirs:
    dp = BASE / d
    if dp.is_dir():
        for p in dp.rglob('*'):
            if p.is_file():
                rel = p.relative_to(BASE)
                rel_root = rel.parts[0]
                if rel_root == 'prompts':
                    allowed = set(expected.get('prompts', []))
                    if p.suffix == '.txt' and rel.name not in allowed:
                        unexpected.append(str(rel))
                elif rel_root == 'assets':
                    allowed = set(expected.get('assets', []))
                    # allow extra .json (instructor overrides) and README.md
                    if rel.name not in allowed and not rel.name.endswith('.json') and rel.name != 'README.md':
                        unexpected.append(str(rel))
                elif rel_root == 'schemas':
                    allowed = set(expected.get('schemas', []))
                    if rel.name not in allowed:
                        unexpected.append(str(rel))

print("\n=== EMSTrainer Layout Validation (v1.5.6.1) ===")
print(f"Base: {BASE}")

if missing:
    print("\nMissing:")
    for m in missing:
        print(f" - {m}")
else:
    print("\nMissing: None")

if unexpected:
    print("\nUnexpected (informational):")
    for u in unexpected:
        print(f" - {u}")
else:
    print("\nUnexpected: None (or only allowed extras)")

# Exit non-zero if missing any required paths
sys.exit(1 if missing else 0)

