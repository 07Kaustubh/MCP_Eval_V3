#!/usr/bin/env python3
"""
Usage:
    python Validators/test_registry_schema.py

Shape gate for the UNIVERSES registry in `universes.py`.

Why this exists
---------------
`UNIVERSES` is a hand-maintained dict of ~40 keys per universe, and nothing has ever
checked that the entries agree on their key set. They do not: entries have drifted as
universes were added, so a consumer that reads `consts["personas"]` works for one
universe and raises KeyError for another. The failure is silent until the wrong
universe is loaded.

This gate derives the expected key set as the UNION of every entry's keys, then reports
per-entry gaps and per-key type disagreements.

It also enforces the sentinel rule (Hydra `MISSING` / pydantic `extra='forbid'`): a
registry value of the literal string "UNRESOLVED" means a fact was not adjudicated from
primary sources. Encoding a guess instead is the failure this rule exists to prevent, so
a live sentinel keeps this gate RED on purpose until a human resolves it.

Exit 0 when every entry has an identical key set, types agree, and no sentinel remains.
Non-zero otherwise.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from universes import UNIVERSES  # noqa: E402

SENTINEL = "UNRESOLVED"

# CORE keys are load-bearing for every universe: a consumer may read them unconditionally,
# so an absent one is a latent KeyError. These MUST be present in every entry.
CORE_KEYS = {
    "name", "framework_version", "domain", "base_path", "docs_path", "evals_path",
    "tool_catalog", "persona_briefs", "qc_reference_path",
    "similarity_corpus_globs", "similarity_reads_injection",
    "today", "today_tz", "persona_email_domain", "business_functions",
    "tight_identifiers", "oe_service_map", "cross_service_pairs",
    "retention_codes", "slack_channels", "classifications", "npcs", "services",
    "account_trap_check", "entity_name_to_id", "tool_param_traps", "landmines",
}

# OPTIONAL keys are genuinely domain-specific (TRID windows mean nothing outside a
# mortgage universe). Absence is legitimate, so it is reported as INFO, never FAIL.
# Listing them explicitly is the point: absence must be a declared choice, not an
# accident nobody noticed. Anything in neither set is an UNDECLARED key and does fail.
OPTIONAL_KEYS = {
    "business_function_weights", "personas", "universe_one_pager", "business_function_doc",
    "lifecycle_check_kind", "lifecycle_states_closed", "lifecycle_states_open",
    "blackline_exception_types",
    "loan_statuses_open", "loan_statuses_closed", "condition_statuses", "trid_windows",
    "universe_schema", "persona_acl_roster", "tool_access_dir", "injection_window",
    "long_horizon_calls", "acl_scoped_services", "acl_unscoped_services",
    "id_pattern_set", "index_internal_by_domain", "index_tz_from_registry",
    "weekend_comms_rule",
    # Logical-table -> split-source overrides for build_universe_index. Declared only by a
    # universe whose export tables are named differently from the v3-family defaults
    # (HarmonyGames: `slack.users`, `linear.issues`). Absence means "the defaults are
    # correct here", which is true for the other four, so it is optional by design.
    "index_table_map",
}


def type_name(value) -> str:
    return type(value).__name__


def check_key_parity(universes: dict) -> tuple:
    """CORE keys must exist everywhere. OPTIONAL absences are informational.

    A key in neither set is undeclared: the registry grew a field nobody classified.
    """
    issues, notes = [], []
    union = set()
    for entry in universes.values():
        union |= set(entry.keys())

    undeclared = sorted(union - CORE_KEYS - OPTIONAL_KEYS)
    for key in undeclared:
        holders = sorted(u for u in universes if key in universes[u])
        issues.append(
            f"FAIL: key `{key}` is in neither CORE_KEYS nor OPTIONAL_KEYS "
            f"(declared by: {', '.join(holders)}). Classify it so absence is a choice."
        )

    for name in sorted(universes):
        present = set(universes[name].keys())
        for key in sorted(CORE_KEYS - present):
            issues.append(f"FAIL: universe `{name}` is missing CORE key `{key}`")
        for key in sorted((OPTIONAL_KEYS & union) - present):
            notes.append(f"note: `{name}` omits optional key `{key}` (domain-specific)")

    return issues, notes


def check_type_parity(universes: dict) -> list:
    """A key shared by 2+ entries should carry the same type in each."""
    issues = []
    types_by_key: dict = {}
    for name, entry in universes.items():
        for key, value in entry.items():
            types_by_key.setdefault(key, {})[name] = type_name(value)

    for key in sorted(types_by_key):
        seen = types_by_key[key]
        distinct = set(seen.values())
        if len(distinct) > 1:
            detail = ", ".join(f"{u}={t}" for u, t in sorted(seen.items()))
            issues.append(f"FAIL: key `{key}` has inconsistent types across universes ({detail})")
    return issues



def check_paths_resolve(universes: dict) -> list:
    """Every path a universe declares must actually exist on disk.

    This exists because of a real near-miss: an edit intended to remove duplicated path
    keys from FRAMEWORKS also stripped `docs_path` / `evals_path` / `qc_reference_path`
    from all four UNIVERSES entries, and `check_regression.py` still reported PASS -
    78/78 anchors, 21/21 identical reports, 7/7 verdicts. The regression suite has no
    coverage of path resolution, which is the mechanism by which every validator finds
    its spec. Adding a universe is exactly the change that breaks it.
    """
    issues = []
    root = Path(__file__).resolve().parent.parent
    path_keys = ("base_path", "docs_path", "evals_path", "qc_reference_path",
                 "tool_catalog", "persona_briefs")
    for name in sorted(universes):
        entry = universes[name]
        for key in path_keys:
            val = entry.get(key)
            if val is None:
                issues.append(f"FAIL: `{name}.{key}` is None - a consumer resolving it gets no path")
                continue
            if not (root / val).exists():
                issues.append(f"FAIL: `{name}.{key}` = {val!r} does not exist on disk")
    return issues


def check_sentinels(universes: dict) -> list:
    """No registry value may be the UNRESOLVED sentinel."""
    issues = []
    for name in sorted(universes):
        for key, value in sorted(universes[name].items()):
            if isinstance(value, str) and value.strip() == SENTINEL:
                issues.append(
                    f"FAIL: `{name}.{key}` is the {SENTINEL} sentinel - a primary-source "
                    f"adjudication is outstanding. Resolve it; do not encode a guess."
                )
    return issues


def main() -> int:
    issues, notes = check_key_parity(UNIVERSES)
    issues += check_paths_resolve(UNIVERSES)
    issues += check_type_parity(UNIVERSES)
    issues += check_sentinels(UNIVERSES)

    for line in notes:
        print(line)
    if notes:
        print()
    for line in issues:
        print(line)

    print()
    print(f"REGISTRY SCHEMA: {len(issues)} gaps across {len(UNIVERSES)} universes "
          f"({', '.join(sorted(UNIVERSES))})")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
