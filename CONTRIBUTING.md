# Contributing to EMSTrainer

Thank you for helping improve EMSTrainer! Please follow these guidelines:

## Pre-push Checklist
- Run `make validate` to ensure all example and export files pass basic validation.
- Run `make exports` to confirm the export logic works and demo files are generated.

## Continuous Integration
Every pull request to `dev` triggers a GitHub Actions workflow:
- **Validate job**: Checks JSON, CSV, and Markdown files.
- **Exports smoke test**: Generates demo ACS export files and uploads them as artifacts.

If these checks fail, your PR cannot be merged. Running the commands locally before pushing saves time.

## Branching
- Create feature branches from `dev`.
- Use descriptive names like `fix/make-validate-exports` or `feature/instructor-scenarios`.

## Pull Requests
- Open PRs against `dev`.
- Include a clear description of changes and any new files added.
