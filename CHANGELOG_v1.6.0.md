# EMSTrainer Changelog - v1.6.0

**Release Date:** 2025-01-06  
**Branch:** feat/strict-json-code-blackout  
**Breaking Changes:** Yes (file structure reorganization)

---

## 🎯 Major Changes

### Modular Architecture
- **BREAKING:** Split monolithic `EMSTrainer_Core_Prompt.txt` into modular files
- Created `EMSTrainer_Core.txt` (16k): Foundation + Test/Study modes
- Created `EMSTrainer_Scenario_Mode.txt` (23k): Scenario engine with all features
- Eliminated character limit concerns (drag-and-drop support)

### GPT-5 Requirement
- **BREAKING:** Now requires GPT-5 for medical accuracy
- Must be manually enabled in Copilot/ChatGPT settings
- Added warnings in all documentation

---

## ✨ New Features

### Difficulty System Overhaul
- Explicit definitions for all 4 difficulty modes
- Easy: Learning-focused, no penalties, supportive
- Standard: NREMT-level, realistic, balanced
- Hard: Strict timing, penalties, consequences
- Monica: Extreme ("pants on fire"), all modules max

### Air Care Paramedic (ACP) Level
- New provider level between Paramedic and CCP
- Skills: Cricothyrotomy, RSI, blood products, flight physiology
- Cannot: Advanced ventilator modes, ECMO
- Added to partner pool (`emstrainer_partner_names.json`)

### Continuous Scene Safety Assessment
- Scenarios can START unsafe (require staging)
- Dynamic scene deterioration during care
- Hidden grading criteria (15 points)
- Students must continuously reassess

### Dynamic Equipment Failures
- IV access failures (vein blows, infiltration)
- Monitor issues (battery, leads, reboots)
- Oxygen equipment (regulator, tank, BVM)
- Airway equipment (suction, lights, leaks)
- Probability scales with difficulty (0% to 35%)

### Hidden Grading Criteria
- **5 Rights Medication Check** (10 pts): Patient, Drug, Dose, Route, Time
- **AIDET Communication** (10 pts): Acknowledge, Introduce, Duration, Explanation, Thank you
- **Scene Safety Reassessment** (15 pts): Continuous throughout

### Enhanced Debrief Format
- Timing analysis (target vs actual vs hard max)
- Timestamped action log with partner interactions
- Hidden criteria scores revealed
- Difficulty-specific feedback
- Markdown source + PDF output
- Standardized filename: `[Date]_[ScenarioID]_Debrief_[StudentID].md`

### Vitals Trending by Difficulty
- Easy: Slow decline, rapid improvement, forgiving
- Standard: Realistic response to interventions
- Hard: Faster decompensation, requires correct care
- Monica: RAPID decline, minimal error tolerance

### Partner Interaction Tracking
- Partner actions appear in timestamped log
- Shows orders given, confirmations, completions, failures
- Integrated into debrief timeline

---

## 📚 Documentation

### New Files
- `docs/Student_Quick_Start_Guide.md` - Comprehensive student onboarding
- `docs/Instructor_Quick_Start_Guide.md` - Instructor workflow guide
- `docs/WHATS_NEW_v1.6.0.md` - This release summary
- `examples/scenario_cardiac_arrest_vf.json` - Standard ACLS example
- `examples/scenario_mvc_trauma_monica.json` - Monica Mode example

### Updated Files
- `README.md` - Complete restructure for v1.6.0
- `planning/EMSTrainer_Feature_Document.md` - Added v1.6 features
- `planning/EMS_Trainer_Future_Ideas_with_Status.md` - Updated roadmap

---

## 🔧 Technical Improvements

### Local Provider Scope Customization
- Added `assets/schema/provider_levels.schema.json`
- Added `assets/provider_levels.json` example
- Supports jurisdiction-specific scope overrides
- Add/remove skills per level without editing prompts

### Repository Cleanup
- Removed old monolithic prompt file
- Removed GitHub workflow validations (temporary, will restore later)
- Organized folder structure
- Added example scenarios

---

## 🐛 Bug Fixes

None - this is a feature release with architecture refactor.

---

## 🔄 Migration Guide

### For Students (v1.5.x → v1.6.0):

1. **Delete old bookmarks:**
   - Remove references to `EMSTrainer_Core_Prompt.txt`

2. **Enable GPT-5:**
   - Open Copilot/ChatGPT settings
   - Manually enable GPT-5 model

3. **Load new files:**
   - Drag `EMSTrainer_Core.txt` into chat (Test/Study)
   - Optional: Drag `EMSTrainer_Scenario_Mode.txt` (Scenarios)

4. **Review guide:**
   - Read `docs/Student_Quick_Start_Guide.md`

### For Instructors (v1.5.x → v1.6.0):

1. **Enable GPT-5:**
   - Open Copilot/ChatGPT settings
   - Manually enable GPT-5 model

2. **Load new files:**
   - Drag `EMSTrainer_Core.txt` into chat
   - Optional: Drag `EMSTrainer_Scenario_Mode.txt`

3. **Review examples:**
   - Check `examples/scenario_cardiac_arrest_vf.json`
   - Check `examples/scenario_mvc_trauma_monica.json`

4. **Customize scope (optional):**
   - Copy `assets/provider_levels.json`
   - Modify for your jurisdiction
   - Reference in scenarios

5. **Review guide:**
   - Read `docs/Instructor_Quick_Start_Guide.md`

---

## 📋 Known Issues

None at release.

---

## 🚀 Coming in v1.7 (Planned)

- Scenario encryption (prevent tampering)
- Equipment timing delays (LUCAS setup, EtCO2 calibration)
- In-prompt scenario editor
- Instructor test/study generation on specific topics
- Enhanced tamper detection

---

## 📊 Statistics

- **Files Added:** 8
- **Files Modified:** 10
- **Files Removed:** 4
- **Lines Added:** ~1,900
- **Lines Removed:** ~600
- **Net Change:** +1,300 lines

---

## 🙏 Acknowledgments

- Beta testers (5 active)
- EMS subject matter experts
- Development tooling: Claude 3.5 Sonnet (Cursor), GPT-5 (target platform)

---

## 📞 Support

- Review Quick Start Guides in `docs/`
- Check planning documents in `planning/`
- Contact instructor or project maintainer
- Report issues via repository

---

*EMSTrainer v1.6.0 - Released 2025-01-06*  
*Previous Version: v1.5.6.3 (2025-10-06)*
