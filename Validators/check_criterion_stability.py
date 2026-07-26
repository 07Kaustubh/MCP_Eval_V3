#!/usr/bin/env python3
"""
Usage:
    python Validators/check_criterion_stability.py <task_dir>

Measures grader agreement across repeated gradings of the SAME trajectories, using Cohen's
kappa rather than raw percentage agreement, and names the criteria whose grading is a
coin flip.

Why this exists
---------------
Task 44 produced three independent gradings of twelve byte-identical trajectories. The
pipeline reported the instability as "8.5% and 8.6% of cells moved", which is raw agreement
and overstates reliability: on a set where most cells are Fail, two graders agree on ~90% of
cells purely by chance. The LLM-as-judge literature is explicit that kappa, which corrects
for chance agreement, is the right statistic, with the conventional reading that kappa above
0.6 is acceptable and above 0.8 is strong. Published work on rubric grading finds overall
kappa around 0.37 to 0.42, and crucially finds that agreement is high for objective criteria
(around 0.57 to 0.63) and poor for subjective ones (below 0.35).

That last point is the actionable one: per-criterion agreement identifies which criteria are
subjectively worded. Those are the ones to reword, and they are exactly the criteria that
produce false fails in the deliverable that must never be wrong.

Inputs
------
Every archived export under `_aux/Verifier_Exports/` (written by
`check_export_freshness.py --pin`) plus the current exports. At least two gradings of the
same model are needed; with one grading the tool reports what it has and exits 0.

Output
------
Overall Cohen's kappa per model, with the interpretation band, plus a per-criterion
disagreement list ordered worst-first. A criterion that flips on 2+ cells across gradings
of identical trajectories is a rewording candidate regardless of which grading was right.

Advisory: exits 0. This is a diagnostic for rubric wording, not a task gate.
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def norm_title(s):
    s = re.sub(r"\[([^\]]+)\]\(mailto:[^)]+\)", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = s.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip().rstrip(".").lower()


def parse_export(path: Path):
    runs, cur = {}, None
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"^Run\s*#?(\d+)\s*$", raw.strip())
        if m:
            cur = int(m.group(1)); runs[cur] = {}; continue
        if "\t" not in raw or cur is None:
            continue
        p = raw.split("\t")
        if len(p) < 2 or p[1].strip() not in ("Pass", "Fail"):
            continue
        runs[cur][norm_title(p[0])] = p[1].strip()
    return runs


def cohen_kappa(pairs):
    """pairs: list of (a, b) categorical labels from two gradings of the same cell."""
    n = len(pairs)
    if not n:
        return None
    agree = sum(1 for a, b in pairs if a == b) / n
    cats = {c for p in pairs for c in p}
    pe = 0.0
    for c in cats:
        pa = sum(1 for a, _ in pairs if a == c) / n
        pb = sum(1 for _, b in pairs if b == c) / n
        pe += pa * pb
    if pe >= 1.0:
        return 1.0 if agree == 1.0 else 0.0
    return (agree - pe) / (1 - pe)


def band(k):
    if k is None:
        return "n/a"
    if k < 0:      return "worse than chance"
    if k <= 0.20:  return "slight"
    if k <= 0.40:  return "fair"
    if k <= 0.60:  return "moderate"
    if k <= 0.80:  return "substantial (acceptable)"
    return "almost perfect (strong)"


def model_of(name):
    return "opus" if "Opus" in name else ("gemini" if "Gemini" in name else "model")


def main():
    if len(sys.argv) != 2:
        print(__doc__); return 2
    task = Path(sys.argv[1])
    if not task.is_absolute():
        task = ROOT / task

    # gather gradings per model: archived + current
    gradings = defaultdict(list)   # model -> [(label, grid)]
    arch = task / "_aux" / "Verifier_Exports"
    if arch.is_dir():
        for p in sorted(arch.glob("*.txt")):
            gradings[model_of(p.name)].append((p.name, parse_export(p)))
    for n in ("8a_Verifier_Fails_Opus.txt", "8b_Verifier_Fails_Gemini.txt", "8_Verifier_Fails.txt"):
        p = task / n
        if p.is_file() and p.stat().st_size:
            g = parse_export(p)
            m = model_of(n)
            if not any(existing == g for _, existing in gradings[m]):
                gradings[m].append((f"{n} (current)", g))

    if not gradings:
        print(f"[SKIP] {task.name}: no verifier exports found"); return 0

    print(f"=== Criterion stability: {task.name} ===")
    print("Cohen's kappa on repeated gradings of identical trajectories. Raw percentage")
    print("agreement overstates reliability on an imbalanced grid; kappa corrects for chance.")
    print("Conventional reading: >0.60 acceptable, >0.80 strong.\n")

    flips = defaultdict(int)
    any_pair = False
    for m, gs in sorted(gradings.items()):
        print(f"--- {m}: {len(gs)} grading(s) on disk")
        for label, _ in gs:
            print(f"      {label}")
        if len(gs) < 2:
            print(f"      only one grading archived, so agreement is not computable yet.")
            print(f"      Re-pin after each platform re-export to build the series:")
            print(f"        python Validators/check_export_freshness.py {task} --pin\n")
            continue
        any_pair = True
        # compare each consecutive pair
        for (l1, g1), (l2, g2) in zip(gs, gs[1:]):
            pairs = []
            for run in sorted(set(g1) & set(g2)):
                for t in set(g1[run]) & set(g2[run]):
                    a, b = g1[run][t], g2[run][t]
                    pairs.append((a, b))
                    if a != b:
                        flips[t] += 1
            k = cohen_kappa(pairs)
            raw = sum(1 for a, b in pairs if a == b) / len(pairs) if pairs else 0
            print(f"      {l1[:34]} vs {l2[:34]}")
            print(f"        cells={len(pairs)}  raw agreement={raw:.1%}  "
                  f"kappa={k:.3f} ({band(k)})")
        print()

    if not any_pair:
        return 0

    if flips:
        rub = task / "7_Rubrics.json"
        idx = {}
        if rub.is_file():
            crits = json.loads(rub.read_text(encoding="utf-8"))
            crits = crits if isinstance(crits, list) else (crits.get("rubrics") or crits.get("criteria"))
            idx = {norm_title(c.get("title") or ""): i + 1 for i, c in enumerate(crits)}
        print("Criteria whose grading moved on identical trajectories, worst first.")
        print("2+ flips means the wording, not the agent, is deciding the cell.\n")
        for t, n in sorted(flips.items(), key=lambda kv: -kv[1]):
            if n < 2:
                continue
            print(f"  {n} flip(s)  criterion {idx.get(t, '?')}: {t[:88]}")
        print()
        print("Reword these before appealing any cell on them. A criterion that flips under")
        print("re-grading will keep flipping, and an appeal cannot fix wording.")
    else:
        print("[OK] no cell changed between gradings.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
