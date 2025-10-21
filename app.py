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
from flask import Flask, jsonify, request, session, render_template

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

    result = {
        'score': round(score, 2),
        'message': message,
        'graph_json': graph_json,
        'final_level': f"LPERL {int(score) if score <= 4 else 4}",
        'has_graph': HAS_PLOTLY
    }
    
    session.clear()
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


@app.route('/determine_blocks', methods=['POST'])
def determine_blocks_endpoint():
    """Determine which question blocks to include based on user's initial answers."""
    answers = {
        'product_for_LEAs': request.form.get('product_for_LEAs', 'no'),
        'uses_personal_data': request.form.get('uses_personal_data', 'no'),
        'uses_AI': request.form.get('uses_AI', 'no')
    }
    
    session['determining_answers'] = answers
    session['blocks'] = determine_blocks(answers)
    session['current_block_index'] = 0
    session['current_question'] = get_first_question_of_block(session['blocks'][0])

    print(f"Determined blocks: {session['blocks']}")
    print(f"First question: {session['current_question']}")

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
                            'block': question['block']
                        },
                        'score': session.get('score', 4),
                        'block': current_block
                    })

            # Move to next block
            session['current_block_index'] += 1
            session.pop('current_question', None)

    # No more questions
    return jsonify(end_session_and_present_results())


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
        cur.execute("SELECT yes_score, no_score FROM questions WHERE number = ?", 
                   (str(current_question_number),))
        scores = cur.fetchone()
    finally:
        cur.close()
        conn.close()

    if not scores:
        return jsonify({'error': 'Question not found'}), 404

    # Calculate score change
    score_change = scores['yes_score'] if answer.lower() == 'yes' else scores['no_score']
    session['score'] = round(session.get('score', 4) + score_change, 3)
    
    # Store answer
    session.setdefault('answers', {})[current_question_number] = answer
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
        'score': session.get('score', 4)
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


@app.route('/restart', methods=['GET'])
def restart():
    """Restart the assessment by clearing the session."""
    session.clear()
    return jsonify({'message': 'Session cleared'})


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