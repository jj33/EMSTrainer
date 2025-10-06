# EMSTrainer Tools

Utility scripts for development and maintenance.

## Cleanup Scripts

### cleanup_common.sh
**Use:** Regular maintenance  
**Purpose:** Remove common development artifacts  
**Removes:** .DS_Store, Python cache, temp files, logs  
**Run:** `./tools/cleanup_common.sh` anytime

### cleanup_v1.6.0_refactor.sh
**Use:** One-time only (v1.6.0 migration)  
**Purpose:** Remove obsolete files from architecture refactor  
**Run once:** `./tools/cleanup_v1.6.0_refactor.sh`  
**Then delete:** This script after running

## Lint Scripts

### lint_emstrainer_prompts.py
**Purpose:** Enforce UI suppression policy in prompt files  
**What it does:**
- Removes markdown checkboxes `- [ ]` → bullets `•`
- Strips interactive HTML tags (button, form, input, etc.)
- Removes YAML front matter `---`

**Usage:**
```bash
# Check for issues (dry run)
python3 tools/lint_emstrainer_prompts.py . --dry-run

# Fix issues (creates .bak backups)
python3 tools/lint_emstrainer_prompts.py . --backup
```

### lint_ci.sh
**Purpose:** Wrapper script for CI/CD integration  
**Usage:**
```bash
# Check only
./tools/lint_ci.sh

# Apply fixes
./tools/lint_ci.sh --apply
```

## Why Lint Scripts?

EMSTrainer enforces **UI suppression** to prevent clickable elements in AI chat interfaces (Copilot, ChatGPT). These scripts ensure prompt files never contain:
- Markdown checkboxes (render as clickable in some clients)
- HTML form elements
- Interactive widgets

This keeps the experience consistent across platforms.

---

*Tools for EMSTrainer v1.6.0+*
