# Code Blackout - Instructor Guide

**Scenario Version:** 1.0  
**EMSTrainer Version:** 1.6.1  
**Difficulty:** Monica (Extreme)  
**Duration:** 60 minutes  
**Provider Level:** Paramedic  
**Last Updated:** October 9, 2025

---

## Overview

Code Blackout is the ultimate Monica-level scenario - a 60-minute cascading medical emergency designed to test every aspect of paramedic practice. This is not simply a cardiac arrest scenario; it's a multi-system disaster that compounds with equipment failures, environmental challenges, and human factors.

### What Makes Code Blackout Unique

**Multi-System Medical Emergency:**
- Critical hypoglycemia (glucometer reads "Low")
- Symptomatic bradycardia requiring intervention
- Hypothermia (95.2°F)
- Agonal respirations requiring immediate airway management
- Flash pulmonary edema development
- High probability of cardiac arrest if poorly managed

**Equipment Realism:**
- Main O2 tank: 800 PSI (only 40% full)
- Portable tank #1: Empty (failed rig check)
- Portable tank #2: Full (only backup)
- Monitor battery: 20 minutes remaining
- IV Pump #1: Working (only one available)
- IV Pump #2: Dead battery
- LUCAS: Full battery (45 minutes - the one thing that works!)

**Complete Isolation:**
- Lightning strike at T+2:00 cuts all communications
- No radio, no cell service, no backup units
- Air transport grounded due to storm
- Student is completely autonomous


**Family Dynamics:**
- Wife's anxiety level responds to AIDET communication
- Poor communication → Active interference during care
- Good communication → Helpful and manageable
- May force way into ambulance if ignored

**Equipment Failures:**
- Inverter surge at patient loading (T+22:00)
- Cody intentionally kicks inverter cabinet (trying to fix it)
- Monitor shorts → Electrical burns to patient
- Monitor AC input destroyed (battery only from that point)
- Forces adaptation and troubleshooting

**Medical Consequences:**
- Arrest triggers are based on actual medical reality
- NOT arbitrary time-based events
- Rebound hypoglycemia if D50 used without recheck
- Bradycardia progression if untreated
- Hypoxic arrest if airway delayed
- Patient may survive OR arrest based on student care quality

---

## Pre-Scenario Setup

### Files to Load (In This Order):

1. **EMSTrainer_Core.txt**
   - Foundation with equipment tracking rules
   - O2 calculations, battery management
   - Monitor vitals request protocol

2. **EMSTrainer_Instructor_Interface.txt**
   - Your instructor interface

3. **code_blackout_scenario.json**
   - This specific scenario with all parameters


### Verify AI Understanding

After loading all files, confirm the AI understands:

**Ask:** "Confirm you've loaded Code Blackout scenario. What are the key equipment limitations?"

**AI Should Respond With:**
- Main O2: 800 PSI
- Monitor battery: 20 minutes
- Only 1 working IV pump
- LUCAS: 45 minutes
- Equipment tracking enabled

**Ask:** "How do arrest triggers work in this scenario?"

**AI Should Respond:**
- Medical-based, not time-based
- Triggered by student's interventions (or lack thereof)
- Multiple possible arrest pathways
- Patient may survive with excellent care

**Ask:** "How does the wife respond to communication?"

**AI Should Respond:**
- AIDET reduces anxiety
- Ignoring her escalates interference
- May force into ambulance if poorly managed

---

## Scenario Timeline Overview

### Phase 1: Dispatch & Arrival (T-5:00 to T+1:30)
**Dispatch:** "03:17 - Lift assist, 58M fell, rural residence"
- Appears routine BLS call
- Storm brewing in distance
- Normal radio traffic

**Arrival:**
- Wife meets at door: "He just fell!"
- Walk in, assess patient
- Reality: This is NOT a lift assist - critical multi-system emergency


### Phase 2: Lightning Strike & Isolation (T+2:00)
**The Blackout Event:**
```
"Right as you recognize how critical he is, a massive BOOM 
shakes the house. Lightning has struck the transformer down 
the road. The lights flicker and die. Your radio crackles to 
static, then silence. Cell phone: No Service. You're cut off."
```

**Effects:**
- Complete darkness (flashlights only)
- No radio communication
- No cell service
- No backup units available
- Air transport grounded
- Storm intensifying
- Student is completely autonomous

### Phase 3: Scene Management (T+2:00 to T+20:00)
**Student Must Manage:**
- Airway crisis (agonal → intubation)
- Critical hypoglycemia (glucometer "Low")
- Symptomatic bradycardia (38 irregular)
- Hypothermia (95.2°F)
- Wife's anxiety
- Limited equipment
- Monitor battery draining

**Key Decision Points:**
- D10 vs D50 for glucose (D10 preferred)
- Which drug on the single working pump?
- Pacing vs Atropine for bradycardia
- CPAP for pulmonary edema? (burns O2 fast)
- When to transport? (load-and-go vs stay-and-play)
- How to manage wife? (AIDET)


### Phase 4: Loading & Inverter Surge (T+20:00 to T+25:00)
**Patient Being Loaded:**
- Moving to ambulance
- Equipment secured
- Preparing for transport

**T+22:00 - The Surge Event:**
```
"Patient secured. Cody walks to the driver's door, muttering 
'These damn inverters have been acting up all week...' 
WHAM! He kicks the inverter cabinet hard.

CLICK-WHIRRRR! The inverters roar to life.

CRACK! Sparks fly from the monitor. The patient screams and 
jerks violently. Current surged through the pads. You smell 
burning flesh. The monitor goes black.

Cody: 'Oh shit! Sorry! I didn't think—'"
```

**Effects:**
- Electrical burns to patient (2nd degree, pad sites)
- Monitor AC input destroyed (battery only now)
- Inverters are now working (good!)
- Pump #2 now available (if student realizes)
- New injury to manage
- Cody feels terrible

**Student Must:**
1. Remove pads immediately
2. Assess and treat burns
3. Understand monitor battery-only (20 min max)
4. Decide: Restart monitor or work manually?
5. Reassure/redirect Cody
6. Continue with transport


### Phase 5: Transport (T+25:00 to T+60:00)
**Cody Driving, Student Alone in Back:**
- Managing all interventions solo
- Monitor battery draining (if restarted)
- O2 depleting
- LUCAS available if arrest
- Bumpy rural roads
- Dark, stormy conditions
- 25+ minute transport

**Possible Complications:**
- Patient arrests (if interventions poor)
- Monitor battery dies
- O2 runs out (must switch to portable)
- LUCAS battery dies at T+45 (if used from start)
- Glucose crashes if not rechecked
- Wife interfering (if in ambulance)

**If Student Did Well:**
- Patient remains tenuous but stable
- Continuous management required
- May still arrest from MI extension (30% chance)
- OR survives to hospital (70% chance)

**If Student Made Mistakes:**
- High probability of arrest
- Arrest type depends on what was missed:
  - Rebound hypoglycemia → Seizure → PEA
  - Untreated bradycardia → Complete block → Asystole
  - Poor airway → Hypoxia → PEA/Asystole
  - Hypothermia → VF
  - MI extension → VF

### Phase 6: Hospital Arrival (T+60:00)
**Student Gives Report:**
- Complete patient information
- All interventions performed
- Current status
- Ongoing needs

**Outcome Determined By:**
- Quality of interventions
- Timing of interventions
- Resource management
- Communication effectiveness
- Adaptability to failures


---

## Equipment Management Guide

### Oxygen Tracking

**Formula:** (Current_PSI - 200) × Cylinder_Constant / Flow_Rate = Minutes

**M Cylinder (Main Tank):**
- Starting: 800 PSI
- Constant: 1.56
- Examples:
  - 15 LPM (NRB): (800-200) × 1.56 / 15 = 62 minutes
  - 25 LPM (CPAP): (800-200) × 1.56 / 25 = 37 minutes

**D Cylinder (Portable #2):**
- Starting: 350 PSI (full)
- Constant: 0.16
- Examples:
  - 15 LPM: (350-200) × 0.16 / 15 = 1.6 minutes (very limited!)
  - 10 LPM: (350-200) × 0.16 / 10 = 2.4 minutes

**When Student Says:** "Start CPAP at 10 cmH2O"
- AI calculates flow rate: ~25 LPM
- Starts O2 depletion timer
- Warns at 25%, 10%, 5% remaining
- Forces switch to portable or discontinue CPAP

**Track All Oxygen Use:**
- BVM ventilation
- NRB mask
- CPAP/BiPAP
- Nasal cannula
- Cumulative from all sources


### Battery Tracking

**Monitor (Zoll X Series):**
- Starting: 20 minutes remaining
- Why so low? Not charged, self-discharged, cold weather
- Continuous monitoring: Drains full 20 minutes
- Strategic use (on/off): Can extend significantly
- Heavy use (pacing, defib): Drains faster

**Warn Student:**
- At 50% (10 min): "Monitor battery 50%"
- At 25% (5 min): "Monitor battery warning: 25%"
- At 10% (2 min): "Monitor battery critical: 2 minutes"
- At 0%: "Monitor screen black. Battery depleted."

**LUCAS:**
- Starting: 45 minutes full battery
- Continuous operation from deployment
- No power-save mode
- Warn at 10 minutes remaining
- Dies at 45 minutes (must switch to manual CPR)

**IV Pump #1:**
- Starting: 120 minutes
- Only one available (Pump #2 dead until inverters work)
- Student must choose which drug gets the pump
- Common choices: D10 continuous, or Dopamine

### Monitor Vitals Request Protocol

**CRITICAL:** Student must ASK for vitals from monitor

**Incorrect:**
- AI automatically shows vitals
- Student assumes monitoring happening

**Correct:**
```
Student: "Cody, what's the monitor showing?"
Cody: "Sinus brady at 52, BP 98/60, SpO2 94%"
```

**If Student Doesn't Ask:**
- Don't provide vitals automatically
- They're working with less information
- Part of monitor battery management decision


---

## Wife Character Guide

### Playing the Wife Realistically

**Baseline State:**
- High anxiety (completely appropriate)
- Loves her husband, terrified
- Wants to help but doesn't know how
- Will escalate if ignored

### If Student Uses AIDET

**AIDET Framework:**
- **A**cknowledge: "I can see you're scared, that's normal"
- **I**ntroduce: "I'm [name], I'm a paramedic, this is Cody"
- **D**uration: "We'll work on him a few minutes, then transport"
- **E**xplanation: "His blood sugar is very low, I'm giving glucose"
- **T**hank you: "Thank you for calling us, you did the right thing"

**Wife Response (Good Communication):**
```
Wife: "His medications... yes, they're in the kitchen. 
       Is he going to be okay?"
[Moves out of the way, tries to help with tasks]
[Still anxious but manageable and helpful]

At transport:
Student: "I need you to follow in your car or get a ride. 
          Hospital is St. Mary's, 20 minutes."
Wife: "Okay... please save him." [Follows separately]
```

