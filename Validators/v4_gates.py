#!/usr/bin/env python3
"""V4-only validation phases: injection quality (Evals 0) and submission gate (Evals 5).

Both phases are framework-gated: they run only when the task's universe framework
profile lists them in extra_phases (v4 / starpm). For v3-family universes the phase
reports SKIP and exits clean, so legacy behavior is untouched.

Every deterministic check cites the eval rule it enforces, e.g. [Eval0 P3 TEMPORAL_VIOLATION].
Rules requiring semantic judgment are surfaced as COUNCIL notes, never silently dropped.
The enforcement audit mapping every eval mandate to a check id lives in
Validators/regression_baseline/V4_ENFORCEMENT_AUDIT.md.
"""
import json
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

WINDOW_START = date(2026, 5, 1)
WINDOW_END = date(2026, 7, 1)

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
ISO_DATE_RE = re.compile(r"\b(20\d{2})-(\d{2})-(\d{2})\b")
MONEY_RE = re.compile(r"\$[\d,]+(?:\.\d{2})?")
SLACK_CH_RE = re.compile(r"\bC0\d{2}\b")
EPOCH_TS_RE = re.compile(r"\b(1[6-9]\d{8})(?:\.\d+)?\b")
# ID-ish token: known starpm shapes observed in base data
ID_TOKEN_RE = re.compile(
    r"\b(?:rec[A-Z0-9][A-Za-z0-9]{4,}|tbl[A-Z0-9][A-Za-z0-9]{4,}|app[A-Z0-9][A-Za-z0-9]{4,}|viw[A-Z0-9][A-Za-z0-9]{4,}|"
    r"MT-2026-\d{2,4}|OPS-\d{1,5}|INV-[A-Z0-9-]{3,}|BILL-2026-\d{3,4}|QR-2026-\d{3,4}|"
    r"B-2026-\d{3,4}|EVF-2026-\d{2,4}|MR-[A-Z0-9-]{3,}|U0\d{2}|C0\d{2}|"
    r"deal_[A-Za-z0-9_]{3,}|cnt_[A-Za-z0-9_]{2,}|thr_[A-Za-z0-9_]{2,}|msg_[A-Za-z0-9_]{2,}|"
    r"iss_[A-Za-z0-9_]{2,}|evt_[A-Za-z0-9_]{2,}|inv_[A-Za-z0-9_]{2,}|p_\d{3})\b"
)
AI_TELL_PHRASES = [
    "i wanted to formally", "i wanted to circle back", "circle back on",
    "i hope this email finds you well", "i hope this finds you well",
    "please do not hesitate", "do not hesitate to reach out",
    "i wanted to bring to your attention", "i wanted to let you know that",
    "kindly ", "synergize", "per my last", "i trust this",
]
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF\u2705\u274C\u2764\uFE0F\u2728\u26A0]")
TOOL_OUTPUT_DEP_RE = re.compile(
    r"tool returned|returned success|response (?:shows|contains|includes)|"
    r"from the tool (?:output|response)|tool output|query returns|returns? (?:the|a) (?:list|value|result)|"
    r"confirm it was sent successfully|was sent successfully|delivered successfully",
    re.IGNORECASE,
)
PROCESS_GATE_RE = re.compile(
    r"\b(?:uses|calls|invokes|queries|searches|runs)\b.{0,40}\b(?:tool|search|list|query|api)\b",
    re.IGNORECASE,
)
INSERT_RE = re.compile(
    r"INSERT\s+INTO\s+([A-Za-z0-9_.\"]+)\s*\(([^)]*)\)\s*VALUES\s*(.+?);",
    re.IGNORECASE | re.DOTALL,
)
UPDATE_RE = re.compile(
    r"UPDATE\s+([A-Za-z0-9_.\"]+)\s+SET\s+(.+?)(?:WHERE\s+(.+?))?;",
    re.IGNORECASE | re.DOTALL,
)
STMT_SPLIT_RE = re.compile(r";\s*(?:\n|$)")


def _read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _split_tuples(values_blob: str):
    """Split a VALUES (...),(...) blob into per-row strings, quote-aware."""
    rows, depth, cur, in_str = [], 0, [], False
    i = 0
    while i < len(values_blob):
        ch = values_blob[i]
        if in_str:
            cur.append(ch)
            if ch == "'":
                if i + 1 < len(values_blob) and values_blob[i + 1] == "'":
                    cur.append("'")
                    i += 1
                else:
                    in_str = False
        else:
            if ch == "'":
                in_str = True
                cur.append(ch)
            elif ch == "(":
                depth += 1
                if depth == 1:
                    cur = []
                else:
                    cur.append(ch)
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    rows.append("".join(cur))
                else:
                    cur.append(ch)
            elif depth >= 1:
                cur.append(ch)
        i += 1
    return rows


def _split_row_values(row: str):
    vals, cur, in_str, depth = [], [], False, 0
    i = 0
    while i < len(row):
        ch = row[i]
        if in_str:
            cur.append(ch)
            if ch == "'":
                if i + 1 < len(row) and row[i + 1] == "'":
                    cur.append("'")
                    i += 1
                else:
                    in_str = False
        elif ch == "'":
            in_str = True
            cur.append(ch)
        elif ch == "(" :
            depth += 1
            cur.append(ch)
        elif ch == ")":
            depth -= 1
            cur.append(ch)
        elif ch == "," and depth == 0:
            vals.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
        i += 1
    if cur:
        vals.append("".join(cur).strip())
    return [v[1:-1].replace("''", "'") if len(v) >= 2 and v.startswith("'") and v.endswith("'") else v for v in vals]


def parse_inject_sql(sql_text: str):
    """Return (inserts, updates, errors). inserts: list of dicts {table, cols, rows:[{col:val}] , raw}."""
    inserts, updates, errors = [], [], []
    body = re.sub(r"--[^\n]*", "", sql_text)
    for m in INSERT_RE.finditer(body):
        table = m.group(1).strip().strip('"')
        cols = [c.strip().strip('"') for c in m.group(2).split(",") if c.strip()]
        rows = []
        for row_blob in _split_tuples(m.group(3)):
            vals = _split_row_values(row_blob)
            if len(vals) != len(cols):
                errors.append(f"table {table}: column/value count mismatch ({len(cols)} cols vs {len(vals)} values)")
                continue
            rows.append(dict(zip(cols, vals)))
        inserts.append({"table": table, "cols": cols, "rows": rows, "raw": m.group(0)})
    for m in UPDATE_RE.finditer(body):
        updates.append({"table": m.group(1).strip().strip('"'), "set": m.group(2), "where": m.group(3) or "", "raw": m.group(0)})
    stripped = re.sub(INSERT_RE, "", re.sub(UPDATE_RE, "", body))
    for stmt in STMT_SPLIT_RE.split(stripped):
        s = stmt.strip()
        if s and not s.upper().startswith(("BEGIN", "COMMIT", "SET ", "DELETE")) and ("INSERT" in s.upper() or "UPDATE" in s.upper() or "VALUES" in s.upper()):
            errors.append(f"unparseable statement fragment: {s[:100]}")
    return inserts, updates, errors


def _dates_in(text: str):
    out = []
    for m in ISO_DATE_RE.finditer(text):
        try:
            out.append((date(int(m.group(1)), int(m.group(2)), int(m.group(3))), m.group(0)))
        except ValueError:
            out.append((None, m.group(0)))
    for m in EPOCH_TS_RE.finditer(text):
        try:
            out.append((datetime.fromtimestamp(int(m.group(1)), tz=timezone.utc).date(), m.group(0)))
        except (ValueError, OverflowError):
            pass
    return out


def _text_fields(row: dict):
    for col, val in row.items():
        if isinstance(val, str) and len(val) > 40 and " " in val:
            if any(k in col.lower() for k in ("message", "body", "text", "note", "description", "content", "snippet", "subject", "comment")) or len(val) > 120:
                yield col, val


def _ai_tell_count(text: str) -> list:
    tells = []
    low = text.lower()
    for ph in AI_TELL_PHRASES:
        if ph in low:
            tells.append(f"phrase '{ph.strip()}'")
    if EMOJI_RE.search(text):
        tells.append("emoji in business comms")
    return tells


def _rubric_atoms(rubrics) -> set:
    atoms = set()
    for r in rubrics:
        blob = " ".join(str(r.get(k, "")) for k in ("title", "criterion", "justification", "evidence"))
        atoms.update(MONEY_RE.findall(blob))
        atoms.update(ID_TOKEN_RE.findall(blob))
        atoms.update(EMAIL_RE.findall(blob))
    return atoms


def load_rubrics(task_dir: Path):
    p = task_dir / "7_Rubrics.json"
    if not p.is_file():
        return None
    try:
        data = json.loads(_read(p))
    except json.JSONDecodeError:
        return None
    if isinstance(data, dict):
        for key in ("rubrics", "criteria", "items"):
            if isinstance(data.get(key), list):
                return data[key]
        return None
    return data if isinstance(data, list) else None


def validate_injection(task_dir: Path, rep, universe: str, consts: dict, profile: dict) -> bool:
    """Returns True if phase ran, False if skipped (non-v4 framework)."""
    if "injection" not in profile.get("extra_phases", ()):
        rep.note(f"SKIP: injection phase not applicable to universe '{universe}' (framework {profile.get('framework_version', 'v3')}); v4-only gate")
        return False

    sql_path = task_dir / "9_Universe_inject.sql"
    chg_path = task_dir / "4_Changelog.json"
    uni_path = task_dir / "3_UniverseDataForThisTask.json"
    base_text = _read(uni_path)
    prompt_text = _read(task_dir / "5_Prompt.txt")
    rubrics = load_rubrics(task_dir) or []

    # P1 Schema & Structural (HARD GATE)  [Eval0 P1 SCHEMA_VIOLATION]
    sql_text = _read(sql_path)
    inserts, updates, errors = parse_inject_sql(sql_text) if sql_text.strip() else ([], [], [])
    for e in errors:
        rep.fail(f"[Eval0 P1 SCHEMA_VIOLATION] {e}")
    changelog = None
    if chg_path.is_file():
        try:
            changelog = json.loads(_read(chg_path))
        except json.JSONDecodeError as e:
            rep.fail(f"[Eval0 P1 SCHEMA_VIOLATION] 4_Changelog.json is not valid JSON: {e}")
    else:
        rep.warn("[Eval0 P1] 4_Changelog.json missing (V4 task shape expects it)")
    if not sql_text.strip():
        rep.warn("[Eval0 P1] 9_Universe_inject.sql missing or empty - no injection declared; remaining gates evaluate the empty set")
    if changelog is not None and not isinstance(changelog, (list, dict)):
        rep.fail("[Eval0 P1 SCHEMA_VIOLATION] 4_Changelog.json must be a JSON array or object")

    base_ids = set(ID_TOKEN_RE.findall(base_text))
    base_emails = set(e.lower() for e in EMAIL_RE.findall(base_text))
    personas = {e.lower() for e in (consts.get("personas") or {})} if isinstance(consts.get("personas"), dict) else set()
    valid_channels = set()
    for ch in (consts.get("slack_channels") or {}):
        valid_channels.add(ch if isinstance(ch, str) else str(ch))
    domain = consts.get("persona_email_domain", "starpm.com")

    injected_ids, injected_emails, all_rows = set(), set(), []
    for ins in inserts:
        for row in ins["rows"]:
            all_rows.append((ins["table"], row))
            blob = " ".join(str(v) for v in row.values())
            injected_ids.update(ID_TOKEN_RE.findall(blob))
            injected_emails.update(e.lower() for e in EMAIL_RE.findall(blob))

    # P2 ID format  [Eval0 P2 ID_VIOLATION]
    for table, row in all_rows:
        for col, val in row.items():
            if col.lower() in ("id",) or col.lower().endswith("_id"):
                sval = str(val).strip()
                if sval and sval.upper() not in ("NULL", "DEFAULT") and not sval.isdigit():
                    if not ID_TOKEN_RE.fullmatch(sval) and not EMAIL_RE.fullmatch(sval):
                        rep.fail(f"[Eval0 P2 ID_VIOLATION] {table}.{col} = '{sval}' does not match any StarPM ID convention observed in the base universe")

    # P3 dates  [Eval0 P3 TEMPORAL_VIOLATION]
    for table, row in all_rows:
        blob = " ".join(f"{c}={v}" for c, v in row.items())
        for d, raw in _dates_in(blob):
            if d is None:
                rep.fail(f"[Eval0 P3 TEMPORAL_VIOLATION] {table}: invalid calendar date '{raw}'")
            elif not (WINDOW_START <= d <= WINDOW_END):
                rep.fail(f"[Eval0 P3 TEMPORAL_VIOLATION] {table}: injected date {raw} outside universe window {WINDOW_START}..{WINDOW_END} (today = {WINDOW_END})")
    for upd in updates:
        for d, raw in _dates_in(upd["set"]):
            if d is not None and not (WINDOW_START <= d <= WINDOW_END):
                rep.fail(f"[Eval0 P3 TEMPORAL_VIOLATION] UPDATE {upd['table']}: date {raw} outside window {WINDOW_START}..{WINDOW_END}")

    # P4 integrity & cross-service  [Eval0 P4]
    for table, row in all_rows:
        for col, val in row.items():
            # own primary key only; *_id columns are foreign keys and SHOULD reference existing records
            if col.lower() == "id" and str(val) in base_ids:
                rep.fail(f"[Eval0 P4 COLLISION] {table}.{col} '{val}' already exists in the base universe (record collision)")
    for table, row in all_rows:
        blob = " ".join(str(v) for v in row.values())
        for ref in ID_TOKEN_RE.findall(blob):
            if ref not in base_ids and ref not in injected_ids:
                rep.fail(f"[Eval0 P4 CROSS_SERVICE_VIOLATION] {table}: broken cross-reference '{ref}' - not found in base universe or injection")
        for ch in SLACK_CH_RE.findall(blob):
            if valid_channels and ch not in valid_channels:
                rep.fail(f"[Eval0 P4 CROSS_SERVICE_VIOLATION] {table}: slack channel {ch} is not a valid {universe} channel ({sorted(valid_channels)[0]}..{sorted(valid_channels)[-1]})")
    for em in sorted(injected_emails):
        if em.endswith("@" + domain) and personas and em not in personas and em not in base_emails:
            rep.fail(f"[Eval0 P4 CROSS_SERVICE_VIOLATION] injected @{domain} address '{em}' matches no persona or base-universe mailbox (email format mismatch)")
    rep.note("[Eval0 P4] COUNCIL: fact/status/amount/timeline contradiction review vs base universe requires semantic judgment - deterministic layer covers collisions, broken refs, channel validity, mailbox validity")

    # P5 naturalness  [Eval0 P5 AI_TELL]
    telling_fields = 0
    for table, row in all_rows:
        for col, val in _text_fields(row):
            tells = _ai_tell_count(val)
            if tells:
                telling_fields += 1
                rep.warn(f"[Eval0 P5 AI_TELL] {table}.{col}: {', '.join(tells)}")
    if telling_fields >= 3:
        rep.fail(f"[Eval0 P5 AI_TELL] {telling_fields} injected text fields show AI-generation patterns (3+ = FAIL per counting rule)")
    rep.note("[Eval0 P5] COUNCIL: formality/length/register match vs channel norms requires semantic judgment - deterministic layer counts phrase/emoji tells")

    # P6 reachability  [Eval0 P6 ORPHANED]
    prompt_atoms = set(ID_TOKEN_RE.findall(prompt_text)) | {e.lower() for e in EMAIL_RE.findall(prompt_text)}
    for ins in inserts:
        for row in ins["rows"]:
            blob = " ".join(str(v) for v in row.values())
            row_atoms = set(ID_TOKEN_RE.findall(blob)) | {e.lower() for e in EMAIL_RE.findall(blob)}
            anchored = bool(row_atoms & (base_ids | base_emails | prompt_atoms)) or bool((row_atoms - {next(iter(row_atoms))} if row_atoms else set()) & injected_ids)
            if row_atoms and not anchored and not (row_atoms & injected_ids or row_atoms & injected_emails):
                rep.fail(f"[Eval0 P6 ORPHANED] {ins['table']} row shares no identifier/email with base universe, prompt, or other injected rows - no discovery path")
    rep.note("[Eval0 P6] COUNCIL: tool-call chain depth (>5 calls) requires tool-surface simulation - deterministic layer verifies atom anchoring")

    # P7 pre-solve  [Eval0 P7 PRE_SOLVED]
    expected = _rubric_atoms(rubrics)
    for table, row in all_rows:
        for col, val in _text_fields(row):
            hits = {a for a in expected if a in val}
            if len(hits) >= 3:
                rep.fail(f"[Eval0 P7 PRE_SOLVED] {table}.{col} contains {len(hits)} rubric-expected values verbatim ({', '.join(sorted(hits)[:4])}) - single record hands the agent the answer")
            elif len(hits) == 2:
                rep.warn(f"[Eval0 P7] {table}.{col} concentrates 2 rubric-expected values ({', '.join(sorted(hits))}) - verify signal is scattered")
    rep.note("[Eval0 P8] COUNCIL: injection difficulty/complexity composite (minimum 3.5) requires semantic scoring - not deterministically checkable")
    return True


def validate_submission_gate(task_dir: Path, rep, universe: str, consts: dict, profile: dict) -> bool:
    if "submission_gate" not in profile.get("extra_phases", ()):
        rep.note(f"SKIP: submission_gate phase not applicable to universe '{universe}' (framework {profile.get('framework_version', 'v3')}); v4-only gate")
        return False

    prompt_text = _read(task_dir / "5_Prompt.txt")
    oe_text = _read(task_dir / "6_Oracle_Events.txt")
    persona_text = _read(task_dir / "2_Persona.txt")
    base_text = _read(task_dir / "3_UniverseDataForThisTask.json")
    inject_text = _read(task_dir / "9_Universe_inject.sql")
    rubrics = load_rubrics(task_dir)
    if rubrics is None:
        rep.fail("[Eval5 P0] 7_Rubrics.json missing or unparseable - cannot run submission gate")
        return True

    # tool catalog (universe SSOT)
    tool_names = set()
    cat_path = ROOT / consts.get("tool_catalog", "")
    if cat_path.is_file():
        try:
            cat = json.loads(_read(cat_path))
            def _collect(obj):
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        if k in ("name", "tool_name") and isinstance(v, str):
                            tool_names.add(v)
                        _collect(v)
                elif isinstance(obj, list):
                    for it in obj:
                        _collect(it)
            _collect(cat)
        except json.JSONDecodeError:
            rep.warn("[Eval5 P1] tool catalog unparseable - F1 tool cross-ref degraded")
    services = set(consts.get("services", []))
    searchable = base_text + "\n" + inject_text + "\n" + oe_text
    domain = consts.get("persona_email_domain", "starpm.com")
    personas = {e.lower() for e in (consts.get("personas") or {})} if isinstance(consts.get("personas"), dict) else set()

    SERVICE_PREFIX_RE = re.compile(r"\b(?:slack|gmail|airtable|linear|hubspot|quickbooks|gcalendar|contacts|crm|stripe|oracle_gl|sap|blackline)_[a-z_]{3,}\b")
    blank_fields = 0
    for idx, r in enumerate(rubrics, 1):
        title = str(r.get("title", r.get("criterion", "")))
        cat = str(r.get("category", "")).lower()
        just = str(r.get("justification", ""))
        evid = str(r.get("evidence", ""))
        blob = " ".join((title, just, evid))

        # F6.5 blank fields  [Eval5 P6 6.5 BLANK_FIELD]
        for fname, fval in (("title/criterion", title), ("category", cat), ("justification", just), ("evidence", evid)):
            if not fval.strip():
                rep.fail(f"[Eval5 P6 6.5 BLANK_FIELD] rubric #{idx}: blank {fname}")
                blank_fields += 1

        # F1 impossible-with-tools  [Eval5 P1 IMPOSSIBLE]
        for tok in SERVICE_PREFIX_RE.findall(blob):
            if tool_names and tok not in tool_names:
                rep.fail(f"[Eval5 P1 IMPOSSIBLE] rubric #{idx} references tool '{tok}' which does not exist in the {universe} tool catalog")
        for svc in re.findall(r"\b(oracle_gl|sap_subledger|blackline|records_vault|mortgage_los|stripe|filesystem)\b", blob):
            if svc not in services:
                rep.fail(f"[Eval5 P1 IMPOSSIBLE] rubric #{idx} references service '{svc}' which is not in the {universe} service set")

        # F2 persona/date  [Eval5 P2]
        for d, raw in _dates_in(title + " " + evid):
            if d is not None and not (WINDOW_START - timedelta(days=365) <= d <= WINDOW_END):
                rep.fail(f"[Eval5 P2 MISMATCH] rubric #{idx} references date {raw} after universe today ({WINDOW_END}) - future-dated expectation")

        # F2 phantom refs  [Eval5 P2 PHANTOM]
        for ref in set(ID_TOKEN_RE.findall(blob)):
            if ref not in searchable:
                rep.fail(f"[Eval5 P2 PHANTOM] rubric #{idx} cites '{ref}' which appears nowhere in universe data, injection, or OEs")
        for em in set(e.lower() for e in EMAIL_RE.findall(blob)):
            if em.endswith("@" + domain) and personas and em not in personas and em not in searchable.lower():
                rep.fail(f"[Eval5 P2 PHANTOM] rubric #{idx} cites persona address '{em}' matching no {universe} persona or universe mailbox")

        # F3 process gates  [Eval5 P3 TOOL_GATE/QUERY_GATE]
        if cat == "process" and PROCESS_GATE_RE.search(title):
            rep.fail(f"[Eval5 P3 TOOL_GATE] process rubric #{idx} credits tool-calling motions ('{title[:80]}') instead of a verification outcome")

        # F4 broken rubric: expected value absent from SSOT  [Eval5 P4 BROKEN]
        for amt in set(MONEY_RE.findall(title)):
            if amt not in searchable:
                rep.fail(f"[Eval5 P4 BROKEN] rubric #{idx} expects amount {amt} which does not exist in universe data, injection, or OEs")

        # F5 illegal tool-output dependency  [Eval5 P5 NEEDS_TOOL_OUTPUT]
        m = TOOL_OUTPUT_DEP_RE.search(blob)
        if m:
            rep.fail(f"[Eval5 P5 NEEDS_TOOL_OUTPUT] rubric #{idx} grading depends on tool output ('{m.group(0)}') which the judge cannot see in call arguments")

        # F6.1 atomicity  [Eval5 P6 6.1 NOT_ATOMIC]
        value_atoms = set(MONEY_RE.findall(title)) | set(ID_TOKEN_RE.findall(title)) | set(EMAIL_RE.findall(title))
        if len(value_atoms) >= 2 and re.search(r"\band\b", title):
            rep.warn(f"[Eval5 P6 6.1 NOT_ATOMIC] rubric #{idx} bundles {len(value_atoms)} independently-verifiable values with 'and' - split candidate (COUNCIL confirms)")

    # F6.4 destination consistency  [Eval5 P6 6.4 WRONG_DESTINATION]
    prompt_channels = set(SLACK_CH_RE.findall(prompt_text)) | set(re.findall(r"#[a-z][a-z0-9-]{2,}", prompt_text))
    rubric_blob = " ".join(" ".join(str(r.get(k, "")) for k in ("title", "justification", "evidence")) for r in rubrics)
    rubric_channels = set(SLACK_CH_RE.findall(rubric_blob)) | set(re.findall(r"#[a-z][a-z0-9-]{2,}", rubric_blob))
    if prompt_channels and rubric_channels and not (prompt_channels & rubric_channels):
        rep.fail(f"[Eval5 P6 6.4 WRONG_DESTINATION] prompt names destination(s) {sorted(prompt_channels)} but rubrics check {sorted(rubric_channels)} - artifact mismatch")

    # F6.7 delegation clarity  [Eval5 P6 6.7 DELEGATION_AMBIGUITY]
    if re.search(r"\bI'?ll\s+\w+|\bI will\s+\w+", prompt_text) and re.search(r"^(?:Please\s+)?(?:send|create|update|draft|post|prepare|compile|schedule)\b", prompt_text, re.IGNORECASE | re.MULTILINE):
        rep.warn("[Eval5 P6 6.7 DELEGATION_AMBIGUITY] prompt mixes 'I'll [verb]' with agent imperatives - COUNCIL: confirm who acts on each deliverable")

    # F6.2 forward coverage  [Eval5 P6 6.2 MISSING_CRITERIA]
    outcome_count = sum(1 for r in rubrics if str(r.get("category", "")).lower() == "outcome")
    process_count = sum(1 for r in rubrics if str(r.get("category", "")).lower() == "process")
    if outcome_count == 0:
        rep.fail("[Eval5 P6 6.2 MISSING_CRITERIA] zero Outcome rubrics - every deliverable is uncovered")
    if rubrics and process_count > outcome_count:
        rep.fail(f"[Eval5 P3] Process rubrics ({process_count}) outnumber Outcome rubrics ({outcome_count}) - violates outcome-first mandate")
    rep.note(f"[Eval5 P7] rubric census: {outcome_count} outcome / {process_count} process / {len(rubrics)} total")
    rep.note("[Eval5 P6] COUNCIL: under-strictness (6.3), exclusion coverage (6.6), UGT convergence (6.8), OE authority (6.9), strict feasibility (6.10), date-alignment ambiguity (6.11) require semantic judgment - flagged for council review")
    return True
