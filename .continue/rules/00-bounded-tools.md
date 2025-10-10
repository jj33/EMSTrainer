---
name: Bounded tool usage
description: Prevent multi-tool bursts in VS Code.
alwaysApply: true
---

# Tool Discipline
- Read at most **2 files per turn**.
- Do **not** call `builtin_edit_existing_file` until you produce a short PLAN and get approval.
- Combine changes into **one** edit call per turn.
- Prefer minimal diffs, not full rewrites.

