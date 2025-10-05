
# Scenario Pack Spec (v1) — Plaintext Structure

- `spec_version`: "1.0"
- `type`: "scenario"
- IDs: `scenario_id` (`SCN-*`), optional `run_id` (`RUN-*`)
- Security: Encryption/wrapping defined in `/specs/security/crypto_spec_v1.md`
- Required sections: vitals_trend, assessment_points, expected_interventions, rubric, policy
- **Schema**: `/schemas/scenario.schema.json` (Draft 2020-12)

## Schema ID & References
- `$id`: `https://emstrainer/schemas/scenario.schema.json`
- The `rubric` property is validated by an absolute `$ref` to
  `https://emstrainer/schemas/rubric.schema.json`.
- Tooling **must not** fetch these over the network. CI and local scripts preload a
  store mapping `$id` → local file content to keep validation offline/hermetic.

See also: `/schemas/README.md` and `/tools/validate_examples.py`.
