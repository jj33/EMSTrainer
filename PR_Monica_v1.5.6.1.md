# PR: Monica v1.5.6.1 — Seed + Distractions; Latency ignored in Normal; Assets/Schemas/Docs; Layout Validator

**Base**: `main`  
**Head**: `dev`  
**Date**: 2025-10-05

## Summary
This PR promotes the latest Monica-mode enhancements to `main` and aligns the repository structure for testing and instructor overrides. It introduces deterministic seeding, forced distractions in Monica, latency tracking *ignored in Normal* (toggleable in Hard), objective-only debrief in Monica, updated assets/schemas, docs, and a repo layout validator.

## Changes in this PR
### Core Prompt
- `prompts/EMSTrainer_Core_Prompt_v1.5.6.1.txt`
  - Monica v2 strict overlay carried forward; clarified policy: **Latency always ON in Monica, ignored in Normal, toggleable in Hard**.

### Assets (instructor-configurable)
- `assets/instructor_timing_config.json` — Monica timing preset; key segments including `arrest_time_to_tor_call`.
- `assets/module_toggles.json` — (already present) includes `monica_seed`, `distractions`, `latency_tracking.normal_ignored: true`, `auto_redact`.
- `assets/provider_levels.json` — provider scope maps.
- `assets/emstrainer_partner_names.json` — partner pool (includes Joel).
- `assets/med_director_rules.json` — consult & ToR rules; patch penalties.
- `assets/security_policy.json` — submission filename template, retention.

### Schemas
- `schemas/instructor_timing_config.schema.json`
- `schemas/module_toggles.schema.json`
- `schemas/provider_levels.schema.json`
- `schemas/partner_pool.schema.json`
- `schemas/med_director_rules.schema.json`
- `schemas/security_policy.schema.json`

### Docs
- `docs/TESTING_MONICA_v1.5.6.1.md` — Monica testing & acceptance criteria.
- `docs/README.md` — docs index.
- Root `README.md` — quick links and usage.
- `CHANGELOG.md` — v1.5.4 → v1.5.5 → v1.5.6 → v1.5.6.1 entries.

### Tools
- `tools/validate_repo_layout.py` + `tools/expected_layout_v1.5.6.1.json` — validates required files/paths; fails on missing.

## Rationale (key policy)
- **Normal mode** is for practice and learning → **latency tracking ignored** to avoid over-penalizing learners.
- **Monica (evaluation)** requires rigor → distractions forced ON, latency tracking ON, objective debrief, deterministic seed supported for fair retesting.
- **Hard** offers realism → latency toggle available via assets.

## Testing Instructions
1. **Structure check**
   ```bash
   python3 tools/validate_repo_layout.py
   ```
   Expect `Missing: None`. Any `Unexpected` lines are informational only.

2. **Monica acceptance** — follow `docs/TESTING_MONICA_v1.5.6.1.md`:
   - Seed determinism (`monica_seed`) → reproducible runs.
   - Distractions appear (consume simulated time, no vitals changes).
   - Latency tracking logs LATLOG events; scoring deductions on WARN/FAIL.
   - Auto-redaction → debrief shows objective metrics only.

3. **Mode regression**
   - Normal: latency **ignored**; no LATLOG/penalties.
   - Hard: enable latency via `assets/module_toggles.json` and verify.

## Compatibility
- Student narrative flow unchanged outside Monica policy.
- Instructor overrides remain JSON-based; no code changes required.

## Risks & Mitigations
- **Over-ending scenarios in Monica:** `penalty_only` segments can be used in instructor timing to avoid hard ends.
- **Determinism vs. randomness:** expose `monica_seed` and log in `TLOG.meta` for audit.

## Checklist
• Core prompt updated to v1.5.6.1
• Assets present and validated
• Schemas present and validate assets
• Docs updated (testing guide + index + README)
• Validator passes (`Missing: None`)

--
Maintainer: please **Squash & Merge** into `main` once acceptance criteria pass.
