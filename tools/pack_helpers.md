# Pack Helpers

- Author a scenario using `/scenario.*` commands in the Instructor prompt.
- Use `/scenario.lock secret=<InstructorSecret>` to encrypt to `.emsx`.
- Collect a submission and decrypt via `/submission.load b64=<payload> filename=<...>.subx secret=<InstructorSecret>`.
- Always verify via `/submission.verify` before grading.
- Run `/grade.auto rubric=embedded policy=default`, then `/grade.export format=md`.

