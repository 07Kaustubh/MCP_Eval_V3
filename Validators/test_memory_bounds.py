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
ACCESSOR = ROOT / "Validators" / "universe_data_source.py"

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

    # (c) the walk must stay extension-filtered.
    #
    # This REPLACED the old _COMBINED_BLOB check. That check asserted the scan skipped
    # Base_Universe_Complete_Data.json; the V5 drop does not ship that file, `find` matches
    # zero of them, so the check guarded dead code and could not fail for a real reason.
    # The filter below is the live equivalent: the payload carries a 105,206,509-byte git
    # packfile at github/root/harmonygames-Games/liveops/.git/objects/pack/ plus ~245k other
    # non-JSON files, and `name.endswith(".json")` in _scan_roots is the ONLY thing keeping
    # them out of the byte stream. Drop it and the scan streams 7.6 GB instead of 1.9 GB.
    scan = next((n for n in ast.walk(presence)
                 if isinstance(n, ast.FunctionDef) and n.name == "_scan_roots"), None)
    if scan is None:
        findings.append("Presence._scan_roots() is gone - cannot confirm the walk is still "
                        "extension-filtered, so the 105 MB packfile would be streamed.")
    else:
        seg = ast.get_source_segment(source, scan) or ""
        if '".json"' not in seg and "'.json'" not in seg:
            findings.append("Presence._scan_roots() no longer filters on the .json extension - "
                            "the 105 MB git packfile and ~245k non-JSON payload files would be "
                            "streamed as if they were service tables.")

    # (d) the chunk must not be retained across iterations.
    #
    # A bounded .read(size) inside a loop that appends into a growing buffer is still
    # O(file): it satisfies (a) and (b) and defeats both. None of the read-shape mutants can
    # express this, so without (d) the suite has a blind spot exactly where rule 33 bites.
    for node in ast.walk(prime):
        if (isinstance(node, ast.AugAssign) and isinstance(node.op, ast.Add)
                and isinstance(node.value, ast.Name) and node.value.id == "chunk"):
            findings.append(
                "Presence.prime() accumulates `chunk` into a growing buffer - the read is "
                "bounded but the retention is not, so peak memory is O(file) again.")
    return findings


# --------------------------------------------------------------------------------------
# G1b - static guard on the ACCESSOR path (universe_data_source)
#
# Why a SECOND static guard rather than widening the first: the two files answer different
# questions and fail differently. verify_universe_atoms streams BYTES to answer "does this
# atom appear anywhere"; universe_data_source yields ROWS to answer "what records exist".
# G1 above is keyed to Presence.prime()'s chunked byte reads, which have no counterpart
# here, so pointing it at this file would report clean against code it cannot describe.
#
# This guard exists because that is exactly what happened. AGENTS.md HG-U22 recorded
# `load_universe_records` peaking at ~1.55 GiB - 4x this file's own ceiling - and the gate
# sat next to it reporting PASS, because `guard_static` targets `class Presence` and
# nothing else. A ceiling that only watches one of the two paths that can breach it is
# a ceiling for one path.
# --------------------------------------------------------------------------------------

def guard_static_accessor(source: str) -> list:
    """Fail if the base-export walk could materialise the payload. Allocates nothing."""
    findings = []
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        return [f"universe_data_source.py does not parse: {e}"]

    walk = next((n for n in ast.walk(tree)
                 if isinstance(n, ast.FunctionDef) and n.name == "_iter_base_export"), None)
    if walk is None:
        findings.append("`_iter_base_export` is gone - the streaming seam moved; re-point "
                        "this gate. (It replaced `_stream_base_export`, which returned a "
                        "list and is the shape HG-U22 records.)")
        return findings

    seg = ast.get_source_segment(source, walk) or ""

    # (a) it must be a generator. A function that returns a list is O(universe) by
    #     construction no matter how carefully each file is read.
    if not any(isinstance(n, (ast.Yield, ast.YieldFrom)) for n in ast.walk(walk)):
        findings.append(
            "`_iter_base_export` contains no `yield` - it accumulates and returns instead of "
            "streaming, which is the 1.55 GiB shape AGENTS.md HG-U22 describes.")

    # (a2) and it must not accumulate. `yield` alone is not enough: the walk has two yield
    #      sites, so replacing one with an append leaves the function a generator while
    #      quietly building a list again. This is the precise shape of HG-U22, and without
    #      this check the matching mutant was only ever "caught" because the replacement
    #      happened to be unbalanced - i.e. as a SyntaxError, proving nothing about memory.
    for node in ast.walk(walk):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr == "append":
            findings.append(
                "`_iter_base_export` calls `.append(...)` - it is accumulating records "
                "instead of yielding them, which is the O(universe) shape this gate exists "
                "to prevent, whether or not a `yield` survives elsewhere in the function.")

    # (b) no recursive glob. `rglob` is the specific call that descended into gdrive/root/
    #     and github/root/ and promoted 296k individual file payloads to universe records.
    for node in ast.walk(walk):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr in ("rglob", "walk"):
            findings.append(
                f"`_iter_base_export` calls `.{node.func.attr}()` - a recursive walk descends "
                f"into the per-file payload trees (gdrive/root, github/root) and turns every "
                f"individual file into its own record source. That is the HG-U21/HG-U22 root "
                f"cause: 47,571 junk source stems and 715,697 records.")

    # (c) the include/exclude rule must come from the registry, not from a literal in here.
    #     A hardcoded filename list makes the next upstream rename a silent breakage rather
    #     than a config change.
    if "export_table_scan" not in seg:
        findings.append(
            "`_iter_base_export` no longer reads the `export_table_scan` contract from the "
            "registry - the table/payload split has been hardcoded, so an upstream rename "
            "fails silently instead of loudly.")

    # (c2) the per-file reader must not hold a whole file. MEASURED: with the walk already
    #      scoped to the real tables, `json.loads` on the payload still peaked at 738 MiB and
    #      merely holding the file TEXT still peaked at 620 MiB, because CPython widens
    #      github/data.json from 39.4 MB on disk to a 157.4 MB str. Scoping the walk was
    #      necessary and not sufficient, so both halves are guarded.
    rows = next((n for n in ast.walk(tree)
                 if isinstance(n, ast.FunctionDef) and n.name == "_iter_table_rows"), None)
    if rows is None:
        findings.append("`_iter_table_rows` is gone - the per-file streaming seam moved; "
                        "re-point this gate.")
    else:
        for node in ast.walk(rows):
            if not isinstance(node, ast.Call):
                continue
            nm = ""
            if isinstance(node.func, ast.Attribute):
                base = node.func.value
                nm = (base.id + "." if isinstance(base, ast.Name) else "") + node.func.attr
            elif isinstance(node.func, ast.Name):
                nm = node.func.id
            if nm in ("json.load", "json.loads", "read_text", "read_bytes") \
                    or nm.endswith(".read_text") or nm.endswith(".read_bytes"):
                findings.append(
                    f"`_iter_table_rows` calls `{nm}` - that materialises a whole service "
                    f"file. Measured: 738 MiB via json.loads, 620 MiB via file text alone, "
                    f"against a {CEILING_MIB} MiB ceiling.")

    # (c3) the sliding window must actually slide. A cursor that only ever APPENDS is
    #      lazy but not bounded: it ends up holding the entire file and measures exactly
    #      like the read_text version it replaced. Discarding the consumed prefix is the
    #      one line that makes it constant-memory, so it is guarded on its own.
    cursor = next((n for n in ast.walk(tree)
                   if isinstance(n, ast.ClassDef) and n.name == "_JsonCursor"), None)
    if cursor is None:
        findings.append("`_JsonCursor` is gone - the sliding-window seam moved; re-point "
                        "this gate.")
    else:
        fill = next((n for n in ast.walk(cursor)
                     if isinstance(n, ast.FunctionDef) and n.name == "_fill"), None)
        fseg = ast.get_source_segment(source, fill) if fill else ""
        if not fill or "self.buf[self.pos:]" not in (fseg or ""):
            findings.append(
                "`_JsonCursor._fill` no longer discards the consumed prefix "
                "(`self.buf = self.buf[self.pos:]`) - the window grows without bound, so the "
                "reader holds the whole file again and the 620 MiB measurement returns.")

    # (d) the caller must not re-materialise what the generator was written to avoid.
    loader = next((n for n in ast.walk(tree)
                   if isinstance(n, ast.FunctionDef) and n.name == "load_universe_records"), None)
    if loader is None:
        findings.append("`load_universe_records` is gone - re-point this gate.")
    else:
        lseg = ast.get_source_segment(source, loader) or ""
        for node in ast.walk(loader):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                    and node.func.id in ("list", "tuple", "sorted"):
                findings.append(
                    f"`load_universe_records` wraps the export stream in `{node.func.id}(...)` "
                    f"- that materialises every row and defeats the generator entirely.")
                break
        del lseg

    # (e) require_resolvable must stay cheap. It is called by FOUR S0 builders purely to ask
    #     "does this resolve?"; routing that through the record loader made every one of them
    #     pay the full payload cost for a yes/no answer.
    req = next((n for n in ast.walk(tree)
                if isinstance(n, ast.FunctionDef) and n.name == "require_resolvable"), None)
    if req is not None:
        for node in ast.walk(req):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                    and node.func.id in ("load_universe_records", "_iter_base_export"):
                findings.append(
                    f"`require_resolvable` calls `{node.func.id}` - four S0 builders call it "
                    f"only to ask whether the data resolves, so this reads the whole export "
                    f"to answer a boolean.")
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
        real="arthur.blake@harmonygames.co",
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


_ACCESSOR_PROBE = r"""
import resource, sys, collections
from pathlib import Path
sys.path.insert(0, {validators!r})
try:
    resource.setrlimit(resource.RLIMIT_AS, ({cap}, resource.getrlimit(resource.RLIMIT_AS)[1]))
except (ValueError, OSError):
    pass  # macOS refuses RLIMIT_AS; the assertion on measured RSS is the real gate
from universe_data_source import iter_universe_records
rows, meta = iter_universe_records(Path({task!r}), {universe!r})
# Consume the whole stream. Counting is the point: if the generator were a list in
# disguise the peak would show it, and if it stopped early the count would.
n = 0
srcs = collections.Counter()
for r in rows:
    n += 1
    srcs[r.get("source")] += 1
print("RECORDS", n)
print("SOURCES", len(srcs))
"""


def guard_empirical_accessor(universe: str, verbose: bool = False) -> list:
    """Measure the RECORD accessor, not just the byte scan.

    Separate from guard_empirical because it drives a different entry point. AGENTS.md
    HG-U22 is precisely the finding that measuring one proved nothing about the other.
    """
    findings = []
    task = _scratch_task(universe)
    if task is None:
        print(f"  [SKIP] G2b: could not stage a {universe} task to drive the accessor")
        return findings

    code = _ACCESSOR_PROBE.format(
        validators=str(ROOT / "Validators"),
        cap=CEILING_BYTES,
        task=str(task),
        universe=universe,
    )
    before = peak_rss_bytes(children=True)
    proc = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    after = peak_rss_bytes(children=True)
    peak = max(after, before)

    if proc.returncode != 0:
        tail = (proc.stderr or "").strip().splitlines()[-3:]
        findings.append(f"G2b: accessor probe failed ({proc.returncode}): {' | '.join(tail)}")
        return findings

    mib = peak / 1048576.0
    if verbose:
        print(f"  accessor peak RSS (children): {mib:.1f} MiB   ceiling {CEILING_MIB} MiB")
        print(f"  probe stdout: {proc.stdout.strip().splitlines()}")
    if peak > CEILING_BYTES:
        findings.append(
            f"G2b: iter_universe_records peaked at {mib:.1f} MiB, over the {CEILING_MIB} MiB "
            f"ceiling. This is the HG-U22 shape: the record accessor is O(universe).")
    else:
        counts = " ".join(proc.stdout.split())
        print(f"  [PASS] G2b accessor: peak {mib:.1f} MiB < {CEILING_MIB} MiB ceiling "
              f"({counts})")
    return findings


def _scratch_task(universe: str):
    """Stage a throwaway task dir OUTSIDE the repo that resolves to the base export.

    Deliberately NOT a QC_Tasks path. `detect_universe` write-caches `_aux/Universe.txt`
    into whatever directory it is handed, and the labeled corpus is content-hash pinned by
    check_qc_corpus.py, so pointing a detecting entry point at it mutates a pinned artifact.
    The pointer file is copied, never written back.
    """
    src = None
    for cand in sorted((ROOT / "QC_Tasks" / "V5_HG_Buckets").glob("*/*_HG")):
        if (cand / "3_UniverseDataForThisTask.json").is_file():
            src = cand
            break
    if src is None:
        return None
    tmp = Path(tempfile.mkdtemp(prefix="membounds_task_"))
    (tmp / "_aux").mkdir(parents=True, exist_ok=True)
    (tmp / "_aux" / "Universe.txt").write_text(universe + "\n", encoding="utf-8")
    shutil.copy2(src / "3_UniverseDataForThisTask.json", tmp / "3_UniverseDataForThisTask.json")
    if (src / "4_Changelog.json").is_file():
        shutil.copy2(src / "4_Changelog.json", tmp / "4_Changelog.json")
    _SCRATCH_DIRS.append(tmp)
    return tmp


_SCRATCH_DIRS = []


def _cleanup_scratch() -> None:
    while _SCRATCH_DIRS:
        shutil.rmtree(_SCRATCH_DIRS.pop(), ignore_errors=True)


# --------------------------------------------------------------------------------------
# G3 - self-check: prove the gate reports dirty
# --------------------------------------------------------------------------------------

def run_self_check(verbose: bool = False) -> int:
    """Mutate a COPY to do the forbidden thing; G1 must catch every mutant.

    A gate that has only ever reported clean is indistinguishable from a gate that cannot
    report at all. This repo has been bitten three times by exactly that.
    """
    # Each mutant names the file it mutates AND the guard that must catch it. Before this,
    # every mutant was applied to verify_universe_atoms.py and checked with guard_static;
    # the accessor path had no mutants at all, which is how a 1.55 GiB function lived next
    # to a 384 MiB gate reporting PASS.
    mutants = {
        "whole-file read_text() in prime()":
            (TARGET, guard_static, r"chunk = fh\.read\(8 << 20\)", "chunk = path.read_text()"),
        "unbounded .read() in prime()":
            (TARGET, guard_static, r"chunk = fh\.read\(8 << 20\)", "chunk = fh.read()"),
        "json.load() in prime()":
            (TARGET, guard_static, r"chunk = fh\.read\(8 << 20\)", "chunk = json.load(fh)"),
        # Replaced "combined blob no longer skipped" (seam `or name == _COMBINED_BLOB`).
        # That mutant still reported [CAUGHT] after the V5 re-hydrate, but only because it
        # mutated source text - the file it protected no longer exists in the payload, so it
        # proved nothing about memory. These two are pointed at guards that hold real bytes
        # out of the stream today.
        "extension filter dropped from _scan_roots (105 MB packfile enters the stream)":
            (TARGET, guard_static, r'not name\.endswith\("\.json"\) or ', ""),
        "chunk retained across the read loop (bounded read, unbounded retention)":
            (TARGET, guard_static, r'tail = chunk\[-overlap:\] if overlap > 0 else b""',
             "tail += chunk"),
        # --- accessor mutants (G1b). These are the HG-U21 / HG-U22 shapes. ---
        "recursive glob reintroduced in _iter_base_export (296k file payloads become records)":
            (ACCESSOR, guard_static_accessor, r"svc_dir\.glob\(table_glob\)",
             "svc_dir.rglob(table_glob)"),
        # The replacement is deliberately BALANCED. The first draft of this mutant dropped
        # the closing paren, so it was reported [CAUGHT] as a SyntaxError - a mutant that
        # tests the ast.parse guard rather than the memory guard. Guard (a2) is what
        # catches this one now, and it catches it as what it is: accumulation.
        "_iter_base_export collapsed from generator back to an accumulating list":
            (ACCESSOR, guard_static_accessor,
             r'yield \{"source": source, "row_data": json\.dumps\(row, ensure_ascii=False\)\}',
             'records.append({"source": source, "row_data": json.dumps(row, ensure_ascii=False)})'),
        # The replacement MATERIALISES deliberately. A bare `load_universe_records(...)`
        # is caught by guard (e) but is behaviourally free now that the loader returns a
        # generator - calling it consumes nothing - so it would be a mutant that proves
        # nothing about memory. `list(...)` is the regression this guard actually exists to
        # stop: four S0 builders reading the whole export to answer a boolean.
        "require_resolvable routed back through the full record loader":
            (ACCESSOR, guard_static_accessor, r"_resolve_or_raise\(Path\(task_dir\), universe\)",
             "list(load_universe_records(Path(task_dir), universe)[0])"),
        # These two are the measured failure modes that scoping the walk did NOT fix.
        # Without them the suite would certify a 620-738 MiB accessor as constant-memory,
        # which is precisely the gap that let HG-U22 exist next to a 384 MiB ceiling.
        "whole-file read reintroduced in _iter_table_rows (620 MiB: the str alone)":
            (ACCESSOR, guard_static_accessor, r'fh = open\(path, "r", encoding="utf-8"\)',
             'fh = io.StringIO(path.read_text(encoding="utf-8"))'),
        # Replaces BOTH lines of the prefix drop, not just the slice. Dropping the slice
        # alone left `self.pos = 0` behind, which resets the cursor over a retained buffer:
        # the reader then fails immediately instead of growing, so the mutant proved the
        # code was broken rather than that it was unbounded. Removing the pair keeps the
        # reader CORRECT and makes it append-only, which is the memory defect itself.
        "_JsonCursor window stops sliding (append-only buffer holds the whole file)":
            (ACCESSOR, guard_static_accessor,
             r"self\.buf = self\.buf\[self\.pos:\]\n            self\.pos = 0",
             "pass"),
    }
    print(f"Self-check: {len(mutants)} mutants, each MUST be caught by its guard\n")
    missed = []
    sources = {}
    for label, (target, guard, pattern, replacement) in mutants.items():
        src = sources.setdefault(target, target.read_text(encoding="utf-8"))
        mutated, n = re.subn(pattern, replacement, src, count=1)
        if n != 1:
            missed.append(f"{label}: mutation seam not found in {target.name} "
                          f"(pattern {pattern!r}) - this gate is pointed at code that no "
                          f"longer exists")
            print(f"[STALE] {label} - seam not found in {target.name}")
            continue
        findings = guard(mutated)
        if findings:
            print(f"[CAUGHT] {label}")
            if verbose:
                for f in findings:
                    print(f"           - {f}")
        else:
            missed.append(f"{label}: NOT caught by {guard.__name__} - the guard is blind to "
                          f"this reintroduction of an O(universe) load")
            print(f"[MISSED] {label}")

    # The unmutated sources must be clean, or "caught" above proves nothing.
    for target, guard in ((TARGET, guard_static), (ACCESSOR, guard_static_accessor)):
        baseline = guard(target.read_text(encoding="utf-8"))
        if baseline:
            missed.append(f"baseline: {guard.__name__} reports findings against the UNMUTATED "
                          f"{target.name}, so every 'caught' above is a false positive")
            print(f"[BASELINE DIRTY] {guard.__name__} flags the real {target.name}")
            if verbose:
                for f in baseline:
                    print(f"           - {f}")
        else:
            print(f"[BASELINE CLEAN] {guard.__name__} is silent on the real {target.name}")

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

    print("G1 static - byte scan, verify_universe_atoms.py (no hydration required):")
    g1 = guard_static(TARGET.read_text(encoding="utf-8"))
    findings += g1
    if g1:
        for f in g1:
            print(f"  [FAIL] {f}")
    else:
        print("  [PASS] the export scan is chunked, bounded, extension-filtered, and "
              "retains no chunk")

    print("\nG1b static - record accessor, universe_data_source.py (no hydration required):")
    g1b = guard_static_accessor(ACCESSOR.read_text(encoding="utf-8"))
    findings += g1b
    if g1b:
        for f in g1b:
            print(f"  [FAIL] {f}")
    else:
        print("  [PASS] the record accessor streams, globs one level, reads its "
              "include/exclude contract from the registry, and is not re-materialised")

    universes = export_backed_universes()
    print(f"\nG2 empirical (export-backed universes from the registry: "
          f"{', '.join(universes) or 'none'}):")
    try:
        for u in universes:
            if not is_hydrated(u):
                print(f"  [SKIP] {u}: payload not hydrated ({services_dir(u)}) - gitignored by "
                      f"design; G1/G1b still covered this edit")
                continue
            findings += guard_empirical(u, args.verbose)
            findings += guard_empirical_accessor(u, args.verbose)
    finally:
        _cleanup_scratch()

    print()
    if findings:
        print(f"MEMORY BOUNDS: FAIL - {len(findings)} finding(s)")
        return 1
    print("MEMORY BOUNDS: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
