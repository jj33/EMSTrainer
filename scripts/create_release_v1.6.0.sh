#!/bin/bash
# EMSTrainer v1.6.0 - Automated Release Script
# Creates PR, merges to main, creates GitHub release with packages

set -e

echo "════════════════════════════════════════════════════════════════"
echo "EMSTrainer v1.6.0 - Automated Release"
echo "════════════════════════════════════════════════════════════════"
echo ""

# Check if gh CLI is authenticated
if ! gh auth status &>/dev/null; then
    echo "❌ GitHub CLI not authenticated. Please run: gh auth login"
    exit 1
fi

echo "✅ GitHub CLI authenticated"
echo ""

# Verify we're on dev branch
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "dev" ]; then
    echo "⚠️  Not on dev branch (currently on: $CURRENT_BRANCH)"
    read -p "Switch to dev branch? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git checkout dev
    else
        echo "❌ Aborted. Please switch to dev branch first."
        exit 1
    fi
fi

echo "✅ On dev branch"
echo ""

# Make sure we're up to date
echo "📡 Fetching latest changes..."
git fetch origin
echo ""

# Check if deployment ZIPs exist
if [ ! -f "deployment/EMSTrainer_Instructor_v1.6.0.zip" ]; then
    echo "❌ Instructor package not found: deployment/EMSTrainer_Instructor_v1.6.0.zip"
    exit 1
fi

if [ ! -f "deployment/EMSTrainer_Student_v1.6.0.zip" ]; then
    echo "❌ Student package not found: deployment/EMSTrainer_Student_v1.6.0.zip"
    exit 1
fi

echo "✅ Both deployment packages found"
echo "   - Instructor: $(ls -lh deployment/EMSTrainer_Instructor_v1.6.0.zip | awk '{print $5}')"
echo "   - Student: $(ls -lh deployment/EMSTrainer_Student_v1.6.0.zip | awk '{print $5}')"
echo ""

# Create Pull Request
echo "════════════════════════════════════════════════════════════════"
echo "Step 1: Creating Pull Request (dev → main)"
echo "════════════════════════════════════════════════════════════════"
echo ""

PR_TITLE="Release v1.6.0 - Complete Instructor & Student Packages"
PR_BODY="## v1.6.0 - Major Release

Complete instructor and student deployment packages with comprehensive testing and validation.

### 📦 Two Packages, One Release
- **Instructor Package** (40KB) - Create, deploy, grade scenarios
- **Student Package** (28KB) - Practice and improve skills

### ✅ Highlights
- Modular architecture (Core + Scenario + Instructor)
- 4 difficulty modes (Easy → Monica)
- 30-student stress test: 100% validation pass
- Regression baseline established
- Comprehensive documentation (6 guides + READMEs)

### 🎯 Ready For
- Instructor deployment to classes
- Student practice and certification prep
- Production use

See \`RELEASE_NOTES_v1.6.0.md\` for complete details.

### 📊 Testing Results
- Grade distribution: Perfect match (8A, 4B, 5C, 13D)
- Data integrity: 100%
- ROSC rate: 60% (realistic)
- Mean score: 70.0/100

### 📦 Packages Included
- EMSTrainer_Instructor_v1.6.0.zip (40KB)
- EMSTrainer_Student_v1.6.0.zip (28KB)

Ready to merge and release! 🚀"

# Check if PR already exists
EXISTING_PR=$(gh pr list --base main --head dev --json number --jq '.[0].number' 2>/dev/null || echo "")

if [ -n "$EXISTING_PR" ]; then
    echo "⚠️  Pull request already exists: #$EXISTING_PR"
    read -p "Use existing PR? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        PR_NUMBER=$EXISTING_PR
        echo "✅ Using existing PR #$PR_NUMBER"
    else
        echo "❌ Aborted. Close or merge existing PR first."
        exit 1
    fi
else
    echo "Creating pull request..."
    PR_URL=$(gh pr create \
        --base main \
        --head dev \
        --title "$PR_TITLE" \
        --body "$PR_BODY")
    
    PR_NUMBER=$(echo $PR_URL | grep -o '[0-9]*$')
    echo "✅ Pull request created: $PR_URL"
fi

echo ""

# Ask if ready to merge
echo "════════════════════════════════════════════════════════════════"
echo "Step 2: Merge Pull Request"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "PR #$PR_NUMBER is ready to merge."
read -p "Merge now? (y/n) " -n 1 -r
echo

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "✋ Stopped before merge."
    echo ""
    echo "To continue later, run:"
    echo "  gh pr merge $PR_NUMBER --merge --delete-branch=false"
    echo "  Then run this script again (it will skip to release creation)"
    echo ""
    exit 0
fi

echo ""
echo "Merging PR #$PR_NUMBER..."
gh pr merge $PR_NUMBER --merge --delete-branch=false

echo "✅ Merged to main"
echo ""

# Switch to main and pull
echo "📥 Switching to main branch and pulling..."
git checkout main
git pull origin main
echo ""

# Create Release
echo "════════════════════════════════════════════════════════════════"
echo "Step 3: Creating GitHub Release v1.6.0"
echo "════════════════════════════════════════════════════════════════"
echo ""

RELEASE_NOTES="## Two Packages, One Release

**👨‍🏫 For Instructors:** Download \`EMSTrainer_Instructor_v1.6.0.zip\`  
**👨‍🎓 For Students:** Download \`EMSTrainer_Student_v1.6.0.zip\`

Both packages are standalone and complete. Choose the one you need!

---

## What's New

✨ **Modular architecture** - no more character limits  
✨ **4 difficulty modes** - Easy, Standard, Hard, Monica  
✨ **Instructor tools** - create scenarios, tests, grade submissions  
✨ **Student tools** - practice scenarios, study guides, feedback  
✨ **100% validated** - 30-student stress test passed all checks  

---

## Quick Start

### For Instructors
1. Download instructor package
2. Load into GPT-5 (Copilot/ChatGPT)
3. Drag-and-drop: Core.txt + Instructor_Prompt.txt
4. Type: \"Create a scenario\"

### For Students  
1. Download student package
2. Load into GPT-5 (Copilot/ChatGPT)
3. Drag-and-drop: Core.txt + Scenario_Mode.txt
4. Get scenario from instructor
5. Type: \"Start scenario\"

---

## 📊 Validation Results (30-Student Stress Test)

- **Grade Distribution:** Perfect match to expected (8A, 4B, 5C, 13D)
- **Data Integrity:** 100% (all hashes matched)
- **ROSC Rate:** 60% (realistic outcome)
- **Mean Score:** 70.0/100

---

## 📋 What's Included

### Instructor Package (40KB)
- 3 prompt files (Core, Instructor, Scenario Mode)
- 2 documentation guides (Quick Start, Reference)
- Comprehensive README
- 2 example scenarios

### Student Package (28KB)
- 2 prompt files (Core, Scenario Mode)
- Quick Start Guide
- What's New document
- Comprehensive README

---

## ⚠️ Requirements

- **GPT-5 required** for medical accuracy
- Copilot (free tier works) or ChatGPT
- Drag-and-drop file capability
- No coding knowledge needed

---

## 🔜 Coming in v1.7

- Equipment timing delays (LUCAS, EtCO₂)
- Scenario encryption (AES-256)
- In-prompt scenario editor
- Enhanced reporting
- Multi-agency scenarios

---

## 📞 Documentation

Full documentation included in each package:
- Quick Start Guides
- Reference guides
- Complete READMEs
- Example scenarios

See \`RELEASE_NOTES_v1.6.0.md\` for complete details.

---

**Note to Beta Testers:** Thanks for testing! This is the official v1.6.0 release with both instructor and student packages. Please download the updated version.

---

*Live long and prosper!* 🖖"

echo "Creating release v1.6.0..."
gh release create v1.6.0 \
    --title "EMSTrainer v1.6.0 - Complete Instructor & Student Packages" \
    --notes "$RELEASE_NOTES" \
    --target main \
    --latest \
    deployment/EMSTrainer_Instructor_v1.6.0.zip \
    deployment/EMSTrainer_Student_v1.6.0.zip

echo ""
echo "✅ Release v1.6.0 created!"
echo ""

# Show release URL
RELEASE_URL=$(gh release view v1.6.0 --json url --jq '.url')
echo "🎉 Release published: $RELEASE_URL"
echo ""

echo "════════════════════════════════════════════════════════════════"
echo "Step 4: GitHub Actions - PDF Generation"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "GitHub Actions is now automatically generating PDFs..."
echo "This will take 2-3 minutes."
echo ""
echo "Watch progress:"
echo "  https://github.com/jj33/EMSTrainer/actions"
echo ""
echo "PDFs will be automatically attached to the release when complete."
echo ""

read -p "Open Actions page in browser? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    open "https://github.com/jj33/EMSTrainer/actions" 2>/dev/null || \
    xdg-open "https://github.com/jj33/EMSTrainer/actions" 2>/dev/null || \
    echo "Please open: https://github.com/jj33/EMSTrainer/actions"
fi

echo ""
echo "════════════════════════════════════════════════════════════════"
echo "🎉 Release Complete!"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "✅ Pull Request merged"
echo "✅ Release v1.6.0 published"
echo "✅ Both packages attached"
echo "⏳ PDFs generating (check Actions tab)"
echo ""
echo "Release URL: $RELEASE_URL"
echo ""
echo "Next steps:"
echo "  1. Wait for PDF generation (2-3 min)"
echo "  2. Verify PDFs attached to release"
echo "  3. Share release link with instructors/students"
echo "  4. Notify beta testers to upgrade"
echo ""
echo "Done! 🚀"
