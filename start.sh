#!/bin/bash
# LPERL Assessment Tool - Quick Start Script with Virtual Environment

echo "LPERL Assessment Tool - Setup and Launch"
echo "========================================"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not found."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create virtual environment."
        echo "Please ensure you have venv module available."
        exit 1
    fi
    echo "Virtual environment created successfully!"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies in virtual environment
echo "Installing Python dependencies in virtual environment..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "Dependencies installed successfully!"
    echo "Starting LPERL Assessment Tool..."
    echo ""
    echo "🌐 Open your web browser and go to: http://localhost:5000"
    echo "⏹️  Press Ctrl+C to stop the server when finished."
    echo ""
    python app.py
else
    echo "Error: Failed to install dependencies."
    echo "Please check your internet connection and try again."
    deactivate
    exit 1
fi

# Deactivate virtual environment when script ends
deactivate