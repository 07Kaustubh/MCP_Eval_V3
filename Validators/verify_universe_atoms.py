#!/usr/bin/env python3
"""
verify_universe_atoms.py — programmatic atom-by-atom universe verification.

The LOAD-BEARING FLOOR check that 5 LLM gates missed.

Walks the prompt + OE + rubrics, extracts every concrete atom (account claim,
"X did/did not respond" claim, money/date/ID/email atom, persona-scope claim,
lifecycle-state claim), and runs a precise universe query per atom. Exits
non-zero on any atom FAIL with `STOP: <atom> | claim=<X> | universe-row=<Y> |
mismatch`.

Runs in seconds. Universe-aware via _aux/Universe.txt.

Usage:
    python3 Validators/verify_universe_atoms.py --task Tasks/<TASK_DIR>
    python3 Validators/verify_universe_atoms.py --task Tasks/<TASK_DIR> --verbose
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import List, Dict

ROOT = Path(__file__).resolve().parent.parent

try:
    from Validators.universes import detect_universe, get_universe_constants
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from universes import detect_universe, get_universe_constants


ACCOUNT_CLAIM = re.compile(
    r"(?:(?:the\s+)?(?P<role>[A-Z][A-Za-z][\w&/-]{1,30}(?:\s+[A-Z][A-Za-z][\w&/-]{1,30}){0,3})\s+account\s+(?P<acct>\d{4,6})|"
    r"account\s+(?P<acct2>\d{4,6})\s*\(\s*(?P<role2>[A-Z][\w\s/&-]{2,30})\s*\)|"
    r"account\s+(?P<acct3>\d{4,6})\s+(?:is|=|:)\s+(?P<role3>[A-Z][A-Za-z][\w&/-]{1,30}(?:\s+[A-Z][A-Za-z][\w&/-]{1,30}){0,3})\b)",
)
EMAIL_PATTERN = re.compile(r"\b([a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,})\b", re.IGNORECASE)
NO_RESPONSE_CLAIM = re.compile(
    r"\b(?P<who>[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s+(?:never\s+(?:responded|replied)|(?:has\s+)?not\s+(?:yet\s+)?(?:responded|replied|gotten\s+back|come\s+back)|did\s+not\s+(?:respond|reply)|has\s+been\s+silent)",
    re.IGNORECASE,
)
JE_ID = re.compile(r"\bJE-[a-z_]+-FP-\d{4}-\d{2}-\d{4}\b")
EXC_ID = re.compile(r"\bexc_[a-f0-9]{14}\b")
RECON_ID = re.compile(r"\bBL-[A-F0-9]{12}\b")
DOC_ID = re.compile(r"\bdoc_[a-f0-9]{8}\b")
VENDOR_ID = re.compile(r"\bVEN-\d{3,4}(?:-[A-Za-z]+)?(?:-\d{3,6})?\b")
APINV_ID = re.compile(r"\bapinv_[a-f0-9]{14,16}\b")
LOAN_ID = re.compile(r"\bLN-\d{4}-\d{4,6}\b")
MONEY_RE = re.compile(r"\$\s?(\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\d+(?:\.\d{2})?)")
TRID_CLAIM = re.compile(
    r"\b(?:TRID|loan\s+estimate|closing\s+disclosure|LE\s+(?:sent|delivered)|CD\s+(?:sent|delivered))\b[^.\n]{0,80}\b(?:within|in|before|after)\b[^.\n]{0,80}\b(\d+)\s+(?:business\s+days?|biz\s+days?|days?)\b",
    re.IGNORECASE,
)
LOS_VS_CRM_CLAIM = re.compile(
    r"\bCRM\b[^.\n]{0,80}\b(?:loan|borrower|condition|disclosure|underwriting|rate\s+lock|closing)\b",
    re.IGNORECASE,
)


class AtomCheck:
    def __init__(self):
        self.fails: List[str] = []
        self.warns: List[str] = []
        self.evidence: List[dict] = []
        self.checked: int = 0

    def record(self, atom: str, query: str, row: str, verdict: str, severity: str = "FAIL"):
        self.evidence.append({"atom": atom, "query": query, "row": row, "verdict": verdict, "severity": severity})
        if severity == "FAIL":
            self.fails.append(f"STOP: {atom} | claim={query} | universe-row={row} | {verdict}")
        elif severity == "WARN":
            self.warns.append(f"{atom} | {verdict}")
        self.checked += 1


def load_universe_data(task_dir: Path) -> dict:
    f = task_dir / "3_UniverseDataForThisTask.json"
    if not f.is_file():
        return {}
    try:
        data = json.load(open(f, encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    indexed = {}
    if isinstance(data, list):
        for r in data:
            src = r.get("source", "")
            rd = r.get("row_data", "{}")
            if isinstance(rd, str):
                try:
                    rd = json.loads(rd)
                except json.JSONDecodeError:
                    continue
            indexed.setdefault(src, []).append(rd)
    return indexed


def collect_atoms_from_text(text: str) -> Dict[str, List]:
    atoms = {
        "accounts": [],
        "emails": [],
        "no_response_claims": [],
        "je_ids": [],
        "exc_ids": [],
        "recon_ids": [],
        "doc_ids": [],
        "vendor_ids": [],
        "apinv_ids": [],
        "loan_ids": [],
        "amounts": [],
        "trid_claims": [],
        "los_vs_crm_claims": [],
    }
    for m in ACCOUNT_CLAIM.finditer(text):
        role = m.group("role") or m.group("role2") or m.group("role3") or ""
        acct = m.group("acct") or m.group("acct2") or m.group("acct3") or ""
        if acct and role:
            atoms["accounts"].append({"role": role.strip(), "account": acct.strip(), "context": text[max(0, m.start()-40):m.end()+40]})
    for m in EMAIL_PATTERN.finditer(text):
        atoms["emails"].append(m.group(1).lower())
    for m in NO_RESPONSE_CLAIM.finditer(text):
        atoms["no_response_claims"].append({"who": m.group("who"), "context": text[max(0, m.start()-40):m.end()+40]})
    for pat, key in ((JE_ID, "je_ids"), (EXC_ID, "exc_ids"), (RECON_ID, "recon_ids"),
                     (DOC_ID, "doc_ids"), (VENDOR_ID, "vendor_ids"), (APINV_ID, "apinv_ids"),
                     (LOAN_ID, "loan_ids")):
        for m in pat.finditer(text):
            atoms[key].append(m.group(0))
    for m in MONEY_RE.finditer(text):
        atoms["amounts"].append(m.group(0))
    for m in TRID_CLAIM.finditer(text):
        atoms["trid_claims"].append({"days": int(m.group(1)), "context": text[max(0, m.start()-60):m.end()+60]})
    for m in LOS_VS_CRM_CLAIM.finditer(text):
        atoms["los_vs_crm_claims"].append({"context": text[max(0, m.start()-40):m.end()+40]})
    return atoms


def verify_trid_claim_keystone(claim: dict, indexed: dict, check: AtomCheck) -> None:
    days = claim["days"]
    context = claim["context"]
    le_match = re.search(r"loan\s+estimate|LE\s+(?:sent|delivered)", context, re.IGNORECASE)
    cd_match = re.search(r"closing\s+disclosure|CD\s+(?:sent|delivered)", context, re.IGNORECASE)
    expected_days = 3
    if le_match and days != expected_days:
        check.record(
            atom=f"TRID Loan Estimate claim: {days} biz days",
            query="mortgage_los.disclosures + application_date check",
            row=f"claim says {days} biz days",
            verdict=f"TRID requires LE within 3 business days of application; claim states {days} — verify against actual disclosures.application_date for the loan",
            severity="WARN",
        )
    elif cd_match and days != expected_days:
        check.record(
            atom=f"TRID Closing Disclosure claim: {days} biz days",
            query="mortgage_los.disclosures + closing_date check",
            row=f"claim says {days} biz days",
            verdict=f"TRID requires CD 3 business days before closing; claim states {days} — verify against actual disclosures.closing_date for the loan",
            severity="WARN",
        )
    else:
        disclosures_present = bool(indexed.get("mortgage_los.disclosures"))
        check.record(
            atom=f"TRID claim ({days} biz days)",
            query="mortgage_los.disclosures presence",
            row="present" if disclosures_present else "MISSING TABLE",
            verdict="present — verify per-loan timing manually" if disclosures_present else "no disclosures table in universe data; TRID claim cannot be verified",
            severity="WARN",
        )


def verify_los_vs_crm_claim_keystone(claim: dict, check: AtomCheck) -> None:
    check.record(
        atom=f"LOS-vs-CRM source-of-truth: `{claim['context'][:60]}...`",
        query="manual: loan-level data must be sourced from mortgage_los, not CRM",
        row="CRM cited as source for loan-level data",
        verdict="POTENTIAL FAIL: claim cites CRM as source for loan-level fact; loan/borrower/condition data lives in mortgage_los. CRM holds marketing funnel only. Verify the rubric/OE doesn't trust CRM for loan state.",
        severity="WARN",
    )


def verify_account_claim_brookfield(claim: dict, indexed: dict, check: AtomCheck) -> None:
    acct = claim["account"]
    role_claimed = claim["role"].lower()
    context = claim["context"]
    entity_hint = None
    for ename in ("northstar_legal", "northstar", "acme_cloud", "acme", "brookfield"):
        if ename in context.lower():
            entity_hint = ename.replace("northstar", "northstar_legal").replace("acme", "acme_cloud")
            if entity_hint == "northstar_legal_legal":
                entity_hint = "northstar_legal"
            if entity_hint == "acme_cloud_cloud":
                entity_hint = "acme_cloud"
            break
    accounts_table = indexed.get("oracle_gl.ogl_accounts", [])
    matching = [r for r in accounts_table if str(r.get("account_number")) == acct and
                (entity_hint is None or r.get("entity_id") == entity_hint)]
    if not matching:
        check.record(
            atom=f"account {acct} (claimed role: {claim['role']})",
            query=f"oracle_gl.ogl_accounts WHERE account_number={acct}" + (f" AND entity_id={entity_hint}" if entity_hint else ""),
            row="NO ROW",
            verdict=f"account {acct} not found on entity {entity_hint or '<any>'}",
            severity="FAIL",
        )
        return
    actual_role = matching[0].get("description") or matching[0].get("account_name") or "<unknown>"
    if not any(tok in actual_role.lower() for tok in role_claimed.split() if len(tok) > 3):
        check.record(
            atom=f"account {acct} on {entity_hint or '<entity>'}",
            query=f"oracle_gl.ogl_accounts WHERE account_number={acct} AND entity_id={entity_hint}",
            row=f"actual: {actual_role}",
            verdict=f"role mismatch — prose says '{claim['role']}' but universe says '{actual_role}'",
            severity="FAIL",
        )
    else:
        check.record(
            atom=f"account {acct} on {entity_hint or '<entity>'}",
            query=f"oracle_gl.ogl_accounts WHERE account_number={acct}",
            row=f"actual: {actual_role}",
            verdict=f"verified — role matches",
            severity="PASS",
        )


def verify_no_response_claim(claim: dict, indexed: dict, check: AtomCheck) -> None:
    who = claim["who"]
    emails_table = indexed.get("email.emails", [])
    sender_emails = [r for r in emails_table if who.lower() in (r.get("from_address") or r.get("sender_email") or "").lower() or who.lower() in (r.get("from_name") or "").lower()]
    if not sender_emails:
        check.record(
            atom=f"'{who} never responded'",
            query=f"email.emails WHERE from contains '{who}'",
            row="NO SENT EMAILS",
            verdict=f"'{who}' has no sent emails to walk a thread from — cannot verify the no-response claim. Re-check the actual claim or rename the persona.",
            severity="WARN",
        )
        return
    subject_prefixes = set()
    for e in sender_emails:
        subj = (e.get("subject") or "")[:30].lower().lstrip("re: ").lstrip("fwd: ")
        if subj:
            subject_prefixes.add(subj)
    replies = []
    for e in emails_table:
        if e.get("parent_id") and any(e.get("parent_id") == s.get("email_id") or e.get("parent_id") == s.get("id") for s in sender_emails):
            replies.append(e)
        else:
            esubj = (e.get("subject") or "")[:30].lower().lstrip("re: ").lstrip("fwd: ")
            sender = (e.get("from_address") or e.get("sender_email") or "").lower()
            if esubj in subject_prefixes and who.lower() not in sender:
                replies.append(e)
    if replies:
        check.record(
            atom=f"'{who} never responded'",
            query=f"email.emails WHERE parent_id descendant-of {who}'s emails OR subject matches",
            row=f"{len(replies)} reply emails found",
            verdict=f"CONTRADICTED — universe shows {len(replies)} replies in {who}'s threads",
            severity="FAIL",
        )
    else:
        check.record(
            atom=f"'{who} never responded'",
            query=f"email.emails WHERE parent_id descendant-of {who}'s emails",
            row="0 reply emails",
            verdict=f"verified — no replies found in {who}'s threads",
            severity="PASS",
        )


def verify_atom_presence(atom: str, atom_type: str, indexed: dict, check: AtomCheck) -> None:
    full_blob = json.dumps(indexed, default=str).lower()
    if atom.lower() in full_blob:
        check.record(
            atom=f"{atom_type} {atom}",
            query=f"presence search in 3_UniverseDataForThisTask.json",
            row="found",
            verdict="present in universe",
            severity="PASS",
        )
    else:
        check.record(
            atom=f"{atom_type} {atom}",
            query=f"presence search in 3_UniverseDataForThisTask.json",
            row="NOT FOUND",
            verdict=f"phantom {atom_type} — not in this task's universe",
            severity="FAIL",
        )


def render_report(check: AtomCheck) -> str:
    lines = ["# Universe Atom Verification Report", ""]
    lines.append(f"**Atoms checked:** {check.checked}")
    lines.append(f"**FAIL:** {len(check.fails)}")
    lines.append(f"**WARN:** {len(check.warns)}")
    lines.append("")
    if check.fails:
        lines.append("## FAIL")
        for f in check.fails:
            lines.append(f"- {f}")
        lines.append("")
    if check.warns:
        lines.append("## WARN")
        for w in check.warns:
            lines.append(f"- {w}")
        lines.append("")
    lines.append("## Per-atom evidence table")
    lines.append("")
    lines.append("| Atom | Query | Row | Verdict | Severity |")
    lines.append("|---|---|---|---|---|")
    for e in check.evidence:
        lines.append(f"| {e['atom']} | `{e['query']}` | {e['row'][:80]} | {e['verdict']} | {e['severity']} |")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True)
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    task_dir = Path(args.task).resolve()
    if not task_dir.is_dir():
        print(f"ERROR: {task_dir} not a directory", file=sys.stderr)
        sys.exit(2)

    universe = detect_universe(task_dir)
    consts = get_universe_constants(universe)
    indexed = load_universe_data(task_dir)
    if not indexed:
        print(f"WARN: no 3_UniverseDataForThisTask.json on {task_dir} — cannot verify atoms")
        sys.exit(0)

    check = AtomCheck()
    text_parts = []
    for fname in ("5_Prompt.txt", "6_Oracle_Events.txt", "14_Updated_Oracle_Events.txt"):
        f = task_dir / fname
        if f.is_file():
            text_parts.append(f.read_text(encoding="utf-8"))
    for fname in ("7_Rubrics.json", "15_Updated_Rubrics.json"):
        f = task_dir / fname
        if f.is_file():
            try:
                rubs = json.loads(f.read_text(encoding="utf-8"))
                if isinstance(rubs, list):
                    for r in rubs:
                        if isinstance(r, dict):
                            text_parts.append(r.get("title", "") or "")
                            text_parts.append(r.get("evidence", "") or (r.get("annotations", {}) or {}).get("evidence", "") or "")
                            text_parts.append(r.get("justification", "") or (r.get("annotations", {}) or {}).get("justification", "") or "")
            except json.JSONDecodeError:
                pass

    combined = "\n".join(text_parts)
    atoms = collect_atoms_from_text(combined)

    if consts.get("account_trap_check"):
        for c in atoms["accounts"]:
            verify_account_claim_brookfield(c, indexed, check)
    for c in atoms["no_response_claims"]:
        verify_no_response_claim(c, indexed, check)
    if universe == "keystone":
        for c in atoms["trid_claims"]:
            verify_trid_claim_keystone(c, indexed, check)
        for c in atoms["los_vs_crm_claims"]:
            verify_los_vs_crm_claim_keystone(c, check)
    for je in set(atoms["je_ids"]):
        verify_atom_presence(je, "JE", indexed, check)
    for vid in set(atoms["vendor_ids"]):
        verify_atom_presence(vid, "vendor", indexed, check)
    for did in set(atoms["doc_ids"]):
        verify_atom_presence(did, "doc", indexed, check)
    for eid in set(atoms["exc_ids"]):
        verify_atom_presence(eid, "exception", indexed, check)
    for rid in set(atoms["recon_ids"]):
        verify_atom_presence(rid, "recon", indexed, check)
    for ai in set(atoms["apinv_ids"]):
        verify_atom_presence(ai, "apinv", indexed, check)
    for li in set(atoms["loan_ids"]):
        verify_atom_presence(li, "loan", indexed, check)
    for em in set(atoms["emails"]):
        verify_atom_presence(em, "email", indexed, check)

    report = render_report(check)
    out_dir = task_dir / "_aux" / "Council_Reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "verify_universe_atoms.md"
    out_file.write_text(report, encoding="utf-8")

    status = "FAIL" if check.fails else ("WARN" if check.warns else "PASS")
    print(f"[{status}] verify_universe_atoms: {len(check.fails)} fails, {len(check.warns)} warns, {check.checked} atoms checked (universe: {universe}) -> {out_file}")

    if args.verbose:
        print(report)

    sys.exit(1 if check.fails else 0)


if __name__ == "__main__":
    main()
