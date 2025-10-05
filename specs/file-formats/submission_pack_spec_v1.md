
# Submission Pack Spec (v1) — Plaintext Structure

- `spec_version`: "1.0"
- `type`: "submission"
- Required: `scenario_id`, `student_id`, `submitted_at_utc`, `events[]`
- Event types:
  - `intervention`: id, at_s, (dose?), (success?)
  - `assessment`:   id, at_s, answer
  - `note`:         at_s, text
- **Schema**: `/schemas/submission.schema.json` (Draft 2020-12)

## Schema ID
- `$id`: `https://emstrainer/schemas/submission.schema.json`

Validation uses a preloaded schema store (see `/schemas/README.md`).
