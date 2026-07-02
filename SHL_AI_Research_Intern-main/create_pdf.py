"""
Script to convert APPROACH_CONCISE.md to PDF format
"""

import os
import subprocess
import sys

def create_pdf_from_markdown():
    """Convert markdown to PDF"""
    
    input_file = 'APPROACH_CONCISE.md'
    output_file = 'APPROACH_JAY_TIWARI.pdf'
    
    print("="*60)
    print("Creating PDF from Approach Document")
    print("="*60)
    
    # Method 1: Try using markdown-pdf (if installed)
    try:
        result = subprocess.run(
            ['npx', '--yes', 'markdown-pdf', input_file, '-o', output_file],
            capture_output=True,
            text=True,
            timeout=60
        )
        if os.path.exists(output_file):
            print(f"\n[SUCCESS] PDF created: {output_file}")
            return True
    except Exception as e:
        print(f"Method 1 failed: {e}")
    
    # Method 2: Try using pandoc (if installed)
    try:
        result = subprocess.run(
            ['pandoc', input_file, '-o', output_file, '--pdf-engine=wkhtmltopdf'],
            capture_output=True,
            text=True,
            timeout=60
        )
        if os.path.exists(output_file):
            print(f"\n[SUCCESS] PDF created: {output_file}")
            return True
    except Exception as e:
        print(f"Method 2 failed: {e}")
    
    # Method 3: Try using markdown2pdf
    try:
        import markdown2
        from weasyprint import HTML, CSS
        from weasyprint.text.fonts import FontConfiguration
        
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Convert markdown to HTML
        html_content = markdown2.markdown(markdown_content)
        
        # Add basic styling
        styled_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    margin: 40px;
                    max-width: 800px;
                }}
                h1 {{
                    color: #333;
                    border-bottom: 2px solid #667eea;
                    padding-bottom: 10px;
                }}
                h2 {{
                    color: #555;
                    margin-top: 30px;
                }}
                h3 {{
                    color: #777;
                    margin-top: 20px;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 5px;
                    border-radius: 3px;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 10px;
                    border-radius: 5px;
                    overflow-x: auto;
                }}
            </style>
        </head>
        <body>
        {html_content}
        </body>
        </html>
        """
        
        HTML(string=styled_html).write_pdf(output_file)
        print(f"\n[SUCCESS] PDF created: {output_file}")
        return True
        
    except ImportError:
        print("\n[INFO] PDF generation libraries not installed.")
        print("\nTo create PDF, you can:")
        print("1. Install markdown-pdf: npm install -g markdown-pdf")
        print("2. Install pandoc: https://pandoc.org/installing.html")
        print("3. Use online converter: https://www.markdowntopdf.com/")
        print("4. Use Python libraries: pip install markdown2 weasyprint")
        return False
    except Exception as e:
        print(f"Method 3 failed: {e}")
        return False

def create_html_version():
    """Create HTML version that can be printed to PDF"""
    input_file = 'APPROACH_CONCISE.md'
    output_file = 'APPROACH_JAY_TIWARI.html'
    
    try:
        import markdown2
        
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        html_content = markdown2.markdown(markdown_content, extras=['fenced-code-blocks', 'tables'])
        
        styled_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>SHL Assessment Recommendation System - Approach Document</title>
            <style>
                @media print {{
                    @page {{
                        size: A4;
                        margin: 2cm;
                    }}
                    body {{
                        font-size: 11pt;
                    }}
                }}
                body {{
                    font-family: 'Segoe UI', Arial, sans-serif;
                    line-height: 1.6;
                    margin: 40px auto;
                    max-width: 800px;
                    color: #333;
                }}
                h1 {{
                    color: #667eea;
                    border-bottom: 3px solid #667eea;
                    padding-bottom: 10px;
                    page-break-after: avoid;
                }}
                h2 {{
                    color: #555;
                    margin-top: 30px;
                    page-break-after: avoid;
                }}
                h3 {{
                    color: #777;
                    margin-top: 20px;
                    page-break-after: avoid;
                }}
                p {{
                    text-align: justify;
                    margin: 10px 0;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 5px;
                    border-radius: 3px;
                    font-family: 'Courier New', monospace;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 15px;
                    border-radius: 5px;
                    overflow-x: auto;
                    border-left: 4px solid #667eea;
                }}
                ul, ol {{
                    margin: 10px 0;
                    padding-left: 30px;
                }}
                li {{
                    margin: 5px 0;
                }}
                strong {{
                    color: #667eea;
                }}
            </style>
        </head>
        <body>
        {html_content}
        </body>
        </html>
        """
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(styled_html)
        
        print(f"\n[SUCCESS] HTML version created: {output_file}")
        print("\nTo convert to PDF:")
        print("1. Open the HTML file in your browser")
        print("2. Press Ctrl+P (or Cmd+P on Mac)")
        print("3. Select 'Save as PDF' as the destination")
        print("4. Set margins to 'Minimum' and ensure 'Background graphics' is enabled")
        print("5. Save as APPROACH_JAY_TIWARI.pdf")
        return True
        
    except ImportError:
        print("\n[INFO] markdown2 not installed. Installing...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'markdown2'])
            return create_html_version()
        except:
            print("\n[ERROR] Could not install markdown2")
            return False
    except Exception as e:
        print(f"\n[ERROR] Failed to create HTML: {e}")
        return False

if __name__ == '__main__':
    print("Creating PDF from Approach Document...")
    print("Submission by: Jay Tiwari")
    print("Position: AI Reach Intern")
    print("Company: SHL Company\n")
    
    # Try to create PDF directly
    if not create_pdf_from_markdown():
        # Fallback: Create HTML that can be printed to PDF
        print("\nFalling back to HTML version...")
        create_html_version()

