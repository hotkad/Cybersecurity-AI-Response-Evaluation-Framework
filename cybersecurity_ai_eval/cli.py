"""CLI for scenario validation and human-review scoring."""
import argparse, csv, json
from pathlib import Path
from .scoring import score_review

def main():
    parser=argparse.ArgumentParser(description="Human-led cybersecurity AI evaluation")
    sub=parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    ev=sub.add_parser("evaluate"); ev.add_argument("--responses", required=True); ev.add_argument("--out", default="reports")
    args=parser.parse_args()
    if args.command=="validate":
        data=json.loads(Path("data/scenarios/scenarios.json").read_text(encoding="utf-8"))
        ids=[x["id"] for x in data]
        assert len(ids)==20 and len(ids)==len(set(ids)), "Expected 20 unique scenarios"
        assert all(x.get("prompt") and x.get("reference_expectations") for x in data), "Missing scenario fields"
        print("Validated 20 unique scenarios."); return
    data=json.loads(Path(args.responses).read_text(encoding="utf-8")); reviews=data.get("reviews", data) if isinstance(data,dict) else data
    results=[]
    for i,r in enumerate(reviews):
        for field in ("scenario_id","ratings","evidence_notes"):
            if field not in r: raise ValueError(f"Review {i} missing {field}")
        result=score_review(r); result.update({"reviewer":r.get("reviewer","unspecified"),"evidence_notes":r["evidence_notes"]}); results.append(result)
    out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    (out/"evaluation-results.json").write_text(json.dumps(results,indent=2),encoding="utf-8")
    fields=list(results[0]) if results else ["scenario_id","model","score"]
    with (out/"evaluation-results.csv").open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=fields); writer.writeheader(); writer.writerows(results)
    print(f"Scored {len(results)} human reviews; reports saved to {out}.")
if __name__=="__main__": main()
