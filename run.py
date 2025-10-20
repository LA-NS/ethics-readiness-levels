#!/usr/bin/env python3
"""
LPERL Assessment Tool Launcher

Simple launcher script for the local LPERL assessment tool.
"""

import sys
import os
import subprocess

def check_virtual_env():
    """Check if we're in a virtual environment, if not, try to activate one."""
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        # Not in virtual environment
        venv_path = os.path.join(os.getcwd(), 'venv')
        if os.path.exists(venv_path):
            print("Virtual environment found. Please run:")
            print("source venv/bin/activate")
            print("python run.py")
            return False
        else:
            print("Virtual environment not found. Please run:")
            print("./start.sh")
            print("This will create a virtual environment and install dependencies.")
            return False
    return True

def install_dependencies():
    """Install required dependencies."""
    try:
        import flask
        import matplotlib
        return True
    except ImportError:
        print("Installing dependencies...")
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("Dependencies installed successfully!")
            return True
        else:
            print("Failed to install dependencies. Error:")
            print(result.stderr)
            return False

def main():
    print("LPERL Assessment Tool - Local Version")
    print("=" * 50)
    
    # Check virtual environment
    if not check_virtual_env():
        return
        
    print("This tool evaluates the Legal, Privacy, and Ethical")
    print("Readiness Level (LPERL) of your technology project.")
    print()
    print("Choose an option:")
    print("1. Start LPERL Assessment")
    print("2. View project information")
    print("3. Install/Check dependencies")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            if not install_dependencies():
                print("Cannot start assessment without dependencies.")
                continue
                
            print("\nStarting LPERL Assessment Tool...")
            print("The application will open in your web browser.")
            print("Go to: http://localhost:5000")
            print("Press Ctrl+C in this terminal to stop the server when done.")
            print()
            
            try:
                os.system("python app.py")
            except KeyboardInterrupt:
                print("\nServer stopped.")
            break
            
        elif choice == '2':
            print("\nLPERL Assessment Tool Information:")
            print("- Evaluates ethical, legal, and privacy readiness")
            print("- Covers 4 assessment blocks: Basic Ethics, GDPR, AI, Law Enforcement")
            print("- Provides scores from LPERL 0 (lacking) to LPERL 4 (excellent)")
            print("- Generates detailed score progression graphs")
            print("- Completely local - no data leaves your computer")
            print("- Based on actual LPERL framework questions")
            print("- 129 validated questions across all domains")
            input("\nPress Enter to return to main menu...")
            
        elif choice == '3':
            if install_dependencies():
                print("All dependencies are installed and ready!")
            else:
                print("Failed to install dependencies. Try running ./start.sh instead.")
            input("\nPress Enter to return to main menu...")
            
        elif choice == '4':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == '__main__':
    main()