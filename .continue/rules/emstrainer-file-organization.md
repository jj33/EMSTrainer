---
description: Use when organizing files, creating new documents, or doing
  repository cleanup in EMSTrainer
alwaysApply: false
---

EMSTrainer repository structure rules:

1. Directory purposes:
   - /prompts/ = Production prompt files only
   - /docs/ = Public-facing documentation only
   - /internal/ = All dev notes, session notes, internal planning (gitignored)
   - /planning/ = Feature planning, architecture docs (tracked in git)
   - /examples/ = Example scenarios, sample files for users

2. Internal vs Planning distinction:
   - internal/ = Temporary dev work, session notes, chat context (never commit)
   - planning/ = Permanent architecture docs, feature specs (commit these)

3. Documentation file naming:
   - User guides: [Role]_[Type]_Guide.md (e.g., Student_Quick_Start_Guide.md)
   - Internal notes: SESSION_NOTES_[date].md
   - Feature docs: [Feature]_Document.md

4. Before committing: Verify no internal/ files leaked into docs/ or planning/

5. Keep .gitignore simple: just "internal/" not scattered patterns