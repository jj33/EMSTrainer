# EMSTrainer v1.6.1 Release Notes

**Release Date:** October 10, 2025  
**Version:** 1.6.1  
**Status:** Production Ready

---

## 🎯 Overview

v1.6.1 adds the **Code Blackout** Monica-level mega-code scenario, PlatinumPlanner test export instructions, architecture improvements, and enhanced documentation.

---

## 📦 Download

### 👨‍🎓 For Students:
- **Package:** `EMSTrainer_Student_v1.6.1.zip`
- **Includes:** Core.txt, Student Interface, Scenario examples, Quick Start Guide

### 👨‍🏫 For Instructors:
- **Package:** `EMSTrainer_Instructor_v1.6.1.zip`
- **Includes:** Core.txt, Instructor Interface, Scenario creation tools, Reference guides

---

## ✨ What's New

### 🚨 Code Blackout Scenario

**Monica-level mega-code challenge** - A 60-minute cascading medical emergency designed to push experienced providers to their limits.

**Features:**
- Multi-system patient complexity (hypoglycemia, bradycardia, hypothermia, hypoxia)
- Equipment realism (limited O2, 20-minute monitor battery)
- Dynamic wife character (AIDET-responsive)
- Medical-based arrest triggers (not arbitrary timing)
- 1000-point grading rubric with timing penalties
- Instructor guide with setup instructions
- Student brief (spoiler-free)

**Files:**
- `assets/scenarios/code_blackout_scenario.json`
- `assets/scenarios/code_blackout_grading_rubric.json`
- `docs/Code_Blackout_Instructor_Guide.md`
- `docs/Code_Blackout_Student_Brief.md`

---

### 📊 PlatinumPlanner Integration

**Step-by-step instructions** for downloading test results from PlatinumPlanner to upload to EMSTrainer for personalized training.

**Includes:**
- Screenshot guide (3 images)
- Navigation instructions
- Export button location
- Integration into Student Quick Start Guide

**Benefit:** Students can upload their test results and get targeted practice on weak areas.

---

### 🏗️ Architecture Improvements

**Refactored to Core + Interface pattern:**

```
EMSTrainer_Core.txt                  ← Foundation (Test/Study modes)
├── EMSTrainer_Student_Interface.txt     ← Student-facing
└── EMSTrainer_Instructor_Interface.txt  ← Instructor-facing
```

**Benefits:**
- Cleaner separation of concerns
- Easier to maintain and update
- More modular architecture
- Better version compatibility checking

---

### 🛠️ Technical Improvements

**PDF Generation:**
- Switched from WeasyPrint to reportlab
- Pure Python solution (no system dependencies)
- Eliminates Cairo/Pango/GTK requirements
- Better cross-platform compatibility

**Equipment Tracking:**
- Enhanced tracking in Core.txt
- Preparation for v1.7.0 equipment timing delays

**Temporary Chat Mode:**
- Added recommendations to prevent AI hallucinations
- Explained in Student Quick Start Guide
- Best practice for long interactive scenarios

---

### 📚 Documentation Updates

**New Documents:**
- v1.7.0 Feature Planning (comprehensive roadmap)
- Code Blackout Instructor Guide
- Code Blackout Student Brief
- Continue.dev workflow rules (for contributors)

**Updated Documents:**
- Student Quick Start Guide (PlatinumPlanner, temp chat mode)
- README (v1.6.1 updates, structure corrections)
- CHANGELOG (complete v1.6.1 entry)

---

## 🔄 Upgrade Instructions

### From v1.6.0 to v1.6.1:

**For Students:**
1. Download new Student Package v1.6.1
2. Replace old prompt files with new ones
3. Load `EMSTrainer_Core.txt` first
4. Load `EMSTrainer_Student_Interface.txt` second
5. Optional: Try Code Blackout scenario (Monica Mode!)

**For Instructors:**
1. Download new Instructor Package v1.6.1
2. Replace old prompt files with new ones
3. Load `EMSTrainer_Core.txt` first
4. Load `EMSTrainer_Instructor_Interface.txt` second
5. Optional: Deploy Code Blackout to students

**Breaking Changes:** None - fully backward compatible

---

## 🧪 Testing

- Code Blackout scenario validated
- Architecture refactor tested
- PDF generation verified on multiple platforms
- All example scenarios confirmed working

---

## 📋 Known Issues

None currently.

---

## 🔮 Coming in v1.7.0 (Q1 2026)

### Priority 1 Features:
- **Equipment Timing Delays** - LUCAS (30-45s), EtCO₂ (15s), 12-lead (45s)
- **Scenario Encryption** - AES-256 password-based encryption
- **In-Prompt Scenario Editor** - Natural language scenario editing
- **Results Encryption** - Tamper-proof student submissions

### Priority 2 Features:
- **Instructor Test Generator** - Generate custom tests on any topic
- **Study Guide Generator** - Create targeted study materials
- **Multi-Agency Dynamics** - Fire, Police, First Responder integration

See `planning/v1.7.0_Feature_Planning.md` for complete roadmap.

---

## 📞 Support

- **Documentation:** [docs/](docs/) directory
- **Issues:** [GitHub Issues](https://github.com/jj33/EMSTrainer/issues)
- **Discussions:** [GitHub Discussions](https://github.com/jj33/EMSTrainer/discussions)

---

## 🙏 Credits

**Developed by:** Joel Jameson  
**Release Date:** October 10, 2025  
**License:** Copyright © 2025 - FREE for individual student use

---

## 📝 Changelog Summary

```
Added:
- Code Blackout Monica-level mega-code scenario
- PlatinumPlanner test export instructions with screenshots
- Architecture refactor (Core + Interface pattern)
- v1.7.0 comprehensive feature planning
- Temporary chat mode recommendations

Improved:
- PDF generation (reportlab instead of WeasyPrint)
- Equipment tracking in scenarios
- Documentation organization

Technical:
- Continue.dev workflow rules
- Session management documentation
- Testing standards documented
```

See [CHANGELOG.md](CHANGELOG.md) for complete details.

---

**Ready to train! 🚑**

*Live long and prosper!* 🖖
