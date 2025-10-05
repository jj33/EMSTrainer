# EMSTrainer Development Workflow

---

## Table of Contents
- [Branching Strategy](#branching-strategy)
- [Typical Workflow](#typical-workflow)
- [Feature Branch Workflow (Optional)](#feature-branch-workflow-optional)
- [Commit Message Guidelines](#commit-message-guidelines)
- [.gitignore Conventions](#gitignore-conventions)
- [Quick Reference Commands](#quick-reference-commands)
- [Pushing to GitHub](#pushing-to-github)
- [Polish](#polish)
- [Extra Notes](#extra-notes)

---

## Branching Strategy
- **main**: stable, production-ready
- **dev**: day-to-day development
- **feature/***: optional experimental branches for new features

---

## Typical Workflow
1. Switch to `dev`
2. Make changes
3. Stage and commit changes
4. Push to remote
5. Merge into `main` when stable

---

## Feature Branch Workflow (Optional)
- Create `feature/<name>` from `dev`
- Commit and push changes
- Merge back into `dev` and delete the feature branch

---

## Commit Message Guidelines
- Use short, descriptive, present tense messages
- Examples:
  - `Add LICENSE file and custom badge`
  - `Update README with workflow notes`

---

## .gitignore Conventions
Exclude:
- macOS junk files
- IDE settings
- Logs and temp files
- Python/Node/Ruby clutter
- Test coverage artifacts

---

## Quick Reference Commands
- `git checkout <branch>`
- `git pull`
- `git push`
- `git merge <branch>`

---

## Pushing to GitHub
- Initialize repo: `git init`
- Add remote: `git remote add origin <URL>`
- First push: `git push -u origin dev`
- Merge/push `main` when stable

---

## Polish
- Include a Table of Contents with auto-links
- Maintain clean heading hierarchy
- Use horizontal rules for readability

---

## Extra Notes
- Always pull latest changes before starting work
- Resolve merge conflicts promptly
- Keep commits atomic (one logical change per commit)
