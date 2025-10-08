# EMSTrainer

**Version:** v1.6.0  
**Released:** January 2025  
**Status:** Production Ready

**Latest Release:** [v1.6.0](https://github.com/jj33/EMSTrainer/releases/tag/v1.6.0)

## Overview
EMSTrainer is a Copilot-driven EMS training assistant with three learner modes (Scenario, Test Questions, Study Guide) and an instructor timing overlay. The **student-facing logic** lives entirely in the **core prompt**; **instructor overrides** are supplied via JSON assets.

### Two-Part System
- **Student Side:** Run scenarios, practice skills, receive immediate feedback
- **Instructor Side:** Create scenarios, deploy to students, collect results, auto-grade submissions

## Requirements

### ⚠️ IMPORTANT: GPT-5 Required

**EMSTrainer requires GPT-5** (available in Microsoft Copilot or ChatGPT) for medical accuracy.

- **Why GPT-5?** Medical knowledge depth, protocol accuracy, and clinical reasoning
- **How to enable:** Open Copilot/ChatGPT settings and manually enable GPT-5
- **DO NOT use:** GPT-4o mini or earlier models (insufficient medical accuracy)

### 📱 Mobile Use

**Keyboard recommended** for mobile devices - typing scenarios and orders with on-screen keyboard is limiting. Consider:
- Bluetooth keyboard for tablets/phones
- Laptop/desktop for best experience
- Voice-to-text as alternative (though less precise for medical terms)

## 🚀 Quick Start

### For Students:
1. **Download:** [Student Package v1.6.0](https://github.com/jj33/EMSTrainer/releases/tag/v1.6.0)
2. **Enable GPT-5** in Copilot or ChatGPT (see Requirements above)
3. **Load prompts:** Drag and drop the files into your AI assistant
4. **Start practicing:** Choose Test Questions, Study Guide, or Scenario mode
5. **Select difficulty:** Easy, Standard, Hard, or Monica Mode

See [Student Quick Start Guide](docs/Student_Quick_Start_Guide.md) for detailed instructions.

### For Instructors:
1. **Download:** [Instructor Package v1.6.0](https://github.com/jj33/EMSTrainer/releases/tag/v1.6.0)
2. **Load prompts:** Drag files into GPT-5
3. **Create scenarios, tests, and study guides**
4. **Deploy to students via email**
5. **Auto-grade submissions and generate class summaries**

See [Instructor Quick Start Guide](docs/Instructor_Quick_Start_Guide.md) and [Instructor Reference Guide](docs/Instructor_Reference_Guide.md) for complete documentation.

## 📁 Repository Structure

```
EMSTrainer/
├── prompts/                    # AI prompt files
│   ├── EMSTrainer_Core.txt            (16k) Foundation + Test/Study
│   ├── EMSTrainer_Scenario_Mode.txt   (23k) Scenario engine
│   └── EMSTrainer_Instructor_Prompt.txt (21k) Instructor interface
├── deployment/                # Release packages
│   ├── instructor_package_v1.6.0/
│   └── student_package_v1.6.0/
├── docs/                      # Documentation
│   ├── Student_Quick_Start_Guide.md
│   ├── Instructor_Quick_Start_Guide.md
│   ├── Instructor_Reference_Guide.md
│   └── WHATS_NEW_v1.6.0.md
├── examples/                  # Sample scenarios
│   ├── scenario_cardiac_arrest_vf.json
│   └── scenario_mvc_trauma_monica.json
├── tests/                     # Testing & validation
│   ├── baseline/                  # Regression baseline
│   └── results/                   # Test reports
├── scripts/                   # Automation tools
└── planning/                  # Features & roadmap
```

## ✨ What's New in v1.6.0

### Major Features:
- **🏛️ Modular Architecture** - Split into Core, Scenario Mode, and Instructor prompts (no more character limits!)
- **🎯 4 Difficulty Modes** - Easy (learning), Standard (NREMT-level), Hard (challenge), Monica (extreme)
- **👨‍🏫 Instructor Tools** - Create scenarios, generate tests/study guides, auto-grade with detailed feedback
- **👩‍🎓 Student Tools** - Practice scenarios, get targeted study materials, receive comprehensive debriefs
- **🚨 Continuous Scene Safety** - Not a one-time check; scenarios can start unsafe or degrade dynamically
- **🔧 Equipment Failures** - Realistic failures (IV, monitor, O2, airway) with probability scaling by difficulty
- **🔒 Hidden Grading** - 5 Rights, AIDET, scene safety reassessment (students discover through feedback)
- **✈️ ACP Provider Level** - Air Care Paramedic support with advanced scope

### Quality Assurance:
- **✅ 100% Validated** - 30-student stress test with perfect grade distribution
- **📊 Regression Baseline** - Established for future stability testing
- **📝 Complete Documentation** - Quick Start Guides, Reference Guides, and comprehensive READMEs

See [WHATS_NEW_v1.6.0.md](docs/WHATS_NEW_v1.6.0.md) for complete details.

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
---

## 📜 License & Copyright

**Copyright © 2025 Joel Jameson**

See [LICENSE](LICENSE) for complete terms.

---

*Last Updated: January 7, 2025*
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
