#!/usr/bin/env python3
"""
Usage:
    python Validators/check_capability_registry.py

A capability-registry linter for `universes.py`.

Why this exists
---------------
Kubernetes KEP-2558 makes a point worth stealing: when a project keeps a registry of
capabilities, the registry drifts from its consumers silently, so the project adds a
MECHANICAL check that the declared registry and the code reading it have not diverged.
Nobody notices the drift by reading, because the registry still looks correct on its own
terms. It is only wrong relative to something else. AGENTS.md rule 30 says the same thing
for this repo: the pipeline's own internal citations are checked, not trusted.

`universes.py` is that registry here: `UNIVERSES` (four tenants) plus `FRAMEWORKS` (four
behavioral profiles). A fifth universe is being added. Four failure modes are worth
pinning before that happens, because each one gets harder to see with a fifth entry.

RED BY DESIGN
-------------
This linter FAILS today, and the findings are pre-existing. It changes no behavior in
`universes.py`; C4 in particular REPORTS a fallback rather than removing it.

Checks
------
C1 CONSUMERS      A capability nothing consumes is a claim, not a capability. Verifies
                  `get_framework_profile` has at least one non-test caller outside
                  `universes.py`, and that the registry's own description of its consumers
                  matches reality.
C2 NO DUPLICATION No key may live in BOTH a FRAMEWORKS profile and a UNIVERSES entry. Two
                  homes for one fact is two places to update and one place to forget.
C3 FLAG PARITY    No profile may omit a flag another profile declares. A missing flag does
                  not read as "not applicable"; it reads as whatever each caller's own
                  .get() default happens to be.
C4 NO SILENT      Absence must raise, not inherit. Hydra models this with the MISSING
   INHERIT        sentinel (interpolating an unset value is an error, never a default) and
                  pydantic with `extra='forbid'`. A lookup that silently returns another
                  tenant's record is the same class of bug as a multi-tenant query missing
                  its tenant filter: it succeeds, and it answers about the wrong tenant.

Exit 0 clean, non-zero on any finding.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VALIDATORS = ROOT / "Validators"

try:
    from Validators.universes import (
        FRAMEWORKS,
        UNIVERSES,
        get_framework_profile,
        get_universe_constants,
    )
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from universes import (
        FRAMEWORKS,
        UNIVERSES,
        get_framework_profile,
        get_universe_constants,
    )

REGISTRY_FILE = VALIDATORS / "universes.py"
CAPABILITY = "get_framework_profile"
STALE_CLAIM = re.compile(r"Nothing reads this yet", re.IGNORECASE)
UNKNOWN_UNIVERSE = "__no_such_universe__"


def _consumer_files() -> list:
    """Validators/*.py mentioning the capability, excluding the registry, tests and self."""
    hits = []
    for path in sorted(VALIDATORS.glob("*.py")):
        if path.name in ("universes.py", Path(__file__).name) or path.name.startswith("test_"):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        lines = [
            (n, line.strip())
            for n, line in enumerate(text.splitlines(), 1)
            if CAPABILITY in line
        ]
        if lines:
            hits.append((path.name, lines))
    return hits


def _stale_claims() -> list:
    """Lines in universes.py asserting the capability has no consumers."""
    if not REGISTRY_FILE.is_file():
        return []
    text = REGISTRY_FILE.read_text(encoding="utf-8", errors="ignore")
    return [
        (n, line.strip())
        for n, line in enumerate(text.splitlines(), 1)
        if STALE_CLAIM.search(line)
    ]


def check_consumers() -> list:
    """C1: is the capability actually consumed, and does the registry describe that truthfully?"""
    issues = []
    print("--- C1 CONSUMERS ---")
    consumers = _consumer_files()
    call_sites = [
        (name, n, line)
        for name, lines in consumers
        for n, line in lines
        if re.search(rf"{CAPABILITY}\s*\(", line)
    ]

    if not consumers:
        issues.append(
            f"FAIL C1: `{CAPABILITY}` has ZERO non-test callers outside universes.py. "
            f"A profile table nothing reads cannot diverge from behavior, because it drives "
            f"none. It is documentation shaped like code."
        )
    else:
        print(f"[OK] C1: {CAPABILITY} has {len(consumers)} consumer file(s), "
              f"{len(call_sites)} call site(s):")
        for name, lines in consumers:
            for n, line in lines:
                print(f"       {name}:{n}: {line}")

    stale = _stale_claims()
    if stale and call_sites:
        print("[FAIL] C1: the registry's own account of its consumers is stale:")
        for n, line in stale:
            print(f"       universes.py:{n}: {line}")
        issues.append(
            f"FAIL C1: universes.py lines {', '.join(str(n) for n, _ in stale)} still assert "
            f"\"Nothing reads this yet\" while {len(call_sites)} call site(s) exist in "
            f"{', '.join(name for name, _ in consumers)}. Validators/AGENTS.md meanwhile states "
            f"\"Every other validator imports its constants from here.\" Both cannot be true. "
            f"A reader trusting the comment will assume the table is inert and safe to edit."
        )
    return issues


def check_no_duplication() -> list:
    """C2: a key must not be defined in both tables - one of them is stale by construction."""
    issues = []
    print("--- C2 NO DUPLICATION ---")
    framework_keys = set()
    for profile in FRAMEWORKS.values():
        framework_keys |= set(profile.keys())
    universe_keys = set()
    for entry in UNIVERSES.values():
        universe_keys |= set(entry.keys())

    for key in sorted(framework_keys & universe_keys):
        fw = sorted(v for v, p in FRAMEWORKS.items() if key in p)
        uv = sorted(u for u, e in UNIVERSES.items() if key in e)
        agree = all(
            UNIVERSES[u].get(key)
            == FRAMEWORKS.get(UNIVERSES[u].get("framework_version"), {}).get(key)
            for u in uv
        )
        issues.append(
            f"FAIL C2: key `{key}` is defined in BOTH tables - "
            f"FRAMEWORKS({', '.join(fw)}) and UNIVERSES({', '.join(uv)}). "
            f"Values agree today: {agree}. That is precisely the danger: the next edit lands "
            f"in one table, both lookups keep succeeding, and which value a consumer sees "
            f"depends on which accessor it happened to call."
        )
    if not issues:
        print("[OK] C2: no key is defined in both FRAMEWORKS and UNIVERSES")
    return issues


def check_flag_parity() -> list:
    """C3: every profile declares every flag, so absence is never ambiguous."""
    issues = []
    print("--- C3 FLAG PARITY ---")
    union = set()
    for profile in FRAMEWORKS.values():
        union |= set(profile.keys())

    for version in sorted(FRAMEWORKS):
        for flag in sorted(union - set(FRAMEWORKS[version].keys())):
            holders = {v: FRAMEWORKS[v][flag] for v in sorted(FRAMEWORKS) if flag in FRAMEWORKS[v]}
            issues.append(
                f"FAIL C3: framework profile `{version}` omits flag `{flag}` "
                f"(declared elsewhere as {holders}). An omitted flag is not 'not applicable'. "
                f"Every consumer reaching for it supplies its own .get() default, so the "
                f"profile that omits it has no single answer - it has one answer per call site."
            )
    if not issues:
        print(f"[OK] C3: all {len(FRAMEWORKS)} profiles declare the same {len(union)} flags")
    return issues


def check_no_silent_inherit() -> list:
    """C4: an unknown universe/framework must RAISE, never inherit a sibling's values."""
    issues = []
    UNKNOWN_UNIVERSE = "__no_such_universe__"
    try:
        consts = get_universe_constants(UNKNOWN_UNIVERSE)
        issues.append(
            f"FAIL C4: get_universe_constants({UNKNOWN_UNIVERSE!r}) returned "
            f"{consts.get('name')!r} instead of raising. A typo in _aux/Universe.txt would "
            f"silently apply another universe's constants."
        )
    except KeyError:
        print("[OK] C4a: get_universe_constants raises on an unknown universe")
    try:
        prof = get_framework_profile(UNKNOWN_UNIVERSE)
        issues.append(
            f"FAIL C4: get_framework_profile({UNKNOWN_UNIVERSE!r}) returned a profile "
            f"(density_target={prof.get('density_target')!r}) instead of raising."
        )
    except KeyError:
        print("[OK] C4b: get_framework_profile raises on an unknown universe")
    return issues


def main() -> int:
    print("=== Capability registry: Validators/universes.py ===")
    print(f"{len(UNIVERSES)} universes: {', '.join(sorted(UNIVERSES))}")
    print(f"{len(FRAMEWORKS)} framework profiles: {', '.join(sorted(FRAMEWORKS))}\n")

    issues = []
    issues += check_consumers()
    issues += check_no_duplication()
    issues += check_flag_parity()
    issues += check_no_silent_inherit()

    if issues:
        print()
        for line in issues:
            print(line)

    print()
    print(f"CAPABILITY REGISTRY: {len(issues)} findings")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
