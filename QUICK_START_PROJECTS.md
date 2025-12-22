# EMSTrainer Project Setup - Quick Start

**TL;DR:** Add these files to your Claude Project Knowledge, never copy/paste again.

---

## Student Practice Project

**Create new project named:** "EMSTrainer - Student"

**Add files via GitHub Connector (RECOMMENDED):**
1. Click "Add content" → "Connect GitHub"
2. Select repository: `jj33/EMSTrainer`
3. Select branch: `dev`
4. Add files:
   - `prompts/EMSTrainer_Core.txt`
   - `prompts/EMSTrainer_Student_Interface.txt`

**OR add files by local path:**
1. `~/EMSTrainer/prompts/EMSTrainer_Core.txt`
2. `~/EMSTrainer/prompts/EMSTrainer_Student_Interface.txt`

**Why GitHub connector?** Automatically pulls latest version when you push to git. Works from any device.

**Custom Instructions:**
```
You are EMSTrainer, an AI-powered paramedic training system.
Follow EMSTrainer_Core.txt and EMSTrainer_Student_Interface.txt from Project Knowledge.
Use Partner "Pat" in Monica Mode.
Apply current Core features: time tracking, immersion, death pathways.
Make it real, make it challenging, make it memorable.
```

**Note:** Version info comes from Core.txt itself - these instructions never need updating.

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
3. `~/EMSTrainer/docs/National-Model-EMS-Clinical-Guidelines_2022.pdf` (optional)

**Custom Instructions:**
```
You are EMSTrainer for Pattern Recognition training.
Focus on Pattern Recognition Mode exclusively.
Present 2-4 findings, student gives differential.
Guide assessment iteratively.
Target weak areas based on student performance.
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
2. `~/EMSTrainer/prompts/EMSTrainer_Instructor_Interface.txt`
3. `~/EMSTrainer/assets/partner_pool.json` (optional)

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
- Edit files in `~/EMSTrainer/`
- Commit changes
- Project automatically uses updated files
- No copying, no version drift

**When you update EMSTrainer:**
```bash
cd ~/EMSTrainer
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
Core:              ~/EMSTrainer/prompts/EMSTrainer_Core.txt
Student:           ~/EMSTrainer/prompts/EMSTrainer_Student_Interface.txt
Instructor:        ~/EMSTrainer/prompts/EMSTrainer_Instructor_Interface.txt
```

**Assets:**
```
Scenarios:         ~/EMSTrainer/assets/scenarios/
Partner Pool:      ~/EMSTrainer/assets/partner_pool.json
Guidelines:        ~/EMSTrainer/docs/National-Model-EMS-Clinical-Guidelines_2022.pdf
```

---

## Current Versions

Version info is in the files themselves (see header in Core.txt).
GitHub connector ensures you always have the latest version from your dev branch.

**As of 2025-12-20:**
- Core: v1.6.3
- Student Interface: v1.6.3
- Instructor Interface: v1.6.2
- Code Blackout: v1.1

---

## Full Documentation

See: `~/EMSTrainer/docs/CLAUDE_PROJECT_SETUP.md` for complete guide.

---

**Created:** 2025-12-20  
**Status:** Ready to use ✅
