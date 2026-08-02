#!/usr/bin/env python3
"""
Usage:
    python Validators/universe_data_source.py <task_dir>        # describe the resolved source
    from universe_data_source import load_universe_records      # library use

Single accessor for "give me this task's universe records", dispatching on the
universe's `universe_data_contract` capability flag.

Why this exists
---------------
Two contracts are in play, and until now only one was implemented.

`per_task_json` (brookfield / keystone / moveops / starpm)
    `3_UniverseDataForThisTask.json` IS the data: a flat array of records, each
    carrying a `source` field naming its service.table. This is what
    `split_universe.py` has always assumed.

`base_export_plus_changelog` (harmonygames)
    `3_UniverseDataForThisTask.json` is a ~721-byte POINTER: a one-element array
    describing where the data lives, with no records in it at all. Truth is the
    base universe export under `<base_path>/Services_Data/`, optionally overlaid
    by the task's `4_Changelog.json`.

The distinction is not cosmetic. Feeding a pointer to the `per_task_json` reader
produces one record with no `source` key, which the old splitter counted as a
"record with no source field" warning and then wrote an empty split. Every
downstream builder (index, fact ledger, graph report, feasible surface) then ran
against nothing and reported success, because none of them distinguishes "no
data" from "no matching data".

A survey of the repo found the pointer shape in 52 of 105 task folders, so this
is not a HarmonyGames quirk. It is the upstream default that authored tasks
normally overwrite with a real export. HarmonyGames is the universe where the
pointer is the EXPECTED steady state, which is why it forced the issue.

Note on the 42 non-HarmonyGames pointers: every one names
`MCP_Eval_V2.2/Mortgage_Base_Universe` regardless of which universe the task
belongs to, so the embedded path is not trustworthy as a universe hint. This
module resolves the base path from the REGISTRY, and uses the embedded string
only to detect that a pointer is present.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from universes import detect_universe, get_universe_constants, get_framework_profile  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

POINTER_MARKERS = {"How This Works", "Base Universe Path", "Changelog Path", "SQL Query"}


class UniverseDataError(RuntimeError):
    """Raised when a task's universe data cannot be resolved. Message is operator-facing."""


def is_pointer(payload) -> bool:
    """A pointer is a 1-element array whose object carries the upstream marker keys."""
    return (
        isinstance(payload, list)
        and len(payload) == 1
        and isinstance(payload[0], dict)
        and bool(POINTER_MARKERS & set(payload[0]))
    )


def _read_task_json(task_dir: Path):
    src = task_dir / "3_UniverseDataForThisTask.json"
    if not src.is_file():
        raise UniverseDataError(f"missing {src}")
    try:
        return json.loads(src.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise UniverseDataError(f"{src} is not valid JSON: {e}") from e


def _load_changelog(task_dir: Path) -> list:
    """Changelog rows override base rows for this task only. Absent/empty is normal."""
    f = task_dir / "4_Changelog.json"
    if not f.is_file():
        return []
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    if isinstance(d, list):
        return d
    if isinstance(d, dict):
        for key in ("rows", "records", "changelog", "_changelog"):
            if isinstance(d.get(key), list):
                return d[key]
    return []


def _services_data_dir(universe: str) -> Path:
    consts = get_universe_constants(universe)
    return ROOT / consts["base_path"] / "Services_Data"


def _stream_base_export(services_dir: Path) -> list:
    """Read per-service JSON files rather than the single multi-hundred-MB blob.

    The combined `Base_Universe_Complete_Data.json` is ~223 MB; loading it to answer
    "what records exist" would put the whole universe in memory for every builder.
    The per-service directories carry the same rows, so we walk those and skip the
    combined file entirely.
    """
    records = []
    for svc_dir in sorted(p for p in services_dir.iterdir() if p.is_dir()):
        for f in sorted(svc_dir.rglob("*.json")):
            if ".git" in f.parts:
                continue
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError, UnicodeDecodeError):
                continue
            source = f"{svc_dir.name}.{f.stem}"
            rows = d if isinstance(d, list) else [d]
            for row in rows:
                if isinstance(row, dict) and "source" in row:
                    records.append(row)
                else:
                    records.append({"source": source, "row_data": json.dumps(row, ensure_ascii=False)})
    return records


def load_universe_records(task_dir: Path, universe: str = None) -> tuple:
    """Return (records, meta). Raises UniverseDataError with an actionable message.

    meta carries: contract, universe, pointer(bool), changelog_rows, base_dir.
    """
    task_dir = Path(task_dir).resolve()
    universe = universe or detect_universe(task_dir)
    contract = get_framework_profile(universe).get("universe_data_contract", "per_task_json")
    payload = _read_task_json(task_dir)
    pointer = is_pointer(payload)

    meta = {
        "universe": universe,
        "contract": contract,
        "pointer": pointer,
        "changelog_rows": 0,
        "base_dir": None,
    }

    if contract == "per_task_json":
        if pointer:
            raise UniverseDataError(
                f"{task_dir.name}: 3_UniverseDataForThisTask.json is an upstream POINTER "
                f"template, not universe data, but universe '{universe}' uses the "
                f"'per_task_json' contract. Paste the real per-task export over it. "
                f"(Silently splitting a pointer yields an empty universe and every "
                f"downstream builder then reports success against no data.)"
            )
        if not isinstance(payload, list):
            raise UniverseDataError("top-level JSON must be an array")
        return payload, meta

    if contract == "base_export_plus_changelog":
        services_dir = _services_data_dir(universe)
        meta["base_dir"] = str(services_dir)
        if not services_dir.is_dir() or not any(p.is_dir() for p in services_dir.iterdir()):
            raise UniverseDataError(
                f"{task_dir.name}: universe '{universe}' resolves its data from "
                f"{services_dir}, which is not hydrated. That directory is deliberately "
                f"gitignored (multi-GB). Hydrate it first: see "
                f"{services_dir / 'README_HYDRATE.md'}"
            )
        records = _stream_base_export(services_dir)
        changelog = _load_changelog(task_dir)
        meta["changelog_rows"] = len(changelog)
        if changelog:
            # Changelog rows override base rows for this task only; append-then-override
            # keeps provenance visible to callers that inspect `source`.
            records = records + changelog
        return records, meta

    raise UniverseDataError(
        f"universe '{universe}' declares unknown universe_data_contract "
        f"'{contract}'. Register it in FRAMEWORKS."
    )


def require_resolvable(task_dir: Path, universe: str = None) -> None:
    """Raise UniverseDataError if this universe's records cannot be resolved.

    Only a `base_export_plus_changelog` universe can be un-hydrated; a `per_task_json`
    universe carries its rows in the task file and is unaffected, so this is a no-op there.

    Exists because the S0 builders happily reported success against no data: on an
    un-hydrated HarmonyGames task, build_universe_index and build_fact_ledger both exited 0
    and wrote a Fact_Ledger whose every atom count was zero. check_hydration.py predicted
    exactly that ("Downstream builders will report success against no data") but nothing
    invoked it, so the warning could not fire.
    """
    universe = universe or detect_universe(task_dir)
    contract = get_framework_profile(universe).get("universe_data_contract", "per_task_json")
    if contract != "base_export_plus_changelog":
        return
    load_universe_records(Path(task_dir), universe)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python Validators/universe_data_source.py <task_dir>", file=sys.stderr)
        return 1
    task_dir = Path(sys.argv[1])
    try:
        records, meta = load_universe_records(task_dir)
    except UniverseDataError as e:
        print(f"UNRESOLVED: {e}")
        return 1
    print(f"universe:       {meta['universe']}")
    print(f"contract:       {meta['contract']}")
    print(f"pointer file:   {meta['pointer']}")
    print(f"changelog rows: {meta['changelog_rows']}")
    if meta["base_dir"]:
        print(f"base dir:       {meta['base_dir']}")
    print(f"records:        {len(records)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
