# EMSTrainer v1.5.6.2 — Monica integrated, UI suppression, linter/CI, DLOG/LATLOG, safety scoring

**Release date:** 2025-10-05

## Summary
This release integrates **Monica Mode** directly into the canonical student prompt, hardens the UX by **suppressing clickable UI elements**, and adds **seed logging**, **DLOG/LATLOG debriefing**, and **combined safety scoring** with severity bias controls. It also ships a linter + CI guardrail to prevent reintroduction of task-list checkboxes or HTML widgets that can render as interactive elements.

## What’s New
- **Monica Mode (Integrated)**
  - Strict **countdown timer** with `[T- MM:SS]` per turn; hard stop at timeout with outcome/debrief.
  - **Curveball** module (≥1 guaranteed event within configured window).
  - **Aggressive vitals trending** under delayed/inappropriate care; strict **peds/OB** policy.
  - **Termination timing + Med Director call** logic via config.
  - **Compressed** responses in Monica for high-signal interaction.

- **UI Clickables Suppression**
  - Explicit policy to avoid Markdown task lists (`- [ ]`, `- [x]`), HTML widgets (`<button>`, `<details>`, `<form>`, etc.), and YAML front matter.
  - **Self-check header** printed once at scenario start (toggle with `ui_suppression_selfcheck`):
    ```
    [UI-SAFE ✓] Clickables suppressed; task lists disabled; HTML widgets disabled.
    ```

- **Reproducibility & Debriefing**
  - **Run seed logging** for reproducible test sessions.
  - **DLOG** (decision log) / **LATLOG** (latency log) summaries for debrief.
  - **Combined safety scoring** with severity bias controls.

## Files & Locations
- **Canonical prompt**: `prompts/EMSTrainer_Core_Prompt.txt`
- **Instructor config**: `assets/instructor_config.json`
- **Docs**: all README-style docs live under `docs/` (only the project root `README.md` exists outside `docs/`).

## Configuration (examples)
```jsonc
// assets/instructor_config.json
{
  "monica_mode": true,
  "ui_suppression_selfcheck": true,
  "monica": {
    "timer_seconds": 900,
    "curveball_enabled": true,
    "peds_ob_strict": true,
    "aggressive_trending": true,
    "compressed_prompt": true,
    "termination_timing": { "enabled": true, "med_director_call_required": true },
    "monica_lock": true
  },
  "curveball": { "min_seconds": 180, "max_seconds": 720 },
  "provider_level": "Paramedic",
  "student_role": "Paramedic",
  "partner": { "name": "(default)", "cert": "EMT", "acts_only_on_order": true }
}
```

## Upgrade Guide
1. **Pull latest** on your working branch.
2. Ensure `prompts/EMSTrainer_Core_Prompt.txt` is the canonical prompt (Monica integrated, UI suppression present).
3. Merge or update `assets/instructor_config.json` to include your desired Monica and UI suppression toggles.
4. (Optional) Restore `assets/emstrainer_partner_names.json` if your Instructor UI expects it.
5. Run the linter to confirm no clickable UI syntax remains:
   ```bash
   bash tools/lint_ci.sh --root . --dry-run   # Exit 0 if clean; 2 if changes needed
   ```

## Known Considerations
- If any prompt or doc still emits `- [ ]` / `- [x]` or contains interactive HTML, the linter will flag it. Run `--apply` to auto-fix and re-commit.
- If your workflow references `assets/emstrainer_partner_names.json`, ensure it exists and matches the expected schema for the Instructor UI.

## Thanks
Huge thanks to contributors iterating on Monica Mode, UX hardening, and CI guardrails.
