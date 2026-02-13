#!/usr/bin/env python3
"""
Ethics Readiness Levels Tool - Version 0.2-dev
A four-level, iterative method to track how ethical reflection is implemented 
in the design of AI systems.

** DEVELOPMENT VERSION - NOT FOR PRODUCTION USE **

Based on the research paper: "Ethics Readiness of Artificial Intelligence: 
A Practical Evaluation Method" (under review)

Authors: Laurynas Adomaitis (RISE), Vincent Israel-Jost (CEA-Saclay/Larsim), 
         Alexei Grinbaum (CEA-Saclay/Larsim)

Implementation & Hosting: RISE (Research Institutes of Sweden)
Funding: AIOLIA project (EU Grant 101187937) & MultiRATE EU Horizon project (Grant 101073929)

Created: 20/06/2023
Updated: 20/10/2025 - Version 0.1 Release
"""

import os
import time
import sqlite3
import json
import requests
from flask import Flask, jsonify, request, session, render_template, send_file

# Try to import visualization libraries
try:
    import plotly.graph_objects as go
    import plotly.utils
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False
    print("⚠️  Warning: Plotly not available. Real-time graphs will be disabled.")
    print("   To enable real-time graphs, install plotly: pip install plotly")

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'lperl-local-secret-key-change-in-production')
DATABASE = 'lperl_local.sqlite'
AIOLIA_OVERRIDES_FILE = 'aiolia_pairings_overrides.json'
AIOLIA_LOGO_PATH = '/Users/laurynasadomaitis/.cursor/projects/Users-laurynasadomaitis-Downloads-erl-tool/assets/image-f0b7f3b3-5cdc-458a-9246-82244fc1d956.png'

# AIOLIA technical measures mapped dynamically to the active indicator set.
AIOLIA_TECHNICAL_MEASURES = [
    "Using diverse and representative datasets to prevent bias during AI model design and training.",
    "Conducting continuous bias testing and monitoring throughout the AI system's lifecycle.",
    "Performing computational subgroup performance analysis to detect and mitigate bias across different demographic or user groups.",
    "Implementing technical subgroup validation procedures, specifically applied in healthcare contexts, to ensure model fairness across patient populations.",
    "Utilizing automated fairness drift detection to continuously monitor for emergent biases as the system operates in the real world.",
    "Applying sensitivity analysis algorithms in models, such as automotive safety systems, to mathematically ensure fairness and robustness.",
    "Executing automated monitoring of algorithmic moderation outcomes across different user groups to detect and prevent discriminatory effects.",
    "Running automated, continuous fairness reviews of AI-generated risk scores in workplace and HR systems.",
    "Integrating cultural and linguistic technical checks into security narrative models to computationally detect bias.",
    "Designing user interfaces with direct, built-in consent mechanisms to protect user autonomy.",
    "Enforcing digital access controls that restrict system access exclusively to individuals technically verified as understanding the AI's purpose and limitations.",
    "Structuring the system architecture to technically minimize the total number of users with access to sensitive AI components.",
    "Maintaining automated audit logs to ensure total technical traceability of AI outputs and decisions.",
    "Automatically logging all human validation actions to maintain a transparent, verifiable record of human-in-the-loop oversight.",
    "Generating and digitally storing case-level evidence chains and appeal records for AI decisions in healthcare settings.",
    "Implementing standards-driven technical traceability that aligns directly with hardware safety artifacts in systems like automotive AI.",
    "Applying strict technical version control mechanisms for both the AI models and their underlying datasets.",
    "Utilizing role-based digital permissions to securely manage access and intervention capabilities within the system.",
    "Building technical manual override and change mechanisms into the UI that allow human operators to alter or pause AI decisions.",
    "Deploying restricted or undisclosed computational tooling in security contexts to technically enforce confidentiality.",
    "Enforcing automated data quality, integrity, and validation protocols within the machine learning training pipeline.",
    "Executing formal technical model auditing against established baseline computational metrics.",
    "Conducting boundary testing to computationally map the absolute technical limits of the AI system's reliable performance.",
    "Running continuous performance validation scripts to ensure the system consistently performs its intended tasks safely in real-time.",
    "Designing and deploying resilient hardware and software architectures technically capable of withstanding errors, data corruption, or attacks.",
    "Programming the UI to generate user-facing explanations that clarify the AI's functioning and limitations directly on the screen.",
    "Creating automated, patient-facing plain-language summaries for AI-generated outputs in clinical settings.",
    "Integrating automated explanation notices directly into the workflow of algorithmic moderation systems.",
    "Providing simplified, dynamically generated technical explanations of AI tools tailored specifically for employees using workplace systems.",
    "Displaying visual safety boundaries directly within the user interface for real-time applications like automotive AI.",
    "Rendering mathematical confidence and uncertainty indicators on the screen alongside AI-generated outputs.",
    "Implementing automated backend generation of documentation regarding model behavior to support technical explainability.",
    "Executing strict, automated backend logging of all system decisions and user inputs for forensic traceability.",
    "Applying clear, hardcoded UI labeling to explicitly distinguish AI-generated outputs from human-generated content.",
    "Forcing users via the digital interface to input documented text justification before the system allows them to accept specific AI recommendations.",
    "Triggering automated explanation prompts in the UI to force human reflection before confirming an AI-generated decision.",
    "Displaying technical comparison views on-screen that explicitly contrast the AI's assessment with a human's assessment.",
    "Enforcing bounded automation via hardcoded technical limits that restrict exactly what the AI can execute without a human override.",
    "Conducting computational robustness and resilience testing against adverse conditions, corrupted data, or malicious attacks.",
    "Performing comprehensive, technical hazard and failure-mode analysis on the system's underlying architecture.",
    "Deploying algorithmic anomaly detection to automatically flag abnormal data patterns or potential system misuse.",
    "Utilizing automated real-time content filtering algorithms to instantly block harmful or unsafe outputs.",
    "Implementing automated behavior pattern detection models in virtual assistants to identify risks, abuse, or psychological distress.",
    "Running continuous technical performance monitoring pipelines to mathematically ensure the system operates within defined safe parameters.",
    "Automating the ongoing monitoring of algorithmic risk scores and generating instant digital alerts when thresholds are exceeded.",
    "Building explicit technical safeguards directly into the code designed to detect and block attempted system misuse or manipulation.",
    "Integrating automated control mechanisms that instantly pause, downgrade, rollback, or constrain system outputs when predefined risk thresholds are met.",
    "Hardcoding Human-in-the-loop workflows directly into the software's operational pipeline so processes cannot advance without human input.",
    "Designing specialized, secure clinician sign-off interfaces for authorizing AI-driven healthcare decisions.",
    "Utilizing automated confidence flags that are technically wired to halt system execution and trigger mandatory human review.",
    "Implementing technical safe-fail protocols that automatically shut down or default the system to a safe state during critical errors.",
    "Deploying tiered severity appreciation systems powered by Large Language Model judges and specialized classification models.",
    "Utilizing real-time algorithmic pattern detection to intercept harmful content in the milliseconds before it is disseminated to users.",
    "Implementing explicit algorithmic jailbreak detection mechanisms to prevent users from bypassing the AI's safety filters.",
    "Utilizing specially labeled and curated training datasets mathematically designed to teach the AI model its explicit safety boundaries.",
    "Applying robust data encryption protocols to technically protect sensitive information and user privacy across the system.",
    "Executing automated data anonymization and pseudonymization processes on datasets wherever technically feasible.",
    "Implementing highly secure, restricted-access logging environments to protect the absolute integrity of system audit trails.",
    "Designing backend infrastructure with restricted, isolated data access environments for processing highly sensitive personal information.",
    "Hardcoding data minimization rules directly into the system's data collection APIs and storage architecture.",
    "Building large-scale technical consent and data lifecycle management architectures, particularly for virtual assistants and HR platforms.",
    "Utilizing algorithmic threshold-based classification models to drive automated content moderation decisions.",
    "Configuring highly conservative, mathematically strict flagging thresholds in workplace tools to prevent algorithmic over-censorship.",
    "Deploying context-aware natural language processing moderation models to protect freedom of expression in virtual assistants.",
    "Implementing automated tiered response algorithms that apply proportional UI restrictions based on the calculated severity of the content.",
    "Designing technical alternative-narrative generation models specifically for use in security and defense contexts.",
    "Automating the programmatic generation and delivery of explanatory messages sent to users exactly when their content is restricted.",
    "Recording technical logs of all automated moderation actions taken by the system.",
    "Deploying specialized, secondary automated classifiers that are explicitly trained solely for harmful advice prevention.",
    "Integrating separate, external software solutions via API that are specifically trained for rapid psychological or physical crisis detection.",
    "Implementing multi-layered technical scope controls to strictly constrain the AI from generating advice beyond its designated boundaries.",
    "Triggering automated UI explanations precisely at the moment user content is actively restricted, flagged, or taken down.",
    "Integrating large-scale system logging and moderation records directly into the backend of underlying platform and payment architectures.",
    "Constructing multi-layer, redundant, and self-monitoring hardware and software architectures to technically guarantee high system reliability.",
    "Executing extreme technical resilience testing focused specifically on catastrophic hardware/software failures like sensor loss and cyberattacks.",
    "Running automated validation cycles that computationally test the model's weights and outputs against standardized benchmark datasets.",
    "Building specialized moderator escalation tools and buttons directly into the user interface for handling algorithmic borderline cases.",
    "Implementing digital age verification API mechanisms to protect minors and ensure human safety at the point of access.",
    "Automating the backend execution of account warnings or bans based strictly on a pre-defined computational tier of safety violations.",
    "Building dynamic technical consent portals that allow users to actively toggle and adjust their data tracking preferences over time.",
    "Deploying continuous output monitoring data pipelines to actively scan for and algorithmically block harmful psychological or physical advice.",
    "Utilizing immutable, append-only logs that are cryptographically secured so they technically cannot be altered or deleted once written.",
    "Automatically generating computational reasoning traces that allow independent auditors to reconstruct the exact logic path the AI took.",
    "Embedding cryptographic artefacts like secure hashes and keys throughout the infrastructure to mathematically protect data integrity.",
    "Conducting active, aggressive security penetration tests to computationally identify and patch technical vulnerabilities.",
    "Requiring and verifying secure digital cryptographic signatures from both human reviewers and responsible engineers on final system outputs.",
    "Creating specialized, interactive UI dashboards engineered explicitly to make the human review of algorithmic data drift highly efficient.",
    "Automating the backend tracking, calculation, and reporting of specific system performance metrics like Mean Time To Repair.",
    "Continuously tracking and computationally calculating the automated alert precision and recall rates of the AI system.",
    "Executing computational disagreement analysis to mathematically identify where different models, humans, or data subsets diverge in their outputs."
]

AIOLIA_MEASURE_MAP = {}


def indicator_sort_key(indicator_number):
    """Natural sort key for hierarchical indicator numbers like 10.1.2."""
    return tuple(int(part) if part.isdigit() else 0 for part in str(indicator_number).split('.'))


def load_aiolia_overrides():
    """Load persistent indicator -> AIOLIA id overrides from disk."""
    if not os.path.exists(AIOLIA_OVERRIDES_FILE):
        return {}
    try:
        with open(AIOLIA_OVERRIDES_FILE, 'r', encoding='utf-8') as f:
            raw = json.load(f)
        if not isinstance(raw, dict):
            return {}
        cleaned = {}
        for indicator, measure_id in raw.items():
            try:
                mid = int(measure_id)
            except (TypeError, ValueError):
                continue
            # 0 is a special value meaning "explicitly unpaired".
            if mid == 0:
                cleaned[str(indicator)] = 0
            elif 1 <= mid <= len(AIOLIA_TECHNICAL_MEASURES):
                cleaned[str(indicator)] = mid
        return cleaned
    except Exception as e:
        print(f"Warning: failed to load AIOLIA overrides: {e}")
        return {}


def save_aiolia_overrides(overrides):
    """Persist indicator -> AIOLIA id overrides to disk."""
    with open(AIOLIA_OVERRIDES_FILE, 'w', encoding='utf-8') as f:
        json.dump(overrides, f, indent=2, sort_keys=True)


def get_sorted_indicator_rows():
    """Return all active indicators sorted naturally."""
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT number, question, block FROM questions")
        rows = [
            {
                'number': str(row['number']),
                'question': row['question'],
                'block': row['block']
            }
            for row in cur.fetchall()
        ]
    finally:
        cur.close()
        conn.close()

    rows.sort(key=lambda item: indicator_sort_key(item['number']))
    return rows


def build_manual_aiolia_seed_map():
    """
    Manual, content-read seed pairing between active indicators and AIOLIA measures.
    This is intentionally curated (not NLP/similarity based).
    """
    return {
        # zero_case (removed all pairings scored < 5)
        '1.1': 19, '1.2': 35, '1.2.1': 36,
        '2': 40, '2.1': 25, '2.2': 46, '2.2.1': 85, '2.4': 46, '2.4.1.1': 47,
        '3': 1, '3.1': 3, '3.3': 3, '3.3.1': 5,
        '5': 8, '5.3': 37, '5.3.1': 29, '5.3.2': 29,
        '6': 13, '6.1': 82,
        '7': 48, '7.1': 14,

        # gdpr_block
        '8': 56, '8.1': 59, '8.1.2': 60, '8.3': 61, '8.3.1': 60, '8.3.2': 21, '8.3.3': 61,
        '10': 84, '10.1': 56, '10.1.1': 57, '10.1.2': 61,
        '11': 80, '11.1': 61,
        '12': 26, '12.1': 67, '12.1.1': 27, '12.1.2': 10, '12.1.3': 80,
        '13': 78, '13.1': 78, '13.1.1': 78, '13.1.2': 27, '13.1.3': 80,
        '14': 57, '14.1': 60, '14.1.1': 34,

        # led_block
        '15': 60, '15.1': 61, '15.1.1': 21, '15.1.2': 18, '15.2': 1, '15.2.1': 56,
        '16': 61, '16.1': 61, '16.1.1': 18, '16.1.2': 15,
        '17': 13, '17.2.1': 32, '17.3': 19, '17.3.1': 72,

        # ai_block
        '18': 22, '18.1': 32,
        '19': 76, '19.1': 44, '19.1.1': 40, '19.1.2': 17, '19.3': 32,
        '20': 26, '20.1': 34, '20.2': 30, '20.3': 67,
        '21': 38, '21.1': 41, '21.1.1': 51, '21.2': 48, '21.2.1': 19, '21.2.1.1': 87, '21.2.1.1.1': 29, '21.3': 31, '21.3.1': 76,
        '22': 39, '22.1': 56, '22.2': 54, '22.3': 84, '22.4': 45,
        '23': 29, '23.1': 29, '23.4': 27,
    }


def get_seed_aiolia_id(indicator_number, seed_map):
    """Resolve seed id only for explicitly paired indicators."""
    return seed_map.get(str(indicator_number))


def build_aiolia_measure_map():
    """Use curated seed pairing, then apply user overrides."""
    rows = get_sorted_indicator_rows()
    indicator_numbers = [row['number'] for row in rows]
    measure_map = {}
    seed_map = build_manual_aiolia_seed_map()

    for indicator_number in indicator_numbers:
        seed_id = get_seed_aiolia_id(indicator_number, seed_map)
        if not seed_id:
            continue
        measure_map[indicator_number] = {
            'id': seed_id,
            'text': AIOLIA_TECHNICAL_MEASURES[seed_id - 1]
        }

    # Apply user overrides on top of curated seed mapping.
    overrides = load_aiolia_overrides()
    for indicator_number, override_measure_id in overrides.items():
        if indicator_number in indicator_numbers and override_measure_id == 0:
            measure_map.pop(indicator_number, None)
        elif indicator_number in indicator_numbers:
            measure_map[indicator_number] = {
                'id': override_measure_id,
                'text': AIOLIA_TECHNICAL_MEASURES[override_measure_id - 1]
            }

    return measure_map


def get_aiolia_measure(indicator_number):
    """Get AIOLIA technical measure for an indicator from active indicator set."""
    global AIOLIA_MEASURE_MAP
    if not AIOLIA_MEASURE_MAP:
        AIOLIA_MEASURE_MAP = build_aiolia_measure_map()
    return AIOLIA_MEASURE_MAP.get(str(indicator_number))


def refresh_aiolia_measure_map():
    """Rebuild in-memory AIOLIA mapping cache after edits."""
    global AIOLIA_MEASURE_MAP
    AIOLIA_MEASURE_MAP = build_aiolia_measure_map()


def get_db():
    """Get database connection with row factory."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_db():
    """Initialize the SQLite database if it doesn't exist."""
    if not os.path.exists(DATABASE):
        print("Initializing database with LPERL questions...")
        conn = sqlite3.connect(DATABASE)
        with open('schema.sql', 'r') as f:
            conn.executescript(f.read())
        conn.close()
        print("Database initialized successfully!")


def determine_blocks(answers):
    """Determine which question blocks to include based on initial answers."""
    session['user_name'] = 'User'  # Default user name since field was removed
    session['product_name'] = request.form.get('product_name', '')
    blocks = ['zero_case']  # 'zero_case' is included for all users

    # Check each condition separately - following original logic
    if answers['product_for_LEAs'].lower() == 'yes':
        blocks.append('led_block')
    if answers['uses_personal_data'].lower() == 'yes':
        blocks.append('gdpr_block')
    if answers['uses_AI'].lower() == 'yes':
        blocks.append('ai_block')

    return blocks


def get_first_question_of_block(block_name):
    """Get the first question number for a given block."""
    conn = get_db()
    cur = conn.cursor()
    try:
        # Query for minimum whole number question of the block (no decimal points)
        cur.execute("SELECT MIN(CAST(number AS DECIMAL)) FROM questions WHERE block = ? AND number NOT LIKE '%.%'", (block_name,))
        result = cur.fetchone()
        return str(result[0]) if result and result[0] else None
    except Exception as e:
        print("Database error in get_first_question_of_block:", e)
        return None
    finally:
        cur.close()
        conn.close()


def question_exists(number):
    """Check if a question with the given number exists."""
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT COUNT(*) FROM questions WHERE number = ?", (str(number),))
        count = cur.fetchone()[0]
        return count > 0
    finally:
        cur.close()
        conn.close()


def increment_question_number(number):
    """Increment the question number by 1."""
    number = str(number)
    parts = number.split('.')
    parts[-1] = str(int(parts[-1]) + 1)
    return '.'.join(parts)


def get_next_question(number, answer):
    """
    Determine the next question based on current question and answer.
    This follows the original logic for hierarchical question navigation.
    """
    if answer.lower() == 'yes':
        # Try to go deeper (add .1)
        deeper_question_number = number + '.1'
        if question_exists(deeper_question_number):
            return deeper_question_number
        else:
            # If no deeper question, increment at current level
            next_number = increment_question_number(number)
            while '.' in next_number and not question_exists(next_number):
                # If incremented question doesn't exist, go up a level and try again
                parts = next_number.split('.')
                parts.pop()
                next_number = '.'.join(parts)
                next_number = increment_question_number(next_number)
            return next_number if question_exists(next_number) else None
    else:  # Answer is 'no'
        # Skip deeper questions and go to next at current level
        next_number = increment_question_number(number)
        while '.' in next_number and not question_exists(next_number):
            # If incremented question doesn't exist, go up a level and try again
            parts = next_number.split('.')
            parts.pop()
            next_number = '.'.join(parts)
            next_number = increment_question_number(next_number)
        return next_number if question_exists(next_number) else None


def get_message_by_score(score):
    """Get assessment message based on final score."""
    if score <= 0:
        return "LPERL 0 – Ethical, Legal, and Privacy considerations lacking. You should start by identifying ethical issues related to your project."
    elif 0 < score <= 1:
        return "LPERL 1 – Identified Ethical and Privacy Issues. You have identified key issues and should analyse them better to understand how they relate to your project."
    elif 1 < score <= 2:
        return "LPERL 2 – Characterized Ethical and Privacy Interactions. You have identified and characterized ethical issues relevant to your project. Now you should work on integrating them into a coherent ethical design."
    elif 2 < score <= 3:
        return "LPERL 3 – Compatibility of Solutions and Ethics by Design. The system's ethical and privacy considerations have been identified, characterized, and conceptualized in a coherent system. You should ensure the fluid implementation and accountability of the design choices."
    elif score > 3:
        return "LPERL 4 - Control Over Ethical, Legal, and Privacy Issues. Your project has sufficient working control mechanisms in place to manage its ethical and privacy considerations and ensure accountability and demonstrates ethical maturity."
    return ""


def analyze_top_concerns():
    """
    Analyze top 3 areas of concern based on NET LOSS that was never recovered.
    Tracks the parent indicator that caused loss and all its children.
    """
    answers = session.get('answers', {})
    score_progression = session.get('score_progression', [4])
    indicator_progression = session.get('indicator_progression', [])
    
    if not answers or len(score_progression) < 2:
        return []
    
    # Track all indicators and find those that caused initial loss
    all_indicators = []
    
    for idx, (question_num, answer_data) in enumerate(answers.items()):
        indicator = indicator_progression[idx] if idx < len(indicator_progression) else question_num
        score_before = score_progression[idx] if idx < len(score_progression) else 4
        score_after = score_progression[idx + 1] if idx + 1 < len(score_progression) else score_before
        score_change = score_after - score_before
        
        all_indicators.append({
            'indicator': str(indicator),
            'answer': answer_data['answer'],
            'question': answer_data.get('question', 'N/A'),
            'score_change': score_change,
            'score_before': score_before,
            'score_after': score_after,
            'index': idx
        })
    
    # Find parent indicators that caused loss
    parent_losses = {}
    
    for item in all_indicators:
        if item['score_change'] < -0.001:  # This caused a loss
            indicator = item['indicator']
            
            # This is a parent that caused loss
            if indicator not in parent_losses:
                parent_losses[indicator] = {
                    'parent': item,
                    'children': [],
                    'net_change': item['score_change'],
                    'initial_loss': item['score_change']
                }
    
    # Now find all children of these parents and calculate net change
    for parent_indicator, parent_data in parent_losses.items():
        parent_idx = parent_data['parent']['index']
        
        # Find all subsequent indicators that are children (start with parent prefix)
        for item in all_indicators:
            if item['index'] > parent_idx:
                # Check if this is a child (e.g., "5" is parent of "5.1", "5.2", "5.2.1")
                if item['indicator'].startswith(parent_indicator + '.'):
                    parent_data['children'].append(item)
                    parent_data['net_change'] += item['score_change']
    
    # Filter: ONLY indicators with net loss after recovery attempts.
    # Recovery is computed from positive child deltas only, capped by initial parent loss.
    # This prevents impossible values (e.g., recovery > 100% negative/positive mix artifacts).
    concerns = []
    for indicator, data in parent_losses.items():
        initial_loss = abs(data['initial_loss'])
        children = data['children']

        # Positive child deltas are true recovery contributions.
        positive_recovery = sum(item['score_change'] for item in children if item['score_change'] > 0)
        recovery_amount = min(initial_loss, max(0.0, positive_recovery))
        unrecovered_parent_loss = max(0.0, initial_loss - recovery_amount)

        # Extra child penalties are additional unresolved loss beyond the parent event.
        additional_child_loss = sum(abs(item['score_change']) for item in children if item['score_change'] < 0)
        net_loss = unrecovered_parent_loss + additional_child_loss

        if net_loss > 0.001:  # Still has unresolved loss
            recovery_percent = (recovery_amount / initial_loss * 100) if initial_loss > 0 else 0
            
            # Build full answer list: parent + children
            all_answers = [data['parent']] + children
            
            concerns.append({
                'indicator': indicator,
                'net_loss': net_loss,
                'initial_loss': initial_loss,
                'recovery_amount': recovery_amount,
                'recovery_percent': recovery_percent,
                'unrecovered_parent_loss': unrecovered_parent_loss,
                'additional_child_loss': additional_child_loss,
                'parent_question': data['parent']['question'],
                'parent_answer': data['parent']['answer'],
                'all_answers': all_answers
            })
    
    # Sort by net loss (worst first)
    concerns.sort(key=lambda x: x['net_loss'], reverse=True)
    
    return concerns[:3]  # Top 3 only


def end_session_and_present_results():
    """End the current session and generate results with score progression graph."""
    score = session.get('score', 4)  # Default starting score is 4
    message = get_message_by_score(score)

    # Generate a timestamp to create a unique filename
    product_name = session.get('product_name', 'Product')
    timestamp = f"assessment_{int(time.time())}"
    
    # Generate Plotly visualization for final results
    graph_json = None
    if HAS_PLOTLY:
        scores = session.get('score_progression', [4])
        indicators = session.get('indicator_progression', [])
        
        # Create x-axis labels: use indicator numbers if available, otherwise question numbers
        if indicators:
            x_labels = indicators
        else:
            x_labels = list(range(1, len(scores) + 1))
        
        # Create Plotly figure
        fig = go.Figure()
        
        # Add score progression line
        fig.add_trace(go.Scatter(
            x=x_labels,
            y=scores,
            mode='lines+markers',
            name='LPERL Score',
            line=dict(color='#2E86AB', width=3),
            marker=dict(size=8)
        ))
        
        # Add LPERL level reference lines
        fig.add_hline(y=1, line_dash="dash", line_color="red", opacity=0.5, 
                     annotation_text="LPERL 1", annotation_position="right")
        fig.add_hline(y=2, line_dash="dash", line_color="orange", opacity=0.5,
                     annotation_text="LPERL 2", annotation_position="right")
        fig.add_hline(y=3, line_dash="dash", line_color="gold", opacity=0.5,
                     annotation_text="LPERL 3", annotation_position="right")
        fig.add_hline(y=4, line_dash="dash", line_color="green", opacity=0.5,
                     annotation_text="LPERL 4", annotation_position="right")
        
        # Update layout with product name
        fig.update_layout(
            title=f'{product_name} - Final Ethics Readiness Assessment Results',
            xaxis_title='Indicator',
            yaxis_title='LPERL Score',
            yaxis=dict(range=[0, 4.5]),
            showlegend=False,
            height=400,
            margin=dict(l=50, r=50, t=50, b=50)
        )
        
        # Convert to JSON for embedding
        graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # Store final results in database
    conn = get_db()
    cur = conn.cursor()
    try:
        if 'session_id' in session:
            cur.execute("UPDATE sessions SET end_time = DATETIME('now'), final_score = ? WHERE id = ?", 
                       (score, session['session_id']))
            conn.commit()
    except Exception as e:
        print(f"Error saving session results: {e}")
    finally:
        cur.close()
        conn.close()

    # Analyze top 3 areas of concern
    top_concerns = analyze_top_concerns()

    result = {
        'score': round(score, 2),
        'message': message,
        'graph_json': graph_json,
        'final_level': f"LPERL {int(score) if score <= 4 else 4}",
        'has_graph': HAS_PLOTLY,
        'top_concerns': top_concerns
    }
    
    # Preserve ALL data needed for AI recommendations
    # (analyze_top_concerns needs answers, score_progression, indicator_progression)
    app_desc = session.get('application_description', '')
    prod_name = session.get('product_name', '')
    answers = session.get('answers', {})
    score_progression = session.get('score_progression', [])
    indicator_progression = session.get('indicator_progression', [])
    
    session.clear()
    
    # Restore the preserved data for AI recommendations
    session['application_description'] = app_desc
    session['product_name'] = prod_name
    session['answers'] = answers
    session['score_progression'] = score_progression
    session['indicator_progression'] = indicator_progression
    session['assessment_complete'] = True
    
    return result


def start_new_session():
    """Initialize a new assessment session."""
    conn = get_db()
    cur = conn.cursor()
    try:
        user_id = 0  # Default user_id for local sessions
        cur.execute("INSERT INTO sessions (user_id, start_time) VALUES (?, DATETIME('now'))", (user_id,))
        conn.commit()
        session_id = cur.lastrowid
        session['session_id'] = session_id
        session['score'] = 4  # Starting score is 4
        session['answers'] = {}
        session['score_progression'] = [4]
        session['indicator_progression'] = []  # Track indicator numbers for chart x-axis
    except Exception as e:
        print(f"Error starting session: {e}")
    finally:
        cur.close()
        conn.close()


@app.route('/')
def index():
    """Render the main assessment page."""
    start_new_session()
    return render_template('index.html')


@app.route('/aiolia-pairings')
def aiolia_pairings_page():
    """Render standalone AIOLIA pairings editor page."""
    return render_template('aiolia_pairings.html')


@app.route('/aiolia-logo')
def aiolia_logo():
    """Serve AIOLIA logo used in UI cards."""
    if not os.path.exists(AIOLIA_LOGO_PATH):
        return jsonify({'error': 'AIOLIA logo not found'}), 404
    return send_file(AIOLIA_LOGO_PATH, mimetype='image/png')


@app.route('/determine_blocks', methods=['POST'])
def determine_blocks_endpoint():
    """Determine which question blocks to include based on user's initial answers."""
    answers = {
        'product_for_LEAs': request.form.get('product_for_LEAs', 'no'),
        'uses_personal_data': request.form.get('uses_personal_data', 'no'),
        'uses_AI': request.form.get('uses_AI', 'no')
    }
    
    # Store product name and application description
    session['product_name'] = request.form.get('product_name', 'Product')
    session['application_description'] = request.form.get('application_description', '')
    session['lifelines_remaining'] = 10  # Initialize lifelines
    
    session['determining_answers'] = answers
    session['blocks'] = determine_blocks(answers)
    session['current_block_index'] = 0
    session['current_question'] = get_first_question_of_block(session['blocks'][0])

    print(f"Determined blocks: {session['blocks']}")
    print(f"First question: {session['current_question']}")
    print(f"Application: {session['application_description'][:50]}...")

    return jsonify({'message': 'Blocks determined, fetching first question'})


@app.route('/question', methods=['GET'])
def get_question():
    """Get the current question to display to the user."""
    if 'blocks' in session and 'current_block_index' in session:
        while session['current_block_index'] < len(session['blocks']):
            current_block = session['blocks'][session['current_block_index']]
            current_question_number = session.get('current_question', None)

            if not current_question_number:
                # Get first question of the current block
                current_question_number = get_first_question_of_block(current_block)
                if current_question_number:
                    session['current_question'] = current_question_number

            if current_question_number:
                conn = get_db()
                cur = conn.cursor()
                try:
                    cur.execute("SELECT * FROM questions WHERE block = ? AND number = ?", 
                               (current_block, current_question_number))
                    question = cur.fetchone()
                finally:
                    cur.close()
                    conn.close()

                if question:
                    return jsonify({
                        'question': {
                            'id': question['id'],
                            'number': question['number'],
                            'question': question['question'],
                            'yes_score': question['yes_score'],
                            'no_score': question['no_score'],
                            'block': question['block'],
                            'aiolia_measure': get_aiolia_measure(question['number'])
                        },
                        'score': session.get('score', 4),
                        'block': current_block,
                        'lifelines_remaining': session.get('lifelines_remaining', 5)
                    })

            # Move to next block
            session['current_block_index'] += 1
            session.pop('current_question', None)

    # No more questions
    return jsonify(end_session_and_present_results())


@app.route('/aiolia_pairings', methods=['GET'])
def get_aiolia_pairings():
    """Return all active indicator -> AIOLIA pairings for review/editing."""
    rows = get_sorted_indicator_rows()
    current_map = build_aiolia_measure_map()
    overrides = load_aiolia_overrides()
    seed_map = build_manual_aiolia_seed_map()
    pairings = []

    for row in rows:
        default_id = get_seed_aiolia_id(row['number'], seed_map)
        current_measure = current_map.get(row['number'])
        pairings.append({
            'indicator': row['number'],
            'question': row['question'],
            'block': row['block'],
            'default_aiolia_id': default_id,
            'default_aiolia_text': AIOLIA_TECHNICAL_MEASURES[default_id - 1] if default_id else None,
            'aiolia_id': current_measure['id'] if current_measure else None,
            'aiolia_text': current_measure['text'] if current_measure else None,
            'is_overridden': row['number'] in overrides
        })

    measures = [{'id': i + 1, 'text': text} for i, text in enumerate(AIOLIA_TECHNICAL_MEASURES)]
    return jsonify({
        'total_indicators': len(rows),
        'total_measures': len(AIOLIA_TECHNICAL_MEASURES),
        'overrides_count': len(overrides),
        'measures': measures,
        'pairings': pairings
    })


@app.route('/aiolia_pairings_overrides', methods=['POST'])
def save_aiolia_pairing_overrides():
    """Save manual indicator -> AIOLIA id overrides."""
    payload = request.get_json(silent=True) or {}
    raw_overrides = payload.get('overrides', {})
    if not isinstance(raw_overrides, dict):
        return jsonify({'error': 'Invalid payload format. Expected overrides object.'}), 400

    valid_indicators = {row['number'] for row in get_sorted_indicator_rows()}
    cleaned_overrides = {}

    for indicator, measure_id in raw_overrides.items():
        indicator = str(indicator)
        if indicator not in valid_indicators:
            continue
        try:
            mid = int(measure_id)
        except (TypeError, ValueError):
            continue
        if mid == 0:
            cleaned_overrides[indicator] = 0
        elif 1 <= mid <= len(AIOLIA_TECHNICAL_MEASURES):
            cleaned_overrides[indicator] = mid

    save_aiolia_overrides(cleaned_overrides)
    refresh_aiolia_measure_map()

    return jsonify({
        'success': True,
        'overrides_count': len(cleaned_overrides),
        'message': 'AIOLIA pairings saved successfully.'
    })


@app.route('/answer', methods=['POST'])
def post_answer():
    """Process user's answer and calculate score."""
    answer = request.form['answer']

    if 'current_question' not in session:
        return jsonify(end_session_and_present_results())

    current_question_number = session['current_question']

    # Get question scores
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT yes_score, no_score, question FROM questions WHERE number = ?", 
                   (str(current_question_number),))
        row = cur.fetchone()
    finally:
        cur.close()
        conn.close()

    if not row:
        return jsonify({'error': 'Question not found'}), 404

    # Calculate score change
    score_change = row['yes_score'] if answer.lower() == 'yes' else row['no_score']
    session['score'] = max(0, round(session.get('score', 4) + score_change, 3))
    
    # Store answer with question text
    session.setdefault('answers', {})[current_question_number] = {
        'answer': answer,
        'question': row['question']
    }
    session['score_progression'].append(session['score'])
    
    # Track indicator numbers for chart x-axis
    session.setdefault('indicator_progression', []).append(str(current_question_number))

    print(f"Question {current_question_number}: {answer} -> score change: {score_change} -> new score: {session['score']}")

    # Calculate next question
    next_question_number = get_next_question(current_question_number, answer)
    if not next_question_number:
        # End of current block, move to next
        session['current_block_index'] += 1
        if session['current_block_index'] < len(session['blocks']):
            next_question_number = get_first_question_of_block(session['blocks'][session['current_block_index']])

    session['current_question'] = next_question_number
    return jsonify({
        'message': 'Answer received',
        'score': session.get('score', 4),
        'score_progression': session.get('score_progression', [4]),
        'indicator_progression': session.get('indicator_progression', [])
    })


@app.route('/chart_data', methods=['GET'])
def chart_data():
    """Return current score progression as JSON for real-time charting."""
    if not HAS_PLOTLY:
        return jsonify({'error': 'Plotly not available'})
    
    scores = session.get('score_progression', [4])
    indicators = session.get('indicator_progression', [])
    current_score = session.get('score', 4)
    product_name = session.get('product_name', 'Product')
    
    # Create x-axis labels: use indicator numbers if available, otherwise question numbers
    if indicators:
        x_labels = indicators
    else:
        x_labels = list(range(1, len(scores) + 1))
    
    # Create Plotly figure
    fig = go.Figure()
    
    # Add score progression line
    fig.add_trace(go.Scatter(
        x=x_labels,
        y=scores,
        mode='lines+markers',
        name='LPERL Score',
        line=dict(color='#2E86AB', width=3),
        marker=dict(size=6, color='#2E86AB')
    ))
    
    # Add LPERL level reference lines
    fig.add_hline(y=1, line_dash="dash", line_color="red", opacity=0.5)
    fig.add_hline(y=2, line_dash="dash", line_color="orange", opacity=0.5)
    fig.add_hline(y=3, line_dash="dash", line_color="gold", opacity=0.5)
    fig.add_hline(y=4, line_dash="dash", line_color="green", opacity=0.5)
    
    # Update layout with product name
    fig.update_layout(
        title=f'{product_name} - Ethics Readiness',
        xaxis_title='Indicator',
        yaxis_title='LPERL Score',
        yaxis=dict(range=[0, 4.5]),
        showlegend=False,
        height=250,
        font=dict(size=10),
        margin=dict(l=50, r=50, t=50, b=50),
        plot_bgcolor='rgba(248,248,248,1)',
        paper_bgcolor='rgba(255,255,255,1)'
    )
    
    # Convert to JSON
    chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return jsonify({
        'chart': chart_json,
        'current_score': current_score,
        'total_questions': len(scores) - 1  # Subtract 1 for initial score
    })


@app.route('/get_llm_help', methods=['POST'])
def get_llm_help():
    """Get AI help for understanding a question (costs 1 lifeline)."""
    # Check lifelines
    lifelines = session.get('lifelines_remaining', 0)
    if lifelines <= 0:
        return jsonify({'error': 'No lifelines remaining'}), 403
    
    # Get request data
    question_text = request.json.get('question', '')
    question_number = request.json.get('question_number', '')
    app_description = session.get('application_description', '')
    
    if not question_text or not app_description:
        return jsonify({'error': 'Missing required data'}), 400
    
    # Get block and parent context for child indicators
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT block FROM questions WHERE number = ?", (str(question_number),))
        row = cur.fetchone()
        block_name = row['block'] if row else 'unknown'
        
        # If this is a child indicator (has dots), get parent context
        parent_context = ""
        if '.' in question_number:
            parts = question_number.split('.')
            parent_number = '.'.join(parts[:-1])
            cur.execute("SELECT question FROM questions WHERE number = ?", (parent_number,))
            parent_row = cur.fetchone()
            if parent_row:
                parent_context = f"\n\nParent Indicator {parent_number}: \"{parent_row['question']}\""
    finally:
        cur.close()
        conn.close()
    
    # Map block names to readable text
    block_descriptions = {
        'zero_case': 'General Ethics (applies to all products)',
        'gdpr_block': 'GDPR - General Data Protection Regulation',
        'led_block': 'LED - Law Enforcement Directive',
        'ai_block': 'AI Act - Artificial Intelligence Regulation'
    }
    block_desc = block_descriptions.get(block_name, block_name)
    
    # Build the prompt with context
    prompt = f"""Help the user interpret this question for their specific application.

Question: "{question_text}"
Indicator: {question_number}
Regulatory Block: {block_desc}{parent_context}

Application: "{app_description}"

Explain what this question means for THIS specific application. Be brief (2-3 sentences) and practical."""
    
    try:
        # Call local LLM
        response = requests.post(
            'http://127.0.0.1:1234/v1/chat/completions',
            json={
                'model': 'google/gemma-3-12b',
                'messages': [
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ],
                'temperature': 0.7,
                'max_tokens': 200
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            ai_response = data['choices'][0]['message']['content']
            
            # Decrement lifeline
            session['lifelines_remaining'] = lifelines - 1
            
            return jsonify({
                'success': True,
                'hint': ai_response,
                'lifelines_remaining': session['lifelines_remaining']
            })
        else:
            return jsonify({'error': f'LLM API error: {response.status_code}'}), 500
            
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to connect to LLM: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500


@app.route('/restart', methods=['GET'])
def restart():
    """Restart the assessment by clearing the session."""
    session.clear()
    return jsonify({'message': 'Session cleared'})


@app.route('/get_ai_recommendations', methods=['POST'])
def get_ai_recommendations():
    """Generate AI recommendations for each unrecovered indicator with full context."""
    # Get unrecovered indicators from session
    app_description = session.get('application_description', '')
    product_name = session.get('product_name', 'this application')
    
    if not app_description:
        return jsonify({
            'error': 'Session expired or application description not found.',
            'help': 'The session may have been lost due to a server restart. Please start a new assessment to use this feature.'
        }), 400
    
    # Analyze top concerns to get unrecovered indicators
    concerns = analyze_top_concerns()
    
    if not concerns:
        return jsonify({
            'success': True,
            'message': '✅ Excellent! No unrecovered indicators found. All issues were successfully addressed through sub-indicators.',
            'recommendations': []
        }), 200
    
    # Generate recommendations for EACH indicator separately
    all_recommendations = []
    
    for concern in concerns:
        indicator = concern['indicator']
        parent_question = concern['parent_question']
        parent_answer = concern['parent_answer']
        net_loss = concern['net_loss']
        recovery_percent = concern['recovery_percent']
        all_answers = concern['all_answers']
        
        # Build detailed context including all child indicators
        context_lines = [f"Parent Indicator {indicator}: {parent_answer.upper()} → {parent_question}"]
        
        for ans_data in all_answers[1:]:  # Skip parent (already shown)
            child_indicator = ans_data['indicator']
            child_answer = ans_data['answer']
            child_question = ans_data['question']
            child_score = ans_data['score_change']
            
            recovery_marker = "✓" if child_score > 0 else ("✗" if child_score < 0 else "—")
            context_lines.append(
                f"  └─ Sub-indicator {child_indicator}: {child_answer.upper()} {recovery_marker} ({child_score:+.2f} pts)\n"
                f"     {child_question}"
            )
        
        full_context = "\n".join(context_lines)
        
        # Create focused prompt for THIS indicator
        prompt = f"""Product: {product_name}
Context: {app_description}

PROBLEM:
{full_context}

Give 1-2 PRACTICAL, WORKING solutions. Focus on:
- What they can actually DO (design changes, processes, tools)
- Common-sense steps anyone can implement
- Real improvements, not formal procedures

Keep it brief and useful. Skip generic advice."""

        try:
            # Call local LLM for this specific indicator
            response = requests.post(
                'http://127.0.0.1:1234/v1/chat/completions',
                json={
                    'model': 'google/gemma-3-12b',
                    'messages': [
                        {
                            'role': 'system',
                            'content': 'You are a practical advisor. Give brief, actionable solutions. No fluff.'
                        },
                        {
                            'role': 'user',
                            'content': prompt
                        }
                    ],
                    'temperature': 0.5,
                    'max_tokens': 300
                },
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                raw_recommendation = data['choices'][0]['message']['content'].strip()
                
                # Clean up common LLM preamble patterns
                cleaned = raw_recommendation
                cleanup_patterns = [
                    r'^(Okay|Sure|Here|Alright)[,\s]+.*?[:.\n]',
                    r'^I\'ll.*?[:.\n]',
                    r'^Here are.*?[:.\n]',
                    r'^Based on.*?[:.\n]'
                ]
                import re
                for pattern in cleanup_patterns:
                    cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE | re.MULTILINE)
                cleaned = cleaned.strip()
                
                all_recommendations.append({
                    'indicator': indicator,
                    'question': parent_question,
                    'answer': parent_answer.upper(),
                    'net_loss': round(net_loss, 2),
                    'recovery_percent': round(recovery_percent, 0),
                    'recommendation': cleaned,
                    'editable': True
                })
            else:
                # Failed - return placeholder
                all_recommendations.append({
                    'indicator': indicator,
                    'question': parent_question,
                    'answer': parent_answer.upper(),
                    'net_loss': round(net_loss, 2),
                    'recovery_percent': round(recovery_percent, 0),
                    'recommendation': f'[Error generating recommendation: LLM returned status {response.status_code}]',
                    'editable': True
                })
                
        except Exception as e:
            # Error - return placeholder
            all_recommendations.append({
                'indicator': indicator,
                'question': parent_question,
                'answer': parent_answer.upper(),
                'net_loss': round(net_loss, 2),
                'recovery_percent': round(recovery_percent, 0),
                'recommendation': f'[Error: {str(e)}]',
                'editable': True
            })
    
    return jsonify({
        'success': True,
        'recommendations': all_recommendations
    })



@app.route('/debug')
def debug_questions():
    """Debug endpoint to see all questions in database."""
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT block, COUNT(*) as count FROM questions GROUP BY block ORDER BY block")
        blocks = cur.fetchall()
        
        cur.execute("SELECT number, question, block FROM questions ORDER BY block, number")
        questions = cur.fetchall()
        
        return jsonify({
            'blocks': [dict(row) for row in blocks],
            'total_questions': len(questions),
            'sample_questions': [dict(row) for row in questions[:10]]
        })
    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    # Ensure static directory exists
    os.makedirs('static', exist_ok=True)
    
    # Initialize database
    initialize_db()
    
    print("Ethics Readiness Levels Tool - Version 0.2-dev")
    print("================================================")
    print("🚧 DEVELOPMENT VERSION - NOT FOR PRODUCTION USE 🚧")
    print("A four-level, iterative method to track ethical reflection in AI systems")
    print("Starting local Flask server...")
    print("Open your web browser and go to: http://localhost:8080")
    print("Press Ctrl+C to stop the server")
    print()
    
    app.run(debug=True, host='127.0.0.1', port=8080)