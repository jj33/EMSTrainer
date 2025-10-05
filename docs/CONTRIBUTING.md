# Contributing to EMSTrainer

Thanks for your interest in contributing! This project organizes EMS training materials by version and format. Here's how to add new content or update existing files.

## Adding a New Version

1. Create a new folder:

       docs/imports/vX.Y.Z/

2. Drop in raw files (Pages, PDFs, etc.)

3. Run the cleanup script:

       ./scripts/cleanup-import.sh vX.Y.Z --apply

4. Convert any `.docx` files to `.pages` manually and move them to `docs/source/`

5. Commit your changes:

       git checkout -b import/vX.Y.Z-clean
       git add .
       git commit -m "import: vX.Y.Z baseline (cleaned)"
       git push -u origin import/vX.Y.Z-clean

6. (Optional) Tag the version:

       git tag vX.Y.Z-cleanup
       git push origin vX.Y.Z-cleanup

## Guidelines

- Use `.pages` format for editable documents
- Use `.pdf` for finalized exports
- Avoid committing `.docx` — convert to `.pages` first
- Keep version folders clean and organized
- Don’t commit macOS system files (see `.gitignore`)

## Testing Your Import

Before committing, run the cleanup script in dry-run mode to preview changes:

    ./scripts/cleanup-import.sh vX.Y.Z

## Questions?

Open an issue or contact the maintainer if you're unsure about anything.
