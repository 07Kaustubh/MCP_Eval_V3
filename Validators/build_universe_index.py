#!/usr/bin/env python3
"""
build_universe_index.py — build per-task summaries from Universe_Split/.

Record shape in Universe_Split: every JSON object has two top-level keys:
  - `source`: <service>.<table> string
  - `row_data`: JSON-encoded string of the actual row fields

Produces Tasks/<TASK_DIR>/_aux/Universe_Index/ with:
- service_inventory.md   record counts per service file
- entities_personas.md   personas + NPCs + contacts seen in this task
- key_facts.md           JE/recon/exception/AP/doc counts and states
- today_horizon.json     universe today + last_event_timestamp
- accounts_per_entity.md Oracle GL chart of accounts grouped by entity

Usage:
    python Validators/build_universe_index.py <path_to_task_dir>
"""

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

UNIVERSE_FIXED_TODAY_DEFAULT = "2026-06-12"

try:
    from Validators.universes import detect_universe, get_universe_constants
except ImportError:
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from universes import detect_universe, get_universe_constants


def resolve_universe_today(task_dir: Path) -> str:
    try:
        u = detect_universe(task_dir)
        return get_universe_constants(u).get("today", UNIVERSE_FIXED_TODAY_DEFAULT)
    except Exception:
        return UNIVERSE_FIXED_TODAY_DEFAULT


def load(path: Path):
    if not path.is_file():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def rows_of(path: Path):
    """Yield parsed inner row dicts from a Universe_Split JSON file."""
    raw = load(path)
    if not raw:
        return
    for rec in raw:
        rd = rec.get("row_data")
        if isinstance(rd, str):
            try:
                yield json.loads(rd)
            except json.JSONDecodeError:
                continue
        elif isinstance(rd, dict):
            yield rd
        elif isinstance(rec, dict):
            yield rec


def service_inventory(split_dir: Path, out: Path) -> None:
    rows = []
    for p in sorted(split_dir.glob("*.json")):
        if p.name == "Universe_complete_data.json":
            continue
        data = load(p)
        n = len(data) if isinstance(data, list) else "n/a"
        rows.append((p.stem, n))
    lines = ["# Service Inventory (per-task)", "", "| Source | Records |", "|---|---:|"]
    for name, n in rows:
        lines.append(f"| `{name}` | {n} |")
    lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")


def entities_personas(split_dir: Path, out: Path) -> None:
    rows = []
    seen = set()

    for d in rows_of(split_dir / "contacts.contacts.json"):
        email = d.get("email")
        name = " ".join(filter(None, [d.get("first_name"), d.get("last_name")])).strip() or d.get("display_name") or d.get("name")
        role = d.get("job") or d.get("job_title") or d.get("role")
        is_user = d.get("is_user")
        if email and email not in seen:
            seen.add(email)
            tag = "persona" if is_user else "npc"
            rows.append((name or "", email, role or "", tag))

    for d in rows_of(split_dir / "slack.slack_users.json"):
        prof = d.get("profile") if isinstance(d.get("profile"), dict) else {}
        email = d.get("email") or prof.get("email")
        name = d.get("real_name") or prof.get("real_name") or d.get("display_name") or d.get("name")
        if email and email not in seen:
            seen.add(email)
            rows.append((name or "", email, "slack-only", ""))

    rows.sort(key=lambda r: r[1])
    lines = [
        "# Entities and Personas (per-task)",
        "",
        f"Total unique emails: **{len(rows)}**",
        "",
        "| Name | Email | Role | Kind |",
        "|---|---|---|---|",
    ]
    for name, email, role, tag in rows:
        lines.append(f"| {name} | `{email}` | {role} | {tag} |")
    lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")


def key_facts(split_dir: Path, out: Path) -> None:
    lines = ["# Key Facts (per-task)", ""]

    jes = list(rows_of(split_dir / "oracle_gl.ogl_journal_entries.json"))
    if jes:
        by_status = Counter(j.get("status", "?") for j in jes)
        by_period = Counter(j.get("period_id", "?") for j in jes)
        lines += [
            "## Oracle GL Journal Entries",
            f"- Total JEs: **{len(jes)}**",
            "- By status: " + ", ".join(f"`{k}`={v}" for k, v in by_status.most_common()),
            "- Top 10 periods by JE count:",
        ]
        for p, n in by_period.most_common(10):
            lines.append(f"  - `{p}`: {n}")
        lines.append("")

    fps = list(rows_of(split_dir / "oracle_gl.ogl_fiscal_periods.json"))
    if fps:
        lines += ["## Fiscal Periods", "", "| period_id (=id) | status | locked_at | bd3_lock_at |", "|---|---|---|---|"]
        for d in sorted(fps, key=lambda r: r.get("id", "")):
            lines.append(
                f"| `{d.get('id','?')}` | {d.get('status','?')} | "
                f"{d.get('locked_at') or 'null'} | {d.get('bd3_lock_at') or 'null'} |"
            )
        lines.append("")

    excs = list(rows_of(split_dir / "blackline.blackline_exceptions.json"))
    if excs:
        by_state = Counter(e.get("state", "?") for e in excs)
        by_type = Counter(e.get("type", e.get("exception_type", "?")) for e in excs)
        lines += [
            "## BlackLine Exceptions",
            f"- Total: **{len(excs)}**",
            "- By state: " + ", ".join(f"`{k}`={v}" for k, v in by_state.most_common()),
            "- By type: " + ", ".join(f"`{k}`={v}" for k, v in by_type.most_common()),
            "",
        ]

    recs = list(rows_of(split_dir / "blackline.blackline_reconciliations.json"))
    if recs:
        by_state = Counter(r.get("state", "?") for r in recs)
        lines += [
            "## BlackLine Reconciliations",
            f"- Total: **{len(recs)}**",
            "- By state: " + ", ".join(f"`{k}`={v}" for k, v in by_state.most_common()),
            "",
        ]

    aps = list(rows_of(split_dir / "sap_subledger.ap_invoices.json"))
    if aps:
        by_status = Counter(a.get("status", "?") for a in aps)
        by_entity = Counter(a.get("entity_id", "?") for a in aps)
        lines += [
            "## SAP AP Invoices",
            f"- Total: **{len(aps)}**",
            "- By status: " + ", ".join(f"`{k}`={v}" for k, v in by_status.most_common()),
            "- By entity: " + ", ".join(f"`{k}`={v}" for k, v in by_entity.most_common()),
            "",
        ]

    docs = list(rows_of(split_dir / "records_vault.rv_documents.json"))
    if docs:
        by_class = Counter(d.get("classification", "?") for d in docs)
        by_ret = Counter(d.get("retention_policy_code", "?") for d in docs)
        by_kind = Counter(d.get("kind", "?") for d in docs)
        lines += [
            "## Records Vault Documents",
            f"- Total: **{len(docs)}**",
            "- By classification: " + ", ".join(f"`{k}`={v}" for k, v in by_class.most_common()),
            "- By retention code: " + ", ".join(f"`{k}`={v}" for k, v in by_ret.most_common()),
            "- Top 10 kinds: " + ", ".join(f"`{k}`={v}" for k, v in by_kind.most_common(10)),
            "",
        ]

    emails = list(rows_of(split_dir / "email.emails.json"))
    if emails:
        lines += [f"## Email Messages\n- Total: **{len(emails)}**\n"]

    msgs = list(rows_of(split_dir / "slack.slack_messages.json"))
    if msgs:
        by_channel = Counter(m.get("channel_id", m.get("channel", "?")) for m in msgs)
        lines += [
            "## Slack Messages",
            f"- Total: **{len(msgs)}**",
            "- Top 10 channels: " + ", ".join(f"`{k}`={v}" for k, v in by_channel.most_common(10)),
            "",
        ]

    issues = list(rows_of(split_dir / "linear.linear_issues.json"))
    if issues:
        by_state = Counter(i.get("state", i.get("status", "?")) for i in issues)
        lines += [
            "## Linear Issues",
            f"- Total: **{len(issues)}**",
            "- By state: " + ", ".join(f"`{k}`={v}" for k, v in by_state.most_common()),
            "",
        ]

    out.write_text("\n".join(lines), encoding="utf-8")


def today_horizon(split_dir: Path, out: Path, universe_today: str = UNIVERSE_FIXED_TODAY_DEFAULT) -> None:
    last_ts = None
    candidate_fields = ("posted_at", "created_at", "submitted_at", "approved_at", "timestamp", "due_date", "uploaded_at", "sent_at", "occurred_at", "ts", "filed_at", "completed_at")
    counter_post_today = 0
    cutoff = universe_today + "T23:59:59"

    for p in split_dir.glob("*.json"):
        if p.name == "Universe_complete_data.json":
            continue
        for d in rows_of(p):
            for fld in candidate_fields:
                v = d.get(fld)
                if not isinstance(v, str):
                    continue
                if not v[:10].replace("-", "").isdigit():
                    continue
                if last_ts is None or v > last_ts:
                    last_ts = v
                if v > cutoff:
                    counter_post_today += 1
                break

    data = {
        "universe_today": universe_today,
        "universe_timezone": "America/New_York",
        "last_event_timestamp_seen": last_ts,
        "records_dated_after_today": counter_post_today,
        "note": "Records after today are legitimate when status=future (fiscal periods) or upcoming due_dates (AP).",
    }
    out.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def accounts_per_entity(split_dir: Path, out: Path) -> None:
    accts = list(rows_of(split_dir / "oracle_gl.ogl_accounts.json"))
    if not accts:
        out.write_text("# Accounts per Entity (per-task)\n\n_No Oracle GL accounts present in this task._\n", encoding="utf-8")
        return
    by_entity = defaultdict(list)
    for d in accts:
        ent = d.get("entity_id", "?")
        num = d.get("account_number") or d.get("number") or "?"
        name = d.get("account_name") or d.get("name") or ""
        by_entity[ent].append((str(num), name))

    lines = ["# Accounts per Entity (per-task)", ""]
    for ent in sorted(by_entity):
        lines.append(f"## `{ent}`  ({len(by_entity[ent])} accounts)")
        lines.append("")
        lines.append("| Number | Name |")
        lines.append("|---|---|")
        for num, name in sorted(by_entity[ent], key=lambda t: t[0]):
            lines.append(f"| `{num}` | {name} |")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python Validators/build_universe_index.py <path_to_task_dir>", file=sys.stderr)
        sys.exit(1)
    task_dir = Path(sys.argv[1]).resolve()
    split_dir = task_dir / "_aux" / "Universe_Split"
    if not split_dir.is_dir():
        print(f"ERROR: {split_dir} not found. Run split_universe.py first.", file=sys.stderr)
        sys.exit(1)

    idx = task_dir / "_aux" / "Universe_Index"
    idx.mkdir(parents=True, exist_ok=True)

    service_inventory(split_dir, idx / "service_inventory.md")
    entities_personas(split_dir, idx / "entities_personas.md")
    key_facts(split_dir, idx / "key_facts.md")
    today_horizon(split_dir, idx / "today_horizon.json", universe_today=resolve_universe_today(task_dir))
    accounts_per_entity(split_dir, idx / "accounts_per_entity.md")

    print(f"Built Universe_Index at: {idx}")
    for p in sorted(idx.iterdir()):
        print(f"  {p.name}")


if __name__ == "__main__":
    main()
