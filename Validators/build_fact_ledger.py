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

try:
    from Validators.universes import detect_universe, get_universe_constants
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from universes import detect_universe, get_universe_constants

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

# StarPM (V4) ID shapes, selected when detect_universe() == "starpm". Brookfield,
# keystone and moveops keep ID_PATTERNS above (byte-identical); only starpm routes
# through these. Bare-hex gmail/contact ids are intentionally omitted (they over-
# collect); invoice DocNumbers are field-extracted below, not regex-scanned.
STARPM_ID_PATTERNS = {
    "airtable_record": (re.compile(r"\brec[a-f0-9]{14,16}\b"), "id"),
    "linear_issue": (re.compile(r"\bOPS-\d{1,4}\b"), "id"),
    "linear_comment": (re.compile(r"\bcomment_[a-f0-9]{32}\b"), "id"),
    "hubspot_object": (re.compile(r"\b(?:deal|contact|ticket|comp|engagement)_[a-z0-9]{6,40}\b"), "id"),
    "slack_channel": (re.compile(r"\bC\d{3}\b"), "channel_id"),
    "slack_user": (re.compile(r"\bU[A-Z0-9]{9,11}\b"), "user_id"),
}


# Re-derived 2026-08-03 from the HYDRATED Services_Data export, which is the id space
# these patterns are supposed to describe. The previous set was reverse-engineered from
# task text while the payload was un-hydrated, and four of the five were wrong against
# ground truth. Patterns are applied to json.dumps(row) below, which includes Slack
# message BODIES, so precision matters as much as recall: a loose pattern invents ids
# out of prose. Recall/FP below are measured over 586k Slack messages (681 MB) plus the
# users and channels tables; "FP" means matched-but-absent-from-the-owning-table, and
# every residual FP was hand-checked to be id-shaped (orphan references), not prose.
HARMONYGAMES_ID_PATTERNS = {
    # linear.issues.id: 3852 keys, prefixes ENG/ZOM/ART/DES/EPI. \d{2,5} missed the 12
    # single-digit keys (EPI-1..EPI-9, DES-4/7/9). Now 3852/3852. EVT and LATE are absent
    # from the export but occur in authored task text, so they stay in the alternation.
    "linear_issue":  (re.compile(r"\b(?:ENG|ZOM|EVT|DES|ART|EPI|LATE)-\d{1,5}\b"), "id"),
    # slack.channels.id: 985 ids - 385 C (channels) and 600 D (DMs), 11 AND 12 chars.
    # C[0-9A-Z]{10} caught 139/985. A bare [CD][0-9A-Z]{10,11} reaches 985 but drags in
    # 5715 FPs: uppercase UUID segments out of client_msg_id, and words like DRAMATICALLY
    # and CONFIDENTIAL. Requiring an embedded digit kills the words; refusing a hyphen or
    # word char on either side kills the UUID segments. Net: 985/985 recall, 62 FP - both
    # better than the pattern it replaces (139/985, 67 FP).
    "slack_channel": (re.compile(r"(?<![-0-9A-Za-z_])[CD](?=[0-9A-Z]*\d)[0-9A-Z]{10,11}(?![-0-9A-Za-z_])"), "channel_id"),
    # slack.users.id is TWO spaces, not one: 118 raw Slack ids (U + 8..10 chars, incl.
    # USLACKBOT which has no digit) and 100 opaque tokens in four families. Messages
    # reference users by the TOKEN form, so indexing only raw ids missed every message
    # author. The digit guard stops U-prefixed words like UNLIMITED. Now 218/218.
    "slack_user":    (re.compile(r"\b(?:U(?=[0-9A-Z]*\d)[0-9A-Z]{8,10}|USLACKBOT"
                                 r"|(?:PERSON|EMPLOYEE|SVC|SLACK)[A-Z_]*_\d{4}_SLACK_ID)\b"), "user_id"),
    # trello.cards.id: 803 ids, 24 hex chars. Already 803/803 - left alone.
    "trello_card":   (re.compile(r"\b[a-f0-9]{24}\b"), "id"),
    # gdrive.drive_files.id: 53702 ids, ALL `f_`/`d_` + 22 hex. The old Google-style
    # 1[A-Za-z0-9_-]{25,} matched 0 of them while inventing 73730 phantom ids from prose
    # slugs ("1-1-3-screenshot-1701735493647"). Now 53702/53702 with 0 FP.
    "gdrive_file":   (re.compile(r"\b[fd]_[0-9a-f]{22}\b"), "id"),
}

# Registry key `id_pattern_set` selects one; absence means the v3-family default.
ID_PATTERN_SETS = {
    "starpm": STARPM_ID_PATTERNS,
    "harmonygames": HARMONYGAMES_ID_PATTERNS,
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


def _persona_roster(consts):
    """The universe's declared persona roster, or [] when it declares none.

    Keyed off the existing `persona_acl_roster` registry entry rather than a
    `universe == "harmonygames"` branch, per the registry-over-branch rule in
    Validators/AGENTS.md. Only HarmonyGames declares it today.
    """
    rel = consts.get("persona_acl_roster")
    if not rel:
        return []
    p = Path(__file__).resolve().parent.parent / rel
    if not p.is_file():
        return []
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    return data if isinstance(data, list) else []


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

    universe = detect_universe(task_dir)
    consts = get_universe_constants(universe)
    active_id_patterns = ID_PATTERN_SETS.get(consts.get("id_pattern_set"), ID_PATTERNS)

    emails = set()
    amounts = set()
    dates = set()
    ids = {k: set() for k in active_id_patterns}
    if universe == "starpm":
        ids["invoice"] = set()
    accounts_by_entity = defaultdict(dict)
    fiscal_periods = {}
    personas = {}
    aliases_first = defaultdict(set)
    aliases_last = defaultdict(set)
    aliases_full = defaultdict(set)
    entities = set()

    # A declared persona roster is authoritative and is seeded BEFORE the data sweep, so a
    # contacts row cannot overwrite a persona's name or title. Only HarmonyGames declares
    # `persona_acl_roster`, so this is inert for the other four universes and their ledgers
    # are unchanged. It exists because HG persona identity is not derivable from the data:
    # AGENTS.md records this ledger reporting 0 personas against a 17-entry roster, and the
    # irregular addresses (`arthur_blake` -> `blake@`) mean a name cannot be turned into an
    # address either - the roster is the only correct source.
    roster_emails = set()
    for entry in _persona_roster(consts):
        email = (entry.get("email") or "").strip().lower()
        if not email:
            continue
        roster_emails.add(email)
        name = (entry.get("name") or "").strip()
        personas[email] = {
            "name": name,
            "title": entry.get("role") or "",
            "is_user": True,
            "contact_id": entry.get("persona_key"),
        }
        emails.add(email)
        parts = name.split()
        if parts:
            aliases_first[parts[0].lower()].add(email)
        if len(parts) > 1:
            aliases_last[parts[-1].lower()].add(email)
        if name:
            aliases_full[name.lower()].add(email)

    for src, rows in by_source.items():
        for inner in rows:
            _collect(inner, emails, amounts, dates)
            blob = json.dumps(inner, default=str)
            for kind, (pat, _key) in active_id_patterns.items():
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

        if universe == "starpm" and src.endswith("quickbooks_entities"):
            for inner in rows:
                if inner.get("entity_type") not in ("invoice", "bill", "credit_memo", "estimate"):
                    continue
                props = inner.get("properties")
                if isinstance(props, str):
                    try:
                        props = json.loads(props)
                    except json.JSONDecodeError:
                        props = {}
                if isinstance(props, dict):
                    docnum = props.get("DocNumber")
                    if docnum:
                        ids["invoice"].add(str(docnum))

        if src.endswith("contacts"):
            for inner in rows:
                email = (inner.get("email") or "").lower()
                if not email:
                    continue
                if roster_emails and "@" not in email:
                    # HarmonyGames' contacts table carries redacted placeholder tokens
                    # (`EMPLOYEE_0032_EMAIL`, `SVC_2796_EMAIL`) in the email column.
                    # Counting them made the ledger report 174 personas for a universe
                    # with a 17-entry roster - a number that looked like data and was not
                    # one. Gated on the roster so no other universe's ledger moves.
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
                # `personas` stays the superset it has always been: every identity the
                # data carries, with `is_user` distinguishing staff from NPCs. This is the
                # DECLARED subset, emitted separately so the roster count is assertable
                # without overloading a field four universes already depend on. Absent as
                # a key for universes that declare no roster, so their ledgers do not move.
                **({"personas_declared": len(roster_emails)} if roster_emails else {}),
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

    closed_words = consts.get("lifecycle_states_closed", {"closed", "locked"})
    open_words = consts.get("lifecycle_states_open", {"open", "draft", "active"})
    closed_periods_list = sorted(
        pid for pid, info in fiscal_periods.items()
        if isinstance(info, dict) and (info.get("status") or "").lower() in closed_words
    )
    open_periods_list = sorted(
        pid for pid, info in fiscal_periods.items()
        if isinstance(info, dict) and (info.get("status") or "").lower() in open_words
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
    # Refuse to build against an unresolvable universe. A failed split leaves an EMPTY
    # Universe_Split behind, so an is_dir() check passes and the builder writes an artifact
    # full of zeros that downstream phases then trust. ImportError is tolerated (the module
    # is optional); UniverseDataError is NOT swallowed.
    try:
        from universe_data_source import require_resolvable, UniverseDataError
    except ImportError:
        require_resolvable = None
    if require_resolvable is not None:
        try:
            require_resolvable(Path(task_dir))
        except UniverseDataError as _e:
            print(f"FAIL: {_e}", file=sys.stderr)
            return 1
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
    sys.exit(main() or 0)
