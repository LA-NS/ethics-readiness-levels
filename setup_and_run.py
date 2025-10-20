#!/usr/bin/env python3
"""
LPERL Assessment Tool - Simple Setup and Launcher
This script sets up a virtual environment and runs the LPERL tool.
"""

import os
import sys
import subprocess

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"📋 {description}...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error: {description} failed")
        print(f"Error output: {result.stderr}")
        return False
    print(f"✅ {description} completed successfully")
    return True

def main():
    print("🔧 LPERL Assessment Tool - Setup")
    print("=" * 40)
    
    # Check if virtual environment exists
    if not os.path.exists("venv"):
        if not run_command("python3 -m venv venv", "Creating virtual environment"):
            print("❌ Failed to create virtual environment")
            print("Make sure you have Python 3 with venv module installed")
            return False
    else:
        print("✅ Virtual environment already exists")
    
    # Install dependencies
    activate_cmd = "source venv/bin/activate &&" if os.name != 'nt' else "venv\\Scripts\\activate &&"
    install_cmd = f"{activate_cmd} pip install -r requirements.txt"
    
    if not run_command(install_cmd, "Installing dependencies"):
        print("❌ Failed to install dependencies")
        return False
    
    # Run the application
    print("\n🚀 Starting LPERL Assessment Tool...")
    print("🌐 Open your browser and go to: http://localhost:5000")
    print("⏹️  Press Ctrl+C here to stop the server")
    print("-" * 40)
    
    run_cmd = f"{activate_cmd} python app.py"
    subprocess.run(run_cmd, shell=True)
    
    return True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 LPERL Assessment Tool stopped")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)