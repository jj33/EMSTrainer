# EMSTrainer Architecture Audit - Core vs. Student vs. Instructor

## Current Core Structure (Line-by-Line Audit)

### ✅ BELONGS IN CORE (Both need these)

**Lines 17-36: VERSION INFORMATION**
- ✅ Core version, date, architecture
- ✅ CHANGELOG
- ❌ **DUPLICATE CHANGELOG** (appears twice - lines 24-29 and 31-36)
- **ACTION:** Remove duplicate

**Lines 38-52: LOADING INSTRUCTIONS**
- ✅ Proper - both students and instructors need loading order
- ✅ Stay in Core

**Lines 54-62: CORE READY RESPONSE**
- ✅ Proper - standardizes initialization
- ✅ Stay in Core

**Lines 64-76: MODEL REQUIREMENTS**
- ✅ Proper - both need to know model requirements
- ⚠️ **COPILOT-SPECIFIC:** "Must be manually enabled in settings"
- **ACTION:** Make AI-agnostic

**Lines 78-103: NATIONAL MODEL GUIDELINES INTEGRATION**
- ✅ Proper - both Student and Instructor need guideline integration
- ❌ **DUPLICATED at lines 166-192** (exact same content)
- **ACTION:** Keep once, remove duplicate

**Lines 105-150: WEAK AREA TRACKING SYSTEM**
- ✅ Proper - both need to understand tracking
- ❌ **DUPLICATED at lines 193-236** (exact same content)
- **ACTION:** Keep once, remove duplicate

**Lines 152-164: EDUCATIONAL DISCLAIMER**
- ✅ Proper - both need to show this
- ✅ Stay in Core

**Lines 238-266: PROVIDER LEVELS & SCOPE**
- ✅ Proper - both need to enforce scope
- ✅ Stay in Core (fundamental rules)

**Lines 268-280: SCOPE LOADING PRIORITY**
- ✅ Proper - both need config loading rules
- ✅ Stay in Core

**Lines 282-299: PARTNER LOGIC (Shared Rules)**
- ✅ Proper - both need partner behavior rules
- ✅ Stay in Core

**Lines 301-332: PARTNER POOL (Pre-assigned by Certification)**
- ✅ Proper - shared resource both need
- 🤔 **CONSIDERATION:** Could move to assets/partner_pool.json with Core fallback
- **DECISION:** Keep in Core for now (universal defaults), allow override via assets

**Lines 334-343: TIMING STANDARDS**
- ✅ Proper - both need timing enforcement
- ⚠️ References external file: assets/EMSTrainer_Default_Timing_Profiles.json
- **ACTION:** Add inline fallback defaults if file missing

**Lines 345-354: GRADING RUBRIC (100 pts)**
- ✅ Proper - both need rubric (Student to understand, Instructor to apply)
- ✅ Stay in Core

**Lines 356-375: HASH VALIDATION & INTEGRITY**
- ✅ Proper - both need tamper detection
- ✅ Stay in Core

**Lines 377-397: UI SUPPRESSION POLICY**
- ✅ Proper - both need to avoid clickables
- ✅ Stay in Core

---

## ❌ MISSING FROM CORE (Should Add)

**Scenario File Structure:**
- Currently appears to be in Student/Instructor separately
- **SHOULD BE IN CORE:** Basic JSON schema for scenarios (both need to understand it)

**Debrief Format:**
- Currently in Student Interface
- **SHOULD BE IN CORE:** Both generate debriefs (Student sees it, Instructor creates rubrics)

**Equipment Tracking:**
- Currently in Student Interface
- **MIGHT BELONG IN CORE:** If Instructor needs to set equipment limits

---

## 🔄 STUDENT INTERFACE (Student-specific workflows)

**Should contain:**
- ✅ How to take scenarios (workflow)
- ✅ How to take tests (workflow)
- ✅ How to use study guides (workflow)
- ✅ Pattern Recognition Mode (workflow)
- ✅ **HINT POLICY by difficulty** (just updated - Student behavior only)
- ✅ Response formatting for students
- ✅ Export/submission instructions

**Should NOT contain:**
- ❌ Grading rubric details (Core has this)
- ❌ Scenario creation (that's Instructor)
- ❌ Provider scope definitions (Core has this)

---

## 🔄 INSTRUCTOR INTERFACE (Instructor-specific workflows)

**Should contain:**
- ✅ How to create scenarios
- ✅ How to deploy to students
- ✅ How to receive submissions
- ✅ How to grade vs. rubrics
- ✅ Class performance summaries
- ✅ Batch operations

**Should NOT contain:**
- ❌ How students take scenarios (that's Student)
- ❌ Hint policies (that's Student)
- ❌ Core definitions (Provider levels, partner pool, etc.)

---

## 🚨 CRITICAL FIXES NEEDED

### 1. REMOVE DUPLICATES (Lines to delete):
- Lines 31-36: Duplicate CHANGELOG
- Lines 166-192: Duplicate NATIONAL MODEL GUIDELINES INTEGRATION
- Lines 193-236: Duplicate WEAK AREA TRACKING SYSTEM

**Savings:** ~120 lines (30% size reduction)

### 2. MAKE AI-AGNOSTIC (Lines to modify):

**Line 68:** 
```
CURRENT: "Must be manually enabled in settings"
REPLACE: "May require enabling advanced model in your AI platform"
```

**Line 80, 168, etc.:**
```
CURRENT: "When project_knowledge_search tool is available"
REPLACE: "When knowledge search capability is available"
```

### 3. ADD FALLBACK DEFAULTS:

**Line 337:**
```
CURRENT: "Reference: assets/EMSTrainer_Default_Timing_Profiles.json"
ADD: "If file not found, use these defaults: [inline timing values]"
```

---

## 📊 FILE SIZE COMPARISON

**Current Core:** 397 lines
**After Removing Duplicates:** ~277 lines (30% smaller)
**After AI-agnostic cleanup:** ~270 lines

**Current Student Interface:** ~800 lines
**Current Instructor Interface:** ~972 lines

**Total system:** ~2,169 lines
**After cleanup:** ~2,042 lines (cleaner, not dramatically smaller but much clearer)

---

## ✅ PROPOSED ACTION PLAN

### Phase 1: Remove Duplicates (Immediate)
1. Delete duplicate CHANGELOG
2. Delete duplicate NATIONAL MODEL GUIDELINES section
3. Delete duplicate WEAK AREA TRACKING section
4. **Result:** Clean, lean Core at ~277 lines

### Phase 2: Make AI-Agnostic
1. Replace "manually enabled in settings" 
2. Replace "project_knowledge_search tool" → "knowledge search capability"
3. Replace specific AI names with "advanced reasoning models"
4. **Result:** Works in any AI platform

### Phase 3: Add Inline Defaults (Optional)
1. Add fallback timing standards if JSON missing
2. Add fallback partner pool if JSON missing
3. **Result:** Self-contained, doesn't break if assets missing

### Phase 4: Move Shared Content to Core (Optional)
1. Move basic scenario structure to Core
2. Move debrief format to Core
3. **Result:** Better separation of concerns

---

## 🎯 DECISION POINTS

**Do you want me to:**

1. **Phase 1 only** (remove duplicates - safe, immediate ~30% size reduction)
2. **Phases 1+2** (remove duplicates + make AI-agnostic)
3. **Phases 1+2+3** (add fallback defaults for robustness)
4. **Full refactor** (all phases + move shared content)

**I recommend: Phases 1+2** (clean, AI-agnostic, safe)
