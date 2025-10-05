# EMSTrainer

## Continuous Integration: Validate Examples & Exports

We now have a GitHub Actions workflow (`.github/workflows/validate.yml`) that runs on every pull request to the `dev` branch.

### What it does
- **Validate job**: Runs `make validate` to check all JSON, CSV, and Markdown files under `examples/` and `exports/`.
- **Exports smoke test**: Runs `make exports` to generate demo ACS export files (MD + CSV) and uploads them as artifacts.

### Why it matters
This ensures that broken example files or export logic never reach `dev`. If validation fails, the PR cannot be merged.

### How to check locally
Before pushing your changes:

```bash
make validate   # Validate examples and exports
make exports    # Generate demo export files
```

If either command fails, fix the issues before committing.
