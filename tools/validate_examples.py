
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Offline schema validation for EMSTrainer using jsonschema + referencing (no network).
"""
import json
import sys
from pathlib import Path
from jsonschema import validators
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / 'schemas'

# Load schemas into memory
S_RUBRIC     = json.loads((SCHEMAS / 'rubric.schema.json').read_text(encoding='utf-8'))
S_SCENARIO   = json.loads((SCHEMAS / 'scenario.schema.json').read_text(encoding='utf-8'))
S_SUBMISSION = json.loads((SCHEMAS / 'submission.schema.json').read_text(encoding='utf-8'))

# Build a local registry mapping absolute $id -> Resource (prevents any network fetches)
REGISTRY = Registry().with_resources({
    'https://emstrainer/schemas/rubric.schema.json':     Resource.from_contents(S_RUBRIC),
    'https://emstrainer/schemas/scenario.schema.json':   Resource.from_contents(S_SCENARIO),
    'https://emstrainer/schemas/submission.schema.json': Resource.from_contents(S_SUBMISSION),
})


def validate_file(path: Path, schema: dict):
    data = json.loads(path.read_text(encoding='utf-8'))
    Validator = validators.validator_for(schema)
    Validator.check_schema(schema)
    v = Validator(schema, registry=REGISTRY)
    return list(v.iter_errors(data))


def main() -> int:
    errors = []

    for p in ROOT.rglob('examples/**/scenario.json'):
        errs = validate_file(p, S_SCENARIO)
        if errs:
            errors.extend([f"{p}: {m}" for m in errs])
        else:
            print(f"[OK] {p}")

    for p in ROOT.rglob('examples/**/submission.json'):
        errs = validate_file(p, S_SUBMISSION)
        if errs:
            errors.extend([f"{p}: {m}" for m in errs])
        else:
            print(f"[OK] {p}")

    for p in ROOT.rglob('prompts/Instructor/Rubrics/*.json'):
        errs = validate_file(p, S_RUBRIC)
        if errs:
            errors.extend([f"{p}: {m}" for m in errs])
        else:
            print(f"[OK] {p}")

    if errors:
print()
Validation errors:
' + '
'.join(errors))
        return 1

    print('
All examples and rubrics conform to schemas.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
