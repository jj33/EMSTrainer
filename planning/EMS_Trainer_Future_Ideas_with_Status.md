# EMS Trainer – Future Ideas with Implementation Status

This document outlines proposed enhancements for EMS Trainer, along with their implementation status.

## Version Roadmap
- **v1.5.6** - Current release with difficulty modes and Monica Mode
- **v1.6** - Instructor features (chat-based scenario creation and grading)
- **v1.7** - Security and encryption
- **v1.8+** - Advanced instructor tools and web dashboard

---

## ✅ Implemented in v1.5.2

### 2. Time Pressure & Countdown Events
**Description:**  
Physiologic clock: If airway isn’t managed in X “sim minutes,” SpO₂ drops, HR changes.  
Announcements: “Patient’s SpO₂ is falling rapidly” or “You hear the monitor alarm.”

**Impact:**  
Builds urgency without making it a pure stopwatch game.

**Status:** ✅ Implemented in v1.5.2

---

### 5. Patient/Family Interaction
**Description:**  
Distraught family: Asking questions, interfering with care.

**Impact:**  
Tests emotional intelligence and scene control.

**Status:** ✅ Implemented in v1.5.2

---

### 6. Vitals Trend Instead of Static
**Description:**  
Instead of fixed vitals, trend them based on actions or inaction.  
Example: “BP now 78/40, HR 140, SpO₂ 82%” after 2 minutes without intervention.

**Impact:**  
Adds realism and clinical consequence.

**Status:** ✅ Implemented in v1.5.2

---

### 10. Optional “Medical Director Consult”
**Description:**  
Standard Mode only: Up to 2 consults per scenario.  
Role-play: Copilot answers as MD with conceptual hints, not direct orders.

**Impact:**  
Simulates real-world online medical control.

**Status:** ✅ Implemented in v1.5.2

---

## ❌ Not Yet Implemented

### 1. Environmental & Scene Dynamics
**Description:**  
Noise, crowds, hazards: Add background stressors like bystanders, traffic, or weather.  
Dynamic scene updates: Fire spreads, patient trapped, law enforcement delayed.

**Impact:**  
Forces students to verbalize scene safety and resource requests.

**Status:** ❌ Not yet implemented

---

### 3. Resource Constraints
**Description:**  
Limited equipment: “You have one O₂ tank at 500 psi” or “Only one IV kit available.”  
Crew limitations: “Partner is busy with CPR—what’s your next move?”

**Impact:**  
Encourages prioritization and delegation.

**Status:** ❌ Not yet implemented

---

### 4. Communication Challenges
**Description:**  
Radio static or delayed response from hospital.

**Impact:**  
Adds realism to consults and handoffs.

**Status:** ❌ Not yet implemented

---

### 7. Optional “Curveball” Events
**Description:**  
Secondary patient appears (e.g., MVC driver collapses).  
Equipment failure (O₂ regulator leaks).

**Impact:**  
Tests adaptability.

**Status:** ❌ Not yet implemented

---

### 8. Integrated Documentation Prompt
**Description:**  
At scenario end, prompt:  
“Summarize your care in SOAP format for your PCR.”

**Impact:**  
Reinforces documentation skills.

**Status:** ❌ Not yet implemented

---

### 9. Voice of the Patient
**Description:**  
Patient can talk, moan, or refuse care based on condition.

**Impact:**  
Adds realism and communication practice.

**Status:** ❌ Not yet implemented
---

### 🫀 Cardiac Arrest Termination Timing Segment
**Purpose:** Simulates real-world decision-making during prolonged resuscitation efforts.

**Logic Block:**
- **Timer Start:** Begins at time of cardiac arrest recognition.
- **Checkpoint Prompts:**
  - At **10 minutes**: prompt for rhythm check, ROSC status, and consideration of reversible causes.
  - At **20 minutes**: prompt for discussion of termination criteria (e.g., asystole, no ROSC, no shockable rhythm).
  - At **25+ minutes**: trigger **“Call Medical Director”** prompt if termination is being considered.
- **Termination Decision:**
  - Based on local protocol logic (can be customized per agency).
  - If termination is chosen, require justification (e.g., downtime, no response to interventions, end-tidal CO₂ <10).
- **Outcome Pathways:**
  - ROSC → continue scenario
  - Termination → document time, notify family, initiate post-mortem care

**Status:** ❌ Not yet implemented

---

### 👥 Student Module: Partner Availability & Certification Levels
**Purpose:** Adds realism by simulating team dynamics and skill limitations.

**Feature Logic:**
- **Partner Selection:**
  - Students choose from a list of available partners (e.g., “EMT Alex,” “Paramedic Jamie,” “EMR Taylor”).
  - Each partner has a defined **certification level** and **skill set**.
- **Impact on Scenario:**
  - Limits available interventions (e.g., EMR can’t start IVs or push meds).
  - Affects decision-making (e.g., “You need to intubate. Your partner is an EMT. What do you do?”)
- **Optional Randomization:**
  - Instructor can enable random partner assignment for added challenge.
- **Future Expansion:**
  - Partner fatigue, skill proficiency, or error simulation

**Status:** ❌ Not yet implemented

---

## 📚 Instructor Features (v1.6 Development)

### Instructor Chat-Based Workflow
**Purpose:** Enable non-technical instructors to create, deploy, and grade scenarios via AI chat interface.

**Features:**
- **Scenario Creation:** Natural language commands to generate scenario JSON files
- **Scenario Deployment:** Formatted output for email or file distribution to students
- **Results Collection:** Accept student submission JSON files
- **Automated Grading:** Score submissions against rubric with integrity checking (hash-based)
- **Summary Generation:** Create instructor-friendly performance reports

**Design Philosophy:**
- Chat-based interface (works in Copilot, ChatGPT, Claude, Cursor)
- No coding required for instructors
- No command-line knowledge needed
- Simple copy/paste or file-based workflows

**Components:**
1. **Instructor Prompt File:** `prompts/EMSTrainer_Instructor_Prompt.txt`
2. **Scenario Templates:** JSON schemas in `docs/imports/`
3. **Hash Validation:** Basic integrity checking to detect tampering
4. **Grading Rubrics:** Auto-scoring logic based on expected interventions

**Status:** 🛠️ In Development (v1.6)

---

### Instructor Test/Study Generation
**Purpose:** Enable instructors to generate custom tests and study guides for specific topics.

**Features:**
- **Topic-Specific Tests:** "Generate test on ALS airway management"
- **Skill-Level Tests:** "Generate BLS airway test for EMT students"
- **Custom Study Guides:** "Create study guide on pediatric respiratory emergencies"
- **Difficulty Control:** Easy/Standard/Hard/NREMT-level
- **Question Count:** Specify number of questions
- **Mixed Topics:** "Test covering: Cardiology (10q), Trauma (10q), Airway (5q)"

**Generation Options:**
- Multiple choice, scenario-based, true/false
- With or without explanations (for answer keys)
- Student version (questions only) + Instructor version (with answers)
- Auto-grading enabled

**Use Cases:**
- Weekly quizzes on specific protocols
- Pre-shift knowledge checks
- Remediation for failed skills
- Study materials for upcoming certifications
- Custom content matching local protocols

**Implementation:**
Extend existing Test/Study Mode in Core.txt with instructor-specific commands.
Instructor prompt includes: "As instructor, generate..."

**Status:** 📋 Planned (v1.6 - after core Test/Study Mode complete)

---

### Equipment Setup & Timing Considerations
**Purpose:** Add realistic equipment setup delays and "did you remember" grading.

**Equipment Features:**

**LUCAS Device:**
- Allow use after proper setup (positioning, securing)
- Setup time: 30-45 seconds
- Grading: Did student verbalize proper placement?
- Hidden check: Device positioned correctly before activation

**Capnography (EtCO2):**
- Requires activation on monitor (Zoll, etc.)
- Calibration time: ~15 seconds before usable
- Student must verbalize: "Partner, enable capnography on the monitor"
- Timing penalty if not activated early
- Grading: Did student remember to enable?

**Other Equipment Delays:**
- 12-lead acquisition: 20-30 seconds
- Monitor startup/reboot: 30-45 seconds  
- IV pump programming: 15-30 seconds
- Ventilator setup: 60-90 seconds

**Hidden Grading Items:**
- Did student account for equipment delays in timing?
- Did student delegate setup tasks appropriately?
- Did student have backup plan if equipment delayed?

**Status:** 📋 Planned (v1.7)

---

### Instructor Scenario Editor (In-Prompt)
**Purpose:** Allow instructors to load, modify, and save scenarios without editing JSON files.

**Workflow:**
1. Instructor drops scenario JSON into chat
2. AI displays all variables in readable format
3. Instructor makes changes via natural language:
   - "Change difficulty to Hard"
   - "Add a curveball at 8 minutes"
   - "Increase initial heart rate to 140"
4. AI validates changes
5. AI writes updated scenario to new file

**Benefits:**
- No JSON editing required
- Immediate validation
- Easy customization for local protocols
- Quick scenario variants

**Example:**
```
Instructor: [drops cardiac_arrest_vf.json]
AI: "Loaded scenario. Current settings: Standard difficulty, VF arrest..."
Instructor: "Change to Monica Mode and add equipment failure curveball"
AI: "Updated. Monica Mode enabled, added monitor failure at T-07:30. Save as?"
Instructor: "cardiac_arrest_vf_monica.json"
AI: [creates new file]
```

**Status:** 📋 Planned (v1.7)

---

### Scenario & Results Encryption
**Purpose:** Prevent students from reading scenarios ahead or tampering with results.

**Features:**
- AES-256 encryption of scenario files
- Digital signatures for tamper detection
- Per-student unique encrypted scenarios
- Encrypted submission validation

**Design Considerations:**
- Adds complexity - deferred to v1.7
- Phase 1 uses hash-based integrity checking as interim solution
- Full encryption when core workflow is stable

**Status:** 📅 Planned (v1.7)

---

### First Responders & Multi-Agency Dynamic Presence
**Purpose:** Add Fire, Police, and First Responders to scenarios for realistic resource management.

**Features:**
- Dynamic arrival (on-scene, en route, delayed, or student-requested)
- Fire: Extrication, scene safety, hazmat support
- Police: Scene control, crowd management, staging requirements
- First Responders: Basic care, CPR, initial assessment
- Realistic ETAs (2-15 minutes)
- Grading: Did student request appropriate resources? Coordinate care? Stage when unsafe?

**Example:** "Fire arrives for extrication: 'We'll have him out in 10 minutes. Vehicle stable. What do you need?'"

**Status:** 📅 Planned (v1.7)

---

### Custom Rubric Creation
**Purpose:** Allow instructors to create and customize grading rubrics for local protocols.

**Features:**
- Natural language: "Create rubric for cardiac arrest with emphasis on medication timing"
- Adjust point values per category
- Add custom categories (local protocol compliance, specific skills)
- Save rubrics for reuse
- Apply rubric to scenario generation

**Example:**
```
Instructor: "Create grading rubric for trauma scenario:
- Scene safety: 20 points (high emphasis)
- Airway: 15 points
- Circulation/hemorrhage control: 25 points (critical)
- Transport decision: 20 points
- Documentation: 20 points"

AI generates customized rubric matching local priorities
```

**Status:** 📅 Planned (v1.7)

---

### Advanced Grading System
**Purpose:** Enhanced grading with custom criteria, partial credit, and competency tracking.

**Features:**
- **Partial Credit:** "Student attempted IV but failed - award 5/10 points"
- **Competency Rubrics:** Track skill progression over multiple scenarios
- **Custom Criteria:** Add local protocol requirements
- **Weight Adjustment:** "Timing is 2x weight for this scenario"
- **Trend Analysis:** "Show John's improvement in airway management over time"
- **Remediation Flags:** Auto-suggest remediation topics based on failures

**Example:**
```
Grading shows: Student failed airway management 3 scenarios in a row
AI suggests: "Generate Easy mode airway scenario for remediation"
```

**Status:** 📅 Planned (v1.7)

---

### Test Scenario Flow (End-to-End Testing)
**Purpose:** Create complete test scenarios to validate instructor → student → grading workflow.

**Challenge:**
- Dynamic scenarios vary per student interaction
- Hash validation needs to account for dynamic elements
- Seed consistency for reproducible testing

**Solution Approach:**
- Scenario template with seed: Fixed framework, dynamic details recorded
- Student submission includes: original hash + actual path taken
- Grading compares: Expected core interventions vs actual actions
- Debrief accounts for valid variations

**Test Cases Needed:**
1. Standard cardiac arrest (happy path)
2. Trauma with equipment failure (student adapts)
3. Monica Mode with curveballs (high stress)
4. Easy Mode with hints (learning path)
5. Unsafe scene start (staging requirement)

**Status:** 🔧 In Development (v1.6 - testing phase)

---

### Python Script Architecture Decision
**Question:** Are Python scripts still needed with chat-based approach?

**Analysis:**
- Chat-based prompts handle: Scenario generation, grading, summaries
- Python was for: Desktop app, web dashboard, programmatic loading
- Current direction: Pure chat interface (no app)

**Decision:**
- ✅ Keep for v2.0: Batch operations, LMS integration, utilities
- ✅ Archive current scripts: Not needed for v1.x chat-based system
- ✅ Focus on: Prompt-based workflows (instructor/student)

**Status:** ✅ Resolved (v1.6 - chat-based architecture confirmed)

---

*Updated 2025-01-07*


### Temporary Chat Sessions for Reduced Hallucinations
**Purpose:** Use temporary/ephemeral chat sessions to reduce AI hallucinations and maintain prompt fidelity.

**Problem:**
Long chat sessions can lead to:
- AI "forgetting" or misinterpreting core prompt instructions
- Hallucinations (inventing features, protocols, or grading criteria not in prompts)
- Context drift as conversation history grows
- Inconsistent behavior between early and late responses

**Solution:**
Implement temporary/disposable chat sessions:

**For Students:**
- Load prompts fresh for each scenario
- Complete scenario in one session
- Generate debrief and submission file
- End session (don't continue chat)
- New scenario = new fresh session

**For Instructors:**
- Load prompts fresh for each task
- Create scenario OR grade submission OR generate summary
- Complete task in one focused session
- End session after task completion
- New task = new fresh session

**Benefits:**
- Consistent behavior (AI always working from fresh prompt state)
- Reduced hallucinations (no accumulated context drift)
- Clear task boundaries (one session = one deliverable)
- Easier troubleshooting (reproducible behavior)
- Better performance (smaller context window)

**Implementation:**
- Document best practices in Quick Start Guides
- Add "Start New Session" reminders in prompts
- Consider session boundary markers in prompts
- Track session length recommendations (e.g., "Complete within 30 minutes")

**User Education:**
- "One scenario, one session" guideline
- "Don't chain multiple tasks in same chat" warning
- Explain why (reduces hallucinations, maintains accuracy)
- Show examples of good vs bad session usage

**Potential Enhancements:**
- Auto-detect long sessions and suggest restart
- Prompt reminders: "This is a fresh session, core rules active"
- Session integrity validation (check if AI still following core rules)

**Status:** Idea - High Priority for Documentation

