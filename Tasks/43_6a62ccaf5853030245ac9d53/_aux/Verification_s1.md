# Verification — S1 (Prompt)

## Sources consulted
- Per-task data :: `_aux/Universe_Split/` — grounded prompt against: AR invoice `445653930748` (DocNumber 2026-534, customer Linda Castillo, lines $387/$1,140/$95, total $1,622, TxnDate 2026-05-01); belief email `5101c5a41dffa90a` (Carlos to Linda, subj "Mesa Vista 4C Make-Ready Complete. Cost Summary for Your Records"); Airtable 4C make-ready rows (`recc8534b3fd13954` selReady, `recbd087a4abd605b` selProg); AP bills for deep clean $387 / repaint $1,340 / closet $85 / Alamo internal $85. Verified directly (parsed row_data).
- Per-task data :: `_aux/Fact_Ledger.json` — atom surface cross-checked; prompt intentionally carries ZERO tight identifiers (no IDs, amounts, or dates) so the atom-verifier reports 0 atoms (clean, no phantoms).
- Per-task data :: `_aux/Hardness_Plan.md` — levers L2 (structured-DB skip, flagship) / L10 (supersession) / L6 (near-miss) / L11 (net-vs-gross) preserved in the prompt framing; owner anchored as Linda (Pete Donovan is the painter decoy, kept out of the prompt); correct total $1,812 kept out of the prompt.
- Eval spec :: `Evals_starpm/1_Prompt_Eval.md` — all 12 Prompt sub-dims verified (see below); HARD GATES (UGT End-State Divergence, Write-Action Divergence, Delegation Clarity, Feasibility, Truthfulness phantom-grep, Alignment-with-Today) cleared.
- QC spec :: `Docs_starpm/7_QC_Spec_Doc1.json` (+ `8_QC_Spec_Doc2.md`) — Prompt dimension sub-dims scored via Council B (1/3/5 & binary schemes per `Reference/Council_Protocol.md`); AUDIT re-scored under strictest interpretation. Note: the stale "Jun 12 US/Eastern" string inside the JSON is superseded; today = 2026-07-01 America/Chicago.
- Reference :: `Reference/Prompt_Format.md` — voice / anti-patterns / 500-word cap / no-em-dash / no-tool-name / no-ID re-checked. `QC_Tasks/V4_Tasks/QC_Passed/Task1..4/5_Prompt.txt` for reference voice; `Tasks/38..42/5_Prompt.txt` for similarity awareness (Task 42 collision consciously diverged).

## Eval spec sub-dims (Evals_starpm/1_Prompt_Eval.md) verified
- 1.1 Unique Ground Truth :: PASS (5) — one correct end-state ($1,812 corrected invoice + Airtable close + owner note + channel post); $1,622 / $1,897 / $1,727 are trapped model errors the pass-through framing forecloses, not valid readings.
- 1.2 Feasibility :: PASS (5) — all data materialized (AR invoice, AP bills, Airtable 4C, Linda contact, channels). AUDIT note: Airtable tblMakeReady has no cost field / no "Closed" status — absorbed by fldNotes2 (multilineText); carry-forward for S2 write mechanism.
- 1.3 Explicit Tool Mention :: PASS (5) — no MCP tool names, no "use the X tool"; "Airtable" is a locative system-of-record reference (permitted).
- 1.4 Prompt Clarity and Specificity :: PASS (5) — no second reading flips a write action; correct-existing (not create-new) and act-and-fix (not defer) are unambiguous.
- 1.5 Contrived / Unnatural :: PASS (5) — mid-thought entry, one coherent situation, Carlos's steady structured voice.
- 1.6 Truthfulness :: PASS (5) — per-atom evidence table clean (Council A + AUDIT); zero ungrounded claims.
- 1.7 Tool use and Cross-service requirement :: PASS (5) — validator detects 3 named services; real trajectory spans QuickBooks + Airtable + Gmail + Slack + Contacts.
- 1.8 Investigation :: PASS (5) — reconciliation-then-act; investigation (AP-bill re-derivation) + 4 writes.
- 1.9 Coherence :: PASS (5) — bolt-on WARN adjudicated as heuristic false positive (remove-sentence test orphans the downstream "where it landed"/"corrected number" asks → load-bearing).
- 1.10 Persona :: PASS (5) — Carlos Mendez, Onsite PM, anchors Mesa Vista; 4C is his signature scenario.
- 1.11 Business Function :: PASS (5) — Property Operations (StarPM BF1), Unit Turnover Coordination.
- 1.12 Alignment with Today's Date :: PASS (5) — today 2026-07-01; May turn + prior invoice are consistent; no unresolved relative-date window.

## QC spec sub-dims (Docs_starpm/7_QC_Spec_Doc1.json — Prompt dimension) verified
- All 12 Prompt sub-dims scored 5/5 by Council B and re-scored 5/5 by AUDIT under strictest interpretation (NON-FAIL middle bands collapsed to REVISE — none invoked). Universe Data Exists 5/5 and Cross-service Coherence 5/5 also confirmed. Scheme map per `Reference/Council_Protocol.md`.

## Verification statements
- [x] Validator (validate.py --phase prompt) exit 0 (0 fails, 1 heuristic WARN adjudicated false-positive, 4 notes).
- [x] Council A grounding + convention clean (zero ungrounded claims, zero convention drift). Report: `_aux/Council_Reports/prompt_A_grounding.md` → GO.
- [x] Council B QC scoring shows every applicable sub-dim 5/5 (no NON-FAIL bands invoked). Density Opus ~43 PASS / Gemini ~34 THIN (documented-accept); levers 4/4 preserved. Report: `_aux/Council_Reports/prompt_B_adversarial.md` → GO.
- [x] Similarity gate (calc_similarity.py) composite 27.4 (< 40; < 35). `_aux/Similarity_Report.json` present. Task 42 sibling collision consciously diverged (its composite 11.0).
- [x] AUDIT verdict = PASS (STRICT). Report: `_aux/Council_Reports/AUDIT_prompt.md`. 62/62 regression anchors; 0 leakage; 4/4 levers surfaced.

## Discrepancies surfaced (if any)
- None blocking at S1. Four carry-forward watch-items for S2/S3 (from Council B + AUDIT), all downstream OE/rubric grounding, none a prompt-phase defect:
  1. Pin the exact Slack channel in the OE (prompt is channel-agnostic by design; #vendors / #owner-relations / #make-ready all plausible).
  2. Pin the exact 4C Airtable row and grade on content (stale selProg vs live selReady — intended L1 latch).
  3. Specify the Airtable write mechanism — tblMakeReady has no cost field / no "Closed" status; use fldNotes2 (multilineText) for final owner cost + closed state.
  4. Ground the include-closet ($85, real Permian vendor) vs exclude-Alamo ($85, internal walk) rationale explicitly so the $1,727 and $1,897 decoy paths grade as genuine failures.

## Verdict
- PASS — 5_Prompt.txt clears validator, Council A (GO), Council B (GO, 5/5 all sub-dims), similarity (27.4 < 40), and strict AUDIT (PASS (STRICT)). All exit criteria met. Ready for platform linter / S2.
