#!/usr/bin/env python3
"""Zero-regression gate: anchors + frozen report hashes for 7 snapshot tasks.

Baseline captured 2026-07-21 (wave 0) before StarPM V4 integration:
  - test_regression_anchors.py must pass with 0 failures
  - validate.py reports for 7 tasks (3 brookfield, 2 keystone, 2 moveops)
    must hash identically to Validators/regression_baseline/report_hashes.txt
  - validate.py stdout verdict lines must match frozen validate_outputs/*.out
Exit 0 = PASS. Non-zero = regression; offending item printed.
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = Path(__file__).resolve().parent / "regression_baseline"
SNAPSHOT_TASKS = [
    "10_6a2d9411aa26e656b0eff46b",
    "11_6a2d0b401b5f42afec452859",
    "12_6a2e62a409a9532f5347cbb7",
    "33_6a4160e9c4abf61d104018e2",
    "35_6a4421ec8169e23828bb442d",
    "34_6a42ec7493b48d5ada4571bd",
    "36_6a44224ed5d3b47d6d727cf5",
]
PHASES = ["prompt", "oe", "rubrics"]


def sha256(path: Path) -> str:
    """Hash a report OS-neutrally.

    The baseline was captured on macOS: LF endings, POSIX separators in the paths the
    reports quote. On Windows the same validator emits CRLF and backslash-separated
    paths, so a raw byte hash reports drift for content that is otherwise identical.
    Normalise both before hashing. This affects the comparison only, never the file.
    """
    text = path.read_bytes().decode("utf-8")
    text = text.replace("\r\n", "\n").replace("\\", "/")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_baseline_hashes() -> dict:
    out = {}
    for line in (BASE / "report_hashes.txt").read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        digest, path = line.split(None, 1)
        p = Path(path)
        out[(p.parent.name, p.stem)] = digest
    return out


def main() -> int:
    failures = []

    # 1) anchors
    proc = subprocess.run(
        [sys.executable, str(ROOT / "Validators" / "test_regression_anchors.py")],
        capture_output=True, text=True, cwd=ROOT,
    )
    m = re.search(r"Regression anchors: (\d+) passed, (\d+) failed out of (\d+)",
                  proc.stdout + proc.stderr)
    if not m:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        print("REGRESSION GATE: FAIL — could not parse anchor summary")
        return 2
    passed, failed, total = (int(x) for x in m.groups())
    if failed != 0 or passed != total:
        for line in (proc.stdout + proc.stderr).splitlines():
            if "[FAIL]" in line:
                print(line)
        failures.append(f"anchors {passed}/{total} ({failed} failed)")

    # Anchor COUNT is not anchor QUALITY. The dead-gate self-check neuters the validator's
    # ability to emit any finding and asserts every non-allowlisted anchor then fails. Without
    # it an anchor can sit in the suite asserting nothing, which is how two vacuous KeyStone
    # anchors survived for several versions. Standing gate per AGENTS.md rule 18.
    dg = subprocess.run(
        [sys.executable, str(ROOT / "Validators" / "test_regression_anchors.py"), "--dead-gate"],
        capture_output=True, text=True, cwd=ROOT,
    )
    if dg.returncode != 0:
        for line in (dg.stdout + dg.stderr).splitlines():
            if "[LEAK]" in line or "[FAIL]" in line:
                print(line)
        failures.append("dead-gate self-check: anchors pass against a validator that emits nothing")

    # The universe atom scan must stay constant-memory. An earlier fix for the HarmonyGames
    # phantom-atom bug was OOM-KILLED because it materialised the multi-GB base export, and
    # nothing in Validators/ measured memory, so the regression could only ever announce
    # itself as an OOM on an operator's machine. test_memory_bounds asserts a 384 MiB peak-RSS
    # ceiling (measured: 160 MiB streaming vs 673 MiB for the whole-file load it replaced) and
    # SKIPs cleanly when the gitignored payload is not hydrated. Standing gate per AGENTS.md
    # rule 18. --self-check is run too, on the same principle as --dead-gate above: a guard
    # that has only ever reported clean is indistinguishable from one that cannot report.
    for label, extra in (("memory bounds", []), ("memory-bounds self-check", ["--self-check"])):
        mb = subprocess.run(
            [sys.executable, str(ROOT / "Validators" / "test_memory_bounds.py")] + extra,
            capture_output=True, text=True, cwd=ROOT,
        )
        if mb.returncode != 0:
            for line in (mb.stdout + mb.stderr).splitlines():
                if "[FAIL]" in line or "[MISSED]" in line or "[STALE]" in line:
                    print(line)
            failures.append(f"{label}: the universe scan is no longer provably constant-memory")

    # 2) frozen report hashes
    baseline = load_baseline_hashes()
    identical = 0
    for task in SNAPSHOT_TASKS:
        task_dir = ROOT / "Tasks" / task
        if not task_dir.is_dir():
            failures.append(f"snapshot task missing: Tasks/{task}")
            continue
        subprocess.run(
            [sys.executable, str(ROOT / "Validators" / "validate.py"),
             "--phase", "all", "--task", str(task_dir)],
            capture_output=True, text=True, cwd=ROOT,
        )
        for phase in PHASES:
            live = task_dir / "_aux" / "Validator_Reports" / f"{phase}.md"
            key = (task, phase)
            if key not in baseline:
                failures.append(f"no baseline hash for {task}/{phase}")
                continue
            if not live.is_file():
                failures.append(f"missing live report {task}/{phase}.md")
                continue
            if sha256(live) == baseline[key]:
                identical += 1
            else:
                failures.append(f"report drift: {task}/{phase}.md")

    # 3) verdict lines
    verdict_ok = 0
    verdict_re = re.compile(r"^\[(PASS|FAIL)\] (prompt|oe|rubrics):.*?(?= ->)", re.M)
    for task in SNAPSHOT_TASKS:
        frozen_file = BASE / "validate_outputs" / f"{task}.out"
        if not frozen_file.is_file():
            failures.append(f"missing frozen stdout for {task}")
            continue
        proc = subprocess.run(
            [sys.executable, str(ROOT / "Validators" / "validate.py"),
             "--phase", "all", "--task", str(ROOT / "Tasks" / task)],
            capture_output=True, text=True, cwd=ROOT,
        )
        frozen = verdict_re.findall(frozen_file.read_text())
        live = verdict_re.findall(proc.stdout)
        # findall with the lookahead returns tuples; compare raw matched prefixes instead
        frozen_lines = [l.split(" -> ")[0] for l in frozen_file.read_text().splitlines() if l.startswith("[")]
        live_lines = [l.split(" -> ")[0] for l in proc.stdout.splitlines() if l.startswith("[")]
        if frozen_lines == live_lines:
            verdict_ok += 1
        else:
            failures.append(f"verdict drift: {task}")

    n_reports = len(SNAPSHOT_TASKS) * len(PHASES)
    if failures:
        for f in failures:
            print(f"[REGRESSION] {f}")
        print(f"REGRESSION GATE: FAIL — anchors {passed}/{total} ({failed} failed) "
              f"· reports {identical}/{n_reports} identical · verdicts {verdict_ok}/{len(SNAPSHOT_TASKS)} unchanged")
        return 1
    print(f"REGRESSION GATE: PASS — anchors {passed}/{total} (0 failed) "
          f"· reports {identical}/{n_reports} identical · verdicts {verdict_ok}/{len(SNAPSHOT_TASKS)} unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
