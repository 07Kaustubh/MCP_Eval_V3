#!/usr/bin/env python3
"""
Usage:
    python Validators/build_graph_report.py <path_to_task_dir>

Reads <task_dir>/_aux/Universe_Split/*.json and emits
<task_dir>/_aux/Universe_Index/graph_report.md — a compact discovery map
for the HARDNESS phase: who shows up where, which periods are dense, which
exception/recon/JE clusters exist.

Used by HARDNESS to pick the densest persona × period × system intersection
for stump-able levers. Replaces guesswork "which persona has the most
cross-system noise" with a counted answer.

Output sections:
  - People by artifact density          top 30 people by total mention count across services
  - Periods by JE density               JE counts per fiscal period
  - Open exceptions by entity           exception state breakdown per entity
  - Open reconciliations by entity      recon state breakdown per entity
  - Pending AP invoices by vendor       top 20 vendors by pending-AP count
  - Records Vault documents by kind     document type breakdown
  - Cross-service overlap pairs         top 10 (person, period) pairs with the most artifacts
"""

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path


def parse_inner(rec):
    if not isinstance(rec, dict):
        return None
    rd = rec.get("row_data")
    if isinstance(rd, str):
        try:
            return json.loads(rd)
        except json.JSONDecodeError:
            return None
    if isinstance(rd, dict):
        return rd
    return rec


def load_records(split_dir):
    by_source = defaultdict(list)
    for p in split_dir.glob("*.json"):
        if p.name == "Universe_complete_data.json":
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if not isinstance(data, list):
            continue
        for rec in data:
            inner = parse_inner(rec)
            if inner is not None:
                by_source[p.stem].append(inner)
    return by_source


PERSON_FIELDS = (
    "sender", "recipients_json", "cc_json", "bcc_json", "organizer", "attendees",
    "owner", "reviewer", "preparer", "certifier", "approver", "assigned_to",
    "identified_by", "author", "actor", "uploaded_by", "granted_by", "grantee",
    "revoked_by", "locked_by", "unlocked_by", "prepared_by", "posted_by",
    "approved_by", "rejected_by", "completed_by", "creator_id", "user_id",
    "sender_id", "participant_ids", "members_json", "attached_by",
    "author_id", "assignee_id", "lead_id",
)


def walk_persons(obj, out):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in PERSON_FIELDS:
                if isinstance(v, str):
                    out.append(v)
                elif isinstance(v, list):
                    out.extend(s for s in v if isinstance(s, str))
            else:
                walk_persons(v, out)
    elif isinstance(obj, list):
        for x in obj:
            walk_persons(x, out)


def section_people(by_source, ledger_emails):
    counter = Counter()
    person_period_pairs = Counter()
    for src, rows in by_source.items():
        for inner in rows:
            persons = []
            walk_persons(inner, persons)
            persons = [p.strip() for p in persons if isinstance(p, str) and p.strip() and p.strip() not in ("[]", "{}", "null", "None")]
            for p in set(persons):
                counter[p.lower()] += 1
                pid = inner.get("period_id")
                if pid:
                    person_period_pairs[(p.lower(), str(pid))] += 1
    rows = ["## People by artifact density (top 30)", "", "| Person | Mentions |", "|---|---:|"]
    for person, n in counter.most_common(30):
        marker = " ✓" if person in ledger_emails else ""
        rows.append(f"| `{person}`{marker} | {n} |")
    rows.append("")
    return "\n".join(rows), person_period_pairs


def section_periods(by_source):
    je_per_period = Counter()
    for inner in by_source.get("oracle_gl.ogl_journal_entries", []):
        pid = inner.get("period_id")
        if pid:
            je_per_period[str(pid)] += 1
    rows = ["## Periods by JE density (top 20)", "", "| Period | JE count |", "|---|---:|"]
    for pid, n in je_per_period.most_common(20):
        rows.append(f"| `{pid}` | {n} |")
    rows.append("")
    return "\n".join(rows)


def section_exceptions(by_source):
    by_entity_state = defaultdict(Counter)
    for inner in by_source.get("blackline.blackline_exceptions", []):
        ent = str(inner.get("entity_id", "?"))
        state = str(inner.get("state", "?"))
        by_entity_state[ent][state] += 1
    rows = ["## BlackLine exceptions by entity × state", "", "| Entity | State | Count |", "|---|---|---:|"]
    for ent in sorted(by_entity_state):
        for state, n in by_entity_state[ent].most_common():
            rows.append(f"| `{ent}` | `{state}` | {n} |")
    rows.append("")
    return "\n".join(rows)


def section_recons(by_source):
    by_entity_state = defaultdict(Counter)
    for inner in by_source.get("blackline.blackline_reconciliations", []):
        ent = str(inner.get("entity_id", "?"))
        state = str(inner.get("state", "?"))
        by_entity_state[ent][state] += 1
    rows = ["## BlackLine reconciliations by entity × state", "", "| Entity | State | Count |", "|---|---|---:|"]
    for ent in sorted(by_entity_state):
        for state, n in by_entity_state[ent].most_common():
            rows.append(f"| `{ent}` | `{state}` | {n} |")
    rows.append("")
    return "\n".join(rows)


def section_ap(by_source):
    pending_by_vendor = Counter()
    for inner in by_source.get("sap_subledger.ap_invoices", []):
        if str(inner.get("status", "")).lower() == "pending_approval":
            pending_by_vendor[str(inner.get("vendor_id", "?"))] += 1
    rows = ["## Pending AP invoices by vendor (top 20)", "", "| Vendor | Pending count |", "|---|---:|"]
    for vid, n in pending_by_vendor.most_common(20):
        rows.append(f"| `{vid}` | {n} |")
    rows.append("")
    return "\n".join(rows)


def section_docs(by_source):
    by_kind = Counter()
    by_class = Counter()
    for inner in by_source.get("records_vault.rv_documents", []):
        by_kind[str(inner.get("kind", "?"))] += 1
        by_class[str(inner.get("classification", "?"))] += 1
    rows = ["## Records Vault documents", "", "### By kind", "", "| Kind | Count |", "|---|---:|"]
    for k, n in by_kind.most_common():
        rows.append(f"| `{k}` | {n} |")
    rows += ["", "### By classification", "", "| Classification | Count |", "|---|---:|"]
    for k, n in by_class.most_common():
        rows.append(f"| `{k}` | {n} |")
    rows.append("")
    return "\n".join(rows)


def section_pairs(person_period_pairs):
    rows = ["## Densest (person, period) pairs (top 15)", "",
            "Use these for HARDNESS lever discovery: the agent will have to investigate the most artifacts around these intersections.",
            "", "| Person | Period | Artifacts touching both |", "|---|---|---:|"]
    for (person, pid), n in person_period_pairs.most_common(15):
        rows.append(f"| `{person}` | `{pid}` | {n} |")
    rows.append("")
    return "\n".join(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task_dir")
    args = ap.parse_args()
    task_dir = Path(args.task_dir).resolve()
    split_dir = task_dir / "_aux" / "Universe_Split"
    if not split_dir.is_dir():
        print(f"ERROR: {split_dir} missing — run split_universe.py first", file=sys.stderr)
        sys.exit(2)

    by_source = load_records(split_dir)
    ledger_path = task_dir / "_aux" / "Fact_Ledger.json"
    ledger_emails = set()
    if ledger_path.is_file():
        try:
            ledger_emails = set(json.loads(ledger_path.read_text(encoding="utf-8")).get("emails", []))
        except json.JSONDecodeError:
            pass

    people_md, person_period_pairs = section_people(by_source, ledger_emails)
    sections = [
        f"# Graph Report — `{task_dir.name}`",
        "",
        "Compact discovery map for HARDNESS lever selection. People marked `✓` are confirmed contacts in the Fact Ledger.",
        "",
        people_md,
        section_periods(by_source),
        section_exceptions(by_source),
        section_recons(by_source),
        section_ap(by_source),
        section_docs(by_source),
        section_pairs(person_period_pairs),
    ]
    out = task_dir / "_aux" / "Universe_Index" / "graph_report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(sections), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
