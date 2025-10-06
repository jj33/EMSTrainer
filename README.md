# EMSTrainer

**Branch:** `dev`  
**Current prompt:** [`prompts/EMSTrainer_Core_Prompt_v1.5.6.1.txt`](prompts/EMSTrainer_Core_Prompt.txt)
**Current Student Prompt:** [`prompts/EMSTrainer_Core_Prompt.txt`](prompts/EMSTrainer_Core_Prompt.txt)  
**Current Instructor Prompt:** [`prompts/EMSTrainer_Instructor_Prompt.txt`](prompts/EMSTrainer_Instructor_Prompt.txt) *(In Development)*

## Overview
EMSTrainer is a Copilot-driven EMS training assistant with three learner modes (Scenario, Test Questions, Study Guide) and an instructor timing overlay. The **student-facing logic** lives entirely in the **core prompt**; **instructor overrides** are supplied via JSON assets.

### Two-Part System
- **Student Side:** Run scenarios, practice skills, receive immediate feedback
- **Instructor Side:** Create scenarios, deploy to students, collect results, auto-grade submissions

## Quick Start

### For Students:
1. Ensure you are on the `dev` branch and pull latest.



2. Load [`prompts/EMSTrainer_Core_Prompt.txt`](prompts/EMSTrainer_Core_Prompt.txt) into your AI assistant (Copilot, ChatGPT, Claude).
3. Select **Scenario**, **Test Questions**, or **Study Guide** mode.
4. Choose difficulty: Easy, Standard, Hard, or **Monica Mode** (super hard with timer).

### For Instructors:
1. Load [`prompts/EMSTrainer_Instructor_Prompt.txt`](prompts/EMSTrainer_Instructor_Prompt.txt) into your AI assistant.
2. Create scenarios, deploy to students, and auto-grade submissions.
3. Review templates in [`docs/imports/EMSTrainer_v1.5.3_Planning_Files/`](docs/imports/EMSTrainer_v1.5.3_Planning_Files/).

## Folders


- `prompts/` — Student and Instructor prompt files.  
  ↳ **Student:** [`EMSTrainer_Core_Prompt.txt`](prompts/EMSTrainer_Core_Prompt.txt)  
  ↳ **Instructor:** [`EMSTrainer_Instructor_Prompt.txt`](prompts/EMSTrainer_Instructor_Prompt.txt) *(v1.6 - In Development)*
- `assets/` — instructor-configurable JSON (timing, provider levels, partners, module toggles, security policy). See [`assets/README.md`](assets/README.md).
- `schemas/` — JSON Schemas validating asset formats.
- `docs/` — guides for testers and maintainers.  

  ↳ **Student Testing:** [`docs/TESTING_MONICA_v1.5.6.1.md`](docs/TESTING_MONICA_v1.5.6.1.md)  
  ↳ **Instructor Guide:** [`docs/imports/EMSTrainer_v1.5.3_Planning_Files/`](docs/imports/EMSTrainer_v1.5.3_Planning_Files/) *(Templates)*
- `planning/` — Feature roadmaps and development tracking.  
  ↳ [`planning/EMSTrainer_Feature_Document.md`](planning/EMSTrainer_Feature_Document.md)  
  ↳ [`planning/EMS_Trainer_Future_Ideas_with_Status.md`](planning/EMS_Trainer_Future_Ideas_with_Status.md)
- `tools/` — helper scripts (e.g., repo layout validator).

## Monica Mode Highlights (v1.5.6.1)
- **Deterministic seed** (`module_toggles.monica_seed`) for reproducible runs.
- **Distractions overlay** forced **ON** in Monica; weighted, cooldown-limited; consumes simulated time only.
- **Latency tracking** forced **ON** in Monica; **ignored in Normal**; toggleable in Hard.
- **Objective-only debrief** (auto-redaction) in Monica by default.

## Configure via Assets
Edit the following as needed (validate with schemas):
- `assets/instructor_timing_config.json` — Monica timing preset; segments and consequences. 
- `assets/module_toggles.json` — `monica_seed`, `distractions`, `latency_tracking`, `auto_redact`, etc.  
- `assets/provider_levels.json` — provider scope maps.  
- `assets/emstrainer_partner_names.json` — partner pool.  
- `assets/security_policy.json` — filename template and retention policy.

## Testing
See [`docs/TESTING_MONICA_v1.5.6.1.md`](docs/TESTING_MONICA_v1.5.6.1.md) for acceptance criteria and regression checks.

## Validating Repo Layout
Run the layout validator to compare your working copy to the expected structure for this release:
```bash
python3 tools/validate_repo_layout.py
```
It reports **missing**, **unexpected**, and **mismatched** paths relative to repo root.

## Versioning
See [`CHANGELOG.md`](CHANGELOG.md) for full details.


#### **prompts/**
- **EMSTrainer_Core_Prompt.txt**  
  This is the **canonical student-facing prompt**. All updates to student logic, scenario handling, and difficulty settings should be made here.  
  - Includes Scenario, Test, and Study modes.

  - Supports four difficulty levels: Easy, Standard, Hard, and Monica Mode (super-hard difficulty + timer).
  - Handles vitals trending, pediatric/OB fatality policy, and compressed prompt option.

- **EMSTrainer_Instructor_Prompt.txt** *(v1.6 - In Development)*  
  Chat-based interface for instructors to:
  - Create and customize training scenarios
  - Deploy scenarios to students
  - Collect and auto-grade student submissions
  - Generate performance summaries and reports

#### **assets/**
- **instructor_config.json**  
  Stores instructor-defined overrides, such as:
  - Scenario toggles (Curveball, Monica Mode, Termination Timing).
  - Provider level configuration (EMR, EMT, AEMT, Paramedic, CCP).
  - Partner logic (certification level, task delegation rules).
- **emstrainer_partner_names.json**  
  Contains partner names and randomized certification levels for scenario realism.
## Continuous Integration: Validate Examples & Exports

We now have a GitHub Actions workflow (`.github/workflows/validate.yml`) that runs on every pull request to the `dev` branch.

### **Versioning Policy**
- **Canonical File:**  
  `prompts/EMSTrainer_Core_Prompt.txt` is the single source of truth for student-facing logic.
- **History:**  
  Older versions are **not retained in the repo**. Use Git history for rollback if needed.
- **Instructor Config:**  
  Instructor overrides and settings live in JSON files under `assets/`. These files are version-controlled.

---

### **Role Separation**
- **Student Workflow:**  
  Driven by `EMSTrainer_Core_Prompt.txt`. Students interact only with this logic.
- **Instructor Workflow:**  
  Instructor Scenario Creation and grading logic are handled separately via JSON/Python assets.  
  - Encryption and timestamping are applied to both instructor and student files to prevent tampering.
  - Auto-grading supported with secure naming conventions for submissions.

---

### **Special Features**
- **Monica Mode:**  
  Enables maximum difficulty with a timer and Curveball module.
- **Partner Logic:**  
  Students define their role and partner certification level.  
  - Default: Paramedic → EMT partner; EMT → Paramedic partner.
  - Partner acts only when directed by the student.

---

### **Contribution Guidelines**
- **Do not edit archived files** (none exist in repo; use Git history if needed).
- **Update only EMSTrainer_Core_Prompt.txt** for student logic.
- Instructor configs should be modified via JSON in `assets/`.
---
*Updated 2025-10-05*
### What it does
- **Validate job**: Runs `make validate` to check all JSON, CSV, and Markdown files under `examples/` and `exports/`.
- **Exports smoke test**: Runs `make exports` to generate demo ACS export files (MD + CSV) and uploads them as artifacts.

### Why it matters
This ensures that broken example files or export logic never reach `dev`. If validation fails, the PR cannot be merged.

### How to check locally
Before pushing your changes:

```bash
make validate   # Validate examples and exports
make exports    # Generate demo export files
```

If either command fails, fix the issues before committing.
