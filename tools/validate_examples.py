#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate EMSTrainer examples and rubrics against local schemas (offline).

Usage:
  python3 tools/validate_examples.py

Exit codes:
  0 = all good
  1 = validation errors occurred
"""
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator
from jsonschema.validators import RefResolver


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / 'schemas'


def load_json(p: Path):
    return json.loads(p.read_text(encoding='utf-8'))


# Load schemas into memory
S_RUBRIC     = load_json(SCHEMAS / 'rubric.schema.json')
S_SCENARIO   = load_json(SCHEMAS / 'scenario.schema.json')
S_SUBMISSION = load_json(SCHEMAS / 'submission.schema.json')

# Preload store for absolute $id/$ref (no network fetches)
STORE = {
    'https://emstrainer/schemas/rubric.schema.json':     S_RUBRIC,
    'https://emstrainer/schemas/scenario.schema.json':   S_SCENARIO,
    'https://emstrainer/schemas/submission.schema.json': S_SUBMISSION,
}


def validate_file(path: Path, schema: dict):
    data = load_json(path)
    resolver = RefResolver.from_schema(schema, store=STORE)
    v = Draft202012Validator(schema=schema, resolver=resolver)
    return list(v.iter_errors(data))


def main() -> int:
    errors = []

    # Scenarios
    for p in ROOT.rglob('examples/**/scenario.json'):
        errs = validate_file(p, S_SCENARIO)
        if errs:
            errors.extend(['{}: {}'.format(p, e.message) for e in errs])
        else:
            print('[OK] {}'.format(p))

    # Submissions
    for p in ROOT.rglob('examples/**/submission.json'):
        errs = validate_file(p, S_SUBMISSION)
        if errs:
            errors.extend(['{}: {}'.format(p, e.message) for e in errs])
        else:
            print('[OK] {}'.format(p))

    # Rubrics (in prompts)
    for p in ROOT.rglob('prompts/Instructor/Rubrics/*.json'):
        errs = validate_file(p, S_RUBRIC)
        if errs:
            errors.extend(['{}: {}'.format(p, e.message) for e in errs])
        else:
            print('[OK] {}'.format(p))

    if errors:
        print('\nValidation errors:')
        print('\n'.join(errors))
        return 1

    print('\nAll examples and rubrics conform to schemas.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
