# ERL Assessment Tool - Local Version

ERL (Ethics Readiness Levels) / LPERL Assessment Tool is a completely local Flask web application that evaluates the ethical, legal, and privacy readiness of technology projects using validated framework questions.

## Features

- **Comprehensive Assessment**: Uses validated framework questions across core and domain-specific blocks
- **Multi-block Evaluation**: Dynamically includes relevant assessment blocks based on your project:
  - **Zero Case** (Basic Ethics) - included for all projects (35 questions)
  - **GDPR Block** - for projects using personal data (41 questions) 
  - **AI Act Block** - for projects using artificial intelligence (30 questions)
  - **LED Block** - for Law Enforcement Agency products (23 questions)
  - **Healthcare AI Block (AIOLIA route)** - optional healthcare-focused AI assessment
  - **Public Administration AIA Block** - standalone algorithmic impact assessment route

- **Intelligent Navigation**: Hierarchical question flow that adapts based on your answers
- **Real-time Scoring**: Dynamic score calculation with detailed progression tracking
- **Visual Results**: Generates professional score progression graphs with LPERL level indicators
- **Expert Review Export**: Generates an editable `.docx` review sheet for Public Administration AIA indicators
- **Completely Local**: No data leaves your computer - fully offline operation
- **No Dependencies**: Uses only SQLite - no external database setup required

## Quick Start

**🛠️ Using the shell script (recommended):**
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
Then open your browser and go to: **http://127.0.0.1:8080**

## Project Structure

```
erl_tool/
├── app.py                 # Main Flask application
├── start.sh               # Shell launcher
├── templates/
│   ├── index.html         # Main assessment interface
│   └── aiolia_pairings.html  # AIOLIA pairings editor
├── static/               # Generated score graphs
├── export_aia_review.py   # Export Public Administration AIA questions to DOCX
├── schema.sql           # Database schema with actual LPERL questions
├── questions.sql        # Original MySQL dump (reference)
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── lperl_local.sqlite  # Auto-generated database (after first run)
```

## LPERL Assessment Process

### 1. Initial Classification
Answer onboarding questions to identify which assessment blocks apply to your project:
- **LEA Product**: Is your product created for Law Enforcement Agencies?
- **Personal Data**: Does your product use personal data?
- **AI Technology**: Does your product use artificial intelligence?
- **Healthcare AI Route**: Should healthcare-specific AI indicators be used (AIOLIA)?
- **Public Administration AIA Route**: Should the standalone public-sector AIA block be used?

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

### Healthcare and AIA Extensions
- **Healthcare AI (AIOLIA)**: Adds a domain-specific route for clinical and care-related AI systems.
- **Public Administration AIA**: Adds a dedicated block for algorithmic impact assessment in public-sector contexts.
- **AIOLIA Pairings Editor**: `/aiolia-pairings` provides an interface for managing AIOLIA mappings.
- **AIA Expert Review Export**: Run `python3 export_aia_review.py` to generate `AIA_Expert_Review.docx` for external review.

### Question Database
The tool includes validated framework questions across multiple blocks:
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

This version fixes the issues from the earlier archived implementation:

1. **✅ Separated Content**: Clean Python code, HTML templates properly organized
2. **✅ Real Questions**: Uses actual 129 LPERL framework questions instead of samples
3. **✅ Local-Only**: Removed all online/MySQL dependencies for complete locality
4. **✅ Proper Structure**: Flask best practices, organized file structure
5. **✅ No Configuration**: Works out-of-the-box with SQLite
6. **✅ Enhanced Scoring**: Professional visualization with LPERL level indicators
7. **✅ Complete Documentation**: Comprehensive usage and technical documentation

## System Card: ERL Assessment Tool (v0.2)

### **Intended Purpose**
The ERL (Ethics Readiness Levels) Assessment Tool serves as a practical implementation of the LPERL framework. Its primary purpose is to:
- **Democratize Ethics Auditing**: Enable developers and non-experts to conduct sophisticated ethical and legal risk assessments without requiring deep regulatory expertise.
- **Facilitate Ethics-by-Design**: Provide a structured, iterative workflow that guides project teams from initial risk identification to the implementation of concrete technical and procedural safeguards.
- **Bridge the Gap Between Theory and Practice**: Translate high-level ethical principles (like those in the AI Act and GDPR) into specific, actionable indicators and technical measures.
- **Standardize Readiness Reporting**: Offer a quantifiable LPERL level (0-4) that can be used to communicate a project's ethical maturity to stakeholders, auditors, and regulatory bodies.

### **AI Agent Hosting Instructions**
This tool is designed to be easily hosted and managed by AI coding agents within controlled environments (like sandboxes or local dev environments).

#### **Agent Setup Protocol:**
1.  **Environment Check**: Verify Python 3.7+ is installed.
2.  **Dependency Management**: Use the provided `requirements.txt` to install necessary libraries.
3.  **Database Initialization**: The tool automatically initializes `lperl_local.sqlite` on first run if it doesn't exist.
4.  **Port Management**: By default, the tool runs on port `8080` (to avoid common macOS AirPlay conflicts on `5000`). Agents should ensure this port is available or use `lsof -i :8080` to find and terminate conflicting processes.
5.  **Execution Command**:
    ```bash
    python3 app.py > app_output.log 2>&1 &
    ```
6.  **Verification**: Poll `http://127.0.0.1:8080` until it returns a `200 OK` status before notifying the user.

#### **Agent Capabilities for Maintenance:**
- **Dynamic Updates**: Agents can modify `schema.sql` or `app.py` to add new assessment blocks or logic and restart the server to apply changes.
- **Local LLM Bridging**: Agents should facilitate the connection to a local LLM (e.g., via LM Studio on `localhost:1234`) to enable v0.2 AI-assisted features.

### **Technical Specifications**
- **Architecture**: Local Flask web application (Local-First).
- **Database**: SQLite3.
- **Visualization**: Plotly (v0.2).
- **AI Backend**: Compatible with OpenAI-style local API endpoints.

### **Capabilities**
- **Adaptive Flow**: Hierarchical question navigation (1 -> 1.1 -> 1.1.1).
- **Domain Specialization**: Blocks for AI Act, GDPR, Law Enforcement (LED), and Healthcare.
- **Actionable AI Recommendations**: (v0.2) Generates practical solutions for unrecovered ethical concerns.

### **Limitations & Ethical Considerations**
- **Data Sovereignty**: Completely offline. No data ever leaves the local machine.
- **User Responsibility**: The tool is a decision-support system, not an automated compliance officer. Results rely on truthful user input.
- **Transparency**: All scoring weights and indicators are visible in `schema.sql`.

## License

Copyright (c) 2023 laurynasadomaitis

## Academic Reference

This tool implements the LPERL (Legal, Privacy, Ethical Readiness Level) framework. For academic use, please cite the original LPERL research and methodology.