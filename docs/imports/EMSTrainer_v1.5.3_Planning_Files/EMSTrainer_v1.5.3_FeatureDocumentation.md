# EMSTrainer v1.5.3 – Instructor Scenario Creation

## Overview
This feature allows instructors to define custom training scenarios and receive encrypted student submissions for review and grading.

## Instructor Scenario File
- Format: JSON
- Includes: vitals, curveballs, consult limits, documentation prompts, expected interventions

## Student Submission File
- Format: JSON
- Includes: timestamped actions, SOAP summary, vitals trend, curveball handling

## Security
- Encrypted files
- Timestamped submissions
- Naming convention: `submission_<student_id>_<scenario_id>_<timestamp>.json`

## Auto-Grading
- Based on expected interventions
- SOAP rubric scoring
- Curveball response evaluation
