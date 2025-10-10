# EMSTrainer Instructor Reference Guide

**Version:** 1.6.0  
**For:** EMS Instructors using EMSTrainer  
**Keep this open while working!**

---

## Quick Setup Checklist

- [ ] GPT-5 enabled in Copilot or ChatGPT
- [ ] Load EMSTrainer_Core.txt (drag and drop)
- [ ] Load EMSTrainer_Instructor_Prompt.txt (drag and drop)
- [ ] Optional: Load EMSTrainer_Scenario_Mode.txt for scenarios
- [ ] Test: Type "Ready to create scenarios"

---

## Common Commands Reference

### Creating Scenarios
"Create [type] scenario for [level] students, [difficulty] mode"

Examples:
- "Create cardiac arrest scenario for paramedic students, Standard difficulty"
- "Create trauma scenario for EMT students, Easy mode"
- "Create respiratory distress for AEMT, Hard mode with equipment failure"

### Test Questions
"Generate [N] questions on [topic] for [level] students"

Examples:
- "Generate 10 questions on ALS airway for paramedics"
- "Generate 20 NREMT-level questions: 10 cardiac, 5 trauma, 5 respiratory"

### Study Guides
"Create study guide on [topic] for [level] students"

### Deployment
"Format this scenario for email to: [student names]"

### Grading
"Grade this submission: [paste student JSON]"
"Generate class summary for all submissions"


## Difficulty Levels Quick Reference

| Mode | Purpose | Timing | Support | Equipment Failures |
|------|---------|--------|---------|-------------------|
| Easy | Learning | No penalties | Hints provided | None |
| Standard | NREMT-level | Graded | Balanced | 10-15% |
| Hard | Challenge | Penalized | Minimal | 20-25% |
| Monica | Extreme | Hard fail | None | 30-35% |

**When to use:**
- Easy: New students, first exposure to topic
- Standard: Regular training, certification prep
- Hard: Advanced students, pre-test prep
- Monica: Experienced providers only (warning: brutal!)

---

## Provider Levels Available

- EMR (Emergency Medical Responder)
- EMT (Emergency Medical Technician)
- AEMT (Advanced EMT)
- Paramedic
- ACP (Advanced Care Paramedic / Air Care)
- CCP (Critical Care Paramedic)

---

## Creating Your First Scenario (Step-by-Step)

Step 1: Tell AI what you want
"Create a respiratory distress scenario for EMT students, Standard difficulty"

Step 2: AI asks clarifying questions
- Specific cause?
- Learning objectives?
- Curveballs?
- Time limit?

Step 3: Answer the questions

Step 4: AI generates scenario - Review and adjust

Step 5: Save the scenario as JSON file


## Grading Categories Explained

Standard Grading Rubric (100 points):

- Interventions (40-50 pts): Actions taken, timing, appropriateness
- Assessment (15-20 pts): Patient evaluation completeness
- Communication (10-15 pts): Partner orders, medical control
- Documentation (15 pts): SOAP note quality

Hidden Criteria (not told to students):
- 5 Rights medication check (10 pts)
- AIDET communication (10 pts)
- Scene safety reassessment (15 pts)

Students discover these through debriefs!

---

## Timing Standards Reference

Critical Interventions:
- CPR initiation: <60 seconds
- Defibrillation: <2 minutes
- Epinephrine (anaphylaxis): <3 minutes (target), <5 min (max)
- Oxygen (hypoxia): <3 minutes
- IV access (critical): <5 minutes

Transport Decisions:
- On-scene time (medical): Target ≤10 min, Max 15 min
- On-scene time (trauma): Target <10 min (load-and-go)

---

## Common Instructor Tasks

Weekly Skills Check:
"Create 5-question quiz on this week's protocols"

Pre-Shift Scenario:
"Generate quick respiratory scenario, under 10 minutes, Standard mode"

Remediation Training:
"Student failed airway management. Create Easy mode airway scenario with guidance"

NREMT Prep:
"Generate 50-question NREMT-level test covering all topics"


## Troubleshooting

**Scenario seems too easy/hard:**
- Explicitly state difficulty when creating
- Test with 1-2 students first

**Auto-grade seems off:**
- Review grading rubric
- Check hidden criteria
- Manually adjust if needed

**Students confused:**
- Use AI-provided email templates
- Reference Student Quick Start Guide
- Do a demo run-through first

---

## Tips for Success

Scenario Creation:
1. Start simple - Use examples, then modify
2. Focus learning - 2-3 objectives max
3. Match difficulty to student experience
4. Test first - Run it yourself
5. Use Monica sparingly - It's brutal!

Assessment:
1. Target weaknesses from test results
2. Mix difficulty levels
3. Provide immediate feedback
4. Track progress over time

Grading:
1. Review auto-grades before releasing
2. Add personal notes
3. Be consistent with rubrics
4. Use summaries for class trends

---

## File Organization Recommended

instructor_workspace/
├── scenarios_created/
├── deployed_to_class/
├── student_submissions/
└── graded_reports/

---

*Keep this guide handy while using EMSTrainer!*  
*Version 1.6.0 | Updated 2025-01-07*
