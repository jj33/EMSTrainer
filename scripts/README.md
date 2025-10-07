# EMSTrainer Scripts

This folder contains utility scripts for importing, cleaning, and organizing EMS training materials.

---

## 🧹 cleanup-import.sh

Organizes imported files by version and type.

### Usage

Dry-run (preview changes):

    ./scripts/cleanup-import.sh v1.6.0

Apply changes:

    ./scripts/cleanup-import.sh v1.6.0 --apply

### What It Does

- Normalizes filenames (spaces → underscores, removes special characters)
- Archives old versions into `docs/archive/<version>/`
- Routes files:
  - `.pages` → `docs/source/`
  - `.pdf` → `assets/`
  - `.docx` → `docs/needs-convert/` (with reminder to convert)
- Checks for large files (>90MB)

---

## 🧪 Tips

- Always run in dry-run mode first to preview changes
- Convert `.docx` files to `.pages` before committing
- Tag cleaned versions with `vX.Y.Z-cleanup` for easy reference

---

---

## 📄 generate_pdfs.py / generate_pdfs.sh

Automatically generate PDFs from Markdown documentation for deployment packages.

### Usage

**Python version (recommended):**

    python3 scripts/generate_pdfs.py

**Shell version (requires Homebrew):**

    ./scripts/generate_pdfs.sh

### What It Does

- Converts all key markdown docs to PDF
- Applies professional styling (headers, tables, code blocks)
- Outputs to `docs/pdf/` directory
- Ready for inclusion in release archives

### Files Converted

- Instructor Quick Start Guide
- Instructor Reference Guide
- Student Quick Start Guide
- What's New (release notes)
- Ready for Testing docs
- README

### Requirements

**Python version:**
- Installs automatically: `markdown` and `weasyprint`
- Pure Python, cross-platform

**Shell version:**
- Requires: `pandoc` (installs via brew if needed)
- Optional: `wkhtmltopdf` for better formatting

### Adding New Files

Edit the `files` list in either script:

```python
files = [
    'docs/Your_New_Guide.md',
    # ...
]
```

---

## 🛠 Future Scripts

You can add more tools here for:
- Scenario generation helpers
- Study guide exports
- Version diffing
- Batch grading automation
