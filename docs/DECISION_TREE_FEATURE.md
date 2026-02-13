# 📋 Decision Tree Feature Implementation

## What Was Added

### Backend Changes (`app.py`)

**New Function: `analyze_decision_tree()`**
- Analyzes all answers and their score impacts
- Identifies indicators that caused score loss
- Tracks whether those losses were recovered later
- Returns detailed tree data for visualization

**Key Logic:**
- For each indicator answer:
  - Calculates score change (before/after)
  - Marks as "problematic" if:
    - Score decreased (score_change < 0)
    - AND was never fully recovered (no subsequent answer brought score back to previous level)
  - Keeps track of the full decision path

**Updated `end_session_and_present_results()`**
- Calls `analyze_decision_tree()` to get decision data
- Includes decision tree and problematic indicators in response JSON
- Sends full assessment history to frontend

---

### Frontend Changes (`templates/index.html`)

**Updated `displayResults()` function**

Now displays three sections at the end of assessment:

#### 1. **Score Cards** (unchanged)
- Final Score
- LPERL Level

#### 2. **Assessment Message** (unchanged)
- Personalized feedback based on score

#### 3. **NEW: Decision Tree Visualization** 📊

Shows every answer in a scrollable tree with:

**Color Coding:**
- 🟢 **Green** - Answers that gained points
- 🟡 **Yellow** - Answers with no score change
- 🔴 **Red** - Answers that lost points AND were not recovered

**Information per Row:**
- Indicator number (e.g., "1.2.1")
- Answer given (YES/NO)
- Score change (±0.XXX)
- Full score progression (before → after)

**Example Output:**
```
1 → YES ✓                           +0.000 (4.000 → 4.000)
1.1 → YES ✓                         +0.360 (4.000 → 4.360)
1.2 → NO ✓                          +0.360 (4.360 → 4.720)
2 → YES ✗                           -1.000 (4.720 → 3.720)  ← RED (never recovered)
3.1 → NO →                          +0.000 (3.720 → 3.720)
```

#### 4. **NEW: Areas of Concern Alert** ⚠️

If there are problematic indicators (red ones), shows:
- Yellow warning box with list of problematic indicators
- Shows which indicator and answer choice caused the issue
- Displays how many points were lost
- Provides the score range affected

**Example:**
```
⚠️ Areas of Concern (Points Lost & Not Recovered):

• Indicator 2 (Answer: YES)
  Lost 1.000 points (Score dropped from 4.720 to 3.720)

• Indicator 5.2 (Answer: NO)
  Lost 0.365 points (Score dropped from 2.355 to 1.990)
```

---

## Visual Design

### Decision Tree Container
- **Max Height:** 400px with scrollable overflow
- **Background:** Light gray (#f9f9f9)
- **Border:** 1px solid #ddd
- **Font:** Monospace for clean alignment

### Color System
- **Green Background** (#d4edda): Positive answers
- **Yellow Background** (#fff3cd): Warning/neutral
- **Red Background** (#f8d7da): Problematic answers

### Interactive Elements
- Hover effects on tree rows
- Clear visual hierarchy
- Print-friendly design

---

## Data Flow

```
User completes assessment
         ↓
User submits final answer
         ↓
POST /answer endpoint processes
         ↓
No next question available
         ↓
Call end_session_and_present_results()
         ↓
Call analyze_decision_tree() to process all answers
         ↓
Returns: {
  decision_tree: [
    { indicator, answer, score_before, score_after, score_change, is_problematic },
    ...
  ],
  problematic_indicators: [
    { indicator, answer, score_change, score_before, score_after },
    ...
  ]
}
         ↓
Frontend receives JSON
         ↓
displayResults() builds HTML with decision tree
         ↓
User sees full assessment path with problematic areas highlighted
```

---

## Example Scenario

**Assessment path:**
1. Indicator 1.1 → YES → +0.36 points ✓
2. Indicator 1.2 → YES → +0.36 points ✓
3. Indicator 2 → NO → -1.0 points ✗ (causes score drop to 3.72)
4. Indicator 3 → YES → +0.0 points
5. Indicator 4 → YES → +0.5 points ✓
6. Indicator 5 → NO → -0.3 points (score now 3.92, still below the 4.72 from before Indicator 2)

**Result:**
- Indicator 2 is shown in RED because:
  - It lost 1.0 point
  - The score never fully recovered (even with +0.5 later, still at 3.92 < 4.72)
  
- Indicator 5 shows in YELLOW (neutral or gained) because:
  - Though it lost 0.3 points, losses were already marked elsewhere
  - Focus is on the main problematic answers

---

## Benefits

✅ **Transparency** - Users see exactly where they lost points
✅ **Actionable** - Red indicators show improvement areas
✅ **Detailed** - Every answer is visible in the tree
✅ **Visual** - Color coding makes problems obvious
✅ **Context** - Shows score before/after for each answer
✅ **Recovery Tracking** - Shows if losses were recovered

---

## Next Possible Enhancements

- Download decision tree as CSV/JSON
- Comparison of decision trees across multiple assessments
- Recommendations based on problematic indicators
- Filter tree by indicator category (1.x, 2.x, etc.)
- Timeline animation of score progression
