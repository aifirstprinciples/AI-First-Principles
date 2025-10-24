#!/usr/bin/env python3
"""
PDF Generation Helper Script using WeasyPrint

This script properly configures the environment for WeasyPrint on macOS
to work with Homebrew-installed dependencies.

Usage:
    python3 generate_pdf.py input.html output.pdf
"""

import sys
import os

# Set library paths BEFORE importing weasyprint
os.environ['DYLD_LIBRARY_PATH'] = '/opt/homebrew/lib'
os.environ['DYLD_FALLBACK_LIBRARY_PATH'] = '/opt/homebrew/lib'

from weasyprint import HTML

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 generate_pdf.py input.html output.pdf")
        sys.exit(1)
    
    input_html = sys.argv[1]
    output_pdf = sys.argv[2]
    
    if not os.path.exists(input_html):
        print(f"Error: Input file '{input_html}' not found")
        sys.exit(1)
    
    try:
        print(f"Generating PDF from '{input_html}' to '{output_pdf}'...")
        HTML(input_html).write_pdf(output_pdf)
        
        # Get file size
        size = os.path.getsize(output_pdf)
        print(f"✓ Success! Generated {output_pdf} ({size:,} bytes)")
        
    except Exception as e:
        print(f"✗ Error generating PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

