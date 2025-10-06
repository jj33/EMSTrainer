# Beta Testing Instructions - EMSTrainer v1.6.0

**Version:** 1.6.0  
**Testing Period:** TBD  
**Testers:** 5 active beta testers  
**Status:** Ready for testing

---

## What You're Testing

This is a **major architecture overhaul** with significant new features. We need your feedback on:

1. **New modular prompt system** (2 files instead of 1)
2. **GPT-5 requirement** (medical accuracy)
3. **4 difficulty modes** (Easy, Standard, Hard, Monica)
4. **Scene safety features** (continuous assessment, unsafe starts)
5. **Equipment failures** (IV, monitor, O2, airway)
6. **Enhanced debriefs** (timing analysis, partner timeline)

---

## Prerequisites

### Required:
- ✅ **GPT-5 enabled** in Microsoft Copilot or ChatGPT
  - Open settings and manually enable GPT-5
  - **DO NOT use GPT-4o mini or earlier** (medical inaccuracy risk)
- ✅ Access to testing package (provided by instructor)

### Helpful:
- Keyboard for typing (mobile on-screen keyboard is limiting)
- Recent test results (PlatinumPlanner, practice exams)
- List of topics you're studying

---

## Setup Instructions

### Step 1: Extract Package
1. Extract `EMSTrainer_Student_v1.6.0.zip`
2. You'll have:
   - `EMSTrainer_Core.txt` (16k - Foundation + Test/Study)
   - `EMSTrainer_Scenario_Mode.txt` (23k - Scenarios)
   - `Student_Quick_Start_Guide.md` (Reference)
   - `scenario_cardiac_arrest_vf.json` (Example)
   - `README.md` (Overview)

### Step 2: Load into GPT-5
1. Open Microsoft Copilot or ChatGPT
2. **Verify GPT-5 is enabled** in settings
3. **Drag and drop** `EMSTrainer_Core.txt` into chat
4. Wait for confirmation

### Step 3: Choose What to Test
- **For Test/Study modes:** Core.txt is enough
- **For Scenarios:** Also drag `EMSTrainer_Scenario_Mode.txt`

---

## Testing Scenarios

### Test 1: Basic Functionality
**Goal:** Verify system loads and responds

**Steps:**
1. Load `EMSTrainer_Core.txt`
2. Say: "Generate 5 test questions on airway management"
3. Answer the questions
4. Verify you get immediate feedback and explanations

**Success Criteria:**
- ✅ Questions are medically accurate
- ✅ Explanations are clear and helpful
- ✅ Difficulty seems appropriate for your level

---

### Test 2: Study Mode
**Goal:** Test study guide generation

**Steps:**
1. With Core.txt loaded, say: "Create a study guide on cardiac rhythms"
2. Review the content
3. Ask follow-up questions

**Success Criteria:**
- ✅ Content is accurate and comprehensive
- ✅ Examples are helpful
- ✅ You can ask clarifying questions

---

### Test 3: Easy Mode Scenario
**Goal:** Test beginner-friendly scenario

**Steps:**
1. Load both prompt files
2. Say: "Run a respiratory distress scenario in Easy Mode"
3. Work through the scenario
4. Review the debrief

**Success Criteria:**
- ✅ Supportive, not stressful
- ✅ Hints provided when needed
- ✅ Timing tracked but not penalized
- ✅ Debrief is educational and encouraging

---

### Test 4: Standard Mode Scenario
**Goal:** Test realistic NREMT-level practice

**Steps:**
1. Say: "Run a cardiac arrest scenario in Standard Mode"
2. Work through the scenario
3. Note timing, partner interactions, vitals changes
4. Review comprehensive debrief

**Success Criteria:**
- ✅ Realistic difficulty
- ✅ Timing graded in debrief (but no in-scenario penalties)
- ✅ Partner responds to orders appropriately
- ✅ Vitals respond to interventions

---

### Test 5: Hard Mode Scenario
**Goal:** Test challenging, stressful environment

**Steps:**
1. Say: "Run a trauma scenario in Hard Mode"
2. Note environmental stressors, equipment issues
3. Check for timing penalties

**Success Criteria:**
- ✅ Noticeably harder than Standard
- ✅ Environmental distractions present
- ✅ Equipment failures may occur
- ✅ Timing violations have consequences

---

### Test 6: Monica Mode (Optional - Only if Confident!)
**Goal:** Test extreme difficulty

**WARNING:** This is intentionally brutal. Not recommended unless you want to be humbled!

**Steps:**
1. Say: "Run a scenario in Monica Mode"
2. Try to survive 15 minutes
3. Expect chaos, equipment failures, and hard consequences

**Success Criteria:**
- ✅ Timer visible and counts down
- ✅ Curveball occurs around 8-9 minute mark
- ✅ Multiple stressors at once
- ✅ Very challenging but fair

---

### Test 7: Scene Safety Feature
**Goal:** Test continuous scene safety assessment

**Steps:**
1. Say: "Run a scenario where scene safety is questionable"
2. Pay attention to scene descriptions
3. See if scene becomes unsafe during care

**Success Criteria:**
- ✅ Scene may start unsafe (requires staging)
- ✅ Scene may deteriorate during scenario
- ✅ Student must recognize and respond
- ✅ Graded on continuous assessment

---

### Test 8: Equipment Failures
**Goal:** Test realistic equipment issues

**Steps:**
1. Run multiple Standard or Hard scenarios
2. Watch for equipment failures:
   - IV access fails (vein blows)
   - Monitor issues
   - Oxygen equipment
   - Airway equipment

**Success Criteria:**
- ✅ Failures feel realistic (not excessive)
- ✅ Student can adapt (backup equipment, alternate routes)
- ✅ Time penalties applied appropriately

---

## What to Report

### For Each Test, Note:

**1. Medical Accuracy**
- Were protocols correct?
- Were medications/dosages accurate?
- Were vital signs realistic?
- Any concerning errors?

**2. Usability**
- Was it easy to use?
- Were instructions clear?
- Any confusion about what to do?
- File loading issues?

**3. Difficulty Appropriateness**
- Was Easy actually easy?
- Was Standard NREMT-level?
- Was Hard challenging but fair?
- Was Monica brutal? (it should be!)

**4. Debrief Quality**
- Was feedback helpful?
- Timing analysis clear?
- Hidden grading fair?
- Anything missing?

**5. Technical Issues**
- Files not loading?
- GPT-5 errors?
- Unexpected behavior?
- Performance problems?

**6. Educational Value**
- Did you learn something?
- Was it enjoyable?
- Would you use this for studying?
- Better than alternatives?

---

## Feedback Format

Please provide feedback via:
- Email to instructor
- Feedback form (if provided)
- Direct conversation

**Include:**
- Your name
- Which tests you completed
- What worked well
- What didn't work
- Suggestions for improvement
- Overall impression (1-5 stars)

---

## Known Issues

None currently - you're the first to test v1.6.0!

If you encounter issues, that's valuable feedback. Report everything!

---

## Tips for Testing

1. **Test multiple scenarios** - first one might feel awkward, but you'll get the hang of it
2. **Try different difficulties** - see how they compare
3. **Be honest** - we want to know what's broken!
4. **Note medical errors** - this is critical for patient safety
5. **Test your weak areas** - does it actually help you learn?
6. **Compare to old version** - is v1.6.0 better?

---

## Timeline

**Testing Period:** [INSERT DATES]  
**Feedback Due:** [INSERT DATE]  
**Follow-up:** [INSERT DATE]

---

## Questions?

Contact: [INSTRUCTOR CONTACT INFO]

---

## Thank You!

Your testing helps make EMSTrainer better for everyone. We appreciate your time and feedback!

**Good luck and have fun!** 🚑

---

*EMSTrainer v1.6.0 Beta Testing Instructions*  
*Updated: 2025-01-06*
