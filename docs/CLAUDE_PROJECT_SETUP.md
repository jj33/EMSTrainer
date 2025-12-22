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

**RECOMMENDED METHOD: GitHub Connector**

This keeps your project automatically synced with your git repository.

1. Click "Add content" → "Connect GitHub"
2. Select repository: `jj33/EMSTrainer`
3. Select branch: `dev` (or `main` when you're ready for stable)
4. Add the files you need (see below for which files)

**Benefits:**
- ✅ Automatically pulls latest version when you push to git
- ✅ Works from any device (not tied to local files)
- ✅ Always in sync with your dev branch
- ✅ No manual file management

**ALTERNATIVE: Local File Paths**

If you prefer local references (requires local git repo):

Add files by absolute path: `~/EMSTrainer/prompts/[filename]`

---

#### For Student Use:

**Required Files (in this order):**
1. `prompts/EMSTrainer_Core.txt`
2. `prompts/EMSTrainer_Student_Interface.txt`

**Optional (if using specific features):**
3. `assets/partner_pool.json` (if custom partners)
4. `assets/scenarios/*.json` (specific scenarios)

**NOTE:** National Model EMS Clinical Guidelines PDF is NOT in git repository. Upload manually to projects that need it.

#### For Instructor Use:

**Required Files:**
1. `prompts/EMSTrainer_Core.txt`
2. `prompts/EMSTrainer_Instructor_Interface.txt`

**Optional:**
3. `assets/scenarios/*.json` (for editing/grading)
4. Documentation files as needed

---

## How Claude Project Knowledge Works

**When you add files via GitHub Connector:**
- Claude connects to your GitHub repository
- Files are synced automatically when you push to git
- Claude reads the latest version from your selected branch
- No manual updates needed - always current

**When you add files by local path:**
- Claude reads files directly from your filesystem
- Files are re-read when updated (auto-refresh)
- Requires local git repository on your machine
- Updates when you commit/pull locally

**Path Reference Pattern (if using local paths):**
```
~/EMSTrainer/prompts/[filename]
```

**GitHub Reference Pattern (recommended):**
```
Repository: jj33/EMSTrainer
Branch: dev
File: prompts/EMSTrainer_Core.txt
```

**This means:**
- Git commits update the files
- Project automatically sees changes (GitHub connector)
- OR Project sees changes on next read (local paths)
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
- Apply current Core features: time tracking, immersion, adaptation
- Create physiological stress in Monica Mode
- Educational debriefs after scenarios
- Generate submission files for grading

Remember: You're training future paramedics. Make it real, make it challenging, make it memorable.
```

**Note:** These instructions are version-agnostic. Version info comes from the Core.txt file itself, which updates automatically when you push to git.

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
   cd ~/EMSTrainer
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
cd ~/EMSTrainer

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

### GitHub Connector (Recommended):
```
Repository: jj33/EMSTrainer
Branch: dev (or main for stable)
Files to add:
- prompts/EMSTrainer_Core.txt
- prompts/EMSTrainer_Student_Interface.txt
- prompts/EMSTrainer_Instructor_Interface.txt
- assets/scenarios/[scenario_name].json
- assets/partner_pool.json
```

### Local File Paths (Alternative):
```
Core:               ~/EMSTrainer/prompts/EMSTrainer_Core.txt
Student Interface:  ~/EMSTrainer/prompts/EMSTrainer_Student_Interface.txt
Instructor:         ~/EMSTrainer/prompts/EMSTrainer_Instructor_Interface.txt
Scenarios:          ~/EMSTrainer/assets/scenarios/
Partner Pool:       ~/EMSTrainer/assets/partner_pool.json
```

### Manual Upload (Not in Git):
```
National Model EMS Clinical Guidelines PDF - Upload manually to each project
```

### Current Versions:
Check the header in Core.txt for current version number.
GitHub connector ensures you always have the latest from your selected branch.

---

## Why This Is Better Than Copying

**Old way (copying files):**
1. Edit file in git
2. Copy to Claude Project
3. Remember to update project when file changes
4. Multiple versions get out of sync
5. Confusion about which is current

**New way (GitHub connector - RECOMMENDED):**
1. Edit file in git
2. Commit and push changes
3. Project automatically syncs latest version
4. Single source of truth (git repository)
5. Always current, no confusion
6. Works from any device

**Alternative (local file paths):**
1. Edit file in git
2. Commit changes locally
3. Project uses updated file automatically
4. Requires local git repo on device

**Perfect for active development!** ✅

---

## Support Resources

**Documentation:**
- `~/EMSTrainer/docs/` - Full documentation
- `~/EMSTrainer/planning/` - Feature roadmap
- `~/EMSTrainer/internal/` - Development notes (local only)

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
