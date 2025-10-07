# What's New in EMSTrainer v1.6.0

**Release Date:** January 6, 2025  
**Branch:** feat/strict-json-code-blackout

---

## 🎯 Major Changes

### Modular Architecture
- **Split monolithic prompt** into focused, drag-and-drop modules
- **Core.txt (16k):** Foundation + Test/Study modes  
- **Scenario_Mode.txt (23k):** Complex scenarios with all features
- **No more character limits** - drag files into Copilot/ChatGPT!

### GPT-5 Required
- **Medical accuracy requirement** - GPT-5 mandatory for clinical content
- Earlier models (GPT-4o mini, etc.) lack necessary medical knowledge
- Clearly documented in README and guides

---

## ✨ New Features

### Provider Levels
- **Air Care Paramedic (ACP)** added between Paramedic and CCP
- Includes cricothyrotomy, RSI, blood products, flight physiology
- Local scope customization via `provider_levels.json`
- Delta notation (Base + additions/subtractions) for efficiency

### Difficulty Modes (Explicit)
- **Easy:** Learning-focused, no penalties, supportive environment
- **Standard:** NREMT-level, realistic, balanced difficulty  
- **Hard:** Strict timing, consequences, challenging scenarios
- **Monica:** Extreme difficulty - "pants on fire" mode for overconfident providers

### Scene Safety (Continuous Assessment)
- **Not a one-time check** - continuous reassessment required
- Scenarios can **start unsafe** (require staging for PD)
- Dynamic scene degradation during care
- Hidden grading criteria (15 points)
- Examples: Hostile crowds, unsafe structures, weapons present

### Dynamic Equipment Failures
- **IV Access:** First attempt can fail (blown vein, infiltration)
- **Monitor Issues:** Battery dies, leads disconnect, screen failures  
- **O2 Equipment:** Regulator failures, tank pressure issues
- **Airway Equipment:** Suction failures, laryngoscope issues
- Probability by difficulty: 0% (Easy) → 35% (Monica)
- Realistic time penalties (30-60 seconds)

### Hidden Grading Criteria
- **5 Rights Medication Check** (10 pts): Right Patient, Drug, Dose, Route, Time
- **AIDET Communication** (10 pts): Acknowledge, Introduce, Duration, Explanation, Thank you
- **Scene Safety Reassessment** (15 pts): Continuous throughout scenario
- Not announced to students - discovered through debriefs

### Enhanced Debriefs
- **Markdown source** for editing/archiving
- **PDF output** for student distribution
- **Timing analysis** table with target vs actual
- **Partner interactions** in timestamped timeline
- **Standardized filename:** `[Date]_[ScenarioID]_Debrief_[StudentID].md`

---

## 📚 Documentation

### Quick Start Guides
- **Student Quick Start Guide** - Comprehensive onboarding (Test/Study/Scenario modes)
- **Instructor Quick Start Guide** - Workflow and scenario creation
- Mobile keyboard recommendation added

### Example Scenarios
- **Standard ACLS:** `scenario_cardiac_arrest_vf.json`
- **Monica Mode Trauma:** `scenario_mvc_trauma_monica.json` (with curveballs)
- Complete JSON structure examples for instructors

---

## 🔧 Technical Improvements

### Hash Validation
- SHA-256 integrity checking for scenarios
- Detects tampering (warns instructor, doesn't auto-fail)
- Foundation for v1.7 encryption

### Partner Pool
- Added ACP partners: Skyler, Hawk
- Partner interactions logged in timeline
- Closed-loop communication tracked

### Timing Standards
- Industry benchmarks documented
- Enforcement varies by difficulty
- Easy: Explained only | Standard: Graded | Hard: Penalized | Monica: Hard fail

---

## 🗺️ Architecture Changes

### Old Structure (v1.5.x):
```
prompts/EMSTrainer_Core_Prompt.txt (9k+ chars, monolithic)
```

### New Structure (v1.6.0):
```
prompts/
├── EMSTrainer_Core.txt (16k)
│   ├── Foundation (provider levels, timing, grading)
│   ├── Test Mode (PlatinumPlanner integration)
│   └── Study Mode (targeted learning)
└── EMSTrainer_Scenario_Mode.txt (23k)
    ├── 4 Difficulty Modes
    ├── Scene Safety
    ├── Equipment Failures
    ├── Vitals Trending
    └── Debrief Generation
```

---

## 🚀 For Students

### How to Use:
1. Enable GPT-5 in Copilot/ChatGPT
2. Drag `EMSTrainer_Core.txt` into chat
3. For scenarios: Also drag `EMSTrainer_Scenario_Mode.txt`
4. Start learning!

### What You Can Do:
- **Upload test results** → Get targeted practice questions
- **Request study guides** → AI generates focused content
- **Run scenarios** → Choose Easy/Standard/Hard/Monica
- **Track progress** → See improvement over time

---

## 👨‍🏫 For Instructors

### How to Use:
1. Enable GPT-5 in Copilot/ChatGPT
2. Drag both prompt files into chat
3. Say: "Create a [type] scenario for [level] students"
4. Deploy, collect, auto-grade!

### What You Can Do:
- **Create scenarios** via natural language (no JSON editing)
- **Customize difficulty** and timing standards
- **Deploy to students** (email or file distribution)
- **Auto-grade submissions** with comprehensive analytics
- **Generate summaries** of class performance

---

## 🔮 Coming in v1.7

### Planned Features:
- **Equipment Setup Timing:** LUCAS device (30-45s), EtCO2 calibration (15s)
- **In-Prompt Scenario Editor:** Load, modify, save scenarios without JSON editing
- **Full Encryption:** AES-256 for scenarios and results
- **Instructor Test/Study Generator:** "Generate test on ALS airway"

### Under Consideration:
- Complete conversation transcripts (student ↔ patient ↔ partner)
- Voice of patient (dynamic dialogue generation)
- Integrated documentation prompts (SOAP at scenario end)
- Communication challenges (radio static, delays)

---

## 📊 Stats

- **Files Added:** 5 (2 prompts, 2 examples, 2 guides)
- **Files Modified:** 10+
- **Lines Added:** 1,300+
- **Character Budget:** Unlimited (drag-and-drop files)
- **Provider Levels:** 6 (EMR, EMT, AEMT, Paramedic, ACP, CCP)
- **Difficulty Modes:** 4 (Easy, Standard, Hard, Monica)
- **Example Scenarios:** 2 complete JSON files

---

## 🙏 Migration from v1.5.x

### Old Users (5 testers):
1. Delete old `EMSTrainer_Core_Prompt.txt` references
2. Download new `EMSTrainer_Core.txt` and `Scenario_Mode.txt`
3. Read Quick Start Guide for your role
4. No data migration needed (fresh start)

### Configuration Files:
- All `assets/*.json` files remain compatible
- `provider_levels.json` is new (optional, for local scope customization)

---

## 🐛 Known Issues

- Premature close errors when creating very large files in one operation (workaround: smaller chunks)
- Tool call limits (25) in Cursor Agent Mode (workaround: say "continue")

---

## 📝 Credits

- **Original Concept:** Test prep integration with PlatinumPlanner
- **Monica Mode:** Named after team member, designed for maximum difficulty
- **Development:** Solo developer with 5 beta testers
- **AI Assistant:** Claude 3.5 Sonnet (Cursor) for architecture and implementation

---

*Ready to train smarter, not harder?*

See [`Student_Quick_Start_Guide.md`](Student_Quick_Start_Guide.md) or [`Instructor_Quick_Start_Guide.md`](Instructor_Quick_Start_Guide.md) to get started!
