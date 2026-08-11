#!/usr/bin/env python3
"""
Usage:
    python Validators/test_score_extraction.py

Mutation suite for the auditor-form score extractor in `qc_verdict.py`.

Why this exists
---------------
The extractor derives a task's QC score from a human-authored auditor form. Mutation
testing found it mis-scored 8 of 9 realistic variants, and **every single miss was
optimistic**: a `$`-anchored pattern silently dropped any decorated line (`- Score: 2/5`,
`**Score: 2/5**`, `| Score: 2/5 |`, `Score: 2/5 - rationale`) and MIN then ran over the
surviving subset, returning a higher score than the form stated. MIN over a subset is not
MIN, and for a QC gate the optimistic direction is the dangerous one.

Two further cases survived a first round of fixes and were only found by review:
`Coherence: 2/5` (a dimension scored without the literal word "Score") and
`Overall Score: 2/5` (where "Overall Rubric Quality" is a genuine sub-dimension per
AGENTS.md rule 27, so the line is lexically ambiguous with the document's own aggregate).

Three attempts to fix this by widening the regex each traded one defect for another, and
two of them regressed the HarmonyGames corpus from 10/10 to 8/10 (the then-10-task
corpus) - because a pattern cannot
distinguish a dimension score from a score-shaped number in prose ("All other audited
components received 5/5") or from the form's own verdict line ("bad 2/5"). The difference is
structural, not lexical. The extractor now parses blocks.

The bar is not "returns the right number": it is **never returns a number that is too high
without saying so**. Failing loudly on an ambiguous form is acceptable; a confident wrong
answer is not.

ACCEPTED COST, stated rather than left implicit. Buying that guarantee costs false blocks:
several plausible forms now fail loudly rather than resolve. The clearest is legitimate
comparative narrative -- "The prior submission scored 2/5 on rubric quality and this revision
addresses it" -- which carries a value below the minimum scored dimension and is therefore
treated as an ambiguous drop. Em-dash separators, parenthesised scores and word numerals
likewise stop rather than guess. For a QC gate that is the right trade, because a false block
is visible and a false pass is not, but it IS a trade and it will occasionally stop a valid
form. Widen the extractors when a real one is hit; do not widen the guard.

SCOPE, stated honestly. This suite pins the shapes listed below. It does NOT prove the class
is closed, and an earlier version of this docstring claimed that it did. That claim was
false and it was falsified in the obvious way: every case in the first version was
single-score-per-block and blank-line-separated, so the suite was structurally blind to the
dominant failure mode (a block carrying several scores, where breaking on the first silently
discarded the rest). Adversarial review found it, not this file. The multi-score and
no-blank-line shapes below exist because of that miss.
"""
import sys
import shutil
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qc_verdict import parse_auditor_feedback  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# (label, form text, expected score). A result of LOUD (an error dict) is always acceptable:
# refusing to answer is safe, silently answering too high is not.
CASES = [
    # --- the nine that motivated the rewrite; all previously returned 4 instead of 2 ---
    ("plain",                    "Score: 2/5\n\nScore: 4/5\n", 2),
    ("trailing rationale",       "Score: 2/5 - rubric set is diluted\n\nScore: 4/5\n", 2),
    ("em-dash rationale",        "Score: 2/5 \u2014 diluted\n\nScore: 4/5\n", 2),
    ("bold",                     "**Score: 2/5**\n\nScore: 4/5\n", 2),
    ("markdown bullet",          "- Score: 2/5\n\nScore: 4/5\n", 2),
    ("table row",                "| Rubric | Score: 2/5 |\n\nScore: 4/5\n", 2),
    ("out of five",              "Score: 2 out of 5\n\nScore: 4/5\n", 2),
    ("lowercase",                "score: 2/5\n\nScore: 4/5\n", 2),
    ("dash separator",           "Score - 2/5\n\nScore: 4/5\n", 2),
    # --- the two found by review after the first fix round ---
    ("dimension without the word Score",
                                 "Coherence: 2/5\n\nScore: 4/5\n", 2),
    ("'Overall Score' as a dimension name",
                                 "Overall Score: 2/5\n\nScore: 4/5\n", 2),
    # --- spacing variants ---
    ("no space",                 "Score:2/5\n\nScore: 4/5\n", 2),
    ("spaced",                   "Score : 2 / 5\n\nScore: 4/5\n", 2),
    # --- the two real corpus form shapes, which must keep working ---
    ("real block form",
     "Prompt - Clarity\nScore: 2/5\nFeedback: vague\n\nRubrics - Quality\nScore: 4/5\n", 2),
    ("terse approved form",      "Approved. No failing QC issues.\n\nScore 5\n", 5),
    # --- things that must NOT be mistaken for a dimension score ---
    ("prose score shape is not a dimension",
     "Prompt - Clarity\nScore: 2/5\n\nAll other audited components received 5/5. "
     "No failing threshold was triggered.\n\nRubrics - Quality\nScore: 4/5\n", 2),
    ("auditor verdict preamble is not a dimension",
     "Auditor Score and Feedback\nbad 2/5\n\nPrompt - Clarity\nScore: 2/5\n\n"
     "Rubrics - Quality\nScore: 4/5\n", 2),
    # --- multi-score-per-block: the shape whose absence hid the dominant defect ---
    ("two dimensions in ONE block",
     "Prompt - A\nScore: 5/5\nRubrics - B\nScore: 2/5\n", 2),
    ("four dimensions, NO blank lines at all",
     "Prompt - A\nScore: 5/5\nRubrics - B\nScore: 2/5\nOE - C\nScore: 4/5\n", 2),
    ("bullet list, no blank lines",
     "- Prompt A\n- Score: 5/5\n- Rubric B\n- Score: 2/5\n", 2),
    ("indented sub-blocks",
     "Prompt\n  Score: 5/5\nRubrics\n  Score: 2/5\n", 2),
    ("two inline dimensions on one line",
     "Prompt: 5/5, Rubric: 2/5\n\nScore: 5/5\n", 2),
    ("CRLF line endings",
     "Prompt - A\r\nScore: 5/5\r\n\r\nRubrics - B\r\nScore: 2/5\r\n", 2),
    # --- dimension names that must not be eaten by the aggregate/verdict skips ---
    ("dimension named 'Pass Rate' (verdict-word collision)",
     "Pass Rate: 2/5\n\nScore: 5/5\n", 2),
    ("dimension named 'QC Score Alignment' (aggregate-label collision)",
     "QC Score Alignment: 2/5\n\nScore: 5/5\n", 2),
    ("long inline dimension name",
     "Rubric Specificity And Acceptance Criteria Quality: 2/5\n\nScore: 5/5\n", 2),
    ("copula phrasing, trailing period",
     "Score is 2/5.\n\nScore: 5/5\n", 2),
    # --- prose drops are safe in ONE direction only ---
    ("prose score ABOVE the minimum is harmlessly dropped",
     "Prompt - A\nScore: 2/5\n\nAll other audited components received 5/5. No failing threshold.\n", 2),
    ("prose score BELOW the minimum must be LOUD",
     "Prompt - A\nScore: 5/5\n\nAll other components received 2/5.\n", None),
    ("real HG form plus a decorated dimension",
     "Auditor Score and Feedback\nbad 2/5\n\nPrompt - Clarity\nScore: 3/5\n\n"
     "**Rubrics - Quality**\nScore: 2/5\n", 2),
    # --- inline dimensions on SEPARATE lines: the second branch of the same defect ---
    ("two inline dimensions on separate lines",
     "Prompt: 5/5\nRubric: 2/5\n", 2),
    ("three inline dimensions on separate lines",
     "Prompt: 5/5\nRubric: 2/5\nUniverse: 4/5\n", 2),
    # --- phrasings the extractors cannot read must be LOUD, never invisible ---
    ("word numeral must be LOUD",            "Score: two out of five\n\nScore: 5/5\n", None),
    ("'2 of 5' must be LOUD",                "Score: 2 of 5\n\nScore: 5/5\n", None),
    ("out-of-range 0/5 must be LOUD",        "Score: 0/5\n\nScore: 5/5\n", None),
    ("decimal plus rationale must be LOUD",
     "Score: 2.5/5 because the rubric set is diluted and needs work\n\nScore: 5/5\n", None),
    # --- the form's own aggregate is a value too, and only unsafe in one direction ---
    ("aggregate BELOW the minimum must be LOUD",
     "QC Score: 2\n\nPrompt - A\nScore: 4/5\n", None),
    # --- one shared score vocabulary: every RECORDER must know every phrasing the
    #     DETECTOR knows, or a detected block records nothing and the safety comparison
    #     has no value to compare against ---
    ("prose 'two out of five' below min must be LOUD",
     "Prompt - A\nScore: 5/5\n\nThe rubric section was rated two out of five overall in review.\n", None),
    ("prose '2 of 5' below min must be LOUD",
     "Prompt - A\nScore: 5/5\n\nThe rubric section was rated 2 of 5 overall in the review notes.\n", None),
    ("prose '0/5' below min must be LOUD",
     "Prompt - A\nScore: 5/5\n\nThe rubric section was rated 0/5 overall in the review notes.\n", None),
    ("aggregate written as a word numeral must be LOUD",
     "QC Score: two out of five\n\nPrompt - A\nScore: 4/5\n", None),
    # --- all three skips anchor to the first line ---
    ("preamble MENTIONED inside a dimension block is not a skip",
     "Prompt - A\nPer the Auditor Score and Feedback header\nScore: 2/5\n\nScore: 5/5\n", 2),
    # --- a declared dimension with a BLANK value, on any line ---
    ("blank 'Score:' under a header must be LOUD", "Prompt - A\nScore:\n\nScore: 5/5\n", None),
    ("blank 'Score:' as the first line must be LOUD", "Score:\n\nScore: 5/5\n", None),
    # --- an aggregate ABOVE the minimum is harmless and must stay silent ---
    ("aggregate above the minimum stays silent", "QC Score: 5\n\nPrompt - A\nScore: 2/5\n", 2),
    # --- WORD BOUNDARIES. These exist because merging five regexes into one shared token
    #     dropped the \b guards the originals carried, so a scan found a score INSIDE a
    #     larger number: "12 of 55" captured 2.0 and hard-blocked a valid form. Every gate
    #     stayed green while that was live, because no fixture placed a multi-digit number
    #     next to a score token. A consolidation must preserve the UNION of the guards it
    #     replaces; these cases are how that gets caught. ---
    ("multi-digit '12 of 55' in prose must NOT block",
     "Prompt - A\nScore: 2/5\n\nThe rubric declares 12 of 55 criteria in the set.\n", 2),
    ("'section 2 of 5' in prose must NOT block",
     "Prompt - A\nScore: 2/5\n\nSee section 2 of 5 below for the detail.\n", 2),
    ("'10/5 checks' in prose must NOT block",
     "Prompt - A\nScore: 2/5\n\nThe agent completed 10/5 of the required checks.\n", 2),
    # --- bare scores (no denominator) inside a dimension block ---
    ("bare 'Score: 2' in a dimension block",
     "Prompt - A\nScore: 2\n\nRubrics - B\nScore: 5/5\n", 2),
    ("bare score alongside a /5 score in the SAME block",
     "Prompt - A\nScore: 5/5\nScore: 2\n", 2),
    # --- aggregate status is a FALLBACK: a line an extractor can read is never an
    #     aggregate. Adding "Overall" to the aggregate vocabulary made this real dimension
    #     get consumed as the document verdict and then trip the below-minimum rule - a
    #     FALSE BLOCK, invisible while the suite accepted LOUD unconditionally. ---
    ("'Overall Score: 2/5' is a DIMENSION, not the aggregate",
     "Overall Score: 2/5\n\nScore: 5/5\n", 2),
    ("verdict consistent with dimensions resolves",
     "Auditor Score and Feedback\nbad 2/5\n\nPrompt - A\nScore: 3/5\n\n"
     "Rubrics - B\nScore: 2/5\n", 2),
    ("preamble on line 1 with consistent verdict resolves",
     "Task Feedback\nAuditor Score and Feedback\nbad 2/5\nFeedback: x\n\n"
     "Prompt - A\nScore: 3/5\n\nRubrics - B\nScore: 2/5\n", 2),
    # --- MIXED BLOCKS: a `Score:` line and an inline dimension in the SAME block. None of
    #     these shapes was represented, which is why 54 cases AND live 39/39 both stayed
    #     green while the inline collector was gated behind `if not found` - the fourth
    #     instance of one collection path being gated behind another. ---
    ("inline dimension alongside a Score: line",
     "Prompt: 2/5\nScore: 5/5\n", 2),
    ("inline dimension alongside a bare score",
     "Prompt: 2/5\nScore: 5\n", 2),
    ("two inline dimensions alongside a Score: line",
     "Prompt: 2/5\nRubric: 4/5\nScore: 5/5\n", 2),
    ("aggregate-shaped line readable as a dimension, mixed block",
     "QC Score: 2/5\nScore: 5/5\n", 2),
    # --- COPULA multi-score in one block. This pins break-on-first-score INDEPENDENTLY.
    #     After the inline collector was ungated it began redundantly reading "Score: N/5",
    #     which masked that mutation for the slash form - the defect became uncatchable by
    #     a suite that only used slash shapes. `_INLINE_DIM_SCAN` returns nothing for the
    #     copula form, so these cases fail if collection ever breaks on the first score. ---
    ("copula multi-score in one block", "Score is 5/5\nScore is 2/5\n", 2),
    ("mixed copula and colon in one block", "Score is 5/5\nScore: 2/5\n", 2),
    # --- guards must not be skipped merely because the block also contains a score ---
    ("blank 'Score:' alongside a scored line must be LOUD",
     "Prompt - A\nScore: 5/5\nScore:\n", None),
    ("prose below minimum in the SAME block as a score must be LOUD",
     "Prompt - A\nScore: 5/5\nAll other components were rated 2/5 in the earlier review.\n", None),
    ("word-numeral below minimum in the same block must be LOUD",
     "Prompt - A\nScore: 5/5\nThe rubric was rated two out of five in review.\n", None),
    # --- SPAN-level accounting. The guard containers shrank block -> line -> span over
    #     three rounds, and each time the next-finer leak appeared, because "was anything
    #     attributed here?" is the wrong question. The invariant is: every value the
    #     detector can see must be attributed, recorded as an aggregate, or passed through
    #     the one-directional guard. These pin that. ---
    ("two scores on one line, only one attributable",
     "Rubric: 5/5 and the rest scored 2 out of 5\n", None),
    ("inline dimension with a trailing word numeral",
     "Prompt - 5/5, everything else two out of five\n", None),
    # L2, decided explicitly. A historical parenthetical is arguably a correct 5, and this
    # rule makes it LOUD. Accepted for consistency with the block-level trade already taken:
    # the guard cannot tell narrative from a dimension, and a false block is visible while a
    # false pass is not. If a real form is hit, widen the EXTRACTORS, never this accounting.
    ("historical parenthetical is a KNOWN false block, not a pass",
     "Score: 5/5 (prior revision was 2/5)\n", None),
    # --- a declared dimension with no attributable score must fail loudly, not be dropped ---
    ("scoreless dimension block must be LOUD",
     "Prompt - Clarity\nSome note mentioning 3/5 oddly\nMore text\n\nScore: 4/5\n", None),

    # -------------------------------------------------------------------------------
    # FALLBACK A / FALLBACK B - the two shapes the V5 HarmonyGames drop introduced. Both
    # run only after every extractor above attributed nothing and raised no error.
    #
    # Only the OPTIMISTIC direction is testable here, which is the direction this suite
    # exists for: `run_case` reads `expect=None` as "must be LOUD", so it cannot express
    # "no score AND no error" - the state both fallbacks must produce when they decline.
    # Those declining cases are anchored in test_regression_anchors.py as v22 QC-3.
    # -------------------------------------------------------------------------------
    ("FALLBACK A: component form scoring itself `ok 3/5`",
     "Component: Rubrics - Overall Rubric Quality\nRate the Overall Rubric Quality\n\n"
     "Auditor Score and Feedback\nok 3/5\nAnswer: [Non-Fail - 5-20% Minor Errors]\n", 3),
    # THE mutant for A. An implementation that took the first match, or MAX, returns 5 and
    # is caught as OPTIMISTIC. MIN is the same rule the scored path uses.
    ("FALLBACK A: MIN across components, never the highest",
     "Component: Rubrics - Overall Rubric Quality\nRate it\n\n"
     "Auditor Score and Feedback\nok 5/5\nAnswer: [Non-Fail - A]\n\n"
     "Component: Prompt - Coherence\nRate it\n\n"
     "Auditor Score and Feedback\nok 2/5\nAnswer: [Fail - B]\n", 2),
    # NOT the condition-4 discriminator, and labelled so deliberately. Verified by mutation:
    # with `_COMPONENT_HDR` forced true this case STILL returns 2, because `Score: 2/5` is
    # attributable and the fallbacks are never reached. What it does pin is real - a document
    # verdict coexisting with a dimension resolves to the dimension, and a regression letting
    # the verdict win surfaces here as OPTIMISTIC. The actual "A declines when there is no
    # `Component:` header" discriminator requires "no score AND no error", which this harness
    # cannot express, and is v22 QC-3 in test_regression_anchors.py.
    ("FALLBACK A: doc verdict without a Component header stays a verdict",
     "Task Feedback\nAuditor Score and Feedback\nok 5/5\n\nPrompt - Coherence\nScore: 2/5\n", 2),
    ("FALLBACK B: whole-file single summary line",
     "5/5 tasks in all dimensions.\n", 5),
    # NOT the condition-5 discriminator, same reason and verified the same way: with the
    # single-line requirement relaxed to `>= 1` this case STILL returns 2, because the
    # fallback is unreachable once `Score: 2/5` is attributed. It pins that a leading summary
    # never outranks a real dimension. The "B declines on a multi-line file" discriminator is
    # also v22 QC-3.
    ("FALLBACK B must decline when the file continues past the summary",
     "5/5 tasks in all dimensions.\n\nPrompt - Coherence\nScore: 2/5\n", 2),
]


def run_case(label: str, body: str, expect):
    d = Path(tempfile.mkdtemp())
    try:
        (d / "9_QC_Feedback.txt").write_text(body, encoding="utf-8")
        r = parse_auditor_feedback(d)
        got, loud = r.get("qc_score"), bool(r.get("error"))
    finally:
        shutil.rmtree(d, ignore_errors=True)

    if loud:
        # A loud failure is acceptable ONLY where the case does not assert a value. Where a
        # correct value IS known, accepting LOUD masks a real regression: adding "Overall"
        # to the aggregate vocabulary turned the "'Overall Score' as a dimension" case from
        # returning 2 into a false block, and the suite stayed green because it accepted
        # LOUD unconditionally. Safe-direction regressions must still be visible.
        return (expect is None), got, "LOUD"
    if expect is None:
        # This case REQUIRES a loud failure; a silent number is the defect.
        return False, got, "silent"
    if got == expect:
        return True, got, ""
    # The only thing that truly matters: never silently optimistic.
    if got is not None and got > expect:
        return False, got, "OPTIMISTIC"
    return False, got, "wrong"


def check_live_corpus_parses() -> int:
    """Every REAL auditor form in the repo must parse. Returns the number that do not.

    SCOPE, measured rather than asserted. An earlier version of this docstring claimed this
    gate "would have caught both F1 and the preamble regression". That was FALSE and was
    disproved by mutation: re-introducing each previously-found defect and re-running this
    check gives

        preamble anchored to line 0   ->  8/39 loud   RED    caught
        break-on-first-score          ->  0/39 loud   GREEN  missed
        word boundaries removed       ->  0/39 loud   GREEN  missed
        bare-score collection dropped ->  0/39 loud   GREEN  missed
        inline scan on line 0 only    ->  0/39 loud   GREEN  missed

    and the extracted score vector is UNCHANGED for all four misses, so pinning values
    would not help either. The live corpus contains no multi-score block, no multi-digit
    number beside a score, no bare score, and no multi-inline block.

    So this gate detects exactly one class: a form that becomes UNPARSEABLE. That class is
    worth a gate, because such a regression is otherwise invisible - the affected tasks
    route via the verdict file, so the 133/133 selftest stays green while the fallback is
    broken, and a form that cannot be parsed is not a safe outcome merely because it is
    loud: the fallback is unavailable precisely when the verdict file is missing, which is
    the only situation it exists for.

    The synthetic suite above remains the primary defense for every other class.
    """
    roots = ["QC_Tasks/V3_Buckets", "QC_Tasks/V3.1_Buckets", "QC_Tasks/V2.1_Buckets",
             "QC_Tasks/V4_Tasks", "QC_Tasks/V5_HG_Buckets"]
    total = failed = 0
    for root in roots:
        base = ROOT / root
        if not base.is_dir():
            continue
        for f in sorted(base.rglob("9_QC_Feedback.txt")):
            if not f.read_text(encoding="utf-8", errors="ignore").strip():
                continue
            total += 1
            r = parse_auditor_feedback(f.parent)
            if r.get("error"):
                failed += 1
                print(f"  BAD  live corpus form fails to parse: {f.parent.name}")
                print(f"       {r['error'][:150]}")
    print(f"  {'ok ' if not failed else 'BAD'} live corpus: {total - failed}/{total} real auditor forms parse")
    return failed


def main() -> int:
    print("=== score-extractor mutation suite ===")
    failures, optimistic = [], 0
    for label, body, expect in CASES:
        ok, got, note = run_case(label, body, expect)
        if not ok:
            failures.append((label, got, note))
            if note == "OPTIMISTIC":
                optimistic += 1
        flag = "ok " if ok else "BAD"
        suffix = f"  [{note}]" if note else ""
        print(f"  {flag} {label:44} -> {got}{suffix}")

    print()
    live_failed = check_live_corpus_parses()
    print()
    print(f"SCORE EXTRACTION: {len(failures)} failure(s) of {len(CASES)}, "
          f"{optimistic} silently optimistic")
    if optimistic:
        print("A silently optimistic miss is the failure this suite exists to prevent: "
              "the extractor reported a HIGHER score than the form states, with no signal.")
    return 1 if (failures or live_failed) else 0


if __name__ == "__main__":
    sys.exit(main())
