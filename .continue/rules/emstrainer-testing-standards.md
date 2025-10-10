---
description: Use before releasing any EMSTrainer version or when validating changes
alwaysApply: false
---

Before releasing EMSTrainer updates:

1. Test all loading combinations:
   - Core + Student_Interface (run scenario, test mode, study mode)
   - Core + Instructor_Interface (create scenario, grade submission)
   - Verify NO role confusion

2. Test all difficulty modes:
   - Easy (learning, forgiving)
   - Standard (NREMT-level)
   - Hard (challenging)
   - Monica (extreme, all features forced on)

3. Validate key features:
   - Scenario loading and execution
   - Vitals trending
   - Grading rubrics
   - Debrief generation
   - Hash validation

4. Check documentation matches code:
   - Loading instructions correct
   - Version numbers synchronized
   - Examples work as documented

5. Run regression baseline if available (tests/ directory)

6. Test with actual AI models (GPT-5 for medical, Claude for dev)