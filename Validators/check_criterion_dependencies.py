#!/usr/bin/env python3
"""
Usage:
    python Validators/check_criterion_dependencies.py <task_dir>

Finds criteria that PASS for the wrong reason.

Why this exists
---------------
S4's trajectory walk is fail-driven: the runbook says "for EVERY failing rubric,
walk the trajectory". Nothing ever inspects a *passing* cell, so a criterion that
is graded Pass on an artifact its own subject presupposes is structurally
invisible to the phase.

Task 44 shipped exactly that defect through S3, AUDIT, FINAL and four S4 passes:
the West-cluster owner criterion passed 6/6 on Gemini while the criterion that
requires the West coverage item to exist at all passed only 2/6. In four runs the
owner credit was banked on a comment written to a pre-existing record, which
diluted the lever the pair was built to carry. It was caught by an operator
reading the matrix by eye, not by any gate.

What it does
------------
1. Builds the criterion x run decision grid from the verifier export(s).
2. Infers dependency edges between criteria from their own text: a criterion whose
   subject is "the <X>" that another criterion is responsible for *raising* or
   *creating* depends on that one.
3. Reports every cell where a dependent criterion passed in a run where its
   antecedent failed. Those gradings are not merely generous, they are
   inconsistent: the artifact the dependent grades on did not exist.

Exit 0 when no inconsistent cell is found, 1 otherwise. Advisory by design:
a hit means "go look at this pair", not "the rubric is broken".
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# A criterion that CREATES a tracked artifact. Group 1 is the artifact noun phrase.
CREATOR = re.compile(
    r"\bThe Agent\s+(?:raises|creates|opens|files|schedules|posts|drafts|leaves)\b"
    r"(?:\s+a|\s+an|\s+new|\s+tracking)*\s+(.{6,90}?)(?:\s+(?:for|on|in|covering|to|that|which|whose)\b|[.,]|$)",
    re.IGNORECASE)

# A criterion whose subject is a possessed artifact: "The Agent's <artifact> states/names/covers ..."
DEPENDENT = re.compile(
    r"\bThe Agent's\s+(.{4,80}?)\s+(?:states|names|covers|records|describes|identifies|reads|carries)\b",
    re.IGNORECASE)

STOP = {
    "the", "a", "an", "new", "agent", "agents", "that", "this", "work", "item",
    "items", "tracking", "of", "for", "on", "in", "to", "and", "or", "its",
}


def toks(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 2}


def load_criteria(task: Path):
    data = json.loads((task / "7_Rubrics.json").read_text(encoding="utf-8"))
    crits = data if isinstance(data, list) else (data.get("rubrics") or data.get("criteria"))
    return [(i + 1, c.get("title") or "", c.get("evidence") or "") for i, c in enumerate(crits)]


def norm_title(s):
    s = re.sub(r"\[([^\]]+)\]\(mailto:[^)]+\)", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = s.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip().rstrip(".").lower()


def parse_export(path: Path):
    """Return {run_no: {normalised_title: 'Pass'|'Fail'}}."""
    runs, cur = {}, None
    for raw in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^Run\s*#?(\d+)\s*$", raw.strip())
        if m:
            cur = int(m.group(1))
            runs[cur] = {}
            continue
        if "\t" not in raw or cur is None:
            continue
        parts = raw.split("\t")
        if len(parts) < 2 or parts[1].strip() not in ("Pass", "Fail"):
            continue
        runs[cur][norm_title(parts[0])] = parts[1].strip()
    return runs


def discover_exports(task: Path):
    out = []
    for name in ("8a_Verifier_Fails_Opus.txt", "8b_Verifier_Fails_Gemini.txt",
                 "8_Verifier_Fails.txt"):
        p = task / name
        if p.is_file() and p.stat().st_size > 0:
            label = "opus" if "Opus" in name else ("gemini" if "Gemini" in name else "model")
            out.append((label, p))
    return out


def infer_edges(criteria):
    """[(dependent_idx, antecedent_idx, overlap_score, artifact_phrase)]"""
    creators = []
    for idx, title, _ in criteria:
        m = CREATOR.search(title)
        if m:
            # Token bag is the WHOLE title, not just the captured noun phrase. The
            # phrase alone truncates at the first preposition ("raises a tracking item
            # ON the Operations board FOR the West cluster ... gap"), which strands the
            # discriminating words and made this checker miss the defect it was written
            # for. The full title carries them.
            creators.append((idx, toks(title), m.group(1).strip()))

    edges = []
    for idx, title, _ in criteria:
        m = DEPENDENT.search(title)
        if not m:
            continue
        subj = toks(m.group(1))
        if not subj:
            continue
        best = None
        for cidx, ctoks, cphrase in creators:
            if cidx == idx or not ctoks:
                continue
            shared = subj & ctoks
            # Require a real noun-phrase overlap, not one incidental word.
            if len(shared) >= 2 or (len(shared) == 1 and len(subj) == 1):
                # Rank on shared-token COUNT first so a dependent binds to the most
                # specific antecedent, then on coverage ratio as the tie-break.
                key = (len(shared), len(shared) / max(1, len(subj)))
                if best is None or key > best[1]:
                    best = (cidx, key, cphrase)
        if best:
            edges.append((idx, best[0], round(best[1][1], 2), m.group(1).strip()))
    return edges


def overly_broad_severity(task_dir) -> str:
    """Severity of an Overly Broad finding, for THIS universe.

    The ordering is not universal. StarPM adopted a 07/16 swap making Overly Specific
    Moderate and Overly Broad Minor; HarmonyGames ships the pre-swap ordering, the exact
    reverse. Overall Rubric Quality needs zero Major AND zero Moderate for a 5, so the
    direction decides whether one criterion costs the top score.
    """
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from universes import detect_universe, get_framework_profile
        smap = get_framework_profile(detect_universe(Path(task_dir))).get("severity_map", {})
        return smap.get("overly_broad", "moderate").upper()
    except Exception:
        return "MODERATE"


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    task = Path(sys.argv[1])
    if not task.is_absolute():
        task = ROOT / task
    if not (task / "7_Rubrics.json").is_file():
        print(f"[SKIP] {task}: no 7_Rubrics.json")
        return 0

    criteria = load_criteria(task)
    by_idx = {i: t for i, t, _ in criteria}
    exports = discover_exports(task)
    if not exports:
        print(f"[SKIP] {task.name}: no verifier export present yet")
        return 0

    edges = infer_edges(criteria)
    if not edges:
        print(f"[OK] {task.name}: no dependent criterion pairs inferred")
        return 0

    print(f"=== Criterion dependency audit: {task.name} ===")
    print(f"Inferred {len(edges)} dependent pair(s) from criterion text.\n")

    violations = []
    for label, path in exports:
        runs = parse_export(path)
        for dep, ante, score, phrase in edges:
            dtitle, atitle = norm_title(by_idx[dep]), norm_title(by_idx[ante])
            for run in sorted(runs):
                d = runs[run].get(dtitle)
                a = runs[run].get(atitle)
                if d == "Pass" and a == "Fail":
                    violations.append((label, run, dep, ante, phrase))

    for dep, ante, score, phrase in edges:
        print(f"  criterion {dep:>2} depends on {ante:>2}  (overlap {score})  subject: \"{phrase}\"")
    print()

    if not violations:
        print(f"[OK] {task.name}: no criterion passed in a run where its antecedent failed.")
        return 0

    grouped = defaultdict(list)
    for label, run, dep, ante, phrase in violations:
        grouped[(dep, ante)].append(f"{label} run {run}")

    print(f"[FAIL] {len(violations)} inconsistent cell(s) across {len(grouped)} pair(s):\n")
    for (dep, ante), where in sorted(grouped.items()):
        print(f"  criterion {dep} PASSED while criterion {ante} FAILED in: {', '.join(where)}")
        print(f"    {dep}: {by_idx[dep]}")
        print(f"    {ante}: {by_idx[ante]}")
        print(f"    -> criterion {dep} is graded on an artifact criterion {ante} says was never created.")
        print(f"       Bind {dep}'s subject to that artifact, or explain why it can stand alone.\n")
    _sev = overly_broad_severity(task_dir)
    print(f"This is the Overly Broad signal a fail-driven trajectory walk cannot see. "
          f"Severity for this universe: {_sev}.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
