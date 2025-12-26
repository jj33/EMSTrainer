# Protocol-Based Grading Feature Request

**Date:** December 25, 2025  
**Requested By:** User  
**Target Version:** v1.7.0  
**Priority:** Priority 1 (expansion of existing Protocol Loading feature)

---

## Feature Request

**Add protocol-based grading** as expansion of the existing Protocol Loading & Validation feature (v1.7.0 Feature #1).

## Current State

v1.7.0 Feature #1 includes:
- Protocol upload and parsing
- Scenario validation against protocols
- Protocol-compliant scenario generation
- Brief mention of "grading integration"

## Requested Addition

**Expand grading integration to full protocol-based grading system:**

### What It Does

Grade student performance against agency-specific protocols instead of (or in addition to) NREMT standards.

### Why It Matters

- **NREMT gets you certified** → National standards for certification
- **Agency protocols keep you employed** → Local medical director requirements
- Students need to know when their protocols differ from NREMT
- Teaches real-world protocol compliance

### Example Output

```
=== PROTOCOL COMPLIANCE DEBRIEF ===

Grading Mode: Agency Protocol (Brainerd ALS 2024)

**Overall Scores:**
- NREMT Score: 88/100 (B+) - Strong NREMT-level performance
- Protocol Score: 82/100 (B) - Some agency protocol deviations

**Protocol Compliance Breakdown:**

✅ COMPLIANT (7 interventions):
1. O2 15 LPM NRB (Protocol 2.1, p.14)
2. Aspirin 324mg (Protocol 2.1, p.15)
3. IV 18g established (Protocol 2.1, p.15)
4. Cardiac monitor applied (Protocol 2.1, p.14)
5. Vital signs Q5min (Protocol 2.1, p.16)
6. Position: Fowler's (Protocol 2.1, p.14)
7. Transport to STEMI center (Protocol 2.1, p.17)

❌ PROTOCOL DEVIATIONS (2 interventions):
1. 12-lead at 8min → Protocol requires <5min (Protocol 2.1, p.14) [-5pts]
2. Nitro before 12-lead → Protocol requires ECG first (Protocol 2.1, p.15) [-3pts]

**Key Learning:**
Your agency protocol is MORE strict than NREMT:
- 12-lead timing: NREMT allows 10min, Brainerd requires 5min
- Nitro sequence: NREMT flexible, Brainerd requires 12-lead first

Know YOUR protocols, not just NREMT standards.
```

### Key Features

**1. Dual Scoring:**
- Show both NREMT score (certification standard)
- Show protocol score (agency compliance)
- Student sees difference between national vs local standards

**2. Protocol-Specific Validation:**
- Medication doses (agency-specific)
- Timing requirements (agency-specific)
- Treatment sequences (agency-specific)
- Equipment usage (agency-specific)

**3. Deviation Tracking:**
- Flag each protocol deviation
- Provide specific protocol reference (page number, section)
- Explain WHY protocol differs from NREMT
- Point deductions based on severity

**4. Educational Debrief:**
- Compare NREMT vs agency requirements
- Identify where agency is stricter/more lenient
- Teach protocol-specific rationale
- Provide learning points for improvement

### Use Cases

**Rural Service (Extended Scene Times):**
- Protocol allows 15min scene time vs NREMT 10min
- Student isn't penalized for realistic rural timing
- Grading reflects local reality

**Urban Service (Aggressive Cardiac Protocols):**
- Protocol requires 12-lead <3min vs NREMT 10min
- Student held to stricter local standard
- Prepares for actual job requirements

**Flight Service (CCP Protocols):**
- Protocol includes RSI, blood products, advanced procedures
- Grading against CCP scope, not standard paramedic
- Protocol-specific equipment and interventions

**Student Learning Department Protocols:**
- Show NREMT score (what gets certified)
- Show protocol score (what gets employed)
- Highlight differences
- Teach local medical director requirements

### Implementation Notes

**Grading Mode Selection:**

```json
{
  "grading_mode": "protocol",
  "protocol_source": "Brainerd Ambulance ALS Protocols 2024",
  "show_nremt_comparison": true,
  "strict_compliance": false
}
```

**OR via command:**
```
Student: "Grade against Brainerd protocols"
```

**Instructor Control:**
```
Instructor: "Enable protocol grading for all scenarios"
Instructor: "Grade with both NREMT and protocol scores"
```

### Multi-Level Support (CRITICAL)

**Must work for EMR, EMT, Paramedic:**

- **EMR:** Graded on EMR-appropriate interventions from protocol
- **EMT:** Graded on EMT-level protocol compliance  
- **Paramedic:** Graded on full protocol scope

**Scope recognition graded positively:**
- EMR recognizes need for ALS → +points
- EMT recognizes own limitations → +points

**Protocol parsing identifies scope:**
- Extract BLS vs ALS interventions
- Flag scope-specific timing
- Identify when "ALS required" per protocol

### Technical Requirements

**Protocol Extraction:**
- Medication doses
- Route requirements
- Timing windows
- Treatment sequences
- Contraindications
- Medical control requirements

**Grading Logic:**
- Compare student actions to protocol requirements
- Calculate deviations
- Generate point deductions
- Provide specific references

**Debrief Generation:**
- Protocol compliance section
- NREMT comparison (optional)
- Deviation explanations
- Learning points
- Protocol references with page numbers

### Files to Update

**When implementing:**

1. **EMSTrainer_Core.txt:**
   - Add protocol grading rubric section
   - Add protocol deviation tracking
   - Add dual-scoring logic
   - Add protocol reference formatting

2. **EMSTrainer_Instructor_Interface.txt:**
   - Add protocol grading enable/disable
   - Add protocol score weighting
   - Add protocol compliance reports

3. **v1.7.0_Feature_Planning.md:**
   - Expand Protocol Loading feature (Section 1, Phase 4)
   - Add protocol grading to implementation phases
   - Add to testing requirements
   - Update success metrics

### Benefits

✅ Teaches real-world protocol compliance  
✅ Prepares students for actual agency requirements  
✅ Highlights NREMT vs local differences  
✅ Maintains NREMT-level training (dual scoring)  
✅ Provides specific, actionable feedback  
✅ References protocol documentation

### Status

**Requested:** December 25, 2025  
**Target:** v1.7.0 Priority 1 (expansion of existing feature)  
**Implementation:** Part of Protocol Loading & Validation feature  
**Estimated Effort:** Medium (builds on existing protocol parsing)

---

## Integration with Existing v1.7.0 Features

This feature enhances existing Protocol Loading feature:

**Phase 1-3 (Already Planned):**
- Protocol upload ✅
- Scenario validation ✅  
- Protocol-compliant generation ✅

**Phase 4 (This Request):**
- **Protocol-based grading** ⭐ NEW
- Dual scoring (NREMT + Protocol)
- Deviation tracking with references
- Educational compliance debrief

---

## Next Steps

1. Review this feature request
2. Confirm fit within v1.7.0 scope
3. Add to Phase 4 of Protocol Loading feature
4. Update planning docs when ready
5. Implement after Phase 1-3 complete

---

**Document Status:** Feature Request  
**Requested By:** User (Joel)  
**Date:** December 25, 2025  
**File:** planning/feature_requests/protocol_based_grading.md
