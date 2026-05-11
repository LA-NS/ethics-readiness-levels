# Validation 1 Changes Report

This document records the Healthcare AI block updates implemented from client validation notes focused on improving question formulation, practical usefulness, and clarity.

## Scope

- File changed: `schema.sql`
- Block changed: `healthcare_ai`
- Change type: question wording updates and one new top-level question
- No structural DB schema changes (tables/indexes unchanged)
- Existing scoring kept unless explicitly requested otherwise

## Implemented Changes

### 1) Question `25.3.1` (automation bias controls)

- **Previous text:** "Are healthcare workers trained to identify AI limitations and mitigate automation bias?"
- **New text:** "Beyond training, are there operational safeguards (e.g., mandatory human verification, override documentation, second-reader checks, monitoring) to mitigate automation bias?"
- **Why:** Meeting feedback indicated training alone is insufficient to mitigate clinician over-reliance. The new wording asks for concrete operational controls, not only education.
- **Scoring:** unchanged (`yes_score=0.20`, `no_score=0`)

### 2) Question `28` (explainability -> practical justification)

- **Previous text:** "Does the AI model's complexity create a \"black box\" that limits clinical explainability?"
- **New text:** "Do model complexity or design choices prevent clinically useful justification of outputs at the point of care?"
- **Why:** Notes emphasized that abstract "universe-level explainability" is often not actionable. The new wording targets clinically useful decision support.
- **Scoring:** unchanged (`yes_score=-0.40`, `no_score=0`)

### 3) Question `28.1` (case-level rationale)

- **Previous text:** "Is the system transparent enough for clinicians to understand the rationale behind its recommendations?"
- **New text:** "Can clinicians access clear, case-level rationale they can use to defend and communicate AI-informed decisions?"
- **Why:** Clarifies practical utility for real patient cases and communication duties, consistent with requested shift from generic transparency to usable justification.
- **Scoring:** unchanged (`yes_score=0.20`, `no_score=0`)

### 4) Question `31.1` (remove patient values phrase)

- **Previous text:** "Are the AI outputs supported by reasons that align with professional medical standards and patient values?"
- **New text:** "Are the AI outputs supported by reasons that align with professional medical standards?"
- **Why:** Based on validation note that "patient values" was undefined and variable; user requested simplifying by deleting that phrase.
- **Scoring:** unchanged (`yes_score=0`, `no_score=-0.12`)

### 5) Question `31.2` (stronger justification standard)

- **Previous text:** "Can the system provide justification for individual patient recommendations to help clinicians explain treatment choices?"
- **New text:** "For individual recommendations, can the system provide justification grounded in intended use, demonstrated outcome impact, and statistically valid evidence?"
- **Why:** Directly implements note to adjust `31.2` toward evidence-based justification (intended use, impact, statistical validity), not generic explanation.
- **Scoring:** unchanged (`yes_score=0`, `no_score=-0.08`)

### 6) Question `32` (bias wording precision)

- **Previous text:** "Does the AI exhibit bias specific to clinical sub-populations or atypical anatomies?"
- **New text:** "Is there evidence that performance differs across clinically relevant sub-populations or atypical anatomies?"
- **Why:** Reframes from broad accusation-style language to measurable performance disparity evidence, improving assessment precision.
- **Scoring:** unchanged (`yes_score=-0.30`, `no_score=0`)

### 7) Added new top-level question `34` (value/reimbursement feasibility)

- **New question text:** "Is there evidence that the AI delivers measurable operational or clinical value that can justify adoption in settings with limited or no direct reimbursement?"
- **Why:** Implements client note that hospitals prioritize bottleneck removal/throughput and practical value, especially when reimbursement is limited.
- **Scoring:** set per explicit instruction (`yes_score=0`, `no_score=-0.30`)
- **ID used:** `2039` (new row in `healthcare_ai`)
- **Numbering decision:** added as `34` while keeping existing `33`, `33.1`, `33.2` unchanged.

## Explicitly Not Changed

The following stayed unchanged per user decisions: `25.3`, `29`, `29.4`, `30`, `30.2`, `31`, `32.1`, `32.1.1`, and `33`-series.

## Consistency Notes

- Question numbering in `healthcare_ai` now continues through `34`.
- Existing block logic and score model remain intact.
- Changes are formulation-focused and compatible with current yes/no flow.
