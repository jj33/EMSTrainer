# Submission Pack Spec (v1) — Plaintext Structure

- `spec_version`: "1.0"
- `type`: "submission"
- Required: `scenario_id`, `student_id`, `submitted_at_utc`, `events[]`
- Event types:
  - `intervention`: id, at_s, (dose?), (success?)
  - `assessment`:   id, at_s, answer
  - `note`:         at_s, text
- See `/schemas/submission.schema.json` for validation rules.

