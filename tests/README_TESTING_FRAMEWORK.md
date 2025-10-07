# EMSTrainer Testing Framework

**Version:** 1.6.0  
**Purpose:** Validate instructor → student → grading workflow at scale  
**Date:** January 7, 2025

---

## Testing Philosophy

### Goals:
1. **Validate workflow** - End-to-end process works as designed
2. **Ensure consistency** - Same scenario graded similarly across runs
3. **Identify bottlenecks** - Find friction points in real use
4. **Verify accuracy** - Grading reflects actual performance
5. **Test at scale** - System handles realistic class sizes (30+ students)

### Approach:
- **Synthetic data** - AI-generated student submissions
- **Controlled variation** - Known performance distribution
- **Repeatability** - Save test data for regression testing
- **Offline capability** - Test without active AI session

---

## Test Types

### 1. Unit Tests (Individual Components)
- Question generation (various topics)
- Study guide creation
- Single scenario creation
- Single submission grading
- Individual debrief format

### 2. Integration Tests (Workflow)
- Instructor creates → Student runs → Instructor grades
- Hash validation
- Timing enforcement by difficulty
- Equipment failure handling
- Hidden criteria grading

### 3. Stress Tests (Scale)
- 30 students, same scenario
- Class summary generation
- Performance distribution analysis
- Common weakness identification
- Teaching recommendations

### 4. Regression Tests (Stability)
- Re-run same test data
- Compare grading consistency
- Verify no feature degradation
- Check backward compatibility

---

## Test Data Structure

### Organization:
```
tests/
├── README_TESTING_FRAMEWORK.md (this file)
├── TEST_PLAN.md (specific test cases)
├── scenarios/
│   ├── stress_test_scenario_cardiac_vf.json
│   └── [additional test scenarios]
├── submissions/
│   ├── batch_001_30_students/
│   │   ├── individual/
│   │   │   ├── student_001.json
│   │   │   └── ... (30 files)
│   │   └── combined/
│   │       └── all_30_students.json
│   └── batch_002_[next_test]/
├── grading_results/
│   ├── batch_001_results/
│   │   ├── individual_debriefs/
│   │   └── class_summary.md
│   └── batch_002_results/
└── validation/
    ├── expected_outcomes.json
    └── regression_baseline.json
```

---

## Stress Test Protocol

### Setup Phase:
1. **Generate scenario** (Instructor mode in Copilot/GPT-5)
2. **Save scenario** to `tests/scenarios/`
3. **Define expected distribution** (6 excellent, 12 good, 8 adequate, 4 poor)

### Execution Phase:
4. **Generate 30 submissions** (Copilot/GPT-5)
5. **Download files:**
   - Individual submissions ZIP
   - Combined JSON file
   - Pre-graded results ZIP (for comparison)
6. **Save to** `tests/submissions/batch_XXX/`

### Validation Phase:
7. **Grade in EMSTrainer** (load instructor prompt, grade all 30)
8. **Compare results:**
   - Copilot grading vs EMSTrainer grading
   - Should be similar (±5 points acceptable)
9. **Analyze class summary:**
   - Common weaknesses identified?
   - Teaching recommendations useful?
   - Statistics accurate?

### Documentation Phase:
10. **Record results** in test report
11. **Note any discrepancies**
12. **Document lessons learned**
13. **Update baseline** if needed

---

## Success Criteria

### For Scenario Generation:
✅ Complete JSON with all required fields  
✅ Realistic vitals and progression  
✅ Appropriate difficulty scaling  
✅ Valid hash generated  
✅ Clear learning objectives

### For Student Submissions:
✅ Realistic performance variation  
✅ Appropriate timing patterns  
✅ Valid action sequences  
✅ Complete SOAP documentation  
✅ Hash matches original scenario

### For Grading:
✅ Scores reflect performance accurately  
✅ Feedback is specific and actionable  
✅ Timing analysis correct  
✅ Hidden criteria evaluated  
✅ Consistent across similar performance levels

### For Class Summary:
✅ Statistics accurate (averages, distributions)  
✅ Common weaknesses identified correctly  
✅ Teaching recommendations actionable  
✅ Individual student data accessible  
✅ Trends highlighted appropriately

---

## Regression Testing

### Baseline Establishment:
1. Run stress test with 30 students
2. Save all results as "baseline"
3. Document expected scores and patterns

### Future Testing:
1. Re-run same scenario with same student data
2. Compare new grading to baseline
3. Acceptable variance: ±3 points per student
4. Flag if common weaknesses change significantly

### When to Regression Test:
- After prompt updates
- After grading logic changes
- Before major releases
- Monthly (maintenance)

---

## Known Limitations

### Current System:
- Manual file management (no database)
- Single-threaded grading (one at a time)
- No automated batch processing
- Hash validation theoretical (not enforced in chat)
- Submission format varies (student must format correctly)

### Testing Limitations:
- Synthetic data (not real student behavior)
- AI-generated mistakes may not match real patterns
- Timing variations artificial
- No actual patient interaction testing

### Acceptable Variances:
- Grading: ±5 points across different AI sessions
- Timing: ±10 seconds in action logs
- Statistics: ±2% in class averages
- Recommendations: Different wording, same concepts

---

## Test Execution Checklist

### Before Each Test:
- [ ] GPT-5 enabled and verified
- [ ] Latest prompt files loaded
- [ ] Test data prepared
- [ ] Expected outcomes documented
- [ ] Timer started (track execution time)

### During Test:
- [ ] Note any errors or warnings
- [ ] Screenshot unexpected behavior
- [ ] Track time for each phase
- [ ] Monitor AI response quality

### After Test:
- [ ] Compare results to expected
- [ ] Document variances
- [ ] Update baseline if appropriate
- [ ] File bug reports if needed
- [ ] Update test plan with lessons learned

---

## Future Enhancements

### v1.7 Testing Needs:
- Equipment timing validation (LUCAS, EtCO2)
- Encryption testing (when implemented)
- In-prompt editor testing
- Multi-agency scenarios (Fire/Police)

### v2.0 Testing Needs:
- Batch processing automation
- LMS integration testing
- Web dashboard testing
- Performance benchmarking

---

## Contact & Support

**For testing team:**
- Report issues immediately
- Document workarounds
- Share unexpected findings
- Suggest improvements

**Test coordinator:** Joel  
**Testing window:** January 7-14, 2025  
**Feedback due:** January 14, 2025

---

*Framework established. Ready for validation.*
