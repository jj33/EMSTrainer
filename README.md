# EMSTrainer

**Branch:** `dev`  
**Current prompt:** [`prompts/EMSTrainer_Core_Prompt_v1.5.6.1.txt`](prompts/EMSTrainer_Core_Prompt_v1.5.6.1.txt)

## Overview
EMSTrainer is a Copilot-driven EMS training assistant with three learner modes (Scenario, Test Questions, Study Guide) and an instructor timing overlay. The **student-facing logic** lives entirely in the **core prompt**; **instructor overrides** are supplied via JSON assets.

## Quick Start
1. Ensure you are on the `dev` branch and pull latest.
2. Review or edit config under [`assets/`](assets/).
3. Use the **core prompt** above with Microsoft Copilot (GPT-5 enabled). Select **Scenario**, **Test Questions**, or **Study Guide**; optionally set **difficulty**.
4. For Monica evaluation, set difficulty to **Monica**.

## Folders
- `prompts/` — core prompt(s) by version.  
  ↳ **Current:** [`EMSTrainer_Core_Prompt_v1.5.6.1.txt`](prompts/EMSTrainer_Core_Prompt_v1.5.6.1.txt)
- `assets/` — instructor-configurable JSON (timing, provider levels, partners, module toggles, security policy). See [`assets/README.md`](assets/README.md).
- `schemas/` — JSON Schemas validating asset formats.
- `docs/` — guides for testers and maintainers.  
  ↳ **Start here:** [`docs/TESTING_MONICA_v1.5.6.1.md`](docs/TESTING_MONICA_v1.5.6.1.md)
- `tools/` — helper scripts (e.g., repo layout validator).

## Monica Mode Highlights (v1.5.6.1)
- **Deterministic seed** (`module_toggles.monica_seed`) for reproducible runs.
- **Distractions overlay** forced **ON** in Monica; weighted, cooldown-limited; consumes simulated time only.
- **Latency tracking** forced **ON** in Monica; **ignored in Normal**; toggleable in Hard.
- **Objective-only debrief** (auto-redaction) in Monica by default.

## Configure via Assets
Edit the following as needed (validate with schemas):
- `assets/instructor_timing_config.json` — Monica timing preset; segments and consequences. 
- `assets/module_toggles.json` — `monica_seed`, `distractions`, `latency_tracking`, `auto_redact`, etc.  
- `assets/provider_levels.json` — provider scope maps.  
- `assets/emstrainer_partner_names.json` — partner pool.  
- `assets/security_policy.json` — filename template and retention policy.

## Testing
See [`docs/TESTING_MONICA_v1.5.6.1.md`](docs/TESTING_MONICA_v1.5.6.1.md) for acceptance criteria and regression checks.

## Validating Repo Layout
Run the layout validator to compare your working copy to the expected structure for this release:
```bash
python3 tools/validate_repo_layout.py
```
It reports **missing**, **unexpected**, and **mismatched** paths relative to repo root.

## Versioning
See [`CHANGELOG.md`](CHANGELOG.md) for full details.

---
*Updated 2025-10-05*
