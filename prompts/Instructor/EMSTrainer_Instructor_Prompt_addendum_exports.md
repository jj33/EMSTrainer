
# Addendum — /grade.export Templates & Usage (v1)  
**Date:** 2025-10-05

This addendum extends the Instructor prompt with export templates for Markdown and CSV.

## New/Clarified Commands

**`/grade.export format=md template=default|path:<file> include=verification|none`**  
Exports a student‑facing Markdown report using the default template (below) or a provided template path.  
- `include=verification` appends a verification block (template partial `verify_block`).

**`/grade.export format=csv template=default|path:<file>`**  
Exports a CSV event log for the instructor record using the default template or a provided template path.

### Default Template Locations (checked in this order)
- `templates/exports/grade_export.md.tmpl`  
- `templates/exports/grade_export.csv.tmpl`  
- `templates/exports/verify_block.md.tmpl` (partial used by Markdown when `include=verification`)

## Template Placeholders (Mustache‑style)
Common tokens available to both templates:
- `{timestamp_utc}`, `{tool_version}`, `{scenario_id}`, `{scenario_title}`, `{run_id}`, `{student_id}`, `{spec_version}`
- `{score}`, `{out_of}`, `{percent}`  
- `{#sections} … {/sections}` → `name`, `awarded`, `out_of`, `criteria[]` where criterion has `id`, `points`, `awarded`, and `summary`
- `{#notes} … {/notes}` → a list of strings
- CSV only: `{#events} … {/events}` where each event has `timestamp_utc`, `event_time_s`, `event_type`, `id`, `detail`, `points_delta`
- Verification partial: `{> verify_block}` exposes `overrides_json` and `sha256_plaintext`

> **Note:** The templates are engine‑agnostic. In practice, the Instructor prompt fills these tokens directly during `/grade.export`.

## Example Invocations
```text
# Markdown export with verification block
/grade.export format=md template=default include=verification

# CSV export using default template
/grade.export format=csv template=default

# Use a custom template on disk
/grade.export format=md template=path:templates/exports/my_custom.md.tmpl include=verification
```

## Verification Block Fields
Appended when `include=verification` is set:
- `timestamp_utc` — time the export was generated
- `tool_version` — prompt/spec/grader version string (e.g., `spec:1.0`)
- `scenario_id`, `run_id`, `student_id`
- `overrides` — JSON list of any `/grade.override` operations with reasons
- `sha256_plaintext` — hex digest of the plaintext report body for tamper evidence

## Default Templates (for reference)

### `grade_export.md.tmpl`
```md

<!-- EMSTrainer Export Template v1 (Markdown) -->
# EMSTrainer — Feedback Report (Student Copy)

**Scenario:** {{scenario_id}} — {{scenario_title}}  
**Run ID:** {{run_id}}  
**Student:** {{student_id}}  
**Graded (UTC):** {{timestamp_utc}}  
**Spec Version:** {{spec_version}}

## Summary
**Score:** {{score}} / {{out_of}} (**{{percent}}%**)

### Notes at a glance
{{#notes}}
- {{.}}
{{/notes}}
{{^notes}}
- No instructor notes.
{{/notes}}

---

## Section Breakdown
{{#sections}}
**{{name}}** — {{awarded}} / {{out_of}}
{{#criteria}}
- {{id}} — {{awarded}} / {{points}} {{summary}}
{{/criteria}}

{{/sections}}

{{#include_verification}}
---
## Verification
{{> verify_block}}
{{/include_verification}}

```

### `verify_block.md.tmpl`
```md

- timestamp_utc: {{timestamp_utc}}
- tool_version: {{tool_version}}
- scenario_id: {{scenario_id}}
- run_id: {{run_id}}
- student_id: {{student_id}}
- overrides: {{overrides_json}}
- sha256_plaintext: {{sha256_plaintext}}

```

### `grade_export.csv.tmpl`
```csv

# EMSTrainer Export Template v1 (CSV)
# Columns: timestamp_utc,event_time_s,event_type,id,detail,points_delta
# NOTE: Lines beginning with # are comments and should be removed in final output.

timestamp_utc,event_time_s,event_type,id,detail,points_delta
{{#events}}
{{timestamp_utc}},{{event_time_s}},{{event_type}},{{id}},{{detail}},{{points_delta}}
{{/events}}

```
