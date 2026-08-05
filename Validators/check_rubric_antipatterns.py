#!/usr/bin/env python3
"""
Usage:
    python Validators/check_rubric_antipatterns.py <task_dir>

Mechanically enforces the criterion-construction anti-patterns that councils and AUDIT
have found by hand, so a closed finding cannot be silently reintroduced.

Why this exists
---------------
The pipeline already computes a severity census, but it is a council SELF-REPORT in
prose, not a measurement. On Task 44 four separate reports asserted "0 Major / 0
Moderate / 0 Minor across 64" and "0/60 with any issue", while a third-party review of
the same artifact found two Moderate Overly Specific defects and one Overly Broad. An
assertion authored by the same agent that wrote the rubrics cannot catch that agent's
blind spot.

Worse, closed findings were reintroducible. `AUDIT_rubrics.md` finding F1 classified
`FAIL only if` as MODERATE ("made omission a PASS, nullifying the criterion"), fixed it
to the additive `FAIL if X, and FAIL if Y`, and verified the fix with a regex run ONCE
by hand and recorded in prose. Hours later a subsequent edit to that same criterion put
`FAIL only if` straight back, and nothing objected: `validate.py --phase rubrics`
returned 0 fails, 0 warns.

This checker turns those hand-run greps into a standing gate. It is deliberately
standalone rather than folded into `validate.py`, because `check_regression.py` pins the
hashes of 21 `validate.py` reports and changing that output would break the zero-
regression gate.

Checks
------
A1  `FAIL only if`               MODERATE. An exhaustive fail list turns every
                                unenumerated shape into a PASS, including plain
                                omission. Additive `FAIL if ... and FAIL if ...`
                                expresses the same intent with no nullification risk.
A2  bare `after <date>`          MINOR. Excludes a valid same-day action. Use
                                "on or after".
A3  hedged title, no FAIL clause MINOR. A criterion whose title hedges with
                                "recorded/reported as" but whose evidence sets no FAIL
                                condition leaves the grader to invent one, which is the
                                shape that produced attribution-demand misgrading.
A5  negative criteria           [Fail - Criteria Framing], QC dimension 23. Two-stage
                                per the spec: mechanical pre-scan for seven indicators,
                                THEN adjudication of each hit. A blanket ban on the words
                                would itself violate the spec, which ships a MUST-PASS
                                example containing one.
A6  vague exemplar language     MODERATE, one per affected rubric. `such as` / `e.g.` /
                                `for example` in ANY field, not just the title.
Both A5 and A6 come from the 2026-08 HarmonyGames drop and exist in no other universe's
QC spec, so they BLOCK only under the hg framework and print as ADVISORY elsewhere.
NOT mechanised: nested accept-sets (AUDIT_rubrics.md F2, `pass(51) => pass(23)`).
A token-overlap proxy was built and discarded: it produced 14 false positives and zero
true positives on Task 44, because mentioning a location does not mean a criterion is
restricted to it, and shared topic words do not establish that two criteria grade the
same fact. Establishing subject identity needs semantic judgement, so nesting stays a
council/AUDIT check. A gate that noisy would be ignored, which is worse than absent.

Exit 0 clean, 1 when any MODERATE fires, 0 with a printed advisory when only MINORs do.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
try:
    from Validators.universes import detect_universe, get_framework_profile
except ImportError:
    from universes import detect_universe, get_framework_profile
FIELDS = ("title", "evidence", "justification")

FAIL_ONLY_IF = re.compile(r"FAIL\s+only\s+if", re.IGNORECASE)
BARE_AFTER = re.compile(r"(?<!on or )\bdated\s+after\s+\w+\s+\d{1,2},?\s+20\d{2}", re.IGNORECASE)
HEDGE = re.compile(r"\b(?:recorded|reported)\s+as\b", re.IGNORECASE)
HAS_FAIL = re.compile(r"\bFAIL\b", re.IGNORECASE)



# ---------------------------------------------------------------------------
# A5 / A6 - the two rubric QC dimensions the 2026-08 HarmonyGames drop added.
#
# Authority: Docs_harmonygames/8_QC_Spec_Doc2.md:293-302 (Negative criteria) and :270
# (Vague Exemplar Language); Docs_harmonygames/7_QC_Spec_Doc1.json, dimension "Rubric",
# Sub-Dimensions[11] (Negative Criteria, Fail 1/2 = "[Fail - Criteria Framing]", Non-Fail
# 3/4 = "N/A", i.e. BINARY) and Sub-Dimensions[6] ("Scan every field for such as, e.g.,
# and for example; count one Moderate issue per affected rubric").
#
# The spec mandates a TWO-STAGE method and says so explicitly: "Pre-scan for does not,
# must not, never, no, without, fails to, and avoids, THEN REVIEW EACH HIT". A
# word-presence hard fail is itself a spec violation, because the spec ships a worked
# example that contains "no" and MUST pass.
# ---------------------------------------------------------------------------

# Stage 1. The seven indicators are verbatim from 8_QC_Spec_Doc2.md:296. `do not` and
# `did not` are folded in as tense variants of the spec's `does not`; widening stage 1
# cannot widen the verdict, because stage 2 adjudicates every hit.
NEG_INDICATOR = re.compile(
    r"\b(?:does not|do not|did not|must not|never|no|without|fails to|avoids)\b",
    re.IGNORECASE,
)

# Stage 2, part one: WHICH indicator. Only a negation attached to the Agent's own VERB is
# mechanically decidable. `no` and `without` are usually determiners or prepositions
# heading a noun phrase, and then they name the finding rather than negating the action.
#
# This split is not a refinement of taste, it is what the shipped corpus forces. Treating
# every indicator alike flagged seven criteria across two QC_PASSED HarmonyGames tasks,
# and five were plainly valid:
#     "The Agent records no submitted review for PR 854."
#     "The Agent reports 24 merged PRs without an APPROVED submitted review ..."
# Those are the spec's own worked-valid shape minus the `that` complementizer. Shipping
# them would repeat the A4 story in AGENTS.md rule 24: a proxy that produced 14 false
# positives and zero true positives, and a gate nobody could trust.
VERB_NEGATION = re.compile(
    r"\b(?:does not|do not|did not|must not|never|fails to|avoids|refrains from)\b",
    re.IGNORECASE,
)

# The remaining shapes - `makes no ...`, `submits no ...`, `without <noun>` - are listed by
# 8_QC_Spec_Doc2.md:284 as invalid when the prohibition ALONE defines passing, yet
# separating "The Agent makes no repository write" (the Agent's own action, invalid) from
# "The Agent records no submitted review" (a finding about the world, valid) needs
# semantics this file does not have. Both live on QC_PASSED tasks. So they are surfaced for
# the human review the spec explicitly mandates ("then review each hit") and never block.
ABSENCE_PHRASE = re.compile(
    r"\b(?:makes no|make no|has no|have no|performs no|submits no|takes no|leaves no"
    r"|refrains|without)\b",
    re.IGNORECASE,
)

# Stage 2. A negation to the RIGHT of one of these sits inside the content the Agent
# reports, not in a predicate on the Agent. This is the spec's own discriminator: in
# "The Agent reports that PR #438 had no human-submitted review" the actor and action stay
# affirmative and "no ..." only names what is being checked, whereas "The Agent does not
# omit the ENG-1797 link" negates the Agent's own verb.
CONTENT_BOUNDARY = re.compile(
    r"[,:;(]"
    r"|\b(?:that|whether|which|who|whom|whose|where|when|why|how"
    r"|because|since|so|including|if|until|while|with)\b",
    re.IGNORECASE,
)

VAGUE_EXEMPLAR = re.compile(r"\b(?:such as|e\.g\.|for example)", re.IGNORECASE)


def negative_framing_hit(title: str):
    """Stage 2 adjudication. Return (indicator, span) when the title negates the AGENT's
    own action; None when the negation only describes the reported content.

    Two accepted false-NEGATIVE shapes, both deliberate:
      - a comma inside a long subject noun phrase ("The Agent's email to David, Catalina
        and Marcus does not propose ...") reads as a content boundary;
      - a matrix negation in a clause coordinated after a content clause ("... reports that
        X had no review, and does not include the link").
    The miss direction is chosen, not overlooked. Negative Criteria is binary Fail=2/Pass=5
    with no partial band, so one false positive fails the whole sub-dimension for a
    legitimate task, while a false negative merely falls through to the human review the
    spec already requires ("then review each hit").
    """
    m = VERB_NEGATION.search(title)
    if not m:
        return None
    b = CONTENT_BOUNDARY.search(title)
    if b and b.start() < m.start():
        return None
    return m.group(0), title[:m.end() + 40].strip()


def absence_phrase_hit(title: str):
    """Prohibition-shaped but NOT mechanically decidable. Returns (phrase, span) or None.

    Advisory only, and deliberately never blocking - see ABSENCE_PHRASE. Reported so the
    spec's stage-2 human review has the list, rather than silently dropping the shape.
    """
    if negative_framing_hit(title):
        return None
    m = ABSENCE_PHRASE.search(title)
    if not m:
        return None
    b = CONTENT_BOUNDARY.search(title)
    if b and b.start() < m.start():
        return None
    return m.group(0), title[:m.end() + 40].strip()


_MANDATE_STOP = {
    "the", "that", "this", "with", "from", "they", "them", "their", "have", "has", "does",
    "not", "been", "will", "your", "you", "and", "for", "are", "was", "were", "agent",
    "when", "what", "which", "while", "into", "also", "than", "then", "only", "must",
    "shall", "should", "would", "could", "there", "here", "about", "into", "over",
}
# A prohibition MANDATE is an instruction TO THE AGENT, not the author describing
# themselves. Task 34's prompt says "I do not have authority on the client facing piece" -
# a first-person declarative that mandates nothing - and reading it as a mandate would have
# excused two genuine negative predicates in that task's rubric set. So first-person
# subjects are excluded, and the sentence must additionally share >= 2 significant tokens
# with the criterion, so that one unrelated "don't" cannot excuse every negative criterion
# in the set. Both halves are deliberately strict: the exemption should be hard to earn.
_PROHIBITION = re.compile(
    r"\b(?:do not|don'?t|never|must not|avoid|refrain from|no need to)\b"
    r"|\bleave\b[^.]{0,40}\b(?:alone|unchanged|as is|untouched)\b",
    re.IGNORECASE,
)
_FIRST_PERSON = re.compile(
    r"\b(?:i|we)\b[^.]{0,30}?\b(?:do not|don'?t|never|am not|are not|cannot|can'?t|will not|won'?t)\b",
    re.IGNORECASE,
)


def _significant(text: str) -> set:
    return {t for t in re.findall(r"[a-z0-9#-]{4,}", text.lower()) if t not in _MANDATE_STOP}


def prompt_mandate_for(title: str, prompt_text: str):
    """Return the prompt sentence that explicitly mandates this non-action, else None."""
    if not prompt_text:
        return None
    t_sig = _significant(title)
    for sent in re.split(r"(?<=[.!?])\s+|\n+", prompt_text):
        s = sent.strip()
        if not s or not _PROHIBITION.search(s) or _FIRST_PERSON.search(s):
            continue
        if len(_significant(s) & t_sig) >= 2:
            return " ".join(s.split())
    return None


def vague_exemplar_fields(fields: dict) -> list:
    """[(field, phrase)] across EVERY field. The caller counts ONE Moderate per rubric,
    per 7_QC_Spec_Doc1.json Sub-Dimensions[6]: "one Moderate issue per affected rubric",
    regardless of how many phrases or fields are involved."""
    out = []
    for name, val in fields.items():
        if not isinstance(val, str):
            continue
        m = VAGUE_EXEMPLAR.search(val)
        if m:
            out.append((name, m.group(0)))
    return out


def load(task: Path):
    data = json.loads((task / "7_Rubrics.json").read_text(encoding="utf-8"))
    crits = data if isinstance(data, list) else (data.get("rubrics") or data.get("criteria"))
    return [{"idx": i + 1, **{f: (c.get(f) or "") for f in FIELDS}} for i, c in enumerate(crits)]


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    task = Path(sys.argv[1])
    if not task.is_absolute():
        task = ROOT / task
    if not (task / "7_Rubrics.json").is_file():
        print(f"[SKIP] {task}: no 7_Rubrics.json")
        return 0

    try:
        crits = load(task)
    except json.JSONDecodeError as e:
        # A gate must not answer with a traceback. One of the ten shipped HarmonyGames
        # corpus tasks (QC_Non_Fails/Task1_6a5ad85c4c083980490873d6_HG) carries an
        # unescaped double quote inside a justification string, so this path is reachable
        # on real vendored data, not just on operator typos.
        print(f"[FAIL] {task.name}: 7_Rubrics.json is not valid JSON: {e}")
        return 1
    mod, minor, advisory, notes = [], [], [], []

    # A5/A6 BLOCK only where the dimension exists. Per AGENTS.md rule 25 each universe
    # follows its own spec, and only HarmonyGames has these two. Elsewhere the finding is
    # still printed - it is a real observation - but as ADVISORY, not a spec claim.
    profile = get_framework_profile(detect_universe(task))
    neg_blocks = profile.get("rubric_negative_criteria_gate", False)
    vague_all_fields = profile.get("rubric_vague_exemplar_scope") == "all_fields"
    pf = task / "5_Prompt.txt"
    prompt_raw = pf.read_text(encoding="utf-8") if pf.is_file() else ""

    for c in crits:
        hit = negative_framing_hit(c["title"])
        if hit:
            indicator, span = hit
            mandate = prompt_mandate_for(c["title"], prompt_raw)
            if mandate:
                notes.append(("A5", c["idx"], "title",
                              f"negative framing `{indicator}` is prompt-mandated, so the "
                              f"spec's explicit non-action exemption applies. Mandating "
                              f"sentence: \"{mandate[:140]}\"", span))
            else:
                (mod if neg_blocks else advisory).append((
                    "A5", c["idx"], "title",
                    "[Fail - Criteria Framing] the title negates the Agent's own action via "
                    f"`{indicator}`, and no prompt sentence mandates that prohibition. "
                    "Rewrite affirmatively. A negative word is fine when it only names the "
                    "reported content, as in `reports that PR #438 had no human-submitted "
                    "review`.", span))
        else:
            ap = absence_phrase_hit(c["title"])
            if ap:
                notes.append(("A5", c["idx"], "title",
                              f"prohibition-shaped `{ap[0]}` needs the stage-2 human review "
                              "the spec mandates: it is invalid only if the prohibition ALONE "
                              "defines passing. Never blocking - `records no submitted review` "
                              "is valid, `makes no repository write` is not, and telling them "
                              "apart is semantic.", ap[1]))
        vf = vague_exemplar_fields({f: c[f] for f in FIELDS})
        if vf:
            # One Moderate per affected rubric, not per phrase and not per field.
            field, phrase = vf[0]
            extra = f" (+{len(vf) - 1} more field(s))" if len(vf) > 1 else ""
            (mod if vague_all_fields else advisory).append((
                "A6", c["idx"], field,
                f"Vague Exemplar Language: `{phrase}`{extra}. Illustrative language leaves "
                "the accepted set undefined. State the accepted set or an objective "
                "semantic rule instead.", c[field][:110]))

    for c in crits:
        for f in FIELDS:
            for m in FAIL_ONLY_IF.finditer(c[f]):
                mod.append(("A1", c["idx"], f,
                            "`FAIL only if` makes every unenumerated shape a PASS, "
                            "including plain omission. Rewrite additively: "
                            "`FAIL if X, and FAIL if Y`.",
                            c[f][max(0, m.start() - 60):m.start() + 90]))
            for m in BARE_AFTER.finditer(c[f]):
                minor.append(("A2", c["idx"], f,
                              "bare `after <date>` excludes a valid same-day action; "
                              "use `on or after`.", m.group(0)))
        if HEDGE.search(c["title"]) and not HAS_FAIL.search(c["evidence"]):
            minor.append(("A3", c["idx"], "evidence",
                          "title hedges with 'recorded/reported as' but the evidence sets "
                          "no FAIL condition, leaving the grader to invent one. This is the "
                          "shape that produces attribution-demand misgrading.",
                          c["title"][:90]))

    print(f"=== Rubric anti-pattern scan: {task.name} ===")
    print(f"{len(crits)} criteria x {len(FIELDS)} fields\n")

    seen, uniq_mod = set(), []
    for h in mod:
        k = (h[0], h[1], h[2])
        if k not in seen:
            seen.add(k)
            uniq_mod.append(h)

    for label, bucket in (("MODERATE", uniq_mod), ("MINOR", minor),
                          ("ADVISORY (dimension not in this universe's QC spec)", advisory),
                          ("NOTE (prompt-mandated, allowed)", notes)):
        if not bucket:
            continue
        print(f"[{label}] {len(bucket)} finding(s):")
        for code, idx, field, why, snip in bucket:
            print(f"  {code}  criterion {idx} [{field}]")
            print(f"      {why}")
            print(f"      ...{snip.strip()}...")
        print()

    if not uniq_mod and not minor and not advisory and not notes:
        print(f"[OK] {task.name}: no construction anti-patterns found.")
        return 0
    if uniq_mod:
        print("MODERATE findings block. Each one has cost this project a council round "
              "before; they are mechanically detectable and must not ship.")
        return 1
    print("No blocking findings. MINOR/ADVISORY/NOTE are informational.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
