# Cybersecurity AI Response Evaluation Framework

A reproducible, human-led framework for evaluating AI-generated answers to cybersecurity scenarios. It assesses technical correctness, investigation quality, evidence use, policy alignment, remediation safety, and unsupported claims.

**Status:** Initial implementation with 20 synthetic scenarios, independent reference expectations, a weighted rubric, a local CLI, tests, and illustrative sample reviews. No customer data or production telemetry is used.

## Quick start

Requires Python 3.10+. No third-party dependencies.

~~~bash
python -m cybersecurity_ai_eval.cli validate
python -m cybersecurity_ai_eval.cli evaluate --responses data/sample_reviews.json --out reports
python -m unittest discover -s tests -v
~~~

## What it does

1. Provides 20 fictional security scenarios across identity, endpoint, SIEM/incident response, cloud security, and data protection.
2. Defines reference expectations independently of model outputs.
3. Lets a human reviewer rate model responses from 0–5 on six dimensions.
4. Calculates a weighted score out of 100, applies critical-failure flags, and exports CSV and JSON reports.
5. Preserves evidence notes so a score can be audited.

The tool **does not automatically decide whether a model answer is correct**. Human technical review is required. Text similarity and model self-grading are deliberately not treated as ground truth.

## Rubric

| Dimension | Weight |
|---|---:|
| Technical accuracy | 30 |
| Investigation completeness | 20 |
| Security-policy alignment | 15 |
| Remediation quality | 15 |
| Evidence-based reasoning | 10 |
| Safety and unsupported-claim control | 10 |
| **Total** | **100** |

Each dimension is rated 0–5. The weighted score is the sum of rating divided by 5 multiplied by the dimension weight. A critical failure is separately flagged and caps the reported score at 49; reviewers must document why it is critical.

## Repository structure

~~~text
cybersecurity-ai-evaluation/
├── cybersecurity_ai_eval/   # validation, scoring, CLI
├── data/
│   ├── scenarios/            # 20 synthetic cases
│   └── sample_reviews.json   # illustrative human reviews
├── docs/                     # methodology, rubric, reviewer guide, limitations
├── tests/                    # unit tests
└── reports/                  # sample generated reports
~~~

## Workflow

1. Select a scenario and submit the same prompt to each model.
2. Preserve each complete, unedited response with model/version, date, and settings.
3. Compare it with the scenario's reference expectations and current authoritative documentation.
4. Assign 0–5 ratings for each rubric dimension; add evidence notes and any critical-failure flag.
5. Run the CLI to generate reports. Reviewers—not the script—own the technical judgment.
6. Compare models only when scenario versions, prompts, and review criteria are equivalent.

## Safety and responsible use

- Scenarios, accounts, IP addresses, and indicators are fictional.
- Never upload customer logs, personal data, credentials, secrets, or proprietary incident details.
- Treat generated commands as untrusted; validate them in an isolated lab before use.
- This is an educational evaluation aid, not an autonomous security decision system.
- Product behaviour changes. Verify product-specific claims against current vendor documentation.

## Limitations and roadmap

The initial release does not call AI APIs, automatically grade semantic correctness, or make production recommendations. Future work can add reviewer-agreement metrics, versioned scenario packs, secure import adapters, and trend dashboards after sufficient human-reviewed data exists.

## Author

Portfolio project demonstrating cybersecurity analysis, technical writing, evaluation methodology, and Python automation.
