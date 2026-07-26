#!/usr/bin/env python3
"""
Usage:
    python Validators/parse_trajectories.py <path_to_task_dir>

Reads platform-exported agent trajectories and the per-run verifier-fails
text, computes pass@1 and tool-call density. Removes the manual chore from
REVIEW step 3 and S4.

Trajectory discovery is driven by the universe's framework profile
(get_framework_profile(universe)["trajectory_layout"]):

  flat (v3 / v3.1 / v2.1) - single-model runs, first match wins:
    <task_dir>/trajectory-runs/trajectory-run-N (*).json
    <task_dir>/trajectory-runs/Run*.json
    <task_dir>/Agent_Responses/Run*.json

  per_model (v4 / starpm) - dual-model runs (Opus + Gemini):
    <task_dir>/Agent_Responses/Opus/RunN_Trajectory.json    -> tagged 'opus'
    <task_dir>/Agent_Responses/Gemini/RunN_Trajectory.json  -> tagged 'gemini'
  plus the flat V4 QC export layout, tagged 'unknown':
    <task_dir>/Agent_Responses/trajectory-run-N.json
    <task_dir>/trajectory-runs/trajectory-run-N.json

Trajectory shape (Claude Code SDK export): top-level is a list of events.
Tool calls are 'tool_use' blocks in message.content[] on assistant events.
Names starting with 'mcp__' are platform MCP tools; the rest are Claude
Code internal scaffolding (Task, TaskCreate, TaskUpdate, etc.).

Verifier-fails shape (8_Verifier_Fails.txt, or per-model 8a/8b for v4):
per-run blocks beginning 'Run #N', followed by 'X/Y criteria passed'. A run
passes (for pass@1) iff X == Y on the rubrics line.

Outputs:
    - stdout: per-run table + summary verdict (per-model breakout for v4)
    - <task_dir>/_aux/Trajectory_Stats.json
"""

import argparse
import json
import re
import sys
from pathlib import Path
from statistics import mean

try:
    from Validators.universes import (
        detect_universe,
        get_framework_profile,
        get_universe_constants,
    )
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from universes import (
        detect_universe,
        get_framework_profile,
        get_universe_constants,
    )

MODEL_SUBDIRS = ("Opus", "Gemini")


def find_trajectory_files(task_dir):
    for d in (task_dir / "trajectory-runs", task_dir / "Agent_Responses"):
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


def find_trajectory_files_per_model(task_dir):
    """Discover per-model trajectories for V4 (dual-model) tasks.

    Returns a list of (run_number, path, model) triples. Files under
    Agent_Responses/Opus and Agent_Responses/Gemini are tagged with their
    model. Flat files (V4 QC exports: trajectory-run-N.json, or RunN files
    directly under Agent_Responses/ or trajectory-runs/) are tagged 'unknown'.
    """
    triples = []
    seen = set()  # (model, run_number)
    ar = task_dir / "Agent_Responses"
    for sub in MODEL_SUBDIRS:
        d = ar / sub
        if not d.is_dir():
            continue
        model = sub.lower()
        files = sorted(d.glob("trajectory-run-*.json")) + sorted(d.glob("Run*.json"))
        for f in files:
            n = parse_run_number(f.name)
            if n is None or (model, n) in seen:
                continue
            seen.add((model, n))
            triples.append((n, f, model))
    for d in (task_dir / "trajectory-runs", ar):
        if not d.is_dir():
            continue
        files = sorted(d.glob("trajectory-run-*.json")) + sorted(d.glob("Run*.json"))
        for f in files:
            n = parse_run_number(f.name)
            if n is None or ("unknown", n) in seen:
                continue
            seen.add(("unknown", n))
            triples.append((n, f, "unknown"))
    triples.sort(key=lambda t: (t[2], t[0]))
    return triples


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
        # Gemini flat format (v4 / starpm dual-model exports): a tool call is a
        # top-level event with type == "tool_use" (keys: tool_name, parameters,
        # tool_id, type). Such events carry no nested `message`, so this branch
        # is mutually exclusive with the Claude-Code branch below and cannot
        # double-count. v3-family / Opus trajectories never emit a top-level
        # `tool_use` event (their event types are system/assistant/user/result),
        # so their counts are unchanged by this branch.
        if ev.get("type") == "tool_use":
            total += 1
            if ev.get("tool_name", "").startswith("mcp_"):
                mcp += 1
            continue
        # Claude-Code / Opus format: tool_use blocks nested in message.content[].
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


def resolve_universe(task_dir):
    """Best-effort universe name; tolerant of read-only task dirs.

    detect_universe writes _aux/Universe.txt on a cache miss, which raises on a
    read-only reference dir (e.g. QC_Tasks). Fall back to a cached marker if
    present, else brookfield (the flat-layout default).
    """
    try:
        return detect_universe(task_dir)
    except OSError:
        marker = task_dir / "_aux" / "Universe.txt"
        try:
            if marker.is_file():
                cached = marker.read_text(encoding="utf-8").strip().lower()
                if cached:
                    return cached
        except OSError:
            pass
        return "brookfield"


def resolve_layout(task_dir):
    """Return (universe, trajectory_layout) for the task.

    Primary driver is the universe's framework profile. A structural override
    forces per_model when Opus/Gemini subfolders exist, so V4 tasks are handled
    correctly even when the universe could not be detected (read-only dirs).
    """
    universe = resolve_universe(task_dir)
    layout = get_framework_profile(universe).get("trajectory_layout", "flat")
    ar = task_dir / "Agent_Responses"
    if (ar / "Opus").is_dir() or (ar / "Gemini").is_dir():
        layout = "per_model"
    return universe, layout


def verifier_files_by_model(task_dir, profile):
    """Map model -> verifier-fails path from the framework profile's list."""
    result = {}
    for fname in profile.get("verifier_files", []):
        low = fname.lower()
        if "opus" in low:
            result["opus"] = task_dir / fname
        elif "gemini" in low:
            result["gemini"] = task_dir / fname
        else:
            result.setdefault("single", task_dir / fname)
    return result


def write_stats(out_path, out):
    """Write Trajectory_Stats.json; tolerate read-only dirs (QC references)."""
    try:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
        return True
    except OSError:
        return False


def build_per_run(discovered, task_dir):
    per_run = []
    for run_n, fp, model in discovered:
        events = load_trajectory(fp)
        if events is None:
            entry = {"run": run_n, "file": str(fp.relative_to(task_dir)), "status": "empty_or_invalid"}
            if model is not None:
                entry["model"] = model
            per_run.append(entry)
            continue
        total, mcp = count_tool_calls(events)
        entry = {
            "run": run_n,
            "file": str(fp.relative_to(task_dir)),
            "status": "ok",
            "tool_calls_total": total,
            "tool_calls_mcp_only": mcp,
        }
        if model is not None:
            entry["model"] = model
        per_run.append(entry)
    return per_run


def run_per_model(task_dir, universe, per_run, valid, totals, mcps, avg_total, avg_mcp):
    profile = get_framework_profile(universe)
    floor = profile.get("density_floor_avg_tool_calls", 40)
    vfiles = verifier_files_by_model(task_dir, profile)

    models = []
    for r in per_run:
        m = r.get("model")
        if m and m not in models:
            models.append(m)
    models.sort()

    by_model = {}
    agg_pass = 0
    agg_runs = 0
    for m in models:
        m_ok = [r for r in valid if r.get("model") == m]
        m_totals = [r["tool_calls_total"] for r in m_ok]
        m_mcps = [r["tool_calls_mcp_only"] for r in m_ok]
        vpath = vfiles.get(m) or vfiles.get("single")
        vf_m = parse_verifier_fails(vpath) if vpath else None
        if vf_m:
            agg_pass += vf_m["runs_passing_all_rubrics"]
            agg_runs += vf_m["runs_total"]
        by_model[m] = {
            "runs_evaluated": len(m_ok),
            "avg_tool_calls_total": round(mean(m_totals), 1) if m_totals else 0.0,
            "avg_tool_calls_mcp_only": round(mean(m_mcps), 1) if m_mcps else 0.0,
            "min_tool_calls_total": min(m_totals) if m_totals else 0,
            "max_tool_calls_total": max(m_totals) if m_totals else 0,
            "verifier_fails": vf_m,
            "pass_at_1": vf_m["pass_at_1"] if vf_m else None,
        }

    overall_pass_at_1 = round(agg_pass / agg_runs, 3) if agg_runs else None
    density_ok = avg_total >= floor
    difficulty_ok = (overall_pass_at_1 <= 0.40) if overall_pass_at_1 is not None else None
    verdict = "OK"
    if not density_ok:
        verdict = "REBUILD_CANDIDATE_DENSITY"
    elif difficulty_ok is False:
        verdict = "REBUILD_CANDIDATE_DIFFICULTY"

    density_key = f"density_ok_at_{floor}"
    out = {
        "task": task_dir.name,
        "framework_version": get_universe_constants(universe).get("framework_version", "v3"),
        "trajectory_layout": "per_model",
        "per_run": per_run,
        "runs_evaluated": len(valid),
        "avg_tool_calls_total": avg_total,
        "avg_tool_calls_mcp_only": avg_mcp,
        "min_tool_calls_total": min(totals) if totals else 0,
        "max_tool_calls_total": max(totals) if totals else 0,
        density_key: density_ok,
        "by_model": by_model,
        "overall_pass_at_1": overall_pass_at_1,
        "difficulty_ok_at_40pct": difficulty_ok,
        "verdict": verdict,
    }

    out_path = task_dir / "_aux" / "Trajectory_Stats.json"
    wrote = write_stats(out_path, out)

    print(f"=== Trajectory stats (per-model): {task_dir.name} ===")
    print(f"Runs evaluated: {len(valid)} / {len(per_run)}")
    print(f"{'Run':>5}  {'Model':>7}  {'Total':>6}  {'MCP':>6}  Status")
    for r in per_run:
        model = r.get("model", "-")
        if r["status"] == "ok":
            print(f"  {r['run']:>3}  {model:>7}  {r['tool_calls_total']:>6}  {r['tool_calls_mcp_only']:>6}  ok")
        else:
            print(f"  {r['run']:>3}  {model:>7}  {'--':>6}  {'--':>6}  {r['status']}")
    print(f"Avg total tool calls: {avg_total}  (density {'OK' if density_ok else 'FAIL'} at {floor}+)")
    print(f"Avg MCP tool calls:   {avg_mcp}")
    for m in models:
        b = by_model[m]
        p1 = b["pass_at_1"]
        p1s = f"pass@1 = {p1}" if p1 is not None else "pass@1 = n/a"
        print(f"  [{m}]  runs={b['runs_evaluated']}  avg_total={b['avg_tool_calls_total']}  avg_mcp={b['avg_tool_calls_mcp_only']}  {p1s}")
    if overall_pass_at_1 is not None:
        print(f"Overall pass@1:       {overall_pass_at_1}  ({'OK' if difficulty_ok else 'FAIL'} at <= 40%)")
    else:
        print(f"Overall pass@1:       n/a - no per-model verifier fails")
    print(f"Verdict:              {verdict}")
    if wrote:
        print(f"Written:              {out_path}")
    else:
        print(f"Written:              (skipped - {out_path.parent} not writable)")

    sys.exit(0 if verdict == "OK" else 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task_dir")
    args = ap.parse_args()
    task_dir = Path(args.task_dir).resolve()
    if not task_dir.is_dir():
        print(f"ERROR: {task_dir} not a directory", file=sys.stderr)
        sys.exit(2)

    universe, layout = resolve_layout(task_dir)

    if layout == "per_model":
        discovered = find_trajectory_files_per_model(task_dir)
    else:
        discovered = [(n, fp, None) for (n, fp) in find_trajectory_files(task_dir)]

    if not discovered:
        print(f"ERROR: no trajectory files found in {task_dir}/trajectory-runs/ or /Agent_Responses/", file=sys.stderr)
        sys.exit(2)

    per_run = build_per_run(discovered, task_dir)

    valid = [r for r in per_run if r["status"] == "ok"]
    totals = [r["tool_calls_total"] for r in valid]
    mcps = [r["tool_calls_mcp_only"] for r in valid]
    avg_total = round(mean(totals), 1) if totals else 0.0
    avg_mcp = round(mean(mcps), 1) if mcps else 0.0

    if layout == "per_model":
        run_per_model(task_dir, universe, per_run, valid, totals, mcps, avg_total, avg_mcp)
        return

    # ---- flat path (v3 / v3.1 / v2.1): behavior byte-identical to the original ----
    vf = parse_verifier_fails(task_dir / "8_Verifier_Fails.txt")

    density_ok = avg_total >= 40
    difficulty_ok = (vf["pass_at_1"] <= 0.40) if vf is not None else None
    verdict = "OK"
    if not density_ok:
        verdict = "REBUILD_CANDIDATE_DENSITY"
    elif difficulty_ok is False:
        verdict = "REBUILD_CANDIDATE_DIFFICULTY"

    out = {
        "task": task_dir.name,
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

    out_path = task_dir / "_aux" / "Trajectory_Stats.json"
    wrote = write_stats(out_path, out)

    print(f"=== Trajectory stats: {task_dir.name} ===")
    print(f"Runs evaluated: {len(valid)} / {len(per_run)}")
    print(f"{'Run':>5}  {'Total':>6}  {'MCP':>6}  Status")
    for r in per_run:
        if r["status"] == "ok":
            print(f"  {r['run']:>3}  {r['tool_calls_total']:>6}  {r['tool_calls_mcp_only']:>6}  ok")
        else:
            print(f"  {r['run']:>3}  {'--':>6}  {'--':>6}  {r['status']}")
    print(f"Avg total tool calls: {avg_total}  (density {'OK' if density_ok else 'FAIL'} at 40+)")
    print(f"Avg MCP tool calls:   {avg_mcp}")
    if vf is not None:
        print(f"Verifier-fails:       pass@1 = {vf['pass_at_1']}  ({vf['runs_passing_all_rubrics']}/{vf['runs_total']} runs passed all rubrics)  ({'OK' if difficulty_ok else 'FAIL'} at <= 40%)")
        for r in vf["runs"]:
            print(f"  Run #{r['run']:<2}  {r['passed']:>3}/{r['total']:<3} criteria passed  {'PASS' if r['passes_all'] else 'FAIL'}")
    else:
        print(f"Verifier-fails:       no 8_Verifier_Fails.txt - difficulty unknown")
    print(f"Verdict:              {verdict}")
    if wrote:
        print(f"Written:              {out_path}")
    else:
        print(f"Written:              (skipped - {out_path.parent} not writable)")

    sys.exit(0 if verdict == "OK" else 1)


if __name__ == "__main__":
    main()
