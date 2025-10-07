#!/bin/bash
# EMSTrainer - Generate PDFs from Markdown documentation
# Requires: pandoc and wkhtmltopdf (installs if needed)

set -e

echo "=== EMSTrainer PDF Generator ==="
echo ""

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "📦 Pandoc not found. Installing via Homebrew..."
    if ! command -v brew &> /dev/null; then
        echo "❌ Error: Homebrew not installed. Please install from https://brew.sh"
        exit 1
    fi
    brew install pandoc
fi

# Check if wkhtmltopdf is installed (optional, for better PDF formatting)
if ! command -v wkhtmltopdf &> /dev/null; then
    echo "⚠️  wkhtmltopdf not found. PDFs will be basic format."
    echo "   To install: brew install --cask wkhtmltopdf"
    USE_WKHTMLTOPDF=false
else
    USE_WKHTMLTOPDF=true
fi

echo ""
echo "✅ PDF generator ready!"
echo ""

# Create output directory
mkdir -p docs/pdf

# Define files to convert
FILES=(
    "docs/Instructor_Quick_Start_Guide.md"
    "docs/Instructor_Reference_Guide.md"
    "docs/Student_Quick_Start_Guide.md"
    "docs/WHATS_NEW_v1.6.0.md"
    "docs/READY_FOR_TESTING_v1.6.0.md"
    "README.md"
)

# Convert each file
for FILE in "${FILES[@]}"; do
    if [ -f "$FILE" ]; then
        BASENAME=$(basename "$FILE" .md)
        OUTPUT="docs/pdf/${BASENAME}.pdf"
        
        echo "📄 Converting: $FILE"
        
        if [ "$USE_WKHTMLTOPDF" = true ]; then
            # Better formatting with wkhtmltopdf
            pandoc "$FILE" -o "$OUTPUT" \
                --pdf-engine=wkhtmltopdf \
                --metadata title="EMSTrainer - $BASENAME" \
                --toc \
                -V geometry:margin=1in
        else
            # Basic PDF
            pandoc "$FILE" -o "$OUTPUT" \
                --metadata title="EMSTrainer - $BASENAME" \
                --toc \
                -V geometry:margin=1in
        fi
        
        echo "   ✅ Created: $OUTPUT"
    else
        echo "   ⚠️  File not found: $FILE"
    fi
done

echo ""
echo "=== PDF Generation Complete ==="
echo "📁 Output directory: docs/pdf/"
echo ""
ls -lh docs/pdf/*.pdf
