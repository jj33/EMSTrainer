
# Changelog

All notable changes to this project are documented here. Dates are in YYYY-MM-DD.

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

