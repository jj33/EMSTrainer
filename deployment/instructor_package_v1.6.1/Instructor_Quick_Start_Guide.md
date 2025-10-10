# EMSTrainer - Instructor Quick Start Guide

**Version:** 1.6.1  
**Date:** October 10, 2025  
**For:** EMS Instructors and Training Officers

---

## Overview

EMSTrainer helps you create, deploy, and grade training scenarios and assessments without technical knowledge. Everything is done through natural conversation with AI.

---

## What You Can Do

### Scenario Management:
- Create custom scenarios from scratch
- Deploy scenarios to students
- Collect and auto-grade submissions
- Generate performance summaries

### Assessment Creation:
- Generate test questions on specific topics
- Create study guides for students
- Customize difficulty levels
- Track student progress

---

## Getting Started

### Prerequisites:
- GPT-5 enabled in Copilot/ChatGPT (medical accuracy required)
- Access to prompt files from repository
- Student list (names or IDs)

### Setup (2 steps):

**Step 1:** Load Core.txt
- Drag `prompts/EMSTrainer_Core.txt` into Copilot/ChatGPT

**Step 2:** Load Scenario Mode (if creating scenarios)
- Drag `prompts/EMSTrainer_Scenario_Mode.txt`

---

## Creating Scenarios

### Simple Method (AI Generates):

```
"Create a cardiac arrest scenario for paramedic students, 
Standard difficulty, with focus on ACLS protocol"
```

AI will generate complete scenario JSON with:
- Patient presentation
- Initial vitals
- Expected interventions
- Grading rubric
- Timing standards

### Advanced Method (Customize):

```
"Create a trauma scenario with these details:
- 25-year-old male, MVC
- Chest trauma with tension pneumothorax
- Monica Mode difficulty
- Add curveball at 8 minutes
- Include equipment failure"
```

### Using Example Scenarios:

Load example from `examples/` folder and modify:
```
[Drop scenario_cardiac_arrest_vf.json into chat]
"Change this to Hard mode and add a second patient curveball"
```

---

## Deploying to Students

### Option A: Email Distribution

```
"Format this scenario for email distribution to: 
John Smith, Sarah Jones, Mike Chen"
```

AI creates email template with:
- Student-specific versions
- Instructions
- Due date field
- Scenario JSON

### Option B: File Distribution

```
"Create individual scenario files for each student with tracking"
```

AI generates:
- Separate JSON files per student
- Tracking spreadsheet
- Deployment instructions

---

## Grading Submissions

### Auto-Grading:

```
"Grade this submission: [paste student JSON]"
```

AI provides:
- Score breakdown by category
- Timing analysis
- Strengths and weaknesses
- Recommended feedback

### Class Summary:

```
"Generate class summary for all submissions"
```

AI creates:
- Average scores by category
- Common mistakes
- Performance trends
- Recommendations for instruction

---

## Creating Tests & Study Guides

### Custom Test Questions:

```
"Generate 20-question test on:
- Cardiology (10 questions)
- Trauma (5 questions)  
- Airway (5 questions)
NREMT difficulty level"
```

### Study Guide Generation:

```
"Create study guide on advanced airway management 
for paramedic students"
```

### Topic-Specific:

```
"Generate test on BLS airway for EMT students"
"Create study guide on pediatric respiratory emergencies"
```

---

## Difficulty Levels Explained

**Easy:** Learning-focused, supportive, no penalties
**Standard:** NREMT-level, realistic, balanced
**Hard:** Challenging, strict timing, complex
**Monica:** Extreme difficulty, maximum stress (use sparingly!)

---

## Example Scenarios Included

Located in `examples/` folder:

1. **scenario_cardiac_arrest_vf.json**
   - Standard ACLS scenario
   - Good for initial training

2. **scenario_mvc_trauma_monica.json**  
   - Monica Mode example
   - Multiple curveballs
   - Environmental stressors

Use these as templates or modify as needed.

---

## File Organization

Recommended structure:
```
instructor_workspace/
├── scenarios/          (your created scenarios)
├── deployed/          (scenarios sent to students)
├── submissions/       (student results)
└── reports/          (graded summaries)
```

---

## Tips for Effective Use

### Scenario Creation:
1. Start with examples, then customize
2. Match difficulty to student level
3. Focus on 2-3 learning objectives per scenario
4. Use Monica Mode sparingly (it's brutal!)

### Assessment:
1. Test on specific weak areas
2. Mix difficulty levels
3. Provide immediate feedback
4. Track progress over time

### Grading:
1. Review auto-grades before releasing
2. Add personal notes when needed
3. Focus on teaching, not just scoring
4. Use summaries to identify class trends

---

## Common Instructor Tasks

### Weekly Skills Check:
```
"Create 5-question quiz on last week's protocols"
```

### Pre-Shift Scenarios:
```
"Generate quick Standard mode respiratory scenario, 
under 10 minutes"
```

### Remediation:
```
"Student failed airway management. Create Easy mode 
airway scenario with step-by-step guidance"
```

### Progress Tracking:
```
"Compare John's scores from last month to this month"
```

---

## Troubleshooting

**Issue:** Scenario too easy/hard for students
**Fix:** Explicitly state difficulty level when creating

**Issue:** Auto-grade seems incorrect  
**Fix:** Review rubric, adjust manually, provide feedback to improve future grading

**Issue:** Students confused by instructions
**Fix:** Use provided email templates, add local context

---

## Advanced Features (Coming Soon)

- Scenario encryption (v1.7)
- In-prompt scenario editor (v1.7)
- Equipment timing delays (LUCAS, EtCO2, etc.)
- Instructor dashboard (v1.8)
- LMS integration (v1.9)

---

## Support Resources

- Student Quick Start Guide (for reference)
- Example scenarios (in `examples/` folder)
- Planning documents (feature roadmap)
- README.md (project overview)

---

## Quick Reference Commands

```
"Create [type] scenario for [level] students"
"Generate [N] test questions on [topic]"
"Deploy scenario to [students]"
"Grade this submission"
"Generate class summary"
"Create study guide on [topic]"
"Change scenario to [difficulty] mode"
"Add curveball at [time]"
```

---

## Getting Help

Contact project maintainer or review:
- `planning/` folder for features and status
- `docs/` folder for detailed documentation  
- Repository issues for bug reports

---

*EMSTrainer v1.6.1 - Instructor Quick Start Guide*  
*Updated: October 10, 2025*


*EMSTrainer v1.6.1 - Instructor Quick Start Guide*  
*Updated: October 10, 2025*
