#!/usr/bin/env python3
"""
Usage:
    python Validators/build_fact_ledger.py <path_to_task_dir>

Reads <task_dir>/_aux/Universe_Split/*.json and emits
<task_dir>/_aux/Fact_Ledger.json — a flat surface of verifiable atoms that
Council A (grounding) checks against instead of grepping the raw JSON each time.

Atoms emitted:
  - emails                lowercased, deduped
  - amounts               canonical 2dp money strings (decimal Decimal-rounded)
  - dates                 ISO YYYY-MM-DD with day_of_week
  - ids                   per-category sets (je, exception, recon, doc, vendor, apinv, slack_channel, contact, persona, airtable_record, linear_issue, reminder, conversation, calendar_event)
  - accounts_by_entity    {entity_id: {account_number: name}}
  - fiscal_periods        {period_id: {status, locked_at, bd3_lock_at, bd5_close_at}}
  - personas              {email: {name, title, is_user}}
  - aliases               {first_name: [emails], last_name: [emails], full_name: [emails]}
  - entities              set of entity_id slugs
  - hash                  sha256 of source universe (regenerate trigger)
"""

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
ISO_DATE_RE = re.compile(r"(?<!\d)(\d{4}-\d{2}-\d{2})(?!\d)")
MONEY_FIELD_HINTS = (
    "amount", "debit", "credit", "balance", "total", "value", "price", "cost",
    "fee", "variance", "_var", "net_", "gross", "paid", "due", "subtotal", "tax",
    "principal", "interest", "accrual", "depreciation", "adjustment",
    "financial_impact",
)

ID_PATTERNS = {
    "je": (re.compile(r"\bJE-[a-z_]+-FP-\d{4}-\d{2}-\d{4}\b"), "entry_number"),
    "exception": (re.compile(r"\bexc_[a-f0-9]{14,16}\b"), "id"),
    "recon": (re.compile(r"\bBL-[A-F0-9]{12,16}\b"), "id"),
    "doc": (re.compile(r"\bdoc_[a-f0-9]{8,16}\b"), "id"),
    "vendor": (re.compile(r"\bVEN-\d{3,4}(?:-[A-Za-z])?(?:-\d{3,6})?\b"), "vendor_id"),
    "apinv": (re.compile(r"\bapinv_[a-f0-9]{14,16}\b"), "id"),
    "linear_issue": (re.compile(r"\bissue_[a-f0-9]{20,40}\b"), "id"),
    "reminder": (re.compile(r"\breminder_[a-z0-9_]{6,}\b"), "id"),
    "conversation": (re.compile(r"\bconv_[a-z0-9_]{6,}\b|\bconversation_[a-z0-9_]{6,}\b"), "id"),
    "airtable_record": (re.compile(r"\bairtable_[a-f0-9]{12,16}\b"), "id"),
    "calendar_event": (re.compile(r"\bevent_[a-f0-9]{6,16}\b"), "id"),
    "slack_channel": (re.compile(r"\bC\d{3}\b"), "channel_id"),
    "contact": (re.compile(r"\bcontact_[a-f0-9]{8,16}\b"), "contact_id"),
    "persona": (re.compile(r"\bpersona_\d{3}\b"), "persona_id"),
}


def _money(val):
    if isinstance(val, bool):
        return None
    if isinstance(val, (int, float)):
        try:
            return str(Decimal(str(val)).quantize(Decimal("0.01")))
        except (InvalidOperation, ValueError):
            return None
    return None


def _weekday(date_str):
    try:
        return date.fromisoformat(date_str).strftime("%A")
    except ValueError:
        return None


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


def _collect(obj, emails, amounts, dates, depth=0):
    if depth > 8:
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            kl = str(k).lower()
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                if any(h in kl for h in MONEY_FIELD_HINTS):
                    m = _money(v)
                    if m is not None:
                        amounts.add(m)
            _collect(v, emails, amounts, dates, depth + 1)
    elif isinstance(obj, list):
        for x in obj:
            _collect(x, emails, amounts, dates, depth + 1)
    elif isinstance(obj, str):
        for em in EMAIL_RE.findall(obj):
            emails.add(em.lower())
        for d in ISO_DATE_RE.findall(obj):
            dates.add(d)


def load_records(split_dir):
    by_source = defaultdict(list)
    for p in split_dir.glob("*.json"):
        if p.name == "Universe_complete_data.json":
            continue
        src = p.stem
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if not isinstance(data, list):
            continue
        for rec in data:
            inner = parse_inner(rec)
            if inner is not None:
                by_source[src].append(inner)
    return by_source


def build_ledger(task_dir):
    split_dir = task_dir / "_aux" / "Universe_Split"
    if not split_dir.is_dir():
        raise SystemExit(f"ERROR: {split_dir} missing — run split_universe.py first")

    src_universe = task_dir / "3_UniverseDataForThisTask.json"
    src_hash = ""
    if src_universe.is_file():
        src_hash = hashlib.sha256(src_universe.read_bytes()).hexdigest()

    by_source = load_records(split_dir)

    emails = set()
    amounts = set()
    dates = set()
    ids = {k: set() for k in ID_PATTERNS}
    accounts_by_entity = defaultdict(dict)
    fiscal_periods = {}
    personas = {}
    aliases_first = defaultdict(set)
    aliases_last = defaultdict(set)
    aliases_full = defaultdict(set)
    entities = set()

    for src, rows in by_source.items():
        for inner in rows:
            _collect(inner, emails, amounts, dates)
            blob = json.dumps(inner, default=str)
            for kind, (pat, _key) in ID_PATTERNS.items():
                for m in pat.finditer(blob):
                    ids[kind].add(m.group(0))
            if isinstance(inner, dict) and inner.get("entity_id"):
                entities.add(str(inner["entity_id"]))

        if src.endswith("ogl_accounts"):
            for inner in rows:
                ent = inner.get("entity_id")
                num = inner.get("account_number") or inner.get("number")
                if ent and num:
                    name = inner.get("account_name") or inner.get("name") or ""
                    accounts_by_entity[str(ent)][str(num)] = name

        if src.endswith("ogl_fiscal_periods"):
            for inner in rows:
                pid = inner.get("id") or inner.get("period_id")
                if pid:
                    fiscal_periods[str(pid)] = {
                        "status": inner.get("status"),
                        "locked_at": inner.get("locked_at"),
                        "locked_by": inner.get("locked_by"),
                        "bd3_lock_at": inner.get("bd3_lock_at"),
                        "bd5_close_at": inner.get("bd5_close_at"),
                        "period_label": inner.get("period_label"),
                        "entity_id": inner.get("entity_id"),
                    }

        if src.endswith("contacts"):
            for inner in rows:
                email = (inner.get("email") or "").lower()
                if not email:
                    continue
                first = (inner.get("first_name") or "").strip()
                last = (inner.get("last_name") or "").strip()
                full = f"{first} {last}".strip()
                personas[email] = {
                    "name": full,
                    "title": inner.get("job") or inner.get("title") or "",
                    "is_user": bool(inner.get("is_user")),
                    "contact_id": inner.get("contact_id"),
                }
                if first:
                    aliases_first[first.lower()].add(email)
                if last:
                    aliases_last[last.lower()].add(email)
                if full:
                    aliases_full[full.lower()].add(email)

    dated = sorted(dates)
    dates_with_dow = [{"date": d, "day_of_week": _weekday(d)} for d in dated]

    EMPTY_IN_BASE_TABLE_SUFFIXES = {
        "linear_issues", "linear_projects", "linear_teams",
        "linear_comments", "linear_users", "linear_team_memberships",
        "threads", "mailboxes", "jmap_emails",
        "ogl_transactions",
        "blackline_sox_controls",
        "rv_chain_of_custody", "rv_legal_holds",
        "_changelog",
    }
    empty_in_base_populated_in_task = sorted(
        src for src in by_source
        if any(src.endswith(suffix) for suffix in EMPTY_IN_BASE_TABLE_SUFFIXES)
        and len(by_source[src]) > 0
    )

    ledger = {
        "meta": {
            "task_dir": str(task_dir.relative_to(task_dir.parent.parent)),
            "source_hash": src_hash,
            "record_count_by_source": {k: len(v) for k, v in by_source.items()},
            "atom_counts": {
                "emails": len(emails),
                "amounts": len(amounts),
                "dates": len(dates),
                **{f"id_{k}": len(v) for k, v in ids.items()},
                "entities": len(entities),
                "personas": len(personas),
                "fiscal_periods": len(fiscal_periods),
            },
        },
        "emails": sorted(emails),
        "amounts": sorted(amounts, key=lambda s: float(s) if s.replace(".", "").replace("-", "").isdigit() else 0),
        "dates": dates_with_dow,
        "ids": {k: sorted(v) for k, v in ids.items()},
        "entities": sorted(entities),
        "accounts_by_entity": {k: dict(v) for k, v in accounts_by_entity.items()},
        "fiscal_periods": fiscal_periods,
        "personas": personas,
        "aliases": {
            "first_name": {k: sorted(v) for k, v in aliases_first.items()},
            "last_name": {k: sorted(v) for k, v in aliases_last.items()},
            "full_name": {k: sorted(v) for k, v in aliases_full.items()},
        },
        "empty_in_base_tables_populated_in_task": empty_in_base_populated_in_task,
    }

    closed_periods_list = sorted(
        pid for pid, info in fiscal_periods.items()
        if isinstance(info, dict) and (info.get("status") or "").lower() in ("closed", "locked")
    )
    open_periods_list = sorted(
        pid for pid, info in fiscal_periods.items()
        if isinstance(info, dict) and (info.get("status") or "").lower() in ("open", "draft", "active")
    )
    today_str = None
    today_horizon_path = task_dir / "_aux" / "Universe_Index" / "today_horizon.json"
    if today_horizon_path.is_file():
        try:
            th = json.loads(today_horizon_path.read_text(encoding="utf-8"))
            today_str = th.get("today")
        except json.JSONDecodeError:
            pass
    ledger["lifecycle"] = {
        "today": today_str,
        "closed_periods": closed_periods_list,
        "open_periods": open_periods_list,
        "fiscal_periods_count": {
            "closed": len(closed_periods_list),
            "open": len(open_periods_list),
            "total": len(fiscal_periods),
        },
    }
    return ledger


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task_dir", help="path to Tasks/<TASK_DIR>")
    args = ap.parse_args()
    task_dir = Path(args.task_dir).resolve()
    if not task_dir.is_dir():
        print(f"ERROR: {task_dir} not a directory", file=sys.stderr)
        sys.exit(2)

    ledger = build_ledger(task_dir)
    out = task_dir / "_aux" / "Fact_Ledger.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(ledger, indent=2, default=str) + "\n", encoding="utf-8")

    counts = ledger["meta"]["atom_counts"]
    print(f"Wrote {out}")
    for k, v in counts.items():
        print(f"  {k:24s} {v:>6d}")


if __name__ == "__main__":
    main()
