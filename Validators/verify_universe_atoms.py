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
import os
import re
import sys
from pathlib import Path
from typing import List, Dict

ROOT = Path(__file__).resolve().parent.parent

try:
    from Validators.universes import detect_universe, get_universe_constants, get_framework_profile
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from universes import detect_universe, get_universe_constants, get_framework_profile


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
PHMSA_HAZMAT_CLAIM = re.compile(
    r"\b(?:PHMSA|DOT\s+(?:hazmat|placard|compliance|certificate|certification)|hazmat\s+(?:certificate|documentation|placard|shipment|compliance))\b",
    re.IGNORECASE,
)
AIRTABLE_VS_CRM_CLAIM = re.compile(
    r"\bCRM\b[^.\n]{0,80}\b(?:relocation|vendor\s+assignment|coordinator\s+assignment|stipend|move\s+status|apartment|moving\s+company)\b",
    re.IGNORECASE,
)
STARPM_AIRTABLE_REC = re.compile(r"\brec[a-f0-9]{14,16}\b")
STARPM_LINEAR_ISSUE = re.compile(r"\bOPS-\d{1,4}\b")
STARPM_HUBSPOT_OBJ = re.compile(r"\b(?:deal|contact|ticket|comp|engagement)_[a-z0-9]{6,40}\b")
STARPM_INVOICE = re.compile(r"\b(?:INV-2026-\d{3,7}(?:-\d{2,4})?|BILL-2026-\d{3,7})\b")
STARPM_SLACK_CHAN = re.compile(r"\bC\d{3}\b")
STARPM_ISO_DATE = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")


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


POINTER_MARKERS = {"How This Works", "Base Universe Path", "Changelog Path", "SQL Query"}
# The V5 HarmonyGames drop no longer ships a combined export, so the old _COMBINED_BLOB
# skip matched zero files on disk and asserted nothing. Payload SHAPE (blob absent, 11
# service dirs) is now check_hydration.py's job; this module's job is staying constant-memory.
# What keeps the 105 MB git packfile and the ~245k other non-JSON payload files out of the
# byte stream is the `.json` extension filter in _scan_roots below - that is the load-bearing
# guard, and test_memory_bounds.py G1(c) is pointed at it.


def is_pointer_payload(task_dir: Path) -> bool:
    """True when 3_UniverseDataForThisTask.json is the upstream pointer, not data."""
    f = task_dir / "3_UniverseDataForThisTask.json"
    if not f.is_file():
        return False
    try:
        payload = json.load(open(f, encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    return (isinstance(payload, list) and len(payload) == 1
            and isinstance(payload[0], dict)
            and POINTER_MARKERS & set(payload[0]))


class Presence:
    """Answers "does this atom appear in the universe?" for one task.

    Two backends, chosen by how the universe stores its data.

    `blob` (brookfield / keystone / moveops / starpm)
        3_UniverseDataForThisTask.json IS the data, so the old in-memory substring test
        is exactly right. It is now built ONCE per task instead of once per atom, which
        is the same answer for a fraction of the work.

    `export` (harmonygames)
        The per-task file is a ~700-byte POINTER. Reading it as data yielded one record
        with no source, so every presence search missed and real personas were reported
        as phantom emails on every HG task. The truth is the hydrated base export, which
        is 1.7 GB of JSON across 71k files - far too much to load, which is what OOM-killed
        an earlier attempt at this fix. So we stream: ONE pass, one compiled alternation
        of every atom, fixed-size chunks with an overlap so a needle straddling a chunk
        boundary is still found, and an early exit as soon as every atom is accounted for.
        Memory is O(atoms), never O(universe).

    Atoms must be primed in a batch before lookup, because the export backend can only
    afford a single pass over the payload.
    """

    def __init__(self, universe: str, task_dir: Path, indexed: dict, consts: dict):
        self.universe = universe
        self.task_dir = task_dir
        contract = get_framework_profile(universe).get("universe_data_contract", "per_task_json")
        self.mode = "export" if contract == "base_export_plus_changelog" else "blob"
        self._blob = None
        self._found = None
        if self.mode == "blob":
            self._blob = json.dumps(indexed, default=str).lower()

    def _scan_roots(self):
        """Files to stream, cheapest-and-likeliest first so the early exit pays off."""
        base = ROOT / get_universe_constants(self.universe)["base_path"] / "Services_Data"
        changelog = self.task_dir / "4_Changelog.json"
        if changelog.is_file():
            yield changelog
        seen = set()
        for depth in (1, None):          # service-level tables first, then nested records
            for dirpath, _dirnames, filenames in os.walk(base):
                rel_depth = len(Path(dirpath).relative_to(base).parts)
                if depth == 1 and rel_depth != 1:
                    continue
                if depth is None and rel_depth <= 1:
                    continue
                for name in sorted(filenames):
                    if not name.endswith(".json") or name.startswith("._"):
                        continue
                    p = os.path.join(dirpath, name)
                    if p in seen:
                        continue
                    seen.add(p)
                    yield Path(p)

    def prime(self, atoms) -> None:
        atoms = sorted({a.lower() for a in atoms if a})
        if self.mode == "blob" or not atoms:
            self._found = set()
            return
        rx = re.compile(b"|".join(re.escape(a.encode()) for a in atoms))
        overlap = max(len(a) for a in atoms) - 1
        found = set()
        for path in self._scan_roots():
            try:
                fh = open(path, "rb")
            except OSError:
                try:                      # Windows MAX_PATH: the payload nests past 260 chars
                    fh = open("\\\\?\\" + str(path.resolve()), "rb")
                except OSError:
                    continue
            with fh:
                tail = b""
                while True:
                    chunk = fh.read(8 << 20)
                    if not chunk:
                        break
                    found.update(m.decode("utf-8", "ignore") for m in rx.findall((tail + chunk).lower()))
                    tail = chunk[-overlap:] if overlap > 0 else b""
            if len(found) == len(atoms):
                break                     # every atom accounted for; no need to read the rest
        self._found = found

    def contains(self, atom: str) -> bool:
        if self.mode == "blob":
            return atom.lower() in self._blob
        if self._found is None:
            raise RuntimeError("Presence.prime() must run before contains() on the export backend")
        return atom.lower() in self._found


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
        "phmsa_claims": [],
        "airtable_vs_crm_claims": [],
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
    for m in PHMSA_HAZMAT_CLAIM.finditer(text):
        atoms["phmsa_claims"].append({"match": m.group(0), "context": text[max(0, m.start()-60):m.end()+80]})
    for m in AIRTABLE_VS_CRM_CLAIM.finditer(text):
        atoms["airtable_vs_crm_claims"].append({"context": text[max(0, m.start()-40):m.end()+40]})
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


def verify_phmsa_claim_moveops(claim: dict, indexed: dict, check: AtomCheck) -> None:
    context = claim["context"]
    has_signed_ref = bool(re.search(
        r"\b(?:signed\s+(?:DOT|hazmat|PHMSA)?\s*certificate|signed\s+(?:certification|documentation|paperwork)|certificate\s+(?:on\s+file|received|signed)|placard(?:ed|ing)?\s+(?:certificate|paperwork))\b",
        context, re.IGNORECASE,
    ))
    has_verbal_only = bool(re.search(
        r"\b(?:verbal\s+(?:confirmation|approval|ok|sign[\-\s]?off)|over\s+the\s+phone|told\s+(?:me|us)\s+(?:on\s+the\s+phone|verbally))\b",
        context, re.IGNORECASE,
    ))
    if has_verbal_only and not has_signed_ref:
        check.record(
            atom=f"PHMSA/DOT hazmat claim: `{claim['match']}`",
            query="manual: PHMSA / DOT hazmat compliance requires a SIGNED carrier certificate (Swift / Heartland email + Airtable record). Verbal-only is non-compliant.",
            row=f"context cites verbal confirmation: `{claim['match']}`",
            verdict="POTENTIAL FAIL: PHMSA/DOT hazmat claim relies on verbal confirmation. Compliance requires a signed certificate on file. Verify Airtable tblRelocations01 and the carrier email thread show actual signed documentation.",
            severity="WARN",
        )
    else:
        airtable_present = bool(indexed.get("airtable.tblRelocations01") or indexed.get("airtable.relocations"))
        check.record(
            atom=f"PHMSA/DOT hazmat claim: `{claim['match']}`",
            query="Airtable tblRelocations01 presence + signed certificate reference",
            row="airtable present" if airtable_present else "no airtable relocations table — cannot verify",
            verdict="present — verify per-shipment signed certificate manually" if airtable_present else "no airtable.tblRelocations01 in universe data; PHMSA claim cannot be machine-verified",
            severity="WARN",
        )


def verify_airtable_vs_crm_claim_moveops(claim: dict, check: AtomCheck) -> None:
    check.record(
        atom=f"Airtable-vs-CRM source-of-truth (MoveOps): `{claim['context'][:60]}...`",
        query="manual: relocation/vendor/coordinator state must be sourced from Airtable tblRelocations01, not CRM",
        row="CRM cited as source for relocation/vendor/stipend state",
        verdict="POTENTIAL FAIL: claim cites CRM as source for relocation/vendor/coordinator state; that lives in Airtable tblRelocations01 / tblStipends00001. CRM holds the deal/engagement funnel only. Verify the rubric/OE doesn't trust CRM for relocation state.",
        severity="WARN",
    )


def verify_starpm_atoms(text: str, indexed: dict, consts: dict, check: AtomCheck,
                        presence: "Presence") -> None:
    # Structured StarPM ids must exist in the universe (a phantom id is a FAIL).
    for pat, label in ((STARPM_AIRTABLE_REC, "airtable record"),
                       (STARPM_LINEAR_ISSUE, "linear issue"),
                       (STARPM_HUBSPOT_OBJ, "hubspot object")):
        for atom in sorted(set(pat.findall(text))):
            verify_atom_presence(atom, label, presence, check)
    full_blob = json.dumps(indexed, default=str).lower()
    # Invoice numbers live in a decoy-heavy space (near-duplicate files); WARN on
    # absence rather than FAIL so the operator disambiguates the authoritative doc.
    for inv in sorted(set(STARPM_INVOICE.findall(text))):
        if inv.lower() not in full_blob:
            check.record(
                atom=f"invoice {inv}",
                query="presence search in 3_UniverseDataForThisTask.json",
                row="NOT FOUND",
                verdict="invoice number not found in universe (verify against QuickBooks DocNumbers; watch for near-duplicate decoy files)",
                severity="WARN",
            )
    # Slack channels must be within the StarPM range (C001-C008).
    valid_channels = consts.get("slack_channels") or set()
    for chan in sorted(set(STARPM_SLACK_CHAN.findall(text))):
        if valid_channels and chan not in valid_channels:
            check.record(
                atom=f"slack channel {chan}",
                query=f"channel in {sorted(valid_channels)}",
                row=chan,
                verdict=f"Slack channel {chan} outside the StarPM valid range (C001-C008)",
                severity="WARN",
            )
    # Dates in a claim should fall in the StarPM active workflow window.
    for y, mo, da in sorted(set(STARPM_ISO_DATE.findall(text))):
        iso = f"{y}-{mo}-{da}"
        if not ("2026-05-01" <= iso <= "2026-07-01"):
            check.record(
                atom=f"date {iso}",
                query="StarPM active window 2026-05-01..2026-07-01",
                row=iso,
                verdict=f"date {iso} is outside the StarPM active workflow window (2026-05-01 to 2026-07-01); verify it is intentional",
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


def verify_atom_presence(atom: str, atom_type: str, presence: "Presence", check: AtomCheck) -> None:
    where = ("the hydrated base export" if presence.mode == "export"
             else "3_UniverseDataForThisTask.json")
    if presence.contains(atom):
        check.record(
            atom=f"{atom_type} {atom}",
            query=f"presence search in {where}",
            row="found",
            verdict="present in universe",
            severity="PASS",
        )
    else:
        check.record(
            atom=f"{atom_type} {atom}",
            query=f"presence search in {where}",
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
    export_backed = (get_framework_profile(universe).get("universe_data_contract", "per_task_json")
                     == "base_export_plus_changelog")

    if export_backed:
        # The per-task file is a POINTER here, so a thin `indexed` is EXPECTED and must not
        # be read as "no data". What would be fatal is an un-hydrated payload: with nothing
        # to search, every atom looks phantom and the gate emits confident false FAILs.
        # Refuse to render a verdict instead - a skipped check is recoverable, a wrong one
        # gets acted on.
        services = ROOT / consts["base_path"] / "Services_Data"
        if not services.is_dir() or not any(p.is_dir() for p in services.iterdir()):
            print(f"[SKIP] verify_universe_atoms: {universe} payload is NOT HYDRATED "
                  f"({services} has no service directories) - cannot verify atoms without "
                  f"data. Hydrate via Validators/hydrate_harmonygames.sh, then re-run.")
            sys.exit(0)
    elif not indexed:
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

    # Every atom that will get a presence verdict, resolved in ONE pass. The export
    # backend cannot afford a scan per atom, and priming up front also means the blob
    # backend stops re-serialising the universe once per atom.
    presence = Presence(universe, task_dir, indexed, consts)
    presence_atoms = set()
    for bucket in ("je_ids", "vendor_ids", "doc_ids", "exc_ids", "recon_ids",
                   "apinv_ids", "loan_ids", "emails"):
        presence_atoms |= set(atoms.get(bucket) or [])
    if universe == "starpm":
        for pat in (STARPM_AIRTABLE_REC, STARPM_LINEAR_ISSUE, STARPM_HUBSPOT_OBJ):
            presence_atoms |= set(pat.findall(combined))
    presence.prime(presence_atoms)

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
    if universe == "moveops":
        for c in atoms["phmsa_claims"]:
            verify_phmsa_claim_moveops(c, indexed, check)
        for c in atoms["airtable_vs_crm_claims"]:
            verify_airtable_vs_crm_claim_moveops(c, check)
    if universe == "starpm":
        verify_starpm_atoms(combined, indexed, consts, check, presence)
    for je in sorted(set(atoms["je_ids"])):
        verify_atom_presence(je, "JE", presence, check)
    for vid in sorted(set(atoms["vendor_ids"])):
        verify_atom_presence(vid, "vendor", presence, check)
    for did in sorted(set(atoms["doc_ids"])):
        verify_atom_presence(did, "doc", presence, check)
    for eid in sorted(set(atoms["exc_ids"])):
        verify_atom_presence(eid, "exception", presence, check)
    for rid in sorted(set(atoms["recon_ids"])):
        verify_atom_presence(rid, "recon", presence, check)
    for ai in sorted(set(atoms["apinv_ids"])):
        verify_atom_presence(ai, "apinv", presence, check)
    for li in sorted(set(atoms["loan_ids"])):
        verify_atom_presence(li, "loan", presence, check)
    for em in sorted(set(atoms["emails"])):
        verify_atom_presence(em, "email", presence, check)

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
