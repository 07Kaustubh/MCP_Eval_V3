#!/usr/bin/env python3
"""
Usage:
    python Validators/check_oe_rubric_sync.py <task_dir>

Enforces AGENTS.md rule 14's mirroring clause: when a criterion is relaxed or cut,
the change must be mirrored into the Oracle Event that governs it, or the artifacts
drift.

Why this exists
---------------
Rule 14 states the requirement but nothing enforced it, and no phase compared the
two files. Every S4 / AUDIT pass diffs rubrics against earlier RUBRIC snapshots and
never opens `6_Oracle_Events.txt`.

On Task 44, criterion 5 was generalised from "OPS-186, dated June 17, 2026, records
the West Cluster work as still underway" to "the most recent dated status statement
on the West cluster ...". OE 29 kept demanding the identifier and the date, including
inside its own `S3 must decompose this into one criterion per content element (...)`
directive, for hours afterwards. The drift was found by an operator reading both
files side by side.

What it checks
--------------
1. Every content element named inside an OE's `S3 must decompose ... (per content
   element ...)` directive still has a plausible carrier criterion in the rubric set.
2. Record identifiers and explicit dates that an OE requires a deliverable to STATE
   are still present in the corresponding criterion's title or evidence. An OE that
   hard-codes `OPS-186 dated 2026-06-17` while no criterion mentions either token is
   the exact drift shape above.

Exit 0 clean, 1 on drift. Advisory: a hit means "these two files disagree about what
the criterion requires", which is sometimes intentional and always worth a look.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OE_SPLIT = re.compile(r"^OE\s+(\d+[a-z]?)\s*:", re.MULTILINE)
DECOMPOSE = re.compile(
    r"must decompose this into one criterion per content element\s*\((.+?)\)",
    re.IGNORECASE | re.DOTALL)
RECORD_ID = re.compile(r"\b(OPS-\d+|MT-\d{4}-\d+)\b")
ISO_DATE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")

STOP = {"the", "a", "an", "that", "this", "and", "or", "of", "for", "on", "in", "to",
        "is", "was", "были", "as", "still", "its", "it", "be", "been", "with", "by",
        "not", "no", "any", "all", "one", "two", "per", "must", "should", "agent",
        "criterion", "criteria", "content", "element", "decompose", "into", "plus",
        "separate", "named", "owner", "never", "them", "enumerating"}


# OE prose that deliberately exempts a named record or fact from being graded.
NON_GRADED = re.compile(
    r"no criterion may|must not be|neither required nor credited|not part of the expected path"
    r"|is corroboration|as corroboration|bound against overclaiming|carries no criterion"
    r"|must be neither|no deliverable may|is not part of|not itself a graded"
    r"|no criterion is built|usable only as|accuracy note|grading note"
    r"|is not required|are not required|not required to|naming the record identifier",
    re.IGNORECASE)

MONTHS = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")


def token_present(tok, blob):
    """True when the criterion set carries this token in any conventional rendering."""
    if tok.lower() in blob:
        return True
    m = re.fullmatch(r"(20\d{2})-(\d{2})-(\d{2})", tok)
    if not m:
        return False
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if not 1 <= mo <= 12:
        return False
    name = MONTHS[mo - 1]
    # "May 23, 2026" / "May 23 2026" / "23 May 2026" / "5/23"
    for variant in (f"{name.lower()} {d}, {y}", f"{name.lower()} {d} {y}",
                    f"{d} {name.lower()} {y}", f"{mo}/{d}", f"{mo:02d}/{d:02d}"):
        if variant in blob:
            return True
    return False


def _stem(w):
    """Crude suffix trim so escalation/escalated and statement/states collide."""
    for suf in ("ations", "ation", "ements", "ement", "ing", "ions", "ion",
                "ed", "es", "s"):
        if len(w) - len(suf) >= 4 and w.endswith(suf):
            w = w[: -len(suf)]
            break
    # Second pass: "escalation"->"escal" but "escalated"->"escalat", so collapse a
    # trailing verbal "at" to make the two forms collide. Guarded on length so short
    # real stems ("stat", "chat") survive.
    if len(w) >= 7 and w.endswith("at"):
        w = w[:-2]
    return w


def toks(s):
    return {_stem(w) for w in re.findall(r"[a-z0-9]+", s.lower())
            if w not in STOP and len(w) > 3}


def load_criteria(task: Path):
    data = json.loads((task / "7_Rubrics.json").read_text(encoding="utf-8"))
    crits = data if isinstance(data, list) else (data.get("rubrics") or data.get("criteria"))
    return [{"idx": i + 1,
             "title": c.get("title") or "",
             "evidence": c.get("evidence") or "",
             "blob": f"{c.get('title') or ''} {c.get('evidence') or ''}"}
            for i, c in enumerate(crits)]


def split_oes(text):
    marks = [(m.start(), m.group(1)) for m in OE_SPLIT.finditer(text)]
    out = []
    for i, (pos, num) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        out.append((num, text[pos:end]))
    return out


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    task = Path(sys.argv[1])
    if not task.is_absolute():
        task = ROOT / task
    oe_path, rub_path = task / "6_Oracle_Events.txt", task / "7_Rubrics.json"
    if not oe_path.is_file() or not rub_path.is_file():
        print(f"[SKIP] {task.name}: needs both 6_Oracle_Events.txt and 7_Rubrics.json")
        return 0

    criteria = load_criteria(task)
    all_blob = " ".join(c["blob"] for c in criteria).lower()
    oes = split_oes(oe_path.read_text(encoding="utf-8"))
    if not oes:
        print(f"[SKIP] {task.name}: no 'OE n:' blocks parsed")
        return 0

    findings = []

    for num, body in oes:
        # ---- 1. decompose directives: does each named content element have a carrier?
        for dm in DECOMPOSE.finditer(body):
            inner = dm.group(1)
            elements = [e.strip() for e in re.split(r",\s*and\s+|,\s+(?=[a-z])|\s+and\s+(?=that\b)", inner)
                        if len(e.strip()) > 12]
            for el in elements:
                et = toks(el)
                if len(et) < 2:
                    continue
                best = max((len(et & toks(c["blob"])) / len(et), c["idx"]) for c in criteria)
                if best[0] < 0.5:
                    findings.append(("orphaned decompose element", num, el[:120],
                                     f"best carrier is criterion {best[1]} at "
                                     f"{best[0]:.0%} token coverage"))

        # ---- 2. hard-coded identifiers / dates the OE requires a deliverable to state
        if re.search(r"\b(?:description|body|message|draft|final response|item|note)\b", body, re.I):
            for tok in set(RECORD_ID.findall(body)) | set(ISO_DATE.findall(body)):
                if token_present(tok, all_blob):
                    continue
                # Only flag where the OE presents it as required statement content AND
                # does not explicitly exempt it from grading. OE bodies routinely name
                # records as investigation context or as deliberate non-graded bounds
                # ("no criterion may be built on what it asserts"), and treating those
                # as drift buries the real signal.
                flagged = False
                for m in re.finditer(re.escape(tok), body):
                    before = body[max(0, m.start() - 200):m.start()]
                    window = body[max(0, m.start() - 400):m.start() + 400]
                    requires = re.search(
                        r"\b(?:covering|states?|stating|carry|carries|record(?:s|ing)?|naming|names)\b"
                        r"[^.]{0,180}$", before, re.I)
                    if requires and not NON_GRADED.search(window):
                        flagged = True
                        break
                if flagged:
                    findings.append(("OE requires a token no criterion carries", num, tok,
                                     "OE asks a deliverable to state this, but it appears in "
                                     "no criterion title or evidence"))

    print(f"=== OE / rubric sync: {task.name} ===")
    print(f"{len(oes)} oracle event(s), {len(criteria)} criteria\n")

    if not findings:
        print(f"[OK] {task.name}: OEs and rubrics agree on required content.")
        return 0

    seen, uniq = set(), []
    for f in findings:
        k = (f[0], f[1], f[2])
        if k not in seen:
            seen.add(k)
            uniq.append(f)

    hard = [f for f in uniq if f[0] == "orphaned decompose element"]
    soft = [f for f in uniq if f[0] != "orphaned decompose element"]

    if hard:
        print(f"[FAIL] {len(hard)} orphaned decompose element(s):\n")
        for kind, num, item, detail in hard:
            print(f"  OE {num}")
            print(f"    element: {item}")
            print(f"    {detail}\n")
        print("Mirror the relaxation into the OE, or restore the element in the rubric set.")
        print("AGENTS.md rule 14: a cut that removes a content element named in an OE's")
        print("decompose directive must be mirrored into that OE in the same pass.")
    else:
        print(f"[OK] {task.name}: every decompose element has a carrier criterion.")

    if soft:
        print(f"\n[INFO] {len(soft)} identifier/date observation(s), advisory only.")
        print("       An OE names these as statement content while no criterion carries")
        print("       them. Often intentional (context, non-graded bounds). Skim, do not")
        print("       treat as failures.")
        for kind, num, item, detail in soft:
            print(f"         OE {num}: {item}")

    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
