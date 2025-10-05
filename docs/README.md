# EMSTrainer Documentation

This folder contains structured documentation and study materials for the EMSTrainer project. Content is organized by version and file type to support clean imports, updates, and historical tracking.

## Versioned Imports

Imported materials are stored under:

    docs/imports/<version>/

Example:

    docs/imports/v1.5.2/

Each version folder contains raw files copied from external sources. These are cleaned and routed using the `cleanup-import.sh` script.

## Cleanup Workflow

To organize a new version:

1. Copy raw files into `docs/imports/<version>/`
2. Run the cleanup script:

       ./scripts/cleanup-import.sh <version> --apply

3. Convert any `.docx` files to `.pages` manually and move them to `docs/source/`
4. Commit changes on a branch and push

## File Routing

After cleanup, files are moved to:

| File Type     | Destination Folder         | Purpose                          |
|---------------|----------------------------|----------------------------------|
| `.pages`      | `docs/source/`             | Editable source documents        |
| `.pdf`        | `assets/`                  | Finalized or exported materials  |
| `.docx`       | `docs/needs-convert/`      | Quarantined until converted      |
| Old versions  | `docs/archive/<version>/`  | Historical backups               |

## Version Tags

Each cleaned version may be tagged for reference:

- `v1.5.2-cleanup`
- `v1.6.0-cleanup`

Use Git tags to compare versions or roll back if needed.

## Tools

- `scripts/cleanup-import.sh` — organizes and routes imported files
- `.gitignore` — filters out macOS system files and editor artifacts

## .gitignore Highlights

This project ignores common macOS and editor artifacts:

    # macOS system files
    .DS_Store
    .AppleDouble
    .LSOverride
    Icon?
    ._*
    .Spotlight-V100
    .Trashes
    .fseventsd
    .VolumeIcon.icns
    *.icloud
    *.icloud*

    # Pages and Office artifacts
    *.pages~
    *.docx~
    *.tmp
    ~$*

    # VS Code
    .vscode/

    # Xcode
    *.xcuserstate
    *.xcworkspace
    *.xcodeproj
    *.xcassets
    DerivedData/
    build/
    *.pbxuser
    *.mode1v3
    *.mode2v3
    *.perspectivev3

    # Git
    *.orig
    *.rej
    *.swp
    *.swo

    # Logs and temp
    *.log
    *.bak
    *.tmp
    *.temp
    *.cache

    # Node / Python / Ruby (if used)
    node_modules/
    .env
    __pycache__/
    *.pyc
    *.pyo
    *.rbc
    .bundle/

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to submit new materials or updates.
