---
description: Use when starting development work on EMSTrainer project or when
  creating large files
alwaysApply: false
---

When starting a new development session for EMSTrainer:

1. Read session context files from internal/:
   - internal/SESSION_NOTES_[most_recent].md (current work)
   - internal/ACTIVE_TASKS.md (task list)
   - internal/LAST_SESSION.md (previous session summary)

2. Check current git status to understand working changes

3. For large file creation (>200 lines):
   - Use incremental approach with multi_edit
   - Create skeleton file first with create_new_file
   - Add content in logical sections using multi_edit
   - Keep each edit operation under ~200 lines
   - This prevents "Premature Close" errors

4. Test as you go - don't create all files before testing

5. Update internal/SESSION_NOTES_[date].md as work progresses

This ensures continuity between sessions and avoids tool limit issues with large file operations.