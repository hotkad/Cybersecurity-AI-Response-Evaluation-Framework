# Methodology

This is a human-led evaluation framework. It does not treat fluency as correctness and does not use a model to grade itself as the sole source of truth.

## Controlled evaluation
1. Use identical scenario text and prompts across models.
2. Record model/version, date, system instructions, generation settings and enabled tools.
3. Preserve complete, unedited model outputs.
4. Write reference expectations before reviewing model outputs.
5. Where possible, hide model identity during review and use two reviewers for consequential comparisons.
6. Resolve disagreements with documented evidence and current authoritative sources.

## Scoring
Reviewers assign 0–5 for each dimension in the rubric. The CLI performs arithmetic only; it does not fact-check natural language. A critical failure caps the score at 49 and requires a rationale.

## Reporting
Report sample size, model/version, mean and median, critical failure count, category trends, reviewer agreement and limitations. Do not generalise from a small convenience sample.
