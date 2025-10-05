
# EMSTrainer Assets (v1.5.6.1)

- `instructor_timing_config.json` — Monica preset with enforced timing and key segments.
- `provider_levels.json` — Capability map for EMR/EMT/AEMT/Paramedic/CCP.
- `emstrainer_partner_names.json` — Partner pool including "Joel".
- `med_director_rules.json` — Consult & ToR rules; patch delay penalties.
- `module_toggles.json` — Feature flags and Monica controls:
  - `monica_seed`: deterministic runs (null/random if omitted)
  - `distractions`: always ON in Monica (`monica_forced: true`), toggleable elsewhere
  - `latency_tracking`: always ON in Monica (`monica_forced: true`), toggleable elsewhere
  - `auto_redact`: Monica debrief objective-only by default
- `security_policy.json` — Hashing, timestamps, and submission filename template.

**Note:** In Normal mode, latency tracking is ignored regardless of toggles (`latency_tracking.normal_ignored: true`).
