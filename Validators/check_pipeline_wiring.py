#!/usr/bin/env python3
"""
Usage:
    python Validators/check_pipeline_wiring.py [--task <task_dir>]

Audits the pipeline's own internal wiring: do the paths, scripts, flags and phases that the
docs and runbooks cite actually exist, and does every validator import and run.

Why this exists
---------------
The pipeline is ~34 validators, 16 runbooks and a dozen reference docs that cite each other
by name. Nothing verified those citations. A runbook can tell an operator to run a script
with a flag the script never had, or to read a file that was renamed, and the only way to
find out was to hit it mid-phase. This is the same class of defect as every other one found
in this repo: a claim in prose that nothing checks.

Checks
------
W1  file paths cited in AGENTS.md / Reference/**.md resolve on disk
W2  scripts cited in runbooks exist under Validators/
W3  CLI flags cited for each script exist in that script's argument parser
W4  --phase values cited for validate.py exist in its phase list
W5  every validator imports cleanly (syntax + import-time errors)
W6  cross-validator symbol references resolve (from X import Y)
W7  every validator declares a usage/CLI entry point
W8  validators referenced in AGENTS.md's registry exist, and vice versa

Exit 0 clean, 1 when any check fails.
"""

import argparse
import ast
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VDIR = ROOT / "Validators"

DOC_GLOBS = ["AGENTS.md", "Reference/*.md", "Reference/Sessions/*.md"]

# path-shaped tokens inside backticks
PATH_RE = re.compile(r"`([A-Za-z0-9_][A-Za-z0-9_./*-]*\.(?:py|md|json|txt|sql|sh))`")
SCRIPT_RE = re.compile(r"(?:python3?\s+)?Validators/([A-Za-z0-9_]+\.py)((?:\s+--?[a-z-]+)*)")
FLAG_RE = re.compile(r"--([a-z][a-z0-9-]*)")
PHASE_RE = re.compile(r"--phase\s+\{?([a-z_|\s]+)\}?")


def docs():
    out = []
    for g in DOC_GLOBS:
        out.extend(sorted(ROOT.glob(g)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", default=None)
    args = ap.parse_args()

    fails, warns = [], []

    # ---------- W1 / W2 : cited paths + scripts resolve
    cited_scripts = set()
    for d in docs():
        txt = d.read_text(encoding="utf-8", errors="replace")
        rel = d.relative_to(ROOT)
        for m in PATH_RE.finditer(txt):
            tok = m.group(1)
            if "*" in tok or tok.startswith(("Docs", "Evals", "Tasks_Template")):
                continue  # glob or per-universe pattern
            # "TaskN..TaskM" is range shorthand and the real dirs carry a hex suffix
            # (QC_Tasks/V3_Tasks/Task11_6a2202b8.../Rubrics.json). Resolve the leaf name
            # under the parent glob instead of treating the literal string as a path.
            if ".." in tok:
                parts = tok.split("/")
                leaf = parts[-1]
                stem = "/".join(parts[:-2]) if len(parts) > 2 else ""
                base = ROOT / stem if stem else ROOT
                if base.is_dir() and any((d / leaf).is_file() for d in base.iterdir() if d.is_dir()):
                    continue
            # try a few plausible roots
            cands = [ROOT / tok, ROOT / "Validators" / tok, ROOT / "Reference" / tok]
            if tok.startswith("Tasks/") or "<TASK_DIR>" in tok:
                continue
            if not any(c.exists() for c in cands) and not list(ROOT.glob(f"**/{tok}"))[:1]:
                fails.append(f"[W1] {rel}: cites `{tok}` which does not exist")
        for m in SCRIPT_RE.finditer(txt):
            script, flagblob = m.group(1), m.group(2) or ""
            cited_scripts.add(script)
            if not (VDIR / script).is_file():
                fails.append(f"[W2] {rel}: cites Validators/{script} which does not exist")
                continue
            # ---------- W3 : cited flags exist in the script
            src = (VDIR / script).read_text(encoding="utf-8", errors="replace")
            for f in FLAG_RE.findall(flagblob):
                if f in ("help",):
                    continue
                if f"--{f}" not in src:
                    fails.append(f"[W3] {rel}: `Validators/{script} --{f}` but the script "
                                 f"declares no --{f}")
        # ---------- W4 : validate.py --phase values
        vsrc = (VDIR / "validate.py").read_text(encoding="utf-8", errors="replace")
        known = set(re.findall(r'"(prompt|oe|rubrics|all|injection|submission_gate)"', vsrc))
        for m in re.finditer(r"validate\.py[^\n]*--phase\s+([a-z_]+)", txt):
            ph = m.group(1)
            if ph not in known:
                fails.append(f"[W4] {rel}: cites validate.py --phase {ph}, not a known phase "
                             f"{sorted(known)}")

    # ---------- W5 : every validator imports cleanly
    for p in sorted(VDIR.glob("*.py")):
        try:
            ast.parse(p.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError as e:
            fails.append(f"[W5] {p.name}: SyntaxError line {e.lineno}: {e.msg}")
            continue
        if p.name in ("test_regression_anchors.py",):
            continue
        spec = importlib.util.spec_from_file_location(f"_w5_{p.stem}", p)
        try:
            mod = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = mod
            spec.loader.exec_module(mod)
        except SystemExit:
            pass
        except Exception as e:
            fails.append(f"[W5] {p.name}: import-time {type(e).__name__}: {e}")

    # ---------- W6 : cross-validator symbol references resolve
    for p in sorted(VDIR.glob("*.py")):
        try:
            tree = ast.parse(p.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module:
                target = VDIR / f"{node.module.split('.')[-1]}.py"
                if not target.is_file():
                    continue
                tsrc = target.read_text(encoding="utf-8", errors="replace")
                try:
                    ttree = ast.parse(tsrc)
                except SyntaxError:
                    continue
                defined = {n.name for n in ast.walk(ttree)
                           if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}
                defined |= {t.id for n in ast.walk(ttree) if isinstance(n, ast.Assign)
                            for t in n.targets if isinstance(t, ast.Name)}
                for a in node.names:
                    if a.name != "*" and a.name not in defined:
                        fails.append(f"[W6] {p.name}: imports `{a.name}` from {target.name} "
                                     f"which does not define it")

    # ---------- W7 : CLI entry point
    for p in sorted(VDIR.glob("*.py")):
        src = p.read_text(encoding="utf-8", errors="replace")
        if p.name in ("universes.py", "v4_gates.py"):
            continue  # library modules by design
        if "__main__" not in src:
            warns.append(f"[W7] {p.name}: no __main__ entry point (library, or missing CLI?)")

    # ---------- W8 : AGENTS registry vs disk
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8", errors="replace")
    # registry tree uses ├── for members and └── for the last item in a group
    registered = set(re.findall(r"│\s+[├└]──\s+([a-z0-9_]+\.py)", agents))
    on_disk = {p.name for p in VDIR.glob("*.py")}
    for s in sorted(registered - on_disk):
        fails.append(f"[W8] AGENTS.md registers Validators/{s} which does not exist")
    for s in sorted(on_disk - registered):
        warns.append(f"[W8] Validators/{s} exists but is not in the AGENTS.md registry")

    # ---------- report
    print("=== Pipeline wiring audit ===")
    print(f"{len(list(VDIR.glob('*.py')))} validators · {len(docs())} docs · "
          f"{len(cited_scripts)} scripts cited by docs\n")
    for f in fails:
        print(f"  {f}")
    if warns:
        print()
        for w in warns:
            print(f"  {w}")
    print()
    if fails:
        print(f"[FAIL] {len(fails)} wiring error(s), {len(warns)} warning(s)")
        return 1
    print(f"[OK] no wiring errors. {len(warns)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
