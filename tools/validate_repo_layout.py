
#!/usr/bin/env python3
"""
Validate local repo layout against expected file paths for EMSTrainer v1.5.6.1
Usage: python3 tools/validate_repo_layout.py
"""
import os, json, sys

BASE = os.path.abspath(os.path.dirname(__file__) + '/..')
EXPECTED_PATH = os.path.join(BASE, 'tools', 'expected_layout_v1.5.6.1.json')

with open(EXPECTED_PATH,'r') as f:
    expected = json.load(f)

missing, unexpected = [], []

# Check expected
for folder, files in expected.items():
    if folder == 'root':
        for fn in files:
            p = os.path.join(BASE, fn)
            if not os.path.exists(p):
                missing.append(fn)
    else:
        for fn in files:
            p = os.path.join(BASE, folder, fn)
            if not os.path.exists(p):
                missing.append(os.path.join(folder, fn))

# Scan for unexpected top-level critical folders/files (optional strictness)
critical_dirs = set(['prompts','docs','assets','schemas'])
for d in critical_dirs:
    dp = os.path.join(BASE, d)
    if os.path.isdir(dp):
        for root, _, files in os.walk(dp):
            relroot = os.path.relpath(root, BASE)
            for fn in files:
                rel = os.path.join(relroot, fn)
                # Allow extra docs by default; flag only if under assets/schemas/prompts
                if relroot.startswith('assets') or relroot.startswith('schemas') or relroot.startswith('prompts'):
                    # if not in expected, mark unexpected
                    if relroot == 'prompts' and fn.endswith('.txt') and fn not in expected.get('prompts', []):
                        unexpected.append(rel)
                    elif relroot == 'assets' and fn not in expected.get('assets', []):
                        # allow additional instructor configs ending with .json
                        if not fn.endswith('.json') and fn != 'README.md':
                            unexpected.append(rel)
                    elif relroot == 'schemas' and fn not in expected.get('schemas', []):
                        unexpected.append(rel)

print("
=== EMSTrainer Layout Validation (v1.5.6.1) ===")
print(f"Base: {BASE}")
if missing:
    print("
Missing:")
    for m in missing:
        print(" -", m)
else:
    print("
Missing: None")

if unexpected:
    print("
Unexpected (informational):")
    for u in unexpected:
        print(" -", u)
else:
    print("
Unexpected: None (or only allowed extras)")

# Exit code non-zero if missing any required paths
sys.exit(1 if missing else 0)
