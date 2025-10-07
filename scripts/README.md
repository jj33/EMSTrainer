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

## 🧪 validate_test_results.py

Validates EMSTrainer test data locally without hitting AI provider limits.

### Usage

Validate default test directory:

    python3 scripts/validate_test_results.py

Validate specific directory:

    python3 scripts/validate_test_results.py tests/VF_Paramedic_Standard_Graded

### What It Validates

- **JSON Structure**: All required fields present
- **Grade Distribution**: Matches expected performance tiers
- **Score Statistics**: Min, max, mean calculations
- **Hash Validation**: Scenario integrity checks
- **ROSC Outcomes**: Clinical outcome analysis
- **Data Consistency**: JSON ↔ CSV matching

### Why This Script?

**Problem:** Large test files (232KB combined JSON) cause HTTP 400 errors when loading into AI chat.  
**Solution:** Process files locally using Python - fast, reliable, no API limits.

### Output

Generates detailed validation report with:
- ✅ Pass/Fail for each check
- 📊 Grade distribution comparison
- 📈 Score statistics
- 🔐 Hash validation results
- 💓 ROSC rate analysis

### Example Output

```
======================================================================
EMSTrainer Test Validation Report
======================================================================

✅ Loaded 30 JSON files
✅ 30/30 files have valid structure

📊 Grade Distribution Analysis...
Grade    Expected     Actual       Diff     Status
--------------------------------------------------
A        8            8             +0      ✅
B        4            4             +0      ✅
C        5            5             +0      ✅
D        13           13            +0      ✅

✅ ALL VALIDATION CHECKS PASSED!
```

---

## 🛠 Future Scripts

You can add more tools here for:
- Scenario generation
- Scenario generation helpers
- Study guide exports
- Version diffing
- Batch grading automation
