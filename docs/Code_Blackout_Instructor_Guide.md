# Code Blackout - Instructor Guide

**Scenario Version:** 1.0  
**EMSTrainer Version:** 1.6.1  
**Difficulty:** Monica (Extreme)  
**Provider Level:** Paramedic  
**Last Updated:** October 10, 2025

---

## Overview

Code Blackout is a Monica-level scenario testing complete paramedic competency through a complex medical emergency with resource constraints and environmental challenges.

**Typical Duration:** 45-75 minutes depending on student decisions and patient outcome.

---

## Setup Instructions

### 1. Load Files in Order

Load these files into your AI assistant:

1. `EMSTrainer_Core.txt` (Foundation with equipment tracking)
2. `EMSTrainer_Instructor_Interface.txt` (Your instructor interface)
3. `code_blackout_scenario.json` (This scenario)

### 2. Verify Loading

After loading, confirm the AI understands the scenario:

**Ask:** "Confirm Code Blackout scenario loaded. Are you tracking equipment dynamically?"

**AI Should Respond:** Confirming equipment tracking is enabled (O2, batteries, supplies) and scenario parameters are loaded.

### 3. Start Scenario

Use standard instructor commands:
- "Start Code Blackout scenario for [student name]"
- AI will present dispatch and begin scenario

---

## Running the Scenario

### AI Handles Automatically

The AI manages:
- Equipment consumption (O2, batteries)
- Vitals trending based on interventions
- Patient response to treatments
- Environmental events as defined in scenario
- Arrest triggers based on medical reality (not time-based)
- Family member behavior based on student communication

**You do not need to calculate or track anything manually.**

### Your Role

- Observe student performance
- Take notes for debrief
- Answer questions about mechanics if needed
- Do NOT hint or guide during scenario

---

## Grading

### Rubric Structure

**Total: 1000 points**

1. **Critical Actions (300 points)**
   - Airway management
   - Glucose management
   - Cardiac management
   - Equipment failure response

2. **Clinical Decision Making (250 points)**
   - Resource prioritization
   - Pharmacology
   - Transport timing
   - Scene safety

3. **Technical Skills (200 points)**
   - IV access
   - LUCAS deployment
   - Monitoring and reassessment
   - Multi-system management

4. **Communication & Leadership (150 points)**
   - Partner direction
   - Family communication (AIDET)
   - Leadership under pressure

5. **Documentation & Handoff (50 points)**
   - Hospital report quality
   - Critical details included

6. **Hidden Criteria (50 points)**
   - Scene safety reassessment
   - Five rights of medication
   - Equipment safety

### Timing Penalties

Timing penalties are integrated throughout the rubric for:
- Delayed recognition of life threats
- Delayed interventions
- Excessive scene time
- Missed reassessment windows

**The AI tracks timing and applies penalties automatically based on the rubric.**

### Grade Scale

- 900-1000: A+ (Exceptional)
- 850-899: A (Excellent)
- 800-849: A- (Very Good)
- 750-799: B+ (Good)
- 700-749: B (Satisfactory - Pass)
- 650-699: B- (Borderline)
- 600-649: C (Marginal)
- 550-599: D (Poor)
- <550: F (Fail)

---

## Debrief Structure

### Opening

"Let's review Code Blackout. This scenario tested your complete skill set under extreme pressure. Take a moment, then let's discuss what happened."

### Key Discussion Areas

**Initial Assessment:**
- What were your first impressions?
- How did you prioritize the multiple problems?
- What was your decision-making process?

**Critical Interventions:**
- Walk me through your airway management
- Explain your pharmacology choices
- How did you manage the cardiac issues?

**Resource Management:**
- How did you handle equipment limitations?
- What was your thinking on resource allocation?
- How did equipment failures affect your plan?

**Communication:**
- How did you communicate with family?
- How did you direct your partner?
- What happened with that dynamic?

**Transport Decision:**
- When did you decide to transport?
- What factored into that decision?
- Looking back, was the timing appropriate?

**Complications:**
- [If arrest occurred] What led to the arrest?
- How did you manage the code?
- What would you do differently?

### Teaching Points

Focus on:
- Multi-system thinking and prioritization
- Time-critical interventions
- Resource conservation strategies
- Communication as a clinical skill
- Adaptation to equipment failures
- Medical consequences of delays

### Grading Review

Provide:
- Total score and grade
- Strengths demonstrated
- Areas for improvement
- Specific examples from their performance
- Timing penalties incurred (if significant)

---

## Technical Notes

### Equipment Tracking

The AI automatically tracks:
- O2 consumption based on flow rates and devices
- Battery depletion based on equipment usage
- Supply usage (IV attempts, medications)

The AI will warn students at appropriate thresholds.

### Medical Realism

Patient outcomes are determined by:
- Quality of interventions
- Timing of interventions
- Recognition of problems
- Appropriate pharmacology

Arrest triggers are medical-based, not arbitrary time limits.

### Scenario Variability

Each run may differ based on:
- Student's intervention choices
- Communication with family
- Resource management decisions
- Equipment troubleshooting approaches

**This is intended - no two runs are identical.**

---

## Support

For questions about scenario mechanics or grading, refer to:
- `code_blackout_scenario.json` - Full scenario parameters
- `code_blackout_grading_rubric.json` - Detailed point breakdown
- `EMSTrainer_Core.txt` - Equipment tracking rules

