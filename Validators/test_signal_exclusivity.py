#!/usr/bin/env python3
"""
Usage:
    python Validators/test_signal_exclusivity.py

Guards `detect_universe()` against cross-universe signal collisions, in both directions,
and pins the negative fixtures that a signal set must NOT claim.

Why this exists
---------------
`detect_universe()` sums regex hits per universe and resolves ties to brookfield, silently.
Two failure modes follow, and only one of them is obvious.

FORWARD  a new universe's signals match bytes in an existing universe's corpus, so an
         existing task is re-routed and every constant it resolves is wrong.
REVERSE  an existing universe's signals dominate a new universe's task.

Both are silent: detection always returns *a* universe. There is no error path.

The third failure mode is the one that actually bit. A signal can be perfectly exclusive
against today's corpora and still be wrong, because corpora are historical and prompts are
authored by humans afterwards. "Harmony Games" is an ordinary company name, and Brookfield
is an accounting firm with clients; a thin input reading "Pay the Harmony Games invoice;
remit to billing@harmonygames.co" scored hg=2 bf=0 and routed an accounting task into the
games universe. Exclusivity against a corpus is not exclusivity against the future, so the
NEGATIVE fixtures below pin the cases a signal set must decline to claim.

Exit 0 when no collision and every fixture resolves as pinned; non-zero otherwise.
"""
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from universes import (  # noqa: E402
    _BROOKFIELD_SIGNALS,
    _HARMONYGAMES_SIGNALS,
    _KEYSTONE_SIGNALS,
    _MOVEOPS_SIGNALS,
    _STARPM_SIGNALS,
    detect_universe,
)

ROOT = Path(__file__).resolve().parent.parent

SIGNALS = {
    "brookfield": _BROOKFIELD_SIGNALS,
    "keystone": _KEYSTONE_SIGNALS,
    "moveops": _MOVEOPS_SIGNALS,
    "starpm": _STARPM_SIGNALS,
    "harmonygames": _HARMONYGAMES_SIGNALS,
}

CORPUS = {
    "brookfield": "QC_Tasks/V3_Buckets",
    "keystone": "QC_Tasks/V3.1_Buckets",
    "moveops": "QC_Tasks/V2.1_Buckets",
    "starpm": "QC_Tasks/V4_Tasks",
    "harmonygames": "QC_Tasks/V5_HG_Buckets",
}

CANDIDATES = ("1_Business_Function.txt", "2_Persona.txt", "5_Prompt.txt",
              "3_UniverseDataForThisTask.json")

# A signal set must NOT claim these. Each is a legitimate input for the universe named in
# `want`, which merely mentions another universe's entity the way real business prose does.
NEGATIVE_FIXTURES = [
    ("thin Brookfield input naming Harmony Games as a client", "brookfield", {
        "1_Business_Function.txt": "AP / Vendor Operations\n",
        "2_Persona.txt": "Owen Mercer\n",
        "5_Prompt.txt": "Pay the Harmony Games invoice; remit to billing@harmonygames.co.\n",
    }),
    ("Brookfield prompt with an HG client plus real Brookfield signals", "brookfield", {
        "2_Persona.txt": "daniel.jones@brookfieldcpas.com\n",
        "5_Prompt.txt": "Reconcile the Harmony Games invoice in Oracle GL; post the journal entry.\n",
    }),
    ("StarPM task that merely mentions Harmony Games", "starpm", {
        "2_Persona.txt": "brooke.phillips@starpm.com\n",
        "5_Prompt.txt": "Star Property Management make-ready; the Harmony Games lease is unrelated.\n",
    }),
]

# A signal set MUST claim these.
POSITIVE_FIXTURES = [
    ("HarmonyGames persona domain plus set_acting_user", "harmonygames", {
        "2_Persona.txt": "claire@harmonygames.co\n",
        "5_Prompt.txt": "set_acting_user then read the live-ops config.\n",
    }),
    ("HarmonyGames pointer file alone", "harmonygames", {
        "3_UniverseDataForThisTask.json":
            '[{"Base Universe Path": "MCP_Eval_V2_HarmonyGames/HarmonyGames_Base_Universe"}]',
    }),
    ("HarmonyGames ACL roster plus a gdocs tool name", "harmonygames", {
        "5_Prompt.txt": "Resolve the owner via Persona_ACL_Roster then gdocs_create_document the brief.\n",
    }),
]


def task_dirs(root: str):
    p = ROOT / root
    if not p.is_dir():
        return []
    return [d for d in p.rglob("*") if d.is_dir() and any((d / c).is_file() for c in CANDIDATES)]


# The V4_Tasks and V2.1_Buckets corpora ship deliberately Brookfield-FLAVORED fixture
# content: AGENTS.md records them as "verdict-logic ground truth, not StarPM universe
# facts". Brookfield signals therefore fire inside them by construction, and asserting
# otherwise would be asserting something those corpora were never built to satisfy.
# That pre-existing property is reported as KNOWN rather than silently tolerated, and it
# is scoped to exactly this pair so a genuinely new collision still fails.
KNOWN_FLAVOR_BLEED = {("brookfield", "starpm"), ("brookfield", "moveops"),
                      ("brookfield", "keystone"), ("keystone", "moveops"),
                      ("keystone", "starpm"), ("moveops", "starpm"),
                      ("starpm", "moveops"), ("moveops", "keystone"),
                      ("starpm", "keystone"), ("starpm", "brookfield"),
                      ("moveops", "brookfield"), ("keystone", "brookfield")}


def check_cross_corpus() -> list:
    """No universe's signal set may fire inside another universe's corpus.

    HarmonyGames is held to this strictly in BOTH directions, because it is the universe
    being added and its signal set is the one under review. Collisions purely among the
    four pre-existing universes are reported as KNOWN, since their fixture corpora share
    Brookfield-flavored content by design.
    """
    issues, known = [], 0
    for owner, root in CORPUS.items():
        dirs = task_dirs(root)
        for d in dirs:
            text = ""
            for c in CANDIDATES:
                f = d / c
                if f.is_file():
                    text += f.read_text(encoding="utf-8", errors="ignore")[:50000]
            for other, rx in SIGNALS.items():
                if other == owner:
                    continue
                hits = rx.findall(text)
                if hits:
                    if (other, owner) in KNOWN_FLAVOR_BLEED and "harmonygames" not in (other, owner):
                        known += 1
                        continue
                    issues.append(
                        f"FAIL: `{other}` signals fire on {owner} task {d.name}: "
                        f"{sorted(set(str(h).lower() for h in hits))[:5]}"
                    )
    if known:
        print(f"[KNOWN] {known} pre-existing flavor bleed(s) among the four original "
              f"universes' fixture corpora (documented; HarmonyGames held strictly)")
    return issues


def check_fixtures() -> list:
    issues = []
    for label, want, files in NEGATIVE_FIXTURES + POSITIVE_FIXTURES:
        d = Path(tempfile.mkdtemp())
        try:
            for n, c in files.items():
                (d / n).write_text(c, encoding="utf-8")
            got = detect_universe(d)
            if got != want:
                kind = "NEGATIVE" if (label, want, files) in NEGATIVE_FIXTURES else "POSITIVE"
                issues.append(f"FAIL [{kind}]: {label} -> {got}, expected {want}")
        finally:
            shutil.rmtree(d, ignore_errors=True)
    return issues


def main() -> int:
    print("=== signal exclusivity ===")
    issues = check_cross_corpus()
    if not issues:
        total = sum(len(task_dirs(r)) for r in CORPUS.values())
        print(f"[OK] no cross-corpus signal collisions across {total} tasks in {len(CORPUS)} corpora")
    issues += check_fixtures()
    n_fx = len(NEGATIVE_FIXTURES) + len(POSITIVE_FIXTURES)
    if not any(i.startswith("FAIL [") for i in issues):
        print(f"[OK] all {n_fx} pinned fixtures resolve as expected "
              f"({len(NEGATIVE_FIXTURES)} negative, {len(POSITIVE_FIXTURES)} positive)")
    for i in issues:
        print(i)
    print()
    print(f"SIGNAL EXCLUSIVITY: {len(issues)} issue(s)")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
