# LPERL Assessment Tool - Quick Setup Guide

## Simple Setup (Recommended)

### Step 1: Create Virtual Environment
```bash
python3 setup.py
```

### Step 2: Activate Virtual Environment  
```bash
source venv/bin/activate
```
Your terminal prompt should now show `(venv)` at the beginning.

### Step 3: Install Dependencies
Start with minimal dependencies:
```bash
pip install -r requirements-minimal.txt
```

Or for full features including graphs:
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Open Your Browser
Go to: **http://localhost:5000**

## That's it! 

### To use it again later:
1. `source venv/bin/activate` (to activate the virtual environment)
2. `python app.py` (to run the app)

### To stop:
- Press `Ctrl+C` in the terminal where the app is running

### If matplotlib fails to install:
The tool works fine without matplotlib - you just won't get the score progression graphs. To fix matplotlib later, you might need to install system dependencies first.