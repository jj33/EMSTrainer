---
description: Use when modifying prompt files or adding new features to EMSTrainer
alwaysApply: false
---

EMSTrainer v1.6.1+ architecture rules:

1. Three-file structure (never mix):
   - Core.txt = ALL shared configuration (provider levels, difficulty modes, grading, timing)
   - Student_Interface.txt = Student UI and workflows only
   - Instructor_Interface.txt = Instructor UI and workflows only

2. Loading rules:
   - Students: Core + Student_Interface ONLY
   - Instructors: Core + Instructor_Interface ONLY
   - NEVER load both interfaces together

3. When adding features:
   - Shared config/data → goes in Core.txt
   - Student-facing UI → goes in Student_Interface.txt
   - Instructor-facing UI → goes in Instructor_Interface.txt

4. Test both loading combinations separately to ensure no role confusion

5. Any data needed by BOTH students and instructors MUST be in Core.txt

6. Interfaces should reference Core sections, not duplicate them