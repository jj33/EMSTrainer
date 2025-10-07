================================================================================
EMSTrainer v1.6.0 - Student Package
================================================================================

Welcome! This package contains everything you need to practice EMS scenarios
and improve your skills.

================================================================================
QUICK START (5 minutes)
================================================================================

Step 1: Open GPT-5
  - Use GitHub Copilot (recommended) or ChatGPT
  - Make sure GPT-5 is enabled (medical accuracy required)

Step 2: Load the prompts (drag and drop into chat)
  a) Drag: EMSTrainer_Core.txt
  b) Drag: EMSTrainer_Scenario_Mode.txt

Step 3: Get your scenario from instructor
  - Your instructor will email you a scenario file
  - Drag that file into the chat

Step 4: Run the scenario!
  Type: "Start scenario"
  
That's it! Follow the prompts and practice your skills.

================================================================================
WHAT'S INCLUDED
================================================================================

PROMPT FILES:
  - EMSTrainer_Core.txt ................. Foundation system
  - EMSTrainer_Scenario_Mode.txt ........ Scenario player

DOCUMENTATION:
  - Student_Quick_Start_Guide.md ........ Step-by-step instructions
  - WHATS_NEW_v1.6.0.md ................. What's new in this version
  - README_STUDENT.txt .................. This file

================================================================================
WHAT YOU CAN DO
================================================================================

RUN SCENARIOS:
  Your instructor assigns scenarios, you complete them
  
  1. Load scenario file from instructor
  2. Type: "Start scenario"
  3. Make clinical decisions
  4. Document your care (SOAP notes)
  5. Get automatic feedback
  6. Submit results to instructor

PRACTICE MODES:
  - Easy: Learning mode, hints provided, no penalties
  - Standard: Realistic NREMT-level practice
  - Hard: Challenge mode for advanced practice
  - Monica: Extreme difficulty (brutal!)

GENERATE STUDY MATERIALS:
  "Create study guide on [topic]"
  "Generate practice questions on [topic]"

UPLOAD TEST RESULTS:
  "I got these PlatinumPlanner results: [paste results]"
  "Generate targeted practice questions on my weak areas"

================================================================================
HOW TO USE
================================================================================

STEP 1 - LOAD SCENARIO:
  Instructor sends you a scenario file (scenario_xxx.json)
  Drag it into your GPT-5 chat

STEP 2 - START:
  Type: "Start scenario"
  Read the initial patient presentation

STEP 3 - MAKE DECISIONS:
  The AI asks: "What would you like to do?"
  You respond with your clinical actions:
    - "Assess airway, breathing, circulation"
    - "Apply oxygen via NRB at 15 LPM"
    - "Start IV, normal saline"
    - "Check vitals"
    - "Document findings"

STEP 4 - FOLLOW THE FLOW:
  - Patient vitals update based on your care
  - Time passes (scenarios have time limits!)
  - Equipment may fail (depending on difficulty)
  - Scene may change
  - You must adapt and treat

STEP 5 - DOCUMENT:
  When ready to complete:
    "I want to document and submit"
  
  Write your SOAP note:
    S: Subjective (what patient/bystanders say)
    O: Objective (vitals, findings)
    A: Assessment (your clinical impression)
    P: Plan (what you did, transport decision)

STEP 6 - GET FEEDBACK:
  AI provides:
    - Your score and grade
    - What you did well
    - What to improve
    - Timing analysis
    - Export file for instructor

STEP 7 - SUBMIT:
  Copy the JSON output
  Save as a file
  Email to your instructor

================================================================================
DIFFICULTY MODES
================================================================================

EASY MODE (Learning):
  ✓ Hints when you're stuck
  ✓ No time penalties
  ✓ Supportive feedback
  ✓ Forgiving vitals
  ✓ No equipment failures
  → Perfect for first time learning

STANDARD MODE (NREMT-level):
  ✓ Realistic timing graded
  ✓ Balanced support
  ✓ Realistic vitals
  ✓ 10-15% equipment failure rate
  → Normal practice and certification prep

HARD MODE (Challenge):
  ✓ Strict timing with penalties
  ✓ Minimal hints
  ✓ Challenging vitals
  ✓ 20-25% equipment failure rate
  → Advanced practice and pre-test

MONICA MODE (Extreme):
  ✓ Hard fail on timeout
  ✓ No hints
  ✓ Aggressive decompensation
  ✓ 30-35% equipment failure rate
  ✓ Guaranteed curveballs
  → For experienced providers only!

================================================================================
GRADING
================================================================================

Your performance is scored on:

INTERVENTIONS (40-50 points):
  - Did you take appropriate actions?
  - Were they timely?
  - Did you follow protocols?

ASSESSMENT (15-20 points):
  - Did you assess the patient thoroughly?
  - Did you identify critical findings?

COMMUNICATION (10-15 points):
  - Did you give clear orders to your partner?
  - Did you contact medical control when needed?

DOCUMENTATION (15 points):
  - Is your SOAP note complete?
  - Did you document times and interventions?

HIDDEN CRITERIA (35 points):
  - Some grading criteria aren't told to you upfront
  - You'll discover them through feedback
  - Examples: 5 Rights, AIDET, scene safety reassessment

TOTAL: 100 points possible

================================================================================
TIPS FOR SUCCESS
================================================================================

BEFORE STARTING:
  ✓ Review protocols for scenario type
  ✓ Have reference materials handy
  ✓ Find a quiet place to focus
  ✓ Budget enough time (scenarios: 10-30 minutes)

DURING SCENARIO:
  ✓ Scene safety FIRST (and reassess continuously!)
  ✓ Follow systematic assessment (ABC's)
  ✓ Verbalize your actions clearly
  ✓ Check vitals regularly
  ✓ Communicate with your partner
  ✓ Document as you go (mental notes)
  ✓ Watch the clock

COMMUNICATION:
  ✓ Use AIDET: Acknowledge, Introduce, Duration, Explanation, Thank you
  ✓ Give clear orders to partner
  ✓ Use closed-loop communication
  ✓ Consider patient/family

MEDICATIONS:
  ✓ Always check 5 Rights:
    - Right Patient
    - Right Drug
    - Right Dose
    - Right Route
    - Right Time
  ✓ Verbalize each check

DOCUMENTATION:
  ✓ Use proper SOAP format
  ✓ Include times for key interventions
  ✓ Be thorough but concise
  ✓ Document your clinical reasoning

AFTER SCENARIO:
  ✓ Review your debrief carefully
  ✓ Note what you did well
  ✓ Focus on areas for improvement
  ✓ Ask instructor questions
  ✓ Practice weak areas

================================================================================
TIMING STANDARDS
================================================================================

Know these critical time windows:

IMMEDIATE (<60 seconds):
  - CPR initiation

URGENT (<2-3 minutes):
  - Defibrillation
  - Oxygen for hypoxia
  - Epinephrine for anaphylaxis

IMPORTANT (<5 minutes):
  - IV access (critical patients)
  - Advanced airway (if needed)
  - Blood glucose check (altered mental status)

SCENE TIME:
  - Medical: ≤10 minutes target, 15 max
  - Trauma (load-and-go): <10 minutes

Note: Timing enforced based on difficulty mode

================================================================================
COMMON MISTAKES TO AVOID
================================================================================

✗ Skipping scene safety assessment
✗ Not reassessing scene safety during care
✗ Forgetting to check vitals regularly
✗ Missing critical timing windows
✗ Not verbalizing 5 Rights for medications
✗ Incomplete SOAP documentation
✗ Not giving partner clear directions
✗ Forgetting to update patient/family
✗ Tunnel vision (missing other problems)
✗ Not adapting when equipment fails

================================================================================
NEED HELP?
================================================================================

1. Read: Student_Quick_Start_Guide.md (detailed instructions)
2. Ask: Your instructor for guidance
3. Review: What's New doc for v1.6.0 features
4. Practice: Start with Easy mode, work up to Standard

Common questions:
  "What should I do next?" → Think systematically (ABC's)
  "How much time do I have left?" → AI will tell you
  "Can I restart?" → Ask your instructor for permission
  "What if equipment fails?" → Adapt! Use backup equipment/techniques

================================================================================
TROUBLESHOOTING
================================================================================

Q: Can't load scenario file?
A: Make sure using GPT-5. Drag file (don't copy/paste). Load Core.txt first.

Q: AI won't start scenario?
A: Check you loaded both prompt files. Type exact command: "Start scenario"

Q: Lost my place in scenario?
A: Type: "Where am I in the scenario? What just happened?"

Q: Don't know what to do?
A: Think systematically. Start with ABCs. Ask AI for hints (Easy mode).

Q: Time ran out?
A: That's part of learning! Review debrief, focus on efficiency next time.

================================================================================
VERSION INFORMATION
================================================================================

Version: 1.6.0
Released: January 2025
Tested: 30-student stress test (100% validation)

Features in this version:
  ✓ 4 difficulty modes
  ✓ Dynamic vitals that respond to your care
  ✓ Equipment failures (realistic scenarios)
  ✓ Continuous scene safety assessment
  ✓ Hidden grading criteria
  ✓ Detailed feedback and debriefs
  ✓ Study guide generation
  ✓ Practice question generation

================================================================================

Good luck with your training! 🚑 You've got this!

