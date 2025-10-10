#!/usr/bin/env python3
"""
EMSTrainer - Generate PDFs from Markdown documentation
Uses reportlab (pure Python, no system dependencies)
"""

import os
import sys
import subprocess
import re
from pathlib import Path

def check_and_install_dependencies():
    """Check for required Python packages and install if needed"""
    required = ['markdown2', 'reportlab']
    missing = []
    
    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"📦 Installing required packages: {', '.join(missing)}")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--quiet'] + missing)
            print("✅ Dependencies installed!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install: {e}")
            return False
    
    return True

def markdown_to_pdf(md_file, output_file):
    """Convert markdown directly to PDF using reportlab"""
    import markdown2
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
    from reportlab.platypus import Table, TableStyle
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT, TA_CENTER
    from reportlab.pdfgen import canvas
    
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert markdown to HTML
    html = markdown2.markdown(md_content, extras=['tables', 'fenced-code-blocks', 'header-ids'])
    
    # Create PDF
    doc = SimpleDocTemplate(
        str(output_file),
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=30,
        spaceBefore=0,
        leading=28
    )
    
    h1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=12,
        spaceBefore=12,
        leading=22
    )
    
    h2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=10,
        spaceBefore=10,
        leading=18
    )
    
    h3_style = ParagraphStyle(
        'CustomHeading3',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=8,
        spaceBefore=8
    )
    
    code_style = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontSize=9,
        textColor=colors.black,
        backColor=colors.HexColor('#f4f4f4'),
        leftIndent=20,
        rightIndent=20,
        spaceAfter=10,
        spaceBefore=10
    )
    
    normal_style = styles['Normal']
    normal_style.fontSize = 10
    normal_style.leading = 14
    
    # Parse HTML and create story
    story = []
    
    # Simple HTML parser
    lines = html.split('\n')
    i = 0
    first_h1 = True
    
    while i < len(lines):
        line = lines[i].strip()
        
        if not line:
            i += 1
            continue
        
        # Headers
        if line.startswith('<h1'):
            text = re.sub(r'<.*?>', '', line)
            if first_h1:
                story.append(Paragraph(text, title_style))
                first_h1 = False
            else:
                story.append(Paragraph(text, h1_style))
        elif line.startswith('<h2'):
            text = re.sub(r'<.*?>', '', line)
            story.append(Spacer(1, 0.1*inch))
            story.append(Paragraph(text, h2_style))
        elif line.startswith('<h3'):
            text = re.sub(r'<.*?>', '', line)
            story.append(Paragraph(text, h3_style))
        # Code blocks
        elif line.startswith('<pre><code>'):
            code_lines = []
            while i < len(lines) and '</code></pre>' not in lines[i]:
                code_line = re.sub(r'<.*?>', '', lines[i])
                if code_line:
                    code_lines.append(code_line)
                i += 1
            if code_lines:
                code_text = '<br/>'.join(code_lines)
                story.append(Paragraph(code_text, code_style))
        # Lists
        elif line.startswith('<ul>') or line.startswith('<ol>'):
            list_items = []
            i += 1
            while i < len(lines) and not (lines[i].strip().startswith('</ul>') or lines[i].strip().startswith('</ol>')):
                if lines[i].strip().startswith('<li>'):
                    text = re.sub(r'<.*?>', '', lines[i].strip())
                    list_items.append(text)
                i += 1
            for item in list_items:
                story.append(Paragraph(f"• {item}", normal_style))
            story.append(Spacer(1, 0.1*inch))
        # Paragraphs
        elif line.startswith('<p>'):
            text = re.sub(r'<.*?>', '', line)
            # Handle inline code
            text = re.sub(r'`([^`]+)`', r'<font face="Courier">\1</font>', text)
            # Handle bold
            text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
            # Handle italic
            text = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', text)
            if text:
                story.append(Paragraph(text, normal_style))
                story.append(Spacer(1, 0.05*inch))
        
        i += 1
    
    # Add footer
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.grey,
        alignment=TA_CENTER
    )
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph(f"EMSTrainer Documentation | Generated from {md_file.name}", footer_style))
    
    # Build PDF
    doc.build(story)
    
    return True

def convert_file(md_file, output_dir):
    """Convert a single markdown file to PDF"""
    md_path = Path(md_file)
    
    if not md_path.exists():
        print(f"   ⚠️  File not found: {md_file}")
        return False
    
    output_file = output_dir / f"{md_path.stem}.pdf"
    
    print(f"📄 Converting: {md_file}")
    
    try:
        # Convert markdown to PDF
        markdown_to_pdf(md_path, output_file)
        
        # Get file size
        size = output_file.stat().st_size
        size_kb = size / 1024
        print(f"   ✅ Created: {output_file} ({size_kb:.1f} KB)")
        return True
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=== EMSTrainer PDF Generator ===")
    print("")
    
    # Check and install dependencies
    if not check_and_install_dependencies():
        print("❌ Failed to install dependencies")
        print("   Try manually: pip3 install markdown2 reportlab")
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
