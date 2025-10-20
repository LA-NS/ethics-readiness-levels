# LPERL Assessment Tool - Local Version

LPERL (Legal, Privacy, Ethical Readiness Level) Assessment Tool is a completely local Flask web application that evaluates the ethical, legal, and privacy readiness of technology projects using the actual LPERL framework questions.

## Features

- **Comprehensive Assessment**: Uses the real LPERL framework with 129 validated questions across 4 blocks
- **Multi-block Evaluation**: Dynamically includes relevant assessment blocks based on your project:
  - **Zero Case** (Basic Ethics) - included for all projects (35 questions)
  - **GDPR Block** - for projects using personal data (41 questions) 
  - **AI Block** - for projects using artificial intelligence (30 questions)
  - **LED Block** - for Law Enforcement Agency products (23 questions)

- **Intelligent Navigation**: Hierarchical question flow that adapts based on your answers
- **Real-time Scoring**: Dynamic score calculation with detailed progression tracking
- **Visual Results**: Generates professional score progression graphs with LPERL level indicators
- **Completely Local**: No data leaves your computer - fully offline operation
- **No Dependencies**: Uses only SQLite - no external database setup required

## Quick Start

**🚀 Easiest way (Recommended):**
```bash
python3 setup_and_run.py
```

**🛠️ Using the shell script:**
```bash
./start.sh
```

**📋 Manual setup:**
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

**🎮 Interactive launcher:**
```bash
# After dependencies are installed
source venv/bin/activate
python run.py
```

Then open your browser and go to: **http://localhost:5000**

## Project Structure

```
erl_tool/
├── app.py                 # Main Flask application
├── run.py                 # Launcher script
├── templates/
│   └── index.html         # Web interface
├── static/               # Generated score graphs
├── schema.sql           # Database schema with actual LPERL questions
├── questions.sql        # Original MySQL dump (reference)
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── lperl_local.sqlite  # Auto-generated database (after first run)
```

## LPERL Assessment Process

### 1. Initial Classification
Answer three determining questions to identify which assessment blocks apply to your project:
- **LEA Product**: Is your product created for Law Enforcement Agencies?
- **Personal Data**: Does your product use personal data?
- **AI Technology**: Does your product use artificial intelligence?

### 2. Dynamic Question Flow
The tool uses hierarchical question navigation:
- **"Yes" answers** typically lead to deeper, more specific questions (e.g., 1 → 1.1 → 1.1.1)
- **"No" answers** skip sub-questions and move to the next main topic
- Questions are dynamically selected from the relevant blocks

### 3. Score Calculation
- **Starting Score**: 4.0 (representing optimal readiness)
- **Score Changes**: Each answer modifies your score based on the question's weight
- **Real-time Updates**: See your score change with each answer
- **Final LPERL Level**: Determined by your final score (0-4 scale)

## LPERL Levels Explained

- **LPERL 0** (Score ≤ 0): Ethical, Legal, and Privacy considerations lacking
- **LPERL 1** (Score 0-1): Identified Ethical and Privacy Issues
- **LPERL 2** (Score 1-2): Characterized Ethical and Privacy Interactions  
- **LPERL 3** (Score 2-3): Compatibility of Solutions and Ethics by Design
- **LPERL 4** (Score > 3): Control Over Ethical, Legal, and Privacy Issues

## Technical Details

### Question Database
The tool includes 129 actual LPERL framework questions:
- Sourced from validated academic research
- Professionally weighted scoring system
- Covers comprehensive ethical, legal, and privacy domains
- Hierarchically organized for adaptive assessment

### Local-First Design
- **SQLite Database**: Automatically initialized on first run
- **No Network Calls**: Completely offline operation
- **Data Privacy**: All data stays on your local machine
- **Portable**: Single directory contains everything needed

### Assessment Logic
The tool implements the original LPERL navigation logic:
- Hierarchical question numbering (1, 1.1, 1.2, 1.2.1, etc.)
- Conditional question flow based on previous answers
- Block-based organization for different technology domains
- Weighted scoring system reflecting question importance

## Development

### Adding Custom Questions
Edit `schema.sql` to add questions following this format:
```sql
INSERT INTO questions (id, number, question, yes_score, no_score, block) VALUES
(9999, '25', 'Your question text?', 0.1, -0.2, 'zero_case');
```

### Debug Information
Visit `/debug` while the app is running to see:
- Question counts by block
- Database structure
- Sample questions

### Customizing Scoring
Modify the `get_message_by_score()` function in `app.py` to adjust:
- LPERL level thresholds
- Assessment messages
- Score interpretations

## Changes from Original

This version fixes all issues from the original `tool.py`:

1. **✅ Separated Content**: Clean Python code, HTML templates properly organized
2. **✅ Real Questions**: Uses actual 129 LPERL framework questions instead of samples
3. **✅ Local-Only**: Removed all online/MySQL dependencies for complete locality
4. **✅ Proper Structure**: Flask best practices, organized file structure
5. **✅ No Configuration**: Works out-of-the-box with SQLite
6. **✅ Enhanced Scoring**: Professional visualization with LPERL level indicators
7. **✅ Complete Documentation**: Comprehensive usage and technical documentation

## License

Copyright (c) 2023 laurynasadomaitis

## Academic Reference

This tool implements the LPERL (Legal, Privacy, Ethical Readiness Level) framework. For academic use, please cite the original LPERL research and methodology.