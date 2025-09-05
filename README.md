# Ethics Readiness Levels (ERLs)

This repository contains the research paper and data for **Ethics Readiness Levels (ERLs)**, a four-level, iterative method to track how ethical reflection is implemented in the design of AI systems.

**Paper:** "Ethics Readiness of Artificial Intelligence: A Practical Evaluation Method" (under review)

**Authors:** Laurynas Adomaitis (RISE), Vincent Israel-Jost (CEA-Saclay/Larsim), Alexei Grinbaum (CEA-Saclay/Larsim)

## About The Project

The ERL methodology addresses a critical challenge in AI governance: translating high-level ethical principles and values into operational, actionable steps for AI researchers and software developers.

Instead of a static, "box-ticking" checklist, ERLs provide a framework to facilitate structured dialogue, guide reflection, and systematically track the integration of ethical thinking throughout the AI development lifecycle. The primary goal is to foster a shift from narrow technological solutionism to a more reflective, ethics-by-design approach.

## The ERL Methodology

The methodology is built on four key pillars:

#### 1. The 5 Ethics Readiness Levels

The ERL scale measures the maturity of ethical integration in a project, from initial unawareness to full control and accountability.

* **ERL 0 – Lacking:** Ethical considerations are absent from the development process.

* **ERL 1 – Identified:** Potential ethical issues, risks, and societal impacts have been identified.

* **ERL 2 – Characterized:** The interactions, tradeoffs, and tensions between different ethical issues are understood.

* **ERL 3 – Harmonized:** Ethical considerations are proactively addressed and integrated into the system's design (Ethics-by-Design).

* **ERL 4 – Controlled:** Robust control mechanisms for accountability, oversight, and verification are implemented.

#### 2. Modular Indicator Blocks

The evaluation is tailored to specific contexts using modular **Indicator Blocks**. These are sets of indicators grouped by technology or application area, ensuring the assessment is always relevant to the use case. This repository contains the following blocks:

* Common

* AI

* Privacy

* Law Enforcement

* Robotics

#### 3. Dynamic Tree-Like Questionnaire

We use a tree-like structure for the questionnaire. Questions branch based on "yes" or "no" answers, ensuring that the evaluation is efficient and only presents relevant indicators. This avoids overwhelming users and adapts dynamically to the specifics of the system being evaluated.

#### 4. Progressive Scoring

The scoring system is designed to track progress over time. Rather than a simple pass/fail, it quantifies the state of ethics readiness, gamifying the process to motivate continuous improvement and reflective design. The true value, however, lies in the dialogue and reflection the process generates.

## Repository Contents

* `README.md`: This overview file.

* `Ethics_Readiness_Levels_Paper.pdf`: The full research paper detailing the methodology.

* `/indicators`: A directory containing the CSV files with the indicators and scoring weights for each block.

  * `common_block.csv`

  * `ai_block.csv`

  * `privacy_block.csv`

  * `lea_block.csv` (Law Enforcement)

  * `robotics_block.csv`

Each CSV file contains the following columns: `number`, `indicator`, `yes_score`, `no_score`.

## How to Use This Methodology

This repository does not contain an executable software tool but rather the components of a methodology designed to facilitate structured dialogue.

1. **Read the Paper:** Start by reading the full research paper to understand the methodology, its theoretical underpinnings, and the case studies.

2. **Select Indicator Blocks:** Choose the relevant indicator block `.csv` files for your project. For example, for an AI-powered collaborative robot, you would use `common_block.csv`, `ai_block.csv`, and `robotics_block.csv`.

3. **Facilitate a Dialogue:** In a session with an ethics expert and the technical team, use the `indicator` column from the selected files as prompts for a guided discussion.

4. **Track Progress:** Follow the tree-like structure implied by the indicator numbers (e.g., 2.1 is a sub-question of 2). While the scoring (`yes_score`, `no_score`) can be used to track progress between sessions, the primary goal is the qualitative reflection and design changes that result from the dialogue.

The ERL tool is most effective when used iteratively (e.g., every 6-12 months) to measure progress and guide development, not as a one-time audit. Comparison between use cases is discouraged and often meaningless, however tracking progress over time and having iterative dialogue is very a very effective ethics-by-design approach.

## Citation

Research article with the full methodology of how to use this tool is under review.

## License

This project is licensed under the GNU General Public License v3.0. See the `LICENSE` file for more details.

## Contact

For questions about the methodology, please contact the authors Laurynas Adomaitis (RISE), Vincent Israel-Jost (CEA), or Alexei Grinbaum (CEA).
