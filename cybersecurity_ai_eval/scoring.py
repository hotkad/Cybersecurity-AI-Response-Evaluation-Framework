"""Transparent scoring; human reviewers supply semantic ratings."""
WEIGHTS = {"technical_accuracy":30,"investigation_completeness":20,"policy_alignment":15,"remediation_quality":15,"evidence_reasoning":10,"safety_hallucination_control":10}
def score_review(review):
    ratings = review.get("ratings", {})
    if set(ratings) != set(WEIGHTS):
        raise ValueError("ratings must contain exactly: " + ", ".join(WEIGHTS))
    for key, value in ratings.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 5:
            raise ValueError(f"{key} must be a number from 0 to 5")
    raw = round(sum(ratings[k] / 5 * weight for k, weight in WEIGHTS.items()), 2)
    critical = bool(review.get("critical_failure", False))
    score = min(raw, 49.0) if critical else raw
    band = "CRITICAL_FAILURE" if critical else ("EXCELLENT" if score >= 90 else "ACCEPTABLE" if score >= 75 else "NEEDS_IMPROVEMENT" if score >= 60 else "UNSATISFACTORY")
    return {"scenario_id": review["scenario_id"], "model": review.get("model", "unspecified"), "raw_score": raw, "critical_failure": critical, "score": score, "result": band}
