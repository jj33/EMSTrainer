# EMSTrainer CI Linter (One-Shot)

**Date:** 2025-10-05

This package provides a CI-friendly one-shot linter and fixes the wrapper so positional roots like `.` are accepted.

## Files
- `tools/lint_emstrainer_prompts.py` — Python linter (supports positional ROOT, `--dry-run`, `--backup`, and `--exit-nonzero-on-changes`).
- `tools/run_lint.sh` — Wrapper accepting optional repo root and flags (defaults to dry-run if none provided).
- `tools/lint_ci.sh` — One-shot CI tool: dry-run fails with exit code **2** if changes needed; `--apply` auto-fixes and exits 0.

## Quick Use
```bash
# Preview (no changes)
bash tools/run_lint.sh . --dry-run

# Apply (keeps .bak backups)
bash tools/run_lint.sh . --backup
```

## CI (GitHub Actions) Example
```yaml
name: Lint Prompts
on: [pull_request]

jobs:
  lint-prompts:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - name: Run EMSTrainer linter (fail on changes)
        run: |
          bash tools/lint_ci.sh --root .
```

### Auto-fix Workflow (Optional)
```yaml
name: Lint & Auto-Fix Prompts
on: workflow_dispatch

jobs:
  fix-prompts:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${ github.head_ref }
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - name: Apply linter fixes
        run: |
          bash tools/lint_ci.sh --root . --apply
      - name: Commit changes
        run: |
          git config user.name "github-actions"
          git config user.email "github-actions@users.noreply.github.com"
          git add -A
          if ! git diff --cached --quiet; then
            git commit -m "chore: lint prompts (auto-fix)"
            git push
          else
            echo "No changes to commit"
          fi
```
