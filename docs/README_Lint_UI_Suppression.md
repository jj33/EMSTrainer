# EMSTrainer UI Suppression + Linter Package

**Date:** 2025-10-05

This package provides:

- `prompts/EMSTrainer_Core_Prompt.txt` — Canonical prompt with **UI clickables suppression** and **Monica Mode** integrated, plus a **self-check header**.
- `assets/instructor_config.json` — Template enabling Monica Mode and `ui_suppression_selfcheck`.
- `tools/lint_emstrainer_prompts.py` — Batch linter to **remove Markdown checkboxes**, **strip interactive HTML**, and **remove YAML front matter**.
- `tools/run_lint.sh` — Convenience wrapper to run the linter against your repo.

## Install
1. Backup your existing `prompts/EMSTrainer_Core_Prompt.txt`.
2. Copy this `prompts/EMSTrainer_Core_Prompt.txt` over your repo's canonical prompt.
3. Copy/merge `assets/instructor_config.json` as needed.
4. (Optional) Run the linter on your repo:
   ```bash
   # From your repo root
   bash tools/run_lint.sh . --dry-run   # Preview changes
   bash tools/run_lint.sh . --backup    # Apply changes and keep .bak backups
   ```

## Self-Check Header
- On scenario start, the trainer prints: `[UI-SAFE ✓] Clickables suppressed; task lists disabled; HTML widgets disabled.`
- Disable by setting `ui_suppression_selfcheck` to `false` in `assets/instructor_config.json`.

## Notes
- The linter modifies only text-like files: `.txt`, `.md`, `.markdown`, `.prompt`.
- It converts `• Option` and `• Option` (and similar) to `• Option`.
- It removes interactive HTML tags but keeps inner text.
- It strips YAML front matter at file start.
