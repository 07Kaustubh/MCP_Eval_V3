#!/usr/bin/env python3
"""
test_memory_bounds.py - standing gate on the constant-memory universe scan.

Usage:
    python3 Validators/test_memory_bounds.py               # run the gate
    python3 Validators/test_memory_bounds.py --self-check  # prove it can report dirty
    python3 Validators/test_memory_bounds.py --verbose

Why this file exists
--------------------
`verify_universe_atoms.py` answers "does this atom appear in the universe?". For an
export-backed universe (HarmonyGames) the universe is the hydrated base export: 5.0 GB
today, 8.1 GB after the current drop, including a single 223 MB
`Base_Universe_Complete_Data.json` that becomes 359 MB in the new drop.

An earlier fix for the phantom-atom bug was OOM-KILLED because it materialised that
payload. The surviving fix (commit ef75e26) streams instead: one pass, one compiled
alternation of every atom, fixed-size chunks with an overlap so a needle straddling a
chunk boundary is still found. Memory is O(atoms), never O(universe).

Nothing enforced that. `grep -rn "ru_maxrss\\|getrusage\\|RUSAGE" Validators/` returned
NOTHING before this file, so a future edit could reintroduce a whole-file load and the
only symptom would be an OOM kill on the operator's machine - the failure mode that cost
this work a full attempt already. AGENTS.md rule 18: a closed finding must become a
standing gate, not a note in prose.

Measured on the 5.0 GB payload (macOS, Darwin 25.5.0), early exit deliberately defeated
so the scan reads EVERY file:

    streaming scan (correct)                        160.3 MiB peak RSS
    json.load(Base_Universe_Complete_Data.json)     673.0 MiB peak RSS

CEILING is set at 384 MiB: 2.4x headroom over correct behaviour so it cannot flake, and
1.75x below the forbidden operation so reintroduction trips it. The margin only widens
as the payload grows, because the streaming cost is O(atoms) while the whole-file cost
scales with the blob (359 MB blob => roughly 1.1 GB).

Three guards, deliberately layered
----------------------------------
G1 STATIC   - source-level. Runs in milliseconds, needs no hydration, and fails at EDIT
              time rather than at OOM time. This is the guard that makes the requirement
              "must FAIL, not OOM" unconditionally true: it never allocates anything.
G2 EMPIRICAL- runs the real scan against the real payload and asserts measured peak RSS.
              SKIPs cleanly when the payload is not hydrated (it is gitignored).
G3 SELFCHECK- `--self-check` mutates a COPY of the validator to do the forbidden thing and
              asserts G1 reports it. Per Validators/AGENTS.md: when a check reports clean,
              confirm it can report dirty. Three defects in this repo were matching rules
              that produced the expected number while matching the wrong thing.

Portability traps pinned here because both were verified empirically on this machine and
both silently corrupt the measurement:
  * `ru_maxrss` is BYTES on Darwin and KIBIBYTES on Linux. Unnormalised, the ceiling is
    wrong by 1024x and the gate becomes either vacuous or permanently red.
  * `RLIMIT_AS` is NOT settable on macOS ("current limit exceeds maximum limit"), so a
    hard address-space cap cannot be the enforcement mechanism. It is applied only where
    the OS honours it, as a belt-and-braces extra; G1+G2 are the real gate.
"""

import argparse
import ast
import os
import re
import resource
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "Validators" / "verify_universe_atoms.py"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from universes import UNIVERSES, get_universe_constants, get_framework_profile  # noqa: E402

CEILING_MIB = 384
CEILING_BYTES = CEILING_MIB * 1024 * 1024

# The scan must never whole-file load. These are the call shapes that do.
FORBIDDEN_CALLS = ("json.load", "json.loads", "read_text", "read_bytes", "readlines")


def peak_rss_bytes(children: bool = False) -> int:
    """Normalise ru_maxrss to BYTES.

    Darwin reports bytes; Linux reports kibibytes. Getting this wrong is a 1024x error,
    which would either make the ceiling unreachable (gate asserts nothing) or make it
    permanently exceeded (gate is noise). Verified on this machine: a 200 MiB allocation
    reported 224903168, i.e. bytes.
    """
    who = resource.RUSAGE_CHILDREN if children else resource.RUSAGE_SELF
    raw = resource.getrusage(who).ru_maxrss
    return raw if sys.platform == "darwin" else raw * 1024


def export_backed_universes() -> list:
    """Universes whose data is the base export, resolved from the REGISTRY.

    Deliberately NOT `if universe == "harmonygames"`. AGENTS.md documents 11 existing
    per-universe branches as intentional and asks for no 12th where a registry key will
    do. `universe_data_contract` already exists and already carries exactly this meaning,
    so no new flag is declared and check_capability_registry C3 flag-parity is untouched.
    """
    out = []
    for name in UNIVERSES:
        contract = get_framework_profile(name).get("universe_data_contract", "per_task_json")
        if contract == "base_export_plus_changelog":
            out.append(name)
    return out


def services_dir(universe: str) -> Path:
    return ROOT / get_universe_constants(universe)["base_path"] / "Services_Data"


def is_hydrated(universe: str) -> bool:
    d = services_dir(universe)
    try:
        return d.is_dir() and any(p.is_dir() for p in d.iterdir())
    except OSError:
        return False


# --------------------------------------------------------------------------------------
# G1 - static guard
# --------------------------------------------------------------------------------------

def guard_static(source: str) -> list:
    """Fail if the export scan could whole-file load. Allocates nothing, so it can only
    FAIL - never OOM. Returns a list of findings (empty == clean)."""
    findings = []
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        return [f"verify_universe_atoms.py does not parse: {e}"]

    presence = next((n for n in ast.walk(tree)
                     if isinstance(n, ast.ClassDef) and n.name == "Presence"), None)
    if presence is None:
        findings.append("class `Presence` is gone - the streaming seam moved; re-point this gate")
        return findings

    prime = next((n for n in ast.walk(presence)
                  if isinstance(n, ast.FunctionDef) and n.name == "prime"), None)
    if prime is None:
        findings.append("Presence.prime() is gone - the streaming seam moved; re-point this gate")
        return findings

    # (a) no whole-file read anywhere in the streaming path
    for node in ast.walk(prime):
        if not isinstance(node, ast.Call):
            continue
        name = ""
        if isinstance(node.func, ast.Attribute):
            base = node.func.value
            prefix = base.id + "." if isinstance(base, ast.Name) else ""
            name = prefix + node.func.attr
        elif isinstance(node.func, ast.Name):
            name = node.func.id
        for bad in FORBIDDEN_CALLS:
            if name == bad or name.endswith("." + bad.split(".")[-1]):
                findings.append(
                    f"Presence.prime() calls `{name}` - that materialises a whole file. "
                    f"The scan must stay chunked (this is the OOM that killed an earlier fix)."
                )

    # (b) reads must be bounded: at least one .read(<positive int>) with an argument
    bounded = False
    for node in ast.walk(prime):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr == "read"):
            if node.args:
                bounded = True
            else:
                findings.append("Presence.prime() calls .read() with NO size argument - "
                                "that reads the entire file into memory.")
    if not bounded:
        findings.append("Presence.prime() performs no bounded .read(size) - the scan is no "
                        "longer streaming.")

    # (c) the combined multi-hundred-MB blob must stay excluded from the walk
    if "_COMBINED_BLOB" not in source:
        findings.append("_COMBINED_BLOB constant is gone - the 223 MB combined export is no "
                        "longer being skipped by the scan.")
    else:
        scan = next((n for n in ast.walk(presence)
                     if isinstance(n, ast.FunctionDef) and n.name == "_scan_roots"), None)
        if scan is None:
            findings.append("Presence._scan_roots() is gone - cannot confirm the combined "
                            "blob is skipped.")
        else:
            seg = ast.get_source_segment(source, scan) or ""
            if "_COMBINED_BLOB" not in seg:
                findings.append("Presence._scan_roots() no longer references _COMBINED_BLOB - the "
                                "combined export would be streamed as if it were a service table.")
    return findings


# --------------------------------------------------------------------------------------
# G2 - empirical guard
# --------------------------------------------------------------------------------------

_PROBE = r"""
import resource, sys
from pathlib import Path
sys.path.insert(0, {validators!r})
try:
    resource.setrlimit(resource.RLIMIT_AS, ({cap}, resource.getrlimit(resource.RLIMIT_AS)[1]))
except (ValueError, OSError):
    pass  # macOS refuses RLIMIT_AS; G2's assertion on measured RSS is the real gate
from verify_universe_atoms import Presence
p = Presence({universe!r}, Path({task!r}), {{}}, {{}})
assert p.mode == "export", "expected the export backend, got " + p.mode
# One real atom plus one that cannot exist: the early exit can never fire, so this reads
# EVERY file in the payload. Measuring the happy path would understate peak memory.
p.prime({{{real!r}, "zzz-no-such-atom-anywhere@nowhere.invalid"}})
print("FOUND", len(p._found))
"""


def guard_empirical(universe: str, verbose: bool = False) -> list:
    findings = []
    task = None
    for cand in sorted((ROOT / "QC_Tasks" / "V5_HG_Buckets").glob("*/*_HG")):
        if (cand / "3_UniverseDataForThisTask.json").is_file():
            task = cand
            break
    if task is None:
        print(f"  [SKIP] G2: no {universe} task folder found to drive the scan")
        return findings

    code = _PROBE.format(
        validators=str(ROOT / "Validators"),
        cap=CEILING_BYTES,
        universe=universe,
        task=str(task),
        real="blake@harmonygames.co",
    )
    before = peak_rss_bytes(children=True)
    proc = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    after = peak_rss_bytes(children=True)
    peak = max(after, before)

    if proc.returncode != 0:
        tail = (proc.stderr or "").strip().splitlines()[-3:]
        if "MemoryError" in (proc.stderr or ""):
            findings.append(
                f"G2: the scan hit MemoryError under a {CEILING_MIB} MiB cap - it is no "
                f"longer constant-memory. {' | '.join(tail)}")
        else:
            findings.append(f"G2: probe failed ({proc.returncode}): {' | '.join(tail)}")
        return findings

    mib = peak / 1048576.0
    if verbose:
        print(f"  measured peak RSS (children): {mib:.1f} MiB   ceiling {CEILING_MIB} MiB")
        print(f"  probe stdout: {proc.stdout.strip()}")
    if peak > CEILING_BYTES:
        findings.append(
            f"G2: full-payload scan peaked at {mib:.1f} MiB, over the {CEILING_MIB} MiB "
            f"ceiling. Something in the scan is now O(universe) rather than O(atoms).")
    else:
        print(f"  [PASS] G2 empirical: peak {mib:.1f} MiB < {CEILING_MIB} MiB ceiling "
              f"(full payload, early exit defeated)")
    return findings


# --------------------------------------------------------------------------------------
# G3 - self-check: prove the gate reports dirty
# --------------------------------------------------------------------------------------

def run_self_check(verbose: bool = False) -> int:
    """Mutate a COPY to do the forbidden thing; G1 must catch every mutant.

    A gate that has only ever reported clean is indistinguishable from a gate that cannot
    report at all. This repo has been bitten three times by exactly that.
    """
    src = TARGET.read_text(encoding="utf-8")
    mutants = {
        "whole-file read_text() in prime()":
            (r"chunk = fh\.read\(8 << 20\)", "chunk = path.read_text()"),
        "unbounded .read() in prime()":
            (r"chunk = fh\.read\(8 << 20\)", "chunk = fh.read()"),
        "json.load() in prime()":
            (r"chunk = fh\.read\(8 << 20\)", "chunk = json.load(fh)"),
        "combined blob no longer skipped":
            (r"or name == _COMBINED_BLOB", ""),
    }
    print(f"Self-check: {len(mutants)} mutants, each MUST be caught by G1\n")
    missed = []
    for label, (pattern, replacement) in mutants.items():
        mutated, n = re.subn(pattern, replacement, src, count=1)
        if n != 1:
            missed.append(f"{label}: mutation seam not found (pattern {pattern!r}) - this "
                          f"gate is pointed at code that no longer exists")
            print(f"[STALE] {label} - seam not found")
            continue
        findings = guard_static(mutated)
        if findings:
            print(f"[CAUGHT] {label}")
            if verbose:
                for f in findings:
                    print(f"           - {f}")
        else:
            missed.append(f"{label}: NOT caught by G1 - the guard is blind to this "
                          f"reintroduction of a whole-file load")
            print(f"[MISSED] {label}")

    # The unmutated source must be clean, or "caught" above proves nothing.
    baseline = guard_static(src)
    if baseline:
        missed.append("baseline: G1 reports findings against the UNMUTATED file, so every "
                      "'caught' above is a false positive")
        print("[BASELINE DIRTY] G1 flags the real file")
    else:
        print("[BASELINE CLEAN] G1 is silent on the real file")

    print()
    if missed:
        print(f"SELF-CHECK: FAIL - {len(missed)} problem(s)")
        for m in missed:
            print(f"  - {m}")
        return 1
    print(f"SELF-CHECK: PASS - all {len(mutants)} mutants caught, baseline clean")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--self-check", action="store_true",
                    help="prove the gate can report dirty by mutating a copy")
    args = ap.parse_args()

    if args.self_check:
        return run_self_check(args.verbose)

    print(f"Memory bounds gate - ceiling {CEILING_MIB} MiB\n")
    findings = []

    print("G1 static (no hydration required):")
    g1 = guard_static(TARGET.read_text(encoding="utf-8"))
    findings += g1
    if g1:
        for f in g1:
            print(f"  [FAIL] {f}")
    else:
        print("  [PASS] the export scan is chunked, bounded, and skips the combined blob")

    universes = export_backed_universes()
    print(f"\nG2 empirical (export-backed universes from the registry: "
          f"{', '.join(universes) or 'none'}):")
    for u in universes:
        if not is_hydrated(u):
            print(f"  [SKIP] {u}: payload not hydrated ({services_dir(u)}) - gitignored by "
                  f"design; G1 still covered this edit")
            continue
        findings += guard_empirical(u, args.verbose)

    print()
    if findings:
        print(f"MEMORY BOUNDS: FAIL - {len(findings)} finding(s)")
        return 1
    print("MEMORY BOUNDS: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
