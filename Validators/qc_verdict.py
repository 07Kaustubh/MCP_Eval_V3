#!/usr/bin/env python3
"""Deterministic QC verdict engine for V4 (StarPM-framework) tasks.

Commands:
  parse    <task_dir>   - structural parse of QC_Feedback_Verdict.txt + 9/10/11 trio -> JSON
  classify <task_dir>   - derive bucket from parsed CONTENT (scores + dispute decision)
  selftest <corpus_dir> - classify all labeled tasks, compare to bucket labels; every
                          classifiable task must match its bucket. Corpus size varies by
                          universe (V3/V3.1/V4 = 16, V2.1 = 80, HarmonyGames = 7 vendored
                          in a 2/3/2/0 split with one legitimately empty bucket, of which 5
                          are GRADED - two `_HG_DEPRECATED` dirs are skipped and named.
                          VENDORED and GRADED are different numbers: check_qc_corpus.py pins
                          135, selftest grades 133.
  audit    <task_dir>   - SSOT cross-reference: every finding's cited atoms checked against
                          the task's own universe data / prompt / OE / rubrics
  feedback <task_dir>   - draft a 9_QC_Feedback.txt skeleton from validator reports with
                          per-finding SSOT citations

Classification is CONTENT-ONLY (never directory names):
  qc_score 5                                  -> QC_Passed
  qc_score 3                                  -> QC_Non_Fails
  qc_score 2 + dispute approved (raised)      -> QC_False_Fails_PT_Dispute_Accepted
  qc_score 2 + no dispute or dispute rejected -> QC_True_Fails
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
MONEY_RE = re.compile(r"\$[\d,]+(?:\.\d{2})?")
ATOM_ID_RE = re.compile(
    r"\b(?:BL-[A-F0-9]{6,}|JE-[A-Za-z0-9-]{4,}|exc_[a-z0-9_]{4,}|doc_[a-f0-9]{8,}|"
    r"email_scen_[a-z0-9_]+|scenario_[a-f0-9]{6,}|FP-2026-\d{2}|C\d{3}|"
    r"rec[A-Z0-9][A-Za-z0-9]{4,}|MT-2026-\d{2,4}|OPS-\d{1,5}|INV-[A-Z0-9-]{3,}|"
    r"BILL-2026-\d{3,4}|msg_[a-z0-9_]{3,}|thr_[a-z0-9_]{3,}|cnt_[a-z0-9_]{3,}|deal_[a-z0-9_]{3,})\b"
)
CATEGORY_TAG_RE = re.compile(r"\[(Fail|Non-Fail)\s*-\s*([^\]]+)\]")
SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def _read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _sections(text: str) -> dict:
    """Split on '## Heading' markers; returns {heading: body}."""
    out = {}
    matches = list(SECTION_RE.finditer(text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[m.end():end].strip().strip("=").strip()
        out[m.group(1).strip()] = body
    return out


def _int_field(text: str, label: str):
    m = re.search(rf"^{re.escape(label)}:\s*(\d+)", text, re.MULTILINE)
    return int(m.group(1)) if m else None


def parse_verdict(task_dir: Path) -> dict:
    vp = task_dir / "QC_Feedback_Verdict.txt"
    text = _read(vp)
    if not text.strip():
        # No derived verdict file, or an empty one. Fall back to the raw auditor form
        # before giving up: the score is usually still recoverable from 9_QC_Feedback.txt.
        fallback = parse_auditor_feedback(task_dir)
        if fallback:
            return fallback
        return {"error": f"missing or empty {vp}, and 9_QC_Feedback.txt carries no score"}
    secs = _sections(text)
    error_cats = []
    ec_body = secs.get("Error Categories", "")
    m = re.search(r"\[.*\]", ec_body, re.DOTALL)
    if m:
        try:
            error_cats = json.loads(m.group(0))
        except json.JSONDecodeError:
            error_cats = re.findall(r'"([^"]+)"', ec_body)
    dispute = None
    for key in secs:
        if "Dispute" in key and "Response" not in key:
            body = secs[key]
            dv = re.search(r"^Verdict:\s*(\w+)", body, re.MULTILINE)
            ps = re.search(r"^Proposed Score:\s*(\d+)", body, re.MULTILINE)
            dispute = {
                "verdict": dv.group(1) if dv else None,
                "proposed_score": int(ps.group(1)) if ps else None,
                "feedback": body,
            }
    validation = None
    for key in secs:
        if "Validation" in key:
            body = secs[key]
            dec = re.search(r"^Decision:\s*(\w+)", body, re.MULTILINE)
            validation = {"decision": dec.group(1) if dec else None, "body": body}
    fv = None
    for key in secs:
        if key.startswith("Final Verdict"):
            m2 = re.search(r"Final Score:\s*(\d+)\s*[-\u2014]*\s*([A-Z -]+)?", secs[key])
            if m2:
                fv = {"final_score": int(m2.group(1)), "label": (m2.group(2) or "").strip()}
    findings = []
    fb = secs.get("QC Auditor Feedback", "")
    for m3 in CATEGORY_TAG_RE.finditer(fb):
        findings.append({"severity": m3.group(1), "tag": m3.group(2).strip()})
    return {
        "task": re.search(r"^Task:\s*(.+)$", text, re.MULTILINE).group(1).strip() if re.search(r"^Task:\s*(.+)$", text, re.MULTILINE) else task_dir.name,
        "business_function": (re.search(r"^Business Function:\s*(.+)$", text, re.MULTILINE) or [None]) and (re.search(r"^Business Function:\s*(.+)$", text, re.MULTILINE).group(1).strip() if re.search(r"^Business Function:\s*(.+)$", text, re.MULTILINE) else None),
        "qc_score": _int_field(text, "QC Score"),
        "final_score": _int_field(text, "Final Score"),
        "auditor_feedback": fb,
        "findings": findings,
        "error_categories": error_cats,
        "dispute": dispute,
        "validation": validation,
        "final_verdict": fv,
        "trio": {
            "9_QC_Feedback": (task_dir / "9_QC_Feedback.txt").is_file(),
            "10_PT_Dispute": (task_dir / "10_PT_Dispute_To_QC_Feedback.txt").is_file(),
            "11_Final_QC_Validation": (task_dir / "11_Final_QC_Validation_On_PT_Dispute.txt").is_file(),
        },
    }



# --- structural extraction -------------------------------------------------------------
# Regex tuning was tried three times on this and failed three times, twice by regressing the
# HarmonyGames corpus from 10/10 to 8/10 - measured against the then-10-task corpus, which
# vendors 7 and grades 5 today. The reason is that a pattern cannot tell a
# dimension score from a score-shaped number in prose ("All other audited components
# received 5/5") or from the document's own verdict line ("bad 2/5"), because the difference
# is STRUCTURAL, not lexical. So this parses structure.
#
# Two real form shapes exist in the corpus:
#   BLOCK  a dimension header line, then its `Score: N/5`, repeated, blank-line separated
#   TERSE  a two-line summary: "Approved. No failing QC issues." / "Score 5"
#
# The denominator is the number of DIMENSION BLOCKS found, so a block that declares a
# dimension but yields no attributable score is reported rather than dropped. Scope note:
# this guard covers blocks with NO attributable score. It is not a universal proof that no
# term can ever be dropped - the paths that did drop terms silently (break-on-first-score,
# over-broad aggregate skips, a prose heuristic swallowing a real dimension) were found by
# adversarial review, not by this guard, and are fixed individually above.

# A copula between the label and the value is ordinary human phrasing ("Score is 2/5."),
# and without it that line matched nothing and fell through to the prose branch, which
# dropped it silently.
_SCORE_LINE = re.compile(r"^\W*Score\s*(?:is|was|of|=)?\s*[:\-]?\s*"
                         r"([1-5])\s*(?:/\s*5|\s+out\s+of\s+5)\b", re.IGNORECASE)
# A dimension whose score is inline on the header itself: "Coherence: 2/5".
_INLINE_DIM = re.compile(r"^\W*(?P<name>[A-Za-z][\w &/()'.-]{2,60}?)\s*[:\-]\s*"
                         r"(?P<score>[1-5])\s*(?:/\s*5|\s+out\s+of\s+5)\b", re.IGNORECASE)
# The document's own verdict, not a dimension: a bare quality word plus a score.
# The form's own verdict is a BARE quality word plus a score and nothing else. Allowing
# trailing text made "Pass Rate: 2/5" match on `pass` and discarded a real dimension along
# with its score.
# Same shape as _INLINE_DIM but scannable mid-line, for headers carrying several dimensions.
# A score with no denominator ("Score: 2"). Real forms use this - the TERSE shape is a bare
# "Score 5" - but it was honored ONLY in the terse fallback, which runs when nothing else
# scored, so inside a dimension block it was invisible and the block was skipped in silence.
# Safe to attribute here because aggregate lines are skipped upstream by _AGG_LABEL.
# ONE bare-score vocabulary, shared by every consumer that needs it. Previously three
# hand-maintained patterns disagreed: `Score of 2` was known to _SCORE_LINE but not here,
# `Score is 2` was known here but not to the aggregate sweep, `Score: 2.` to neither. That
# is the same sibling drift the shared _SCORE_TOKEN removed for denominator-bearing scores
# and which was left fully intact for bare ones.
# 0 is accepted here on purpose: it is OUT OF RANGE for a 1-5 scale, and capturing it means
# the out-of-range guard can report it. Excluding it made "Score: 0" invisible instead.
_BARE_SCORE = r"Score\s*(?:is|was|of|=)?\s*[:\-]?\s*([0-5])\s*\.?\s*"
_BARE_SCORE_LINE = re.compile(r"^\W*" + _BARE_SCORE + r"$", re.IGNORECASE)
_INLINE_DIM_SCAN = re.compile(r"(?P<name>[A-Za-z][\w &/()'.-]{2,60}?)\s*[:\-]\s*"
                              r"(?P<score>[1-5])\s*(?:/\s*5|\s+out\s+of\s+5)\b", re.IGNORECASE)
_VERDICT_LINE = re.compile(r"^\W*(?:ok|bad|good|poor|pass|fail|approved|rejected)\s+"
                           r"[1-5]\s*/\s*5\W*$", re.IGNORECASE)
# The separator must follow `Score` directly. Matching the prefix alone discarded a real
# dimension named "QC Score Alignment" together with its score.
# Vocabulary kept in step with _BARE_SCORE: the copula forms ("QC Score is 2") and the
# "Overall Score" label were known to neither this nor the dimension path, so those lines
# were neither skipped as aggregates nor scored as dimensions - they were simply invisible.
# KNOWN LIMITATION, deliberate. _AGG_LABEL is `^`-anchored, so an aggregate stated
# mid-sentence ("The Final Score: 2 was assigned by the auditor in review.") is neither
# skipped as an aggregate nor read as a dimension, and a form carrying only that returns the
# dimension minimum instead. Un-anchoring it is NOT the fix: that reopens the class where a
# real dimension named "Pass Rate: 2/5" was consumed as a verdict because it began with a
# quality word. A mid-sentence score is narrative-shaped, and no live corpus form uses it.
_AGG_LABEL = re.compile(
    r"^\W*(?:QC|Final|Proposed|Auditor|Overall)\s+Score\s*(?:is|was|of|=)?\s*[:\-]?\s*\d",
    # NOTE: membership here is not sufficient to classify a line as an aggregate; see
    # _readable_as_dimension in _extract_dimension_scores. "Overall Rubric Quality" is a
    # real sub-dimension per AGENTS.md rule 27, so "Overall Score" is genuinely ambiguous
    # and must lose to any extractor that can read the line.
    re.IGNORECASE)
_PREAMBLE = re.compile(r"Auditor\s+Score\s+and\s+Feedback", re.IGNORECASE)
# Canonical vocabulary for DENOMINATOR-BEARING scores ("2/5", "two out of five"), used by
# every consumer that asks "what values does this text claim?". Bare scores ("Score: 2")
# have their own shared definition, `_BARE_SCORE`, below. The strict per-line EXTRACTORS
# (_SCORE_LINE, _INLINE_DIM, _INLINE_DIM_SCAN) are deliberately narrower than both and are
# not derived from them: the guard must be permissive so an unreadable form is loud, while
# extraction stays strict so a value is only claimed when it is unambiguous.
#
# This exists because hand-syncing several regexes was the defect generator, not a defect.
# Three rounds running, a fix landed in one site and its siblings kept the old vocabulary:
# _SCORE_LINE was taught to collect every line while _INLINE_DIM_SCAN still read only the
# first; the detector was widened to accept "two out of five" while the two RECORDERS that
# feed the safety comparison stayed narrow, so those blocks were detected as
# should-have-parsed and then recorded nothing, leaving the comparison with no value and
# returning the higher number. A shared token makes that class of drift impossible.
#
# Deliberately WIDER than the extractors: it answers only "should this block have carried a
# score?". A phrasing the extractors cannot read must be LOUD, never invisible.
_WORD_NUM = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
# NOTE on percentages: a "%" alternative was tried and REMOVED against evidence. Real
# auditor forms carry percentage thresholds in error-category names - "[Non-Fail - Up to 10%
# Major Errors]" - and a scan finds the "0%" inside "10%", recording a score of 0.0 that
# then trips the below-minimum rule on entirely legitimate text. A percentage is not a score
# out of five in this corpus, so it is deliberately out of vocabulary.
# BOTH word boundaries are load-bearing and were lost when five regexes were merged into
# this one. Without them a scan finds a score inside a larger number: "12 of 55" captured
# 2.0, "10/5" captured 0.0, "15 of 5" captured 5.0. Every gate stayed green while that was
# live, because no fixture placed a multi-digit number next to a score token. That missing
# left boundary is also the REAL reason a "%" alternative appeared to fail - it matched the
# "0%" inside "10%" - so the earlier diagnosis ("a percentage is not a score") was right
# about the conclusion and wrong about the cause.
_SCORE_TOKEN = (r"\b(?:(?P<num>[0-9](?:\.[0-9])?)|"
                r"(?P<word>zero|one|two|three|four|five))"
                r"\s*(?:/\s*5|\s*(?:out\s+)?of\s+(?:5|five))\b")
_ANY_SCORE_SHAPE = re.compile(_SCORE_TOKEN, re.IGNORECASE)


def _score_values(text: str) -> list:
    """Every score-like value in `text`, using the ONE canonical vocabulary.

    Returns floats so a decimal or a word numeral compares correctly against the minimum.
    Every consumer that needs "what values does this text claim?" calls this, so widening
    the vocabulary widens all of them at once.
    """
    out = []
    for m in _ANY_SCORE_SHAPE.finditer(text):
        if m.group("num") is not None:
            out.append(float(m.group("num")))
        else:
            out.append(float(_WORD_NUM[m.group("word").lower()]))
    return out


# A component-structured auditor form headers each section `Component: <dimension>`. The
# header and that component's score sit in DIFFERENT blocks (a blank line separates them),
# so this is deliberately a whole-FILE test, not a same-block one. It is the discriminator
# that keeps FALLBACK A off a genuine document-level verdict - see _extract_dimension_scores.
_COMPONENT_HDR = re.compile(r"^\s*Component\s*[:\-]", re.MULTILINE | re.IGNORECASE)
# A whole form that is nothing but its own summary line: "5/5 tasks in all dimensions."
# Anchored at the start and used ONLY against a single-line file - see FALLBACK B.
_TERSE_SUMMARY = re.compile(r"^([1-5])\s*/\s*5\b")


def _extract_dimension_scores(text: str, fname: str) -> tuple:
    """Return (scores, error). Structural, block-aware, fails loudly on a scoreless block."""
    blocks = [b for b in re.split(r"\n\s*\n", text) if b.strip()]
    scores, unparsed, dropped, aggregates = [], [], [], []

    for block in blocks:
        lines = [ln for ln in block.splitlines() if ln.strip()]
        if not lines:
            continue
        # Preamble / verdict / aggregate are LINE-level skips, not BLOCK-level.
        #
        # Anchoring to lines[0] and skipping the whole block was wrong in BOTH directions.
        # The real corpus's dominant form puts a "Task Feedback" title on line 0 with
        # "Auditor Score and Feedback" on line 1, so lines[0] never matched, the block was
        # kept, and its verdict value "bad 2/5" was then reported as an unattributable
        # dimension - 8 of 39 real auditor forms failed to parse. Searching the whole block
        # instead is also wrong: that was R3, where a block merely MENTIONING the preamble
        # lost its scores. Removing the offending LINES and scoring what remains satisfies
        # both, and the surviving text must be rebuilt or the checks below re-find the value
        # on a line that was just removed.
        # A line that a DIMENSION extractor can read is never an aggregate. Adding
        # "Overall" to _AGG_LABEL made the real dimension "Overall Score: 2/5" get consumed
        # as the document verdict, removed, and then trip the below-minimum rule - a false
        # block on a case an earlier round had established should score 2. Aggregate status
        # is therefore the FALLBACK: claim a line only when no extractor could attribute it.
        def _readable_as_dimension(ln: str) -> bool:
            t = ln.strip()
            return bool(_SCORE_LINE.match(t) or _BARE_SCORE_LINE.match(t)
                        or _INLINE_DIM.match(t))

        agg_lines = [ln for ln in lines
                     if not _readable_as_dimension(ln)
                     and (_PREAMBLE.match(ln.strip()) or _VERDICT_LINE.match(ln.strip())
                          or _AGG_LABEL.match(ln.strip()))]
        if agg_lines:
            for ln in agg_lines:
                aggregates.extend(_score_values(ln))
                aggregates.extend(float(m.group(1)) for m in
                                  re.finditer(_BARE_SCORE + r"(?![\d/])", ln, re.IGNORECASE))
            lines = [ln for ln in lines if ln not in agg_lines]
            if not lines:
                continue
            block = "\n".join(lines)

        # Collect EVERY score in the block. Breaking on the first meant a block carrying
        # N dimension scores contributed exactly ONE term, so [5,2,4,3] became [5] and MIN
        # silently returned 5 - the dominant silent-optimistic path, and it bypassed the
        # denominator guard entirely because a score WAS found. Verified corpus-neutral:
        # 0 of 95 blocks across all five corpora carry more than one score line.
        found = [int(m.group(1)) for m in
                 (_SCORE_LINE.match(ln.strip()) for ln in lines) if m]
        # ALWAYS collect bare scores alongside, never only-when-nothing-else-matched.
        # Gating them behind `if not found` reproduced the D1/E1 lesson a third time: a
        # block holding both "Score: 5/5" and "Score: 2" contributed only the 5. The two
        # patterns cannot overlap - _BARE_SCORE_LINE requires end-of-line after the digit,
        # so "Score: 5/5" can never match it - hence no double counting.
        found += [int(m.group(1)) for m in
                  (_BARE_SCORE_LINE.match(ln.strip()) for ln in lines) if m]
        # Collect inline dimensions ALONGSIDE, never only-when-nothing-else-matched. This
        # is the FOURTH instance of the same pattern in this function: _SCORE_LINE was
        # ungated (D1), _INLINE_DIM_SCAN's line scope widened (E1), _BARE_SCORE_LINE
        # ungated (F2) - and this gate was left. A block holding both a `Score:` line and
        # an inline dimension silently dropped the inline one, and once aggregate status
        # became a fallback, a line like "QC Score: 2/5" was excluded from the aggregate
        # path AND unreachable on this one, so its value was lost from both.
        # Measured corpus-neutral: 0 of 39 live forms change their minimum. Safe by
        # construction too - adding values can only LOWER a MIN, which is the safe
        # direction, and a duplicate match is harmless for the same reason.
        found += [int(m.group("score"))
                  for ln in lines
                  for m in _INLINE_DIM_SCAN.finditer(ln.strip())]

        # Run the remaining guards over the RESIDUAL (non-scoring) lines instead of
        # skipping them when a score was found. `if found: continue` was the FIFTH instance
        # of one path being gated behind another, and the most consequential: it meant a
        # blank label, an unattributable score shape, or prose carrying a BELOW-MINIMUM
        # value became invisible whenever it shared a block with any scored line. The
        # one-directional prose rule - built specifically to make prose drops safe - was
        # therefore effective only when a blank line happened to separate the prose from a
        # score. Guard strength must not depend on paragraph breaks.
        # Measured corpus-neutral: 0 of 39 live forms change.
        # SPAN-level accounting, implementing the invariant directly.
        #
        # The guard containers shrank each round - whole block, then per line - and each
        # time the next-finer leak appeared, because "was anything attributed here?" is the
        # wrong question. The right one is the invariant: EVERY value _score_values() can
        # see must end up attributed to a dimension, recorded as an aggregate, or passed
        # through the one-directional guard. A line yielding one attributable score was
        # removed whole, so "Rubric: 5/5 and the rest scored 2 out of 5" hid the 2.
        #
        # Cost, accepted deliberately and consistently with the same trade at block level:
        # a genuinely historical parenthetical - "Score: 5/5 (prior revision was 2/5)" -
        # now goes LOUD rather than resolving. That is a false block, and it is the safe
        # direction: a false block is visible, a false pass is not. Widen the EXTRACTORS if
        # a real form is hit; do not narrow this accounting.
        # Measured corpus-neutral: 0 of 39 live forms carry a hidden surplus.
        residual, surplus = [], []
        for ln in lines:
            t = ln.strip()
            attributed = []
            m = _SCORE_LINE.match(t)
            if m:
                attributed.append(float(m.group(1)))
            m = _BARE_SCORE_LINE.match(t)
            if m:
                attributed.append(float(m.group(1)))
            attributed += [float(m.group("score")) for m in _INLINE_DIM_SCAN.finditer(t)]
            if not attributed:
                residual.append(ln)
                continue
            leftover = list(_score_values(t))
            for a in attributed:
                if a in leftover:
                    leftover.remove(a)
            surplus.extend(leftover)
        residual_text = "\n".join(residual)

        blank_label = next((ln for ln in residual
                            if re.match(r"^\W*Score\s*[:\-]?\s*$", ln.strip(), re.IGNORECASE)),
                           None)
        if blank_label is not None:
            unparsed.append(f"{lines[0].strip()[:50]} -> blank {blank_label.strip()!r}")
            continue

        if residual and _ANY_SCORE_SHAPE.search(residual_text):
            if not _looks_like_prose(residual_text):
                unparsed.append(lines[0].strip()[:70])
                continue
            dropped.extend(_score_values(residual_text))

        # A value sharing a line with an attributed score is narrative by position, so it
        # goes through the same one-directional check rather than being discarded.
        dropped.extend(surplus)

        if found:
            scores.extend(found)
            continue

    if unparsed:
        return [], (f"partial score extraction in {fname}: {len(unparsed)} block(s) declare a "
                    f"dimension but no score could be attributed: {unparsed}. Refusing to "
                    f"report MIN over a subset, which is systematically optimistic.")

    if scores:
        # Enforce the one-directional safety property described above.
        floor = min(scores)
        below_agg = sorted(a for a in aggregates if a < floor)
        if below_agg:
            return [], (f"aggregate below minimum in {fname}: the form states an overall "
                        f"score of {below_agg} while the lowest scored dimension is {floor}. "
                        f"Reporting {floor} would be higher than the form's own verdict, "
                        f"which is the one direction that is never safe.")
        below = sorted(d for d in dropped if d < floor)
        if below:
            return [], (f"ambiguous score in {fname}: value(s) {below} appear in text read as "
                        f"narrative, but they are BELOW the minimum scored dimension "
                        f"({floor}). Dropping them would raise the reported score, which is "
                        f"the one direction a drop is never safe in. Attribute them to a "
                        f"dimension or reword the line.")
        return scores, None

    # TERSE form: "Approved. No failing QC issues." / "Score 5"
    bare = [int(x) for x in re.findall(r"^\W*" + _BARE_SCORE + r"$", text,
                                       re.MULTILINE | re.IGNORECASE)]
    if bare:
        return [min(bare)], None

    # Everything below is reached ONLY when every extractor above attributed nothing AND
    # raised no error. That gate is what makes these additive: no form that resolves today
    # can reach them, so neither can change a score that is already being reported.

    # FALLBACK A - component-structured form whose per-component score is VERDICT-shaped.
    #
    # V5 HarmonyGames ships auditor forms where each `Component:` section scores itself with
    # `ok 3/5` under the `Auditor Score and Feedback` preamble, and nothing else in the file
    # is score-shaped. `ok N/5` matches _VERDICT_LINE, so the block loop above reads it as the
    # DOCUMENT's verdict and strips it into `aggregates` - correct for a form that has one
    # verdict, wrong for a form that has one per component. Those files therefore scored
    # nothing at all and their tasks classified UNKNOWN.
    #
    # The discriminator is a `Component:` header anywhere in the file. A form without one
    # keeps the old reading and still returns nothing here, which is precisely what stops this
    # from swallowing a genuine document-level verdict line.
    #
    # MIN across components, matching the rule the scored path uses. Safe by construction in
    # the one direction that matters: these values came from `aggregates`, so the returned
    # score equals the lowest number the form states about itself and cannot exceed it.
    if _COMPONENT_HDR.search(text):
        comp = []
        for block in re.split(r"\n\s*\n", text):
            block_lines = block.splitlines()
            if not any(_PREAMBLE.match(ln.strip()) for ln in block_lines):
                continue
            for ln in block_lines:
                if _VERDICT_LINE.match(ln.strip()):
                    comp += [int(v) for v in _score_values(ln)]
        if comp:
            return [min(comp)], None

    # FALLBACK B - the whole form is a single terse summary line: "5/5 tasks in all
    # dimensions." No extractor above can read it: _SCORE_LINE and _BARE_SCORE_LINE both
    # require the literal word `Score`, and _INLINE_DIM requires a `name:` prefix.
    #
    # The file must be EXACTLY that one line. A file that merely BEGINS with a score and
    # continues with other content is not a summary - it is a form whose remaining content
    # still has to be read - and taking the leading number there would be exactly the
    # silently-optimistic move this module exists to prevent.
    body_lines = [ln for ln in text.strip().splitlines() if ln.strip()]
    if len(body_lines) == 1:
        m = _TERSE_SUMMARY.match(body_lines[0].strip())
        if m:
            return [int(m.group(1))], None

    return [], None


def _looks_like_prose(block: str) -> bool:
    """A score shape inside a sentence is narrative, not a dimension score.

    Real auditor forms write "All other audited components received 5/5. No failing
    threshold was triggered." Counting that as an unattributed dimension made the guard fire
    on 2 of 10 legitimate HarmonyGames tasks (measured against the then-10-task corpus).
    """
    first = block.splitlines()[0].strip() if block.splitlines() else ""
    # A line OPENING with a score label is a dimension line even when the extractors cannot
    # read its value ("Score: 2.5/5 because ..."). Length and punctuation are not evidence
    # against that; treating them as evidence sent an unreadable dimension down the prose
    # path, where it was dropped silently instead of reported.
    if re.match(r"^\W*Score\b", first, re.IGNORECASE):
        return False
    if _INLINE_DIM.match(first) or _SCORE_LINE.match(first):
        # It declares a dimension and a score. Length and punctuation are not evidence
        # against that, and treating them as evidence dropped real dimensions silently -
        # the same convenient-heuristic failure this parser exists to remove.
        return False
    for ln in block.splitlines():
        if _ANY_SCORE_SHAPE.search(ln):
            words = len(ln.split())
            if words > 8 or ln.strip().endswith("."):
                return True
    return False


def parse_auditor_feedback(task_dir: Path) -> dict:
    """Fallback parser for the RAW auditor form in `9_QC_Feedback.txt`.

    Some corpora ship the auditor's working document without the derived
    `QC_Feedback_Verdict.txt`, or ship that file empty (HarmonyGames does both: 2 of its
    7 vendored tasks have no verdict file and 3 more ship a 0-byte one). The score is still
    recoverable, because the raw form carries a per-dimension `Score: N/5` for every
    dimension the auditor touched.

    The overall score is taken as the MINIMUM across per-dimension scores. Be honest about
    the strength of that rule:

    - It is consistent with `Reference/Sessions/FEEDBACK.md:119` ("overall score can only be
      as high as the lowest scoring rubric"), but that line itself says "Per the QC docs
      scoring rule" and the primary source is NOT located in `Docs*/` or `Evals*/`. Treat
      this as a working rule justified by agreement with recorded scores, not as a quoted
      spec requirement.
    - Cross-validation is N=2, and BOTH cases are now deprecated. Of the 7 vendored
      HarmonyGames tasks exactly 2 ship a usable verdict file to check MIN against, and both
      are the `_HG_DEPRECATED` QC_True_Fails tasks scoring 2. MIN therefore has no
      cross-validation at all among the 5 tasks selftest actually grades.
    - MIN over several dimensions is exercised on 2 of 7, both deprecated. The other 5 resolve
      through a single score: 2 via the terse bare-score form, 2 via FALLBACK A, 1 via
      FALLBACK B.

    These figures are DISK-DERIVED and go stale on every drop. RE-COUNT them; do not rescale
    them. They were already wrong before this pass - they described a 10-task corpus while
    disk held 8 tasks with no usable verdict file and 2 with one - because the 2026-08 drop
    moved the artifacts and the prose was rescaled from the prior version instead of
    re-measured. Rescaling a wrong number produces a differently-wrong number.

    Returns {} when no score can be read, so the caller reports an honest skip rather than
    inventing a classification.

    Returns {} when no score can be read, so the caller can report an honest skip
    rather than inventing a classification.
    """
    f = task_dir / "9_QC_Feedback.txt"
    text = _read(f)
    if not text.strip():
        return {}

    scores, err = _extract_dimension_scores(text, f.name)
    if err:
        return {"error": err, "qc_score": None, "final_score": None}
    if not scores:
        return {}

    qc = min(scores)
    return {
        "task": task_dir.name,
        "business_function": None,
        "qc_score": qc,
        "final_score": qc,
        "auditor_feedback": text,
        "findings": [{"severity": m.group(1), "tag": m.group(2).strip()}
                     for m in CATEGORY_TAG_RE.finditer(text)],
        "error_categories": [],
        "dispute": None,
        "validation": None,
        "final_verdict": {"final_score": qc, "label": ""},
        "source": "9_QC_Feedback.txt (raw auditor form; score = min across dimensions)",
        "trio": {
            "9_QC_Feedback": True,
            "10_PT_Dispute": (task_dir / "10_PT_Dispute_To_QC_Feedback.txt").is_file(),
            "11_Final_QC_Validation": (task_dir / "11_Final_QC_Validation_On_PT_Dispute.txt").is_file(),
        },
    }


def classify(parsed: dict) -> str:
    qc = parsed.get("qc_score")
    final = parsed.get("final_score")
    dispute = parsed.get("dispute")
    validation = parsed.get("validation") or {}
    decision = (validation.get("decision") or "").lower()
    if qc == 5:
        return "QC_Passed"
    if qc == 3:
        return "QC_Non_Fails"
    if qc == 2:
        approved = decision.startswith("approve") or (final is not None and final > 2)
        if dispute is not None and approved:
            return "QC_False_Fails_PT_Dispute_Accepted"
        return "QC_True_Fails"
    if qc == 4:
        return "QC_Non_Fails"
    return "UNKNOWN"


def selftest(corpus: Path) -> int:
    rows, correct, total = [], 0, 0
    skipped = []
    deprecated = []
    for bucket_dir in sorted(corpus.iterdir()):
        if not bucket_dir.is_dir() or not bucket_dir.name.startswith("QC_"):
            continue
        for task_dir in sorted(bucket_dir.iterdir()):
            if not task_dir.is_dir():
                continue
            # A `_DEPRECATED` task is NOT graded. The V5 drop retired two HarmonyGames tasks
            # by RENAMING them `_HG_DEPRECATED` rather than deleting them, so their artifacts
            # stay vendored and hash-pinned (check_qc_corpus.py pins 7 HG dirs) while their
            # labels stop asserting anything about current verdict logic. Grading them would
            # let a retired task's label gate the engine; dropping them silently would make 7
            # dirs on disk render as 5 with no explanation, which is worse than not skipping
            # at all. They are excluded from BOTH numerator and denominator and REPORTED.
            #
            # This MUST stay above the has_verdict/has_raw gate: both deprecated dirs still
            # ship a non-empty 9_QC_Feedback.txt, so they would otherwise reach `total += 1`.
            if task_dir.name.endswith("_DEPRECATED"):
                deprecated.append((task_dir.name, bucket_dir.name))
                continue
            # A task is classifiable if it carries EITHER the derived verdict file or the
            # raw auditor form. Requiring only the former silently hid 5 of HarmonyGames'
            # 7 vendored tasks: 2 ship no verdict file and 3 ship a 0-byte one. Verified to
            # add zero tasks to the four pre-existing corpora, so their totals cannot move.
            has_verdict = (task_dir / "QC_Feedback_Verdict.txt").is_file() and \
                (task_dir / "QC_Feedback_Verdict.txt").stat().st_size > 0
            has_raw = (task_dir / "9_QC_Feedback.txt").is_file()
            if not has_verdict and not has_raw:
                skipped.append((task_dir.name, bucket_dir.name, "no verdict file and no 9_QC_Feedback.txt"))
                continue
            total += 1
            parsed = parse_verdict(task_dir)
            got = classify(parsed)
            ok = got == bucket_dir.name
            correct += ok
            rows.append((task_dir.name, bucket_dir.name, got,
                         parsed.get("qc_score"), parsed.get("final_score"),
                         (parsed.get("validation") or {}).get("decision"), "OK" if ok else "MISS"))
    w = max(len(r[0]) for r in rows) if rows else 10
    print(f"{'task':<{w}}  {'label':<38} {'classified':<38} qc fin decision  result")
    for r in rows:
        print(f"{r[0]:<{w}}  {r[1]:<38} {r[2]:<38} {str(r[3]):<2} {str(r[4]):<3} {str(r[5]):<9} {r[6]}")
    print()
    if skipped:
        print(f"skipped {len(skipped)} unclassifiable task(s):")
        for name, bucket, why in skipped:
            print(f"  {bucket}/{name}: {why}")
        print()
    if deprecated:
        print(f"skipped {len(deprecated)} deprecated task(s) (not graded, not counted):")
        for name, bucket in deprecated:
            print(f"  {bucket}/{name}")
        print()
    # Corpus size is NOT fixed at 16, and the printed denominator is the GRADED count, which
    # is not the vendored count. HarmonyGames vendors 7 dirs and grades 5: two are
    # `_HG_DEPRECATED` and are skipped above. Asserting a universal 16 would fail a valid
    # corpus, and asserting the vendored count would fail this one.
    print(f"QC VERDICT SELFTEST: {correct}/{total} bucket-correct")
    return 0 if correct == total and total > 0 else 1


def audit(task_dir: Path) -> int:
    parsed = parse_verdict(task_dir)
    if "error" in parsed:
        print(parsed["error"])
        return 2
    ssot_text = "\n".join(_read(task_dir / f) for f in (
        "3_UniverseDataForThisTask.json", "5_Prompt.txt", "6_Oracle_Events.txt",
        "7_Rubrics.json", "8_Verifier_Fails.txt", "1_Business_Function.txt", "2_Persona.txt"))
    traj_dir = task_dir / "Agent_Responses"
    if traj_dir.is_dir():
        for f in sorted(traj_dir.rglob("*.json"))[:8]:
            ssot_text += _read(f)
    fb = parsed.get("auditor_feedback", "")
    blocks = re.split(r"\n(?=\[(?:Fail|Non-Fail))", fb)
    n_conf = n_missing = n_none = 0
    for block in blocks:
        tag_m = CATEGORY_TAG_RE.search(block)
        if not tag_m:
            continue
        tag = f"[{tag_m.group(1)} - {tag_m.group(2).strip()}]"
        atoms = set(ATOM_ID_RE.findall(block)) | set(MONEY_RE.findall(block)) | set(EMAIL_RE.findall(block))
        if not atoms:
            n_none += 1
            print(f"FINDING {tag} | atoms: none cited | NO-ATOM-CITED (not independently verifiable - flag for revision)")
            continue
        confirmed = sorted(a for a in atoms if a in ssot_text)
        missing = sorted(a for a in atoms if a not in ssot_text)
        n_conf += len(confirmed)
        n_missing += len(missing)
        status = "CONFIRMED" if not missing else "PARTIAL" if confirmed else "NOT-FOUND"
        print(f"FINDING {tag} | atoms: {', '.join(sorted(atoms))} | {status}"
              + (f" (missing from SSOT: {', '.join(missing)})" if missing else ""))
    print(f"\nAUDIT SUMMARY: {n_conf} atoms confirmed in SSOT, {n_missing} not found, {n_none} findings cite no atoms")
    return 0


def feedback(task_dir: Path) -> int:
    """Draft 9_QC_Feedback skeleton from validator reports, per-finding SSOT citations."""
    from universes import detect_universe
    universe = detect_universe(task_dir)
    rep_dir = task_dir / "_aux" / "Validator_Reports"
    fails, nonfails = [], []
    for rp in sorted(rep_dir.glob("*.md")) if rep_dir.is_dir() else []:
        phase = rp.stem
        for line in _read(rp).splitlines():
            if line.startswith("- ") and "COUNCIL" not in line:
                entry = f"{line[2:].strip()} (validator: {phase})"
                sect = _read(rp)
                if line in sect.split("## WARN")[0] and "## FAIL" in sect.split("## WARN")[0]:
                    fails.append(entry)
                else:
                    nonfails.append(entry)
    lines = ["## QC Auditor Feedback", ""]
    if fails:
        lines.append("Failing issues:")
        for f in fails:
            atoms = set(ATOM_ID_RE.findall(f)) | set(MONEY_RE.findall(f)) | set(EMAIL_RE.findall(f))
            cite = f" [SSOT: {', '.join(sorted(atoms))}]" if atoms else " [SSOT: cite the specific record before shipping]"
            lines.append(f"- {f}{cite}")
        lines.append("")
    if nonfails:
        lines.append("Non-failing issues:")
        for f in nonfails[:20]:
            atoms = set(ATOM_ID_RE.findall(f)) | set(MONEY_RE.findall(f)) | set(EMAIL_RE.findall(f))
            cite = f" [SSOT: {', '.join(sorted(atoms))}]" if atoms else ""
            lines.append(f"- {f}{cite}")
        lines.append("")
    cats = []
    for f in fails:
        cats.append('"[All] [All] [Fail - Validator Finding]"')
    lines += ["## Error Categories", "", "[" + ", ".join(sorted(set(cats))) + "]", "",
              f"(draft generated from deterministic validator reports; universe={universe})"]
    print("\n".join(lines))
    return 0


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ("parse", "classify", "selftest", "audit", "feedback"):
        print(__doc__)
        return 2
    cmd, target = sys.argv[1], Path(sys.argv[2]).resolve()
    if cmd == "parse":
        print(json.dumps(parse_verdict(target), indent=2))
        return 0
    if cmd == "classify":
        parsed = parse_verdict(target)
        bucket = classify(parsed)
        print(f"bucket: {bucket}")
        print(f"evidence: qc_score={parsed.get('qc_score')} final_score={parsed.get('final_score')} "
              f"dispute={'yes' if parsed.get('dispute') else 'no'} "
              f"validation_decision={(parsed.get('validation') or {}).get('decision')}")
        return 0
    if cmd == "selftest":
        return selftest(target)
    if cmd == "audit":
        return audit(target)
    if cmd == "feedback":
        return feedback(target)
    return 2


if __name__ == "__main__":
    sys.exit(main())
