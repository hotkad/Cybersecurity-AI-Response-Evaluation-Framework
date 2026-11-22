# Reviewer guide

1. Read the scenario and reference expectations before reviewing the answer.
2. Separate observed facts from assumptions and hypotheses.
3. Verify product-specific claims against current primary documentation (for example, Microsoft Learn for Microsoft products, NIST publications for risk frameworks, and OWASP for LLM/application risks).
4. Assign each rubric dimension a 0–5 rating independently.
5. Record the response claim, why it is correct/incorrect, and the source checked. Do not place sensitive data in notes.
6. Flag critical failure only for materially unsafe guidance or significant fabrication; explain why.

## Review input
The CLI accepts a JSON array or an object containing a `reviews` array. Each review requires `scenario_id`, `ratings`, and `evidence_notes`; `model`, `reviewer`, and `critical_failure` are supported optional fields. Ratings must include all six rubric keys and values 0–5.
