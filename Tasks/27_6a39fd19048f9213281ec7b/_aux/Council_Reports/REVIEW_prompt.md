# REVIEW — Prompt (Council A grounding + Council B 5-lens)

## Validator

PASS, 0 fails / 0 warns / 3 notes. Notes: word count 389 (over 300 but inside 500 cap); relative date "this week" present (resolvable against universe today 2026-06-12).

## Council A — Grounding sweep

Every entity Ben names is in the per-task universe (verified by grep against `_aux/Universe_Split/Universe_complete_data.json`):

- `brookfield_FP-2026-05`: confirmed.
- account `102000` Cash - Payroll: confirmed.
- recon `BL-333FF9956BC6`: confirmed, variance -28.59, gl_balance 2,192,357.22, supporting 2,192,385.81, variance_explanations carries the FX revaluation note.
- exception `exc_aade06f6129e43`: confirmed, financial_impact -28.59, description "Subledger feed dropped 29 expected rows...".
- Slack thread on C005: confirmed (slack message id 488ff92cf7665e079e4f5e1308949571).
- email "Disposition approval request: exc_aade06f6129e43" Blue → Daniel: confirmed.
- messaging thread `conversation_scen_009_orphan_exception_0001`: confirmed.
- FP-2025-11 BL-8DCA6908E272: confirmed (variance -3.42, certified).
- FP-2025-11 payroll feed run_9e4afe5f93d549: confirmed (status `retried`, 119/119/0).

The prompt does not name `brookfield_6000001115`. The fabricated record only appears in OE5b/5c and rubric 6 — Council A grounding is on the prompt only.

## Council B — 5 lenses

### Lens 1 — Truthfulness

PASS. The prompt does not assert the "true cause." It only asks the agent to disprove the thread story and find what really moved the balance. Asking is fair; the universe-gap is downstream in OE/rubric.

### Lens 2 — Hardness / lever density

PASS. Multi-thread adjudication (Slack + email + messaging), feed-history check, recon attachment check, precedent check, multi-party writeback, reminder. Five-plus levers.

### Lens 3 — Persona fit

PASS. Bookkeeper context-pull arc, matches the canonical Marina-Soko-AML-triage pattern Ben anchors elsewhere. The earlier linter pushback (`_aux/Linter_Decision.md`) is sound.

### Lens 4 — Coherence / naturalness

PASS. Reads like a Slack ask. The "Blue asked me to sanity-check" framing carries the social context cleanly.

### Lens 5 — Red-team

CONCERN — feasibility. The prompt itself is honest about asking for a real cause. The risk is that the prompt's framing ("don't just check that one feed") nudges the agent toward expecting a real discriminator that the universe does not contain. This concern fires at the rubric, not the prompt.

## Verdict — Prompt phase only

**Worst sub-dim Score: 2 (Feasibility, FAIL band).** The prompt would be a solid PASS in isolation; it is only a FAIL because the scenario it commits to has no grounded answer.

## Findings flagged into changes.md (Prompt phase)

| Severity | Finding |
|---|---|
| Minor | Word count 389 — over 300 sweet spot; tighten in rebuild. |
| Minor | Relative date "this week" — pin to "the FP-2026-05 close cycle" or similar to remove resolution ambiguity. |
| Major | Prompt's implicit discriminator (real cause beyond "unsupported") does not exist in the universe — see Universe + OE findings. |
