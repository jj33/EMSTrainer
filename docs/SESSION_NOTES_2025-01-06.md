# Development Session Notes - January 6, 2025

**Session Duration:** ~6 hours  
**Developer:** Joel (EMT with AEMT scope)  
**AI Assistant:** Claude 3.5 Sonnet v4.5 (Cursor Agent Mode)  
**Branch:** feat/strict-json-code-blackout

---

## 🎯 Session Goals Accomplished

### Primary Mission: Modular Architecture
✅ Split monolithic prompt into focused modules  
✅ Core.txt (16k): Foundation + Test/Study  
✅ Scenario_Mode.txt (23k): Complete scenario engine  
✅ Removed character limit constraints (drag-drop files)

---

## 🏗️ Architecture Decisions

### Why We Split the Prompts:
1. **Character Limits**: Copilot chat has ~8k input limit for paste, unlimited for file drag-drop
2. **Maintainability**: Easier to update specific features
3. **User Choice**: Students can load just Core for tests, or add Scenario Mode as needed
4. **Original Mission**: Test/Study modes were the original intent (PlatinumPlanner integration)

### File Structure Rationale:
```
Core.txt = Foundation + Test/Study (the learning system)
Scenario_Mode.txt = Complex scenarios (Monica, scene safety, equipment failures, etc.)
```

### Provider Level Approach:
- **Base + Delta notation** (not redundant full lists)
- **Local overrides** via provider_levels.json
- **Example:** Joel's EMT = EMT_national + IV/IO/limited_meds/12-lead (AEMT-level minus advanced airway)

---

## 💡 Key Design Principles Established

### 1. Teaching First
- Easy Mode: No penalties, supportive, explained timing
- Standard: NREMT-level, graded timing
- Hard: Penalized timing
- Monica: Hard fail on timing violations

### 2. Monica Mode Philosophy
- "Everything on, pants on fire mode"
- For "paragods" who think they know everything
- Designed to humble, not to teach
- Warning label included

### 3. Scene Safety
- NOT one-time check - continuous assessment required
- Scenarios CAN start unsafe (require staging)
- Dynamic degradation during care
- Hidden grading (15 pts)

### 4. Equipment Realism
- IV failures (first attempt can blow)
- Monitor issues (battery, leads)
- O2 equipment problems
- Timing penalties realistic (30-60s)
- Probability scales with difficulty

### 5. Hidden Grading
- 5 Rights medication check (10 pts)
- AIDET communication (10 pts)
- Scene safety reassessment (15 pts)
- Students discover through debriefs

---

## 🚧 Technical Challenges Solved

### Issue: Premature Close Errors
**Problem:** Large file creation operations hitting 25 tool-call limit in Cursor Agent Mode  
**Solution:** Work in smaller chunks, use terminal cat commands for large files  
**Status:** Workaround successful

### Issue: Token Budget Anxiety
**Problem:** Developer concerned about 200k token session limit  
**Reality:** Each SESSION gets 200k tokens (not monthly limit)  
**Result:** Plenty of tokens remaining (54k+ left at end)

### Issue: Character Limits
**Problem:** Original 8k character limit for prompts  
**Solution:** Drag-and-drop files bypass limit (Copilot processes files separately)  
**Impact:** Removed all character limit constraints, files now 16k-23k

---

## 📋 Feature Tracking

### Completed This Session:
- Modular prompt architecture
- ACP provider level
- Scene safety (continuous, unsafe starts)
- Equipment failures
- Hidden grading
- Quick Start guides
- Example scenarios (2)
- What's New doc
- CHANGELOG update
- Provider levels schema & example

### Deferred to v1.7:
- Equipment timing (LUCAS 30-45s, EtCO2 15s calibration)
- In-prompt scenario editor
- Full encryption (AES-256)
- Complete conversation transcripts
- Voice of patient
- Integrated documentation prompts

### Tracked for Later:
- Instructor test/study generator ("Generate test on ALS airway")
- Communication challenges (radio static, delays)

---

## 🎓 Domain Knowledge Captured

### Joel's Local Scope (Example County EMS):
- **EMT:** Can do IV/IO, limited meds, 12-lead (AEMT-level minus advanced airway)
- **Paramedic:** Can run vents, some CC meds, but NOT crich or ECMO

### Equipment Timing Realism:
- **LUCAS device:** 30-45 second setup after proper positioning
- **EtCO2 capnography:** ~15 second calibration after activation on Zoll
- Hidden grading: "Did you remember to enable it?"

### Monica Mode Named After:
- Team member Monica
- Designed for experienced providers who need humbling
- "Pants on fire" difficulty

### Industry Timing Standards:
- On-scene: Target ≤10min, Hard max 15min
- CPR: <1min, Defib: <2min
- Epi (anaphylaxis): <3min target, 5min hard max
- Trauma load-go: <10min

---

## 🗂️ File Organization

### New Files Created:
```
prompts/
├── EMSTrainer_Core.txt (16k)
└── EMSTrainer_Scenario_Mode.txt (23k)

docs/
├── Student_Quick_Start_Guide.md
├── Instructor_Quick_Start_Guide.md
├── WHATS_NEW_v1.6.0.md
└── SESSION_NOTES_2025-01-06.md (this file)

examples/
├── scenario_cardiac_arrest_vf.json
├── scenario_mvc_trauma_monica.json
└── provider_levels_expanded_emt.json

assets/schema/
└── provider_levels.schema.json
```

### Files Modified:
- README.md (v1.6.0 architecture)
- planning/*.md (updated features, roadmap)
- assets/emstrainer_partner_names.json (added ACP partners)
- CHANGELOG.md (v1.6.0 entry)

### Files Removed:
- prompts/EMSTrainer_Core_Prompt.txt (replaced)
- .github/workflows/*.yml (solo dev, can restore later)

---

## 🎯 Next Session Priorities

### Immediate (15 min tasks):
1. Test Core.txt in GPT-5 (verify it loads and works)
2. Test Scenario_Mode.txt with Core loaded
3. Generate a sample test question set
4. Run a sample scenario (Standard difficulty)

### Short-term (30-60 min tasks):
1. Create provider_levels.json for Joel's jurisdiction
2. Test equipment failure scenarios
3. Verify hidden grading works in debriefs
4. Create one more example scenario (respiratory distress?)

### Medium-term (Next few sessions):
1. Implement equipment timing delays (LUCAS, EtCO2)
2. Build in-prompt scenario editor
3. Create instructor test/study generator
4. Add more example scenarios

### Long-term (v1.7+):
1. Full encryption implementation
2. Conversation transcript capture
3. Voice of patient enhancement
4. Documentation prompts integration

---

## 💭 Open Questions for Next Session

1. **Testing Results:** Did Core.txt + Scenario_Mode.txt work as expected in GPT-5?
2. **User Feedback:** What do the 5 beta testers think of v1.6.0?
3. **Provider Levels:** Should we create more jurisdiction examples?
4. **Equipment Timing:** Priority level for LUCAS/EtCO2 implementation?
5. **Instructor Features:** When to build test/study generator?

---

## 🔧 Development Environment Notes

### Joel's Setup:
- **Display:** 4K TV at 10 feet (not optimal!)
- **Font Size:** Small at default, recommend Cmd/Ctrl + = to zoom
- **Time Zone:** Central (work shift starts 6:30pm)
- **Mobile Note:** Keyboard strongly recommended for mobile use

### Cursor Issues Encountered:
- Premature close errors (25 tool-call limit)
- File creation operations timing out
- Workaround: Smaller chunks, terminal commands

### Token Usage Pattern:
- Started: 0/200k
- Ended: ~145k/200k (72% used)
- Remaining: 54k+ tokens
- Efficient session with room to spare

---

## 📝 Style & Convention Decisions

### Prompt Files:
- Plain text (.txt) for universal compatibility
- Markdown formatting for structure
- Drag-and-drop distribution (no copy/paste needed)

### Scenario Files:
- JSON format with comprehensive structure
- Filename pattern: scenario_[type]_[variant].json
- Include grading rubrics and timing standards

### Debrief Files:
- Markdown source for editing
- PDF export for students
- Filename: [Date]_[ScenarioID]_Debrief_[StudentID].md

### Documentation:
- Quick Start guides for user onboarding
- What's New for release notes
- Session Notes for development continuity
- Planning docs for feature tracking

---

## 🎬 Memorable Moments

- **"Engage!"** - Joel is a Star Trek fan 🖖
- **Monica Mode Warning** - Added specific warning about being designed to humble "paragods"
- **Token Anxiety** - Clarified session vs monthly token limits
- **Character Limit Discovery** - Drag-drop files = unlimited size!
- **GPT-5 Reality Check** - Joel confirmed GPT-5 is available in Copilot (manually enabled)
- **Equipment Realism** - LUCAS and EtCO2 timing from real-world experience
- **Scene Safety Philosophy** - "Not a one-time check" - continuous assessment critical

---

## 🚀 Ready for Tomorrow

### What's Committed & Pushed:
✅ All new prompt files  
✅ Documentation complete  
✅ Examples ready  
✅ README updated  
✅ CHANGELOG current  
✅ Planning docs synced

### What to Test:
- Load Core.txt in GPT-5
- Generate test questions
- Create study guide
- Run scenarios (all difficulties)
- Verify equipment failures
- Check hidden grading

### What to Build Next:
- Equipment timing delays
- In-prompt scenario editor
- More example scenarios
- Joel's local provider_levels.json

---

**Session Status:** ✅ Complete  
**Branch Status:** Ready to merge or continue  
**Next Session:** Test and iterate on v1.6.0 features

*Live long and prosper!* 🖖
