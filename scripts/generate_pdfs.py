#!/usr/bin/env python3
"""
EMSTrainer - Generate PDFs from Markdown documentation
Pure Python solution - no external dependencies except pip packages
"""

import os
import sys
import subprocess
from pathlib import Path

def check_and_install_dependencies():
    """Check for required Python packages and install if needed"""
    required = ['markdown', 'weasyprint']
    missing = []
    
    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"📦 Installing required packages: {', '.join(missing)}")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing)
        print("✅ Dependencies installed!")
    
    return True

def markdown_to_html(md_file):
    """Convert markdown to HTML"""
    import markdown
    
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Configure markdown with extensions
    html = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'toc', 'codehilite']
    )
    
    # Add CSS styling
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>{md_file.stem}</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                line-height: 1.6;
                padding: 2em;
                max-width: 900px;
                margin: 0 auto;
                color: #333;
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 0.3em;
            }}
            h2 {{
                color: #34495e;
                border-bottom: 2px solid #95a5a6;
                padding-bottom: 0.3em;
                margin-top: 1.5em;
            }}
            h3 {{
                color: #34495e;
            }}
            code {{
                background-color: #f4f4f4;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: 'Monaco', 'Courier New', monospace;
            }}
            pre {{
                background-color: #f4f4f4;
                padding: 1em;
                border-radius: 5px;
                overflow-x: auto;
            }}
            pre code {{
                background-color: transparent;
                padding: 0;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 1em 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #3498db;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
            blockquote {{
                border-left: 4px solid #3498db;
                padding-left: 1em;
                margin-left: 0;
                color: #555;
            }}
            .footer {{
                margin-top: 3em;
                padding-top: 1em;
                border-top: 1px solid #ddd;
                color: #777;
                font-size: 0.9em;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        {html}
        <div class="footer">
            <p>EMSTrainer Documentation | Generated from {md_file.name}</p>
        </div>
    </body>
    </html>
    """
    
    return styled_html

def html_to_pdf(html_content, output_file):
    """Convert HTML to PDF using WeasyPrint"""
    from weasyprint import HTML
    
    HTML(string=html_content).write_pdf(output_file)

def convert_file(md_file, output_dir):
    """Convert a single markdown file to PDF"""
    md_path = Path(md_file)
    
    if not md_path.exists():
        print(f"   ⚠️  File not found: {md_file}")
        return False
    
    output_file = output_dir / f"{md_path.stem}.pdf"
    
    print(f"📄 Converting: {md_file}")
    
    try:
        # Convert markdown to HTML
        html = markdown_to_html(md_path)
        
        # Convert HTML to PDF
        html_to_pdf(html, str(output_file))
        
        # Get file size
        size = output_file.stat().st_size
        size_kb = size / 1024
        print(f"   ✅ Created: {output_file} ({size_kb:.1f} KB)")
        return True
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def main():
    print("=== EMSTrainer PDF Generator ===")
    print("")
    
    # Check and install dependencies
    try:
        check_and_install_dependencies()
    except Exception as e:
        print(f"❌ Failed to install dependencies: {e}")
        print("   Try: pip3 install markdown weasyprint")
        return 1
    
    # Create output directory
    output_dir = Path('docs/pdf')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Files to convert
    files = [
        'docs/Instructor_Quick_Start_Guide.md',
        'docs/Instructor_Reference_Guide.md',
        'docs/Student_Quick_Start_Guide.md',
        'docs/WHATS_NEW_v1.6.0.md',
        'docs/READY_FOR_TESTING_v1.6.0.md',
        'README.md',
    ]
    
    print("")
    success = 0
    failed = 0
    
    for file in files:
        if convert_file(file, output_dir):
            success += 1
        else:
            failed += 1
    
    print("")
    print("=== PDF Generation Complete ===")
    print(f"✅ Successful: {success}")
    if failed > 0:
        print(f"❌ Failed: {failed}")
    print(f"📁 Output directory: {output_dir}/")
    print("")
    
    # List generated files
    pdf_files = sorted(output_dir.glob('*.pdf'))
    if pdf_files:
        for pdf_file in pdf_files:
            size = pdf_file.stat().st_size / 1024
            print(f"   {pdf_file.name} ({size:.1f} KB)")
    
    return 0 if failed == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
