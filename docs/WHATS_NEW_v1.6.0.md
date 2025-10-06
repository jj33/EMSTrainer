# What's New in EMSTrainer v1.6.0

**Release Date:** 2025-01-06  
**Branch:** feat/strict-json-code-blackout

---

## Major Changes

### 🏗️ Modular Architecture

**Old (v1.5.x):** Single monolithic prompt file  
**New (v1.6.0):** Modular, focused prompt files

- **EMSTrainer_Core.txt (16k):** Foundation + Test/Study modes
- **EMSTrainer_Scenario_Mode.txt (23k):** Complex scenarios with vitals, Monica Mode

**Benefits:**
- Easier to maintain and update
- Students load only what they need
- No character limit concerns (drag-and-drop files)
- Clear separation of concerns

---

## New Features

### 🎓 Enhanced Difficulty System

Four explicit difficulty modes with clear behaviors:

**Easy Mode:**
- Learning-focused, supportive environment
- Timing tracked but NOT penalized
- Hints and scaffolding provided
- No equipment failures or complications
- Perfect for new students

**Standard Mode:**
- NREMT-level realistic practice
- Timing graded in debrief (affects score)
- Moderate support
- Industry-standard expectations
- Best for most training

**Hard Mode:**
- Strict timing with penalties
- Environmental stressors
- Equipment failures (20-25% probability)
- Minimal support
- Tests real-world readiness

**Monica Mode:**
- EXTREME difficulty ("pants on fire")
- ALL modules forced ON at max intensity
- Timer with HARD FAIL at timeout
- Curveballs guaranteed
- Designed to humble the overconfident

---

### 👨‍⚕️ Air Care Paramedic (ACP) Level

New provider level between Paramedic and CCP:

**Skills Added:**
- Cricothyrotomy
- RSI (Rapid Sequence Intubation)
- Blood products administration
- Flight physiology considerations

**Cannot (Standard):**
- Advanced ventilator management
- ECMO

Reflects real-world air medical provider scope.

---

### 🚨 Continuous Scene Safety Assessment

**Game Changer:** Scenarios can now START unsafe!

**Features:**
- Initial scene safety check required
- Scenes can deteriorate during care
- Students must recognize and respond
- Unsafe starts require staging for PD/Fire
- Hidden grading criteria (15 points)

**Example:**
"Body visible inside house, no PD on scene, suspicious circumstances..."
Correct: Stage and wait for PD
Incorrect: Enter scene = SCENARIO FAILED

---

### 🔧 Dynamic Equipment Failures

Realistic equipment issues based on difficulty:

**Failure Types:**
- **IV Access:** Vein blows, infiltration (first attempt fails)
- **Monitor:** Battery dies, lead malfunction
- **Oxygen:** Regulator fails, tank pressure low
- **Airway:** Suction fails, laryngoscope light dies

**Probability:**
- Easy: 0%
- Standard: 10-15%
- Hard: 20-25%
- Monica: 30-35%

Timing penalties applied, students must adapt.

---

### 🎯 Hidden Grading Criteria

Students graded on things they may not realize:

**5 Rights Medication Check (10 pts):**
- Right Patient
- Right Drug
- Right Dose
- Right Route
- Right Time

**AIDET Communication (10 pts):**
- Acknowledge patient
- Introduce self and role
- Duration (how long)
- Explanation (what you're doing)
- Thank you

**Scene Safety Reassessment (15 pts):**
- Continuous assessment throughout scenario
- Not just initial check

---

### 📊 Enhanced Debrief Format

**Structure:**
- Scenario summary with settings
- Timing analysis (target vs actual)
- Timestamped action log (includes partner interactions)
- Outcome summary
- Grading breakdown by category
- Hidden criteria scores revealed
- Difficulty-specific feedback
- NREMT prep tips

**Output:**
- Markdown source (.md)
- PDF for students
- Standardized filename: `[Date]_[ScenarioID]_Debrief_[StudentID].md`

---

### 📈 Vitals Trending by Difficulty

Dynamic patient response based on difficulty:

**Easy:** Slow decompensation, rapid improvement, very forgiving  
**Standard:** Realistic response to appropriate interventions  
**Hard:** Faster decline, requires correct interventions  
**Monica:** RAPID decompensation, minimal tolerance for errors

---

### 🤝 Partner Interactions in Timeline

Partner actions now tracked with timestamp:

```
| Time  | Actor   | Event                        | Notes              |
|-------|---------|------------------------------|-------------------|
| 13:20 | Student | "Start NRB, establish 2 IVs" | Closed-loop order |
| 13:15 | Partner | "NRB on, attempting left AC" | Confirms and acts |
| 13:10 | Partner | "Left AC blown, right hand"  | IV failure        |
| 13:05 | Partner | "Right 18g established"      | Success 2nd try   |
```

---

## Documentation Updates

### 📚 Quick Start Guides

**New Files:**
- `docs/Student_Quick_Start_Guide.md` - Comprehensive student onboarding
- `docs/Instructor_Quick_Start_Guide.md` - Instructor workflow guide

**Contents:**
- Prerequisites (GPT-5 requirement)
- Step-by-step setup
- Mode explanations
- Example commands
- Troubleshooting
- Tips for success

---

### 📋 Example Scenarios

**New Files:**
- `examples/scenario_cardiac_arrest_vf.json` - Standard ACLS
- `examples/scenario_mvc_trauma_monica.json` - Monica Mode with curveballs

Use as templates or modify for your needs.

---

## Technical Improvements

### 🔐 Local Provider Scope Customization

**Problem:** EMS scope varies by jurisdiction  
**Solution:** `assets/provider_levels.json` override file

**Example:**
Your EMT can do IV/IO but not advanced airways? Override:
```json
{
  "EMT": {
    "base": "EMT_national",
    "add_skills": ["iv_access", "io_access", "12_lead_acquisition"],
    "remove_skills": []
  }
}
```

---

### 📏 Character Limits Eliminated

**Old Problem:** 8000 character limit for copy/paste  
**New Solution:** Drag-and-drop files into Copilot/ChatGPT

No more chunking or splitting!

---

### 🗂️ Repository Cleanup

**Removed:**
- Old monolithic prompt file
- GitHub workflow validations (will add back later if needed)

**Organized:**
- Clear folder structure
- Example scenarios
- Comprehensive documentation

---

## Breaking Changes

### ⚠️ File Name Changes

**OLD (v1.5.x):**
- `prompts/EMSTrainer_Core_Prompt.txt`

**NEW (v1.6.0):**
- `prompts/EMSTrainer_Core.txt`
- `prompts/EMSTrainer_Scenario_Mode.txt`

**Migration:** Use new files, old file deleted.

---

### ⚠️ GPT-5 Now Required

**Previously:** Any model worked  
**Now:** GPT-5 required for medical accuracy

Must be manually enabled in Copilot/ChatGPT settings.

---

## Coming Soon (v1.7 Planned)

- **Scenario Encryption:** Prevent student tampering/preview
- **Equipment Timing Delays:** LUCAS setup, EtCO2 calibration
- **In-Prompt Scenario Editor:** Modify scenarios without editing JSON
- **Instructor Test/Study Generation:** Create custom tests on specific topics

---

## Upgrade Instructions

### For Students:

1. Delete old bookmarks/references to `EMSTrainer_Core_Prompt.txt`
2. Enable GPT-5 in settings
3. Load `EMSTrainer_Core.txt` (Test/Study)
4. Optional: Load `EMSTrainer_Scenario_Mode.txt` (Scenarios)
5. Review `docs/Student_Quick_Start_Guide.md`

### For Instructors:

1. Enable GPT-5 in settings
2. Load `EMSTrainer_Core.txt`
3. Optional: Load `EMSTrainer_Scenario_Mode.txt`
4. Review example scenarios in `examples/`
5. Review `docs/Instructor_Quick_Start_Guide.md`

---

## Contributors

- Architecture redesign
- Modular prompt system
- Scene safety features
- Equipment failures
- Hidden grading criteria
- ACP provider level
- Documentation overhaul

---

**Questions?** Review planning docs or contact your instructor.

---

*EMSTrainer v1.6.0 - Released 2025-01-06*
