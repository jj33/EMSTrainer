---
description: Use when updating version numbers or releasing new versions of EMSTrainer
alwaysApply: false
---

When updating EMSTrainer versions:

1. Version numbers must be synchronized across:
   - All prompt files (Core, Student_Interface, Instructor_Interface)
   - CHANGELOG.md
   - Any release notes
   - Package README files
   - Documentation that references version

2. Version format: MAJOR.MINOR.PATCH (e.g., 1.6.1)
   - MAJOR: Breaking architecture changes
   - MINOR: New features, backward compatible
   - PATCH: Bug fixes, hotfixes

3. Always update CHANGELOG.md with:
   - What changed
   - Why it changed
   - Migration notes if breaking

4. For hotfixes: Clearly mark as HOTFIX in release notes

5. Test with actual prompt loading before releasing