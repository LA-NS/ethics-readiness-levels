# Ethics Readiness Levels (ERL) Tool: Description and Logic

## 1. Introduction and the Necessity of Dialogue

Evaluating the ethical maturity of AI systems requires more than checklist compliance: it demands *structured reflection* among stakeholders. High-level principles (transparency, fairness, accountability) must be translated into concrete, context-sensitive questions that technical and non-technical actors can discuss together. The Ethics Readiness Levels (ERL) tool is designed to support this need by turning abstract values into a *dialogue-led*, stepwise assessment. The tool explicitly assumes that the assessment is conducted *with a partner*—a colleague, an ethics advisor, or a domain expert—so that each question becomes an occasion for shared interpretation and deliberation rather than a yes/no formality. This dialogue is necessary to surface assumptions, clarify scope, and align the evaluation with the specific use case and organisational context.

## 2. What the ERL Tool Is

The ERL tool is a software implementation of the *Ethics Readiness Levels* method: a four-level, iterative framework for tracking how ethical reflection is integrated into the design and deployment of AI systems (Adomaitis et al., 2025). The method bridges high-level ethical principles and everyday engineering practice by converting ethical values into concrete prompts, checks, and controls that can be applied within real use cases. The evaluation is carried out via a *dynamic, tree-like questionnaire* built from context-specific indicators, so that the questions presented are relevant both to the technology and to the application domain.

Beyond functioning as a managerial or self-assessment instrument, the ERL tool is intended to facilitate a *structured dialogue* between ethics experts and technical teams, while a scoring mechanism helps track progress over time and supports comparison across projects or iterations.

## 3. Logic and Purpose

**Structure.** The tool organises questions into *blocks*. Every assessment includes a core “zero case” block of general ethical considerations (e.g. impact on autonomy, security, accessibility, environment, labour, auditability, oversight). Additional blocks are activated depending on the *profile* of the use case: for example, products that process personal data receive a GDPR-oriented block; those intended for law-enforcement contexts receive a dedicated block; and those that use AI receive a general AI-act–oriented block. The profile is determined by a short onboarding sequence so that the questionnaire adapts to the respondent’s context.

**Navigation.** Questions are arranged hierarchically (e.g. a top-level question with sub-questions 1.1, 1.2, …). Answering “yes” to a parent typically leads to more specific follow-ups; answering “no” skips sub-questions and moves to the next main theme. This keeps the path through the questionnaire relevant and avoids unnecessary length.

**Scoring.** The tool assigns a starting score (e.g. on a 0–4 scale) and updates it with each answer according to predefined weights (positive or negative contributions). The result is a *progression* of the ethics readiness score across the answered indicators, supporting both a final level and a narrative of where gains or concerns arise.

**Purpose.** The overall purpose is to make ethical reflection *actionable*: to prompt teams to articulate and justify their choices, to identify gaps (e.g. missing safeguards or documentation), and to encourage a shift from narrow technological solutionism toward an ethics-by-design mindset.

## 4. Example: The Healthcare AI Module

To illustrate how the method is specialised by domain, the tool includes an optional **Healthcare AI** module (developed in the context of the AIOLIA project). When the respondent indicates that the system is a *healthcare AI* application (e.g. clinical decision support, medical imaging, or patient-data analytics), the tool can follow an “AIOLIA Healthcare route.” In this route, the assessment combines the core ethical block with a *healthcare-specific* block rather than the generic AI block, so that the indicators align with clinical and regulatory expectations.

The healthcare AI block addresses themes such as:

- **Patient autonomy and shared decision-making** (e.g. information and consent, including dynamic or electronic opt-out);
- **Role of the AI relative to clinical judgment** (complement vs. replacement, overrideability, automation bias and training);
- **Fairness and non-discrimination** (representative data, multi-institutional collaboration, audits for contextual, racial, or gender bias);
- **Data and safety** (sensitive biomedical data, cybersecurity, anonymisation, clinical validation, and safeguards against commercialisation or misuse);
- **Explainability and transparency** (black-box risk, clinician-facing rationale, documentation of assumptions and limitations);
- **Ethical oversight and accountability** (integration of ethicists, impact assessments, standardised checklists, liability and compensation);
- **Clinical validity and justifiability** (accuracy, alignment with medical standards and patient values, and justification at the level of individual inference);
- **Sub-population and atypical-anatomy bias** (performance disparities, rare comorbidities);
- **Usability in the clinical workflow** (presentation of risk scores, heatmaps, and documentation for clinicians and regulators).

Each indicator is associated with score contributions so that the same dialogue-led, stepwise logic applies: the team answers in context, and the tool records both the path taken and the resulting ethics readiness progression. The healthcare module thus serves as a concrete example of how the ERL method can be extended to a high-stakes, regulated domain while preserving the emphasis on dialogue and context-specific reflection.

---

*References:* Adomaitis, L., Israel-Jost, V., & Grinbaum, A. (2025). Ethics Readiness of Artificial Intelligence: A Practical Evaluation Method. *arXiv:2512.09729* [cs.CY].  
The tool implementation is developed and hosted by RISE (Research Institutes of Sweden). Funding: AIOLIA (EU Grant 101187937), MultiRATE (EU Horizon 101073929), SOPRANO (EU Horizon 101120990).
