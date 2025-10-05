# EMSTrainer

**Branch:** `dev`  
**Current prompt:** [`prompts/EMSTrainer_Core_Prompt_v1.5.6.1.txt`](prompts/EMSTrainer_Core_Prompt.txt)

## Overview
EMSTrainer is a Copilot-driven EMS training assistant with three learner modes (Scenario, Test Questions, Study Guide) and an instructor timing overlay. The **student-facing logic** lives entirely in the **core prompt**; **instructor overrides** are supplied via JSON assets.

## Quick Start
1. Ensure you are on the `dev` branch and pull latest.
2. Review or edit config under [`assets/`](assets/).
3. Use the **core prompt** above with Microsoft Copilot (GPT-5 enabled). Select **Scenario**, **Test Questions**, or **Study Guide**; optionally set **difficulty**.
4. For Monica evaluation, set difficulty to **Monica**.

## Folders
- `prompts/` — core prompt(s) by version.  
  ↳ **Current:** [`EMSTrainer_Core_Prompt_v1.5.6.1.txt`](prompts/EMSTrainer_Core_Prompt_v1.5.6.1.txt)
- `assets/` — instructor-configurable JSON (timing, provider levels, partners, module toggles, security policy). See [`assets/README.md`](assets/README.md).
- `schemas/` — JSON Schemas validating asset formats.
- `docs/` — guides for testers and maintainers.  
  ↳ **Start here:** [`docs/TESTING_MONICA_v1.5.6.1.md`](docs/TESTING_MONICA_v1.5.6.1.md)
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
  - Supports Monica Mode (super-hard difficulty + timer).
  - Handles vitals trending, pediatric/OB fatality policy, and compressed prompt option.

#### **assets/**
- **instructor_config.json**  
  Stores instructor-defined overrides, such as:
  - Scenario toggles (Curveball, Monica Mode, Termination Timing).
  - Provider level configuration (EMR, EMT, AEMT, Paramedic, CCP).
  - Partner logic (certification level, task delegation rules).
- **emstrainer_partner_names.json**  
  Contains partner names and randomized certification levels for scenario realism.

---

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
