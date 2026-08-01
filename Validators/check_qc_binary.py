#!/usr/bin/env python3
"""
Usage:
    python Validators/check_qc_binary.py <task_dir>

One gate for the ten BINARY QC sub-dimensions: the ones with no 3/4 band, where a single
defect is a FAIL with no partial credit.

Why this exists
---------------
`Docs*/7_QC_Spec_Doc1.json` defines 24 sub-dimensions across 5 dimensions. Ten of them
carry "NA" in the Non-Fail (3/4 Rating) column, which means they are pass-or-fail. Those
ten are where a task dies, and they were the ones most likely to be adjudicated in council
prose rather than measured.

This consolidates them into a single deterministic report with the spec citation for each,
so a council does not have to re-derive the standard, and so the sub-dimensions that
genuinely need human judgement are named explicitly instead of being assumed covered.

The ten binary sub-dimensions
-----------------------------
Prompt      Tool use and Cross-service requirement   deterministic
Prompt      Investigation                            deterministic (pre-solving patterns)
Prompt      Coherence                                deterministic (bolt-on test below)
Prompt      Alignment with Today's Date              deterministic
Universe    Universe Feasibility (Data Exists)       deterministic (delegated)
Universe    Cross-service Coherence                  HUMAN, conditional on agent failure
Rubric      Rubric Category Balance                  deterministic
Trajectory  Tool Call Count                          deterministic (delegated)
Trajectory  Agent Failure Rate                       deterministic (delegated)
Trajectory  Error Rate                               deterministic (delegated)

The bolt-on test is the spec's own
----------------------------------
QC spec, Prompt / Coherence, Fail condition: "Contains unrelated bolt-on requests;
removing a sentence doesn't change the rest." That is an operational test, so it is
implemented rather than left to judgement: for each sentence, measure how much of its
content vocabulary is shared with the rest of the prompt. A sentence that shares almost
nothing is a bolt-on candidate. Reported as a candidate, not a verdict, because a
legitimately cohesive sentence can still introduce new vocabulary.

Exit 0 when no binary sub-dimension fails, 1 otherwise.
"""

import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = "Docs*/7_QC_Spec_Doc1.json"

STOP = set("""a an the and or but if then so that this these those it its it's is are was were be been
being to of in on at for with from by as not no any all one two some more most other into than
i me my we our you your they them their he she his her need needs needed get gets got make makes
made put puts do does did have has had can could should would will just now today yesterday
tomorrow every each both here there what which who whom whose when where why how""".split())


def toks(s):
    return {w for w in re.findall(r"[a-z][a-z'-]{2,}", s.lower()) if w not in STOP}


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n{2,}", text)
    return [p.strip() for p in parts if len(p.strip()) > 25]


def universe_today(task: Path):
    for rel in ("_aux/Universe_Index/today_horizon.json",):
        p = task / rel
        if p.is_file():
            try:
                d = json.loads(p.read_text())
                for k in ("today", "universe_today", "date"):
                    if k in d:
                        m = re.search(r"(\d{4})-(\d{2})-(\d{2})", str(d[k]))
                        if m:
                            return date(*map(int, m.groups()))
            except Exception:
                pass
    return None


def run(script, *args):
    try:
        r = subprocess.run([sys.executable, str(ROOT / "Validators" / script), *map(str, args)],
                           capture_output=True, text=True, timeout=300)
        return r.returncode, r.stdout
    except Exception as e:
        return None, str(e)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    task = Path(sys.argv[1])
    if not task.is_absolute():
        task = ROOT / task
    prompt_p = task / "5_Prompt.txt"
    if not prompt_p.is_file():
        print(f"[SKIP] {task.name}: no 5_Prompt.txt")
        return 0
    prompt = prompt_p.read_text(encoding="utf-8")

    results = []   # (dimension, sub-dim, verdict, detail)

    def add(dim, sub, ok, detail):
        results.append((dim, sub, ok, detail))

    # ---- Prompt / Coherence : the spec's own bolt-on test
    # A bolt-on introduces NEW SUBJECT MATTER unconnected to the rest ("Check weather in
    # Miami, update my calendar, email Marcus about Q3, look up Seattle flights" - each
    # names its own subject). Low vocabulary overlap alone is not the signal: an abstractly
    # phrased directive about HOW to write a deliverable ("If it is not, say straight out
    # that my earlier sign-off does not hold") shares little vocabulary while being entirely
    # load-bearing. A first cut flagged exactly that sentence on Task 44, which would have
    # told the author to delete the retraction beat the task is built around. So a candidate
    # must ALSO introduce a proper-noun subject that appears nowhere else in the prompt.
    sents = sentences(prompt)
    boltons = []
    if len(sents) >= 3:
        for i, s in enumerate(sents):
            mine = toks(s)
            others = [x for j, x in enumerate(sents) if j != i]
            rest = set().union(*[toks(x) for x in others]) if others else set()
            if not mine:
                continue
            shared = len(mine & rest) / len(mine)
            if shared >= 0.25:
                continue
            # proper nouns / service names introduced only here.
            # A word capitalised only because it OPENS its sentence is not a proper noun, and
            # neither is a month name. Both defeated this guard on Task 46, where 'Where',
            # 'Bring', 'Post' and 'July' were reported as newly introduced subjects on four
            # load-bearing sentences (two of them the imperative verbs of the deliverables).
            # Count a token as an introduced subject only when it is capitalised at a
            # NON-initial position; suppress on any capital seen anywhere else in the prompt.
            _MONTHS = {"January", "February", "March", "April", "May", "June", "July",
                       "August", "September", "October", "November", "December"}
            _fm = re.match(r"\s*([A-Za-z']+)", s)
            _first = _fm.group(1) if _fm else ""
            mine_caps = ({w for w in re.findall(r"\b[A-Z][a-z]{2,}\b", s)}
                         - {"If", "The", "This", "That"} - _MONTHS - {_first})
            rest_caps = {w for x in others for w in re.findall(r"\b[A-Z][a-z]{2,}\b", x)}
            novel = mine_caps - rest_caps
            if novel:
                boltons.append((round(shared, 2), sorted(novel)[:4], s[:110]))
    add("Prompt", "Coherence", not boltons,
        "no sentence is lexically isolated from the rest"
        if not boltons else
        "; ".join(f"{p:.0%} shared vocabulary and introduces {n} found nowhere else: \"{t}...\""
                  for p, n, t in boltons))

    # ---- Prompt / Alignment with Today's Date
    ut = universe_today(task)
    future = []
    if ut:
        for m in re.finditer(r"\b(20\d{2})-(\d{2})-(\d{2})\b", prompt):
            try:
                d = date(*map(int, m.groups()))
                if d > ut:
                    future.append(m.group(0))
            except ValueError:
                pass
        MON = ("january february march april may june july august september october "
               "november december").split()
        for m in re.finditer(r"\b(" + "|".join(MON) + r")\s+(\d{1,2})?,?\s*(20\d{2})\b", prompt, re.I):
            try:
                d = date(int(m.group(3)), MON.index(m.group(1).lower()) + 1, int(m.group(2) or 1))
                if d > ut:
                    future.append(m.group(0))
            except ValueError:
                pass
    add("Prompt", "Alignment with Today's Date", not future,
        f"universe today = {ut}; no prompt date is in the future" if ut and not future
        else (f"future-dated reference(s) vs universe today {ut}: {sorted(set(future))}" if future
              else "universe today not resolvable from _aux/Universe_Index/today_horizon.json"))

    # ---- Rubric / Category Balance  (QC spec 05/22, binary)
    rub = task / "7_Rubrics.json"
    if rub.is_file():
        crits = json.loads(rub.read_text())
        crits = crits if isinstance(crits, list) else (crits.get("rubrics") or crits.get("criteria"))
        out = sum(1 for c in crits if (c.get("category") or "").lower() == "outcome")
        pro = sum(1 for c in crits if (c.get("category") or "").lower() == "process")
        ok = out > 0 and out > pro and (pro / max(1, out + pro)) <= 0.5
        add("Rubric", "Rubric Category Balance", ok,
            f"outcome={out}, process={pro}. Spec Pass(5): outcome > process (05/22). "
            f"Fail: zero outcome, or >50% process")

    # ---- delegated deterministic gates
    rc, so = run("verify_universe_atoms.py", "--task", task)
    add("Universe", "Universe Feasibility (Data Exists)", rc == 0,
        (so.strip().splitlines() or ["no output"])[-1][:150])

    tstats = task / "_aux" / "Trajectory_Stats.json"
    if tstats.is_file():
        st = json.loads(tstats.read_text())
        bym = st.get("by_model") or {}
        if bym:
            dens = {m: v.get("avg_tool_calls_total") for m, v in bym.items()}
            p1 = {m: v.get("pass_at_1") for m, v in bym.items()}
            add("Trajectory", "Tool Call Count", all((d or 0) >= 40 for d in dens.values()),
                f"avg total per model: {dens} (V4 target 40+, QC fail floor 15)")
            add("Trajectory", "Agent Failure Rate", all((p or 0) <= 40 for p in p1.values()),
                f"pass@1 per model: {p1} (fail if > 40%)")
        errs = sum(1 for r in st.get("per_run", []) if r.get("status") != "ok")
        add("Trajectory", "Error Rate", errs <= 2,
            f"{errs} errored run(s) of {len(st.get('per_run', []))} (fail if >= 3)")

    # ---- Prompt / cross-service + Investigation are enforced inside validate.py
    rc, so = run("validate.py", "--task", task, "--phase", "prompt")
    vp = rc == 0 and "0 fails" in so
    add("Prompt", "Tool use and Cross-service requirement", vp,
        "delegated to validate.py --phase prompt (hard FAIL below 2 distinct services)")
    add("Prompt", "Investigation", vp,
        "delegated to validate.py --phase prompt (pre-solving anti-pattern check)")

    # ---- render
    print(f"=== Binary QC sub-dimensions: {task.name} ===")
    print(f"Authority: {SPEC}. Ten sub-dimensions carry NA in the 3/4 column, so each is")
    print("pass-or-fail with no partial credit.\n")
    print(f"{'DIM':<11}{'SUB-DIMENSION':<40}{'VERDICT'}")
    print("-" * 78)
    fails = 0
    for dim, sub, ok, detail in results:
        v = "PASS" if ok else "**FAIL**"
        if not ok:
            fails += 1
        print(f"{dim:<11}{sub:<40}{v}")
        print(f"{'':<11}  {detail}")
    print()
    print("HUMAN judgement required, not measurable here:")
    print("  Universe / Cross-service Coherence — spec makes it conditional on the")
    print("    contradiction CAUSING an agent failure, so it can only be judged against")
    print("    trajectories. Check that injected or base contradictions inside the active")
    print("    window did not break a run, and record the finding.")
    print()
    if fails:
        print(f"[FAIL] {fails} binary sub-dimension(s) failing. No partial credit exists on these.")
        return 1
    print(f"[OK] all {len(results)} measurable binary sub-dimension(s) pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
