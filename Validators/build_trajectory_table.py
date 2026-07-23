#!/usr/bin/env python3
"""
Usage:
    python Validators/build_trajectory_table.py <task_dir> --run <N> [--model {opus,gemini}]
    python Validators/build_trajectory_table.py <task_dir> --run <N> --model opus --validate <existing.json>

Two modes:

1. Scaffold mode (default): emit a stub JSON with title, category, decision (from
   verifier), and a trajectory_hint block. The trajectory_hint gives the agent
   the raw evidence needed to write an OWN-analysis justification without
   re-walking the trajectory manually. Agent fills justification, removes
   trajectory_hint, then runs --validate to enforce style rules.

2. Validate mode: check an existing pass/fail JSON file for em-dashes,
   cross-references (Rn, cascade from, same as), and null justifications.
   Exit 0 clean, non-zero on any violation.

The scaffold source:
- title, category :: 7_Rubrics.json (canonical rubric list)
- decision        :: 8[a/b]_Verifier_Fails_*.txt (parsed per-run Pass/Fail row)
- trajectory_hint :: Agent_Responses/[<Model>/]Run<N>_Trajectory.json
                     (tool call item numbers, key params, content excerpts
                      matched from the rubric's evidence field)

Justification stays authored by the agent. This preserves 'our own analysis'
by construction. Scaffold only removes the tedious lookup work.
"""

import argparse
import json
import re
import sys
from pathlib import Path


FORBIDDEN_DASH = re.compile(r"[\u2014\u2013]")
CROSS_REF = re.compile(
    r"\b(?:cascade\s+from|same\s+as|see\s+rubric|per\s+rubric|as\s+in|as\s+with)\s+R?\d+",
    re.IGNORECASE,
)


def norm(s: str) -> str:
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return re.sub(r"\s+", " ", s.strip().lower())


def load_rubrics(task_dir: Path):
    return json.loads((task_dir / "7_Rubrics.json").read_text(encoding="utf-8"))


def resolve_paths(task_dir: Path, model, run_n: int):
    if model == "opus":
        vf = task_dir / "8a_Verifier_Fails_Opus.txt"
        traj = task_dir / "Agent_Responses" / "Opus" / f"Run{run_n}_Trajectory.json"
    elif model == "gemini":
        vf = task_dir / "8b_Verifier_Fails_Gemini.txt"
        traj = task_dir / "Agent_Responses" / "Gemini" / f"Run{run_n}_Trajectory.json"
    else:
        vf = task_dir / "8_Verifier_Fails.txt"
        traj = task_dir / "Agent_Responses" / f"Run{run_n}_Trajectory.json"
    return vf, traj


def load_verifier_decisions(vf_path: Path, run_n: int):
    if not vf_path.is_file():
        return {}
    text = vf_path.read_text(encoding="utf-8")
    blocks = re.split(r"(?m)^Run\s*#\s*(\d+)\s*$", text)
    for i in range(1, len(blocks), 2):
        n = int(blocks[i])
        body = blocks[i + 1] if i + 1 < len(blocks) else ""
        if n != run_n:
            continue
        rows = re.findall(r"^(.+?)\t(Pass|Fail)\t(.*?)$", body, re.MULTILINE)
        return {norm(r): dec for r, dec, _ in rows}
    return {}


def extract_tool_calls(events):
    calls = []
    for item_num, ev in enumerate(events, start=1):
        if not isinstance(ev, dict):
            continue
        if ev.get("type") == "tool_use":
            calls.append(
                {
                    "item": item_num,
                    "name": ev.get("tool_name") or ev.get("name") or "",
                    "input": ev.get("input") or ev.get("parameters") or {},
                }
            )
            continue
        msg = ev.get("message") or {}
        content = msg.get("content") if isinstance(msg, dict) else None
        if not isinstance(content, list):
            continue
        for block in content:
            if isinstance(block, dict) and block.get("type") == "tool_use":
                calls.append(
                    {
                        "item": item_num,
                        "name": block.get("name") or "",
                        "input": block.get("input") or {},
                    }
                )
    return calls


TOOL_NAME_PAT = re.compile(
    r"\b(?:a|the)\s+([a-z_][a-z0-9_]*(?:_[a-z0-9_]+)*)\s+call",
    re.IGNORECASE,
)
FIELD_PAT = re.compile(
    r"(?:Check\s+the\s+|the\s+)([a-zA-Z_][\w.]*)\s+parameter",
)
TARGET_ID_PAT = re.compile(
    r"targeting\s+(?:id\s+)?([\w.\-@:]+)",
    re.IGNORECASE,
)
TO_EMAIL_PAT = re.compile(
    r"to\s+containing\s+([\w.@\-]+)",
    re.IGNORECASE,
)
FOR_ATOM_PAT = re.compile(
    r"for\s+(?:the\s+)?(.+?)(?=\.\s*(?:[A-Z]|A\s+|The\s+)|\Z)",
    re.IGNORECASE | re.DOTALL,
)


def parse_evidence(evidence: str):
    hint = {}
    m = TOOL_NAME_PAT.search(evidence)
    if m:
        hint["tool_name"] = m.group(1)
    m = FIELD_PAT.search(evidence)
    if m:
        hint["field"] = m.group(1)
    m = TARGET_ID_PAT.search(evidence)
    if m:
        hint["target_id"] = m.group(1).rstrip(".,)")
    m = TO_EMAIL_PAT.search(evidence)
    if m and "target_id" not in hint:
        hint["target_id"] = m.group(1)
    m = FOR_ATOM_PAT.search(evidence)
    if m:
        atom = m.group(1).strip().rstrip(".")
        if len(atom) < 300:
            hint["atom"] = atom
    return hint


def match_tool_call(calls, hint):
    if not hint.get("tool_name"):
        return None
    tool_name = hint["tool_name"].lower()
    target_id = (hint.get("target_id") or "").lower()
    candidates = []
    for c in calls:
        cname = c["name"].lower()
        if tool_name not in cname:
            continue
        if not target_id:
            candidates.append(c)
            continue
        blob = json.dumps(c["input"], default=str).lower()
        if target_id in blob:
            candidates.append(c)
    return candidates[0] if candidates else None


def content_excerpt(call, field, atom, max_len=300):
    if not call or not field:
        return None
    inp = call["input"]
    keys = field.split(".")
    val = inp
    for k in keys:
        if isinstance(val, dict):
            val = val.get(k)
        else:
            val = None
            break
    if val is None:
        for k in ("body", "message", "description", "text", "fields"):
            if isinstance(inp.get(k), dict):
                nested = inp[k]
                for kk in keys:
                    if isinstance(nested, dict) and kk in nested:
                        val = nested[kk]
                        break
    if val is None:
        return None
    text = str(val)
    if atom:
        low = text.lower()
        keywords = [w for w in re.findall(r"[a-z0-9$]{4,}", atom.lower()) if w not in {"similar", "phrasing", "exact", "approximately"}]
        if keywords:
            hits = sum(1 for kw in keywords if kw in low)
            if hits >= max(1, len(keywords) // 2):
                first = next((kw for kw in keywords if kw in low), None)
                if first:
                    pos = low.find(first)
                    start = max(0, pos - 60)
                    end = min(len(text), pos + 200)
                    return {"contains_atom_guess": True, "excerpt": text[start:end].strip(), "keywords_hit": f"{hits}/{len(keywords)}"}
    return {"contains_atom_guess": False, "excerpt": text[:max_len].strip()}


def build_scaffold_entry(rubric, decision, calls):
    hint = parse_evidence(rubric.get("evidence", ""))
    matched_call = match_tool_call(calls, hint)
    trajectory_hint = {"parsed_from_evidence": hint}
    if matched_call:
        trajectory_hint["matched_tool_call"] = {
            "item": matched_call["item"],
            "name": matched_call["name"],
            "input_keys": sorted(matched_call["input"].keys())[:12],
        }
        excerpt = content_excerpt(matched_call, hint.get("field"), hint.get("atom"))
        if excerpt:
            trajectory_hint["content_excerpt"] = excerpt
    else:
        trajectory_hint["matched_tool_call"] = None
    return {
        "title": rubric["title"],
        "category": rubric.get("category", "outcome"),
        "decision": decision or "Unknown",
        "justification": None,
        "_trajectory_hint": trajectory_hint,
    }


def cmd_scaffold(args, task_dir: Path):
    vf_path, traj_path = resolve_paths(task_dir, args.model, args.run)
    rubrics = load_rubrics(task_dir)
    decisions = load_verifier_decisions(vf_path, args.run)
    if not traj_path.is_file():
        print(f"ERROR: trajectory not found: {traj_path}", file=sys.stderr)
        sys.exit(2)
    events = json.loads(traj_path.read_text(encoding="utf-8"))
    calls = extract_tool_calls(events)

    entries = []
    matched_verifier = 0
    for r in rubrics:
        dec = decisions.get(norm(r["title"]))
        if dec:
            matched_verifier += 1
        entries.append(build_scaffold_entry(r, dec, calls))

    out_name = (
        f"Trajectory_Run{args.run}_{args.model.capitalize()}_scaffold.json"
        if args.model
        else f"Trajectory_Run{args.run}_Table_scaffold.json"
    )
    out_path = task_dir / "_aux" / out_name
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Rubrics scaffolded: {len(entries)}")
    print(f"Decisions matched from verifier: {matched_verifier}/{len(entries)}")
    print(f"Tool calls extracted from trajectory: {len(calls)}")
    print(f"Written: {out_path}")
    print()
    print("Next step: for each rubric, read the _trajectory_hint block and author")
    print("a standalone justification (no em-dashes, no rubric-number cross-refs).")
    print("Remove _trajectory_hint before emit. Run --validate on the final file.")


def cmd_validate(args, task_dir: Path):
    p = Path(args.validate)
    if not p.is_absolute():
        p = task_dir / p
    if not p.is_file():
        print(f"ERROR: file not found: {p}", file=sys.stderr)
        sys.exit(2)
    data = json.loads(p.read_text(encoding="utf-8"))
    entries = data if isinstance(data, list) else data.get("rubrics") or []
    problems = []
    for i, e in enumerate(entries):
        title = e.get("title", f"<rubric {i+1}>")
        just = e.get("justification")
        if just is None or (isinstance(just, str) and not just.strip()):
            problems.append((i + 1, title, "justification is null or empty"))
            continue
        if FORBIDDEN_DASH.search(just):
            problems.append((i + 1, title, "justification contains em-dash or en-dash"))
        m = CROSS_REF.search(just)
        if m:
            problems.append((i + 1, title, f"justification contains cross-reference: {m.group(0)!r}"))
        if "_trajectory_hint" in e:
            problems.append((i + 1, title, "_trajectory_hint block was not removed before final emit"))
        if e.get("decision") not in ("Pass", "Fail"):
            problems.append((i + 1, title, f"decision must be 'Pass' or 'Fail', got {e.get('decision')!r}"))

    if not problems:
        print(f"[OK] {p.name}: {len(entries)} entries clean.")
        sys.exit(0)
    print(f"[FAIL] {p.name}: {len(problems)} problem(s)")
    for idx, title, msg in problems:
        print(f"  rubric {idx}: {msg}")
        print(f"    title: {title[:80]}")
    sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task_dir")
    ap.add_argument("--run", type=int, default=1, help="Run number (default 1).")
    ap.add_argument("--model", choices=["opus", "gemini"], default=None,
                    help="StarPM V4 dual-model tasks: pick per-model verifier / trajectory paths.")
    ap.add_argument("--validate", metavar="PATH",
                    help="Validate an existing final JSON file for em-dashes, cross-references, "
                         "null justifications, and residual _trajectory_hint blocks. "
                         "Exit non-zero on any violation.")
    args = ap.parse_args()

    task_dir = Path(args.task_dir).resolve()
    if not task_dir.is_dir():
        print(f"ERROR: {task_dir} not a directory", file=sys.stderr)
        sys.exit(2)

    if args.validate:
        cmd_validate(args, task_dir)
    else:
        cmd_scaffold(args, task_dir)


if __name__ == "__main__":
    main()
