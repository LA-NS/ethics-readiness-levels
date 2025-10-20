#!/usr/bin/env python3
"""
LPERL Assessment Tool - One-time Setup
Creates a virtual environment for the LPERL tool (run once).
"""

import os
import sys
import subprocess

def main():
    print("🔧 LPERL Assessment Tool - One-time Setup")
    print("=" * 50)
    
    # Check if virtual environment already exists
    if os.path.exists("venv"):
        print("✅ Virtual environment already exists!")
        print("\nTo use the LPERL tool:")
        print("1️⃣  Activate the virtual environment:")
        print("   source venv/bin/activate")
        print("2️⃣  Install dependencies (if not done yet):")
        print("   pip install -r requirements.txt")
        print("3️⃣  Run the application:")
        print("   python app.py")
        print("4️⃣  Open your browser to: http://localhost:5000")
        return
    
    # Create virtual environment
    print("📋 Creating virtual environment...")
    result = subprocess.run([sys.executable, "-m", "venv", "venv"], capture_output=True, text=True)
    
    if result.returncode != 0:
        print("❌ Failed to create virtual environment")
        print(f"Error: {result.stderr}")
        print("\nMake sure you have Python 3 with venv module installed")
        return
    
    print("✅ Virtual environment created successfully!")
    print("\n🎉 Setup complete!")
    print("\nNext steps:")
    print("1️⃣  Activate the virtual environment:")
    print("   source venv/bin/activate")
    print("2️⃣  Install dependencies:")
    print("   pip install -r requirements.txt")
    print("3️⃣  Run the application:")
    print("   python app.py")
    print("4️⃣  Open your browser to: http://localhost:5000")
    print("\n💡 Tip: Once activated, your terminal prompt will show (venv)")

if __name__ == "__main__":
    main()