# EMSTrainer v1.6.0 - Test Plan

**Test Coordinator:** Joel  
**Test Period:** January 7-14, 2025  
**Testers:** Joel + 5 beta testers  
**Status:** In Progress

---

## Test Phases

### Phase 1: Stress Test (30 Students) - ✅ COMPLETE
**Scenario:** Cardiac Arrest VF, Standard Mode  
**Students:** 30 synthetic (AI-generated)  
**Distribution:** 8 excellent, 4 good, 5 adequate, 13 poor (actual)  
**Tool:** Copilot (free tier)  
**Status:** Complete - All validation passed

**Deliverables:**
- [x] Individual submissions ZIP (30 files)
- [x] Combined submissions JSON (all 30)
- [x] Pre-graded results ZIP (baseline comparison)
- [x] Class summary report
- [x] Validation script created
- [x] Test report documented

**Success Criteria:**
- ✅ Grading identifies correct performance tiers (Perfect match: 8A, 4B, 5C, 13D)
- ✅ Class summary highlights real weaknesses (5 key areas identified)
- ✅ Teaching recommendations actionable for Cody (6 specific drills)
- ✅ All data integrity checks passed (100%)

**Results:** See `tests/results/test_001_stress_30_students.md`

---

### Phase 2: Real Student Testing (3-5 Students)
**Scenario:** TBD (instructor creates)  
**Students:** Real beta testers  
**Difficulty:** Standard Mode  
**Tool:** GPT-5 in Copilot/ChatGPT

**Test Cases:**

**Test 2.1: Student Question Generation**
- Student uploads PlatinumPlanner results
- Request targeted questions
- Verify: Questions match weak areas
- Expected: 10-20 targeted questions with explanations

**Test 2.2: Student Study Guide**
- Student requests study guide on topic
- Verify: Appropriate level, clear explanations
- Expected: Complete study material with examples

**Test 2.3: Easy Mode Scenario**
- Student runs respiratory distress, Easy mode
- Verify: Supportive, hints provided, no penalties
- Expected: Learning-focused debrief

**Test 2.4: Standard Mode Scenario**  
- Student runs trauma scenario, Standard mode
- Verify: Realistic timing, graded debrief
- Expected: NREMT-level challenge

**Test 2.5: Hard Mode Scenario** (Advanced only)
- Student runs cardiac scenario, Hard mode
- Verify: Strict timing, equipment failures, challenges
- Expected: Difficult but fair

---

### Phase 3: Instructor Workflow Testing
**Tester:** Joel as instructor  
**Tool:** GPT-5 with instructor prompts

**Test 3.1: Create Test Questions**
```
"Generate 10 questions on ALS airway for paramedic students"
```
- [ ] Questions generated
- [ ] Answer key included
- [ ] Appropriate difficulty
- [ ] Medically accurate

**Test 3.2: Create Study Guide**
```
"Create study guide on pediatric respiratory emergencies for EMT students"
```
- [ ] Complete content
- [ ] Age-appropriate
- [ ] Practice questions included
- [ ] NREMT tips provided

**Test 3.3: Create Scenario**
```
"Create respiratory distress scenario for AEMT students, Standard difficulty"
```
- [ ] Complete JSON generated
- [ ] Realistic vitals
- [ ] Appropriate for level
- [ ] Grading rubric included

**Test 3.4: Deploy Scenario**
```
"Format this scenario for email to: Student1, Student2, Student3"
```
- [ ] Email template generated
- [ ] Instructions clear
- [ ] JSON formatted correctly
- [ ] Copy-paste ready

**Test 3.5: Grade Submission**
```
"Grade this submission: [paste student JSON]"
```
- [ ] Scores accurate
- [ ] Feedback specific
- [ ] Timing analyzed
- [ ] Recommendations useful

**Test 3.6: Class Summary**
```
"Generate class summary for all submissions"
```
- [ ] Statistics accurate
- [ ] Patterns identified
- [ ] Teaching recommendations
- [ ] Actionable for instructor

---

### Phase 4: Edge Cases & Error Handling

**Test 4.1: Hash Mismatch**
- Modify scenario hash in submission
- Verify: Flagged but not auto-failed
- Expected: Warning to instructor

**Test 4.2: Invalid Submission Format**
- Submit malformed JSON
- Verify: Error message, guidance provided
- Expected: Clear error, instructions to fix

**Test 4.3: Timing Violations**
- Easy: Over time → No penalty
- Standard: Over time → Graded
- Hard: Over time → Penalized
- Monica: Over time → Hard fail

**Test 4.4: Scope Violations**
- EMT attempts intubation
- Verify: Rejected appropriately
- Expected: "Outside your scope" message

**Test 4.5: Equipment Failures**
- Standard: 10-15% probability
- Hard: 20-25%
- Monica: 30-35%
- Verify: Failures occur at expected rates

---

### Phase 5: Difficulty Scaling Validation

**Test 5.1: Easy Mode Characteristics**
- No penalties observed
- Hints provided when stuck
- Supportive debrief tone
- Vitals forgiving

**Test 5.2: Standard Mode Characteristics**
- Timing graded but not penalized in-scenario
- Balanced support
- NREMT-level challenge
- Realistic vitals

**Test 5.3: Hard Mode Characteristics**
- Timing penalized
- Equipment failures occur
- Minimal support
- Challenging but fair

**Test 5.4: Monica Mode Characteristics**
- Timer countdown active
- Hard fail at timeout
- Curveballs guaranteed
- Maximum difficulty
- Brutal but consistent

---

## Test Data Tracking

### For Each Test:
- Test ID
- Date/Time
- Tester name
- Test type (unit/integration/stress/regression)
- Expected outcome
- Actual outcome
- Pass/Fail
- Notes/Issues
- Time to complete

### Results Storage:
```
tests/
├── results/
│   ├── test_001_stress_30_students.md
│   ├── test_002_easy_mode_validation.md
│   └── test_003_grading_accuracy.md
└── data/
    ├── batch_001/ (30 students)
    ├── batch_002/ (next test)
    └── baseline/ (regression baseline)
```

---

## Bug Reporting

### Format:
```
**Bug ID:** BUG-001
**Date:** 2025-01-07
**Tester:** Joel
**Component:** Grading
**Severity:** Medium
**Description:** Grading gave 91/100 but expected 85/100 based on missed interventions
**Steps to Reproduce:** [details]
**Expected:** 85/100
**Actual:** 91/100
**Workaround:** Manual adjustment
**Status:** Open
```

---

## Success Metrics

### v1.6.0 Release Criteria:

**Must Pass:**
- [X] 30-student stress test completes without errors
- [X] Class summary identifies valid teaching priorities
- [X] Individual grading within ±5 points of expected (Perfect match)
- [ ] All difficulty modes behave as specified
- [ ] Question/study generation produces quality content
- [ ] Documentation sufficient for new users

**Should Pass:**
- [ ] Grading consistent across multiple runs (±3 points)
- [ ] Equipment failures occur at expected rates
- [ ] Hidden grading criteria work correctly
- [ ] Timing enforcement appropriate per difficulty
- [ ] Scope violations caught correctly

**Nice to Have:**
- [ ] All 5 testers complete scenarios successfully
- [ ] Feedback universally positive
- [ ] No critical bugs found
- [ ] Performance acceptable (grading <5 min per student)

---

## Timeline

**January 7 (Today):**
- [X] Generate stress test data (Copilot)
- [X] Import and organize files
- [X] Run grading validation (validate_test_results.py)
- [X] Document results (test_001_stress_30_students.md)
- [X] Resolve 400 error (created local validation script)

**January 8-10:**
- [ ] Beta tester scenarios (3-5 real students)
- [ ] Collect feedback
- [ ] Fix critical bugs

**January 11-13:**
- [ ] Regression testing
- [ ] Documentation updates
- [ ] Final refinements

**January 14:**
- [ ] Testing complete
- [ ] Go/No-Go decision for v1.6.0 release
- [ ] Plan v1.7 features

---

*Test plan active. Data generation in progress.*
