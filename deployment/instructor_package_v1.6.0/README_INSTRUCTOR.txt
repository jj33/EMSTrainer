================================================================================
EMSTrainer v1.6.0 - Instructor Package
================================================================================

Welcome! This package contains everything you need to use EMSTrainer as an

Copyright © 2025 Joel Jameson
FREE for individual instructors. Institutional licensing available.

EMS instructor.

================================================================================
QUICK START (5 minutes)
================================================================================

Step 1: Open GPT-5
  - Use GitHub Copilot (recommended) or ChatGPT
  - Make sure GPT-5 is enabled (required for medical accuracy)

Step 2: Load the prompts (drag and drop into chat)
  a) Drag: EMSTrainer_Core.txt
  b) Drag: EMSTrainer_Instructor_Prompt.txt
  c) Optional: EMSTrainer_Scenario_Mode.txt (for creating scenarios)

Step 3: Test it!
  Type: "Create a cardiac arrest scenario for paramedic students"
  
That's it! You're ready to go.

================================================================================
WHAT'S INCLUDED
================================================================================

PROMPT FILES (the AI system):
  - EMSTrainer_Core.txt ..................... Foundation system
  - EMSTrainer_Instructor_Prompt.txt ........ Instructor interface
  - EMSTrainer_Scenario_Mode.txt ............ Scenario creation (optional)

DOCUMENTATION:
  - Instructor_Quick_Start_Guide.md ......... Step-by-step setup
  - Instructor_Reference_Guide.md ........... Quick reference (keep open!)
  - README_INSTRUCTOR.txt ................... This file

EXAMPLES:
  - examples/scenario_cardiac_arrest_vf.json ... Standard scenario
  - examples/scenario_mvc_trauma_monica.json ... Advanced (Monica Mode)

================================================================================
WHAT YOU CAN DO
================================================================================

CREATE SCENARIOS:
  "Create [type] scenario for [level] students, [difficulty] mode"
  
  Examples:
    - "Create respiratory distress for EMT students, Standard difficulty"
    - "Create trauma scenario for paramedics, Hard mode"
    - "Create cardiac arrest with equipment failures, Monica mode"

GENERATE TEST QUESTIONS:
  "Generate [N] questions on [topic] for [level] students"
  
  Examples:
    - "Generate 10 questions on ALS airway for paramedics"
    - "Generate 20 NREMT-level questions: 10 cardiac, 5 trauma, 5 respiratory"
    - "Create easy quiz on BLS skills"

CREATE STUDY GUIDES:
  "Create study guide on [topic] for [level] students"
  
  Examples:
    - "Create study guide on pediatric emergencies for EMT"
    - "Make study guide on advanced airway for paramedics"

DEPLOY TO STUDENTS:
  "Format this scenario for email to: [student names]"

GRADE SUBMISSIONS:
  "Grade this submission: [paste student JSON]"
  "Generate class summary for all submissions"

================================================================================
DIFFICULTY LEVELS
================================================================================

EASY MODE:
  - For: New students, first exposure
  - Features: Hints provided, no penalties, supportive
  - Use when: Teaching fundamentals

STANDARD MODE:
  - For: Regular training, NREMT prep
  - Features: Realistic timing, balanced support
  - Use when: Normal skills practice

HARD MODE:
  - For: Advanced students, challenge
  - Features: Strict timing, equipment failures (20-25%)
  - Use when: Pre-test preparation

MONICA MODE:
  - For: Experienced providers ONLY
  - Features: Extreme difficulty, hard fail on timeout, 30-35% failures
  - Use when: Humbling overconfident "paragods"
  - WARNING: Brutal! Use sparingly!

================================================================================
PROVIDER LEVELS
================================================================================

  - EMR (Emergency Medical Responder)
  - EMT (Emergency Medical Technician)
  - AEMT (Advanced EMT)
  - Paramedic
  - ACP (Advanced Care Paramedic / Air Care)
  - CCP (Critical Care Paramedic)

Match to your students' certification level.

================================================================================
EXAMPLE WORKFLOW
================================================================================

1. CREATE A SCENARIO:
   You: "Create respiratory distress scenario for EMT students, Standard difficulty"
   AI: [asks clarifying questions]
   You: [answer questions]
   AI: [generates complete scenario JSON]

2. DEPLOY TO STUDENTS:
   You: "Format this for email to: John, Sarah, Mike"
   AI: [creates email template with instructions]
   You: [copy/paste into your email, send]

3. COLLECT SUBMISSIONS:
   Students complete scenarios and send you their results JSON files

4. GRADE SUBMISSIONS:
   You: "Grade this submission: [paste student JSON]"
   AI: [provides detailed grading and feedback]

5. CLASS SUMMARY:
   You: "Generate class summary for all submissions"
   AI: [analyzes class performance, recommends focus areas]

================================================================================
TIPS FOR SUCCESS
================================================================================

SCENARIO CREATION:
  ✓ Start with examples, then modify
  ✓ Focus on 2-3 learning objectives per scenario
  ✓ Match difficulty to student experience
  ✓ Test scenarios yourself first
  ✓ Use Monica Mode sparingly (it's brutal!)

ASSESSMENT:
  ✓ Target weak areas from test results
  ✓ Mix difficulty levels
  ✓ Provide immediate feedback
  ✓ Track progress over time

GRADING:
  ✓ Review auto-grades before releasing
  ✓ Add personal notes when helpful
  ✓ Be consistent with rubrics
  ✓ Use summaries to identify class trends

================================================================================
GRADING CATEGORIES
================================================================================

Standard rubric (100 points total):
  - Interventions (40-50 pts): Actions, timing, appropriateness
  - Assessment (15-20 pts): Patient evaluation completeness
  - Communication (10-15 pts): Partner orders, medical control
  - Documentation (15 pts): SOAP note quality

Hidden criteria (students discover through debriefs):
  - 5 Rights medication check (10 pts)
  - AIDET communication (10 pts)
  - Scene safety reassessment (15 pts)

================================================================================
TIMING STANDARDS
================================================================================

Critical interventions:
  - CPR initiation: <60 seconds
  - Defibrillation: <2 minutes
  - Epinephrine (anaphylaxis): <3 min target, <5 min max
  - Oxygen (hypoxia): <3 minutes
  - IV access (critical): <5 minutes

Transport decisions:
  - On-scene (medical): ≤10 min target, 15 min max
  - On-scene (trauma): <10 min (load-and-go)

Note: Enforcement varies by difficulty mode

================================================================================
NEED HELP?
================================================================================

1. Read: Instructor_Quick_Start_Guide.md (step-by-step)
2. Reference: Instructor_Reference_Guide.md (quick lookup)
3. Examples: Check examples/ folder for scenario templates
4. Test: Try modifying an example scenario first

Common commands are in the Reference Guide - keep it open!

================================================================================
TROUBLESHOOTING
================================================================================

Q: Scenario seems too easy/hard?
A: Explicitly state difficulty when creating. Test with 1-2 students first.

Q: Auto-grade seems incorrect?
A: Review grading rubric, check hidden criteria, manually adjust if needed.

Q: Students confused by instructions?
A: Use AI-provided email templates, add your own context.

Q: Can't load files?
A: Make sure using GPT-5. Drag files (don't copy/paste). Load Core.txt first.

================================================================================
VERSION INFORMATION
================================================================================

Version: 1.6.0
Released: January 2025
Tested: 30-student stress test (100% validation passed)

Features in this version:
  ✓ 4 difficulty modes (Easy, Standard, Hard, Monica)
  ✓ 6 provider levels (EMR through CCP)
  ✓ Dynamic equipment failures
  ✓ Continuous scene safety assessment
  ✓ Hidden grading criteria
  ✓ Test/study generation
  ✓ Auto-grading with detailed feedback
  ✓ Class performance summaries

Coming in v1.7:
  - Scenario encryption
  - Equipment timing delays
  - In-prompt scenario editor
  - Enhanced reporting

================================================================================
CONTACT & SUPPORT
================================================================================

Questions? Issues? Feedback?
Contact: [Your contact info here]

Project: github.com/jj33/EMSTrainer

================================================================================

Good luck with your class! 🚑

