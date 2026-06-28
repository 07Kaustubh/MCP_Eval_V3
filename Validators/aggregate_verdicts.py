#!/usr/bin/env python3
"""
aggregate_verdicts.py — cross-task QC trend aggregator (v12 F2 unified verdict schema).

Globs `Tasks/*/_aux/Council_Reports/*.md`, extracts trailing JSON verdict blocks
(the v12 F2 unified format), emits per-universe portfolio-level QC trend tables.

Usage:
    python3 Validators/aggregate_verdicts.py
    python3 Validators/aggregate_verdicts.py --universe brookfield
    python3 Validators/aggregate_verdicts.py --since 2026-06-01
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

try:
    from Validators.universes import detect_universe
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from universes import detect_universe


JSON_BLOCK_RE = re.compile(r"```(?:json)?\s*\n(\{.*?\})\s*\n```", re.DOTALL)


def extract_verdict_json(report_text: str) -> dict:
    matches = JSON_BLOCK_RE.findall(report_text)
    for m in reversed(matches):
        try:
            d = json.loads(m)
            if isinstance(d, dict) and "verdict" in d:
                return d
        except json.JSONDecodeError:
            continue
    return {}


def aggregate(universe_filter: str = None) -> dict:
    tasks_dir = ROOT / "Tasks"
    by_universe = defaultdict(lambda: {
        "tasks": 0,
        "verdicts": defaultdict(int),
        "sub_dim_fails": defaultdict(int),
        "perspective_blocks": defaultdict(int),
        "density_band_distribution": defaultdict(int),
        "lever_preservation_misses": 0,
        "bucket_1_risk_pct_avg": [],
    })

    for task_dir in tasks_dir.iterdir():
        if not task_dir.is_dir() or task_dir.name.startswith("_"):
            continue
        try:
            universe = detect_universe(task_dir)
        except Exception:
            universe = "brookfield"
        if universe_filter and universe != universe_filter:
            continue
        by_universe[universe]["tasks"] += 1
        reports_dir = task_dir / "_aux" / "Council_Reports"
        if not reports_dir.is_dir():
            continue
        for report in reports_dir.glob("*.md"):
            verdict_json = extract_verdict_json(report.read_text(encoding="utf-8"))
            if not verdict_json:
                continue
            v = verdict_json.get("verdict", "<unknown>")
            by_universe[universe]["verdicts"][v] += 1
            perspectives = verdict_json.get("perspectives", {})
            for pname, pdata in perspectives.items():
                if isinstance(pdata, dict) and pdata.get("status") == "FAIL":
                    by_universe[universe]["perspective_blocks"][pname] += 1
            scores = verdict_json.get("scores", {})
            for sd, sdata in scores.items():
                if isinstance(sdata, dict) and sdata.get("score", 5) < 5:
                    by_universe[universe]["sub_dim_fails"][sd] += 1
            density = verdict_json.get("density_projection") or {}
            if density.get("band"):
                by_universe[universe]["density_band_distribution"][density["band"]] += 1
            lever = verdict_json.get("lever_preservation") or {}
            if lever.get("missing"):
                by_universe[universe]["lever_preservation_misses"] += 1
            b1 = verdict_json.get("bucket_1_risk_pct")
            if isinstance(b1, (int, float)):
                by_universe[universe]["bucket_1_risk_pct_avg"].append(b1)

    return dict(by_universe)


def render(by_universe: dict) -> str:
    lines = ["# Cross-Task Verdict Aggregation", ""]
    for universe, data in sorted(by_universe.items()):
        lines.append(f"## Universe: {universe}")
        lines.append(f"**Tasks analyzed:** {data['tasks']}")
        lines.append("")
        if data["verdicts"]:
            lines.append("### Verdict distribution")
            for v, c in sorted(data["verdicts"].items(), key=lambda x: -x[1]):
                lines.append(f"- {v}: {c}")
            lines.append("")
        if data["sub_dim_fails"]:
            lines.append("### Top failing sub-dimensions (across tasks)")
            for sd, c in sorted(data["sub_dim_fails"].items(), key=lambda x: -x[1])[:15]:
                lines.append(f"- {sd}: {c} task failures")
            lines.append("")
        if data["perspective_blocks"]:
            lines.append("### Most-blocking council perspectives")
            for p, c in sorted(data["perspective_blocks"].items(), key=lambda x: -x[1])[:15]:
                lines.append(f"- {p}: {c} blocks")
            lines.append("")
        if data["density_band_distribution"]:
            lines.append("### Density-band distribution")
            for b, c in sorted(data["density_band_distribution"].items(), key=lambda x: -x[1]):
                lines.append(f"- {b}: {c}")
            lines.append("")
        if data["lever_preservation_misses"]:
            lines.append(f"### Lever-preservation misses: {data['lever_preservation_misses']}")
            lines.append("")
        b1_list = data["bucket_1_risk_pct_avg"]
        if b1_list:
            avg = sum(b1_list) / len(b1_list)
            lines.append(f"### FINAL Lens 6 Bucket-1-Risk average: {avg:.1f}% across {len(b1_list)} tasks")
            lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--universe", help="Filter to one universe (brookfield | keystone)")
    ap.add_argument("--output", help="Write report to file (default: stdout)")
    args = ap.parse_args()

    by_universe = aggregate(universe_filter=args.universe)
    report = render(by_universe)

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"Aggregated report written to {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
