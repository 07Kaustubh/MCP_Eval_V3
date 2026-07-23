#!/usr/bin/env python3
"""
Usage:
    python Validators/parse_trajectories.py <path_to_task_dir>

Reads platform-exported agent trajectories and the per-run verifier-fails
text, computes pass@1 and tool-call density. Removes the manual chore from
REVIEW step 3 and S4.

Looks for trajectories in (first match wins):
    <task_dir>/trajectory-runs/trajectory-run-N (*).json
    <task_dir>/trajectory-runs/Run*.json
    <task_dir>/Agent_Responses/Run*.json

For StarPM V4 dual-model tasks, pass --model {opus,gemini}. Trajectories then
resolve to <task_dir>/Agent_Responses/<Model>/Run*.json and verifier-fails to
<task_dir>/8a_Verifier_Fails_Opus.txt or <task_dir>/8b_Verifier_Fails_Gemini.txt.

Density and difficulty gates:
    - Opus (or single-model V3 tasks): density < 40 -> REBUILD_CANDIDATE_DENSITY;
      pass@1 > 40% -> REBUILD_CANDIDATE_DIFFICULTY. Both trigger REDO.
    - Gemini (StarPM V4): density and pass@1 are INFORMATIONAL only. Recorded in
      the output but never trigger a REBUILD_CANDIDATE verdict. Rationale: Gemini
      batches tool calls differently from Opus (naturally lower avg total), and
      gating on Gemini metrics would REDO tasks that discriminate correctly. See
      commit a342b8c (Gemini pass@1 informational) extended to density.

Trajectory shape (Claude Code SDK export): top-level is a list of events.
Tool calls are 'tool_use' blocks in message.content[] on assistant events.
Names starting with 'mcp__' are platform MCP tools; the rest are Claude
Code internal scaffolding (Task, TaskCreate, TaskUpdate, etc.).

Verifier-fails shape (8_Verifier_Fails.txt): per-run blocks beginning
'Run #N', followed by 'X/Y criteria passed'. A run passes (for pass@1)
iff X == Y on the rubrics line.

Outputs:
    - stdout: per-run table + summary verdict
    - <task_dir>/_aux/Trajectory_Stats.json
"""

import argparse
import json
import re
import sys
from pathlib import Path
from statistics import mean


def find_trajectory_files(task_dir, model=None):
    if model:
        model_subdir = task_dir / "Agent_Responses" / model.capitalize()
        search_dirs = (model_subdir,)
    else:
        search_dirs = (task_dir / "trajectory-runs", task_dir / "Agent_Responses")
    for d in search_dirs:
        if not d.is_dir():
            continue
        files = sorted(d.glob("trajectory-run-*.json")) + sorted(d.glob("Run*.json"))
        seen = {}
        for f in files:
            n = parse_run_number(f.name)
            if n is None or n in seen:
                continue
            seen[n] = f
        if seen:
            return sorted(seen.items())
    return []


def parse_run_number(name):
    m = re.search(r"(?:trajectory-run-|Run)(\d+)", name)
    return int(m.group(1)) if m else None


def load_trajectory(path):
    if not path.is_file() or path.stat().st_size == 0:
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def count_tool_calls(events):
    if not isinstance(events, list):
        return 0, 0
    total = 0
    mcp = 0
    for ev in events:
        if not isinstance(ev, dict):
            continue
        # Gemini flat format: top-level tool_use events with tool_name key
        if ev.get("type") == "tool_use":
            total += 1
            tool_name = ev.get("tool_name", ev.get("name", ""))
            if tool_name.startswith("mcp_") or tool_name.startswith("mcp__"):
                mcp += 1
            continue
        # Opus / Claude Code SDK format: tool_use blocks inside message.content
        msg = ev.get("message")
        if not isinstance(msg, dict):
            continue
        content = msg.get("content")
        if not isinstance(content, list):
            continue
        for block in content:
            if isinstance(block, dict) and block.get("type") == "tool_use":
                total += 1
                if block.get("name", "").startswith("mcp__"):
                    mcp += 1
    return total, mcp


def parse_verifier_fails(path):
    if not path.is_file() or path.stat().st_size == 0:
        return None
    text = path.read_text(encoding="utf-8")
    blocks = re.split(r"(?m)^Run\s*#\s*(\d+)\s*$", text)
    runs = []
    for i in range(1, len(blocks), 2):
        run_n = int(blocks[i])
        body = blocks[i + 1] if i + 1 < len(blocks) else ""
        m = re.search(r"(\d+)\s*/\s*(\d+)\s+criteria\s+passed", body, re.IGNORECASE)
        if not m:
            continue
        passed = int(m.group(1))
        total = int(m.group(2))
        runs.append({
            "run": run_n,
            "passed": passed,
            "total": total,
            "passes_all": passed == total,
        })
    if not runs:
        return None
    passing = sum(1 for r in runs if r["passes_all"])
    n = len(runs)
    return {
        "runs": runs,
        "runs_total": n,
        "runs_passing_all_rubrics": passing,
        "pass_at_1": round(passing / n, 3) if n else 0.0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task_dir")
    ap.add_argument("--model", choices=["opus", "gemini"], default=None,
                    help="StarPM V4 dual-model tasks: 'opus' gates density/difficulty; "
                         "'gemini' records both as informational (never triggers REBUILD).")
    args = ap.parse_args()
    task_dir = Path(args.task_dir).resolve()
    if not task_dir.is_dir():
        print(f"ERROR: {task_dir} not a directory", file=sys.stderr)
        sys.exit(2)

    files = find_trajectory_files(task_dir, model=args.model)
    if not files:
        loc = f"{task_dir}/Agent_Responses/{args.model.capitalize()}/" if args.model else f"{task_dir}/trajectory-runs/ or /Agent_Responses/"
        print(f"ERROR: no trajectory files found in {loc}", file=sys.stderr)
        sys.exit(2)

    per_run = []
    for run_n, fp in files:
        events = load_trajectory(fp)
        if events is None:
            per_run.append({"run": run_n, "file": str(fp.relative_to(task_dir)), "status": "empty_or_invalid"})
            continue
        total, mcp = count_tool_calls(events)
        per_run.append({
            "run": run_n,
            "file": str(fp.relative_to(task_dir)),
            "status": "ok",
            "tool_calls_total": total,
            "tool_calls_mcp_only": mcp,
        })

    valid = [r for r in per_run if r["status"] == "ok"]
    totals = [r["tool_calls_total"] for r in valid]
    mcps = [r["tool_calls_mcp_only"] for r in valid]
    avg_total = round(mean(totals), 1) if totals else 0.0
    avg_mcp = round(mean(mcps), 1) if mcps else 0.0

    if args.model == "opus":
        vf_path = task_dir / "8a_Verifier_Fails_Opus.txt"
    elif args.model == "gemini":
        vf_path = task_dir / "8b_Verifier_Fails_Gemini.txt"
    else:
        vf_path = task_dir / "8_Verifier_Fails.txt"
    vf = parse_verifier_fails(vf_path)

    density_ok = avg_total >= 40
    difficulty_ok = (vf["pass_at_1"] <= 0.40) if vf is not None else None
    # Gemini metrics (StarPM V4) are informational only, parallel to commit a342b8c.
    # Never trigger REBUILD_CANDIDATE on Gemini even when the raw check fails.
    density_gated = (args.model != "gemini")
    difficulty_gated = (args.model != "gemini")
    verdict = "OK"
    if not density_ok and density_gated:
        verdict = "REBUILD_CANDIDATE_DENSITY"
    elif difficulty_ok is False and difficulty_gated:
        verdict = "REBUILD_CANDIDATE_DIFFICULTY"

    out = {
        "task": task_dir.name,
        "model": args.model,
        "gated": {"density": density_gated, "difficulty": difficulty_gated},
        "per_run": per_run,
        "runs_evaluated": len(valid),
        "avg_tool_calls_total": avg_total,
        "avg_tool_calls_mcp_only": avg_mcp,
        "min_tool_calls_total": min(totals) if totals else 0,
        "max_tool_calls_total": max(totals) if totals else 0,
        "density_ok_at_40": density_ok,
        "verifier_fails": vf,
        "difficulty_ok_at_40pct": difficulty_ok,
        "verdict": verdict,
    }

    stats_filename = f"Trajectory_Stats_{args.model.capitalize()}.json" if args.model else "Trajectory_Stats.json"
    out_path = task_dir / "_aux" / stats_filename
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")

    print(f"=== Trajectory stats: {task_dir.name} ===")
    print(f"Runs evaluated: {len(valid)} / {len(per_run)}")
    print(f"{'Run':>5}  {'Total':>6}  {'MCP':>6}  Status")
    for r in per_run:
        if r["status"] == "ok":
            print(f"  {r['run']:>3}  {r['tool_calls_total']:>6}  {r['tool_calls_mcp_only']:>6}  ok")
        else:
            print(f"  {r['run']:>3}  {'--':>6}  {'--':>6}  {r['status']}")
    density_label = 'OK' if density_ok else ('FAIL' if density_gated else 'INFORMATIONAL')
    print(f"Avg total tool calls: {avg_total}  (density {density_label} at 40+)")
    print(f"Avg MCP tool calls:   {avg_mcp}")
    if vf is not None:
        difficulty_label = 'OK' if difficulty_ok else ('FAIL' if difficulty_gated else 'INFORMATIONAL')
        print(f"Verifier-fails:       pass@1 = {vf['pass_at_1']}  ({vf['runs_passing_all_rubrics']}/{vf['runs_total']} runs passed all rubrics)  ({difficulty_label} at <= 40%)")
        for r in vf["runs"]:
            print(f"  Run #{r['run']:<2}  {r['passed']:>3}/{r['total']:<3} criteria passed  {'PASS' if r['passes_all'] else 'FAIL'}")
    else:
        print(f"Verifier-fails:       no verifier-fails file found ({vf_path.name}) - difficulty unknown")
    if args.model == "gemini":
        print(f"Note:                 Gemini density and pass@1 are informational only (per commit a342b8c extended to density).")
    print(f"Verdict:              {verdict}")
    print(f"Written:              {out_path}")

    sys.exit(0 if verdict == "OK" else 1)


if __name__ == "__main__":
    main()
