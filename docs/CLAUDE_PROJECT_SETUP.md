# EMSTrainer Claude Project Setup - Direct Git Reference

**Purpose:** Create a Claude Project that references EMSTrainer prompt files directly from your local git repository, ensuring you always use the current developed version without copying files.

**Date Created:** 2025-12-20  
**Current Versions:** Core v1.6.3, Student Interface v1.6.3, Instructor v1.6.2

---

## Why This Approach?

**Problems with copying files:**
- Version drift (project copy gets out of date)
- Duplicate maintenance (changes need copying)
- Confusion about which version is current
- No single source of truth

**Benefits of git reference:**
- Always using latest developed version
- Single source of truth (git repo)
- Changes propagate immediately to project
- No file duplication or drift

---

## Setup Instructions

### Step 1: Create New Claude Project

1. Open Claude.ai
2. Click "Projects" in sidebar
3. Click "Create Project"
4. Name: **"EMSTrainer - Student"** (or "EMSTrainer - Instructor" depending on use)
5. Description: "Paramedic training scenarios using EMSTrainer system from local git repo"

### Step 2: Add Project Knowledge Files

**IMPORTANT:** Add files as **references** to git repo, not copies.

#### For Student Use:

**Required Files (in this order):**
1. `***REMOVED***/prompts/EMSTrainer_Core.txt`
2. `***REMOVED***/prompts/EMSTrainer_Student_Interface.txt`

**Optional (if using specific features):**
3. `***REMOVED***/assets/partner_pool.json` (if custom partners)
4. `***REMOVED***/assets/scenarios/*.json` (specific scenarios)
5. `***REMOVED***/docs/National-Model-EMS-Clinical-Guidelines_2022.pdf` (if using guidelines)

#### For Instructor Use:

**Required Files:**
1. `***REMOVED***/prompts/EMSTrainer_Core.txt`
2. `***REMOVED***/prompts/EMSTrainer_Instructor_Interface.txt`

**Optional:**
3. `***REMOVED***/assets/scenarios/*.json` (for editing/grading)
4. Documentation files as needed

---

## How Claude Project Knowledge Works

**When you add files to Project Knowledge:**
- Claude indexes the content
- Files are re-read when updated (auto-refresh)
- Claude can search and reference the content
- Multiple files create combined knowledge base

**Path Reference Pattern:**
```
***REMOVED***/prompts/[filename]
```

**This means:**
- Git commits update the files
- Project automatically sees changes
- No manual copying needed
- Always in sync with development

---

## Custom Instructions for Project

Add this to your project's **Custom Instructions** field:

```
You are EMSTrainer, an AI-powered paramedic training system.

CORE BEHAVIOR:
- Follow EMSTrainer_Core.txt rules exactly
- Use EMSTrainer_Student_Interface.txt for student interactions
- Reference National Model EMS Guidelines when available
- Maintain difficulty modes: Easy, Standard, Hard, Monica
- Track time realistically (no arbitrary timestamps)
- Use immersive adaptation for Hard/Monica modes
- Apply death pathways appropriately in Monica Mode

PARTNER SYSTEM:
- Monica Mode: Partner is "Pat" (generic new EMT, unhelpful)
- Other modes: Use partner pool or scenario-specified partners
- Never use real student names for incompetent partners

SCENARIO EXECUTION:
- Load scenario JSON when provided
- Apply v1.6.3 features: time tracking, immersion, adaptation
- Create physiological stress in Monica Mode
- Educational debriefs after scenarios
- Generate submission files for grading

VERSION INFO:
- Core: v1.6.3 (2025-12-20)
- Student Interface: v1.6.3
- Features: Pattern Recognition, Weak Area Tracking, Immersive Scenarios

Remember: You're training future paramedics. Make it real, make it challenging, make it memorable.
```

---

## Usage Workflow

### Starting a Scenario

**Option 1: From Scenario File**
```
[Upload or drag scenario JSON file]

"Load this scenario in Monica Mode"
```

**Option 2: Generate Scenario**
```
"Generate a cardiac arrest scenario, Monica difficulty, 
focusing on symptomatic bradycardia and pacing"
```

**Option 3: Pattern Recognition Mode**
```
"Start Pattern Recognition Mode for respiratory emergencies.
I need to work on differentiating CHF, COPD, and pneumonia."
```

### After Scenario

Claude will:
1. Provide debrief (performance, timing, decisions)
2. Generate submission file (JSON)
3. Offer to run similar scenario or address weak areas

---

## File Update Workflow

**When you update EMSTrainer in git:**

1. Make changes in git repo:
   ```bash
   cd ***REMOVED***
   # Edit files
   git add .
   git commit -m "description"
   git push origin dev
   ```

2. Project automatically uses updated files
   - No manual refresh needed
   - Next conversation uses new version
   - Changes propagate immediately

**Version tracking:**
- Check `EMSTrainer_Core.txt` header for current version
- Changelog shows recent updates
- Projects always reference latest committed version

---

## Multiple Project Setup

You can create multiple projects for different uses:

### Project 1: "EMSTrainer - Student Practice"
**Purpose:** Personal scenario training
**Files:**
- Core v1.6.3
- Student Interface v1.6.3
- Your weak area test results
- Saved scenarios you want to retry

### Project 2: "EMSTrainer - Pattern Recognition"
**Purpose:** Focused differential diagnosis drills
**Files:**
- Core v1.6.3
- Student Interface v1.6.3
- National Model Guidelines
**Custom Instructions:** "Focus on Pattern Recognition Mode exclusively"

### Project 3: "EMSTrainer - Study Group"
**Purpose:** Creating scenarios for classmates
**Files:**
- Core v1.6.3
- Instructor Interface v1.6.2
- Partner pool (classmate names)
**Custom Instructions:** "Generate Easy/Standard scenarios for study group"

### Project 4: "EMSTrainer - Instructor" (If you become instructor)
**Purpose:** Full instructor capabilities
**Files:**
- Core v1.6.3
- Instructor Interface v1.6.2
- All scenario templates
- Grading rubrics

---

## Troubleshooting

### "Claude doesn't seem to be following the rules"
**Fix:** Start new chat session (don't chain multiple scenarios)
- One scenario = one fresh chat
- Reduces hallucinations
- Maintains prompt fidelity

### "Time tracking seems off"
**Check:** Core version in project
- Should be v1.6.3 or later
- Time tracking added in v1.6.3
- Older versions used arbitrary times

### "Partner named Cody instead of Pat"
**Fix:** Scenario file outdated
- Update scenario to v1.1+
- Or manually specify: "Partner should be Pat"

### "Death pathways not triggering"
**Check:** 
- Monica Mode enabled?
- Core v1.6.3 loaded?
- Scenario has death pathway triggers?

### "Files not updating in project"
**Fix:**
- Verify git commit/push completed
- Start new chat (refresh)
- Re-add file to project knowledge if needed

---

## Advanced: Development Workflow

**For active EMSTrainer development:**

### Working Branch Pattern:
```bash
cd ***REMOVED***

# Create feature branch
git checkout -b feature/new-cardiac-scenarios
# Make changes
git add .
git commit -m "Added STEMI scenarios"

# Test in Claude Project
# [Project automatically uses new branch]

# If good, merge to dev
git checkout dev
git merge feature/new-cardiac-scenarios
git push origin dev

# Project now uses merged version
```

### Testing New Features:
1. Create test scenario in `assets/scenarios/test_*.json`
2. Add to project knowledge temporarily
3. Run scenario, verify behavior
4. If good, commit. If not, iterate.
5. Remove test file when done (or keep for regression testing)

---

## Version Compatibility

**Core versions:**
- v1.6.3+ required for: Time tracking, death pathways, immersive adaptation
- v1.6.2 required for: Pattern Recognition, Weak Area Tracking
- v1.6.0+ required for: Instructor features, scenario creation
- v1.5.6+ required for: Monica Mode

**Scenario versions:**
- v1.1+ scenarios: Full v1.6.3 compliance (time tracking, immersion, deaths)
- v1.0 scenarios: Basic functionality, missing v1.6.3 features

**Upgrading scenarios:**
See: `assets/scenarios/CODE_BLACKOUT_v1.1_UPDATE_SUMMARY.md` for example

---

## Quick Reference

### Essential File Paths:
```
Core:               ***REMOVED***/prompts/EMSTrainer_Core.txt
Student Interface:  ***REMOVED***/prompts/EMSTrainer_Student_Interface.txt
Instructor:         ***REMOVED***/prompts/EMSTrainer_Instructor_Interface.txt
Scenarios:          ***REMOVED***/assets/scenarios/
Guidelines:         ***REMOVED***/docs/National-Model-EMS-Clinical-Guidelines_2022.pdf
Partner Pool:       ***REMOVED***/assets/partner_pool.json
```

### Current Versions (2025-12-20):
```
Core: v1.6.3 - Immersive scenarios, death pathways, time tracking
Student Interface: v1.6.3 - Refined hint policy, Monica Mode enhancements
Instructor Interface: v1.6.2 - Scenario creation, grading
Code Blackout: v1.1 - Full v1.6.3 compliance
```

---

## Why This Is Better Than Copying

**Old way (copying files):**
1. Edit file in git
2. Copy to Claude Project
3. Remember to update project when file changes
4. Multiple versions get out of sync
5. Confusion about which is current

**New way (git reference):**
1. Edit file in git
2. Commit changes
3. Project uses updated file automatically
4. Single source of truth
5. Always current, no confusion

**Perfect for active development!** ✅

---

## Support Resources

**Documentation:**
- `***REMOVED***/docs/` - Full documentation
- `***REMOVED***/planning/` - Feature roadmap
- `***REMOVED***/internal/` - Development notes (local only)

**Git Repository:**
- Branch: `dev` (active development)
- Branch: `main` (stable releases - when you're ready)
- Commit history shows all changes

**For Questions:**
- Check `planning/EMS_Trainer_Future_Ideas_with_Status.md`
- Check `internal/ACTIVE_TASKS.md` for priorities
- Reference this setup guide

---

## Created: 2025-12-20
## Author: EMSTrainer Development Team (Joel)
## Purpose: Single source of truth for project setup
## Status: Ready to use ✅
