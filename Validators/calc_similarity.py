#!/usr/bin/env python3
"""
Usage:
    python Validators/calc_similarity.py <path_to_task_dir>

Computes similarity 0-100 between this task's 5_Prompt.txt and every other
project prompt (Tasks/*/5_Prompt.txt + QC_Tasks/V3_Tasks/*/Prompt.txt) so
the pipeline knows BEFORE platform upload whether the prompt is at risk
of the 40% similarity ceiling.

Method: Jaccard similarity on word bigrams (lowercase, punctuation-stripped).
Catches paraphrased and rephrased prompts, not just verbatim copies. Score
ranges 0 (no shared bigrams) to 100 (identical bigram sets).

Output:
    - stdout: ranked top-10 most-similar prompts with scores
    - <task_dir>/_aux/Similarity_Report.json
    - Exit 0 if all scores < 40, exit 1 if any >= 40 (needs Class B pivot)
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TASKS_DIR = ROOT / "Tasks"
QC_V3_DIR = ROOT / "QC_Tasks" / "V3_Tasks"


def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    return [t for t in text.split() if t]


def bigrams(tokens):
    return set(zip(tokens, tokens[1:]))


def jaccard(a, b):
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return (inter / union * 100.0) if union else 0.0


def gather_corpus(self_path):
    out = []
    for pattern_dir, pattern in ((TASKS_DIR, "*/5_Prompt.txt"), (QC_V3_DIR, "*/Prompt.txt")):
        if not pattern_dir.is_dir():
            continue
        for p in pattern_dir.glob(pattern):
            if p.resolve() == self_path.resolve():
                continue
            if not p.is_file() or p.stat().st_size == 0:
                continue
            try:
                text = p.read_text(encoding="utf-8").strip()
            except UnicodeDecodeError:
                continue
            if not text:
                continue
            out.append((str(p.relative_to(ROOT)), text))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task_dir")
    args = ap.parse_args()
    task_dir = Path(args.task_dir).resolve()
    self_path = task_dir / "5_Prompt.txt"
    if not self_path.is_file():
        print(f"ERROR: {self_path} not found", file=sys.stderr)
        sys.exit(2)
    self_text = self_path.read_text(encoding="utf-8").strip()
    if not self_text:
        print(f"ERROR: {self_path} is empty", file=sys.stderr)
        sys.exit(2)

    self_bg = bigrams(tokenize(self_text))
    corpus = gather_corpus(self_path)

    scored = []
    for path, text in corpus:
        score = round(jaccard(self_bg, bigrams(tokenize(text))), 1)
        scored.append({"path": path, "score": score})
    scored.sort(key=lambda r: r["score"], reverse=True)

    over_ceiling = [r for r in scored if r["score"] >= 40]
    near_ceiling = [r for r in scored if 25 <= r["score"] < 40]

    out = {
        "task": task_dir.name,
        "this_prompt": str(self_path.relative_to(ROOT)),
        "corpus_size": len(corpus),
        "top10": scored[:10],
        "over_40_ceiling": over_ceiling,
        "near_25_to_40": near_ceiling,
        "max_score": scored[0]["score"] if scored else 0.0,
    }

    out_path = task_dir / "_aux" / "Similarity_Report.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")

    print(f"=== Similarity report: {task_dir.name} ===")
    print(f"Self:         {out['this_prompt']}")
    print(f"Corpus size:  {len(corpus)} other prompts")
    print(f"Max score:    {out['max_score']}")
    print()
    print(f"Top 10 most similar:")
    for r in scored[:10]:
        flag = " >>> OVER 40 CEILING" if r["score"] >= 40 else (" (near ceiling)" if r["score"] >= 25 else "")
        print(f"  {r['score']:>5.1f}  {r['path']}{flag}")
    print()
    print(f"Written:      {out_path}")

    if over_ceiling:
        print(f"\nSTOP: {len(over_ceiling)} prompt(s) at >= 40 similarity.")
        print("This will be blocked by the platform linter. Pivot the prompt via PIPELINE S1.5 (Class B).")
        sys.exit(1)
    print(f"\n[OK] all similarity scores < 40 — clear of the ceiling")
    sys.exit(0)


if __name__ == "__main__":
    main()
