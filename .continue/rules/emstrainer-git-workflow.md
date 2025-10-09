---
description: Use when committing changes, creating releases, or managing
  branches in EMSTrainer
alwaysApply: false
---

EMSTrainer git and release workflow:

1. Branch strategy:
   - main = production releases only
   - dev = active development (not currently used, but available)
   - Work directly on main for hotfixes
   - Use branches for major features

2. Commit practices:
   - Clear commit messages describing what changed
   - Group related changes together
   - Don't commit internal/ directory contents

3. Before pushing:
   - Run git status to verify changes
   - Check no .DS_Store or temp files
   - Verify .gitignore working correctly

4. Release process:
   - Update all version numbers
   - Update CHANGELOG.md
   - Create release notes
   - Tag release: v1.6.1
   - Build deployment packages
   - Generate PDFs via GitHub Actions
   - Test packages before publishing

5. Hotfix process:
   - Branch from main (or work on main directly)
   - Fix critical issue
   - Test thoroughly
   - Fast-track release
   - Clearly mark as HOTFIX