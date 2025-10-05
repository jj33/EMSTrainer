# EMS Trainer v1.5.3 – Future Ideas with Implementation Status

This document outlines proposed enhancements for EMS Trainer v1.5.3, along with their implementation status based on features already present in v1.5.2.

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
