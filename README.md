# EMSTrainer

**Version:** v1.6.1  
**Released:** October 10, 2025  
**Status:** Production Ready

**Latest Release:** [Download v1.6.1](https://github.com/jj33/EMSTrainer/releases/tag/v1.6.1)

---

## Overview

EMSTrainer is an AI-powered EMS training system with three modes: **Scenario Practice**, **Test Questions**, and **Study Guides**. Designed for both students and instructors, it provides realistic training scenarios with automatic grading and detailed feedback.

### Two-Part System
- **👨‍🎓 Student Side:** Practice scenarios, generate study materials, receive immediate feedback
- **👨‍🏫 Instructor Side:** Create scenarios, generate tests/study guides, deploy to students, auto-grade submissions

---

## ⚠️ Requirements

### GPT-5 Required
**EMSTrainer requires GPT-5** for medical accuracy and clinical reasoning.

- **Available in:** Microsoft Copilot (free tier) or ChatGPT Plus
- **How to enable:** Open settings in Copilot/ChatGPT and manually enable GPT-5
- **DO NOT use:** GPT-4 or earlier models (insufficient medical knowledge)

### Device Recommendations
- **Best:** Laptop or desktop computer
- **Mobile:** Bluetooth keyboard strongly recommended
- **Voice input:** Works but less precise for medical terminology

---

## 🚀 Quick Start

### For Students:
1. **Download:** [Student Package v1.6.1](https://github.com/jj33/EMSTrainer/releases/download/v1.6.1/EMSTrainer_Student_v1.6.1.zip)
2. **Enable GPT-5** in Copilot or ChatGPT
3. **Load prompts:** Drag and drop files into your AI assistant
4. **Start practicing:** Choose your mode and difficulty
5. **Get feedback:** Receive detailed performance analysis

📖 See [Student Quick Start Guide](docs/Student_Quick_Start_Guide.md) for detailed instructions.

### For Instructors:
1. **Download:** [Instructor Package v1.6.1](https://github.com/jj33/EMSTrainer/releases/download/v1.6.1/EMSTrainer_Instructor_v1.6.1.zip)
2. **Load prompts:** Drag files into GPT-5
3. **Create content:** Scenarios, tests, and study guides via natural conversation
4. **Deploy to students:** Email templates provided
5. **Auto-grade:** Paste student submissions for instant feedback and class summaries

📖 See [Instructor Quick Start Guide](docs/Instructor_Quick_Start_Guide.md) and [Instructor Reference Guide](docs/Instructor_Reference_Guide.md).

---

## ✨ What's New in v1.6.1

### 🚨 Code Blackout Scenario
- Monica-level mega-code (60-minute cascading emergency)
- Multi-system patient complexity
- Equipment realism and failures
- 1000-point grading rubric

### 📊 PlatinumPlanner Integration
- Step-by-step test export instructions
- Upload test results for personalized training
- Focus on weak areas automatically

### 🛠️ Improvements
- PDF generation using pure Python (reportlab)
- Temporary chat mode recommendations
- Enhanced equipment tracking in scenarios
- Continue.dev workflow rules for contributors

### 📖 What's New in v1.6.0

### 🏗️ Modular Architecture
- Split into Core, Scenario Mode, and Instructor prompts
- No more character limits (drag-and-drop files)
- Easier maintenance and updates

### 🎯 Four Difficulty Modes
- **Easy:** Learning-focused, hints provided, no penalties
- **Standard:** NREMT-level, realistic timing, balanced support
- **Hard:** Strict timing, equipment failures (20-25%), minimal hints
- **Monica:** Extreme difficulty (30-35% failures), hard fail on timeout

### 👨‍🏫 Instructor Tools
- Create custom scenarios via conversation
- Generate test questions on any topic
- Create study guides for students
- Auto-grade submissions with detailed feedback
- Generate class performance summaries

### 👨‍🎓 Student Tools
- Practice realistic scenarios
- Generate targeted study materials
- Upload test results for personalized practice questions
- Receive comprehensive performance debriefs

### 🚨 Continuous Scene Safety
- Not a one-time check
- Scenarios can start unsafe (require staging)
- Dynamic degradation during care
- Hidden grading criteria (15 points)

### 🔧 Equipment Failures
- IV failures, monitor issues, O2 problems, airway challenges
- Realistic probability scaling by difficulty (0% → 35%)
- Students must adapt and use backup options

### 🔒 Hidden Grading
- 5 Rights medication check (10 pts)
- AIDET communication (10 pts)
- Scene safety reassessment (15 pts)
- Students discover through debriefs

### ✈️ ACP Provider Level
- Air Care Paramedic support
- Advanced airway, vent management, critical care meds
- Helicopter operations context

### ✅ Quality Assurance
- 100% validated with 30-student stress test
- Perfect grade distribution (8A, 4B, 5C, 13D)
- Regression baseline established
- All data integrity checks passed

📖 See [WHATS_NEW_v1.6.0.md](docs/WHATS_NEW_v1.6.0.md) for complete details.

---

## 📁 Repository Structure

```
EMSTrainer/
├── prompts/                    # AI prompt files
│   ├── EMSTrainer_Core.txt                  Foundation + Test/Study
│   ├── EMSTrainer_Student_Interface.txt     Student interface
│   └── EMSTrainer_Instructor_Interface.txt  Instructor interface
├── deployment/                # Release packages
│   ├── instructor_package_v1.6.1/
│   └── student_package_v1.6.1/
├── docs/                      # Documentation
│   ├── Student_Quick_Start_Guide.md
│   ├── Instructor_Quick_Start_Guide.md
│   ├── Instructor_Reference_Guide.md
│   └── WHATS_NEW_v1.6.0.md
├── examples/                  # Sample scenarios
│   ├── scenario_cardiac_arrest_vf.json
│   └── scenario_mvc_trauma_monica.json
├── assets/scenarios/          # Advanced scenarios
│   ├── code_blackout_scenario.json       # Monica-level mega-code
│   └── code_blackout_grading_rubric.json # 1000-point rubric
├── tests/                     # Testing & validation
│   ├── baseline/                  # Regression baseline
│   └── results/                   # Test reports
├── scripts/                   # Automation tools
└── planning/                  # Features & roadmap
```

---

## 🛠️ Configuration & Customization

### Provider Scope Customization
Create `assets/provider_levels.json` to override default scope by jurisdiction:

```json
{
  "EMT": {
    "can_perform": ["IV", "IO", "12-lead", "limited_medications"],
    "cannot_perform": ["advanced_airway", "RSI"]
  }
}
```

See `examples/provider_levels_expanded_emt.json` for a complete example.

---

## 🧪 Testing & Validation

### Automated Testing
Run validation scripts to check test data integrity:
```bash
python3 scripts/validate_test_results.py
```

### Regression Baseline
The v1.6.1 release includes a 30-student stress test baseline in `tests/baseline/`.

See `tests/TEST_PLAN.md` and `tests/README_TESTING_FRAMEWORK.md` for details.

---

## 📚 Documentation

- **[Student Quick Start Guide](docs/Student_Quick_Start_Guide.md)** - Get started as a student
- **[Instructor Quick Start Guide](docs/Instructor_Quick_Start_Guide.md)** - Set up as an instructor
- **[Instructor Reference Guide](docs/Instructor_Reference_Guide.md)** - Command reference
- **[What's New v1.6.0](docs/WHATS_NEW_v1.6.0.md)** - Release highlights
- **[CHANGELOG](CHANGELOG.md)** - Version history
- **[CONTRIBUTING](CONTRIBUTING.md)** - Contribution guidelines

---

## 🚀 Releases

**Latest:** [v1.6.1](https://github.com/jj33/EMSTrainer/releases/tag/v1.6.1) - October 10, 2025

### Download Packages:
- [Instructor Package](https://github.com/jj33/EMSTrainer/releases/download/v1.6.1/EMSTrainer_Instructor_v1.6.1.zip)
- [Student Package](https://github.com/jj33/EMSTrainer/releases/download/v1.6.1/EMSTrainer_Student_v1.6.1.zip)

All documentation also available as PDFs in the release.

---

## 🔮 Coming in v1.7 (Q1 2026)

- Equipment timing delays (LUCAS 30-45s, EtCO₂ 15s calibration)
- Scenario encryption (AES-256 with digital signatures)
- In-prompt scenario editor
- Enhanced reporting and analytics
- First responders multi-agency scenarios (Fire/Police/FR)
- Instructor test/study generator

---

## 📜 License & Copyright

**Copyright © 2025 Joel Jameson**

FREE for individual student use. Institutional licensing available.

See [LICENSE](LICENSE) for complete terms.

---

## 🤝 Contributing

Contributions welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📞 Support

- **Documentation:** See guides in `docs/` directory
- **Issues:** [GitHub Issues](https://github.com/jj33/EMSTrainer/issues)
- **Discussions:** [GitHub Discussions](https://github.com/jj33/EMSTrainer/discussions)

---

*Last Updated: October 10, 2025*
