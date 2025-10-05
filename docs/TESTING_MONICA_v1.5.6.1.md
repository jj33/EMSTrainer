
# TESTING_MONICA_v1.5.6.1

Validates Monica v2+ features: deterministic seed, distraction overlay, latency tracking, auto-redaction.

## 1) Setup
- Branch `dev`. Files: `EMSTrainer_Core_Prompt_v1.5.6.1.txt`, updated `assets/`, `schemas/`.

## 2) Determinism
- Set a seed in `assets/module_toggles.json`: `"monica_seed": 12345`.
- Run the same Monica scenario twice and verify identical: curveball type, order of distractions (subject to cooldown), and vitals jitter patterns.
- Command: `show seed` → prints seed value.

## 3) Distractions (Monica forced ON)
- Start Monica and progress normally. Expect periodic distraction events (short, objective notes) consuming small simulated time increments.
- Verify no clinical vitals are altered by distraction events directly.
- In Normal/Hard, toggle by setting `distractions.enabled_default` true/false and confirm behavior.

## 4) Latency tracking (ignored in Normal mode)
- Track BVM effect: start BVM, delay effective ventilation cues so that ETCO2 improvement occurs after 70s → expect LATLOG entry with `FAIL` and a small score deduction (−6 by default), but not necessarily a strike.
- Repeat with 50s → `WARN` (−3).
- In Normal/Hard, toggle via `latency_tracking.enabled_default` and confirm.

## 5) Auto-redaction
- End a Monica scenario and confirm debrief shows only: Timing Summary, Strike Summary, Score breakdown, submission filename (no narrative/environment details).
- In Normal/Hard, auto-redaction should be off by default.

## 6) Regression
- v1.5.5 strike thresholds and timing enforcement unchanged.
- Instructor-configured penalty_only segments still avoid immediate end.

## 7) Acceptance
- Seed determinism produces reproducible runs.
- Distractions appear in Monica and are toggleable elsewhere.
- Latency tracking records events and applies scoring penalties per thresholds.
- Monica debrief is objective-only when auto_redact is enabled.
