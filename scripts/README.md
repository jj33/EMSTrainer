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

## 🛠 Future Scripts

You can add more tools here for:
- Scenario generation
- Study guide exports
- Version diffing
