import os
import subprocess
import sys
from pathlib import Path

def generate_pdf():
    script_dir = Path(__file__).parent.resolve()
    html_file = script_dir / "index.html"
    pdf_file = script_dir / "shehane_logan_resume.pdf"
    
    # Candidate browser executables on Windows
    browsers = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]
    
    browser_path = None
    for b in browsers:
        if os.path.exists(b):
            browser_path = b
            break
            
    if not browser_path:
        print("Error: Chrome or Edge not found.")
        sys.exit(1)
        
    print(f"Using browser: {browser_path}")
    print(f"Rendering {html_file} -> {pdf_file}")
    
    file_url = html_file.as_uri()
    
    cmd = [
        browser_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_file}",
        file_url
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Successfully generated PDF at: {pdf_file}")
    else:
        print(f"PDF generation failed: {result.stderr}")
        sys.exit(result.returncode)

if __name__ == "__main__":
    generate_pdf()
