#!/usr/bin/env python3
"""
Usage:
    python Validators/test_s0_builders.py            # verify against the pinned baseline
    python Validators/test_s0_builders.py --update   # re-pin (deliberate act, see below)

Frozen-output gate for the three S0 builders on the NON-HarmonyGames universes.

Why this exists
---------------
check_regression.py was cited as proof that the HG-U21 / HG-U22 rewrites left the other
universes untouched. It is not. It runs `validate.py --phase all` over 7 snapshot tasks,
plus anchors, memory bounds and `qc_verdict selftest`, and it invokes NONE of:

    split_universe.py          rewritten to stream the split for export-backed universes
    universe_data_source.py    rewritten from a materialising loader to a generator
    build_universe_index.py    gained index_table_map, a new walk, and a rows_of skip
    build_fact_ledger.py       gained roster-seeded persona identities

So "reports 21/21 identical" proves `validate.py` is unchanged and states nothing at all
about the four builders that actually moved. The claim that the other universes' S0 output
was byte-identical existed only as prose, which AGENTS.md hard rule 18 forbids.

What this covers, and what it does not
-------------------------------------
COVERS: split_universe.py, build_universe_index.py and build_fact_ledger.py, end to end,
hashed file by file, over ALL SEVEN snapshot tasks that check_regression.py already pins
(3 brookfield, 2 keystone, 2 moveops) PLUS one starpm task, because starpm has no snapshot
task and would otherwise be the one non-HG universe with no builder coverage at all. The
task list is IMPORTED from check_regression rather than restated, so the two cannot drift.

Seven-plus-one rather than one-per-universe, because one-per-universe was a false economy:
same-universe tasks do NOT share a payload. The three brookfield snapshot tasks have three
distinct `3_UniverseDataForThisTask.json` hashes (d0366deb / a9b02330 / b2514d39), so a
second task of the same universe exercises a genuinely different data shape and can fail
independently. Measured cost of the full set is ~25s, against ~12s for the subset, which
is not worth the coverage given up.

DOES NOT COVER: HarmonyGames, whose builders are covered instead by the IDX-*/FL-*/UDS-*
anchors driving the real hydrated export; `build_graph_report.py` and
`build_feasible_surface.py`, which no baseline pins today; any task outside the pinned set;
and the semantic CORRECTNESS of any output. This is a frozen-output gate. It answers "did
the bytes move", not "are the bytes right".

Everything runs in a temp directory. Nothing under Tasks/ is read except the inputs, and
nothing there is written - a builder that wrote into the repo would be a finding, not a
convenience.

Re-pinning
----------
`--update` rewrites regression_baseline/s0_builder_hashes.txt. That is a deliberate act:
it declares the new bytes correct. Only run it when the output SHOULD have moved, and say
in the commit why. A re-pin that follows a surprise is how a real regression gets adopted
as the baseline.
"""

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = Path(__file__).resolve().parent / "regression_baseline"
PIN = BASE / "s0_builder_hashes.txt"

# starpm has no snapshot task, so it is named explicitly; everything else is imported.
_STARPM_SUBJECT = "39_6a602c8886ebb06f12354d77"


def subjects():
    """The 7 pinned snapshot tasks + one starpm task, labelled by their own Universe.txt.

    SNAPSHOT_TASKS is imported, never restated: a second copy of that list is exactly the
    kind of drift W10 exists to catch, and this gate would silently stop covering a task
    that check_regression had added.
    """
    sys.path.insert(0, str(ROOT / "Validators"))
    from check_regression import SNAPSHOT_TASKS
    out = []
    for name in list(SNAPSHOT_TASKS) + [_STARPM_SUBJECT]:
        rel = f"Tasks/{name}"
        ux = ROOT / rel / "_aux" / "Universe.txt"
        universe = ux.read_text(encoding="utf-8").strip() if ux.is_file() else "unknown"
        out.append((f"{universe}/{name}", rel))
    return out


SUBJECTS = None   # resolved lazily in collect(); see subjects()

BUILDERS = [
    ("split_universe", ["split_universe.py"]),
    ("universe_index", ["build_universe_index.py"]),
    ("fact_ledger",    ["build_fact_ledger.py"]),
]

# Inputs copied into the sandbox. _aux/Universe.txt is copied deliberately: detect_universe()
# WRITES its verdict into the directory it is pointed at, and a gate must not depend on a
# side effect it also measures.
INPUTS = ["3_UniverseDataForThisTask.json", "1_Business_Function.txt", "2_Persona.txt",
          "5_Prompt.txt", "4_Changelog.json", "9_Universe_inject.sql"]


def sha256_text(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def sha256_file(p: Path, sandbox=()) -> str:
    """Hash a produced artifact OS-neutrally, with the sandbox path normalised out.

    Mirrors check_regression.sha256 on line endings: the baseline is captured on macOS
    with LF, and a raw byte hash would report drift for content that is otherwise
    identical.

    The `sandbox` substitution is NOT masking builder output. build_fact_ledger records
    the task directory it was pointed at in `meta.task_dir`, and this gate points it at a
    fresh mkdtemp path every run, so without this the ledger hash would differ on every
    invocation and the gate would be permanently red for a reason that has nothing to do
    with the builders. Verified by diffing two consecutive runs of the same code on the
    same input: `meta.task_dir` was the ONLY differing field, so the builders are
    otherwise deterministic and nothing else is being normalised away.
    """
    raw = p.read_bytes()
    try:
        text = raw.decode("utf-8").replace("\r\n", "\n")
    except UnicodeDecodeError:
        return hashlib.sha256(raw).hexdigest()
    for s in (sandbox or ()):
        if s:
            text = text.replace(s, "<SANDBOX>")
    return sha256_text(text)


def build_one(universe: str, task_rel: str) -> dict:
    """Run the three builders in a sandbox; return {relative_output_path: sha256}."""
    src = ROOT / task_rel
    out = {}
    with tempfile.TemporaryDirectory(prefix="s0_" + universe.replace("/", "_") + "_") as tmp:
        work = Path(tmp) / "task"
        (work / "_aux").mkdir(parents=True)
        for name in INPUTS:
            if (src / name).is_file():
                shutil.copy2(src / name, work / name)
        ux = src / "_aux" / "Universe.txt"
        if ux.is_file():
            shutil.copy2(ux, work / "_aux" / "Universe.txt")

        # The input itself is part of the pin. If a universe payload is ever re-dropped,
        # this moves and the failure names the input rather than blaming the builders.
        ud = work / "3_UniverseDataForThisTask.json"
        if not ud.is_file():
            raise SystemExit(f"FAIL: {task_rel} has no 3_UniverseDataForThisTask.json")
        out["SOURCE_SHA"] = sha256_file(ud)   # input, no sandbox path inside

        for label, argv in BUILDERS:
            proc = subprocess.run(
                [sys.executable, str(ROOT / "Validators" / argv[0]), str(work)],
                capture_output=True, text=True)
            if proc.returncode != 0:
                raise SystemExit(
                    f"FAIL: {label} exited {proc.returncode} for {universe}\n"
                    f"{proc.stdout[-2000:]}\n{proc.stderr[-2000:]}")

        aux = work / "_aux"
        for p in sorted(aux.rglob("*")):
            if not p.is_file():
                continue
            rel = p.relative_to(aux).as_posix()
            # Universe.txt is an input we supplied, not a builder product.
            if rel == "Universe.txt":
                continue
            # Three spellings, because the builders do not agree on one. macOS mkdtemp
            # hands back /var/... while .resolve() yields /private/var/..., and
            # build_fact_ledger records neither - it stores only the last two components
            # ("<randomdir>/task"), so the random directory NAME has to be normalised too.
            out[rel] = sha256_file(p, sandbox=(str(work.resolve()), str(work),
                                               Path(tmp).name))
    return out


def collect() -> dict:
    return {u: build_one(u, t) for u, t in subjects()}


def load_pin() -> dict:
    if not PIN.is_file():
        return {}
    return json.loads(PIN.read_text(encoding="utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--update", action="store_true",
                    help="re-pin the baseline (declares the current bytes correct)")
    args = ap.parse_args()

    live = collect()

    if args.update:
        PIN.write_text(json.dumps(live, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        n = sum(len(v) for v in live.values())
        print(f"PINNED {n} artifact hashes across {len(live)} universes -> "
              f"{PIN.relative_to(ROOT)}")
        return 0

    pin = load_pin()
    if not pin:
        print(f"FAIL: no baseline at {PIN.relative_to(ROOT)}. Run --update once, "
              f"deliberately, and say why in the commit.")
        return 1

    failures, checked = [], 0
    for universe in sorted(set(pin) | set(live)):
        want, got = pin.get(universe), live.get(universe)
        if want is None:
            failures.append(f"{universe}: produced output but is not in the baseline")
            continue
        if got is None:
            failures.append(f"{universe}: in the baseline but produced nothing")
            continue
        for rel in sorted(set(want) | set(got)):
            checked += 1
            a, b = want.get(rel), got.get(rel)
            if a is None:
                failures.append(f"{universe}/{rel}: NEW artifact, not in the baseline")
            elif b is None:
                failures.append(f"{universe}/{rel}: MISSING, the baseline expects it")
            elif a != b:
                failures.append(f"{universe}/{rel}: CHANGED ({a[:12]} -> {b[:12]})")

    print("=== S0 builder frozen-output gate ===")
    print(f"{len(subjects())} tasks · {checked} artifacts · "
          f"builders: {', '.join(b[0] for b in BUILDERS)}\n")
    for f in failures:
        print(f"  {f}")
    if failures:
        print(f"\n[FAIL] {len(failures)} S0 builder output difference(s). If this is "
              f"intended, re-pin with --update and say why.")
        return 1
    print(f"[OK] all {checked} S0 builder artifacts byte-identical to the baseline.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
