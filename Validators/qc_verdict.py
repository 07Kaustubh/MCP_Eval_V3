#!/usr/bin/env python3
"""Deterministic QC verdict engine for V4 (StarPM-framework) tasks.

Commands:
  parse    <task_dir>   - structural parse of QC_Feedback_Verdict.txt + 9/10/11 trio -> JSON
  classify <task_dir>   - derive bucket from parsed CONTENT (scores + dispute decision)
  selftest <corpus_dir> - classify all labeled tasks, compare to bucket labels, 16/16 required
  audit    <task_dir>   - SSOT cross-reference: every finding's cited atoms checked against
                          the task's own universe data / prompt / OE / rubrics
  feedback <task_dir>   - draft a 9_QC_Feedback.txt skeleton from validator reports with
                          per-finding SSOT citations

Classification is CONTENT-ONLY (never directory names):
  qc_score 5                                  -> QC_Passed
  qc_score 3                                  -> QC_Non_Fails
  qc_score 2 + dispute approved (raised)      -> QC_False_Fails_PT_Dispute_Accepted
  qc_score 2 + no dispute or dispute rejected -> QC_True_Fails
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
MONEY_RE = re.compile(r"\$[\d,]+(?:\.\d{2})?")
ATOM_ID_RE = re.compile(
    r"\b(?:BL-[A-F0-9]{6,}|JE-[A-Za-z0-9-]{4,}|exc_[a-z0-9_]{4,}|doc_[a-f0-9]{8,}|"
    r"email_scen_[a-z0-9_]+|scenario_[a-f0-9]{6,}|FP-2026-\d{2}|C\d{3}|"
    r"rec[A-Z0-9][A-Za-z0-9]{4,}|MT-2026-\d{2,4}|OPS-\d{1,5}|INV-[A-Z0-9-]{3,}|"
    r"BILL-2026-\d{3,4}|msg_[a-z0-9_]{3,}|thr_[a-z0-9_]{3,}|cnt_[a-z0-9_]{3,}|deal_[a-z0-9_]{3,})\b"
)
CATEGORY_TAG_RE = re.compile(r"\[(Fail|Non-Fail)\s*-\s*([^\]]+)\]")
SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def _read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _sections(text: str) -> dict:
    """Split on '## Heading' markers; returns {heading: body}."""
    out = {}
    matches = list(SECTION_RE.finditer(text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[m.end():end].strip().strip("=").strip()
        out[m.group(1).strip()] = body
    return out


def _int_field(text: str, label: str):
    m = re.search(rf"^{re.escape(label)}:\s*(\d+)", text, re.MULTILINE)
    return int(m.group(1)) if m else None


def parse_verdict(task_dir: Path) -> dict:
    vp = task_dir / "QC_Feedback_Verdict.txt"
    text = _read(vp)
    if not text.strip():
        return {"error": f"missing or empty {vp}"}
    secs = _sections(text)
    error_cats = []
    ec_body = secs.get("Error Categories", "")
    m = re.search(r"\[.*\]", ec_body, re.DOTALL)
    if m:
        try:
            error_cats = json.loads(m.group(0))
        except json.JSONDecodeError:
            error_cats = re.findall(r'"([^"]+)"', ec_body)
    dispute = None
    for key in secs:
        if "Dispute" in key and "Response" not in key:
            body = secs[key]
            dv = re.search(r"^Verdict:\s*(\w+)", body, re.MULTILINE)
            ps = re.search(r"^Proposed Score:\s*(\d+)", body, re.MULTILINE)
            dispute = {
                "verdict": dv.group(1) if dv else None,
                "proposed_score": int(ps.group(1)) if ps else None,
                "feedback": body,
            }
    validation = None
    for key in secs:
        if "Validation" in key:
            body = secs[key]
            dec = re.search(r"^Decision:\s*(\w+)", body, re.MULTILINE)
            validation = {"decision": dec.group(1) if dec else None, "body": body}
    fv = None
    for key in secs:
        if key.startswith("Final Verdict"):
            m2 = re.search(r"Final Score:\s*(\d+)\s*[-\u2014]*\s*([A-Z -]+)?", secs[key])
            if m2:
                fv = {"final_score": int(m2.group(1)), "label": (m2.group(2) or "").strip()}
    findings = []
    fb = secs.get("QC Auditor Feedback", "")
    for m3 in CATEGORY_TAG_RE.finditer(fb):
        findings.append({"severity": m3.group(1), "tag": m3.group(2).strip()})
    return {
        "task": re.search(r"^Task:\s*(.+)$", text, re.MULTILINE).group(1).strip() if re.search(r"^Task:\s*(.+)$", text, re.MULTILINE) else task_dir.name,
        "business_function": (re.search(r"^Business Function:\s*(.+)$", text, re.MULTILINE) or [None]) and (re.search(r"^Business Function:\s*(.+)$", text, re.MULTILINE).group(1).strip() if re.search(r"^Business Function:\s*(.+)$", text, re.MULTILINE) else None),
        "qc_score": _int_field(text, "QC Score"),
        "final_score": _int_field(text, "Final Score"),
        "auditor_feedback": fb,
        "findings": findings,
        "error_categories": error_cats,
        "dispute": dispute,
        "validation": validation,
        "final_verdict": fv,
        "trio": {
            "9_QC_Feedback": (task_dir / "9_QC_Feedback.txt").is_file(),
            "10_PT_Dispute": (task_dir / "10_PT_Dispute_To_QC_Feedback.txt").is_file(),
            "11_Final_QC_Validation": (task_dir / "11_Final_QC_Validation_On_PT_Dispute.txt").is_file(),
        },
    }


def classify(parsed: dict) -> str:
    qc = parsed.get("qc_score")
    final = parsed.get("final_score")
    dispute = parsed.get("dispute")
    validation = parsed.get("validation") or {}
    decision = (validation.get("decision") or "").lower()
    if qc == 5:
        return "QC_Passed"
    if qc == 3:
        return "QC_Non_Fails"
    if qc == 2:
        approved = decision.startswith("approve") or (final is not None and final > 2)
        if dispute is not None and approved:
            return "QC_False_Fails_PT_Dispute_Accepted"
        return "QC_True_Fails"
    if qc == 4:
        return "QC_Non_Fails"
    return "UNKNOWN"


def selftest(corpus: Path) -> int:
    rows, correct, total = [], 0, 0
    for bucket_dir in sorted(corpus.iterdir()):
        if not bucket_dir.is_dir() or not bucket_dir.name.startswith("QC_"):
            continue
        for task_dir in sorted(bucket_dir.iterdir()):
            if not task_dir.is_dir():
                continue
            if not (task_dir / "QC_Feedback_Verdict.txt").is_file():
                continue
            total += 1
            parsed = parse_verdict(task_dir)
            got = classify(parsed)
            ok = got == bucket_dir.name
            correct += ok
            rows.append((task_dir.name, bucket_dir.name, got,
                         parsed.get("qc_score"), parsed.get("final_score"),
                         (parsed.get("validation") or {}).get("decision"), "OK" if ok else "MISS"))
    w = max(len(r[0]) for r in rows) if rows else 10
    print(f"{'task':<{w}}  {'label':<38} {'classified':<38} qc fin decision  result")
    for r in rows:
        print(f"{r[0]:<{w}}  {r[1]:<38} {r[2]:<38} {str(r[3]):<2} {str(r[4]):<3} {str(r[5]):<9} {r[6]}")
    print()
    print(f"QC VERDICT SELFTEST: {correct}/{total} bucket-correct")
    return 0 if correct == total and total > 0 else 1


def audit(task_dir: Path) -> int:
    parsed = parse_verdict(task_dir)
    if "error" in parsed:
        print(parsed["error"])
        return 2
    ssot_text = "\n".join(_read(task_dir / f) for f in (
        "3_UniverseDataForThisTask.json", "5_Prompt.txt", "6_Oracle_Events.txt",
        "7_Rubrics.json", "8_Verifier_Fails.txt", "1_Business_Function.txt", "2_Persona.txt"))
    traj_dir = task_dir / "Agent_Responses"
    if traj_dir.is_dir():
        for f in sorted(traj_dir.rglob("*.json"))[:8]:
            ssot_text += _read(f)
    fb = parsed.get("auditor_feedback", "")
    blocks = re.split(r"\n(?=\[(?:Fail|Non-Fail))", fb)
    n_conf = n_missing = n_none = 0
    for block in blocks:
        tag_m = CATEGORY_TAG_RE.search(block)
        if not tag_m:
            continue
        tag = f"[{tag_m.group(1)} - {tag_m.group(2).strip()}]"
        atoms = set(ATOM_ID_RE.findall(block)) | set(MONEY_RE.findall(block)) | set(EMAIL_RE.findall(block))
        if not atoms:
            n_none += 1
            print(f"FINDING {tag} | atoms: none cited | NO-ATOM-CITED (not independently verifiable - flag for revision)")
            continue
        confirmed = sorted(a for a in atoms if a in ssot_text)
        missing = sorted(a for a in atoms if a not in ssot_text)
        n_conf += len(confirmed)
        n_missing += len(missing)
        status = "CONFIRMED" if not missing else "PARTIAL" if confirmed else "NOT-FOUND"
        print(f"FINDING {tag} | atoms: {', '.join(sorted(atoms))} | {status}"
              + (f" (missing from SSOT: {', '.join(missing)})" if missing else ""))
    print(f"\nAUDIT SUMMARY: {n_conf} atoms confirmed in SSOT, {n_missing} not found, {n_none} findings cite no atoms")
    return 0


def feedback(task_dir: Path) -> int:
    """Draft 9_QC_Feedback skeleton from validator reports, per-finding SSOT citations."""
    from universes import detect_universe
    universe = detect_universe(task_dir)
    rep_dir = task_dir / "_aux" / "Validator_Reports"
    fails, nonfails = [], []
    for rp in sorted(rep_dir.glob("*.md")) if rep_dir.is_dir() else []:
        phase = rp.stem
        for line in _read(rp).splitlines():
            if line.startswith("- ") and "COUNCIL" not in line:
                entry = f"{line[2:].strip()} (validator: {phase})"
                sect = _read(rp)
                if line in sect.split("## WARN")[0] and "## FAIL" in sect.split("## WARN")[0]:
                    fails.append(entry)
                else:
                    nonfails.append(entry)
    lines = ["## QC Auditor Feedback", ""]
    if fails:
        lines.append("Failing issues:")
        for f in fails:
            atoms = set(ATOM_ID_RE.findall(f)) | set(MONEY_RE.findall(f)) | set(EMAIL_RE.findall(f))
            cite = f" [SSOT: {', '.join(sorted(atoms))}]" if atoms else " [SSOT: cite the specific record before shipping]"
            lines.append(f"- {f}{cite}")
        lines.append("")
    if nonfails:
        lines.append("Non-failing issues:")
        for f in nonfails[:20]:
            atoms = set(ATOM_ID_RE.findall(f)) | set(MONEY_RE.findall(f)) | set(EMAIL_RE.findall(f))
            cite = f" [SSOT: {', '.join(sorted(atoms))}]" if atoms else ""
            lines.append(f"- {f}{cite}")
        lines.append("")
    cats = []
    for f in fails:
        cats.append('"[All] [All] [Fail - Validator Finding]"')
    lines += ["## Error Categories", "", "[" + ", ".join(sorted(set(cats))) + "]", "",
              f"(draft generated from deterministic validator reports; universe={universe})"]
    print("\n".join(lines))
    return 0


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ("parse", "classify", "selftest", "audit", "feedback"):
        print(__doc__)
        return 2
    cmd, target = sys.argv[1], Path(sys.argv[2]).resolve()
    if cmd == "parse":
        print(json.dumps(parse_verdict(target), indent=2))
        return 0
    if cmd == "classify":
        parsed = parse_verdict(target)
        bucket = classify(parsed)
        print(f"bucket: {bucket}")
        print(f"evidence: qc_score={parsed.get('qc_score')} final_score={parsed.get('final_score')} "
              f"dispute={'yes' if parsed.get('dispute') else 'no'} "
              f"validation_decision={(parsed.get('validation') or {}).get('decision')}")
        return 0
    if cmd == "selftest":
        return selftest(target)
    if cmd == "audit":
        return audit(target)
    if cmd == "feedback":
        return feedback(target)
    return 2


if __name__ == "__main__":
    sys.exit(main())
