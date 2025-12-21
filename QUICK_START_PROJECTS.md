# EMSTrainer Project Setup - Quick Start

**TL;DR:** Add these files to your Claude Project Knowledge, never copy/paste again.

---

## Student Practice Project

**Create new project named:** "EMSTrainer - Student"

**Add these files as Project Knowledge:**
1. `***REMOVED***/prompts/EMSTrainer_Core.txt`
2. `***REMOVED***/prompts/EMSTrainer_Student_Interface.txt`

**Custom Instructions:**
```
You are EMSTrainer v1.6.3 for paramedic training.
Follow Core and Student Interface rules exactly.
Use Monica Mode partner "Pat" (not Cody).
Apply time tracking and immersive adaptation.
Create physiological stress in Monica Mode.
```

**Start a scenario:**
```
"Load Code Blackout scenario in Monica Mode"
```

---

## Pattern Recognition Project

**Create new project named:** "EMSTrainer - Pattern Recognition"

**Add these files:**
1. Core.txt
2. Student_Interface.txt
3. `***REMOVED***/docs/National-Model-EMS-Clinical-Guidelines_2022.pdf` (optional)

**Custom Instructions:**
```
Focus on Pattern Recognition Mode exclusively.
Present 2-4 findings, student gives differential.
Guide assessment iteratively.
Target weak areas: Respiratory (50%), Airway (65%), Head/Spine (50%)
```

**Start drill:**
```
"Pattern Recognition Mode: Respiratory emergencies.
Focus on differentiating CHF, COPD, pneumonia, PE."
```

---

## Study Group Scenario Creation

**Create new project named:** "EMSTrainer - Study Group"

**Add these files:**
1. Core.txt
2. `***REMOVED***/prompts/EMSTrainer_Instructor_Interface.txt`
3. `***REMOVED***/assets/partner_pool.json` (optional)

**Custom Instructions:**
```
Generate Easy/Standard scenarios for study group.
Include classmate partners from pool.
Create scenarios targeting common weak areas.
```

**Generate scenario:**
```
"Create Standard difficulty cardiac arrest scenario.
Focus: Symptomatic bradycardia and pacing decision.
Partner: Dylan (from pool)"
```

---

## Why This Works

**Git as single source of truth:**
- Edit files in `***REMOVED***/`
- Commit changes
- Project automatically uses updated files
- No copying, no version drift

**When you update EMSTrainer:**
```bash
cd ***REMOVED***
# Make changes
git add .
git commit -m "updates"
git push origin dev
# Project now uses new version automatically
```

---

## File Paths Reference

**Core files:**
```
Core:              ***REMOVED***/prompts/EMSTrainer_Core.txt
Student:           ***REMOVED***/prompts/EMSTrainer_Student_Interface.txt
Instructor:        ***REMOVED***/prompts/EMSTrainer_Instructor_Interface.txt
```

**Assets:**
```
Scenarios:         ***REMOVED***/assets/scenarios/
Partner Pool:      ***REMOVED***/assets/partner_pool.json
Guidelines:        ***REMOVED***/docs/National-Model-EMS-Clinical-Guidelines_2022.pdf
```

---

## Current Versions (2025-12-20)

- **Core:** v1.6.3 (time tracking, death pathways, immersive adaptation)
- **Student Interface:** v1.6.3 (refined hints, Monica enhancements)
- **Instructor Interface:** v1.6.2 (scenario creation, grading)
- **Code Blackout:** v1.1 (full v1.6.3 compliance)

---

## Full Documentation

See: `***REMOVED***/docs/CLAUDE_PROJECT_SETUP.md` for complete guide.

---

**Created:** 2025-12-20  
**Status:** Ready to use ✅
