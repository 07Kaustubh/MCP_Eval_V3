#!/usr/bin/env python3
"""
Usage:
    python Validators/check_retired_servers.py <task_dir>

Enforces the V5 "Retired Server Reference" HARD GATE deterministically, so a prompt that
leans on a server the universe no longer ships cannot reach a council in prose.

Authority (verbatim, Evals_harmonygames/1_Prompt_Eval.md:383):

    **A1. Retired Server Reference (HARD GATE)** - Snowflake and Confluence are UNAVAILABLE
    and must NOT be used, so any prompt that leans on either is unsolvable. Scan for both the
    explicit names and the unnamed stand-ins: `snowflake_*` / `confluence_*` tool names, a
    wiki, knowledge base, or space/page to write up; an analytics or data warehouse to query;
    SQL over warehouse tables; or `SCHEMA.TABLE`-style warehouse paths. Any hit = **FAIL
    Feasibility** - quote the offending phrase and name which retired server it implies.

Restated in the Phase 2.2 checklist at :39.

Why this exists
---------------
The 2026-08 V5 drop cut `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` from 276
tools to 239 and removed every `snowflake_*` and `confluence_*` entry, leaving 11 prefixes.
The registry still DESCRIBES 13 services, and the prose specs still describe a warehouse and
a wiki, so a prompt asking the agent to "check the wiki" reads as perfectly ordinary while
being strictly unsolvable.

AGENTS.md rule 18: a finding closed by a hand-run grep must become a standing gate. This is
that gate. Rule 31 supplies the two-stage precedent it copies - mechanical pre-scan, then
adjudication - and the reason a word-presence hard fail would itself be a defect: Feasibility
is BINARY (Fail=2 / Pass=5, no partial band), so ONE false positive fails the whole
sub-dimension for a legitimate task.

Tiers
-----
Tier 1  BLOCK, unconditional      An explicit `snowflake_*` / `confluence_*` tool name, or the
                                  capitalised product name. Nothing to adjudicate: the server
                                  is named.
Tier 2  BLOCK, verb-context only  The unnamed stand-ins, and ONLY when an action verb sits
                                  within a small token window. "wiki-style formatting" is
                                  prose about style; "check the wiki" is a dependency on a
                                  retired server. The distinction is the whole gate - see
                                  _NOUN_STANDIN and _ACTION_VERB.
Tier 3  SURFACE, never blocks     Everything the mechanical rules cannot adjudicate, printed
                                  for the human review the spec's "quote the offending
                                  phrase" step already requires.

Gated on the framework `retired_services` key. A universe declaring an empty list SKIPs
cleanly and prints why, so the four universes that retired nothing can never be flagged and
this file can never move their pinned `validate.py` report hashes.

Two interpretation choices, recorded rather than buried
-------------------------------------------------------
1. `SCHEMA.TABLE` is adjudicated as Tier 2, i.e. it needs verb context, because the spec
   sentence introducing it sits inside the stand-in list that the verb-window clause governs.
   A bare ALL-CAPS dotted path is a strong warehouse signal on its own, so this is the
   under-blocking direction; it is chosen because Feasibility is binary and a false positive
   costs a legitimate task its 5. A Tier-3 SURFACE line is emitted either way, so a
   verb-less warehouse path is never silently dropped.
2. The shape is deliberately narrow: BOTH halves ALL-CAPS and >= 3 characters. `Docs.README`,
   `Sheet.Total` and an ordinary sentence boundary ("...the warehouse. TABLE 3 shows...") must
   not match, and the >= 3 floor keeps initialisms like `A.B` out.

Exit 0 clean or SKIP, 1 when any Tier 1 or Tier 2 fires, 0 with a printed list when only
Tier 3 does.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
try:
    from Validators.universes import detect_universe, get_framework_profile
except ImportError:
    from universes import detect_universe, get_framework_profile

# Which retired server an unnamed stand-in implies. The spec requires the finding to "name
# which retired server it implies", so every pattern carries its attribution.
_CONFLUENCE, _SNOWFLAKE = "Confluence", "Snowflake"


# ---------------------------------------------------------------------------
# Tier 1. The server is named outright. No adjudication is possible or wanted.
# ---------------------------------------------------------------------------
# Tool names. Lowercase-only by design: the catalog is lowercase snake_case throughout, and
# matching case-insensitively here would double-report every capitalised proper-noun hit.
_RETIRED_TOOL = re.compile(r"\b(snowflake|confluence)_[a-z0-9_]+\b")

# The capitalised product name. Case-SENSITIVE on purpose. "snowflake" lowercase is an
# ordinary English noun (and a well-known ML term of art); `Snowflake` capitalised mid-prose
# is the product. Sentence-initial lowercase-noun use is a Tier-3 surface, not a block.
_RETIRED_NAME = re.compile(r"\b(Snowflake|Confluence)\b")


# ---------------------------------------------------------------------------
# Tier 2. Unnamed stand-ins, blocking ONLY inside a verb window.
# ---------------------------------------------------------------------------
# `wiki` carries a negative lookahead for a hyphen so the compound ADJECTIVE `wiki-style`
# (and `wiki-like`, `wiki-formatted`) cannot match. `\b` alone does not help: `-` is a
# non-word character, so `\bwiki\b` matches inside `wiki-style`. A compound adjective
# describes formatting and depends on no server, which is exactly the false positive that
# would fail a legitimate task on a binary sub-dimension.
_NOUN_STANDIN = (
    (re.compile(r"\bwikis?\b(?!-)", re.IGNORECASE), _CONFLUENCE),
    (re.compile(r"\bknowledge\s+base\b", re.IGNORECASE), _CONFLUENCE),
    # "space" and "page" are far too common alone; the spec names them as "a space/page to
    # write up", so the write-up sense is required rather than the bare noun.
    (re.compile(r"\b(?:confluence\s+)?(?:space|page)\b(?=[^.\n]{0,40}\b(?:write[- ]?up|written up|document(?:ation)?)\b)", re.IGNORECASE), _CONFLUENCE),
    (re.compile(r"\b(?:analytics|data)\s+warehouse\b", re.IGNORECASE), _SNOWFLAKE),
    (re.compile(r"\bwarehouse\s+(?:tables?|schema|query|queries)\b", re.IGNORECASE), _SNOWFLAKE),
    # SQL over warehouse tables. Requires the SQL verb AND a warehouse noun, so ordinary
    # mentions of a query or a table cannot reach it.
    (re.compile(r"\bselect\b[^.\n]{0,60}\bfrom\b[^.\n]{0,40}\b(?:warehouse|snowflake)\b", re.IGNORECASE), _SNOWFLAKE),
    # SCHEMA.TABLE. BOTH halves ALL-CAPS and >= 3 chars - see interpretation note 2 above.
    (re.compile(r"\b[A-Z][A-Z0-9_]{2,}\.[A-Z][A-Z0-9_]{2,}\b"), _SNOWFLAKE),
)

# The verbs that turn a noun into a DEPENDENCY. Taken from the brief's list (query, pull,
# look up, search, check, update, post, document, write up, file) plus the inflections that
# appear in real prompt prose, which is written in the imperative and the third person.
_ACTION_VERB = re.compile(
    r"\b(?:quer(?:y|ies|ied)|pull(?:s|ed|ing)?|look(?:s|ed|ing)?\s+up|looked\s+up"
    r"|search(?:es|ed|ing)?|check(?:s|ed|ing)?|updat(?:e|es|ed|ing)"
    r"|post(?:s|ed|ing)?|document(?:s|ed|ing)?|writ(?:e|es|ing)\s+up|wrote\s+up"
    r"|fil(?:e|es|ed|ing)|read(?:s|ing)?|review(?:s|ed|ing)?|find|found"
    r"|grab(?:s|bed|bing)?|fetch(?:es|ed|ing)?|consult(?:s|ed|ing)?)\b",
    re.IGNORECASE,
)

# Tokens either side of the noun that still count as "near". Six words each way spans a
# normal clause ("check the launch checklist on the wiki") without reaching across a
# sentence boundary into an unrelated verb.
_WINDOW_WORDS = 6


def _verb_in_window(text: str, start: int, end: int) -> str:
    """Return the action verb near text[start:end], or "" when none is in range.

    Window is measured in WORDS, not characters, and is clipped at sentence boundaries so a
    verb in the previous sentence cannot license a noun in this one.
    """
    before = re.split(r"(?<=[.!?\n])\s+", text[:start])[-1]
    after = re.split(r"(?<=[.!?\n])\s+", text[end:])[0]
    lead = " ".join(before.split()[-_WINDOW_WORDS:])
    trail = " ".join(after.split()[:_WINDOW_WORDS])
    m = _ACTION_VERB.search(lead) or _ACTION_VERB.search(trail)
    return m.group(0) if m else ""


def _quote(text: str, start: int, end: int, pad: int = 34) -> str:
    """The offending phrase with a little context, which the spec requires us to quote."""
    return " ".join(text[max(0, start - pad):end + pad].split())


def retired_server_findings(text: str, retired) -> list:
    """[(tier, server, phrase, quote, verb)] for one blob of prompt/OE text.

    `retired` is the framework `retired_services` list. An empty list yields no findings at
    all, which is what keeps every non-HarmonyGames universe untouched.

    Importable so `validate.py` shares this exact logic instead of restating it - the drift
    that AGENTS.md rule 18 exists to prevent, and the reason check_rubric_antipatterns.py is
    imported by validate.py rather than duplicated into it.
    """
    if not text or not retired:
        return []
    active = {s.lower() for s in retired}
    out = []

    for m in _RETIRED_TOOL.finditer(text):
        if m.group(1).lower() in active:
            out.append((1, m.group(1).capitalize(), m.group(0),
                        _quote(text, m.start(), m.end()), ""))
    for m in _RETIRED_NAME.finditer(text):
        if m.group(1).lower() in active:
            out.append((1, m.group(1), m.group(0),
                        _quote(text, m.start(), m.end()), ""))

    for pat, server in _NOUN_STANDIN:
        if server.lower() not in active:
            continue
        for m in pat.finditer(text):
            verb = _verb_in_window(text, m.start(), m.end())
            out.append(((2 if verb else 3), server, m.group(0),
                        _quote(text, m.start(), m.end()), verb))

    # A Tier-1 hit already names the server, so a stand-in for the SAME server adds nothing
    # but noise. Dropping it keeps the finding list about distinct defects.
    named = {s for t, s, *_ in out if t == 1}
    return [f for f in out if f[0] == 1 or f[1] not in named]


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore") if p.is_file() else ""


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    task = Path(sys.argv[1])
    if not task.is_absolute():
        task = ROOT / task

    universe = detect_universe(task)
    retired = get_framework_profile(universe).get("retired_services") or []
    print(f"=== Retired-server scan (V5 A1 HARD GATE): {task.name} ===")
    print(f"universe: {universe}")
    if not retired:
        print(f"[SKIP] universe '{universe}' retires no servers "
              f"(framework `retired_services` is empty); A1 does not apply.")
        return 0
    print(f"retired servers: {', '.join(sorted(retired))}\n")

    sources = [("5_Prompt.txt", _read(task / "5_Prompt.txt")),
               ("6_Oracle_Events.txt", _read(task / "6_Oracle_Events.txt"))]
    if not any(t for _, t in sources):
        print("[SKIP] neither 5_Prompt.txt nor 6_Oracle_Events.txt is present or non-empty.")
        return 0

    blocking, surfaced = [], []
    for name, text in sources:
        for tier, server, phrase, quote, verb in retired_server_findings(text, retired):
            (blocking if tier in (1, 2) else surfaced).append(
                (tier, name, server, phrase, quote, verb))

    for tier, name, server, phrase, quote, verb in blocking:
        why = ("names it outright" if tier == 1
               else f"stands in for it, in the action context `{verb}`")
        print(f"[BLOCK] Tier {tier}  {name}")
        print(f"      [Fail - Feasibility] retired server {server} is UNAVAILABLE and must "
              # `name` is the SOURCE FILE, not the word "prompt". A1 scans the OE as well, and
              # on real corpus data every Tier-1 hit lives in 6_Oracle_Events.txt rather than
              # the prompt, because hard rule 7 bans tool names from prompts and mandates them
              # in OEs. Hardcoding "prompt" here misattributed every real finding.
              f"not be used, and this {name} {why}, so the task is unsolvable.")
        print(f"      offending phrase: \"{phrase}\"")
        print(f"      ...{quote}...")
    if blocking:
        print()

    for tier, name, server, phrase, quote, verb in surfaced:
        print(f"[SURFACE] Tier 3  {name}  (never blocks)")
        print(f"      `{phrase}` could imply {server}, but no action verb sits within "
              f"{_WINDOW_WORDS} words, so it reads as prose rather than a dependency. "
              f"Listed for the human review the spec's quote-the-phrase step requires.")
        print(f"      ...{quote}...")
    if surfaced:
        print()

    if not blocking and not surfaced:
        print(f"[OK] {task.name}: no retired-server dependency found.")
        return 0
    if blocking:
        print(f"{len(blocking)} blocking hit(s). A1 is a HARD GATE and Feasibility is BINARY "
              f"(Fail=2 / Pass=5, no partial band): one hit fails the sub-dimension.")
        return 1
    print(f"[OK] {task.name}: no blocking hit. Tier 3 is informational.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
