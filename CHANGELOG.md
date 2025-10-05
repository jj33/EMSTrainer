
# Changelog

All notable changes to this project are documented here. Dates are in YYYY-MM-DD.
## [1.5.6.2] - 2025-10-05

### Highlights
- **Monica Mode integrated** into the canonical student prompt (`prompts/EMSTrainer_Core_Prompt.txt`) with strict timer, guaranteed curveball, aggressive vitals trending, strict peds/OB policy, and partner “on-order-only” behavior.
- **UI Clickables Suppression**: Hard policy to prevent checkboxes/buttons and interactive HTML in outputs, plus tooling to keep it that way.
- **Reproducibility & Debriefing**: Run seed logging, **DLOG** (decision log) / **LATLOG** (latency log) debrief outputs, combined safety scoring, and severity bias controls.

### Added
- **Monica Mode (Integrated)**
  - Timer enforcement with countdown `[T- MM:SS]`, hard stop on timeout with outcome summary.
  - Curveball module: ≥1 guaranteed event within configured window.
  - Aggressive vitals trending; strict peds/OB difficulty policy.
  - Termination timing + Med Director call hooks (when enabled via config).
  - Compressed responses in Monica for high-signal interaction.
- **Linter & CI tools** (to remove UI clickables):
  - `tools/lint_emstrainer_prompts.py` – removes Markdown task-list checkboxes, strips interactive HTML (`<button>`, `<details>`, etc.), and YAML front matter.
  - `tools/run_lint.sh` – local wrapper; supports positional root (`.`).
  - `tools/lint_ci.sh` – CI one-shot; dry-run fails PRs (exit code 2) if changes needed; `--apply` auto-fixes with `.bak`.
- **Config keys** in `assets/instructor_config.json`:
  - `"monica_mode"` and `"monica"` block (timer, curveball window, peds/OB strictness, aggressive trending, compressed responses, termination timing).
  - `"ui_suppression_selfcheck"` to print a single-line header confirming suppression at scenario start.

### Changed
- **Canonical prompt**: `prompts/EMSTrainer_Core_Prompt.txt` updated with:
  - `=== UI & FORMATTING POLICY (No Clickable Boxes) ===`
  - `=== MONICA MODE (Integrated) ===` and feature toggles.
  - Self-check header at start when `ui_suppression_selfcheck` is `true`:
    ```
    [UI-SAFE ✓] Clickables suppressed; task lists disabled; HTML widgets disabled.
    ```

### Fixed
- Removed accidental task-list syntax in prompt outputs that rendered as interactive checkboxes.
- Clarified wording in UI-suppression policy line (“HTML buttons, forms, or interactive widgets.”).

### Docs
- Moved READMEs under **`docs/`**. Only the project root `README.md` remains outside `docs/`.
- Added:
  - `docs/README_Lint_UI_Suppression.md`
  - `docs/README_CI_Lint.md`
  - Archived older guides under `docs/archive/`.

### DevOps / Quality Gates
- **PR Guardrail (recommended)**: Add a GitHub Actions workflow to run `tools/lint_ci.sh --root .` on pull requests, failing if UI clickables are reintroduced. (See `docs/README_CI_Lint.md`.)

### Notes
- If using the Instructor Setup UI for partner names, ensure `assets/emstrainer_partner_names.json` exists and matches the expected schema. A ready-to-use restore file is available upon request.

## [1.5.6.1] - 2025-10-05
### Changed
- **Normal mode**: Latency tracking explicitly **ignored**, regardless of toggles (`latency_tracking.normal_ignored: true`).
### Added
- Docs moved: `docs/TESTING_MONICA_v1.5.6.1.md` as the tester guide.
- Repo layout validator script and expected layout spec under `tools/`.

## [1.5.6] - 2025-10-05
### Added
- **Deterministic seed** for Monica (`module_toggles.monica_seed`).
- **Distractions overlay** forced ON in Monica; toggleable elsewhere.
- **Latency tracking** forced ON in Monica; toggleable elsewhere.
- **Auto-redaction**: Monica debrief objective-only by default.
### Docs
- `TESTING_MONICA_v1.5.6.md` created (now superseded by v1.5.6.1 doc and moved into `docs/`).

## [1.5.5] - 2025-10-05
### Added
- **Monica v2 overlay**: strike system, strict timing enforcement, objective scoring (0–100), minimal feedback.
- Debrief: Timing Summary, Strike Summary, Score breakdown, submission filename.

## [1.5.4] - 2025-10-05
### Added
- **Provider level & partner logic** with scope enforcement; partner acts only when directed.
- **ToR** segment (`arrest_time_to_tor_call`) + Medical Director consult rules.
- **Module toggles** (Curveball, peds/OB defaults, time pressure) and **submission naming**.

