#!/usr/bin/env python3
"""
Deep audit of LPERL scoring system.
Checks if child questions can fully recover parent losses.
"""

import sqlite3
from collections import defaultdict

def analyze_schema():
    conn = sqlite3.connect('lperl_local.sqlite')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    
    # Get all questions
    cur.execute("SELECT * FROM questions ORDER BY CAST(number AS REAL)")
    questions = {row['number']: dict(row) for row in cur.fetchall()}
    
    # Build parent-child relationships
    relationships = defaultdict(list)
    for qnum in questions.keys():
        if '.' in qnum:
            parts = qnum.split('.')
            parent = '.'.join(parts[:-1])
            if parent in questions:
                relationships[parent].append(qnum)
    
    print("=" * 80)
    print("LPERL SCORING AUDIT REPORT")
    print("=" * 80)
    print()
    
    issues = []
    
    # Check each parent question
    for parent_num, parent_q in questions.items():
        children = relationships.get(parent_num, [])
        
        # Only analyze questions that have negative scores (create loss)
        yes_loss = parent_q['yes_score'] < 0
        no_loss = parent_q['no_score'] < 0
        
        if yes_loss or no_loss:
            # Calculate maximum possible recovery from children
            max_yes_recovery = sum(
                max(questions[child]['yes_score'], 0) for child in children
            )
            max_no_recovery = sum(
                max(questions[child]['no_score'], 0) for child in children
            )
            
            # Check YES path
            if yes_loss:
                loss = abs(parent_q['yes_score'])
                recoverable = max_yes_recovery
                gap = round(loss - recoverable, 3)
                
                if gap > 0.001:  # More than rounding error
                    issues.append({
                        'indicator': parent_num,
                        'path': 'YES',
                        'question': parent_q['question'],
                        'loss': loss,
                        'recoverable': recoverable,
                        'gap': gap,
                        'children': children
                    })
                    
                    print(f"❌ ISSUE: Indicator {parent_num} (YES path)")
                    print(f"   Question: \"{parent_q['question']}\"")
                    print(f"   Loss: {loss:.3f} pts")
                    print(f"   Max recovery from children: {recoverable:.3f} pts")
                    print(f"   UNRECOVERABLE GAP: {gap:.3f} pts")
                    print(f"   Children: {children}")
                    
                    for child in children:
                        c = questions[child]
                        print(f"      {child}: YES={c['yes_score']:+.3f}, NO={c['no_score']:+.3f}")
                    print()
            
            # Check NO path
            if no_loss:
                loss = abs(parent_q['no_score'])
                recoverable = max_no_recovery
                gap = round(loss - recoverable, 3)
                
                if gap > 0.001:
                    issues.append({
                        'indicator': parent_num,
                        'path': 'NO',
                        'question': parent_q['question'],
                        'loss': loss,
                        'recoverable': recoverable,
                        'gap': gap,
                        'children': children
                    })
                    
                    print(f"❌ ISSUE: Indicator {parent_num} (NO path)")
                    print(f"   Question: \"{parent_q['question']}\"")
                    print(f"   Loss: {loss:.3f} pts")
                    print(f"   Max recovery from children: {recoverable:.3f} pts")
                    print(f"   UNRECOVERABLE GAP: {gap:.3f} pts")
                    print(f"   Children: {children}")
                    print()
    
    print("=" * 80)
    print(f"SUMMARY: Found {len(issues)} scoring issues")
    print("=" * 80)
    print()
    
    # Check for orphaned positive scores (rewards with no parent loss)
    print("CHECKING FOR ORPHANED POSITIVE SCORES...")
    print()
    for qnum, q in questions.items():
        if '.' in qnum:  # Is a child
            parts = qnum.split('.')
            parent_num = '.'.join(parts[:-1])
            
            if parent_num in questions:
                parent = questions[parent_num]
                
                # If child has positive YES score, parent must have negative YES score
                if q['yes_score'] > 0 and parent['yes_score'] >= 0:
                    print(f"⚠️  WARNING: {qnum} has YES reward (+{q['yes_score']}) but parent {parent_num} has no YES loss")
                
                # If child has positive NO score, parent must have negative NO score  
                if q['no_score'] > 0 and parent['no_score'] >= 0:
                    print(f"⚠️  WARNING: {qnum} has NO reward (+{q['no_score']}) but parent {parent_num} has no NO loss")
    
    conn.close()
    return issues

if __name__ == '__main__':
    analyze_schema()
