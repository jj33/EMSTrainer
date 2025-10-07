# Changelog

All notable changes to EMSTrainer will be documented in this file.

## [1.6.0] - 2025-01-06

### 🎯 Major Changes
- **Modular Architecture**: Split monolithic prompt into Core.txt (16k) + Scenario_Mode.txt (23k)
- **GPT-5 Required**: Mandatory for medical accuracy and knowledge depth
- **No Character Limits**: Drag-and-drop files into Copilot/ChatGPT

### ✨ Added
- Air Care Paramedic (ACP) provider level between Paramedic and CCP
- Four explicit difficulty modes (Easy, Standard, Hard, Monica)
- Continuous scene safety assessment with unsafe start scenarios
- Dynamic equipment failures (IV, monitor, O2, airway) with realistic probabilities
- Hidden grading criteria (5 Rights, AIDET, scene safety reassessment)
- Partner interactions tracked in timestamped timeline
- Student Quick Start Guide (docs/Student_Quick_Start_Guide.md)
- Instructor Quick Start Guide (docs/Instructor_Quick_Start_Guide.md)
- Example scenarios: cardiac_arrest_vf.json, mvc_trauma_monica.json
- What's New doc (docs/WHATS_NEW_v1.6.0.md)
- Provider levels schema and example with local customization
- Mobile keyboard recommendation in README

### 🔧 Changed
- Test/Study modes integrated into Core.txt (originally separate concept)
- Scenarios moved to Scenario_Mode.txt with full feature set
- README updated for v1.6.0 architecture
- Debrief format: Markdown source → PDF output
- Filename standardization: [Date]_[ScenarioID]_Debrief_[StudentID].md
- Partner pool updated with ACP partners (Skyler, Hawk)

### 🗑️ Removed
- Old monolithic EMSTrainer_Core_Prompt.txt (replaced by modular files)
- GitHub workflow validations (solo dev, will restore later if needed)

### 📝 Planning
- Equipment timing delays (LUCAS 30-45s, EtCO2 15s calibration) - v1.7
- In-prompt scenario editor (load, modify, save) - v1.7
- Full encryption (AES-256) - v1.7
- Instructor test/study generator - v1.6 (after core complete)
- Complete conversation transcripts - Future
- Voice of patient - Future
- Integrated documentation prompts - Future

### 🐛 Fixed
- Character limit issues (now unlimited with drag-drop)
- Scope of practice clarity (delta notation, local overrides)

---

## [1.5.6.3] - 2025-10-06
- Added difficulty mode toggles to core prompt
- Version tracking and compatibility checking

## [1.5.6.2] - 2025-10-05
- Monica Mode integration
- UI suppression for clickable elements

## [1.5.6.1] - 2025-10-05
- Initial Monica Mode implementation
- Self-check header for UI suppression

---

## Versioning

Format: [Major].[Minor].[Patch]

- **Major**: Breaking changes, architecture overhauls
- **Minor**: New features, significant enhancements
- **Patch**: Bug fixes, small improvements

---

*For detailed feature status, see planning/EMSTrainer_Feature_Document.md*
