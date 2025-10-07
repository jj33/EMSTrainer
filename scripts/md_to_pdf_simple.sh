#!/bin/bash
# Simple Markdown to PDF converter using macOS textutil + cupsfilter
# No external dependencies needed!

set -e

echo "=== Simple MD → PDF Converter (macOS) ==="
echo ""

# Check if we're on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "❌ This script requires macOS"
    exit 1
fi

# Create output directory
mkdir -p docs/pdf

# Files to convert
FILES=(
    "docs/Instructor_Quick_Start_Guide.md"
    "docs/Instructor_Reference_Guide.md"
    "docs/Student_Quick_Start_Guide.md"
)

echo "Converting Markdown files to PDF..."
echo ""

for MD_FILE in "${FILES[@]}"; do
    if [ ! -f "$MD_FILE" ]; then
        echo "⚠️  File not found: $MD_FILE"
        continue
    fi
    
    BASENAME=$(basename "$MD_FILE" .md)
    HTML_FILE="docs/pdf/${BASENAME}.html"
    PDF_FILE="docs/pdf/${BASENAME}.pdf"
    
    echo "📄 Converting: $MD_FILE"
    
    # Convert MD to HTML with basic styling
    cat > "$HTML_FILE" << EOF
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>${BASENAME}</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            line-height: 1.6;
            padding: 2em;
            max-width: 900px;
            margin: 0 auto;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 0.3em;
        }
        h2 {
            color: #34495e;
            border-bottom: 2px solid #95a5a6;
            padding-bottom: 0.3em;
            margin-top: 1.5em;
        }
        h3 { color: #34495e; }
        code {
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: Monaco, 'Courier New', monospace;
        }
        pre {
            background-color: #f4f4f4;
            padding: 1em;
            border-radius: 5px;
            overflow-x: auto;
        }
        pre code {
            background-color: transparent;
            padding: 0;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #3498db;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        blockquote {
            border-left: 4px solid #3498db;
            padding-left: 1em;
            margin-left: 0;
            color: #555;
        }
    </style>
</head>
<body>
<pre>
EOF
    
    # Append markdown content (simple text rendering)
    cat "$MD_FILE" >> "$HTML_FILE"
    
    cat >> "$HTML_FILE" << EOF
</pre>
</body>
</html>
EOF
    
    # Convert HTML to PDF using Safari's print functionality
    echo "   Converting to PDF via Safari..."
    /usr/bin/open -a "Safari" "$HTML_FILE"
    
    echo "   ⏳ Please manually: File → Export as PDF → Save to: $PDF_FILE"
    echo "   Press Enter when done..."
    read -r
    
done

echo ""
echo "=== Conversion Process Complete ==="
echo "📁 Check: docs/pdf/"
echo ""
ls -lh docs/pdf/*.pdf 2>/dev/null || echo "No PDFs found yet"
