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
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parent.parent

def _rel(path) -> str:
    """Render a path relative to the repo root.

    Reports are hashed byte-for-byte by check_regression and stdout is frozen under
    regression_baseline/validate_outputs/, so emitting an absolute path bakes the author's
    home directory into both: the gate passed only on the machine that froze it and
    reported drift for every other user. Repo-relative is stable across checkouts.
    """
    try:
        return str(Path(path).resolve().relative_to(ROOT))
    except Exception:
        return str(path)


try:
    from Validators.universes import detect_universe, get_universe_constants, get_framework_profile, canonical_rubric_category
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from universes import detect_universe, get_universe_constants, get_framework_profile, canonical_rubric_category
try:
    from Validators.check_rubric_antipatterns import (
        negative_framing_hit, prompt_mandate_for, vague_exemplar_fields)
except ImportError:
    from check_rubric_antipatterns import (
        negative_framing_hit, prompt_mandate_for, vague_exemplar_fields)

try:
    from Validators.check_persona_acl import (
        load_roster, load_brief_names, check_persona_resolves, check_no_impossible_writes)
except ImportError:
    from check_persona_acl import (
        load_roster, load_brief_names, check_persona_resolves, check_no_impossible_writes)

try:
    from Validators.check_retired_servers import retired_server_findings
except ImportError:
    from check_retired_servers import retired_server_findings

EM_DASH_PATTERN = re.compile(r"[\u2014\u2013]")          # em-dash, en-dash
TOOL_NAME_HINT = re.compile(r"\b(?:[a-z_]+_(?:list|search|get|create|update|send|add|upload|approve|reject|post|reply|submit|delete|show|history)_[a-z_]+|email_send_email|slack_conversations_add_message)\b")
INTERNAL_ID = re.compile(r"\b(?:JE-[a-z_]+-FP-\d{4}-\d{2}-\d{4}|BL-[A-F0-9]{12}|exc_[a-f0-9]{14}|VEN-\d{3,4}(?:-[A-Za-z]+)?(?:-\d{3,6})?|apinv_[a-f0-9]{14,16}|issue_[a-f0-9]{32}|reminder_[a-z0-9_]{6,}|conversation_[a-z0-9_]{6,}|airtable_[a-f0-9]{12}|doc_[a-f0-9]{8}|linear_[a-f0-9]{12})\b")
MCP_SERVER_NAME = re.compile(r"\b(?:MCP server|the Oracle GL MCP|the Email MCP|the Slack MCP|the BlackLine MCP|the Records Vault MCP|the Airtable MCP|the Linear MCP|the SAP MCP)\b", re.IGNORECASE)
PRE_SOLVE_HINT = re.compile(r"\b(?:root cause is|the issue is caused by|the actual culprit is|the answer is|the problem is that|we already know(?:\s+it'?s)?|the issue is clearly|we'?ve confirmed (?:it'?s|that)|we know it'?s|we'?ve identified that|it'?s definitely)\b", re.IGNORECASE)

P2_CONFLICTING = re.compile(
    r"\b(?:do not|don'?t|never|avoid)\s+\w+[^.\n]{0,80}\bbut\s+(?:also\s+)?(?:do|always|definitely|make sure)\b|"
    r"\b(?:always|must|definitely|make sure)\s+\w+[^.\n]{0,80}\bbut\s+(?:do not|don'?t|never)\b|"
    r"\b(?:include|use|cover)\s+everything\b[^.\n]{0,60}\bbut\s+(?:only|just|exclude)\b",
    re.IGNORECASE,
)
P2_IMPOSSIBLE_FUTURE = re.compile(
    r"\b(?:happened|occurred|caused|did|posted|sent|created)\s+(?:in|on|during|next|the\s+week\s+of)\s+(?:next\s+(?:week|month|quarter|year)|July|August|September|October|November|December)\s+\d{4}\b",
    re.IGNORECASE,
)
P5_EXACT_TIMESTAMP = re.compile(
    r"\b(?:at\s+exactly\s+\d{1,2}:\d{2}|on\s+\w+\s+\d{1,2}(?:st|nd|rd|th)?\s+at\s+\d{1,2}:\d{2}|exactly\s+\d{1,2}:\d{2}\s*(?:am|pm|AM|PM))\b",
    re.IGNORECASE,
)
P5_ARBITRARY_FORMAT = re.compile(
    r"\b(?:respond\s+in\s+exactly\s+\d+\s+(?:sentences?|words?|paragraphs?)|use\s+passive\s+voice|respond\s+in\s+(?:json|xml|yaml)\s+format|format\s+your\s+(?:answer|response)\s+as\s+(?:json|xml|yaml|table)|reply\s+in\s+(?:exactly|only)\s+\d+\s+(?:lines?|sentences?))\b",
    re.IGNORECASE,
)
P5_TEST_ERROR_HANDLING = re.compile(
    r"\b(?:intentionally|deliberately|on\s+purpose|knowingly)\s+\w+(?:\s+\w+){0,5}\s+(?:incorrect|wrong|invalid|broken|to\s+(?:test|trigger|simulate))\b|"
    r"\btest\s+(?:error|failure|exception)\s+handling\b|"
    r"\btrigger\s+(?:an?\s+)?(?:error|failure|exception)\s+(?:to|so)\b",
    re.IGNORECASE,
)
SERVICE_KEYWORDS = {
    "gl": re.compile(r"\b(?:journal\s+entr(?:y|ies)|general\s+ledger|trial\s+balance|JE-[a-z]|post(?:ed|ing)?\s+(?:a\s+)?(?:reversal|JE|journal)|Oracle\s+GL)\b", re.IGNORECASE),
    "email": re.compile(r"\b(?:email|inbox|emailed|reach\s+out\s+(?:via\s+email|by\s+email)|message\s+thread\s+from)\b", re.IGNORECASE),
    "slack": re.compile(r"\b(?:Slack|posted?\s+in\s+(?:#|the\s+)|channel|DM\s+\w+|direct\s+message)\b", re.IGNORECASE),
    "blackline": re.compile(r"\b(?:BlackLine|reconciliation|recon\b|exception|variance\s+over\s+SLA)\b", re.IGNORECASE),
    "vault": re.compile(r"\b(?:Records?\s+Vault|filed\s+under|retention|archive\s+the|document\s+vault)\b", re.IGNORECASE),
    "linear": re.compile(r"\b(?:Linear|ticket\s+(?:in\s+Linear|on\s+Linear|tracker)|issue\s+tracker|backlog\s+item)\b", re.IGNORECASE),
    "airtable": re.compile(r"\bAirtable\b", re.IGNORECASE),
    "sap": re.compile(r"\b(?:SAP|subledger|AP\s+(?:invoice|inv\b)|vendor\s+master|accounts?\s+payable\s+sub)\b", re.IGNORECASE),
    "contacts": re.compile(r"\b(?:contacts?\s+(?:list|directory|lookup|search)|email\s+directory)\b", re.IGNORECASE),
    "hubspot": re.compile(r"\bHubSpot\b", re.IGNORECASE),
    "quickbooks": re.compile(r"\bQuickBooks\b", re.IGNORECASE),
    "gcalendar": re.compile(r"\b(?:gcalendar|Google\s+Calendar)\b", re.IGNORECASE),
}
WRITE_ACTION_PROMPT_VERBS = [
    "send", "post", "create", "approve", "deny", "reject", "certify",
    "file", "upload", "update", "void", "reverse", "submit", "archive",
    "notify", "email", "dismiss", "escalate", "reclassify", "forward",
    "schedule", "reply", "draft", "log", "add",
]
WRITE_VERB_PROMPT_RE = re.compile(r"\b(?:" + "|".join(WRITE_ACTION_PROMPT_VERBS) + r")(?:s|ed|ing)?\b", re.IGNORECASE)
X2_POSITIONAL_REFS = re.compile(
    r"\bthe\s+(?:right\s+person|right\s+contact|appropriate\s+(?:person|recipient|approver|partner|stakeholder)|correct\s+(?:person|recipient)|relevant\s+(?:person|recipient|partner|owner)|managing\s+partner|partner\s+in\s+charge|engagement\s+(?:partner|manager)|account\s+(?:owner|manager)|the\s+approver|the\s+reviewer)\b",
    re.IGNORECASE,
)
X7_OVERLY_BROAD_LIST = re.compile(
    r"\b(?:any\s+of|one\s+of|either)\s+(?:[A-Z][\w]*(?:\s*,\s*[A-Z][\w]*){1,}\s*(?:,?\s*or\s+[A-Z][\w]*)?)\b|"
    r"\b(?:contains?|includes?|mentions?)\s+(?:at\s+least\s+one\s+of|any\s+of)\s+(?:[A-Z\w][^.\n]{5,80})",
    re.IGNORECASE,
)
X8_FREETEXT_QUOTED = re.compile(
    r"\b(?:subject(?:\s+line)?|body|title|description|summary|message\s+text|content|email\s+body|note)\s*(?:of|with|containing|that\s+(?:says|reads|states|includes)|matches?)\s*[\"'][^\"'\n]{3,120}[\"']",
    re.IGNORECASE,
)
X9_SYNONYM_PAIRS = [
    ("spending", "expenses"), ("revenue", "sales"), ("margin", "profit"),
    ("vendor", "supplier"), ("client", "customer"), ("invoice", "bill"),
    ("payment", "remittance"), ("approval", "sign-off"), ("certification", "attestation"),
    ("discrepancy", "variance"), ("response", "reply"),
    ("recipient", "addressee"), ("transaction", "entry"),
]

V1_INVESTIGATION_CUES = re.compile(
    r"\b(?:figure\s+out|find\s+out|find\s+(?:the|out)|look\s+into|investigate|work\s+(?:out|through)|dig\s+into|get\s+to\s+the\s+bottom|sort\s+out|what'?s\s+(?:going\s+on|happening|causing|behind)|where\s+(?:it|that|things|this)\s+(?:lands|stands|is)|check\s+(?:what|why|how|where|whether|the)|tell\s+me\s+(?:where|what|why|how|whether)|see\s+(?:what|why|how|whether|if)|walk\s+(?:me\s+)?through|trace\s+(?:through|down)|reconcile|determine|verify\s+(?:what|whether|the))\b",
    re.IGNORECASE,
)
V1_ACTION_VERBS = re.compile(
    r"\b(?:send|sends?|post|posts?|create|creates?|approve|approves?|certify|certifies?|file|files?|upload|uploads?|update|updates?|submit|submits?|notify|notifies?|email|emails?|forward|forwards?|schedule|schedules?|reply|replies?|draft|drafts?|log|logs?|add|adds?|reverse|reverses?|void|voids?|dismiss|dismisses?|escalate|escalates?|reclassify|reclassifies?|archive|archives?|circulate|circulates?|stage|stages?|book|books?|flag|flags?|publish|publishes?|loop\s+in|reach\s+out|let\s+\w+\s+know|set\s+(?:a|me\s+a)\s+reminder|set\s+up)\b",
    re.IGNORECASE,
)
V2_FIRST_PERSON = re.compile(
    r"\b(?:I|me|my|mine|myself|we|us|our|ours|I'?m|I'?ve|I'?ll|I'?d|let'?s|can\s+you|could\s+you|would\s+you|please)\b",
    re.IGNORECASE,
)
V3_VAGUE_CONNECTOR = re.compile(
    r"\b(?:such\s+as|for\s+example|e\.g\.,?|like)\s+[\"'`]?[A-Z\$\d]",
)
V7_MULTI_VALUE_AMBIGUOUS = re.compile(
    r"\b(?!or\b)[A-Za-z][\w\-\.@]*\s*,\s*(?!or\b)[A-Za-z][\w\-\.@]*(?:\s*,\s*(?!or\b)[A-Za-z][\w\-\.@]*)*\s*,?\s+or\s+[A-Za-z][\w\-\.@]*",
)
V7_MULTI_VALUE_CANONICAL = re.compile(
    r"\b(?:one\s+of|including\s+but\s+not\s+limited\s+to|at\s+least\s+one\s+of|must\s+be\s+one\s+of):?\s",
    re.IGNORECASE,
)

F1_BULLETS = re.compile(r"(?m)^[ \t]*[\u2022\u00b7\u2023\u25aa\u25cf*\-]\s+\S")
F2_MD_HEADER = re.compile(r"(?m)^[ \t]*#{1,6}\s+\S")
F3_MD_BOLD_ITALIC = re.compile(r"(?<!\w)(?:\*\*[^*\n]{1,80}\*\*|__[^_\n]{1,80}__|\*[A-Za-z][^*\n]{1,80}\*|_[A-Za-z][^_\n]{1,80}_)(?!\w)")
F4_CODE_BLOCK = re.compile(r"```")
F5_SECTION_HEADER = re.compile(
    r"(?im)^[ \t]*(?:Key\s+Points|Summary|Action\s+Items?|Background|Context|Objective|Deliverables?|Requirements?|Tasks?|Steps?|Overview|Goal):\s*$",
)
F6_AI_CLOSING = re.compile(
    r"\b(?:Let\s+me\s+know\s+if\s+you\s+need\s+anything\s+else|I\s+hope\s+this\s+helps|Happy\s+to\s+(?:assist|help)|Please\s+don'?t\s+hesitate|Don'?t\s+hesitate\s+to|Looking\s+forward\s+to\s+(?:your\s+response|hearing\s+back)|Thanks\s+in\s+advance\s+for\s+your\s+(?:help|assistance|cooperation)|Best\s+regards|Kind\s+regards)\b",
    re.IGNORECASE,
)
F7_AI_OPENING = re.compile(
    r"\b(?:As\s+(?:requested|discussed|per\s+(?:our|the))|Please\s+find\s+(?:below|attached|enclosed)|I\s+am\s+writing\s+to|Per\s+our\s+(?:discussion|conversation|earlier|previous)|Pursuant\s+to|Following\s+up\s+on\s+(?:our|my))\b",
    re.IGNORECASE,
)
F8_BLANK_LINE_PADDING = re.compile(r"\n{4,}")
F11_OE_REF = re.compile(r"\b(?:Per\s+OE\s*\d+|See\s+OE\s*\d+|OE\s*\d+\b)", re.IGNORECASE)
F11_TRAJECTORY_ANCHOR = re.compile(r"\b(?:Look\s+for|Check\s+(?:the|that|whether|whether)|Search\s+(?:for|the)|Verify\s+(?:that|the|whether)|Inspect|Confirm\s+(?:that|the)|Find\s+(?:the|a)|Examine|grep|trajectory|final\s+response|tool\s+call|payload)", re.IGNORECASE)
EMAIL_RE = re.compile(r"\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b", re.IGNORECASE)
MONEY_RE = re.compile(r"\$\s?(\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\d+(?:\.\d{2})?)")
JE_ID = re.compile(r"JE-[a-z_]+-FP-\d{4}-\d{2}-\d{4}")
EXC_ID = re.compile(r"\bexc_[a-f0-9]{14}\b")
RECON_ID = re.compile(r"\bBL-[A-F0-9]{12}\b")
DOC_ID = re.compile(r"\bdoc_[a-f0-9]{8}\b")
VENDOR_ID = re.compile(r"\bVEN-\d{3,4}(?:-[A-Za-z]+)?(?:-\d{3,6})?\b")
APINV_ID = re.compile(r"\bapinv_[a-f0-9]{14,16}\b")
RELATIVE_DATE = re.compile(r"\b(?:tomorrow|yesterday|today|next\s+(?:week|month|monday|tuesday|wednesday|thursday|friday|saturday|sunday)|last\s+(?:week|month|monday|tuesday|wednesday|thursday|friday|saturday|sunday)|\d+\s+days?\s+ago|in\s+\d+\s+days?|this\s+(?:week|month|quarter|morning|afternoon|evening))\b", re.IGNORECASE)
DATE_YMD = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
ACCOUNT_NUM = re.compile(r"(?<![\d.\-])\d{6}(?![\d.\-])")

# Prompt_Guidelines.md anti-patterns
QC_SAMPLE_CLICHE = re.compile(r"\b(?:go through everything and surface every|i need the full picture[:,]|dig through our emails,?\s+slack|email me the full|loop in [a-z]+|cc our ceo|flag the biggest risks|brief [a-z]+ and [a-z]+ with what you found)\b", re.IGNORECASE)
OVER_SIGNAL_INVESTIGATION = re.compile(r"\b(?:check our (?:messages|emails)[\s,]+slack[\s,]+(?:and project records|project tickets)|across (?:emails|email),?\s+slack[\s,]+linear|get into emails,?\s+slack[\s,]+linear|emails[\s,]+slack[\s,]+linear[\s,]+(?:crm|airtable))\b", re.IGNORECASE)
GENERIC_URGENCY = re.compile(r"\b(?:before it blows up|keeping me up at night|i can't tell you what the net position is|i'?m getting paged|something changed in the last few days)\b", re.IGNORECASE)

_ACTION_VERB_BASE = r"(?:dismiss|push(?:\s+(?:it\s+)?through)?|post|approve|deny|defer|escalate|reclassify|reverse|void|certify|sign[- ]off|forward|route|override|archive|reject|accept|hold|release|let\s+it\s+(?:go|pass))"
_NOUN_CONTEXT_SUFFIX = r"threads?|emails?|messages?|documents?|items?|forms?|records?|requests?|notices?|letters?|signatures?|notes?|status(?:es)?|process(?:es)?|paths?|flows?|chains?|fields?|columns?|attributes?|workflow|review|approval|rebill"
ACTION_AMBIGUITY = re.compile(
    rf"\b{_ACTION_VERB_BASE}\b[^.\n]{{0,40}}\s*(?:/|\s+or\s+)\s*\b{_ACTION_VERB_BASE}\b(?![\-\w]*[^.\n]{{0,30}}\b(?:{_NOUN_CONTEXT_SUFFIX})\b)",
    re.IGNORECASE,
)

# Rubric naturalness heuristics (from Archive/rubric_naturalness.py)
# SUBJECTIVE = FAIL: terms the QC spec explicitly bans in rubric criteria.
RUBRIC_SUBJECTIVE = re.compile(r"\b(?:enough|professional|thorough|helpful|properly|appropriately|sufficiently)\b|\bgood\s+(?:enough|job)\b", re.IGNORECASE)
# SOFT = WARN: non-agent voice or eval-internal language.
RUBRIC_SOFT_VOICE = re.compile(r"(?:the summary mentions|the email mentions|the response mentions|\(via\s|via the tool|\(visible in|trajectory shows|the model must use|as expected|should obviously)", re.IGNORECASE)
# NEGATION = WARN: awkward inverted phrasing.
RUBRIC_NEGATION = re.compile(r"(?:does not fail|never fails|must not be wrong)", re.IGNORECASE)

VALID_RETENTION_CODES = {"AICPA_SQMS_7Y", "IRS_TAX_7Y", "FIRM_INTERNAL", "INDEFINITE"}
VALID_CLASSIFICATIONS = {"public", "internal", "restricted"}
VALID_SLACK_CHANNELS = {f"C{n:03d}" for n in range(1, 11)} | {"C012"}
VALID_BL_EXCEPTION_TYPES = {
    "unrecorded_invoice",
    "duplicate_entry_detected",
    "timing_difference_over_sla",
    "subledger_feed_drop",
    "missing_accrual_variance",
    "fx_revaluation_drift",
}
RETENTION_CODE_REF = re.compile(r"retention_policy_code\s*[:=]\s*['\"]?([A-Z][A-Z0-9_]*)['\"]?", re.IGNORECASE)
CLASSIFICATION_REF = re.compile(r"\bclassification\s*[:=]\s*['\"]?(\w+)['\"]?", re.IGNORECASE)
SLACK_CHANNEL_REF = re.compile(r"\b(C\d{3})\b")
BL_EXCEPTION_TYPE_REF = re.compile(r"\bexception_type\s*[:=]\s*['\"]?(\w+)['\"]?", re.IGNORECASE)

COMMAND_LIST_SEQUENTIAL = re.compile(r"\b(?:First[,:]?\s+[A-Z]|Then[,:]?\s+[A-Z]|Finally[,:]?\s+[A-Z])\w*\b")
COMMAND_LIST_NUMBERED = re.compile(r"(?m)^\s*\d+\.\s+[A-Z]\w+\b")
WRITE_VERB_IN_TITLE = re.compile(r"^The\s+Agent\s+(sends?|creates?|posts?|uploads?|updates?|certifies|approves?|denies?|reverses?|voids?|forwards?|submits?|adds?|writes?|files?)\b", re.IGNORECASE)
_AGENT_VERB_BASE = r"(?:sends?|creates?|posts?|uploads?|updates?|certifies|approves?|denies?|reverses?|voids?|forwards?|submits?|adds?|writes?|files?|identifies|reports?|lists?|states?|mentions?|notifies|schedules?|includes?|recommends?|concludes?|flags?|confirms?|verifies)"
AND_BUNDLING = re.compile(rf"^The\s+Agent\s+{_AGENT_VERB_BASE}\b[^.]+?\sAND\s+{_AGENT_VERB_BASE}\b", re.IGNORECASE)

OPEN_GOAL_VERBS = re.compile(r"\b(?:notify|reach\s+out|let\s+\w+\s+know|update|inform|loop\s+in|brief|alert|flag|sync\s+with)\b", re.IGNORECASE)
CHANNEL_LOCK_VERBS_EMAIL = re.compile(r"^The\s+Agent\s+(?:sends?\s+an?\s+email|emails|writes\s+an?\s+email)\b", re.IGNORECASE)
CHANNEL_LOCK_VERBS_SLACK = re.compile(r"^The\s+Agent\s+(?:posts?\s+(?:in|to)\s+(?:#|the\s+)?[a-zA-Z_-]+\s+(?:channel|slack)|sends?\s+a?\s+slack\s+message)\b", re.IGNORECASE)
KNOWN_NPCS = {"Owen Mercer", "Brenda Abbas", "Sofia Halabi", "Farah Dlamini", "James Randall", "Lucia Ferreira", "Mateo Kovac"}
NAMED_ENTITY_RE_PROMPT = re.compile(r"\b[A-Z][a-z]{2,}(?:\s+[A-Z][a-z]+)*\b|\$\d[\d,]*(?:\.\d+)?\b|\b[A-Z]{2,}-[A-Z0-9-]+\b|\b\d{4}-\d{2}-\d{2}\b")
RUBRIC_VALUE_TOKENS = re.compile(r"\d{4}-\d{2}-\d{2}|\$[\d,]+(?:\.\d+)?|\b[A-Z]{2,}-[A-Z0-9-]+\b|\bexc_[a-f0-9]+\b|\bapinv_[a-f0-9]+\b|\bdoc_[a-f0-9]+\b|\bJE-[a-z_]+-FP-\d{4}-\d{2}-\d{4}\b")

# StarPM (V4) ID shapes, selected when detect_universe() == "starpm". The
# Brookfield regexes above stay the default for brookfield/keystone/moveops
# (byte-identical); only starpm routes through these.
STARPM_AIRTABLE_REC = re.compile(r"\brec[a-f0-9]{14,16}\b")
STARPM_LINEAR_ISSUE = re.compile(r"\bOPS-\d{1,4}\b")
STARPM_HUBSPOT_OBJ = re.compile(r"\b(?:deal|contact|ticket|comp|engagement)_[a-z0-9]{6,40}\b")
STARPM_INTERNAL_ID = re.compile(r"\b(?:rec[a-f0-9]{14,16}|OPS-\d{1,4}|(?:deal|contact|ticket|comp|engagement)_[a-z0-9]{6,40}|comment_[a-f0-9]{32}|INV-2026-\d{3,7}(?:-\d{2,4})?|BILL-2026-\d{3,7})\b")
STARPM_VALUE_TOKENS = re.compile(r"\d{4}-\d{2}-\d{2}|\$[\d,]+(?:\.\d+)?|\brec[a-f0-9]{14,16}\b|\bOPS-\d{1,4}\b|\b(?:deal|contact|ticket|comp|engagement)_[a-z0-9]{6,40}\b|\b(?:INV|BILL)-2026-\d{3,7}(?:-\d{2,4})?\b")
# HarmonyGames. Opaque IDs only: Slack C*/U*, Trello 24-hex, Drive file ids. A
# team-prefixed Linear key (ENG-2400) reads like a JIRA key a person would say aloud,
# so it is NOT leakage - but it IS groundable, hence its presence below.
HG_SLACK_CHANNEL = re.compile(r"\bC[0-9A-Z]{10}\b")
HG_SLACK_USER = re.compile(r"\bU[0-9A-Z]{10}\b")
HG_TRELLO_CARD = re.compile(r"\b[a-f0-9]{24}\b")
HG_GDRIVE_FILE = re.compile(r"\b1[A-Za-z0-9_-]{25,}\b")
HG_LINEAR_ISSUE = re.compile(r"\b(?:ENG|ZOM|EVT|DES|ART|EPI|LATE)-\d{2,5}\b")
HG_INTERNAL_ID = re.compile(
    r"\b(?:C[0-9A-Z]{10}|U[0-9A-Z]{10}|[a-f0-9]{24}|1[A-Za-z0-9_-]{25,})\b"
)
HG_GROUNDING = [
    (HG_LINEAR_ISSUE, "Linear issue", "linear_issue"),
    (HG_TRELLO_CARD, "Trello card", "trello_card"),
    (HG_GDRIVE_FILE, "Drive file", "gdrive_file"),
]

STARPM_GROUNDING = [
    (STARPM_AIRTABLE_REC, "airtable record", "airtable_record"),
    (STARPM_LINEAR_ISSUE, "linear issue", "linear_issue"),
    (STARPM_HUBSPOT_OBJ, "hubspot object", "hubspot_object"),
]


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


def load_tool_names(tool_catalog_path: Path = None) -> set:
    if tool_catalog_path is None:
        tool_catalog_path = ROOT / "Brookfield_Base_Universe" / "8_Server_Tools_Details.json"
    if not Path(tool_catalog_path).is_file():
        return set()
    with open(tool_catalog_path, "r", encoding="utf-8") as f:
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


def load_tool_param_map(tool_catalog_path: Path = None) -> dict:
    if tool_catalog_path is None:
        tool_catalog_path = ROOT / "Brookfield_Base_Universe" / "8_Server_Tools_Details.json"
    if not Path(tool_catalog_path).is_file():
        return {}
    with open(tool_catalog_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    out: dict = {}

    def walk(node):
        if isinstance(node, dict):
            tool_name = node.get("name") or node.get("tool_name") or node.get("function_name")
            params = node.get("parameters") or node.get("params") or node.get("inputSchema") or node.get("input_schema")
            if isinstance(tool_name, str) and params is not None:
                param_names = set()
                if isinstance(params, dict):
                    props = params.get("properties") if isinstance(params.get("properties"), dict) else params
                    if isinstance(props, dict):
                        param_names.update(k for k in props.keys() if isinstance(k, str) and not k.startswith("_"))
                elif isinstance(params, list):
                    for p in params:
                        if isinstance(p, dict):
                            n = p.get("name")
                            if isinstance(n, str):
                                param_names.add(n)
                if param_names:
                    out[tool_name] = param_names
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for it in node:
                walk(it)

    walk(data)
    return out


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


def load_fact_ledger(task_dir: Path) -> dict:
    f = task_dir / "_aux" / "Fact_Ledger.json"
    if not f.is_file():
        return {}
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def amount_in_ledger(amt_raw: str, ledger: dict) -> bool:
    if not ledger.get("amounts"):
        return False
    amt = amt_raw.replace(" ", "").lstrip("$").replace(",", "")
    try:
        d = Decimal(amt).quantize(Decimal("0.01"))
    except (InvalidOperation, ValueError):
        return False
    target = str(d)
    return target in ledger["amounts"]


def check_oe_param_traps(text: str, consts: dict, rep: Report) -> None:
    # Registry-driven OE parameter-trap checks (was hardcoded for Brookfield only).
    # Reproduces the legacy checks byte-for-byte via per-trap window/ignorecase in
    # consts["tool_param_traps"] (email/slack window 80 case-sensitive; records_vault
    # window 100 case-insensitive; linear window 100) and extends per universe.
    # content_field + wrong_field(s) => "uses W should be content_field"; required +
    # wrong => "uses W should be required".
    traps = consts.get("tool_param_traps", {}) or {}
    for tool, spec in traps.items():
        window = spec.get("window", 80)
        flags = re.IGNORECASE if spec.get("ignorecase") else 0
        content_field = spec.get("content_field")
        wrong_fields = []
        if spec.get("wrong_field"):
            wrong_fields.append(spec["wrong_field"])
        wrong_fields.extend(spec.get("wrong_fields", []) or [])
        if content_field:
            for wf in wrong_fields:
                if re.search(rf"{re.escape(tool)}[^.\n]{{0,{window}}}\b{re.escape(wf)}\s*[:=]", text, flags):
                    rep.fail(f"{tool} uses `{wf}` — should be `{content_field}`")
        required = spec.get("required")
        wrong = spec.get("wrong")
        if required and wrong:
            if re.search(rf"{re.escape(tool)}[^.\n]{{0,{window}}}\b{re.escape(wrong)}\s*[:=]", text, flags):
                rep.fail(f"{tool} uses `{wrong}` — should be `{required}`")


def validate_prompt(task_dir: Path, rep: Report) -> None:
    f = task_dir / "5_Prompt.txt"
    if not f.is_file():
        rep.fail(f"missing {_rel(f)}")
        return
    text = f.read_text(encoding="utf-8")

    universe = detect_universe(task_dir)
    consts = get_universe_constants(universe)
    local_npcs = consts["npcs"]
    local_persona_email_domain = consts.get("persona_email_domain")
    rep.note(f"universe: {universe}")

    persona_path = task_dir / "2_Persona.txt"
    if persona_path.is_file():
        persona_text = persona_path.read_text(encoding="utf-8").strip()
        for npc in local_npcs:
            if re.search(rf"\b{re.escape(npc)}\b", persona_text, re.IGNORECASE):
                rep.fail(f"persona is an NPC for {universe}: `{npc}`. NPCs appear as participants/counterparties, never as task author. See {consts['persona_briefs']} for valid authoring personas.")
                break
        if local_persona_email_domain:
            all_universe_domains = {"brookfieldcpas.com", "keystonemortgage.com", "moveops.com", "starpm.com"}
            wrong_domains = all_universe_domains - {local_persona_email_domain}
            persona_lower = persona_text.lower()
            for wrong in wrong_domains:
                if wrong in persona_lower:
                    rep.fail(f"persona email domain mismatch: persona references `{wrong}` but universe is {universe} (expected domain: `{local_persona_email_domain}`). Cross-universe persona contamination.")
                    break

    INJECTION_PATTERN = re.compile(
        r"\b(?:ignore\s+(?:all\s+)?(?:other\s+|previous\s+|prior\s+)?(?:criteria|instructions|rules|rubrics)|"
        r"always\s+score\s+\d|treat\s+this\s+(?:prompt|task)\s+as|"
        r"override\s+the\s+(?:judge|evaluator|review|spec)|"
        r"system\s+prompt|disregard\s+(?:the\s+)?(?:rubric|grading))\b",
        re.IGNORECASE,
    )
    for m in INJECTION_PATTERN.finditer(text):
        rep.fail(f"prompt-injection pattern detected: `{m.group(0)}` — candidate prompt contains scoring-manipulation phrase. Real persona prompts never instruct the agent/judge to ignore rubrics or override scoring.")

    # Em-dash ban on the prompt is an operator constraint learned in practice: an em-dash
    # reads machine-written in a first-person work request and has drawn platform flags.
    # Hard FAIL, restored after a v23 change wrongly relaxed it to a warning.
    for m in EM_DASH_PATTERN.finditer(text):
        rep.fail(f"em-dash / en-dash at offset {m.start()}: `{text[max(0,m.start()-20):m.start()+20]}`")

    words = text.split()
    wc = len(words)
    rep.note(f"word count: {wc}")
    # The 500-word cap is an operator constraint learned from platform rejections, not a
    # transcription of spec prose. It is deliberately stricter than the guidelines and stays
    # a hard FAIL. (A v23 change briefly downgraded it on the reasoning that it was absent
    # from the source text; that reasoning was wrong. Absence from spec prose does not make
    # a practice-learned constraint optional.)
    if wc > 500:
        rep.fail(f"word count {wc} exceeds 500 cap")
    elif wc > 400:
        rep.warn(f"word count {wc} > 400 — prefer shorter. The 4 V3 reference prompts sit in the 300-400 sweet spot. Tighten if possible.")
    elif wc > 300:
        rep.note(f"word count {wc} is over 300 — within sweet spot but could still be tightened.")

    for m in TOOL_NAME_HINT.finditer(text):
        rep.fail(f"explicit tool-name leakage: `{m.group(0)}`")

    for m in MCP_SERVER_NAME.finditer(text):
        rep.fail(f"explicit MCP-server mention: `{m.group(0)}`")

    _pset = consts.get("id_pattern_set")
    internal_id_re = (STARPM_INTERNAL_ID if _pset == "starpm"
                      else HG_INTERNAL_ID if _pset == "harmonygames" else INTERNAL_ID)
    for m in internal_id_re.finditer(text):
        rep.fail(f"internal-ID leakage: `{m.group(0)}`")

    for m in PRE_SOLVE_HINT.finditer(text):
        rep.warn(f"possible pre-solve phrase: `{m.group(0)}` (review by hand)")

    ledger_for_date = load_fact_ledger(task_dir)
    today_from_ledger = ledger_for_date.get("lifecycle", {}).get("today") or "2026-06-12"
    for m in RELATIVE_DATE.finditer(text):
        rep.note(f"relative date: `{m.group(0)}` — resolve against universe today `{today_from_ledger}` per Fact_Ledger.lifecycle (single date-alignment source for prompt + OE + rubrics). Verify the resolved window contains universe records for the ask.")

    # Prompt_Guidelines.md anti-patterns (warn, do not fail)
    for m in QC_SAMPLE_CLICHE.finditer(text):
        rep.warn(f"QC sample cliché phrase: `{m.group(0)}` (avoid mass-produced tonality)")
    for m in OVER_SIGNAL_INVESTIGATION.finditer(text):
        rep.warn(f"over-signaling the investigation: `{m.group(0)}` (real persona would not inventory their own systems)")
    for m in GENERIC_URGENCY.finditer(text):
        rep.warn(f"generic urgency framing: `{m.group(0)}` (ground urgency in specific consequences)")

    for m in ACTION_AMBIGUITY.finditer(text):
        rep.fail(f"action-decision ambiguity: `{m.group(0)}` — prompt offers multiple action paths without explicit decision criteria. Either pick one OR add explicit criteria ('dismiss IF X otherwise reclassify'). Unique Ground Truth requires a single end-state, and the platform reviewer flags this as Major Clarity / Action Decision Ambiguity.")

    for m in P2_CONFLICTING.finditer(text):
        rep.fail(f"feasibility — conflicting instructions: `{m.group(0)[:80]}...` — prompt asks the agent to do AND not do the same thing. Resolve the contradiction or remove one side.")
    for m in P2_IMPOSSIBLE_FUTURE.finditer(text):
        rep.fail(f"feasibility — impossible-future ask: `{m.group(0)}` — prompt asks about an event in the future relative to universe today. Adjust the timeframe.")

    distinct_services = sum(1 for name, pat in SERVICE_KEYWORDS.items() if pat.search(text))
    rep.note(f"distinct services referenced: {distinct_services}")
    if distinct_services <= 1:
        rep.fail(f"cross-service requirement — prompt references {distinct_services} distinct service(s) in its body. QC spec Tool-Use & Cross-Service requires investigation across 2+ services (single-service prompts can be trivially answered). Re-frame the ask to span multiple services.")

    has_investigation = bool(V1_INVESTIGATION_CUES.search(text))
    has_action = bool(V1_ACTION_VERBS.search(text))
    if not has_investigation and not has_action:
        rep.fail("Investigation + Action two-phase — prompt has neither investigation language nor action verbs. QC spec requires both phases: 'figure out what's happening' AND 'do something about it'. Add investigation cues (figure out / look into / find out / check) and action verbs (send / post / create / approve / file).")
    elif not has_investigation:
        rep.warn("Investigation + Action two-phase — prompt has action verbs but no clear investigation language. The richest tasks have BOTH phases. Add investigation cues (figure out / look into / find out / check / tell me where) if the task requires discovery.")
    elif not has_action:
        rep.warn("Investigation + Action two-phase — prompt has investigation language but no clear action verb. The richest tasks have BOTH phases. Add ≥1 write action (send / post / create / approve / file) if the task should end in a workplace action.")

    if not V2_FIRST_PERSON.search(text):
        rep.fail("first-person voice — prompt contains no first-person pronouns (I / me / my / we / our / let's / can you / please). QC spec Core Requirement #6 requires natural-voice prompts that read like a real message from persona to AI assistant. Rewrite from a first-person perspective.")

    for m in F1_BULLETS.finditer(text):
        line_no = text.count("\n", 0, m.start()) + 1
        rep.fail(f"formatting — bullet at line {line_no}: `{m.group(0).strip()}...`. Real persona prompts are plain prose; bullets read as AI-generated structure. Rewrite as natural sentences.")
        break
    for m in F2_MD_HEADER.finditer(text):
        line_no = text.count("\n", 0, m.start()) + 1
        rep.fail(f"formatting — markdown header at line {line_no}: `{m.group(0).strip()[:60]}`. Prompts must be plain prose with no markdown headers. Remove the # and integrate the section content.")
        break
    for m in F3_MD_BOLD_ITALIC.finditer(text):
        rep.fail(f"formatting — markdown bold/italic: `{m.group(0)}`. Prompts must be plain prose with no markdown emphasis. Use natural sentence stress instead.")
        break
    if F4_CODE_BLOCK.search(text):
        rep.fail("formatting — code block fence (```) in prompt. Real persona prompts don't contain code blocks. Remove the fence; if a specific value matters, embed it inline in prose.")
    for m in F5_SECTION_HEADER.finditer(text):
        rep.fail(f"formatting — AI-style section header `{m.group(0).strip()}`. Real persona prompts are continuous prose, not structured documents with `Key Points:` / `Summary:` / `Action Items:` sub-headers. Rewrite as natural prose.")
        break
    for m in F6_AI_CLOSING.finditer(text):
        rep.fail(f"formatting — AI-style closing `{m.group(0)}`. Real persona prompts don't use formal email-closer phrases. Drop the closing or replace with natural conversational ending.")
        break
    for m in F7_AI_OPENING.finditer(text):
        rep.fail(f"formatting — AI-style opening `{m.group(0)}`. Real persona prompts start mid-thought, not with formal email-opener phrases. Rewrite to enter the prompt situationally.")
        break
    if F8_BLANK_LINE_PADDING.search(text):
        rep.warn("formatting — 3+ consecutive blank lines detected. This is an AI-formatting padding tell. Collapse to single blank line between paragraphs.")

    for m in P5_EXACT_TIMESTAMP.finditer(text):
        rep.warn(f"contrived — exact-timestamp demand: `{m.group(0)}` — natural prompts say 'last week's email from Andrea' not 'the email from January 15th at 3:47 PM'. Soften or remove.")
    for m in P5_ARBITRARY_FORMAT.finditer(text):
        rep.warn(f"contrived — arbitrary format constraint: `{m.group(0)}` — real users don't impose response-format rules. Drop the constraint unless it's the actual task.")
    for m in P5_TEST_ERROR_HANDLING.finditer(text):
        rep.fail(f"contrived — error-handling test: `{m.group(0)[:80]}...` — prompt asks the agent to intentionally trigger errors. Real users don't ask employees to do this; remove or rewrite as a genuine investigation.")

    for m in COMMAND_LIST_SEQUENTIAL.finditer(text):
        rep.fail(f"command-list detection: sequential instruction `{m.group(0)}` — prompt prescribes step-by-step procedure. Real users phrase asks as natural prose, not numbered playbooks. Rewrite as a coherent ask.")
    for m in COMMAND_LIST_NUMBERED.finditer(text):
        rep.fail(f"command-list detection: numbered step `{m.group(0)}` — prompt lists numbered steps. Rewrite as a coherent ask, not a step-by-step procedure.")

    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip() and len(s.strip()) > 20]
    pronoun_skip = {"The", "If", "When", "Can", "Will", "Would", "Should", "Could", "Please", "Also", "But", "And", "Or", "So", "Now", "Then", "Just", "I", "A", "An", "It", "Here", "There", "This", "That"}
    sentence_ents = []
    for s in sentences:
        ents = set(NAMED_ENTITY_RE_PROMPT.findall(s))
        ents -= pronoun_skip
        sentence_ents.append((s, ents))
    for i_s, (s, ents) in enumerate(sentence_ents):
        if len(ents) < 2:
            continue
        other_ents = set()
        for j_s, (_, e2) in enumerate(sentence_ents):
            if j_s != i_s:
                other_ents |= e2
        if not (ents & other_ents):
            rep.warn(f"bolt-on candidate: sentence `{s[:80]}...` shares no named entities with the rest of the prompt. Apply remove-sentence test — if the rest still makes sense, it's a coherence violation (Major).")


def validate_oe(task_dir: Path, rep: Report) -> None:
    f = task_dir / "6_Oracle_Events.txt"
    if not f.is_file():
        rep.fail(f"missing {_rel(f)}")
        return
    text = f.read_text(encoding="utf-8")

    universe = detect_universe(task_dir)
    consts = get_universe_constants(universe)
    # HarmonyGames adds a parameterized BATCH OE form for long-horizon work
    # (Evals_harmonygames/2). Universes whose grammar is ['standard'] must still
    # reject it, so the allowance is read from the profile rather than assumed.
    _oe_grammar = get_framework_profile(universe).get("oe_grammar", ["standard"])

    def _check_oe_grammar(oe_text: str) -> None:
        """A BATCH / parameterized OE is legal only where the profile declares it.

        HarmonyGames adds the form for long-horizon work; the other four universes have no
        such grammar, so a BATCH OE there is a malformed OE rather than an advanced one.
        Gating on the flag is what makes the flag mean something.
        """
        batch = re.findall(r"^\s*OE\s*\d+\s*[-\u2014]+\s*BATCH\b.*$", oe_text, re.MULTILINE)
        if batch and "batch" not in _oe_grammar:
            for b in batch[:3]:
                rep.fail(f"BATCH OE form is not part of this universe's OE grammar "
                         f"({_oe_grammar}): {b.strip()[:90]}")
        if batch and "batch" in _oe_grammar:
            for b in batch:
                if not re.search(r"\bvary\b|\bover each\b|\bfor each\b", b, re.IGNORECASE):
                    rep.fail(f"BATCH OE states no varied cohort, so its call count is "
                             f"unverifiable: {b.strip()[:90]}")
                elif not re.search(r"Calls?\s*:\s*\d+", b, re.IGNORECASE):
                    rep.warn(f"BATCH OE states no explicit call count: {b.strip()[:90]}")

    _check_oe_grammar(text)
    local_retention_codes = consts["retention_codes"]
    local_slack_channels = consts["slack_channels"]
    local_classifications = consts["classifications"]
    local_bl_exception_types = consts["blackline_exception_types"]
    local_tool_catalog = ROOT / consts["tool_catalog"]
    rep.note(f"universe: {universe}")

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

    tool_names = load_tool_names(local_tool_catalog)
    if not tool_names:
        rep.warn(f"could not load {local_tool_catalog.name} — skipping tool-name existence check")
    else:
        referenced = set(TOOL_NAME_HINT.findall(text))
        unknown = sorted(t for t in referenced if t not in tool_names)
        for t in unknown:
            rep.fail(f"OE references unknown tool: `{t}` (not in {local_tool_catalog.name})")

    check_oe_param_traps(text, consts, rep)

    if local_retention_codes:
        for m in RETENTION_CODE_REF.finditer(text):
            code = (m.group(1) or "").upper()
            if code and code not in local_retention_codes:
                line_no = text.count("\n", 0, m.start()) + 1
                rep.fail(f"line {line_no}: retention code `{code}` not in valid set {{{', '.join(sorted(local_retention_codes))}}}.")

    if local_slack_channels:
        for m in SLACK_CHANNEL_REF.finditer(text):
            chan = m.group(1)
            if chan and chan not in local_slack_channels:
                line_no = text.count("\n", 0, m.start()) + 1
                rep.fail(f"line {line_no}: Slack channel `{chan}` not in valid range for {universe}. Valid: {sorted(local_slack_channels)}.")

    if local_classifications:
        for m in CLASSIFICATION_REF.finditer(text):
            cls = (m.group(1) or "").lower()
            if cls and cls not in local_classifications:
                line_no = text.count("\n", 0, m.start()) + 1
                rep.fail(f"line {line_no}: classification `{cls}` not in {{{', '.join(sorted(local_classifications))}}}.")

    if local_bl_exception_types:
        for m in BL_EXCEPTION_TYPE_REF.finditer(text):
            ex_type = (m.group(1) or "").lower()
            if ex_type and ex_type not in local_bl_exception_types:
                line_no = text.count("\n", 0, m.start()) + 1
                rep.warn(f"line {line_no}: BlackLine exception type `{ex_type}` not in known set ({', '.join(sorted(local_bl_exception_types))}). Verify against universe data.")

    tool_param_map = load_tool_param_map(local_tool_catalog)
    oe_steps_split = re.split(r"(?m)(?=^OE\s*\d+)", text)
    oe_steps_indexed = [s for s in oe_steps_split if re.match(r"^OE\s*\d+", s)]
    param_to_tools: dict = {}
    if tool_param_map:
        for tool, params in tool_param_map.items():
            for p in params:
                param_to_tools.setdefault(p, set()).add(tool)
    if tool_param_map:
        param_binding_patterns = [
            re.compile(r"\b(?:with|using|pass(?:ing)?|set(?:ting)?|bind(?:ing)?|provid(?:ing|e))\s+(?:the\s+|a\s+|`)?([a-z][a-z0-9_]*_[a-z0-9_]+)", re.IGNORECASE),
            re.compile(r"\b(?:parameter|param|argument|arg)\s+`?([a-z][a-z0-9_]*_[a-z0-9_]+)`?", re.IGNORECASE),
            re.compile(r"`([a-z][a-z0-9_]*_[a-z0-9_]+)`\s*(?:[:=]|to\s)", re.IGNORECASE),
            re.compile(r"\bbind\s+`?([a-z][a-z0-9_]*_[a-z0-9_]+)`?\s+(?:to|on)\b", re.IGNORECASE),
        ]
        for i, step in enumerate(oe_steps_indexed, 1):
            tools_in_step = set(TOOL_NAME_HINT.findall(step)) & set(tool_param_map.keys())
            if not tools_in_step:
                continue
            bound_params = set()
            for pat in param_binding_patterns:
                bound_params.update(pat.findall(step))
            suspect_params = bound_params & set(param_to_tools.keys())
            for param in suspect_params:
                valid_tools_for_param = param_to_tools[param]
                if not (tools_in_step & valid_tools_for_param):
                    tool_list = sorted(tools_in_step)
                    allowed = sorted(valid_tools_for_param)[:3]
                    overflow = "..." if len(valid_tools_for_param) > 3 else ""
                    rep.fail(f"OE step {i}: parameter `{param}` bound to tool(s) {tool_list}, but `{param}` exists only on {allowed}{overflow}. Wrong tool binding — bind to the correct tool, or use a different parameter that exists on the named tool.")
    else:
        rep.warn("could not load per-tool parameter map from 8_Server_Tools_Details.json — skipping per-tool param strictness check")

    ledger = load_fact_ledger(task_dir)
    lifecycle = ledger.get("lifecycle", {})
    closed_periods = set(lifecycle.get("closed_periods", []))
    if closed_periods:
        for i, step in enumerate(oe_steps_indexed, 1):
            # Does this step describe posting a JE?
            has_post_action = (
                bool(re.search(r"\bpost(?:s|ing|ed)?\b[^.\n]{0,100}\b(?:journal\s+entry|JE)\b", step, re.IGNORECASE))
                or "_post_journal_entry" in step
                or bool(re.search(r"\bpost(?:s|ing|ed)?\b[^.\n]{0,100}\bJE-", step, re.IGNORECASE))
            )
            if not has_post_action:
                continue
            periods_in_step = [pid for pid in closed_periods if pid in step]
            if not periods_in_step:
                continue
            prior_text = "".join(oe_steps_indexed[: i - 1])
            for pid in periods_in_step:
                has_unlock = bool(re.search(rf"\bunlock(?:s|ing|ed)?\b[^.\n]{{0,100}}\b{re.escape(pid)}\b", prior_text, re.IGNORECASE))
                has_late_post_auth = "late_post_authorization_id" in step
                if not (has_unlock or has_late_post_auth):
                    rep.fail(f"OE step {i}: posts to closed period `{pid}` without an earlier unlock step OR a `late_post_authorization_id` parameter on the post call. Lifecycle precondition missing — the post will fail with `OGL.PERIOD_CLOSED` on all platform runs.")
    elif lifecycle:
        rep.note("no closed fiscal periods in Fact_Ledger.lifecycle.closed_periods — skipping lifecycle precondition check")

    for i, step in enumerate(oe_steps_indexed, 1):
        if re.search(r"\b(?:sends?\s+(?:an?\s+)?email|email_send_email)\b", step, re.IGNORECASE):
            emails_in_step = EMAIL_RE.findall(step)
            if emails_in_step:
                prior_text = "".join(oe_steps_indexed[:i - 1])
                has_lookup = bool(re.search(r"\b(?:look\s+up|contacts?_(?:search|list|get)|find\s+(?:the\s+)?contact|resolve\s+(?:the\s+)?(?:email|recipient)|get\s+(?:the\s+)?(?:contact|email))\b", prior_text, re.IGNORECASE))
                if not has_lookup:
                    rep.warn(f"OE step {i}: sends email to {emails_in_step[0]} but no earlier OE step performs a contact lookup. Dependency chain: typically needs contact-lookup step (contacts_search_contacts or similar) before the send.")

    if oe_steps_indexed and len(oe_steps_indexed) >= 3:
        pronoun_skip_oe = {"The", "If", "When", "Can", "Will", "Would", "Should", "Could", "Please", "Also", "But", "And", "Or", "So", "Now", "Then", "Just", "I", "A", "An", "It", "Here", "There", "This", "That", "OE", "Search", "Send", "Post", "Verify", "Use", "Call", "Look", "Lookup", "Query", "Pull", "Fetch", "Load", "Create", "Update", "Upload", "Add", "Confirm", "Schedule", "Retrieve", "Get", "List", "Check", "Read", "Identify", "Determine", "Filter", "Decide", "Find", "Inspect", "Review", "Compare", "Compute", "Calculate", "Reply", "Forward", "Notify", "Approve", "Reject", "Submit", "Certify", "Archive", "Dismiss", "Next", "Finally", "Optionally", "Resolve", "Write", "Draft", "Log", "Mark", "Set", "Reach"}
        step_ents = []
        for s in oe_steps_indexed:
            ents = set(NAMED_ENTITY_RE_PROMPT.findall(s))
            ents -= pronoun_skip_oe
            step_ents.append((s, ents))
        for idx, (s, ents) in enumerate(step_ents, 1):
            if len(ents) < 2:
                continue
            other_ents = set()
            for j_s, (_, e2) in enumerate(step_ents):
                if j_s != idx - 1:
                    other_ents |= e2
            if not (ents & other_ents):
                head = re.match(r"^OE\s*\d+:?\s*([^\n]{0,80})", s)
                head_str = head.group(1).strip() if head else s[:60].strip()
                rep.warn(f"OE step {idx}: bolt-on candidate — `{head_str}...` shares no named entities with any other OE step. Apply remove-step test: if the rest of the OE chain still makes sense, this is a Coherence violation.")

    or_similar_pat = re.compile(r"`?\b([a-z][a-z0-9_]+)`?\s*\(or\s+similar\)", re.IGNORECASE)
    for m in or_similar_pat.finditer(text):
        tool = m.group(1)
        if tool_names and tool not in tool_names:
            continue
        parts = tool.split("_")
        if len(parts) < 3:
            continue
        server_prefix = "_".join(parts[:2])
        if tool_names:
            same_server_tools = [t for t in tool_names if t.startswith(server_prefix + "_") and t != tool]
            if len(same_server_tools) < 1:
                rep.warn(f"OE: `{tool} (or similar)` claim — no other tools exist in `{server_prefix}_*` server. The (or similar) flexibility claim is hollow.")

    meta_tag_patterns = [
        (re.compile(r"(?:^|\n)\s*(?:[\u2192>\-]+\s*)?(?:Write\s+action|Read\s+action|Read/lookup\s+action|Read\s*/\s*lookup\s+action)\s*[\u2192>\-]"), "meta tag (Write action / Read action / Read-lookup arrow)"),
        (re.compile(r"(?:^|\n)\s*(?:[\u2192>\-]+\s*)?Outcome\s+\d+\.\d+\s*[:\u2192>\-]"), "meta tag (Outcome 1.1/1.2/2.1 inline in OE body)"),
        (re.compile(r"(?:^|\n)\s*(?:[\u2192>\-]+\s*)?Process\s+rubric\s*[:\u2192>\-]"), "meta tag (Process rubric inline in OE body)"),
    ]
    for pat, label in meta_tag_patterns:
        for m in pat.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            rep.fail(f"OE line {line_no}: {label} appears in OE body — meta-tags belong in reasoning files, not 6_Oracle_Events.txt. Remove the tag, keep the action description.")

    for m in F1_BULLETS.finditer(text):
        line_no = text.count("\n", 0, m.start()) + 1
        if not re.match(r"^\s*OE\s*\d+:", text[m.start():m.start() + 30], re.IGNORECASE):
            rep.fail(f"OE line {line_no}: formatting — bullet character at line start (`{m.group(0).strip()}`). OE steps are numbered prose (`OE<n>: ...`), not bulleted lists. Convert to the OE<n> format.")
            break
    for m in F3_MD_BOLD_ITALIC.finditer(text):
        line_no = text.count("\n", 0, m.start()) + 1
        rep.fail(f"OE line {line_no}: formatting — markdown bold/italic `{m.group(0)}`. OE steps are plain prose; remove markdown emphasis.")
        break
    for m in F2_MD_HEADER.finditer(text):
        line_no = text.count("\n", 0, m.start()) + 1
        rep.fail(f"OE line {line_no}: formatting — markdown header `{m.group(0).strip()[:60]}`. OE steps are plain prose with no section headers; convert to OE<n> numbered steps.")
        break

    oe_service_map = consts.get("oe_service_map", {}) or {}
    local_services = sorted(set(consts.get("services", []) or []), key=len, reverse=True)
    oe_steps_x3 = re.split(r"(?m)^OE\s*\d+\s*[:.\)]\s*", text)
    oe_steps_x3 = [s.strip() for s in oe_steps_x3 if s.strip()]
    if oe_service_map and local_services and oe_steps_x3:
        for step_idx, step in enumerate(oe_steps_x3, 1):
            tools_in_step = set(TOOL_NAME_HINT.findall(step))
            if not tools_in_step:
                continue
            step_services = set()
            for tool in tools_in_step:
                for svc in local_services:
                    if tool.startswith(svc + "_"):
                        step_services.add(svc)
                        break
            if not step_services:
                continue
            step_lc = step.lower()
            flagged_for_step = set()
            for data_type, expected_service in oe_service_map.items():
                if expected_service in flagged_for_step:
                    continue
                if not re.search(rf"\b{re.escape(data_type)}\b", step_lc):
                    continue
                if expected_service in step_services:
                    continue
                rep.warn(f"OE step {step_idx} (X3 service-mapping): step text references `{data_type}` (expected service `{expected_service}` per {universe} oe_service_map) but tool call(s) target service(s) {sorted(step_services)}. Verify the right service is being used for this data type. WARN-only observation period.")
                flagged_for_step.add(expected_service)


def _canonical_category(value: str) -> str:
    """Thin alias. The implementation lives in universes.canonical_rubric_category so
    validate.py and v4_gates.py cannot drift apart on rubric-balance counting."""
    return canonical_rubric_category(value)


def validate_rubrics(task_dir: Path, rep: Report) -> None:
    f = task_dir / "7_Rubrics.json"
    if not f.is_file():
        rep.fail(f"missing {_rel(f)}")
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
    prompt_raw = ""
    pf = task_dir / "5_Prompt.txt"
    if pf.is_file():
        prompt_raw = pf.read_text(encoding="utf-8")
        prompt_text = prompt_raw.lower()

    universe = detect_universe(task_dir)
    consts = get_universe_constants(universe)
    _fw_profile = get_framework_profile(universe)
    local_retention_codes = consts["retention_codes"]
    local_slack_channels = consts["slack_channels"]
    local_classifications = consts["classifications"]
    local_bl_exception_types = consts["blackline_exception_types"]
    local_tool_catalog = ROOT / consts["tool_catalog"]
    local_entity_map = consts["entity_name_to_id"]
    local_account_trap = consts["account_trap_check"]
    rep.note(f"universe: {universe}")

    if consts.get("id_pattern_set") == "starpm":
        grounding_specs = STARPM_GROUNDING
        value_tokens_re = STARPM_VALUE_TOKENS
        suspicious_id_pats = (STARPM_AIRTABLE_REC, STARPM_LINEAR_ISSUE, STARPM_HUBSPOT_OBJ)
    elif consts.get("id_pattern_set") == "harmonygames":
        # Ledger keys match HARMONYGAMES_ID_PATTERNS in build_fact_ledger.py - one source.
        grounding_specs = HG_GROUNDING
        value_tokens_re = RUBRIC_VALUE_TOKENS
        suspicious_id_pats = (HG_LINEAR_ISSUE, HG_TRELLO_CARD, HG_GDRIVE_FILE)
    else:
        grounding_specs = [
            (JE_ID, "JE", "je"),
            (EXC_ID, "exception", "exception"),
            (DOC_ID, "doc", "doc"),
            (VENDOR_ID, "vendor", "vendor"),
            (APINV_ID, "apinv", "apinv"),
            (RECON_ID, "recon", "recon"),
        ]
        value_tokens_re = RUBRIC_VALUE_TOKENS
        suspicious_id_pats = (JE_ID, EXC_ID, RECON_ID, DOC_ID, VENDOR_ID, APINV_ID)

    ledger = load_fact_ledger(task_dir)
    universe_blob = load_universe_blob(task_dir) if not ledger else ""
    tool_names = load_tool_names(local_tool_catalog)

    feasible_surface = {}
    fs_file = task_dir / "_aux" / "Feasible_Surface.json"
    if fs_file.is_file():
        try:
            feasible_surface = json.loads(fs_file.read_text(encoding="utf-8")).get("tables", {})
            rep.note(f"Feasible_Surface loaded: {len(feasible_surface)} tables with enum maps")
        except (json.JSONDecodeError, OSError):
            pass
    if ledger:
        rep.note(f"using Fact_Ledger.json for groundedness ({ledger.get('meta', {}).get('atom_counts', {}).get('amounts', 0)} amounts, {ledger.get('meta', {}).get('atom_counts', {}).get('emails', 0)} emails indexed)")
    else:
        rep.note("Fact_Ledger.json not present — falling back to raw blob substring match")

    outcome_n = 0
    process_n = 0
    sub_category_counts: dict = {}
    rubric_severity = {i: {"major": 0, "moderate": 0, "minor": 0} for i in range(len(rubrics))}

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
        if ann:
            rep.warn(f"{loc}: nested schema is deprecated — convert to flat {{title, category, justification, evidence}}. New tasks must ship flat.")
        evidence = ann.get("evidence") or r.get("evidence")
        justification = ann.get("justification") or r.get("justification")
        cat_raw = ann.get("rubric_category") or r.get("category") or r.get("rubric_category") or ""
        if not evidence:
            rep.fail(f"{loc}: evidence missing or empty")
        if not justification:
            rep.fail(f"{loc}: justification missing or empty")
        if not cat_raw:
            rep.fail(f"{loc}: category missing or empty")
        cat_stored = str(cat_raw).strip()
        _enum = _fw_profile.get("rubric_category_enum", {"outcome", "process"})
        if cat_stored.lower() not in {e.lower() for e in _enum}:
            rep.fail(f"{loc}: rubric_category `{cat_stored}` not in {sorted(_enum)}")
        # Canonicalize the STORED value to its parent bucket before counting.
        # HarmonyGames stores a 4-value enum (`Outcome 1.1` / `1.2` / `2.1` / `Process`),
        # which is AGENTS.md rule 24's sub_category already native to the schema. Counting
        # the raw string put every sub-category in neither bucket, so a spec-conformant HG
        # set reported outcome=0 and hard-failed "no outcome rubrics". Canonicalizing keeps
        # the sub-category available for reporting while making the counts correct.
        cat = _canonical_category(cat_stored)
        sub_cat = cat_stored if cat_stored.lower() != cat else None
        if sub_cat:
            sub_category_counts[cat_stored] = sub_category_counts.get(cat_stored, 0) + 1
        if cat == "outcome":
            outcome_n += 1
        elif cat == "process":
            process_n += 1

        if not re.match(r"^(?:The\s+Agent|Agent)\b", title):
            rep.fail(f"{loc}: title must start with `The Agent` or `Agent` — got `{title[:60]}...`")

        if "\n" in title or "\r" in title:
            rep.fail(f"{loc}: title contains newline — V3 reference convention requires single-line titles (even if long).")
            rubric_severity[i]["minor"] += 1
        if F3_MD_BOLD_ITALIC.search(title):
            rep.fail(f"{loc}: title contains markdown bold/italic — plain prose only per V3 reference convention.")
            rubric_severity[i]["minor"] += 1
        if F1_BULLETS.search(title):
            rep.fail(f"{loc}: title contains bullet character — plain prose only.")
            rubric_severity[i]["minor"] += 1

        ev_text = evidence if isinstance(evidence, str) else ""
        if ev_text and not F11_OE_REF.search(ev_text) and not F11_TRAJECTORY_ANCHOR.search(ev_text):
            rep.warn(f"{loc}: evidence neither references an OE step (Per OE<n> / See OE<n> / OE<n>) nor uses trajectory-anchoring phrasing (Look for / Check the / Verify that / Inspect / Confirm / payload / final response). Add an explicit anchoring so the judge knows where to grade from.")
        if isinstance(evidence, str) and F3_MD_BOLD_ITALIC.search(evidence):
            rep.warn(f"{loc}: evidence contains markdown bold/italic — plain prose only.")
        if isinstance(justification, str) and F3_MD_BOLD_ITALIC.search(justification):
            rep.warn(f"{loc}: justification contains markdown bold/italic — plain prose only.")

        for m in TOOL_NAME_HINT.finditer(title):
            if tool_names and m.group(0) in tool_names:
                rep.fail(f"{loc}: tool name `{m.group(0)}` appears in title (allowed only in evidence/justification)")
            else:
                rep.warn(f"{loc}: suspicious tool-shaped token `{m.group(0)}` in title")

        if re.search(r"\bat\s+least\s+\d+\b", title, re.IGNORECASE):
            prompt_mandates_min = bool(re.search(r"\bat\s+least\s+\d+\b", prompt_text, re.IGNORECASE))
            if not prompt_mandates_min:
                rep.fail(f"{loc}: title uses `at least N` but the prompt does not mandate a minimum — split into atomic rubrics")

        for m in RUBRIC_SUBJECTIVE.finditer(title):
            rep.fail(f"{loc}: subjective term `{m.group(0)}` in title (QC spec bans these)")
        for m in RUBRIC_SOFT_VOICE.finditer(title):
            rep.warn(f"{loc}: non-agent voice or eval-internal phrase `{m.group(0)}` in title (use agent-centric phrasing)")
        for m in RUBRIC_NEGATION.finditer(title):
            rep.warn(f"{loc}: awkward negation `{m.group(0)}` in title (state the positive expectation)")

        # Negative Criteria - QC dimension 23, [Fail - Criteria Framing], Fail=2/Pass=5
        # with Non-Fail "N/A", i.e. BINARY (Docs_harmonygames/8_QC_Spec_Doc2.md:293-302).
        # Gated on the framework profile because the dimension exists ONLY in the
        # HarmonyGames spec; the shared logic lives in check_rubric_antipatterns so the
        # standalone gate and this one cannot drift. The spec mandates pre-scan THEN
        # adjudicate, so a blanket ban on the seven indicator words is itself a violation:
        # the spec ships a MUST-PASS example that contains one.
        if _fw_profile.get("rubric_negative_criteria_gate"):
            _neg = negative_framing_hit(title)
            if _neg:
                _mandate = prompt_mandate_for(title, prompt_raw)
                if _mandate:
                    rep.note(f"{loc}: negative framing `{_neg[0]}` in title is prompt-mandated, so the explicit non-action exemption applies. Mandating sentence: \"{_mandate[:140]}\"")
                else:
                    rep.fail(f"{loc}: [Fail - Criteria Framing] title negates the Agent's own action via `{_neg[0]}` and no prompt sentence mandates that prohibition. Rewrite affirmatively. A negative word is fine when it only names the reported content, as in `reports that PR #438 had no human-submitted review`.")

        # Vague Exemplar Language - one Moderate per affected rubric, scanned across EVERY
        # field (7_QC_Spec_Doc1.json Rubric/Sub-Dimensions[6]: "Scan every field ... count
        # one Moderate issue per affected rubric"). V3_VAGUE_CONNECTOR below already bans
        # these in the TITLE for every universe, so a title hit is skipped here rather than
        # charged twice against the same rubric.
        if _fw_profile.get("rubric_vague_exemplar_scope") == "all_fields":
            _vf = vague_exemplar_fields({
                "title": title,
                "evidence": evidence if isinstance(evidence, str) else "",
                "justification": justification if isinstance(justification, str) else "",
            })
            if _vf and not V3_VAGUE_CONNECTOR.search(title):
                _vfield, _vphrase = _vf[0]
                _vextra = f" (+{len(_vf) - 1} more field(s))" if len(_vf) > 1 else ""
                rep.warn(f"{loc}: Vague Exemplar Language — `{_vphrase}` in {_vfield}{_vextra}. Illustrative language leaves the accepted set undefined; state the accepted set or an objective semantic rule. One Moderate per affected rubric.")
                rubric_severity[i]["moderate"] += 1

        if re.search(r"approximately\s+(?:\d{4}-\d{2}-\d{2}|[A-F0-9]{12}|exc_|VEN-)", title):
            rep.fail(f"{loc}: `approximately` used in front of an ID/date — restrict to calculated/rounded values")
            rubric_severity[i]["minor"] += 1

        if re.search(r"\([^)]*or\s+similar[^)]*\)\s*[^.]{0,30}@\w", title):
            rep.warn(f"{loc}: `(or similar)` near an email — emails must be exact-match")
            rubric_severity[i]["minor"] += 1

        for m in X2_POSITIONAL_REFS.finditer(title):
            title_stripped = title[:m.start()] + " " + title[m.end():]
            title_stripped = re.sub(r"\bThe\s+Agent\b", "", title_stripped)
            named_candidates = re.findall(r"\b[A-Z][a-z]+\s+[A-Z][a-z]+\b", title_stripped)
            framing_tokens = {"Managing Partner", "Engagement Partner", "Account Owner", "Account Manager", "Records Vault", "Oracle GL", "Slack Channel", "Records Manager", "Audit Lead"}
            real_names = [n for n in named_candidates if n not in framing_tokens]
            if not EMAIL_RE.search(title) and not real_names:
                rep.fail(f"{loc}: self-containment — title uses positional reference `{m.group(0)}` without an explicit named value (email address or full name). Judge cannot resolve 'the X' without external lookup. Embed the actual recipient/approver/partner.")
                rubric_severity[i]["major"] += 1
                break

        for m in X7_OVERLY_BROAD_LIST.finditer(title):
            rep.warn(f"{loc}: overly-broad list `{m.group(0)[:80]}...` — criterion accepts multiple values; verify each named option is universe-valid and the list does not include invalid options that would pass the rubric.")
            rubric_severity[i]["moderate"] += 1

        if X8_FREETEXT_QUOTED.search(title):
            if "(or similar)" not in title.lower() and "(or equivalent)" not in title.lower():
                rep.fail(f"{loc}: overly-specific freetext — title pins exact wording in a freetext field (subject/body/title/description/summary) without `(or similar)` marker. Allow paraphrase: append `(or similar)` to the quoted phrase.")
                rubric_severity[i]["minor"] += 1

        for m in V3_VAGUE_CONNECTOR.finditer(title):
            rep.fail(f"{loc}: forbidden vague connector `{m.group(0)}` in title — QC spec explicitly forbids `such as` / `for example` / `e.g.` / `like` when defining what counts as correct. Use one of the canonical patterns instead: `must be one of: A, B, or C` (closed set) / `including but not limited to: A, B` (open set) / `at least one of: A, B, or C` (any one).")
            rubric_severity[i]["moderate"] += 1
            break

        if V7_MULTI_VALUE_AMBIGUOUS.search(title) and not V7_MULTI_VALUE_CANONICAL.search(title):
            if not re.search(r"\([^)]*(?:or\s+similar|or\s+equivalent)[^)]*\)", title, re.IGNORECASE):
                rep.warn(f"{loc}: multi-value phrasing — title lists multiple values via `A, B, or C` without a canonical pattern. QC spec requires `must be one of: ...` (closed set) / `including but not limited to: ...` (open set) / `at least one of: ...` (any one). Use the explicit pattern to clarify acceptance semantics.")
                rubric_severity[i]["minor"] += 1

        if feasible_surface:
            enum_value_pattern = re.compile(r"\b(status|state|type|category|kind|classification|milestone|phase)\s*[=:]\s*[\"']?([\w_-]+)[\"']?", re.IGNORECASE)
            for em in enum_value_pattern.finditer(title):
                col_hint = em.group(1).lower()
                val_claimed = em.group(2)
                if val_claimed.isdigit() or len(val_claimed) < 3:
                    continue
                value_found = False
                for table_name, table_enums in feasible_surface.items():
                    for col, valid_vals in table_enums.items():
                        if col_hint in col.lower() and val_claimed in valid_vals:
                            value_found = True
                            break
                    if value_found:
                        break
                if not value_found:
                    rep.warn(f"{loc}: feasible-surface mismatch — `{col_hint}={val_claimed}` not found in any universe table's enum set. Verify the value exists for the entity, or correct the rubric.")

        if prompt_text:
            for a_word, b_word in X9_SYNONYM_PAIRS:
                title_lc = title.lower()
                if a_word in title_lc and a_word not in prompt_text and b_word in prompt_text:
                    rep.warn(f"{loc}: wording mismatch — title uses `{a_word}` but prompt uses `{b_word}`. Align terminology to reduce judge ambiguity.")
                    break
                if b_word in title_lc and b_word not in prompt_text and a_word in prompt_text:
                    rep.warn(f"{loc}: wording mismatch — title uses `{b_word}` but prompt uses `{a_word}`. Align terminology to reduce judge ambiguity.")
                    break

        if local_retention_codes:
            for rm in RETENTION_CODE_REF.finditer(title):
                code = (rm.group(1) or "").upper()
                if code and code not in local_retention_codes:
                    rep.fail(f"{loc}: retention code `{code}` in title not in valid set {{{', '.join(sorted(local_retention_codes))}}}.")
        if local_slack_channels:
            for rm in SLACK_CHANNEL_REF.finditer(title):
                chan = rm.group(1)
                if chan and chan not in local_slack_channels:
                    rep.fail(f"{loc}: Slack channel `{chan}` in title not in valid range for {universe}: {sorted(local_slack_channels)}.")
        if local_classifications:
            for rm in CLASSIFICATION_REF.finditer(title):
                cls = (rm.group(1) or "").lower()
                if cls and cls not in local_classifications:
                    rep.fail(f"{loc}: classification `{cls}` in title not in {{{', '.join(sorted(local_classifications))}}}.")
        if local_bl_exception_types:
            for rm in BL_EXCEPTION_TYPE_REF.finditer(title):
                ex_type = (rm.group(1) or "").lower()
                if ex_type and ex_type not in local_bl_exception_types:
                    rep.warn(f"{loc}: BlackLine exception type `{ex_type}` in title not in known set.")

        if local_slack_channels:
            chan_ids_in_title = SLACK_CHANNEL_REF.findall(title)
            if chan_ids_in_title and not re.search(r"#[a-z0-9-]+", title):
                for chan_id in chan_ids_in_title:
                    if chan_id in local_slack_channels:
                        rep.warn(f"{loc}: pins Slack channel_id `{chan_id}` without channel name (#name) — agent passing the name would wrongly fail this rubric. Accept either form.")

        if cat == "process":
            wm = WRITE_VERB_IN_TITLE.match(title)
            if wm:
                rep.fail(f"{loc}: title starts with write-action verb `{wm.group(1)}` but category is `process`. Write actions belong in Outcome 1.1 — re-classify as `outcome`.")
                rubric_severity[i]["moderate"] += 1

        am = AND_BUNDLING.search(title)
        if am:
            rep.fail(f"{loc}: title bundles two independent actions via AND — split into atomic rubrics. (`{am.group(0)[:80]}...`)")
            rubric_severity[i]["major"] += 1

        if prompt_text and OPEN_GOAL_VERBS.search(prompt_text):
            if CHANNEL_LOCK_VERBS_EMAIL.match(title):
                rep.fail(f"{loc}: rubric locks in email channel but prompt uses open-ended goal verbs (notify/reach out/let know/loop in/update). Rubric would fail an agent posting in Slack or DM instead. Re-phrase as 'The Agent notifies <recipient> ...' to allow alternative channels.")
                rubric_severity[i]["major"] += 1
            if CHANNEL_LOCK_VERBS_SLACK.match(title):
                rep.fail(f"{loc}: rubric locks in Slack channel but prompt uses open-ended goal verbs. Re-phrase to allow alternative channels.")
                rubric_severity[i]["major"] += 1

        if isinstance(evidence, str) and evidence and isinstance(title, str):
            title_strict = set(value_tokens_re.findall(title))
            ev_strict = set(value_tokens_re.findall(evidence))
            extras = ev_strict - title_strict
            if extras:
                rep.warn(f"{loc}: evidence contains dates/IDs/amounts NOT in criterion: {sorted(extras)[:3]}. Evidence must not be stricter than criterion (judge grades criterion text first).")

        if isinstance(title, str) and prompt_text:
            suspicious_ids_in_title = set()
            for pat in suspicious_id_pats:
                suspicious_ids_in_title.update(m.group(0) for m in pat.finditer(title))
            oe_text_lc = ""
            oe_path = task_dir / "6_Oracle_Events.txt"
            if oe_path.is_file():
                oe_text_lc = oe_path.read_text(encoding="utf-8").lower()
            for atom in suspicious_ids_in_title:
                atom_lc = atom.lower()
                if atom_lc not in prompt_text and atom_lc not in oe_text_lc:
                    rep.warn(f"{loc}: ID `{atom}` in title is universe-valid but NOT in prompt OR OE — verify it's a reasonably-implied derivative (e.g., target of investigation surfaced by an OE step), not a beyond-prompt fabricated check.")

        if re.search(r"\b(?:sends?\s+an?\s+email|\bemails\b)\b", title, re.IGNORECASE):
            if not EMAIL_RE.search(title):
                rep.fail(f"{loc}: email rubric without recipient email address — Service Metadata Completeness requires the exact email address in the criterion.")
        if re.search(r"\b(?:posts?\s+(?:in|to)\b.*\bslack|sends?\s+a?\s+slack\s+message)\b", title, re.IGNORECASE):
            if not (re.search(r"#[a-z0-9-]+", title) or SLACK_CHANNEL_REF.search(title)):
                rep.fail(f"{loc}: Slack rubric without channel name (#channel-name) or channel_id — Service Metadata Completeness requires the channel in the criterion.")

        if ledger:
            for m in MONEY_RE.finditer(title):
                if not amount_in_ledger(m.group(0), ledger):
                    rep.warn(f"{loc}: dollar amount `{m.group(0)}` not in Fact_Ledger amounts (verify against universe by hand)")
            email_set = set(ledger.get("emails", []))
            for m in EMAIL_RE.finditer(title):
                if m.group(0).lower() not in email_set:
                    rep.fail(f"{loc}: email `{m.group(0)}` not in Fact_Ledger")
            id_buckets = ledger.get("ids", {})
            for pat, label, bucket in grounding_specs:
                bucket_set = set(id_buckets.get(bucket, []))
                for m in pat.finditer(title):
                    if m.group(0) not in bucket_set:
                        rep.fail(f"{loc}: {label} id `{m.group(0)}` not in Fact_Ledger.ids.{bucket}")

            accounts_by_entity = ledger.get("accounts_by_entity", {}) if local_account_trap else {}
            if accounts_by_entity:
                entity_name_to_id = local_entity_map
                title_lower = title.lower()
                entities_in_title = []
                for name, eid in entity_name_to_id.items():
                    if re.search(rf"\b{re.escape(name)}\b", title_lower):
                        entities_in_title.append(eid)
                if entities_in_title:
                    for acct_m in re.finditer(r"\b(\d{6})\b", title):
                        acct = acct_m.group(1)
                        for eid in entities_in_title:
                            entity_accounts = accounts_by_entity.get(eid, {})
                            if acct not in entity_accounts:
                                rep.warn(f"{loc}: account {acct} mentioned near entity `{eid}` but not present in Fact_Ledger.accounts_by_entity for {eid}. Account-number entity-trap: 105000 differs per entity (Cash-Trust on Brookfield, IOLTA on Northstar, Short-term Investments on Acme). Verify per-entity assignment.")
        elif universe_blob:
            for m in MONEY_RE.finditer(title):
                amt = m.group(0).replace(" ", "")
                amt_no_dollar = amt.lstrip("$")
                amt_no_commas = amt_no_dollar.replace(",", "")
                amt_int = amt_no_commas.split(".")[0]
                variants = {amt, amt_no_dollar, amt_no_commas, amt_int}
                if "." not in amt_no_commas and amt_int.isdigit():
                    variants.add(amt_int + ".0")
                if not any(v in universe_blob for v in variants):
                    rep.warn(f"{loc}: dollar amount `{amt}` not found verbatim in Universe_Split")
            for m in EMAIL_RE.finditer(title):
                if m.group(0).lower() not in universe_blob.lower():
                    rep.fail(f"{loc}: email `{m.group(0)}` not found in Universe_Split")
            for pat, label, _bucket in grounding_specs:
                for m in pat.finditer(title):
                    if m.group(0) not in universe_blob:
                        rep.fail(f"{loc}: {label} id `{m.group(0)}` not found in Universe_Split")

    if len(rubrics) >= 3:
        pronoun_skip_rub = {"The", "Agent", "If", "When", "And", "Or", "But", "Also", "Then", "Just", "A", "An", "It", "This", "That", "Sends", "Posts", "Creates", "Updates", "Forwards", "Submits", "Approves", "Denies", "Reverses", "Voids", "Adds", "Writes", "Files", "Identifies", "Reports", "Lists", "States", "Mentions", "Notifies", "Schedules", "Includes", "Recommends", "Concludes", "Flags", "Confirms", "Verifies"}
        rub_ents = []
        for ri, rr in enumerate(rubrics):
            if not isinstance(rr, dict):
                rub_ents.append((ri, "", set()))
                continue
            rt = rr.get("title", "") if isinstance(rr.get("title", ""), str) else ""
            ents = set(NAMED_ENTITY_RE_PROMPT.findall(rt))
            ents -= pronoun_skip_rub
            rub_ents.append((ri, rt, ents))
        for ri, rt, ents in rub_ents:
            if len(ents) < 2:
                continue
            other_ents = set()
            for rj, _, e2 in rub_ents:
                if rj != ri:
                    other_ents |= e2
            if not (ents & other_ents):
                rep.warn(f"rubric[{ri}]: bolt-on candidate — title `{rt[:80]}...` shares no named entities with any other rubric. Apply remove-rubric test: if the rubric set still tests the prompt's intent without this one, it's an isolated check (Coherence violation).")

    rubric_token_sets = []
    for ri, rr in enumerate(rubrics):
        if not isinstance(rr, dict):
            continue
        rt = rr.get("title", "")
        if not isinstance(rt, str):
            continue
        rtokens = set(re.findall(r"\b\w+\b", rt.lower()))
        rtokens -= {"the", "agent", "a", "an", "to", "in", "on", "at", "of", "for", "with", "and", "or", "is", "are", "be", "has", "have", "that", "this"}
        rubric_token_sets.append((ri, rtokens))
    for i_outer, (idx_a, set_a) in enumerate(rubric_token_sets):
        for idx_b, set_b in rubric_token_sets[i_outer + 1:]:
            if not set_a or not set_b:
                continue
            jacc = len(set_a & set_b) / len(set_a | set_b)
            if jacc >= 0.70:
                rep.warn(f"rubric[{idx_a}] and rubric[{idx_b}]: criterion text Jaccard similarity {jacc * 100:.0f}% — likely overlap/redundancy. Removing one may not change scoring outcomes.")
                rubric_severity[idx_a]["moderate"] += 1
                rubric_severity[idx_b]["moderate"] += 1

    if prompt_text and rubrics:
        prompt_write_verbs_used = {m.group(0).lower().rstrip("eds").rstrip("ing").rstrip("e") for m in WRITE_VERB_PROMPT_RE.finditer(prompt_text)}
        prompt_write_verbs_used = {v for v in prompt_write_verbs_used if len(v) >= 3}
        rubric_outcome_titles = " ".join(
            rr.get("title", "") for rr in rubrics
            if isinstance(rr, dict)
            and isinstance(rr.get("title", ""), str)
            and (rr.get("category") or rr.get("rubric_category") or (rr.get("annotations") or {}).get("rubric_category") or "").lower() == "outcome"
        ).lower()
        for verb in sorted(prompt_write_verbs_used):
            if verb in {"do", "be", "is", "are", "get", "go", "see"}:
                continue
            if verb not in rubric_outcome_titles:
                rep.warn(f"missing-Outcome candidate: prompt uses write-verb `{verb}` but no Outcome rubric title contains that verb. Verify an Outcome rubric checks the corresponding write action.")

    hardness_plan_path = task_dir / "_aux" / "Hardness_Plan.md"
    hardness_text = ""
    if hardness_plan_path.is_file():
        hardness_text = hardness_plan_path.read_text(encoding="utf-8").lower()
    if hardness_text and ledger:
        for i, r in enumerate(rubrics):
            if not isinstance(r, dict):
                continue
            t = r.get("title", "")
            if not isinstance(t, str):
                continue
            for pat in (JE_ID, EXC_ID, RECON_ID, DOC_ID, VENDOR_ID, APINV_ID):
                for m in pat.finditer(t):
                    val_lc = m.group(0).lower()
                    if val_lc not in hardness_text and val_lc not in (prompt_text or "") and val_lc not in (load_universe_blob(task_dir).lower() if not ledger else ""):
                        pass
            for am in MONEY_RE.finditer(t):
                amt = am.group(0)
                if amt.lstrip("$").lower() not in hardness_text and prompt_text and amt.lstrip("$") not in prompt_text:
                    rep.warn(f"rubric[{i}]: amount `{amt}` not in Hardness_Plan ground-truth atoms AND not in prompt. Verify it's not a fabricated value that contradicts the universe-derived correct answer.")

    oe_path_x2 = task_dir / "6_Oracle_Events.txt"
    if oe_path_x2.is_file() and rubrics:
        oe_text_x2 = oe_path_x2.read_text(encoding="utf-8")

        def _x2_norm_amount(raw: str) -> str:
            a = raw.replace(" ", "").lstrip("$").replace(",", "")
            try:
                return str(Decimal(a).quantize(Decimal("0.01")))
            except (InvalidOperation, ValueError):
                return a.lower()

        def _x2_typed_atoms(text: str) -> set:
            atoms = set()
            for m in MONEY_RE.finditer(text):
                atoms.add(("amount", _x2_norm_amount(m.group(0))))
            for m in EMAIL_RE.finditer(text):
                atoms.add(("email", m.group(0).lower()))
            for m in JE_ID.finditer(text):
                atoms.add(("je", m.group(0)))
            for m in EXC_ID.finditer(text):
                atoms.add(("exc", m.group(0)))
            for m in RECON_ID.finditer(text):
                atoms.add(("recon", m.group(0)))
            for m in VENDOR_ID.finditer(text):
                atoms.add(("vendor", m.group(0)))
            for m in APINV_ID.finditer(text):
                atoms.add(("apinv", m.group(0)))
            for m in DOC_ID.finditer(text):
                atoms.add(("doc", m.group(0)))
            if universe == "starpm":
                for m in STARPM_AIRTABLE_REC.finditer(text):
                    atoms.add(("airtable_record", m.group(0)))
                for m in STARPM_LINEAR_ISSUE.finditer(text):
                    atoms.add(("linear_issue", m.group(0)))
                for m in STARPM_HUBSPOT_OBJ.finditer(text):
                    atoms.add(("hubspot_object", m.group(0)))
            for m in DATE_YMD.finditer(text):
                atoms.add(("date", m.group(0)))
            for m in ACCOUNT_NUM.finditer(text):
                atoms.add(("account", m.group(0)))
            for code in (local_retention_codes or set()):
                if re.search(rf"\b{re.escape(code)}\b", text):
                    atoms.add(("retention", code))
            for cls in (local_classifications or set()):
                if re.search(rf"\b{re.escape(cls)}\b", text, re.IGNORECASE):
                    atoms.add(("classification", cls.lower()))
            for chan in (local_slack_channels or set()):
                if re.search(rf"\b{re.escape(chan)}\b", text):
                    atoms.add(("slack_chan", chan))
            return atoms

        oe_atoms_by_type: dict = {}
        for atype, aval in _x2_typed_atoms(oe_text_x2):
            oe_atoms_by_type.setdefault(atype, set()).add(aval)

        for ri, rr in enumerate(rubrics):
            if not isinstance(rr, dict):
                continue
            rt = rr.get("title", "")
            if not isinstance(rt, str) or not rt.strip():
                continue
            rt_lc = rt.lower()
            if "(or similar)" in rt_lc or "(or equivalent)" in rt_lc:
                continue
            seen_x2_keys = set()
            for atype, aval in _x2_typed_atoms(rt):
                key = (atype, aval)
                if key in seen_x2_keys:
                    continue
                seen_x2_keys.add(key)
                oe_set = oe_atoms_by_type.get(atype, set())
                if aval in oe_set:
                    continue
                if oe_set and aval.lower() in {v.lower() for v in oe_set}:
                    continue
                if not oe_set:
                    rep.warn(f"rubric[{ri}] (X2 rubric-OE consistency): typed value `{aval}` ({atype}) in title has no OE step referencing any `{atype}` value. CONSISTENCY_GAP candidate. WARN-only observation period.")
                else:
                    sample = sorted(oe_set)[:3]
                    rep.warn(f"rubric[{ri}] (X2 rubric-OE consistency): typed value `{aval}` ({atype}) in title differs from OE values of same type: {sample}. CONSISTENCY_GAP candidate. WARN-only observation period.")

    rep.note(f"counts: outcome={outcome_n}, process={process_n}")
    if sub_category_counts:
        rep.note("sub-categories: " + ", ".join(f"{k}={v}" for k, v in sorted(sub_category_counts.items())))
    if outcome_n == 0:
        rep.fail("no outcome rubrics (every task needs at least 1)")
    # Balance rule is per-framework. Brookfield/KeyStone/MoveOps/StarPM require an
    # Outcome majority (Docs/7_QC_Spec_Doc1.json:151, dated 05/22). HarmonyGames'
    # own spec replaces that with a flat binary cap of Process <= 40%, and states
    # zero Process is valid. Each universe follows its own spec.
    _rule = _fw_profile.get("rubric_balance_rule", "outcome_gt_process")
    _total = outcome_n + process_n
    if _rule == "process_max_40pct":
        if outcome_n == 0:
            rep.fail("zero outcome rubrics — Outcome is mandatory")
        if _total and (process_n / _total) > 0.40:
            rep.fail(f"process is {process_n}/{_total} ({process_n/_total:.0%}) of the set — cap is 40%")
    else:
        if process_n > outcome_n:
            rep.fail(f"process count ({process_n}) > outcome count ({outcome_n}) — process must be the minority")
        if process_n > 0 and (process_n / max(1, _total)) > 0.5:
            rep.fail(f">50% of rubrics are process — outcome must outnumber process")

    # v21.3 producing-phase backstops (F7 ambiguous target / F8 non-atomic enum /
    # F9 unreconciled future calendar event): catch at S3, not only pre-upload.
    try:
        from Validators import v4_gates as _v4bs
    except ImportError:
        import v4_gates as _v4bs
    _oe_p = task_dir / "6_Oracle_Events.txt"
    _oe_txt = _oe_p.read_text(encoding="utf-8") if _oe_p.is_file() else ""
    _v4bs._false_fail_backstops(task_dir, rep, universe, rubrics, prompt_text, _oe_txt)

    total_rubrics = len(rubrics)
    if total_rubrics > 0:
        rubrics_with_major = sum(1 for i in range(total_rubrics) if rubric_severity[i]["major"] > 0)
        rubrics_with_moderate_or_major = sum(1 for i in range(total_rubrics) if rubric_severity[i]["major"] > 0 or rubric_severity[i]["moderate"] > 0)
        rubrics_with_any = sum(1 for i in range(total_rubrics) if rubric_severity[i]["major"] > 0 or rubric_severity[i]["moderate"] > 0 or rubric_severity[i]["minor"] > 0)
        pct_major = 100 * rubrics_with_major / total_rubrics
        pct_moderate = 100 * rubrics_with_moderate_or_major / total_rubrics
        pct_minor = 100 * rubrics_with_any / total_rubrics
        rep.note(f"Overall Rubric Quality: {rubrics_with_major}/{total_rubrics} ({pct_major:.0f}%) with Major, {rubrics_with_moderate_or_major}/{total_rubrics} ({pct_moderate:.0f}%) with Moderate+ , {rubrics_with_any}/{total_rubrics} ({pct_minor:.0f}%) with any issue")
        if pct_major > 10:
            rep.fail(f"Overall Rubric Quality FAIL — {pct_major:.0f}% of rubrics have Major issues (QC spec band: >10% = FAIL). Cap is 10%.")
        if pct_moderate > 15:
            rep.fail(f"Overall Rubric Quality FAIL — {pct_moderate:.0f}% of rubrics have Moderate-or-Major issues (QC spec band: >15% = FAIL). Cap is 15%.")
        if pct_minor > 20:
            rep.fail(f"Overall Rubric Quality FAIL — {pct_minor:.0f}% of rubrics have any-severity issues (QC spec band: >20% = FAIL). Cap is 20%.")
        if rubrics_with_major >= 3:
            rep.fail(f"Overall Rubric Quality FAIL — {rubrics_with_major} rubrics carry Major issues (absolute-count cap is 2). Tighten or split.")


def validate_persona_acl(task_dir: Path, rep: Report) -> None:
    """Persona ACL as a PROMPT FEASIBILITY gate (AGENTS.md rule 32).

    Docs_harmonygames/14_Persona_ACL.md makes a read the assigned persona cannot
    perform a TASK DEFECT, not a model miss - `[Fail - Prompt Feasibility with Tools]`.
    Universe Explorer god-mode shows ALL records, so authoring against it silently
    produces infeasible prompts.

    Gated on the registry `acl_gate` flag, so every non-HG universe SKIPs and the
    frozen report hashes (38 snapshot tasks, all brookfield/keystone/moveops) cannot move.

    Reads only. :17 "Persona ACL does not govern writes", and :134 forbids making an
    ACL-based write denial necessary to a prompt, Oracle Event or rubric - so the
    write check here is CATALOG feasibility (Gmail has no send tool), never ACL denial.
    """
    universe = detect_universe(task_dir)
    if not get_framework_profile(universe).get("acl_gate", False):
        return
    consts = get_universe_constants(universe)
    roster = load_roster(consts)
    if not roster:
        rep.warn(f"persona ACL: roster missing or empty ({consts.get('persona_acl_roster')}); "
                 f"ACL-1 identity resolution cannot be verified")
        return
    scoped = consts.get("acl_scoped_services", [])
    rep.note(f"persona ACL active: {len(scoped)} scoped service(s) ({', '.join(scoped)}); "
             f"validate every required read from the assigned persona's view, not Universe Explorer god-mode")
    for issue in check_persona_resolves(task_dir, roster, load_brief_names(consts)):
        (rep.fail if issue.strip().startswith("[FAIL]") else rep.warn)(f"persona ACL: {issue.strip()}")
    for issue in check_no_impossible_writes(task_dir):
        (rep.fail if issue.strip().startswith("[FAIL]") else rep.warn)(f"persona ACL: {issue.strip()}")

def validate_retired_servers(task_dir: Path, rep: Report, phase: str) -> None:
    """Retired Server Reference, the V5 A1 HARD GATE (Evals_harmonygames/1_Prompt_Eval.md:383).

    Snowflake and Confluence ship in no catalog after the 2026-08 V5 drop, so a prompt that
    leans on either is unsolvable and it is a Feasibility FAIL - a TASK defect, not a model
    miss, exactly like the persona-ACL gate above.

    Gated on the framework `retired_services` key, and returns having emitted NOTHING when it
    is empty. That silence is load-bearing: check_regression.py pins the hashes of 21
    validate.py reports on brookfield / keystone / moveops snapshot tasks, so a single extra
    NOTE line here would fail the zero-regression gate for four universes that retired no
    server. Same reason validate_persona_acl returns before touching `rep`.

    Logic is imported from check_retired_servers rather than restated, so the standalone
    checker and this gate cannot drift - the failure mode AGENTS.md rule 18 records, where a
    fix verified by a hand-run grep was silently reintroduced.
    """
    retired = get_framework_profile(detect_universe(task_dir)).get("retired_services") or []
    if not retired:
        return
    src = "5_Prompt.txt" if phase == "prompt" else "6_Oracle_Events.txt"
    p = task_dir / src
    if not p.is_file():
        return
    text = p.read_text(encoding="utf-8", errors="ignore")
    for tier, server, phrase, quote, verb in retired_server_findings(text, retired):
        why = ("names it outright" if tier == 1
               else f"stands in for it, in the action context `{verb}`")
        if tier in (1, 2):
            rep.fail(f"[Fail - Feasibility] retired server {server} is UNAVAILABLE and must "
                     f"not be used, and this {src} {why}, so the task is unsolvable. "
                     f"Offending phrase: \"{phrase}\" ...{quote}...")
        else:
            rep.note(f"retired-server stand-in `{phrase}` could imply {server}, but no action "
                     f"verb is nearby, so it reads as prose rather than a dependency. "
                     f"Surfaced for review, not blocking: ...{quote}...")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", required=True, choices=["prompt", "oe", "rubrics", "all", "injection", "submission_gate"])
    ap.add_argument("--task", required=True, help="path to Tasks/<TASK_DIR>")
    args = ap.parse_args()

    task_dir = Path(args.task).resolve()
    if not task_dir.is_dir():
        print(f"ERROR: {task_dir} is not a directory", file=sys.stderr)
        sys.exit(2)

    out_dir = task_dir / "_aux" / "Validator_Reports"
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        print(f"ERROR: {task_dir} is not writable (read-only template or vendored dir); "
              f"validate.py needs to write _aux/Validator_Reports. Copy the task into Tasks/ first.",
              file=sys.stderr)
        sys.exit(2)

    phases = [args.phase] if args.phase != "all" else ["prompt", "oe", "rubrics"]
    overall_fail = False
    for phase in phases:
        rep = Report(phase)
        if phase == "prompt":
            validate_prompt(task_dir, rep)
            validate_persona_acl(task_dir, rep)
            validate_retired_servers(task_dir, rep, "prompt")
        elif phase == "oe":
            validate_oe(task_dir, rep)
            validate_retired_servers(task_dir, rep, "oe")
        elif phase == "rubrics":
            validate_rubrics(task_dir, rep)
        elif phase in ("injection", "submission_gate"):
            # V4-only gates (Evals_starpm 0 and 5); SKIP cleanly on v3-family universes
            try:
                from Validators import v4_gates
            except ImportError:
                import v4_gates
            universe = detect_universe(task_dir)
            consts = get_universe_constants(universe)
            profile = get_framework_profile(universe)
            fn = v4_gates.validate_injection if phase == "injection" else v4_gates.validate_submission_gate
            ran = fn(task_dir, rep, universe, consts, profile)
            if not ran:
                out = out_dir / f"{phase}.md"
                out.write_text(rep.render(), encoding="utf-8")
                print(f"[SKIP] {phase}: not applicable to universe '{universe}' -> {_rel(out)}")
                continue
        out = out_dir / f"{phase}.md"
        out.write_text(rep.render(), encoding="utf-8")
        status = "FAIL" if rep.fails else "PASS"
        print(f"[{status}] {phase}: {len(rep.fails)} fails, {len(rep.warns)} warns, {len(rep.notes)} notes -> {_rel(out)}")
        if rep.fails:
            overall_fail = True

    sys.exit(1 if overall_fail else 0)


if __name__ == "__main__":
    main()
