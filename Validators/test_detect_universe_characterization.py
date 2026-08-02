#!/usr/bin/env python3
"""
Usage:
    python Validators/test_detect_universe_characterization.py

An APPROVAL / CHARACTERIZATION test over `detect_universe()`.

Why this exists
---------------
Characterization tests in the Feathers / Emily Bache sense pin what the code CURRENTLY
does, not what it SHOULD do. That distinction is the whole point. `detect_universe()` is a
heuristic - four regexes, a max, and a tie-break that prefers brookfield - and there is no
specification anywhere that says what it ought to return for any given task. So there is
nothing to assert against. What CAN be asserted is that it keeps returning what it returns
today, for every task in the repo, which is exactly the safety net needed before a fifth
universe adds a fifth regex to the same max.

Adding a signal set is not additive. A new regex can outscore an existing one on a task it
was never meant to match, and the tie-break silently reassigns any task whose new top score
ties. Nothing downstream would notice: a misdetected universe yields the wrong `today`, the
wrong slack channels and the wrong tool-parameter traps, and every validator keeps exiting 0.

This test makes that class of change visible as a diff.

Both the verdict AND the score vector are pinned
------------------------------------------------
Pinning only the winner would hide the interesting movement. A task that scores
brookfield=9 / starpm=2 today and brookfield=9 / starpm=8 after a change still reports
"brookfield" - and is one signal away from flipping. The margin is the early warning, so
the raw per-universe scores are pinned too.

Bypassing the cache
-------------------
`detect_universe()` returns the cached `_aux/Universe.txt` value when present, and WRITES
that file when absent. Calling it here would therefore (a) read back a previous answer
instead of exercising the scorer and (b) mutate task directories. So the scoring is
re-implemented inline from the same private signal regexes, over the same four candidate
files, with the same 50000-char slice and the same tie-break. Nothing under QC_Tasks/ or
Tasks/ is read except those files, and nothing there is written.

If `detect_universe()`'s algorithm changes, `_score_task()` below must change with it, or
this test pins a fiction. That coupling is deliberate and is the cost of not touching the
fixtures.

Behavior
--------
First run (baseline absent):  writes the baseline, prints "PINNED N fixtures", exits 0.
Later runs:                   compares, prints a per-fixture diff, exits non-zero on drift.

A fixture that APPEARS or DISAPPEARS is reported but is not drift: `Tasks/` grows as work
lands, and a new task directory is not a regression in `detect_universe()`. Only a fixture
present in both the baseline and the current scan, whose universe or score vector CHANGED,
counts as drift.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

try:
    from Validators.universes import (
        UNIVERSES,
        _BROOKFIELD_SIGNALS,
        _KEYSTONE_SIGNALS,
        _MOVEOPS_SIGNALS,
        _STARPM_SIGNALS,
    )
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from universes import (
        UNIVERSES,
        _BROOKFIELD_SIGNALS,
        _KEYSTONE_SIGNALS,
        _MOVEOPS_SIGNALS,
        _STARPM_SIGNALS,
    )

BASELINE = ROOT / "Validators" / "regression_baseline" / "detect_universe_characterization.json"

FIXTURE_ROOTS = [
    "QC_Tasks/V3_Buckets",
    "QC_Tasks/V3.1_Buckets",
    "QC_Tasks/V2.1_Buckets",
    "QC_Tasks/V4_Tasks",
    "Tasks",
]

# The same four candidate files detect_universe() reads, in the same order.
TEXT_CANDIDATES = ("1_Business_Function.txt", "2_Persona.txt", "5_Prompt.txt")
UNIVERSE_DATA = "3_UniverseDataForThisTask.json"
UNIVERSE_DATA_SLICE = 50000

SIGNALS = {
    "keystone": _KEYSTONE_SIGNALS,
    "brookfield": _BROOKFIELD_SIGNALS,
    "moveops": _MOVEOPS_SIGNALS,
    "starpm": _STARPM_SIGNALS,
}


def _score_task(task_dir: Path) -> dict:
    """Mirror of detect_universe()'s scoring, minus the cache read and the marker write."""
    scores = {"brookfield": 0, "keystone": 0, "moveops": 0, "starpm": 0}

    for candidate in TEXT_CANDIDATES:
        f = task_dir / candidate
        if f.is_file():
            text = f.read_text(encoding="utf-8", errors="ignore")
            for name, pattern in SIGNALS.items():
                scores[name] += len(pattern.findall(text))

    universe_data = task_dir / UNIVERSE_DATA
    if universe_data.is_file():
        sample = universe_data.read_text(encoding="utf-8", errors="ignore")[:UNIVERSE_DATA_SLICE]
        for name, pattern in SIGNALS.items():
            scores[name] += len(pattern.findall(sample))

    return scores


def _resolve(scores: dict) -> str:
    """Mirror of detect_universe()'s tie-break: all-zero -> brookfield; brookfield wins ties."""
    if all(v == 0 for v in scores.values()):
        return "brookfield"
    max_score = max(scores.values())
    winners = [u for u, s in scores.items() if s == max_score]
    if "brookfield" in winners:
        return "brookfield"
    return sorted(winners)[0]


def find_fixtures() -> list:
    """Every directory under the fixture roots holding at least one candidate file."""
    wanted = set(TEXT_CANDIDATES) | {UNIVERSE_DATA}
    found = set()
    for rel in FIXTURE_ROOTS:
        root = ROOT / rel
        if not root.is_dir():
            continue
        for path in root.rglob("*"):
            if path.is_dir() and any((path / name).is_file() for name in wanted):
                found.add(path)
    return sorted(found, key=lambda p: p.relative_to(ROOT).as_posix())


def observe() -> dict:
    """fixture id -> {universe, scores} for every fixture, computed fresh."""
    observed = {}
    for task_dir in find_fixtures():
        scores = _score_task(task_dir)
        observed[task_dir.relative_to(ROOT).as_posix()] = {
            "universe": _resolve(scores),
            "scores": scores,
        }
    return observed


def load_baseline() -> dict:
    return json.loads(BASELINE.read_text(encoding="utf-8"))["fixtures"]


def write_baseline(observed: dict) -> None:
    BASELINE.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "_meta": {
            "purpose": "Characterization pin for Validators/universes.py detect_universe(). "
                       "Records CURRENT behavior, not desired behavior. Regenerate only with "
                       "a deliberate, reviewed reason.",
            "produced_by": "Validators/test_detect_universe_characterization.py",
            "universes_at_pin_time": sorted(UNIVERSES),
            "fixture_roots": FIXTURE_ROOTS,
            "candidate_files": list(TEXT_CANDIDATES) + [UNIVERSE_DATA],
            "universe_data_slice_chars": UNIVERSE_DATA_SLICE,
        },
        "fixtures": observed,
    }
    BASELINE.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    observed = observe()

    print("=== detect_universe characterization ===")
    print(f"roots: {', '.join(FIXTURE_ROOTS)}")
    print(f"baseline: {BASELINE.relative_to(ROOT).as_posix()}\n")

    if not BASELINE.is_file():
        write_baseline(observed)
        tally = {}
        for rec in observed.values():
            tally[rec["universe"]] = tally.get(rec["universe"], 0) + 1
        print(f"PINNED {len(observed)} fixtures")
        print(f"  distribution: {', '.join(f'{u}={n}' for u, n in sorted(tally.items()))}")
        print()
        print("Baseline written. Re-run after any change to detect_universe() or its signal")
        print("regexes; a diff here means task-to-universe routing moved.")
        return 0

    baseline = load_baseline()

    added = sorted(set(observed) - set(baseline))
    removed = sorted(set(baseline) - set(observed))
    shared = sorted(set(observed) & set(baseline))

    drifted = []
    for fid in shared:
        was, now = baseline[fid], observed[fid]
        if was.get("universe") != now["universe"] or was.get("scores") != now["scores"]:
            drifted.append((fid, was, now))

    if drifted:
        print(f"[FAIL] {len(drifted)} fixture(s) drifted:\n")
        for fid, was, now in drifted:
            print(f"  {fid}")
            if was.get("universe") != now["universe"]:
                print(f"    universe: expected {was.get('universe')!r} -> actual {now['universe']!r}")
            else:
                print(f"    universe: {now['universe']!r} (unchanged)")
            if was.get("scores") != now["scores"]:
                keys = sorted(set(was.get("scores", {})) | set(now["scores"]))
                exp = ", ".join(f"{k}={was.get('scores', {}).get(k, '-')}" for k in keys)
                act = ", ".join(f"{k}={now['scores'].get(k, '-')}" for k in keys)
                print(f"    scores:   expected {exp}")
                print(f"              actual   {act}")
            print()

    if added:
        print(f"[NOTE] {len(added)} new fixture(s) not in the baseline (not drift):")
        for fid in added[:20]:
            print(f"    + {fid} -> {observed[fid]['universe']}")
        if len(added) > 20:
            print(f"    ... and {len(added) - 20} more")
        print()

    if removed:
        print(f"[NOTE] {len(removed)} baseline fixture(s) no longer present (not drift):")
        for fid in removed[:20]:
            print(f"    - {fid} (was {baseline[fid].get('universe')})")
        if len(removed) > 20:
            print(f"    ... and {len(removed) - 20} more")
        print()

    print(f"DETECT CHARACTERIZATION: {len(observed)} fixtures, {len(drifted)} drifted")

    if drifted:
        print()
        print("A drift here is not automatically a bug: if the change to detect_universe() was")
        print("intended to reroute these tasks, the new behavior is correct and the baseline")
        print("should be regenerated. What this test guarantees is that the reroute was SEEN.")
        print("Delete the baseline and re-run to re-pin, but only after reading every line")
        print("above and confirming each move is the one that was intended.")
        return 1

    print("[OK] every shared fixture resolves to its pinned universe with its pinned scores.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
