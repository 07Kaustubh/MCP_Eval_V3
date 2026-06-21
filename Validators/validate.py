#!/usr/bin/env python3
"""
validate.py — phase-aware validator for MCP Eval V3 deliverables.

Usage:
    python Validators/validate.py --phase {prompt|oe|rubrics|all} --task <path_to_task_dir>

Exits 0 on clean, non-zero on any FAIL. Writes a per-phase report to
<task_dir>/_aux/Validator_Reports/<phase>.md and prints summary to stdout.

Checks per phase:

PROMPT (5_Prompt.txt):
  - em-dash / en-dash ban
  - 500-word cap
  - explicit tool / parameter / internal-ID leakage
  - explicit pre-solving phrases (heuristic)
  - explicit MCP-server name mention
  - relative-date phrase scan (warning, not fail)

OE (6_Oracle_Events.txt):
  - em-dash / en-dash ban
  - numbered-prose format (lines start with "OE")
  - tool-name existence vs 8_Server_Tools_Details.json
  - email body parameter named correctly (`content` not `body`)
  - Slack param named `payload` not `text`

RUBRICS (7_Rubrics.json):
  - schema: id (uuid), title (str), annotations {evidence, justification, rubric_category}
  - rubric_category in {outcome, process}
  - title starts with "The Agent" or "Agent"
  - no tool name in title (only allowed in evidence / justification)
  - no "at least N" in title unless prompt explicitly mandates a minimum
  - outcome count > process count (and >=1 outcome)
  - "approximately" only before calculated/rounded values (warn if before IDs / dates)
  - "(or similar)" only in freetext contexts (warn if next to emails / IDs)
  - groundedness sweep: every $amount / email / JE_id / vendor_id in title
    appears at least once in the per-task Universe_Split JSON
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).resolve().parent.parent
TOOL_DEFS = ROOT / "Brookfield_Base_Universe" / "8_Server_Tools_Details.json"

EM_DASH_PATTERN = re.compile(r"[\u2014\u2013]")          # em-dash, en-dash
TOOL_NAME_HINT = re.compile(r"\b(?:[a-z_]+_(?:list|search|get|create|update|send|add|upload|approve|reject|post|reply|submit|delete|show|history)_[a-z_]+|email_send_email|slack_conversations_add_message)\b")
INTERNAL_ID = re.compile(r"\b(?:JE-[a-z_]+-FP-\d{4}-\d{2}-\d{4}|BL-[A-F0-9]{12}|exc_[a-f0-9]{14}|VEN-\d{3,4}(?:-[A-Za-z]+)?(?:-\d{3,6})?|apinv_[a-f0-9]{14,16}|issue_[a-f0-9]{32}|reminder_[a-z0-9_]{6,}|conversation_[a-z0-9_]{6,}|airtable_[a-f0-9]{12}|doc_[a-f0-9]{8}|linear_[a-f0-9]{12})\b")
MCP_SERVER_NAME = re.compile(r"\b(?:MCP server|the Oracle GL MCP|the Email MCP|the Slack MCP|the BlackLine MCP|the Records Vault MCP|the Airtable MCP|the Linear MCP|the SAP MCP)\b", re.IGNORECASE)
PRE_SOLVE_HINT = re.compile(r"\b(?:root cause is|the issue is caused by|the actual culprit is|the answer is|the problem is that)\b", re.IGNORECASE)
EMAIL_RE = re.compile(r"\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b", re.IGNORECASE)
MONEY_RE = re.compile(r"\$\s?(\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\d+(?:\.\d{2})?)")
JE_ID = re.compile(r"JE-[a-z_]+-FP-\d{4}-\d{2}-\d{4}")
EXC_ID = re.compile(r"\bexc_[a-f0-9]{14}\b")
RECON_ID = re.compile(r"\bBL-[A-F0-9]{12}\b")
DOC_ID = re.compile(r"\bdoc_[a-f0-9]{8}\b")
VENDOR_ID = re.compile(r"\bVEN-\d{3,4}(?:-[A-Za-z]+)?(?:-\d{3,6})?\b")
APINV_ID = re.compile(r"\bapinv_[a-f0-9]{14,16}\b")
RELATIVE_DATE = re.compile(r"\b(?:tomorrow|yesterday|today|next\s+(?:week|month|monday|tuesday|wednesday|thursday|friday|saturday|sunday)|last\s+(?:week|month|monday|tuesday|wednesday|thursday|friday|saturday|sunday)|\d+\s+days?\s+ago|in\s+\d+\s+days?|this\s+(?:week|month|quarter|morning|afternoon|evening))\b", re.IGNORECASE)

# Prompt_Guidelines.md anti-patterns
QC_SAMPLE_CLICHE = re.compile(r"\b(?:go through everything and surface every|i need the full picture[:,]|dig through our emails,?\s+slack|email me the full|loop in [a-z]+|cc our ceo|flag the biggest risks|brief [a-z]+ and [a-z]+ with what you found)\b", re.IGNORECASE)
OVER_SIGNAL_INVESTIGATION = re.compile(r"\b(?:check our (?:messages|emails)[\s,]+slack[\s,]+(?:and project records|project tickets)|across (?:emails|email),?\s+slack[\s,]+linear|get into emails,?\s+slack[\s,]+linear|emails[\s,]+slack[\s,]+linear[\s,]+(?:crm|airtable))\b", re.IGNORECASE)
GENERIC_URGENCY = re.compile(r"\b(?:before it blows up|keeping me up at night|i can't tell you what the net position is|i'?m getting paged|something changed in the last few days)\b", re.IGNORECASE)


class Report:
    def __init__(self, phase: str):
        self.phase = phase
        self.fails: List[str] = []
        self.warns: List[str] = []
        self.notes: List[str] = []

    def fail(self, msg: str):
        self.fails.append(msg)

    def warn(self, msg: str):
        self.warns.append(msg)

    def note(self, msg: str):
        self.notes.append(msg)

    def render(self) -> str:
        lines = [f"# Validator report: {self.phase}", ""]
        lines.append(f"**Status:** {'FAIL' if self.fails else 'PASS'}  ")
        lines.append(f"**Fails:** {len(self.fails)} · **Warns:** {len(self.warns)} · **Notes:** {len(self.notes)}")
        lines.append("")
        for tag, items in (("FAIL", self.fails), ("WARN", self.warns), ("NOTE", self.notes)):
            if not items:
                continue
            lines.append(f"## {tag}")
            for i in items:
                lines.append(f"- {i}")
            lines.append("")
        return "\n".join(lines)


def load_tool_names() -> set:
    if not TOOL_DEFS.is_file():
        return set()
    with open(TOOL_DEFS, "r", encoding="utf-8") as f:
        data = json.load(f)
    names = set()

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in ("name", "tool_name", "function_name") and isinstance(v, str):
                    names.add(v)
                walk(v)
        elif isinstance(node, list):
            for it in node:
                walk(it)

    walk(data)
    return names


def load_universe_blob(task_dir: Path) -> str:
    split = task_dir / "_aux" / "Universe_Split"
    if not split.is_dir():
        return ""
    chunks = []
    for p in split.glob("*.json"):
        if p.name == "Universe_complete_data.json":
            continue
        chunks.append(p.read_text(encoding="utf-8"))
    return "\n".join(chunks)


def validate_prompt(task_dir: Path, rep: Report) -> None:
    f = task_dir / "5_Prompt.txt"
    if not f.is_file():
        rep.fail(f"missing {f}")
        return
    text = f.read_text(encoding="utf-8")

    for m in EM_DASH_PATTERN.finditer(text):
        rep.fail(f"em-dash / en-dash at offset {m.start()}: `{text[max(0,m.start()-20):m.start()+20]}`")

    words = text.split()
    rep.note(f"word count: {len(words)}")
    if len(words) > 500:
        rep.fail(f"word count {len(words)} exceeds 500 cap")

    for m in TOOL_NAME_HINT.finditer(text):
        rep.fail(f"explicit tool-name leakage: `{m.group(0)}`")

    for m in MCP_SERVER_NAME.finditer(text):
        rep.fail(f"explicit MCP-server mention: `{m.group(0)}`")

    for m in INTERNAL_ID.finditer(text):
        rep.fail(f"internal-ID leakage: `{m.group(0)}`")

    for m in PRE_SOLVE_HINT.finditer(text):
        rep.warn(f"possible pre-solve phrase: `{m.group(0)}` (review by hand)")

    for m in RELATIVE_DATE.finditer(text):
        rep.note(f"relative date: `{m.group(0)}` (must resolve against universe today 2026-06-12)")

    # Prompt_Guidelines.md anti-patterns (warn, do not fail)
    for m in QC_SAMPLE_CLICHE.finditer(text):
        rep.warn(f"QC sample cliché phrase: `{m.group(0)}` (avoid mass-produced tonality)")
    for m in OVER_SIGNAL_INVESTIGATION.finditer(text):
        rep.warn(f"over-signaling the investigation: `{m.group(0)}` (real persona would not inventory their own systems)")
    for m in GENERIC_URGENCY.finditer(text):
        rep.warn(f"generic urgency framing: `{m.group(0)}` (ground urgency in specific consequences)")


def validate_oe(task_dir: Path, rep: Report) -> None:
    f = task_dir / "6_Oracle_Events.txt"
    if not f.is_file():
        rep.fail(f"missing {f}")
        return
    text = f.read_text(encoding="utf-8")

    for m in EM_DASH_PATTERN.finditer(text):
        rep.fail(f"em-dash / en-dash at offset {m.start()}: `{text[max(0,m.start()-20):m.start()+20]}`")

    oe_lines = re.findall(r"(?m)^OE\s*\d+", text)
    rep.note(f"OE step count: {len(oe_lines)}")
    if not oe_lines:
        rep.fail("no `OE<n>` numbered-prose lines found")
    elif len(oe_lines) < 8:
        rep.warn(f"OE step count is {len(oe_lines)} — V3 reference tasks have 11 to 28 OEs. A sparse OE list usually projects below the 40+ tool-call density bar. Add discovery + write steps.")

    # OE convention checks (from Reference/OE_Convention_Inventory.json)
    opening_keywords = (
        "Search", "Send", "Post", "Call", "Use", "Verify", "Look up", "Lookup",
        "Query", "Pull", "Fetch", "Load",
        "Create", "Update", "Upload", "Add", "When", "Confirm", "Schedule",
        "Retrieve", "Get", "List", "Check", "Read", "Identify", "Determine",
        "Filter", "Decide", "Cross-reference", "Cross reference", "Find",
        "Inspect", "Review", "Compare", "Compute", "Calculate", "Reply",
        "Forward", "Notify", "Approve", "Reject", "Submit", "Certify",
        "Archive", "Dismiss", "Then", "Next", "Finally", "Also", "Optionally",
        "Resolve", "Write", "Draft", "Log", "Mark", "Set", "Reach out"
    )
    found_opening = sum(1 for line in text.splitlines() if re.match(r"^OE\s*\d+:?\s*", line) and any(line.split(":", 1)[-1].strip().startswith(kw) for kw in opening_keywords))
    if oe_lines and found_opening / len(oe_lines) < 0.6:
        rep.warn(f"only {found_opening}/{len(oe_lines)} OE lines start with a recognized action verb (Search / Send / Call / etc.). V3 references use action-first openings consistently.")

    tool_names = load_tool_names()
    if not tool_names:
        rep.warn("could not load 8_Server_Tools_Details.json — skipping tool-name existence check")
    else:
        referenced = set(TOOL_NAME_HINT.findall(text))
        unknown = sorted(t for t in referenced if t not in tool_names)
        for t in unknown:
            rep.fail(f"OE references unknown tool: `{t}` (not in 8_Server_Tools_Details.json)")

    if re.search(r"email_send_email[^.\n]{0,80}\bbody\s*[:=]", text):
        rep.fail("email_send_email uses `body` — should be `content`")
    if re.search(r"slack_conversations_add_message[^.\n]{0,80}\btext\s*[:=]", text):
        rep.fail("slack_conversations_add_message uses `text` — should be `payload`")


def validate_rubrics(task_dir: Path, rep: Report) -> None:
    f = task_dir / "7_Rubrics.json"
    if not f.is_file():
        rep.fail(f"missing {f}")
        return
    try:
        rubrics = json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        rep.fail(f"invalid JSON: {e}")
        return
    if not isinstance(rubrics, list):
        rep.fail("rubrics file must be a JSON array")
        return

    prompt_text = ""
    pf = task_dir / "5_Prompt.txt"
    if pf.is_file():
        prompt_text = pf.read_text(encoding="utf-8").lower()

    universe_blob = load_universe_blob(task_dir)
    tool_names = load_tool_names()

    outcome_n = 0
    process_n = 0

    for i, r in enumerate(rubrics):
        loc = f"rubric[{i}]"
        if not isinstance(r, dict):
            rep.fail(f"{loc}: not an object")
            continue
        rid = r.get("id", "")
        if rid and not re.match(r"^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$", str(rid)):
            rep.warn(f"{loc}: id `{rid}` is not a uuid")
        title = r.get("title", "")
        if not isinstance(title, str) or not title.strip():
            rep.fail(f"{loc}: title missing or empty")
            continue
        # Support both shapes:
        #   nested:  {annotations: {evidence, justification, rubric_category}}
        #   flat:    {evidence, justification, category}
        ann = r.get("annotations") if isinstance(r.get("annotations"), dict) else {}
        evidence = ann.get("evidence") or r.get("evidence")
        justification = ann.get("justification") or r.get("justification")
        cat_raw = ann.get("rubric_category") or r.get("category") or r.get("rubric_category") or ""
        if not evidence:
            rep.fail(f"{loc}: evidence missing or empty")
        if not justification:
            rep.fail(f"{loc}: justification missing or empty")
        if not cat_raw:
            rep.fail(f"{loc}: category missing or empty")
        cat = str(cat_raw).lower()
        if cat not in ("outcome", "process"):
            rep.fail(f"{loc}: rubric_category `{cat}` not in {{outcome, process}}")
        if cat == "outcome":
            outcome_n += 1
        elif cat == "process":
            process_n += 1

        if not re.match(r"^(?:The\s+Agent|Agent)\b", title):
            rep.fail(f"{loc}: title must start with `The Agent` or `Agent` — got `{title[:60]}...`")

        for m in TOOL_NAME_HINT.finditer(title):
            if tool_names and m.group(0) in tool_names:
                rep.fail(f"{loc}: tool name `{m.group(0)}` appears in title (allowed only in evidence/justification)")
            else:
                rep.warn(f"{loc}: suspicious tool-shaped token `{m.group(0)}` in title")

        if re.search(r"\bat\s+least\s+\d+\b", title, re.IGNORECASE):
            prompt_mandates_min = bool(re.search(r"\bat\s+least\s+\d+\b", prompt_text, re.IGNORECASE))
            if not prompt_mandates_min:
                rep.fail(f"{loc}: title uses `at least N` but the prompt does not mandate a minimum — split into atomic rubrics")

        if re.search(r"approximately\s+(?:\d{4}-\d{2}-\d{2}|[A-F0-9]{12}|exc_|VEN-)", title):
            rep.fail(f"{loc}: `approximately` used in front of an ID/date — restrict to calculated/rounded values")

        if re.search(r"\([^)]*or\s+similar[^)]*\)\s*[^.]{0,30}@\w", title):
            rep.warn(f"{loc}: `(or similar)` near an email — emails must be exact-match")

        if universe_blob:
            for m in MONEY_RE.finditer(title):
                amt = m.group(0).replace(" ", "")
                amt_no_dollar = amt.lstrip("$")
                amt_no_commas = amt_no_dollar.replace(",", "")
                amt_int = amt_no_commas.split(".")[0]
                # Try multiple representations: with $, without $, without commas, integer-only, float form
                variants = {amt, amt_no_dollar, amt_no_commas, amt_int}
                # Also try as float with .0 (universe stores 117000.0 etc.)
                if "." not in amt_no_commas and amt_int.isdigit():
                    variants.add(amt_int + ".0")
                if not any(v in universe_blob for v in variants):
                    rep.warn(f"{loc}: dollar amount `{amt}` not found verbatim in Universe_Split (tried: {sorted(variants)})")
            for m in EMAIL_RE.finditer(title):
                if m.group(0).lower() not in universe_blob.lower():
                    rep.fail(f"{loc}: email `{m.group(0)}` not found in Universe_Split")
            for pat, label in ((JE_ID, "JE"), (EXC_ID, "exception"), (DOC_ID, "doc"), (VENDOR_ID, "vendor"), (APINV_ID, "apinv"), (RECON_ID, "recon")):
                for m in pat.finditer(title):
                    if m.group(0) not in universe_blob:
                        rep.fail(f"{loc}: {label} id `{m.group(0)}` not found in Universe_Split")

    rep.note(f"counts: outcome={outcome_n}, process={process_n}")
    if outcome_n == 0:
        rep.fail("no outcome rubrics (every task needs at least 1)")
    if process_n > outcome_n:
        rep.fail(f"process count ({process_n}) > outcome count ({outcome_n}) — process must be the minority")
    if process_n > 0 and (process_n / max(1, outcome_n + process_n)) > 0.5:
        rep.fail(f">50% of rubrics are process — outcome must outnumber process")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", required=True, choices=["prompt", "oe", "rubrics", "all"])
    ap.add_argument("--task", required=True, help="path to <TASK_DIR>")
    args = ap.parse_args()

    task_dir = Path(args.task).resolve()
    if not task_dir.is_dir():
        print(f"ERROR: {task_dir} is not a directory", file=sys.stderr)
        sys.exit(2)

    out_dir = task_dir / "_aux" / "Validator_Reports"
    out_dir.mkdir(parents=True, exist_ok=True)

    phases = [args.phase] if args.phase != "all" else ["prompt", "oe", "rubrics"]
    overall_fail = False
    for phase in phases:
        rep = Report(phase)
        if phase == "prompt":
            validate_prompt(task_dir, rep)
        elif phase == "oe":
            validate_oe(task_dir, rep)
        elif phase == "rubrics":
            validate_rubrics(task_dir, rep)
        out = out_dir / f"{phase}.md"
        out.write_text(rep.render(), encoding="utf-8")
        status = "FAIL" if rep.fails else "PASS"
        print(f"[{status}] {phase}: {len(rep.fails)} fails, {len(rep.warns)} warns, {len(rep.notes)} notes -> {out}")
        if rep.fails:
            overall_fail = True

    sys.exit(1 if overall_fail else 0)


if __name__ == "__main__":
    main()
