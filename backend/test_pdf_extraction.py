"""
Quick diagnostic script to test PDF extraction
Run this to see what's wrong with pdfplumber
"""
import sys

print("=== PDF Extraction Diagnostic ===\n")

# Test 1: Check pdfplumber import
print("1. Testing pdfplumber import...")
try:
    import pdfplumber
    print(f"   ✓ pdfplumber installed (version: {pdfplumber.__version__})")
except ImportError as e:
    print(f"   ✗ pdfplumber NOT installed: {e}")
    print("   Run: pip install pdfplumber")
    sys.exit(1)

# Test 2: Check if demo PDF exists
print("\n2. Checking for demo PDF...")
import os
demo_pdf = "demo_data/sample_cams.pdf"
if os.path.exists(demo_pdf):
    print(f"   ✓ Demo PDF found: {demo_pdf}")
    
    # Test 3: Try extracting from demo PDF
    print("\n3. Testing extraction from demo PDF...")
    try:
        from utils.pdf_extractor import extract_text_from_path
        text = extract_text_from_path(demo_pdf)
        print(f"   ✓ Extraction successful!")
        print(f"   Extracted {len(text)} characters")
        print(f"   First 200 chars: {text[:200]}")
    except Exception as e:
        print(f"   ✗ Extraction failed: {e}")
        import traceback
        traceback.print_exc()
else:
    print(f"   ⚠ Demo PDF not found: {demo_pdf}")
    print("   Upload a real PDF to test")

# Test 4: Check dependencies
print("\n4. Checking pdfplumber dependencies...")
try:
    import PIL
    print(f"   ✓ Pillow (PIL) installed")
except ImportError:
    print(f"   ✗ Pillow missing (required by pdfplumber)")
    print("   Run: pip install Pillow")

try:
    import pdfminer
    print(f"   ✓ pdfminer.six installed")
except ImportError:
    print(f"   ✗ pdfminer.six missing (required by pdfplumber)")
    print("   Run: pip install pdfminer.six")

print("\n=== Diagnostic Complete ===")
