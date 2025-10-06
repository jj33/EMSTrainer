# Development Session Notes - 2025-01-06

**Session Duration:** ~6 hours  
**Developer:** Joel (EMT with AEMT skills)  
**AI Assistant:** Claude 3.5 Sonnet v4.5 (Cursor)  
**Branch:** feat/strict-json-code-blackout  
**Goal:** Modular architecture refactor + v1.6.0 feature implementation

---

## Context for Next Session

### Project Overview
EMSTrainer is an AI-powered EMS training system with three modes:
- Test Mode: Generate practice questions from weak areas
- Study Mode: AI study guides
- Scenario Mode: Realistic patient scenarios with dynamic vitals

**Target Users:** EMS students, instructors, training officers  
**Platform:** GPT-5 (Copilot/ChatGPT) - medical accuracy required

---

## What We Accomplished Today

### Major Refactor: Monolithic → Modular
- Split `EMSTrainer_Core_Prompt.txt` (9k, over limit) into:
  - `EMSTrainer_Core.txt` (16k): Foundation + Test/Study
  - `EMSTrainer_Scenario_Mode.txt` (23k): Scenarios
- Eliminated 8000 char copy/paste limit (drag-and-drop files)

### New Features Implemented
1. **4 Difficulty Modes** with explicit behaviors
2. **ACP (Air Care Paramedic)** provider level
3. **Continuous Scene Safety** (can start unsafe)
4. **Dynamic Equipment Failures** (IV, monitor, O2, airway)
5. **Hidden Grading** (5 Rights, AIDET, scene safety)
6. **Enhanced Debriefs** (timing analysis, partner timeline)
7. **Vitals Trending** by difficulty
8. **Partner Interaction** tracking

### Documentation Created
- Student Quick Start Guide
- Instructor Quick Start Guide
- What's New in v1.6.0
- Example scenarios (cardiac arrest, MVC trauma Monica)
- Provider levels schema + example
- CHANGELOG v1.6.0
- Updated README

---

## Key Decisions Made

### Character Limits
- **Discovery:** Copilot/ChatGPT drag-and-drop bypasses 8k input limit
- **Decision:** Don't worry about char counts, optimize for usability
- **Result:** Files can be 15-25k characters

### GPT-5 Requirement
- **Why:** Medical accuracy, protocol knowledge, clinical reasoning
- **Enforcement:** Warnings in all docs, README, quick starts
- **Alternative:** Claude 3.5 Sonnet only for development (no medical content)

### Provider Scope Customization
- **Problem:** EMS scope varies by jurisdiction
- **Solution:** `assets/provider_levels.json` override file
- **Example:** Joel's EMT can do IV/IO, 12-lead (like AEMT minus airways)

### Monica Mode Philosophy
- **Purpose:** "Pants on fire" mode for the overconfident ("paragods")
- **Design:** Everything on max, no mercy, immediate consequences
- **Tone:** Brutal but fair, objective debrief
- **NOT for learners:** Explicit warnings added

---

## Technical Details

### Cursor Agent Mode Limits
- **Issue:** Premature close errors when creating large files
- **Cause:** 25 tool call limit per request
- **Workaround:** Small chunks, use terminal commands for large files
- **Token Budget:** 200k per session (used 146k, 53k remaining)

### File Structure
```
prompts/
├── EMSTrainer_Core.txt (16k)
└── EMSTrainer_Scenario_Mode.txt (23k)

docs/
├── Student_Quick_Start_Guide.md
├── Instructor_Quick_Start_Guide.md
└── WHATS_NEW_v1.6.0.md

examples/
├── scenario_cardiac_arrest_vf.json
└── scenario_mvc_trauma_monica.json

assets/
├── provider_levels.json (example)
└── schema/provider_levels.schema.json
```

### Git Status
- Branch: feat/strict-json-code-blackout
- Commits today: 8
- All pushed to GitHub
- Ready for PR or merge to dev

---

## Design Patterns Established

### Difficulty Scaling
- **Easy:** Educational, no penalties, hints
- **Standard:** Realistic, graded timing, balanced
- **Hard:** Strict, consequences, minimal support
- **Monica:** Extreme, everything max, hard fail

### Equipment Failures
- Probability scales: 0% (Easy) → 35% (Monica)
- Types: IV, monitor, O2, airway
- Timing penalties applied
- Students must adapt (backup equipment, alternate routes)

### Scene Safety
- NOT one-time check - continuous assessment
- Can start unsafe (staging required)
- Can deteriorate during care
- Hidden grading (15 points)
- Failure = scenario fail in extreme cases

### Debrief Format
- Markdown source (.md)
- PDF for students
- Filename: `[Date]_[ScenarioID]_Debrief_[StudentID].md`
- Sections: Summary, Timing, Timeline, Outcome, Grading, Feedback

---

## Planning Docs Updated

### Feature Document
- Added v1.6 features with status
- Reorganized instructor features
- Added encryption (v1.7), web dashboard (v1.8)

### Future Ideas
- Added equipment timing delays (LUCAS, EtCO2)
- Added in-prompt scenario editor (v1.7)
- Added instructor test/study generation
- Updated status tracking

---

## Unfinished / Next Steps

### Immediate (v1.6 Completion)
- [ ] Test Core.txt in actual GPT-5 (validate medical accuracy)
- [ ] Test Scenario_Mode.txt with students
- [ ] Collect feedback from beta testers (5 active)
- [ ] Merge to dev branch (currently on feature branch)

### v1.7 Planning
- [ ] Equipment timing delays (LUCAS 30-45s, EtCO2 15s calibration)
- [ ] Scenario encryption (AES-256, digital signatures)
- [ ] In-prompt scenario editor (load JSON, modify, save)
- [ ] Instructor test/study generator ("test on ALS airway")

### Known Issues
- Cursor Agent Mode: 25 tool call limit (workaround: small chunks)
- No real-time clock access (must ask user for time)
- Large file creation can trigger premature close errors

---

## User Context (Joel)

### Role & Experience
- EMT with AEMT-level skills (IV/IO, 12-lead, limited meds)
- No advanced airways in local scope
- Paramedics in area: can run vents, some CC meds, but not crich/ECMO
- Solo novice developer (decades-old programming experience, VB Studio)
- Star Trek fan 🖖

### Development Environment
- Cursor IDE (Claude 3.5 Sonnet 4.5)
- 4K TV at 10 feet (font size issues)
- MacOS (M-series)
- Git repo: EMSTrainer (jj33/EMSTrainer on GitHub)
- 5 beta testers using current version

### Working Style
- Agent Mode preferred (handles git, commits, pushes)
- Dislikes copy/paste (too time-consuming)
- Values simplicity for end users (EMS not IT-savvy)
- Works in focused bursts (6pm shift work schedule)
- Pragmatic: "If nobody's using it, just delete it"

### Preferences
- Keep prompts user-friendly (chat-based, no coding)
- Character limits were concern (now resolved)
- Documentation important (Quick Start guides appreciated)
- Planning docs tracked (feature status, roadmap)
- Git workflow: feature branch → commit → push → PR

---

## Important Files Reference

### Load Order for AI
1. This file (session context)
2. `prompts/EMSTrainer_Core.txt` (understand foundation)
3. `prompts/EMSTrainer_Scenario_Mode.txt` (understand features)
4. `planning/EMSTrainer_Feature_Document.md` (status)
5. `planning/EMS_Trainer_Future_Ideas_with_Status.md` (roadmap)

### Examples
- `examples/scenario_cardiac_arrest_vf.json` - Standard scenario structure
- `examples/scenario_mvc_trauma_monica.json` - Monica Mode with curveballs
- `assets/provider_levels.json` - Scope customization example

---

## Terminology / Jargon

**Monica Mode:** Extreme difficulty, named for challenging instructor/concept  
**Paragods:** Overconfident paramedics who think they know everything  
**AIDET:** Communication framework (Acknowledge, Introduce, Duration, Explanation, Thank you)  
**5 Rights:** Medication safety (Patient, Drug, Dose, Route, Time)  
**Scene safety:** Ongoing assessment, not one-time check  
**Curveball:** Unexpected complication during scenario  
**Load-and-go:** Rapid transport decision (trauma)  
**ROSC:** Return of spontaneous circulation (cardiac arrest)  
**VF/VT:** Ventricular fibrillation/tachycardia (shockable rhythms)  
**EtCO2:** End-tidal CO2 monitoring (capnography)  
**LUCAS:** Mechanical CPR device  
**PlatinumPlanner:** Test results system (identifies weak areas)

---

## Code Standards / Patterns

### JSON Scenarios
- Include scenario_hash for integrity
- Timing standards reference industry benchmarks
- Expected interventions with time windows
- Grading rubric totals 100 points
- Hidden grading separate from visible

### Markdown Documents
- Clear headers with emoji for visual scanning
- Code blocks for examples
- Tables for comparisons
- Warnings with ⚠️ symbol
- Links to related documents

### Commit Messages
- Descriptive summary line (<80 chars)
- Bullet points for details
- Reference file counts when large changes
- Note breaking changes

---

## Questions to Ask Tomorrow

1. How did beta testing go?
2. Any feedback on GPT-5 medical accuracy?
3. Issues with new prompt file structure?
4. Ready to merge to dev?
5. Priority for v1.7 features?
6. Any bugs or user confusion?

---

## Mental Model Established

**Architecture:** Modular prompts (Core + Scenario Mode)  
**Philosophy:** Teaching first, challenge second (except Monica)  
**Users:** Non-technical EMS professionals  
**Platform:** GPT-5 drag-and-drop interface  
**Workflow:** Create → Deploy → Grade → Summarize  
**Quality:** Medical accuracy paramount (hence GPT-5)

---

*Session ended ~5:00pm Central, 2025-01-06*  
*Next session: TBD*  
*Files committed, pushed, documented*  
*Ready for testing and feedback*

---

## IMPORTANT NOTE ADDED 5:15pm:

**Debrief Feedback Scope:**
- Subjective suggestions in debriefs need to be CLINICAL, not medical
- We are NOT medical directors
- Avoid appearing to give medical advice
- Focus on: protocols, procedures, skills, decision-making
- Avoid: diagnosis, treatment recommendations beyond protocol
- Liability consideration for v1.7

Example:
- ❌ "Patient likely had MI, should have given aspirin"
- ✅ "Per protocol, aspirin indicated for chest pain with cardiac presentation"


**REVISED APPROACH - Better Solution:**

Add a separate "Discussion Points for Your Instructor/Medical Director" section:
- NOT presented as advice or recommendations
- Phrased as questions or discussion topics
- Encourages seeking proper medical direction
- Maintains educational value while avoiding liability

Example Debrief Structure:
```
## Clinical Performance
[Objective assessment of protocol adherence]

## Skills & Procedures
[Technical performance feedback]

## Discussion Points for Your Instructor/Medical Director
- Why might aspirin be indicated in this presentation?
- What are the differential diagnoses for these symptoms?
- When should medical control be consulted for this chief complaint?
- How do local protocols differ from national standards here?

Note: These are learning questions, not medical recommendations. 
Always consult your instructor or medical director for clinical guidance.
```

This approach:
✅ Maintains educational value
✅ Avoids giving medical advice
✅ Encourages proper chain of command
✅ Reduces liability
✅ Promotes critical thinking
