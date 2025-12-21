# EMSTrainer Project Philosophy

**Last Updated:** 2025-12-21  
**Document Status:** Living Document - Core Principles

---

## Core Mission

EMSTrainer is an AI-powered educational tool providing realistic scenario-based training for emergency medical services personnel across multiple certification levels.

---

## PRIMARY TARGET AUDIENCE (Core Tenet)

**This is NON-NEGOTIABLE:** EMSTrainer must serve multiple certification levels effectively.

### Priority Levels:

**Tier 1 - Primary Focus:**
1. **EMT (Emergency Medical Technician)**
2. **Paramedic (EMT-P)**

**Tier 2 - Important:**
3. **EMR (Emergency Medical Responder / First Responder)**

**Tier 3 - Future Expansion:**
4. Critical Care Paramedic (CCP)
5. Air Care Paramedic (ACP)

---

## Development Philosophy

### Multi-Level Support is Core

**Every feature must consider:**
- Can this work for EMR students?
- Can this work for EMT students?
- Can this work for Paramedic students?
- Does this scale appropriately across cert levels?

**If a feature cannot support all three primary levels (EMR/EMT/Paramedic):**
- First attempt: Adapt feature to work for all levels
- Second attempt: Make feature cert-level aware (different behavior per level)
- Last resort: If truly untenable, consider dropping EMR support
- **NEVER:** Build features only for Paramedic level

### Why EMR Matters

**First Responder scenarios are valuable:**
- Law enforcement officers with medical training
- Fire department first responders
- Industrial/workplace first responders
- Ski patrol, park rangers, event medical
- Community volunteers

**Educational value:**
- Teaches foundational assessment skills
- Teaches scope recognition (when to call for higher level)
- Teaches resource limitation management
- Real-world relevance (many areas have EMR-level first response)

**If EMR becomes untenable:** Only drop if maintaining it actively harms the quality for EMT/Paramedic users. Document the decision and reasoning.

---

## Scenario Design Principles

### Scenarios Should Scale Across Levels

**BLS-Focused Scenarios:**
- Manageable by EMR with basic interventions
- EMT can provide more advanced care (O2, positioning, splinting)
- Paramedic recognizes it's BLS and manages efficiently

**ALS-Optional Scenarios:**
- EMR/EMT manage basic care, recognize need for ALS
- Paramedic provides advanced interventions that improve outcome

**ALS-Critical Scenarios:**
- EMR/EMT manage initial stabilization, early recognition
- Paramedic required for definitive care
- Used to teach scope recognition for EMR/EMT

**Example: Respiratory Distress (COPD)**
- EMR: O2 administration, positioning, recognition, rapid transport
- EMT: O2 + CPAP if available, assisted medications per protocol
- Paramedic: CPAP/BiPAP, IV access, bronchodilators, Versed

---

## Grading Philosophy

### Scope-Appropriate Expectations

**Grading must reflect certification level:**
- EMR graded on EMR scope (assessment, basic interventions, recognition)
- EMT graded on EMT scope (BLS airway, medications per protocol)
- Paramedic graded on Paramedic scope (advanced interventions, medications)

**Scope Recognition is Graded Positively:**
- EMR recognizes need for ALS → positive points
- EMT recognizes limitation, calls for Paramedic → positive points
- Don't penalize for not performing out-of-scope skills

**Example: Cardiac Arrest**
- EMR: CPR, AED, scene management → 100% possible
- EMT: EMR skills + airway adjuncts, detailed assessment
- Paramedic: Full ACLS protocol, medications, advanced airway

---

## Partner Assignment Philosophy

### Complementary Certification Levels

**Default partner assignment:**
- Student EMR → Partner EMT or Paramedic
- Student EMT → Partner Paramedic (or EMT for peer scenarios)
- Student Paramedic → Partner EMT (student leads)

**Educational value:**
- EMR learns from higher-level partner
- EMT practices leadership with EMR, learns from Paramedic
- Paramedic practices delegation and teaching

**Monica Mode:**
- Partner "Pat" is always EMT certification
- Unhelpful but within scope for EMT
- Creates leadership pressure regardless of student level

---

## Feature Development Priorities

### Must Support All Levels (Unless Impossible)

**New features checklist:**
- [ ] Works for EMR students?
- [ ] Works for EMT students?
- [ ] Works for Paramedic students?
- [ ] Grading scale appropriate per level?
- [ ] Partner behavior appropriate per level?
- [ ] Scenarios available for all levels?

**Future Features - Multi-Level Considerations:**

**Protocol Loading (v1.7):**
- Must support EMR, EMT, and Paramedic protocols
- Scope enforcement per cert level
- Grading against level-appropriate protocols

**Timing Standards:**
- Different time targets per cert level where appropriate
- EMR might have longer scene times (less training)
- Paramedic expected to be more efficient

**Pattern Recognition Mode:**
- Present findings appropriate to cert level
- EMR: Basic assessment findings → call for help
- EMT: More detailed findings → BLS differential
- Paramedic: Complex presentations → full differential

**Study Guides:**
- Content targeted to cert level
- NREMT prep specific to exam level (EMR vs EMT vs Paramedic)
- Cross-reference what's in/out of scope

---

## Future Expansion Guidelines

### Critical Care / Air Care (Tier 3)

**When to add CCP/ACP support:**
- After EMR/EMT/Paramedic are solid and tested
- When there's clear demand from user base
- When resources allow without compromising core levels

**How to add CCP/ACP:**
- Extend existing system (don't rebuild)
- Add advanced scope skills incrementally
- Create advanced scenarios (ventilator, ECMO, etc.)
- Maintain backward compatibility

**What NOT to do:**
- Don't prioritize CCP/ACP over core levels
- Don't build features only CCP/ACP can use
- Don't let advanced features bloat the system

---

## Quality Over Feature Creep

**Project values:**
1. **Multi-level support** (EMR/EMT/Paramedic)
2. **Medical accuracy** (realistic, evidence-based)
3. **Educational effectiveness** (students actually learn)
4. **Usability** (easy to set up and use)
5. **Maintainability** (sustainable codebase)

**Feature rejection criteria:**
- Only works for one cert level (unless easily adapted)
- Too complex to maintain
- Minimal educational value
- Bloats system without clear benefit

---

## Project Origin - Remember the Why

**EMSTrainer was built because:**
- Instructor made impossible test → students failed
- Student (Joel) got pissed → built better training system
- Revenge motivation → comprehensive educational platform

**Core motivation:** Help students actually learn and pass, not just memorize.

**This means:**
- Realistic scenarios across all cert levels
- Immediate feedback that teaches
- Practice that builds competence
- Accessible to students at all levels (EMR through Paramedic)

---

## Decision Framework

When making project decisions, ask:

1. **Does this serve EMR, EMT, AND Paramedic students?**
   - Yes → Consider it
   - No → Can it be adapted? If not, reconsider

2. **Does this improve educational outcomes?**
   - Yes → Priority consideration
   - No → Probably reject

3. **Is this sustainable to maintain?**
   - Yes → Good to build
   - No → Will it cause technical debt?

4. **Does this align with project mission?**
   - Multi-level support
   - Realistic training
   - Evidence-based education
   - Accessible and usable

---

## Living Document

This philosophy document should be:
- Referenced when planning features
- Updated when core principles evolve
- Used to evaluate pull requests
- Cited when rejecting scope creep

**Last major update:** 2025-12-21 (Multi-level support clarified as core tenet)

---

**Remember:** EMSTrainer serves the full spectrum of EMS education from first responders to paramedics. Every decision should honor that mission.
