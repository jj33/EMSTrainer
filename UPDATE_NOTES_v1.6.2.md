# EMSTrainer v1.6.2/v1.6.3 Update Summary
**Updated: December 20, 2025**

## 📦 Updated Files

1. **EMSTrainer_Core.txt** → v1.6.2
2. **EMSTrainer_Student_Interface.txt** → v1.6.3  
3. **EMSTrainer_Instructor_Interface.txt** → v1.6.2

## 🎯 Key Enhancements for Spring 2026 Semester

### 1. Pattern Recognition Mode (NEW)
**Purpose:** Addresses your 50% score on respiratory distress by training rapid differential diagnosis.

**How it works:**
- Present: 2-4 key clinical findings
- Student: Provides differential (CHF vs COPD vs pneumonia vs PE vs asthma)
- Guided assessment: Reveals findings one at a time
- Immediate feedback: Explains which discriminators matter most
- Time tracking: Builds speed (60 sec → 30 sec → 15 sec)

**Trigger phrases:**
- "Pattern drill: respiratory distress"
- "Differential diagnosis practice"
- "Help me recognize chest pain presentations"

**Example drill flow:**
```
67 y/o male, dyspnea
- Crackles bilateral bases
- JVD present  
- Orthopnea

Your differential? → [Student lists 2-3]
What would you assess next? → [Student chooses]
Based on findings, which is most likely? → [Student commits]
✅ Correct! CHF - Here's why...
Time: 45 seconds (excellent)
```

**Integration with your test results:**
System automatically weights drills toward your weak areas:
- 50% questions on "critical" areas (respiratory distress 50%)
- 30% questions on "high" priority (airway management 65%)
- 20% maintenance on strong areas

### 2. Weak Area Tracking System (ENHANCED)

**Upload your test results directly:**
```json
{
  "test_date": "2025-12-08",
  "test_name": "Fall 2025 Comprehensive Final",
  "total_score": 77,
  "curriculum_scores": [
    {"category": "AB3 - Respiratory Distress", "score": 50, "questions": 4, "priority": "critical"},
    {"category": "AB1 - Airway Management", "score": 65, "questions": 17, "priority": "high"},
    {"category": "TR6 - Head/Spine Trauma", "score": 50, "questions": 2, "priority": "medium"}
  ]
}
```

**System automatically:**
- Generates weighted question sets (50% critical areas)
- Creates targeted study guides
- Runs pattern recognition drills on weak topics
- Tracks improvement: "Respiratory distress: 50% → 78% over 3 sessions"

### 3. National Model EMS Guidelines Integration

**When project_knowledge_search is available:**

**Study Guides:**
- Auto-pulls relevant guideline sections
- References specific pages: "Per National Model Guidelines, p. 45..."
- Shows decision trees from guidelines
- Compares national vs. local protocols

**Scenarios:**
- Validates interventions against guidelines
- Cites evidence-based care in debrief
- Flags outdated practices

**Test Questions:**
- Built from guideline case examples
- References protocol pages
- Tests current standards vs. old practices

**Usage:** System automatically searches project knowledge when generating content - no extra commands needed.

### 4. Enhanced Monica Mode - Respiratory Focus

**For your Spring clinical prep:**

Monica Mode now includes specific respiratory distress scenarios that:
- Force rapid decision-making (15-30 sec windows)
- Stack multiple stressors at critical moments
- Punish delayed interventions (SpO2 drops 2% every 30 sec)
- Require correct differential to improve patient

**Example:** Respiratory distress + family interference + equipment failure + time pressure

**Use case:** Prepares you for fast-paced Spring clinical rotations where Will's "pace of the 1%" principle matters.

## 🚀 How to Use for Spring Prep

### Week 1-2 (Before ACLS - February)

**Morning routine (10 minutes):**
```
1. Load EMSTrainer (Core + Student Interface)
2. "Pattern drill: respiratory distress" 
3. Run 3-5 rapid drills
4. Track improvement
```

**Evening session (30 minutes):**
```
1. Upload your test results
2. "Generate test on my weak areas" (auto-weighted)
3. Take 20 questions
4. Review missed questions
5. "Study guide on [missed topic]"
```

### Week 3-4 (January - Before Spring Start)

**Advanced practice:**
```
1. "Monica Mode respiratory scenario"
2. Run full scenario under pressure
3. Review debrief for timing/efficiency
4. Repeat with different presentations
```

**Post-shift debrief:**
```
After clinical rotation:
1. "Recreate scenario: [describe call]"
2. Run it through EMSTrainer  
3. Compare your field decisions to guidelines
4. Identify what you'd do differently
```

### During Spring Semester

**Weekly maintenance:**
```
Monday: Pattern drills (respiratory/cardiology)
Wednesday: Test Mode (20 questions on current module)
Friday: Full scenario (Monica Mode for challenge)
Sunday: Study guide on next week's topic
```

**Pre-NREMT prep:**
```
8 weeks out: Upload practice test scores
6 weeks out: Focus drills on persistent weak areas
4 weeks out: Monica Mode scenarios daily
2 weeks out: Mixed topic tests (50 questions/day)
```

## 📋 Quick Start Commands

**Pattern Recognition:**
- "Pattern drill: respiratory distress"
- "Differential diagnosis: chest pain"
- "Recognition practice: shock presentations"

**Test Mode with Weak Areas:**
- "Generate 20 questions on my weak areas"
- "Test me on respiratory differentials"
- "NREMT-level questions: cardiology and trauma"

**Study Guides:**
- "Study guide: respiratory distress presentations"
- "Help me understand CPAP vs. BiPAP indications"
- "National Model Guidelines: shock management"

**Scenarios:**
- "Monica Mode: respiratory distress"
- "Standard scenario: chest pain with complications"
- "Recreate scenario: [describe your actual call]"

## 🔄 Next Steps

### Immediate (This Week):
1. ✅ Commit updated prompts to git
2. ✅ Test Pattern Recognition Mode
3. ✅ Upload your comprehensive exam scores
4. ✅ Run 5 respiratory distress drills

### Before ACLS (Early February):
1. Generate cardiology question sets
2. Practice ACLS algorithms via scenarios
3. Use Monica Mode for algorithm speed training

### Before Spring Semester:
1. Build study guides for Cardiology module
2. Preview shock/trauma scenarios
3. Practice medical emergency differentials

## 📝 Git Commit Message

```bash
cd ***REMOVED***
git add prompts/
git commit -m "Update to v1.6.2/1.6.3: Add Pattern Recognition Mode, weak area tracking, National Model Guidelines integration

- Core v1.6.2: Added guideline integration and weak area tracking system
- Student v1.6.3: Added Pattern Recognition Mode for differential diagnosis
- Instructor v1.6.2: Updated to support new student features

Addresses Spring 2026 prep needs:
- Respiratory distress pattern recognition (50% → target 85%+)
- Airway management procedure drills (65% → target 90%+)
- Integration with National Model EMS Clinical Guidelines
- Enhanced Monica Mode for clinical rotation prep"

git push origin main
```

## 🎓 Strategic Focus

**Based on your test analysis:**

**Top Priority (50% scores):**
1. Respiratory distress differentials → Pattern drills daily
2. Head/spine trauma protocols → Study guide + scenarios

**High Priority (65% score):**
3. Airway management procedures → Monica Mode equipment scenarios

**Bloom's Taxonomy gaps:**
4. "Analyzing" questions (67%) → More case-based scenarios
5. "Remembering" questions (71%) → Quick daily fact drills

**Your advantage:**
- 100% on hardest questions → You excel at complex reasoning
- 83% on Understanding → Strong conceptual grasp
- Need: Basic fact memorization and pattern recognition speed

**EMSTrainer now directly addresses your gaps while leveraging your analytical strengths.**

---

**Questions or issues? Check:**
- `***REMOVED***/prompts/` for updated files
- CHANGELOG in each prompt file
- README.md in EMSTrainer root for full documentation
