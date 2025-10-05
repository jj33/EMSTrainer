
# Export Formats (v1)

## Markdown (Student Copy)
- Human‑readable summary
- Sections with awarded points
- Optional verification block appended

## CSV (Instructor Record)
- Event stream + rubric scoring rows + summary row
- Columns: `timestamp_utc,event_time_s,event_type,id,detail,points_delta`
- Suitable for audit and cohort analysis

Templates live under `templates/exports/`. Use `/grade.export` to render.
