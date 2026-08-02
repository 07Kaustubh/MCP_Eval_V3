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
from functools import lru_cache
from pathlib import Path
from decimal import Decimal, InvalidOperation

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
V3_ID_TOKEN_RE = re.compile(
    r"\b(?:JE-[A-Z0-9-]{4,}|BL-[A-F0-9]{8,}|exc_[a-z0-9_]{4,}|doc_[a-f0-9]{8,}|"
    r"email_scen_[a-z0-9_]{6,}|scenario_[a-f0-9]{6,}|FP-20\d{2}-\d{2}|"
    r"ap_inv_[a-z0-9_]{4,}|recon_[a-z0-9_]{4,}|vend_[a-z0-9_]{3,}|LN-20\d{2}-\d{4,}|"
    r"rec[A-Z0-9][A-Za-z0-9]{4,}|tbl[A-Z0-9][A-Za-z0-9]{4,}|C0\d{2}|U0\d{2}|p_\d{3})\b"
)


# HarmonyGames opaque identifiers, measured in QC_Tasks/V5_HG_Buckets. Team-prefixed
# Linear keys (ENG-2400) are human-speakable and are deliberately NOT treated as opaque.
HG_ID_TOKEN_RE = re.compile(
    r"\b(?:C[0-9A-Z]{10}|U[0-9A-Z]{10}|[a-f0-9]{24}|1[A-Za-z0-9_-]{25,}|"
    r"(?:ENG|ZOM|EVT|DES|ART|EPI|LATE)-\d{2,5})\b"
)


def id_token_re_for(universe: str):
    """Per-universe identifier shapes. Keyed off the registry, not a name comparison."""
    from universes import get_universe_constants
    pset = (get_universe_constants(universe) or {}).get("id_pattern_set")
    if pset == "starpm":
        return ID_TOKEN_RE
    if pset == "harmonygames":
        return HG_ID_TOKEN_RE
    return V3_ID_TOKEN_RE


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
DELETE_RE = re.compile(
    r"DELETE\s+FROM\s+([A-Za-z0-9_.\"]+)(?:\s+WHERE\s+(.+?))?;",
    re.IGNORECASE | re.DOTALL)
STMT_SPLIT_RE = re.compile(r";\s*(?:\n|$)")


# --- money + calendar-create helpers (F4 normalization + F2 write-target exemption) ---
def _canonical_amount(raw: str):
    # normalize a money token to a 2dp Decimal string, or None if unparseable
    s = raw.replace("$", "").replace(",", "").strip()
    try:
        return str(Decimal(s).quantize(Decimal("0.01"))) if s else None
    except (InvalidOperation, ValueError):
        return None


# money-shaped tokens only: carry a $, a thousands-comma group, or a decimal point;
# deliberately excludes bare integers so record ids / counts cannot create phantom matches.
_SEARCH_MONEY_RE = re.compile(r"\$\s?[\d,]+(?:\.\d+)?|\b\d{1,3}(?:,\d{3})+(?:\.\d+)?\b|\b\d+\.\d+\b")


def _searchable_amounts(text: str) -> set:
    # canonical 2dp amount set from money-shaped tokens in the SSOT text
    out = set()
    for m in _SEARCH_MONEY_RE.finditer(text):
        c = _canonical_amount(m.group(0))
        if c:
            out.add(c)
    return out


def _derived_from_amounts(target: str, pool: set, context: str) -> str:
    """Return a shown derivation of `target`, or "" if the rubric does not show one.

    A rubric amount may legitimately be arithmetic OVER universe values rather than a
    literal universe string, and the framework treats that as the model case rather than a
    defect. `Docs*/2_Rubrics_V3_Guidelines.md` gives as its worked example of a GOOD
    outcome rubric "The Agent identifies a $264 overcharge on the Flores file, the
    difference between the $792 Stripe charge and the $528 closing disclosure amount", and
    says plainly: "$264 is derived math." $264 appears nowhere in that universe, so a flat
    membership test marks the guidelines' own exemplar BROKEN.

    The components must come from the RUBRIC'S OWN justification and evidence, not from
    the whole universe. Searching the universe pool was measured at 43 percent acceptance
    on randomly fabricated amounts (1513 amounts admit a two-term sum for almost anything),
    which is not a gate. Requiring the rubric to SHOW its arithmetic, with every component
    independently present in the universe, is both tighter and the thing a reviewer wants:
    an aggregate that cannot name its parts is indistinguishable from a fabricated one.
    """
    try:
        t_val = Decimal(target)
    except (InvalidOperation, ValueError):
        return ""
    comps = []
    for m in _SEARCH_MONEY_RE.finditer(context or ""):
        c = _canonical_amount(m.group(0))
        if not c or c not in pool:
            continue
        try:
            d = Decimal(c)
        except (InvalidOperation, ValueError):
            continue
        if d > 0 and d != t_val:
            comps.append(d)
    comps = sorted(set(comps))

    # Difference of two shown components. This is the case the docstring's exemplar needs: the
    # guidelines' $264 overcharge is $792 minus $528, and BOTH components exceed the target, so any
    # upper filter on component size rejects the very example this function exists to accept.
    n = len(comps)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(comps[i] - comps[j]) == t_val:
                hi, lo = max(comps[i], comps[j]), min(comps[i], comps[j])
                return f"{hi} - {lo}"

    # Sums of two to four shown components. Only components smaller than the target can be addends.
    addends = [d for d in comps if d < t_val]
    n = len(addends)
    for i in range(n):
        for j in range(i + 1, n):
            if addends[i] + addends[j] == t_val:
                return f"{addends[i]} + {addends[j]}"
            for k in range(j + 1, n):
                s3 = addends[i] + addends[j] + addends[k]
                if s3 == t_val:
                    return f"{addends[i]} + {addends[j]} + {addends[k]}"
                if s3 > t_val:
                    break
                for l in range(k + 1, n):
                    if s3 + addends[l] == t_val:
                        return f"{addends[i]} + {addends[j]} + {addends[k]} + {addends[l]}"
                    if s3 + addends[l] > t_val:
                        break
    return ""


# F2 write-target exemption: prompt asked for a calendar/reminder create, the rubric is
# calendar-create-shaped, and the date is near-term (WINDOW_END + 31d).
_PROMPT_SCHED_RE = re.compile(r"\b(remind(?:er)?|calendar|schedule|follow[\s-]?up|come back|revisit|next week|next month)\b", re.IGNORECASE)
_CAL_RUBRIC_RE = re.compile(r"\b(calendar|reminder|gcalendar|create[_\s]?event|save[_\s]?event|schedule|follow[\s-]?up|revisit|come back)\b", re.IGNORECASE)
_NEAR_FUTURE_HI = WINDOW_END + timedelta(days=31)

# F2 future-as-future exemption. Evals_starpm/5 Phase 2 (~L146) defines the F2 date defect
# as future-AS-PAST: a rubric that treats a not-yet-happened event as already analyzed
# (announces its outcome). A rubric that EXPLICITLY states a grounded future event has NOT
# yet happened is the spec-correct opposite (and is exactly what the F9 net rewards when an
# OE cites the date). Downgrade those from FAIL to a COUNCIL NOTE so a confirmed pending
# event can be flagged as pending without a false MISMATCH.
_FUTURE_ACK_RE = re.compile(
    r"\bnot yet (?:occurred|happened|taken place|performed|done|completed|conducted)\b|"
    r"\bstill (?:pending|upcoming|outstanding|open)\b|"
    r"\byet to (?:occur|happen|take place|be (?:done|performed|completed))\b|"
    r"\bremains? (?:pending|upcoming|outstanding|open)\b|"
    r"\b(?:is|are) (?:still )?upcoming\b",
    re.IGNORECASE,
)


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
    # v22: DELETE was previously excluded from the skip-list check, which meant a
    # DELETE against a base-universe row was parsed by nothing and reported by nothing,
    # while AGENTS.md rule 4 states base universe rows are "never modified or deleted".
    # Capture them so validate_injection can fail on them.
    deletes = []
    for m in DELETE_RE.finditer(body):
        deletes.append({"table": m.group(1).strip().strip('"'), "where": m.group(2) or "", "raw": m.group(0)})
    stripped = re.sub(INSERT_RE, "", re.sub(UPDATE_RE, "", re.sub(DELETE_RE, "", body)))
    for stmt in STMT_SPLIT_RE.split(stripped):
        s = stmt.strip()
        if s and not s.upper().startswith(("BEGIN", "COMMIT", "SET ")) and ("INSERT" in s.upper() or "UPDATE" in s.upper() or "DELETE" in s.upper() or "VALUES" in s.upper()):
            errors.append(f"unparseable statement fragment: {s[:100]}")
    return inserts, updates, deletes, errors


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
    sql_path = task_dir / "9_Universe_inject.sql"
    is_v4 = "injection" in profile.get("extra_phases", ())
    # "declared" means the file carries executable statements, not just the template's comment header
    _sql_raw = sql_path.read_text(encoding="utf-8", errors="replace") if sql_path.is_file() else ""
    _sql_body = re.sub(r"--[^\n]*", "", _sql_raw)
    has_sql = bool(re.search(r"\b(?:INSERT|UPDATE|DELETE)\b", _sql_body, re.IGNORECASE))
    if not is_v4 and not has_sql:
        rep.note(f"SKIP: no injection declared for universe '{universe}' (9_Universe_inject.sql absent or empty); "
                 f"injection validation runs whenever an inject file is present - all universes ship it in Tasks_Template")
        return False
    chg_path = task_dir / "4_Changelog.json"
    uni_path = task_dir / "3_UniverseDataForThisTask.json"
    base_text = _read(uni_path)
    prompt_text = _read(task_dir / "5_Prompt.txt")
    rubrics = load_rubrics(task_dir) or []

    # P1 Schema & Structural (HARD GATE)  [Eval0 P1 SCHEMA_VIOLATION]
    sql_text = _read(sql_path)
    inserts, updates, deletes, errors = parse_inject_sql(sql_text) if sql_text.strip() else ([], [], [], [])
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

    tok_re = id_token_re_for(universe)
    base_ids = set(tok_re.findall(base_text))
    base_emails = set(e.lower() for e in EMAIL_RE.findall(base_text))
    personas = {e.lower() for e in (consts.get("personas") or {})} if isinstance(consts.get("personas"), dict) else set()
    npc_mailboxes = {e.lower() for e in (consts.get("npcs") or set()) if isinstance(e, str) and "@" in e}
    valid_channels = set()
    for ch in (consts.get("slack_channels") or {}):
        valid_channels.add(ch if isinstance(ch, str) else str(ch))
    domain = consts.get("persona_email_domain", "starpm.com")

    injected_ids, injected_emails, all_rows = set(), set(), []
    for ins in inserts:
        for row in ins["rows"]:
            all_rows.append((ins["table"], row))
            blob = " ".join(str(v) for v in row.values())
            injected_ids.update(tok_re.findall(blob))
            injected_emails.update(e.lower() for e in EMAIL_RE.findall(blob))

    # P2 ID format  [Eval0 P2 ID_VIOLATION] - convention catalog exists only for starpm (v4);
    # v3-family conventions vary per service, covered by collision/cross-ref checks instead
    for table, row in (all_rows if is_v4 else []):
        for col, val in row.items():
            if col.lower() in ("id",) or col.lower().endswith("_id"):
                sval = str(val).strip()
                if sval and sval.upper() not in ("NULL", "DEFAULT") and not sval.isdigit():
                    if not ID_TOKEN_RE.fullmatch(sval) and not EMAIL_RE.fullmatch(sval):
                        rep.fail(f"[Eval0 P2 ID_VIOLATION] {table}.{col} = '{sval}' does not match any StarPM ID convention observed in the base universe")

    # P3 dates  [Eval0 P3 TEMPORAL_VIOLATION]
    # V4 (starpm): fixed active window. V3-family: ceiling = universe today from the registry
    # (future-dated injections are wrong in every universe); no lower bound.
    if is_v4:
        win_lo, win_hi = WINDOW_START, WINDOW_END
    else:
        try:
            t = consts.get("today", "")
            win_hi = date(int(t[0:4]), int(t[5:7]), int(t[8:10])) if t else WINDOW_END
        except (ValueError, TypeError):
            win_hi = WINDOW_END
        win_lo = date(2000, 1, 1)
    for table, row in all_rows:
        blob = " ".join(f"{c}={v}" for c, v in row.items())
        for d, raw in _dates_in(blob):
            if d is None:
                rep.fail(f"[Eval0 P3 TEMPORAL_VIOLATION] {table}: invalid calendar date '{raw}'")
            elif not (win_lo <= d <= win_hi):
                rep.fail(f"[Eval0 P3 TEMPORAL_VIOLATION] {table}: injected date {raw} outside universe window {win_lo}..{win_hi} (universe today = {win_hi})")
    for upd in updates:
        for d, raw in _dates_in(upd["set"]):
            if d is not None and not (win_lo <= d <= win_hi):
                rep.fail(f"[Eval0 P3 TEMPORAL_VIOLATION] UPDATE {upd['table']}: date {raw} outside window {win_lo}..{win_hi}")

    # P4a base-universe immutability  [Eval0 P4 / AGENTS.md rule 4]
    # Rule 4: "base universe rows are never modified or deleted, and every injection must
    # clear validate.py --phase injection". Injection ADDS scenario data. Upstream Eval0
    # contemplates update/delete operations (P0.7, P4.1), so this repo is deliberately
    # STRICTER than the eval; recorded as such in AGENTS.md. Until v22 the rule existed
    # only in prose: DELETE statements were excluded from the parser's own skip-list and
    # so were reported by nothing at all, and UPDATE statements were only date-checked.
    for dele in deletes:
        rep.fail(f"[Eval0 P4 / AGENTS r4] DELETE against {dele['table']} is forbidden. "
                 f"Injection adds scenario data; base universe rows are never deleted. "
                 f"Re-express the scenario as INSERTs, or state the contradiction in a new "
                 f"row and let the agent reconcile it.")
    inserted_ids_by_table = {}
    for ins in inserts:
        bucket = inserted_ids_by_table.setdefault(ins["table"], set())
        for row in ins["rows"]:
            for col, val in row.items():
                if col.lower() in ("id", "ts", "uuid", "identifier", "ticket_number", "record_id"):
                    bucket.add(str(val).strip().strip("'\""))
    for upd in updates:
        where = upd.get("where") or ""
        touched = set(re.findall(r"'([^']+)'", where)) | set(re.findall(r'"([^"]+)"', where))
        own = inserted_ids_by_table.get(upd["table"], set())
        # An UPDATE that only touches rows this same injection inserted is benign
        # bookkeeping. An UPDATE that reaches anything else mutates the base universe.
        if not touched or not touched <= own:
            rep.fail(f"[Eval0 P4 / AGENTS r4] UPDATE against {upd['table']} modifies rows this "
                     f"injection did not insert (WHERE: {where.strip()[:80] or 'no WHERE clause'}). "
                     f"Base universe rows are never modified. Express the new state as an "
                     f"additional row so the stale one remains discoverable as a contradiction.")

    # P4 integrity & cross-service  [Eval0 P4]
    for table, row in all_rows:
        for col, val in row.items():
            # own primary key only; *_id columns are foreign keys and SHOULD reference existing records
            if col.lower() == "id" and str(val) in base_ids:
                rep.fail(f"[Eval0 P4 COLLISION] {table}.{col} '{val}' already exists in the base universe (record collision)")
    for table, row in all_rows:
        blob = " ".join(str(v) for v in row.values())
        for ref in tok_re.findall(blob):
            if ref not in base_ids and ref not in injected_ids:
                rep.fail(f"[Eval0 P4 CROSS_SERVICE_VIOLATION] {table}: broken cross-reference '{ref}' - not found in base universe or injection")
        for ch in SLACK_CH_RE.findall(blob):
            if valid_channels and ch not in valid_channels:
                rep.fail(f"[Eval0 P4 CROSS_SERVICE_VIOLATION] {table}: slack channel {ch} is not a valid {universe} channel ({sorted(valid_channels)[0]}..{sorted(valid_channels)[-1]})")
    for em in sorted(injected_emails):
        if em.endswith("@" + domain) and personas and em not in personas and em not in npc_mailboxes and em not in base_emails:
            _m = (f"[Eval0 P4 CROSS_SERVICE_VIOLATION] injected @{domain} address '{em}' matches "
                  f"no persona or base-universe mailbox (email format mismatch)")
            if _universe_unresolvable(str(task_dir), universe):
                rep.warn(_m + " - NOTE: universe records unresolvable, base mailboxes unavailable")
            else:
                rep.fail(_m)
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
    prompt_atoms = set(tok_re.findall(prompt_text)) | {e.lower() for e in EMAIL_RE.findall(prompt_text)}
    for ins in inserts:
        for row in ins["rows"]:
            blob = " ".join(str(v) for v in row.values())
            row_atoms = set(tok_re.findall(blob)) | {e.lower() for e in EMAIL_RE.findall(blob)}
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
    rep.note(f"[Eval0 P8] COUNCIL: injection difficulty/complexity composite (minimum "
             f"{profile.get('injection_difficulty_floor') or 3.5}) requires semantic scoring - not deterministically checkable")
    return True


# Built per-universe from consts["services"] rather than a hardcoded alternation.
# The literal list was a v3/v4 one, so on HarmonyGames it recognised only slack_, gmail_,
# linear_ and contacts_ - and those four only by coincidence of prefix overlap. The other
# NINE services (gcal, github, trello, snowflake, gdocs, gdrive, gsheets, gslides,
# confluence) were invisible, so F1 could not flag a phantom tool in any of them. AGENTS.md
# HG-U10 already warned that the F1-F6 trigger conditions do not transfer from V4; this is
# that warning made true in code instead of contradicted by it.
_LEGACY_EXTRA_PREFIXES = {"oracle_gl", "sap", "sap_subledger", "blackline", "records_vault",
                          "mortgage_los", "filesystem", "stripe", "crm", "gcalendar"}
_LEGACY_SERVICE_PREFIX_RE = re.compile(r"\b(?:slack|gmail|airtable|linear|hubspot|quickbooks|gcalendar|contacts|crm|stripe|oracle_gl|sap|blackline)_[a-z_]{3,}\b")


@lru_cache(maxsize=32)
def _universe_unresolvable(task_dir_str: str, universe: str) -> bool:
    """True when this task's universe records cannot be resolved at all.

    The earlier predicate asked "is 3_UniverseDataForThisTask.json a pointer?". That is the
    WRONG signal: HarmonyGames ships a pointer in EVERY task by contract, including when
    Services_Data/ is hydrated and the mailbox set IS knowable, so keying off it made the
    hard-FAIL branch dead code for HG in every state. `load_universe_records` raises
    UniverseDataError only when the payload genuinely cannot be resolved, which is the
    condition this degrade was always meant to express.
    """
    try:
        from universe_data_source import load_universe_records, UniverseDataError
    except Exception:
        return False
    try:
        load_universe_records(Path(task_dir_str), universe)
        return False
    except UniverseDataError:
        return True
    except Exception:
        return False


_COMMS_VERB_RE = re.compile(
    r"\b(?:post|posts|posted|message|messages|messaged|send|sends|sent|email|emails|emailed|"
    r"notify|notifies|notified|reply|replies|replied|announce|announces|dm|dms)\b", re.I)


@lru_cache(maxsize=1)
def _tool_head_vocab() -> frozenset:
    """Head segments observed right after a service prefix in REAL tool catalogs.

    Widening `service_prefix_re` to the union of every universe's services pulled generic
    English nouns into the alternation (email, calendar, public, reminder, filesystem,
    messaging), so ordinary prose matched: "record the email_address on the ticket" raised a
    phantom-tool defect. Measured across all five catalogs, 1130 real tool names yield only
    68 distinct head segments and none of those prose tokens has one. Requiring a real head
    is therefore a precise, self-maintaining filter rather than a hand-kept denylist.
    """
    import re as _re
    from universes import UNIVERSES, get_universe_constants
    names, svcs = set(), set(_LEGACY_EXTRA_PREFIXES)
    for u in UNIVERSES:
        c = get_universe_constants(u)
        svcs |= set(c.get("services") or [])
        try:
            cat = Path(c.get("tool_catalog", ""))
            if not cat.is_absolute():
                cat = Path(__file__).resolve().parent.parent / cat
            if cat.is_file():
                names |= set(_re.findall(r'"(?:name|tool_name)"\s*:\s*"([a-z0-9_]+)"',
                                         cat.read_text(encoding="utf-8", errors="ignore")))
        except Exception:
            pass
    heads = set()
    for n in names:
        pref = max((x for x in svcs if n.startswith(x + "_")), key=len, default=None)
        if pref:
            rest = n[len(pref) + 1:].split("_")
            if rest and rest[0]:
                heads.add(rest[0])
    return frozenset(heads)


@lru_cache(maxsize=1)
def _all_service_prefixes() -> frozenset:
    from universes import UNIVERSES, get_universe_constants
    out = set(_LEGACY_EXTRA_PREFIXES)
    for u in UNIVERSES:
        out |= set(get_universe_constants(u).get("services") or [])
    return frozenset(out)


def _looks_like_tool_name(tok: str) -> bool:
    """True when `tok` plausibly names a tool rather than being snake_case prose."""
    low = tok.lower()
    pref = max((x for x in _all_service_prefixes() if low.startswith(x + "_")), key=len, default=None)
    if not pref:
        return False
    rest = low[len(pref) + 1:].split("_")
    vocab = _tool_head_vocab()
    # Fail CLOSED on an empty vocabulary. The old `not vocab or ...` escape meant a
    # catalogue-read failure silently restored every false positive it exists to suppress.
    # An empty vocab is a broken environment, not a permissive one; check_pipeline_wiring
    # W11 gates it so the breakage surfaces loudly instead of as scoring noise.
    return bool(rest and rest[0] and vocab and rest[0] in vocab)


def service_prefix_re(consts: dict):
    """Tool-name prefix matcher for phantom-tool detection (Eval5 F1).

    Matches THIS universe's services PLUS every other universe's service
    prefixes. In-universe hits are checked against the local tool catalogue by
    the caller; out-of-universe hits are phantom by construction. Building the
    alternation from consts["services"] ALONE was tried and is wrong in the
    other direction: it stops flagging cross-universe leakage such as
    `stripe_create_charge` or `oracle_gl_post_je` in a StarPM rubric, and the
    bare-service fallback below cannot cover them because \b does not match
    between a service name and the trailing underscore of a tool name.
    """
    from universes import UNIVERSES  # local import: avoids an import cycle
    names = set((consts or {}).get("services") or [])
    for _u in UNIVERSES.values():
        names.update(_u.get("services") or [])
    names.update(_LEGACY_EXTRA_PREFIXES)
    if not names:
        return _LEGACY_SERVICE_PREFIX_RE
    alt = "|".join(sorted((re.escape(s) for s in names), key=len, reverse=True))
    return re.compile(r"\b(?:" + alt + r")_[a-z0-9_]+\b", re.IGNORECASE)



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
    # QC Spec Doc2, 07/16: "OEs are CB interpretations, not ground truth ... universe data is
    # sole SOT". Including oe_text here let a rubric cite a value that exists ONLY in an
    # Oracle Event and still clear the phantom check, which is a false-negative generator in
    # the deliverable the pipeline exists to protect. Universe data plus the injection are the
    # source of truth; the OE is not.
    searchable = base_text + "\n" + inject_text
    payload_is_pointer = _universe_unresolvable(str(task_dir), universe)
    weekend_comms_rule = bool(consts.get("weekend_comms_rule"))
    searchable_amounts = _searchable_amounts(searchable)
    prompt_wants_future_write = bool(_PROMPT_SCHED_RE.search(prompt_text))
    domain = consts.get("persona_email_domain", "starpm.com")
    personas = {e.lower() for e in (consts.get("personas") or {})} if isinstance(consts.get("personas"), dict) else set()
    npc_mailboxes = {e.lower() for e in (consts.get("npcs") or set()) if isinstance(e, str) and "@" in e}
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
        for tok in service_prefix_re(consts).findall(blob):
            if tool_names and tok not in tool_names and _looks_like_tool_name(tok):
                rep.fail(f"[Eval5 P1 IMPOSSIBLE] rubric #{idx} references tool '{tok}' which does not exist in the {universe} tool catalog")
        for svc in re.findall(r"\b(oracle_gl|sap_subledger|blackline|records_vault|mortgage_los|stripe|filesystem)\b", blob):
            if svc not in services:
                rep.fail(f"[Eval5 P1 IMPOSSIBLE] rubric #{idx} references service '{svc}' which is not in the {universe} service set")

        # F2 persona/date  [Eval5 P2] - future dates are defects UNLESS they are a
        # prompt-sanctioned near-term calendar/reminder write target (not future-as-past).
        rubric_is_cal_create = bool(_CAL_RUBRIC_RE.search(title + " " + evid))
        future_ack = bool(_FUTURE_ACK_RE.search(title + " " + evid))
        for d, raw in set(_dates_in(title + " " + evid)):
            if d is None or WINDOW_START - timedelta(days=365) <= d <= WINDOW_END:
                continue
            if prompt_wants_future_write and rubric_is_cal_create and WINDOW_END < d <= _NEAR_FUTURE_HI:
                rep.note(f"[Eval5 P2] rubric #{idx} future date {raw} is a prompt-sanctioned calendar/reminder write target (<= {_NEAR_FUTURE_HI}) - COUNCIL confirm resolved day")
                continue
            if future_ack:
                rep.note(f"[Eval5 P2] rubric #{idx} future date {raw} is explicitly stated as not-yet-occurred (future-as-future, spec-compliant per Evals_starpm/5 P2; the F2 defect is future-AS-PAST) - COUNCIL confirm the date is a grounded universe atom")
                continue
            rep.fail(f"[Eval5 P2 MISMATCH] rubric #{idx} references date {raw} after universe today ({WINDOW_END}) - future-dated expectation")

        # Weekend-comms rule. Declared per-universe; only HarmonyGames carries it today.
        # Its own `today` (2026-02-28) IS a Saturday, so a "post this today" ask lands
        # squarely on the violation. Scoped to comms verbs so a weekend date attached to a
        # non-comms fact (a due date, a report period) is not flagged.
        if weekend_comms_rule:
            _ctx = title + " " + evid
            if _COMMS_VERB_RE.search(_ctx):
                for d, raw in set(_dates_in(_ctx)):
                    if d is not None and d.weekday() >= 5:
                        rep.fail(f"[Eval5 P2 MISMATCH] rubric #{idx} dates routine business "
                                 f"communication on {raw}, a {d.strftime('%A')} - {universe} treats "
                                 f"weekend business comms as a temporal violation")

        # F2 phantom refs  [Eval5 P2 PHANTOM]
        for ref in set(id_token_re_for(universe).findall(blob)):
            if ref not in searchable:
                rep.fail(f"[Eval5 P2 PHANTOM] rubric #{idx} cites '{ref}' which appears nowhere in universe data or the injection (QC spec 07/16: universe data is the sole source of truth, an OE mention does not qualify)")
        for em in set(e.lower() for e in EMAIL_RE.findall(blob)):
            if em.endswith("@" + domain) and personas and em not in personas and em not in npc_mailboxes and em not in searchable.lower():
                _m = (f"[Eval5 P2 PHANTOM] rubric #{idx} cites persona address '{em}' "
                      f"matching no {universe} persona or universe mailbox")
                if payload_is_pointer:
                    rep.warn(_m + " - NOTE: universe records are unresolvable (payload not hydrated),"
                                  " so this address cannot be disproven")
                else:
                    rep.fail(_m)

        # F3 process gates  [Eval5 P3 TOOL_GATE/QUERY_GATE]
        if cat == "process" and PROCESS_GATE_RE.search(title):
            rep.fail(f"[Eval5 P3 TOOL_GATE] process rubric #{idx} credits tool-calling motions ('{title[:80]}') instead of a verification outcome")

        # F4 broken rubric: expected value absent from SSOT  [Eval5 P4 BROKEN]
        # normalize money on both sides (universe stores bare floats e.g. 2132.0; rubric writes $2,132.00)
        for amt in set(MONEY_RE.findall(title)):
            c = _canonical_amount(amt)
            present = (c in searchable_amounts) if c else (amt in searchable)
            if not present and c:
                derivation = _derived_from_amounts(c, searchable_amounts, str(r.get("justification", "")) + " " + evid)
                if derivation:
                    rep.note(f"[Eval5 P4] rubric #{idx} amount {amt} is not a literal universe string but derives from universe amounts as {derivation} - aggregate/derived math, permitted per the rubric guidelines' own worked example. COUNCIL: confirm the arithmetic is the intended one.")
                    present = True
            if not present:
                rep.fail(f"[Eval5 P4 BROKEN] rubric #{idx} expects amount {amt} which does not exist in universe data or the injection, and is not a sum or difference of universe amounts (QC spec 07/16: universe data is the sole source of truth)")

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
    # Canonicalize BEFORE counting. HarmonyGames stores the guidelines' Outcome
    # sub-categories directly in `category` ("Outcome 1.1" / "1.2" / "2.1"), so an
    # exact-match census counted them as NEITHER bucket: a conformant HG set of
    # 4 Outcome + 1 Process reported "0 outcome / 1 process" and this gate rejected it
    # with "zero Outcome rubrics". validate.py already had _canonical_category and this
    # file carried a SECOND, unfixed census - the duplicated-logic failure AGENTS.md
    # rule 18 exists to prevent.
    def _canon(v):
        """Alias for universes.canonical_rubric_category (single source of truth)."""
        from universes import canonical_rubric_category
        return canonical_rubric_category(v)

    outcome_count = sum(1 for r in rubrics if _canon(r.get("category")) == "outcome")
    process_count = sum(1 for r in rubrics if _canon(r.get("category")) == "process")
    if outcome_count == 0:
        rep.fail("[Eval5 P6 6.2 MISSING_CRITERIA] zero Outcome rubrics - every deliverable is uncovered")

    # Balance is per-framework, read from the registry. Hardcoding outcome-majority here
    # enforced against HarmonyGames the exact mandate AGENTS.md hard rule 8 EXEMPTS it
    # from: HG's own QC spec replaces it with a flat Process <= 40% cap and states that
    # zero Process is valid.
    _bal = (profile or {}).get("rubric_balance_rule", "outcome_gt_process")
    _total = outcome_count + process_count
    if rubrics and _bal == "process_max_40pct":
        if _total and (process_count / _total) > 0.40:
            rep.fail(f"[Eval5 P3] Process is {process_count}/{_total} "
                     f"({process_count / _total:.0%}) of the set - this universe caps it at 40%")
    elif rubrics and process_count > outcome_count:
        rep.fail(f"[Eval5 P3] Process rubrics ({process_count}) outnumber Outcome rubrics ({outcome_count}) - violates outcome-first mandate")
    rep.note(f"[Eval5 P7] rubric census: {outcome_count} outcome / {process_count} process / {len(rubrics)} total")
    rep.note("[Eval5 P6] COUNCIL: under-strictness (6.3), exclusion coverage (6.6), UGT convergence (6.8), OE authority (6.9), strict feasibility (6.10), date-alignment ambiguity (6.11) require semantic judgment - flagged for council review")
    _false_fail_backstops(task_dir, rep, universe, rubrics, prompt_text, oe_text)
    return True


# ---------------------------------------------------------------------------
# v21.3 false-fail backstops. Post-mortem: Task 39 (Las Palmas 8D) shipped a
# QC-fail-capable fault because the human-judgment gates (Council/AUDIT/FINAL/S4)
# SAW three defect classes and mis-scored them as "Minor / ship-as-is". These are
# deterministic nets so the mis-score cannot ship:
#   F7 AMBIGUOUS_TARGET     rubric pins ONE record id but >=2 universe rows share
#                           its entity and the prompt names none (R2/R3/R4).
#   F8 NON_ATOMIC_ENUM      one criterion enumerates >=3 conjunctive items under a
#                           completeness/step predicate (R11 had 3, R15 had 5).
#   F9 UNRECONCILED_FUTURE_EVT confirmed calendar event dated >= universe today
#                           references the task entity, its date is uncited in the
#                           OEs, and the deliverables assert completeness (the
#                           2026-07-07 carpet walk that broke "disposal is the only
#                           open item").
# ---------------------------------------------------------------------------
_CANON_SET_RE = re.compile(r"must be one of|including but not limited to|at least one of|\bor similar\b|\bor equivalent\b", re.I)
_WRITE_TGT_RE = re.compile(r"\bthe agent(?:'s)?\s+(?:update|updates|change|changes|set|sets|mark|marks|log|logs|edit|edits|correct|corrects|revise|revises|square|squares)\b", re.I)
_ENUM_PREDICATE_RE = re.compile(r"\b(?:are|is|were|was)\s+(?:complete|completed|done|finished|resolved|taken care of|in place)\b|what it(?:'?ll| will)? takes?\b|\bsteps?\b|\bit(?:'?ll| will)? take to\b", re.I)
_REC_ID_RE = re.compile(r"\brec[0-9a-f]{13,20}\b")
_COMPLETE_CLAIM_RE = re.compile(
    r"\beverything else\b|\bthe rest\b|\brest of\b|\ball (?:other )?(?:work|items?) (?:is|are) (?:done|complete)\b|"
    r"\b(?:only|sole|lone|one)\b[^.]{0,45}\b(?:item|thing|blocker|piece)\b[^.]{0,45}\b(?:open|outstanding|left|remaining|blocking|keeping|to close)\b",
    re.I)


def _split_rows_file(task_dir, fname):
    p = task_dir / "_aux" / "Universe_Split" / fname
    if not p.is_file():
        return None
    try:
        d = json.loads(_read(p))
    except json.JSONDecodeError:
        return None
    rows = d if isinstance(d, list) else next((v for v in d.values() if isinstance(v, list)), [])
    out = []
    for r in rows:
        if isinstance(r, dict) and isinstance(r.get("row_data"), str):
            try:
                out.append(json.loads(r["row_data"]))
            except json.JSONDecodeError:
                out.append(r)
        else:
            out.append(r)
    return out


def _false_fail_backstops(task_dir, rep, universe, rubrics, prompt_text, oe_text):
    """v21.3 deterministic backstops (F7/F8/F9). StarPM-only for now (the fault class
    was proven on a StarPM V4 task); the shapes generalize but the universe readers
    below are keyed to the StarPM split layout. F8 (enumeration) is universe-agnostic
    and runs everywhere; F7/F9 need the StarPM split readers and are gated below."""
    prompt_lc = prompt_text.lower()
    oe_lc = oe_text.lower()
    rubric_blob = " ".join(" ".join(str(r.get(k, "")) for k in ("title", "criterion", "justification", "evidence")) for r in rubrics)

    # ---- F8: non-atomic conjunctive enumeration (>=3 items under a completeness/step predicate) ----
    for idx, r in enumerate(rubrics, 1):
        title = str(r.get("title", r.get("criterion", "")))
        if _CANON_SET_RE.search(title) or "@" in title:
            continue
        if title.count(",") >= 2 and re.search(r",\s*(?:and|or)\s+\w", title) and _ENUM_PREDICATE_RE.search(title):
            n = title.count(",") + 1
            rep.fail(f"[Eval5 P6 6.1b NON_ATOMIC_ENUM] rubric #{idx} enumerates ~{n} items in one criterion under a completeness/step predicate - split into one rubric per item (the Airtable write was correctly split into 3; apply the same rule to the rest)")

    if universe != "starpm":
        return  # F7/F9 use the StarPM split readers; F8 above already ran for every universe

    # ---- universe record index (F7 / F9) ----
    recs = _split_rows_file(task_dir, "airtable.airtable_records.json")
    rec_by_id = {}
    if recs:
        for e in recs:
            if not isinstance(e, dict):
                continue
            rid = e.get("id")
            fields = e.get("fields") if isinstance(e.get("fields"), dict) else {}
            tbl = e.get("table_id") or e.get("tableId") or ""
            if rid:
                rec_by_id[rid] = (tbl, fields)

    # ---- F7: ambiguous target record ----
    entity_vals = set()
    for idx, r in enumerate(rubrics, 1):
        title = str(r.get("title", r.get("criterion", "")))
        if not _WRITE_TGT_RE.search(title):
            continue
        for rid in set(_REC_ID_RE.findall(title)):
            if rid not in rec_by_id:
                continue
            tbl, fields = rec_by_id[rid]
            ent = None
            for fv in fields.values():
                if isinstance(fv, str) and len(fv) >= 4 and fv.lower() in title.lower():
                    if ent is None or len(fv) > len(ent):
                        ent = fv
            if not ent:
                continue
            entity_vals.add(ent)
            siblings = [oid for oid, (otbl, of) in rec_by_id.items()
                        if otbl == tbl and any(isinstance(v, str) and ent.lower() in v.lower() for v in of.values())]
            if len(siblings) >= 2 and rid.lower() not in prompt_lc:
                rep.fail(f"[Eval5 P7 AMBIGUOUS_TARGET] rubric #{idx} pins record {rid} but {len(siblings)} records in {tbl} share entity '{ent}' and the prompt names none of them - a reasonable agent may write a sibling row and wrongly fail. Name the record in the prompt, or accept any matching record.")

    # ---- F9: unreconciled future confirmed calendar event on the task entity ----
    if entity_vals and (_COMPLETE_CLAIM_RE.search(oe_text) or _COMPLETE_CLAIM_RE.search(rubric_blob)):
        events = _split_rows_file(task_dir, "gcalendar.gcalendar_events.json") or []
        fired = set()
        for e in events:
            if not isinstance(e, dict):
                continue
            status = str(e.get("status", "")).lower()
            if status and status != "confirmed":
                continue
            start_raw = str(e.get("start_dt") or e.get("start_time") or "")
            try:
                sd = date(int(start_raw[0:4]), int(start_raw[5:7]), int(start_raw[8:10])) if len(start_raw) >= 10 else None
            except ValueError:
                sd = None
            if sd is None or sd < WINDOW_END:
                continue
            iso = start_raw[0:10]
            props = e.get("properties") if isinstance(e.get("properties"), dict) else {}
            blob = " ".join(str(x) for x in (e.get("summary", ""), e.get("title", ""), e.get("description", ""),
                                             props.get("summary", ""), props.get("title", ""), props.get("description", ""), props.get("location", "")))
            blob_lc = blob.lower()
            for ent in entity_vals:
                if ent.lower() in blob_lc and iso not in oe_text and iso not in rubric_blob and (ent, iso) not in fired:
                    fired.add((ent, iso))
                    summ = (props.get("summary") or e.get("summary") or props.get("title") or "calendar event").strip()
                    rep.fail(f"[Eval5 P7 UNRECONCILED_FUTURE_EVT] confirmed calendar event '{summ[:70]}' dated {sd} references task entity '{ent}' but no Oracle Event cites that date - a future confirmed event is open work. Sweep every service (incl. Calendar) before asserting completeness / 'only open item'.")
