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

try:
    from Validators.universes import detect_universe
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from universes import detect_universe


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


def build_id_map(by_source):
    """StarPM: map slack/linear/airtable/hubspot/contacts user-id -> email."""
    m = {}
    for key, idf in (
        ("slack.slack_users", "id"),
        ("linear.linear_users", "id"),
        ("airtable.airtable_users", "id"),
        ("hubspot.hubspot_owners", "id"),
        ("contacts.contacts", "contact_id"),
    ):
        for u in by_source.get(key, []):
            uid = u.get(idf)
            email = u.get("email")
            if not email:
                prof = u.get("profile") if isinstance(u.get("profile"), dict) else {}
                if isinstance(prof, dict):
                    email = prof.get("email")
            if uid and email:
                m[str(uid)] = str(email).lower()
    return m


STARPM_PERSON_FIELDS = PERSON_FIELDS + (
    "from_address", "to_addresses", "cc_addresses", "bcc_addresses",
    "creator_email", "organizer_email",
)


def _emit_person_token(v, out):
    if isinstance(v, str):
        s = v.strip()
        if s.startswith("[") and s.endswith("]"):
            try:
                arr = json.loads(s)
            except json.JSONDecodeError:
                arr = None
            if isinstance(arr, list):
                for e in arr:
                    if isinstance(e, str):
                        out.append(e)
                return
        out.append(v)
    elif isinstance(v, list):
        for e in v:
            if isinstance(e, str):
                _emit_person_token(e, out)


def walk_persons_deep(obj, out, fields):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in fields:
                _emit_person_token(v, out)
            else:
                walk_persons_deep(v, out, fields)
    elif isinstance(obj, list):
        for x in obj:
            walk_persons_deep(x, out, fields)


def _section_people_starpm(by_source, ledger_emails, id_map):
    counter = Counter()
    person_period_pairs = Counter()
    for src, rows in by_source.items():
        for inner in rows:
            tokens = []
            walk_persons_deep(inner, tokens, STARPM_PERSON_FIELDS)
            cleaned = []
            for t in tokens:
                if not isinstance(t, str):
                    continue
                t = t.strip()
                if not t or t in ("[]", "{}", "null", "None"):
                    continue
                t = id_map.get(t, t).lower()
                cleaned.append(t)
            for p in set(cleaned):
                counter[p] += 1
                pid = inner.get("period_id")
                if pid:
                    person_period_pairs[(p, str(pid))] += 1
    rows = ["## People by artifact density (top 30)", "", "| Person | Mentions |", "|---|---:|"]
    for person, n in counter.most_common(30):
        marker = " ✓" if person in ledger_emails else ""
        rows.append(f"| `{person}`{marker} | {n} |")
    rows.append("")
    return "\n".join(rows), person_period_pairs


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


def section_people(by_source, ledger_emails, universe="brookfield", id_map=None):
    if universe == "starpm":
        return _section_people_starpm(by_source, ledger_emails, id_map or {})
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


def section_starpm(by_source):
    rows = []
    atr = by_source.get("airtable.airtable_records", [])
    if atr:
        by_table = Counter()
        mr_status = Counter()
        mt_priority = Counter()
        for r in atr:
            t = r.get("table_id", "?")
            by_table[t] += 1
            fld = r.get("fields") if isinstance(r.get("fields"), dict) else {}
            if t == "tblMakeReady":
                mr_status[str(fld.get("fldTurnStatus", "?"))] += 1
            elif t == "tblMaintenanceTickets":
                mt_priority[str(fld.get("fldPriority", "?"))] += 1
        rows += ["## Airtable make-ready + maintenance (StarPM system of record)", "", "| Table | Records |", "|---|---:|"]
        for t, n in by_table.most_common():
            rows.append(f"| `{t}` | {n} |")
        rows.append("")
        if mr_status:
            rows += ["### Make-Ready by turn status", "", "| Status | Count |", "|---|---:|"]
            for k, n in mr_status.most_common():
                rows.append(f"| `{k}` | {n} |")
            rows.append("")
        if mt_priority:
            rows += ["### Maintenance tickets by priority", "", "| Priority | Count |", "|---|---:|"]
            for k, n in mt_priority.most_common():
                rows.append(f"| `{k}` | {n} |")
            rows.append("")
    qbe = by_source.get("quickbooks.quickbooks_entities", [])
    if qbe:
        by_type = Counter(q.get("entity_type", "?") for q in qbe)
        rows += ["## QuickBooks entities by type", "", "| Entity type | Count |", "|---|---:|"]
        for k, n in by_type.most_common():
            rows.append(f"| `{k}` | {n} |")
        rows.append("")
    hso = by_source.get("hubspot.hubspot_objects", [])
    if hso:
        by_otype = Counter(h.get("object_type", "?") for h in hso)
        deal_stage = Counter()
        for h in hso:
            if h.get("object_type") == "deals":
                props = h.get("properties")
                if isinstance(props, str):
                    try:
                        props = json.loads(props)
                    except json.JSONDecodeError:
                        props = {}
                if isinstance(props, dict):
                    deal_stage[str(props.get("dealstage", "?"))] += 1
        rows += ["## HubSpot objects by type", "", "| Object type | Count |", "|---|---:|"]
        for k, n in by_otype.most_common():
            rows.append(f"| `{k}` | {n} |")
        rows.append("")
        if deal_stage:
            rows += ["### HubSpot deals by pipeline stage", "", "| Stage | Count |", "|---|---:|"]
            for k, n in deal_stage.most_common():
                rows.append(f"| `{k}` | {n} |")
            rows.append("")
    li = by_source.get("linear.linear_issues", [])
    if li:
        by_state = Counter(str(i.get("state_id", "?")) for i in li)
        rows += ["## Linear issues by workflow state", "", "| state_id | Count |", "|---|---:|"]
        for k, n in by_state.most_common():
            rows.append(f"| `{k}` | {n} |")
        rows.append("")
    sm = by_source.get("slack.slack_messages", [])
    if sm:
        by_chan = Counter(str(m.get("channel_id", "?")) for m in sm)
        rows += ["## Slack messages by channel", "", "| Channel | Count |", "|---|---:|"]
        for k, n in by_chan.most_common():
            rows.append(f"| `{k}` | {n} |")
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

    try:
        universe = detect_universe(task_dir)
    except Exception:
        universe = "brookfield"
    id_map = build_id_map(by_source) if universe == "starpm" else {}
    people_md, person_period_pairs = section_people(by_source, ledger_emails, universe, id_map)
    header = [
        f"# Graph Report — `{task_dir.name}`",
        "",
        "Compact discovery map for HARDNESS lever selection. People marked `✓` are confirmed contacts in the Fact Ledger.",
        "",
        people_md,
    ]
    if universe == "starpm":
        sections = header + [section_starpm(by_source), section_pairs(person_period_pairs)]
    else:
        sections = header + [
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
