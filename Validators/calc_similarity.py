#!/usr/bin/env python3
"""
Usage:
    python Validators/calc_similarity.py <path_to_task_dir>
    python Validators/calc_similarity.py <path_to_task_dir> --explain <prior_task_dir>

Multi-dimensional similarity 0-100 between this task's 5_Prompt.txt and every
other project prompt. The COMPOSITE score combines lexical similarity
(word_bigram, word_unigram, word_count) with a MULTIPLICATIVE CONTEXT
modifier that weights contextual analysis (business function, persona,
universe) MORE than raw word stats. Same constants leave lexical similarity
intact; DIFFERENT constants REDUCE the composite multiplicatively (strong
contextual differentiators dominate lexical overlap).

Context multipliers (applied when constants DIFFER):
  business_function differs  ×  0.6   (~40% reduction)
  persona differs            ×  0.6
  universe differs           ×  0.7

Max compounded reduction when all three differ: × 0.252 (~75% reduction).

Bands (simplified, two-band):
  composite <  40   INVALIDATE — write 2-3 sentence justification, move on
  composite >= 40   PIVOT      — high overlap that survives contextual weighting;
                                  constants align, structural similarity is genuine,
                                  redraft via Reference/Similarity_Pivot.md

The 40 threshold matches the platform similarity ceiling. The COMPOSITE has
already discounted contextual differentiators — a sub-40 composite means the
linter complaint is invalidatable (either lexical overlap is genuinely low,
OR constants differ enough that the prompts are structurally different
despite lexical overlap).

Output:
  - stdout: top-10 most-similar with per-dimension breakdown
  - <task_dir>/_aux/Similarity_Report.json
  - Exit 0 if max_composite < 40, exit 1 otherwise
  - --explain mode prints per-dimension breakdown vs ONE specific prior task
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TASKS_DIR = ROOT / "Tasks"
QC_V3_DIR = ROOT / "QC_Tasks" / "V3_Tasks"

# Lexical-score weights (sum to 1.0 — applied to raw lexical components)
W_BIGRAM = 0.40
W_UNIGRAM = 0.40
W_WORDCOUNT = 0.20

# Context multipliers (applied to raw_lexical when constants DIFFER).
# Multiplicative model — context dominates word stats.
MULT_BF_DIFFERS = 0.6
MULT_PERSONA_DIFFERS = 0.6
MULT_UNIVERSE_DIFFERS = 0.7


def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    return [t for t in text.split() if t]


def bigrams(tokens):
    return set(zip(tokens, tokens[1:]))


def unigrams(tokens):
    return set(tokens)


def jaccard(a, b):
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return (inter / union * 100.0) if union else 0.0


def word_count_similarity(wc_a, wc_b):
    """Higher = more similar word counts. 100 = identical, 0 = one is twice/half the other."""
    if wc_a == 0 or wc_b == 0:
        return 0.0
    return (min(wc_a, wc_b) / max(wc_a, wc_b)) * 100.0


def normalize_text(text):
    """Lowercase, collapse whitespace, strip — for boolean constant match."""
    return re.sub(r"\s+", " ", text.lower().strip())


def read_optional(path):
    """Read file if it exists and is non-empty; return None otherwise."""
    if not path.is_file() or path.stat().st_size == 0:
        return None
    try:
        text = path.read_text(encoding="utf-8").strip()
        return text if text else None
    except UnicodeDecodeError:
        return None


def resolve_task_dir(arg_path):
    """Accept absolute path, CWD-relative path, or ROOT-relative path."""
    p = Path(arg_path)
    if p.is_dir():
        return p.resolve()
    p2 = (ROOT / arg_path).resolve()
    if p2.is_dir():
        return p2
    return p.resolve()  # fall through; caller checks existence


def gather_corpus(self_path):
    """Returns list of dicts: path, task_dir, prompt_text, business_function, persona, universe_hash."""
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
            task_dir = p.parent
            out.append({
                "path": str(p.relative_to(ROOT)),
                "task_dir": str(task_dir.relative_to(ROOT)),
                "prompt_text": text,
                "business_function": read_optional(task_dir / "1_Business_Function.txt"),
                "persona": read_optional(task_dir / "2_Persona.txt"),
                "universe_hash": read_optional(task_dir / "_aux" / "data_hash.txt"),
            })
    return out


def score_pair(self_data, other):
    other_tokens = tokenize(other["prompt_text"])
    other_bg = bigrams(other_tokens)
    other_ug = unigrams(other_tokens)
    other_wc = len(other_tokens)

    bigram_score = jaccard(self_data["bigrams"], other_bg)
    unigram_score = jaccard(self_data["unigrams"], other_ug)
    wordcount_score = word_count_similarity(self_data["word_count"], other_wc)

    raw_lexical = (
        W_BIGRAM * bigram_score
        + W_UNIGRAM * unigram_score
        + W_WORDCOUNT * wordcount_score
    )

    bf_match = persona_match = universe_match = None
    differentiating = []
    multiplier = 1.0

    if self_data["business_function"] and other["business_function"]:
        bf_match = normalize_text(self_data["business_function"]) == normalize_text(other["business_function"])
        if not bf_match:
            multiplier *= MULT_BF_DIFFERS
            differentiating.append("business function")

    if self_data["persona"] and other["persona"]:
        persona_match = normalize_text(self_data["persona"]) == normalize_text(other["persona"])
        if not persona_match:
            multiplier *= MULT_PERSONA_DIFFERS
            differentiating.append("persona")

    if self_data["universe_hash"] and other["universe_hash"]:
        universe_match = self_data["universe_hash"] == other["universe_hash"]
        if not universe_match:
            multiplier *= MULT_UNIVERSE_DIFFERS
            differentiating.append("universe")

    composite = raw_lexical * multiplier
    recommendation = "PIVOT" if composite >= 40 else "INVALIDATE"

    return {
        "path": other["path"],
        "task_dir": other["task_dir"],
        "raw_lexical": round(raw_lexical, 1),
        "dimensions": {
            "lexical_bigram": round(bigram_score, 1),
            "token_unigram": round(unigram_score, 1),
            "word_count_similarity": round(wordcount_score, 1),
            "business_function_match": bf_match,
            "persona_match": persona_match,
            "universe_hash_match": universe_match,
        },
        "context_multiplier": round(multiplier, 3),
        "composite": round(composite, 1),
        "differentiating": differentiating,
        "recommendation": recommendation,
    }


def fmt_match(m):
    if m is True:
        return "MATCH   (constants align — no reduction)"
    if m is False:
        return "DIFFERS (strong differentiator — multiplier applied)"
    return "UNKNOWN (one or both task dirs missing this file)"


def run_explain(self_data, self_path, task_dir, explain_arg):
    explain_dir = resolve_task_dir(explain_arg)
    if not explain_dir.is_dir():
        print(f"ERROR: {explain_arg} not a directory (tried {explain_dir})", file=sys.stderr)
        sys.exit(2)
    explain_prompt_path = None
    for candidate in (explain_dir / "5_Prompt.txt", explain_dir / "Prompt.txt"):
        if candidate.is_file():
            explain_prompt_path = candidate
            break
    if explain_prompt_path is None:
        print(f"ERROR: no 5_Prompt.txt or Prompt.txt under {explain_dir}", file=sys.stderr)
        sys.exit(2)
    try:
        explain_rel = str(explain_prompt_path.relative_to(ROOT))
        explain_dir_rel = str(explain_dir.relative_to(ROOT))
    except ValueError:
        explain_rel = str(explain_prompt_path)
        explain_dir_rel = str(explain_dir)

    other = {
        "path": explain_rel,
        "task_dir": explain_dir_rel,
        "prompt_text": explain_prompt_path.read_text(encoding="utf-8").strip(),
        "business_function": read_optional(explain_dir / "1_Business_Function.txt"),
        "persona": read_optional(explain_dir / "2_Persona.txt"),
        "universe_hash": read_optional(explain_dir / "_aux" / "data_hash.txt"),
    }
    result = score_pair(self_data, other)

    print(f"=== EXPLAIN: {task_dir.name} vs {explain_dir.name} ===")
    print()
    print(f"This prompt:       {str(self_path.relative_to(ROOT))}")
    print(f"Compared against:  {other['path']}")
    print()
    print(f"Per-dimension breakdown:")
    d = result["dimensions"]
    print(f"  lexical_bigram        {d['lexical_bigram']:>5.1f}   (word-bigram Jaccard)")
    print(f"  token_unigram         {d['token_unigram']:>5.1f}   (word-unigram Jaccard)")
    print(f"  word_count_similarity {d['word_count_similarity']:>5.1f}   (closer word counts = higher)")
    print(f"  business_function     {fmt_match(d['business_function_match'])}")
    print(f"  persona               {fmt_match(d['persona_match'])}")
    print(f"  universe_hash         {fmt_match(d['universe_hash_match'])}")
    print()
    print(f"Raw lexical (weighted):  {result['raw_lexical']:.1f}")
    print(f"Context multiplier:      ×{result['context_multiplier']}")
    if result["differentiating"]:
        print(f"Differentiating:         {', '.join(result['differentiating'])}")
    else:
        print(f"Differentiating:         (none — all known constants match)")
    print(f"COMPOSITE:               {result['composite']:.1f}")
    print()
    print(f"Recommendation: {result['recommendation']}")
    if result["recommendation"] == "INVALIDATE":
        if result["differentiating"]:
            print()
            print(f"Justification angle for Class B invalidation:")
            print(f"  cite the differing {' + '.join(result['differentiating'])} per the template in")
            print(f"  Reference/Linter_Playbook.md.")
        else:
            print()
            print(f"Composite < 40 from lexical overlap alone — invalidation is defensible")
            print(f"  on lexical grounds. Cite the substantive difference in framing or scenario.")
    else:
        print()
        print(f"Pivot is required — composite >= 40 even after contextual weighting.")
        print(f"  See Reference/Similarity_Pivot.md for the 6-lever pivot menu.")
    sys.exit(0 if result["composite"] < 40 else 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task_dir")
    ap.add_argument(
        "--explain",
        dest="explain_path",
        default=None,
        help="Print per-dimension breakdown vs a specific prior task dir",
    )
    args = ap.parse_args()

    task_dir = resolve_task_dir(args.task_dir)
    if not task_dir.is_dir():
        print(f"ERROR: {args.task_dir} not a directory", file=sys.stderr)
        sys.exit(2)
    self_path = task_dir / "5_Prompt.txt"
    if not self_path.is_file():
        print(f"ERROR: {self_path} not found", file=sys.stderr)
        sys.exit(2)
    self_text = self_path.read_text(encoding="utf-8").strip()
    if not self_text:
        print(f"ERROR: {self_path} is empty", file=sys.stderr)
        sys.exit(2)

    self_tokens = tokenize(self_text)
    self_data = {
        "bigrams": bigrams(self_tokens),
        "unigrams": unigrams(self_tokens),
        "word_count": len(self_tokens),
        "business_function": read_optional(task_dir / "1_Business_Function.txt"),
        "persona": read_optional(task_dir / "2_Persona.txt"),
        "universe_hash": read_optional(task_dir / "_aux" / "data_hash.txt"),
    }

    if args.explain_path:
        run_explain(self_data, self_path, task_dir, args.explain_path)
        return  # never reached; run_explain calls sys.exit

    corpus = gather_corpus(self_path)
    scored = [score_pair(self_data, other) for other in corpus]
    scored.sort(key=lambda r: r["composite"], reverse=True)

    pivot_band = [r for r in scored if r["composite"] >= 40]
    max_composite = scored[0]["composite"] if scored else 0.0

    out = {
        "task": task_dir.name,
        "this_prompt": str(self_path.relative_to(ROOT)),
        "corpus_size": len(corpus),
        "scoring_method": "composite = raw_lexical * context_multiplier (context dominates word stats)",
        "weights": {
            "lexical_bigram": W_BIGRAM,
            "token_unigram": W_UNIGRAM,
            "word_count_similarity": W_WORDCOUNT,
        },
        "multipliers_when_differs": {
            "business_function": MULT_BF_DIFFERS,
            "persona": MULT_PERSONA_DIFFERS,
            "universe_hash": MULT_UNIVERSE_DIFFERS,
        },
        "bands": {
            "below_40": "INVALIDATE — write 2-3 sentence justification, move on",
            "at_or_above_40": "PIVOT — high overlap that survives contextual weighting",
        },
        "top10": scored[:10],
        "pivot_band": pivot_band,
        "max_composite": max_composite,
        "max_score": max_composite,  # back-compat alias for older runbook references
    }

    out_path = task_dir / "_aux" / "Similarity_Report.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")

    print(f"=== Similarity report: {task_dir.name} ===")
    print(f"Self:            {out['this_prompt']}")
    print(f"Corpus size:     {len(corpus)} other prompts")
    print(f"Max composite:   {max_composite}")
    print()
    print(f"Top 10 most similar (by composite):")
    print(f"  {'composite':>9} {'raw_lex':>7} {'mult':>6}  recommendation  path")
    for r in scored[:10]:
        print(
            f"  {r['composite']:>9.1f} {r['raw_lexical']:>7.1f} {r['context_multiplier']:>6.3f}  "
            f"{r['recommendation']:<12}    {r['path']}"
        )
    print()
    print(f"Written:         {out_path}")
    print()
    print(f"For per-dimension breakdown vs a specific task:")
    print(f"  python Validators/calc_similarity.py {args.task_dir} --explain <prior_task_dir>")

    if pivot_band:
        print(f"\n[!] {len(pivot_band)} prompt(s) at >= 40 composite — PIVOT required.")
        print(f"    Composite is high even after context multiplier reduction,")
        print(f"    meaning constants align with a prior task. See Reference/Similarity_Pivot.md.")
        sys.exit(1)
    print(f"\n[OK] all similarity composites < 40 — clear of the ceiling")
    print(f"     If platform linter flags one, INVALIDATE with justification (Class B template).")
    sys.exit(0)


if __name__ == "__main__":
    main()
