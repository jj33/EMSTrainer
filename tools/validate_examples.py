#!/usr/bin/env python3
"""Offline example validator for EMSTrainer

Validates JSON, CSV, and Markdown files using Python stdlib only.
Prints a summary and exits non-zero if any errors are found.

Usage:
    python3 tools/validate_examples.py [PATH ...]

If no PATHs are provided, it scans defaults: examples/, exports/, and current directory.
"""
import argparse
import csv
import json
import sys
from pathlib import Path

def eprint(*args):
    print(*args, file=sys.stderr)

def find_targets(paths):
    exts = {'.json', '.csv', '.md', '.markdown'}
    for p in paths:
        p = Path(p)
        if not p.exists():
            continue
        if p.is_file():
            if p.suffix.lower() in exts:
                yield p
        else:
            for f in p.rglob('*'):
                if f.is_file() and f.suffix.lower() in exts:
                    yield f

def validate_json(path):
    try:
        with path.open('r', encoding='utf-8') as f:
            json.load(f)
        return []
    except Exception as exc:
        return [f"JSON error in {path}: {exc}"]

def validate_csv(path):
    try:
        with path.open('r', encoding='utf-8', newline='') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            if not header:
                return [f"CSV error in {path}: empty file or missing header"]
            ncols = len(header)
            rownum = 1
            errors = []
            for row in reader:
                rownum += 1
                if len(row) != ncols:
                    errors.append(f"CSV error in {path}: row {rownum} has {len(row)} cols, expected {ncols}")
                if rownum > 5000 and not errors:
                    break
            return errors
    except Exception as exc:
        return [f"CSV error in {path}: {exc}"]

def validate_md(path):
    try:
        text = path.read_text(encoding='utf-8')
        if not text.strip():
            return [f"MD error in {path}: file is empty"]
        return []
    except Exception as exc:
        return [f"MD error in {path}: {exc}"]

VALIDATORS = {
    '.json': validate_json,
    '.csv': validate_csv,
    '.md': validate_md,
    '.markdown': validate_md,
}

def main(argv=None):
    parser = argparse.ArgumentParser(description='Offline validator for EMSTrainer example/export files')
    parser.add_argument('paths', nargs='*', help='Files or directories to validate')
    args = parser.parse_args(argv)

    scan_roots = args.paths if args.paths else []
    if not scan_roots:
        for default in ('examples', 'exports', '.'):
            if Path(default).exists():
                scan_roots.append(default)

    print('🔎 Scanning paths:', ', '.join(str(p) for p in scan_roots))

    files = list(find_targets(scan_roots))
    if not files:
        print('ℹ️  No target files (.json/.csv/.md) found. Nothing to validate.')
        return 0

    errors = []
    ok = 0
    for fpath in sorted(files):
        validator = VALIDATORS.get(fpath.suffix.lower())
        if not validator:
            continue
        verrs = validator(fpath)
        if verrs:
            errors.extend(verrs)
        else:
            ok += 1

    total = len(files)
    print()
    print(f"Checked: {total} file(s)")
    print(f"Valid:   {ok}")
    print(f"Errors:  {len(errors)}")

    if errors:
        print()
        print('Validation errors:')
        print('\n'.join(errors))
        return 1

    print('\n✅ All example/export files passed basic validation.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
