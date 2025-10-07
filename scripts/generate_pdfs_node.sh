#!/bin/bash
# EMSTrainer - Generate PDFs using Node.js md-to-pdf
# Best local option - clean PDFs, preserves formatting

set -e

echo "=== EMSTrainer PDF Generator (Node.js) ==="
echo ""

# Check if npm is available
if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install Node.js from nodejs.org"
    exit 1
fi

# Check if md-to-pdf is installed globally, if not install it
if ! command -v md-to-pdf &> /dev/null; then
    echo "📦 Installing md-to-pdf..."
    npm install -g md-to-pdf
    echo "✅ md-to-pdf installed!"
fi

echo ""
echo "✅ PDF generator ready!"
echo ""

# Create output directory
mkdir -p docs/pdf

# Files to convert
FILES=(
    "docs/Instructor_Quick_Start_Guide.md"
    "docs/Instructor_Reference_Guide.md"
    "docs/Student_Quick_Start_Guide.md"
    "docs/WHATS_NEW_v1.6.0.md"
    "docs/READY_FOR_TESTING_v1.6.0.md"
    "README.md"
)

SUCCESS=0
FAILED=0

# Convert each file
for FILE in "${FILES[@]}"; do
    if [ ! -f "$FILE" ]; then
        echo "⚠️  File not found: $FILE"
        ((FAILED++))
        continue
    fi
    
    BASENAME=$(basename "$FILE" .md)
    OUTPUT="docs/pdf/${BASENAME}.pdf"
    
    echo "📄 Converting: $FILE"
    
    if md-to-pdf "$FILE" --dest "$OUTPUT" --stylesheet "https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.1.0/github-markdown.min.css" 2>/dev/null; then
        SIZE=$(du -h "$OUTPUT" | cut -f1)
        echo "   ✅ Created: $OUTPUT ($SIZE)"
        ((SUCCESS++))
    else
        echo "   ❌ Failed to convert $FILE"
        ((FAILED++))
    fi
done

echo ""
echo "=== PDF Generation Complete ==="
echo "✅ Successful: $SUCCESS"
if [ $FAILED -gt 0 ]; then
    echo "❌ Failed: $FAILED"
fi
echo "📁 Output directory: docs/pdf/"
echo ""

# List generated files
if ls docs/pdf/*.pdf 1> /dev/null 2>&1; then
    ls -lh docs/pdf/*.pdf
else
    echo "No PDFs generated"
fi
