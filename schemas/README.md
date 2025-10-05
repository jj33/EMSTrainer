
# EMSTrainer Schemas

This folder contains JSON Schemas (Draft 2020-12) for EMSTrainer packs:

- `scenario.schema.json` — plaintext scenario packs (pre-encryption)
- `submission.schema.json` — plaintext student submissions (pre-encryption)
- `rubric.schema.json` — grading rubric structure

## IDs & References
Each schema includes a stable `$id`:

- `https://emstrainer/schemas/scenario.schema.json`
- `https://emstrainer/schemas/submission.schema.json`
- `https://emstrainer/schemas/rubric.schema.json`

`scenario.schema.json` references the rubric via an **absolute** `$ref`:

```json
"rubric": { "$ref": "https://emstrainer/schemas/rubric.schema.json" }
```

These IDs are **not fetched over the network** during validation. Tooling should
preload a local **store** that maps each `$id` to the in-repo schema JSON. See
`tools/validate_examples.py` and the CI workflow for examples.

## Local Validation
```bash
python3 tools/validate_examples.py
```

The script exits non-zero if any example or rubric fails validation.

## Updating Schemas
- Keep `$id` values stable to avoid breaking references.
- Prefer adding new optional fields for backward compatibility.
- When making breaking changes, bump `spec_version` in example packs and update docs under `/specs`.
