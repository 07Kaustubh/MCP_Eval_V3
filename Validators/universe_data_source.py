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


def _scan_contract(universe: str) -> dict:
    """The declared table/payload split for this universe's export."""
    scan = get_framework_profile(universe).get("export_table_scan")
    if not isinstance(scan, dict):
        raise UniverseDataError(
            f"universe '{universe}' resolves its data from the base export but its framework "
            f"declares no `export_table_scan` contract. Add one to FRAMEWORKS: without it the "
            f"walk has no way to tell a table from a per-file payload."
        )
    return scan


_WS = " \t\n\r"


class _JsonCursor:
    """Forward-only JSON reader that keeps only a bounded window of the file in memory.

    `JSONDecoder.raw_decode` needs the value it is decoding to be present in a str, but it
    does NOT need the rest of the file. That is the seam this class is built on: refill a
    window on demand, decode one value, drop the consumed prefix.

    CHUNK is characters, not bytes. It is deliberately small: the window is the memory
    bound, and a value larger than the window (a long gdoc body) simply grows the buffer
    until it completes, so nothing is lost by keeping the steady state tight.
    """

    CHUNK = 1 << 20

    def __init__(self, fh):
        self.fh = fh
        self.buf = ""
        self.pos = 0
        self.eof = False
        # Per-cursor, not module-level: JSONDecoder carries a `memo` of object keys, and
        # sharing one across every file in the payload would retain keys for the whole run.
        self.dec = json.JSONDecoder()

    def _fill(self) -> bool:
        """Append one chunk, first discarding whatever has already been consumed.

        Dropping the prefix is what makes the window bounded rather than merely lazy. A
        reader that only appended would end up holding the whole file and would measure
        exactly like the `read_text` version it replaced.
        """
        if self.eof:
            return False
        data = self.fh.read(self.CHUNK)
        if not data:
            self.eof = True
            return False
        if self.pos:
            self.buf = self.buf[self.pos:]
            self.pos = 0
        self.buf += data
        return True

    def peek(self) -> str:
        """Next non-whitespace character, or '' at end of file. Does not consume it."""
        while True:
            while self.pos < len(self.buf) and self.buf[self.pos] in _WS:
                self.pos += 1
            if self.pos < len(self.buf):
                return self.buf[self.pos]
            if not self._fill():
                return ""

    def advance(self) -> None:
        self.pos += 1

    def take(self, ch: str) -> bool:
        if self.peek() == ch:
            self.pos += 1
            return True
        return False

    def value(self, bad):
        """Decode exactly one JSON value at the cursor."""
        self.peek()   # position on the first non-whitespace character
        while True:
            try:
                val, end = self.dec.raw_decode(self.buf, self.pos)
            except json.JSONDecodeError as e:
                # Could be a genuinely malformed file, or simply a value that has not been
                # read in full yet. Only the second is fixable, and only by reading more.
                if self._fill():
                    continue
                raise bad(f"at offset {self.pos} of the current window: {e}") from e
            if end >= len(self.buf) and not self.eof and self._fill():
                # A value ending exactly at the window edge may be truncated - `1234` read
                # as `1` with `234` still on disk. Objects and strings cannot end early
                # like this, but numbers and literals can, so redo with more context.
                continue
            self.pos = end
            return val


def _iter_table_rows(path: Path, svc: str):
    """Yield (source, row) one row at a time, never holding the file's full parse.

    Three real shapes exist in the V5 export and each needs a different source name:

      {"issues": [...], "attachments": [...]}   dict-of-tables -> one source PER KEY
      [ {...}, {...} ]                          bare array     -> the file IS the table
      {"labels": 24, "messages": 24738}         adapter counts -> a single row, not a table

    The old walk collapsed all three into `rows = d if isinstance(d, list) else [d]`, so
    `linear/data.json` became ONE record named `linear.data` carrying 7 MB of JSON as a
    string. Nothing downstream could find `linear.issues` because nothing ever emitted it.

    Why this is hand-rolled rather than `json.loads(...)`, which would be four lines:
    MEASURED, three times, each number against the 384 MiB ceiling of AGENTS.md rule 33.

        rglob walk, whole-file json.loads          1,837 MiB   715,697 records
        scoped walk, whole-file json.loads           738 MiB   185,618 records
        scoped walk, whole-file text + raw_decode    620 MiB   185,618 records
        scoped walk, sliding window (this)            see G2b

    The second number is why the walk being scoped is not on its own enough: `json.loads`
    on this payload costs roughly 10x file size, and github/data.json alone adds 364 MiB.
    The third is why row-at-a-time decoding is not enough either: holding the file TEXT is
    itself the dominant term, because CPython widens this file to 4 bytes per character -
    39.4 MB on disk becomes a 157.4 MB str, and reading it peaks at 227 MiB before a single
    row is decoded.

    So the text is never held whole. `_JsonCursor` keeps a bounded sliding window and
    `JSONDecoder.raw_decode` - the stdlib's one incremental entry point - decodes exactly
    one value at a time from it. Peak is the window plus the largest single row.

    Everything outside `raw_decode` is structural bookkeeping only: whitespace, `,`, `:`,
    `[`, `]`, `{`, `}`. No value is ever parsed by this code, so a malformed file still
    fails inside the stdlib decoder. Equivalence with the obvious `json.load`
    implementation is asserted per file by regression anchor `v22 UDS-2`.
    """
    def _bad(where):
        return UniverseDataError(
            f"{path} is not a well-formed service table ({where}). This file is a DECLARED "
            f"table (top-level *.json, not an excluded stem), so a parse failure is a real "
            f"defect rather than a file to skip."
        )

    try:
        fh = open(path, "r", encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        raise UniverseDataError(f"cannot read table file {path}: {e}") from e

    with fh:
        cur = _JsonCursor(fh)
        first = cur.peek()
        if first == "":
            return

        # Shape 1: the file IS the table.
        if first == "[":
            cur.advance()
            source = f"{svc}.{path.stem}"
            if cur.take("]"):
                return
            while True:
                yield source, cur.value(_bad)
                if cur.take(","):
                    continue
                if cur.take("]"):
                    return
                raise _bad("expected ',' or ']' in table array")

        if first != "{":
            raise _bad(f"top level is {first!r}, expected '[' or '{{'")

        # Shapes 2 and 3: an object. Every list-valued key is a table; a file with no
        # list-valued key at all is a single row (the adapter-counts shape).
        cur.advance()
        if cur.take("}"):
            return
        scalars = {}
        emitted_a_table = False
        while True:
            key = cur.value(_bad)
            if not cur.take(":"):
                raise _bad(f"expected ':' after key {key!r}")
            if cur.peek() == "[":
                cur.advance()
                emitted_a_table = True
                source = f"{svc}.{key}"
                if not cur.take("]"):
                    while True:
                        yield source, cur.value(_bad)
                        if cur.take(","):
                            continue
                        if cur.take("]"):
                            break
                        raise _bad(f"expected ',' or ']' in table {key!r}")
            else:
                # Non-list values are the adapter's own counts and are tiny. Nothing in
                # this payload puts a table behind a non-list key.
                scalars[key] = cur.value(_bad)
            if cur.take(","):
                continue
            if cur.take("}"):
                break
            raise _bad("expected ',' or '}' in service file object")

        if not emitted_a_table:
            yield f"{svc}.{path.stem}", scalars


def _iter_base_export(services_dir: Path, scan: dict):
    """Stream (never accumulate) the records of the base export, one table file at a time.

    Constant-memory per AGENTS.md rule 33: peak is one parsed table file, not the payload.
    The predecessor `_stream_base_export` was named for streaming but returned a list, and
    its `rglob` descended into the per-file payload trees. Measured before: 715,697 records
    across 47,571 source stems at ~1,837 MiB peak RSS, against a 384 MiB ceiling.
    """
    table_glob = scan.get("table_glob", "*.json")
    non_table = set(scan.get("non_table_stems") or ())
    content_subdirs = set(scan.get("content_subdirs") or ())

    for svc_dir in sorted(p for p in services_dir.iterdir() if p.is_dir()):
        # An undeclared subdirectory is a loud failure, not a silent skip. This is the half
        # of the contract that makes the next upstream rename visible: if a drop moves the
        # tables under a new directory, this raises instead of quietly emitting nothing -
        # which is exactly how HG-U21 stayed invisible through every gate.
        for child in sorted(svc_dir.iterdir()):
            if not child.is_dir() or child.name.startswith("."):
                continue
            if child.name not in content_subdirs:
                raise UniverseDataError(
                    f"{svc_dir.name}/{child.name}/ is not declared in this universe's "
                    f"`export_table_scan.content_subdirs` ({sorted(content_subdirs)}). "
                    f"Either it holds tables and the contract must name where, or it holds "
                    f"per-file payload and must be listed as content. Refusing to guess: "
                    f"guessing is what produced 47,571 phantom source stems."
                )

        for f in sorted(svc_dir.glob(table_glob)):
            if f.stem in non_table:
                continue
            for source, row in _iter_table_rows(f, svc_dir.name):
                if isinstance(row, dict) and "source" in row:
                    yield row
                else:
                    yield {"source": source, "row_data": json.dumps(row, ensure_ascii=False)}


def iter_universe_records(task_dir: Path, universe: str = None) -> tuple:
    """Return (records, meta) where `records` is ITERABLE, not necessarily a list.

    This is the canonical accessor. `load_universe_records` is a thin alias kept for the
    existing call sites.

    CONTRACT, stated plainly because it changed:
      * `per_task_json` -> `records` is the parsed list, exactly as before. Unchanged.
      * `base_export_plus_changelog` -> `records` is a GENERATOR. It can be iterated once,
        `len()` does not apply, and materialising it re-creates AGENTS.md HG-U22.

    Callers that need a length must count while streaming. The single consumer that took a
    length (split_universe.py) now does exactly that.

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
        scan = _scan_contract(universe)
        changelog = _load_changelog(task_dir)
        meta["changelog_rows"] = len(changelog)

        def _stream():
            yield from _iter_base_export(services_dir, scan)
            # Changelog rows override base rows for this task only; yielding them last
            # keeps provenance visible to callers that inspect `source`, and keeps the
            # override semantics of the previous append-at-the-end behaviour.
            yield from changelog

        return _stream(), meta

    raise UniverseDataError(
        f"universe '{universe}' declares unknown universe_data_contract "
        f"'{contract}'. Register it in FRAMEWORKS."
    )


def load_universe_records(task_dir: Path, universe: str = None) -> tuple:
    """Alias for `iter_universe_records`. See that function for the return contract.

    Deliberately NOT `list(iter_universe_records(...))`: wrapping the generator would
    restore the 1.8 GiB peak this change exists to remove.
    """
    return iter_universe_records(task_dir, universe)


def _resolve_or_raise(task_dir: Path, universe: str) -> None:
    """The cheap half of resolution: every condition that makes the loader raise.

    Kept separate from `can_resolve` (which returns a bool) because callers need the
    actionable message, and separate from the loader because answering "does this resolve?"
    must not read the payload.
    """
    services_dir = _services_data_dir(universe)
    if not services_dir.is_dir() or not any(p.is_dir() for p in services_dir.iterdir()):
        raise UniverseDataError(
            f"{Path(task_dir).name}: universe '{universe}' resolves its data from "
            f"{services_dir}, which is not hydrated. That directory is deliberately "
            f"gitignored (multi-GB). Hydrate it first: see "
            f"{services_dir / 'README_HYDRATE.md'}"
        )
    _scan_contract(universe)


def require_resolvable(task_dir: Path, universe: str = None) -> None:
    """Raise UniverseDataError if this universe's records cannot be resolved.

    Only a `base_export_plus_changelog` universe can be un-hydrated; a `per_task_json`
    universe carries its rows in the task file and is unaffected, so this is a no-op there.

    Exists because the S0 builders happily reported success against no data: on an
    un-hydrated HarmonyGames task, build_universe_index and build_fact_ledger both exited 0
    and wrote a Fact_Ledger whose every atom count was zero. check_hydration.py predicted
    exactly that ("Downstream builders will report success against no data") but nothing
    invoked it, so the warning could not fire.

    FOUR S0 builders call this purely for the yes/no. It used to answer by running the full
    record loader, so each of them paid ~1.8 GiB and a full payload read for a boolean -
    the other half of AGENTS.md HG-U22. It now evaluates only the conditions that can fail.
    """
    universe = universe or detect_universe(task_dir)
    contract = get_framework_profile(universe).get("universe_data_contract", "per_task_json")
    if contract != "base_export_plus_changelog":
        return
    _resolve_or_raise(Path(task_dir), universe)


def can_resolve(task_dir: Path, universe: str = None) -> bool:
    """Cheap "would load_universe_records succeed?" without loading anything.

    Consuming the record stream to answer a yes/no reads every table in the export -
    185,618 records across 38 tables for HarmonyGames on the V5 payload. Calling it merely
    to ask whether the data RESOLVES made every gate that asked that question read the
    whole universe, which took the anchor suite from about a minute to over ten once the
    payload was hydrated. The conditions that make it raise are all cheap directory/shape
    checks, so they are evaluated here on their own.

    (The retired "850k records / 5.6 GB" figures in this docstring described the rglob walk
    that AGENTS.md HG-U22 records; that walk reached 715,697 records at ~1,837 MiB peak RSS
    before it was scoped to the declared tables.)
    """
    task_dir = Path(task_dir)
    universe = universe or detect_universe(task_dir)
    contract = get_framework_profile(universe).get("universe_data_contract", "per_task_json")
    if contract == "per_task_json":
        try:
            payload = _read_task_json(task_dir)
        except Exception:
            return False
        return (not is_pointer(payload)) and isinstance(payload, list)
    if contract == "base_export_plus_changelog":
        d = _services_data_dir(universe)
        try:
            return d.is_dir() and any(p.is_dir() for p in d.iterdir())
        except Exception:
            return False
    return False


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python Validators/universe_data_source.py <task_dir>", file=sys.stderr)
        return 1
    task_dir = Path(sys.argv[1])
    try:
        records, meta = iter_universe_records(task_dir)
        # Count while streaming. `len(records)` was correct only while this returned a list,
        # and restoring it would silently re-materialise the export.
        n_records = 0
        sources = set()
        for rec in records:
            n_records += 1
            sources.add(rec.get("source"))
    except UniverseDataError as e:
        print(f"UNRESOLVED: {e}")
        return 1
    print(f"universe:       {meta['universe']}")
    print(f"contract:       {meta['contract']}")
    print(f"pointer file:   {meta['pointer']}")
    print(f"changelog rows: {meta['changelog_rows']}")
    if meta["base_dir"]:
        print(f"base dir:       {meta['base_dir']}")
    print(f"records:        {n_records}")
    print(f"sources:        {len(sources)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
