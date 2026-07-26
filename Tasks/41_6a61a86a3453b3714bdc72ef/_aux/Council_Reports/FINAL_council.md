# FINAL CROSS-ARTIFACT COUNCIL — Task 41_6a61a86a3453b3714bdc72ef

**Universe:** StarPM V4 (dual-model: Opus 4.8 + Gemini) · **Persona:** Patricia Nguyen (patricia.nguyen@starpm.com, Onsite PM) · **Today in-universe:** 2026-07-01 America/Chicago.
**Scope:** last cross-artifact gate before platform upload. Read prompt + OE + rubrics + Hardness_Plan + Fact_Ledger + Universe_Split TOGETHER; verified every tight identifier and derived figure against `_aux/Universe_Split/` and `StarPM_Base_Universe/7_Server_Tools_Details.json`.
**State of downstream files:** `8a/8b_Verifier_Fails`, `9_QC_Feedback`, PT-dispute, final-QC, and all 12 `Agent_Responses/*/RunN_Trajectory.json` are **0 bytes** → task not yet run. Density is therefore a **projection** (expected at this pre-upload stage), not a measured value.

---

## LENS 1 — Truthfulness (identifier + derived-figure grounding, answer-leakage)

**PASS — zero phantom, zero leak.** Every tight identifier greps to a real row (re-verified from source via python3, not trusting prior councils):

- QB bill **QR-2026-0441 / id 232176553533**: lines 847.00 (May arrears), 925.00 (June rent), 210.00 (late fees thru 6/29), 150.00 ("Partial payment plan credit applied"); **Balance/TotalAmt 2132.00**; **VendorRef "Alamo HVAC Services", CustomerRef ABSENT**; PrivateNote = Teresa Wood consolidated ledger forwarded to Patricia Nguyen/Brooke Phillips. ✔
- QB invoice **7214 / id 283231782926**: Balance 0.00, TotalAmt 8173.44, CustomerRef Tanya Mitchell proj-2e48c594aab7, lines 1125/975/187.5/5885.94, PrivateNote "Mitchell account remains delinquent with no cure received". ✔ (decoy)
- QB bill **2026-EV-047 / id 146128608253**: Balance 185.00, VendorRef Hill Country Plumbing, no CustomerRef, PrivateNote "Internal administrative cost for assembling…filing package". ✔ (not tenant-owed)
- Airtable make-ready: reca8230a8fd9ff51 ("Sunset Ridge Unit 14", selSched), recc83c05d889b354 ("Unit 14", selSched, mod 2026-07-01 11:18:57, JP-coordination possession-hold note + Brooke flag instruction), rec94e86a3007dd5e ("Rio Bend - Unit 14", selReady, decoy). Supersession chain rec769→rec8005(selProg,"Payment Plan Breached")→rec91517("3-Day Notice…June 26/29")→rec3782("did not cure")→receee45("awaiting owner sign-off")→recc83(JP coord, current) all verified verbatim. ✔
- Airtable tickets: EVF-2026-014 (rec922b9a2d1b9451, "Owner authorization received from Linda Castillo…Owner Approved - Ready to File", completion 2026-06-30) and DLQ-2026-0601 (recc0ecc885e9645e, selHigh, "$75 late fee…Past Due - Grace Period Expired", Patricia Nguyen). ✔
- Linear OPS-32 ("Eviction Hearing - Mitchell, Harris Property", In Progress, priority 1, team_001), OPS-38, OPS-54. ✔
- Slack C003 (#general) / C004 (#make-ready); all 5 timestamps present in C003 (1782673915 "payment plan is now breached", 1782673930 "3-day notice has been served", 1782881568 "owner-approved. JP coordination is underway…before the petition goes in", superseded 1778696318 "moved to the court stage" / 1778696320 "locked and ready for the Mitchell hearing"). ✔
- Gmail thread **621640f9e7aa6d46**, subject_normalized "eviction filing authorization. tanya mitchell. unit 14", Linda-Castillo full-authorization reply. ✔
- Contacts: Tanya Mitchell (Tenant), Linda Castillo (Property Owner), John Castillo (Water Delivery Representative, decoy), Patricia Nguyen (Onsite PM). ✔

**Derived figures RECOMPUTABLE from stored atoms:** 847+925+210 = **1,982** charges; −150 credit = **1,832** net; stored Balance 2132 = 1982+150 (credit double-counted as positive). Fully synthesizable, not stated.

**ANSWER-LEAKAGE — CLEAN. I independently re-ran the grep and AGREE with the parent operator.**
- `5_Prompt.txt`: zero hits for `1832`, `1,832`, `1982`, `1,982` (any form).
- `_aux/Universe_Split/`: zero hits for comma-formatted `1,832` or `1,982` anywhere. Bare `1832` occurs exactly 3 times — all coincidental substrings: a base64-encoded email-campaign body (gmail_messages) and a Slack "add it after Alicia's items" campaign message (inside a hash/ts), never as a dollar value. `1982`/`2132` hits are timestamp/microsecond/object-id substrings; `2132.00` appears verbatim only as the intended decoy Balance. Fact_Ledger `amounts[]` contains 2132.00 but **neither 1832.00 nor 1982.00** — confirming both are derive-only.

Grader-side statement of $1,832/$1,982 in OE + Rubrics is required and correct (not leakage).

---

## LENS 2 — Rubric binding (18 rubrics)

**PASS.** 18 Outcome / 0 Process (programmatically confirmed). Every rubric maps to an OE step and a prompt ask; "approximately" appears only on the three derived dollar figures (R0/R1/R14), never on an ID/date/account. No tool names in any title. No channel/method lock-in: R8 accepts OPS-32 OR EVF-2026-014; R11 accepts "#make-ready" name OR C004 id ("Accept the channel name or its id"); R5 accepts either Sunset Ridge record id. All decoy values ($0, $2,132, $8,173.44, $13,208.75, $185; Rio Bend, John Castillo, Harry Harris/"Harris Property") sit exclusively in FAIL/exclusion clauses.

**submission_gate WARN — rubric #2 (idx1, "charges total ~$1,982 comprising $847, $925, $210") NOT_ATOMIC — ADJUDICATED: NOT A DEFECT, no split.** The prompt explicitly demands "walk it back to the underlying charges so I know it is the clean number." The three components are ONE composite walk-back read from the SAME tool output (bill QR-2026-0441 line detail); they pass/fail on the SAME single error (agent walks it back → gets all three; agent cites invoice 7214's $1,125/$975/$187.50 → fails all three). They are not independently sourced, unlike the Learnings #5/#7/#8 owner-approved⟂JP-status pair (different records, judge flip-flop) which WAS correctly split into R9/R10 and R15/R16. Splitting idx1 would manufacture redundancy the always-failing-rubrics doc warns against. Evidence field ("Accept any reference that walks the figure back to the May arrears, June rent, and late-fee components") instructs holistic acceptance. **Verdict: legitimate walk-back composition; keep as-is.** (Single residual watch-item for the first verifier run.)

**rubrics-validator 18 WARNs (evidence-enumeration + X2 amount-consistency):** the "evidence contains $0/$1,832/$2,132/$13,208.75 not in criterion" warns are the blessed L18/L19 high-discrimination pattern — the criterion carries the primary value ($1,832 with "approximately") and the judge grades criterion first; enumerated decoys are consistent guidance, not stricter criteria. The `rubric[10]↔rubric[16]` 73% Jaccard is the same owner-approved fact on two DIFFERENT deliverables (eviction note vs owner email) → per-deliverable coverage across distinct writes (blessed, not redundant). All 18 warns are expected/adjudicated; none escalate.

---

## LENS 3 — Cross-artifact holism (forward/reverse/lever/entity map)

**PASS.** Forward map: all 8 prompt asks → ≥1 OE and ≥1 rubric (balance→OE2-5/R0-R1; eviction status+owner-auth→OE9-13/R2-R3; hold?→OE7-8/R4; update record→OE14/R5-R7; note→OE15/R8-R10; channel→OE16/R11-R12; owner draft→OE17/R13-R17; "tell me if I'm off"→OE18 corrections). Reverse map: every OE and every rubric traces to a prompt ask; no orphan.

**LEVER map — all 5 selected + stacked L6 trace end-to-end:**
| Lever | Prompt sentence | OE | Rubric |
|---|---|---|---|
| L2 structured-DB skip (flagship) | "walk it back to the underlying charges…clean number" | OE4/5 (vendor-linked AP bill, no CustomerRef) | R0, R1 |
| L10 supersession | "last I tracked…about at the hearing stage" | OE9/10/12 (JP coord supersedes active-plan/awaiting-sign-off) | R2, R9, R15 |
| L1 latching | "confirm we have the owner's authorization on file" | OE11/13 (EVF Linda vs OPS-32 "Harris Property hearing") | R3, R10, R16 |
| L11 net-vs-gross/sign | "not double-counting any credit or adjustment" | OE5 ($150 credit stored as positive) | R0 |
| L31 negative-directive (Gemini) | "I don't want the crew mobilizing…or us marketing something we can't deliver" | OE14/16/17 (explicit prohibitions) | R4, R6, R7, R12, R17 |

The rubric split reinforces L1 (owner=Linda now graded on R10+R16) and L10 (not-filed on R9+R15). No lever orphaned.

**Entity map:** Tanya Mitchell / Linda Castillo / Sunset Ridge Unit 14 / Patricia Nguyen consistent across prompt+OE+rubrics. Decoys Rio Bend Unit 14, John Castillo, Harry Harris appear ONLY in OE disambiguation and rubric FAIL clauses — **never in the prompt** (prompt clean, implicit). Zero Lisa Smith in any deliverable (and none in 2_Persona/PersonaBrief, which name Patricia Nguyen).

**Implicit-framing:** persona believes the reassuring frame ("back rent had mostly been squared away", "about at the hearing stage") and asks to verify+execute. No rubric demands an investigation the prompt forbids; no rubric fails a correct-executor. R6 (do-not-advance-turn) and R4/R7/R12/R17 (state the hold) are the intended over-action/negative-directive guards, aligned with "I don't want the crew mobilizing."

---

## LENS 4 — Red-team adversarial

**PASS.** 
- **Shortcut path fails correctly:** an agent that reads AR invoice 7214 (Balance $0) and stops reports "current/paid" → fails R0 (FAIL clause enumerates $0/"current/paid"), R1, R14. An agent that trusts OPS-32/Slack "hearing" framing → fails R2. An agent that grabs Rio Bend Unit 14 → fails R4/R5. No single obvious search recovers $1,832 (requires: query the correct object TYPE = AP bill invisible to customer/invoice queries, read 4 lines, subtract the credit) — the trap is not shallow.
- **Second-reading flips:** none that pass the rubric set — "update to real current state" = held-at-Scheduled (R6 guards advance; petition-not-filed is the real state).
- **Drift sweep across all 3 files:** em-dashes 0/0/0; "at least N" 0; tool names in titles 0; cross-universe tokens (mortgage_los, stripe, keystonemortgage, brookfieldcpas, moveops, April 28, keystone, brookfield) **0 hits**. Clean.

---

## LENS 5 — Narrative-State + Action-Prescription (per-tool strictness)

**PASS.** Airtable is SoR (recc83c05d889b354, 2026-07-01) authoritative over older Linear/Slack framing — consistent. Every OE tool-parameter binding verified on the EXACT named tool in `7_Server_Tools_Details.json`:
- `slack_send_message` uses **message** (OE16) ✔ (not `text`); catalog params channel_id+message.
- `create_draft` uses **body**, draft-only, no send tool exists in gmail server (OE17) ✔.
- `save_comment` uses **issueId + body** with OPS-32 (OE15) ✔ (not internal uuid).
- `update_records_for_table` uses camelCase **baseId/tableId/records** (OE14) ✔.
- `search_records` uses **table** (OE7/10) vs `list_records_for_table`/`update` use **tableId** (OE8/9/14) ✔.
- `get_customer_balance` uses **customer** (OE3) ✔ (valid catalog param; the old `customer_id` advisory is void).
- `contacts_search_contacts` query ✔; `search_bills`/`search_invoices`/`read_invoice(invoice_id)`/`list_bases`/`list_tables_for_base(baseId)`/`list_issues(team)`/`search_threads`/`get_thread(threadId)` ✔.

No OE write to a locked/closed state (n/a — no closed fiscal periods). **OE14 keeps fldTurnStatus at selSched; no OE advances the turn beyond selSched** (R6 enforces). PASS.

---

## LENS 6 — Verifier-Fails-Spec Pre-Upload Bucket-1 risk

Per-rubric Bucket-1 simulation against `4_Verifier_Fails_Eval.md` + `12_Always_Failing_Rubrics.md`:
- **Channel/method lock-in:** none (R8/R11/R5 all offer valid alternatives; R11's #make-ready is prompt-named "our channel").
- **Evidence stricter than criterion (R0/R1/R14):** NOT Bucket-1 — L18 blessed decoy-enumeration; criterion carries the primary "approximately $" value graded first.
- **AND-bundling:** R1 (walk-back) adjudicated acceptable (same-source, single-error); R4/R12/R17 (make-ready+market) same-source single hold-disposition — splitting manufactures redundancy. Not Bucket-1.
- **"approximately" on ID/date/exact amount:** only on the three DERIVED dollar figures (allowed). None on IDs.
- **"(or similar)" on exact id/email/channel:** none. **Service metadata:** R13 draft has recipient; R11 Slack has channel — complete. **Process rubric w/ write verb:** 0 process rubrics. **Persona-scope drift:** none. **Per-rubric value ≠ OE value:** R0/R14 $1,832 = OE5/17; R1 $1,982/847/925/210 = OE5 — all match.

**Genuine Bucket-1 risk = R1 watch-item at most = 1/18 = 5.6% ≤ 20% → PASS.** (The projected all-fail set — the L31 explicit-prohibition rubrics R4/R6/R7/R12/R17 — are valid, grounded, in-scope behaviors expected to fail Gemini and pass Opus: a legitimate Bucket-3 model gap per Learnings L31, not invalid AF.)

---

## Deterministic-gate COUNCIL-notes adjudication

**Injection (PASS, 0 fails):**
- P4 fact/status/amount/timeline vs base universe — **CONFIRM no contradiction.** Every injected atom re-verified against Universe_Split; the stored 2132 Balance and 0-balance invoice are intentional decoys, internally consistent.
- P5 formality/register vs channel norms — **CONFIRM.** Slack terse/operational, Gmail formal-authorization register; matches channel norms.
- P6 tool-call chain depth >5 — **CONFIRM.** 18-step OE / ~22+ canonical calls, far exceeds 5.
- P8 injection difficulty ≥3.5 — **My read: ~4.3/5 for the dual-model set.** Flagship AP-bill structured-DB skip (empirically 0/12 both models on sibling Task 40), stacked with L10 supersession + L1 owner-latch + L11 sign + L31 Gemini negative-directive. Clears 3.5 comfortably.

**Submission gate (PASS, 0 fails, 1 warn):** under-strictness 6.3 — **CONFIRM** (derived figures + decoy enumeration are appropriately strict); exclusion coverage 6.6 — **CONFIRM** (all decoys in FAIL clauses); UGT convergence 6.8 — **CONFIRM** ($1,832 net / hold / not-filed / Linda is single-valued); OE authority 6.9 — **CONFIRM** (OE15 OPS-32 OR EVF-2026-014 dual-surface accommodation); strict feasibility 6.10 — **CONFIRM** (all tools/params exist, end-to-end feasible); date-alignment 6.11 — **CONFIRM** (today 2026-07-01 = recc83 mod date; stale fldMoveOut/fldTargetReady 2026-05-02 and 2026-07-01T14:00 batch `created_time` are intended artifacts, not misalignment).

---

## Hard-rules table

| Rule | Result |
|---|---|
| Answer-leakage ($1,832/$1,982 verbatim) | **PASS** — 0 in prompt; 0 comma-formatted in Universe_Split; 3 bare "1832" are base64/ts/hash substrings (agree with parent operator) |
| Phantom-id | **PASS** — every id/DocNumber/ticket/channel/thread/email verified to a real row |
| Lever-preservation | **PASS** — L2/L10/L1/L11/L31 (+stacked L6) all trace prompt→OE→rubric→atom |
| Density-per-model (StarPM 40+) | **PASS (projected)** — Opus ~47, Gemini ~42; trajectories empty (pre-upload), so unmeasured |
| Outcome > Process | **PASS** — 18 Outcome / 0 Process |
| Entity-consistency | **PASS** — Tanya/Linda/Patricia/Sunset Ridge consistent; Rio Bend/John Castillo/Harris only in FAIL clauses; 0 Lisa drift |
| Implicit-framing | **PASS** — persona believes frame; no rubric forces forbidden investigation or fails a correct executor |
| Per-tool binding | **PASS** — message/body/issueId/camelCase/table-vs-tableId/customer all on correct catalog tools |

---

## Per-model density projection

Trajectories are 0 bytes (task not yet run), so this is a **projection**, consistent with the Hardness_Plan (~50/~43) and the more conservative AUDIT_oe minimal-exploration sketch:
- **Opus 4.8: midpoint ~47** (band 44–52). Flagship L2 forces the bills query after invoices read clean; four conflicting eviction narratives (Airtable/Slack/Linear/Gmail) force reconciliation; 6-record supersession chain + Rio Bend/Las Palmas/catch-all disambiguation; 4 writes. **≥40 → PASS.**
- **Gemini: midpoint ~42** (band ~38–46). ~0.85× leaner traversal; sibling Task 40 empirical 47/45/37/38/33/40 (avg 40.0) on a lighter stack; this heavier stack lands slightly higher midpoint. **≥40 → PASS, margin TIGHT** (a maximally lean Gemini run can dip to high-30s; the gate is on the midpoint, which clears).
- **Breadth:** actual OE chain exercises **6 distinct services** each ≥5% (airtable ~30%, quickbooks ~20%, slack ~12%, gmail ~11%, linear ~10%, contacts ~6%; max <60%) → **PASS** (≥4 services ≥5%). Note: the Hardness_Plan's "8 services / 7 ≥5%" (incl. hubspot/gcalendar) is a benign planning over-count — the OE resolves identities via contacts, not hubspot, and never invokes gcalendar. Does not affect the gate; internal-planning artifact, not a deliverable defect.

**Both models clear the StarPM v4 ≥40 bar on projected midpoint.**

---

## Observations (non-blocking, no MAJOR)

1. **Gemini density margin is tight** (~42 midpoint; lean runs can hit high-30s). Watch the first platform run; if the measured Gemini avg dips below 40, add one disambiguation read (e.g., OPS-38/54 or C004 read) — but the midpoint clears, so no pre-upload change required.
2. **R1 (idx1) AND-bundling** is the single residual watch-item (submission_gate WARN); adjudicated acceptable walk-back composition — monitor judge behavior on the first run.
3. **Escape-valve clause** (prompt line 11, "if anything I've assumed…tell me plainly") mildly lowers difficulty but does NOT neutralize the flagship L2 (agent still must query the correct object type and derive the net); empirical Task 40 anchor (0/12 on the AP-bill arrears with comparable verify-framing) supports stump survival.

No BLOCKER hits. 0 MAJOR hits. Lens-6 Bucket-1 risk 5.6% ≤ 20%. This deliverable set is genuinely clean under adversarial reading — every atom independently re-verified from source, leakage independently re-greped and confirmed, all five levers preserved end-to-end, per-tool bindings correct against the catalog.

VERDICT: PASS

---

## ADDENDUM — Post-PASS atomicity revision (external QC feedback, 2026-07-24)

External QC feedback flagged the rubric set on **Rubrics Atomicity** (5 sub-claims). Re-adjudicated each against the governing rules (Guidelines line 333 "if two claims could plausibly fail independently, split them"; Evals_starpm/3 lines 405-415 "HARD GATE: Atomicity — Split Completely, ML-confirmed July 2026"; and the V4 QC-passed precedent):

- **Claim 1 — R[0] "$1,832 ... nets rather than adds": INVALID (defended).** "Nets rather than adds" is arithmetically entailed by the figure (adding the $150 yields $2,132), graded via the number in evidence. One independently-verifiable item.
- **Claim 2 — R[1] "$1,982 comprising $847/$925/$210": INVALID (defended).** Derived total + components from ONE bill record, meaningfully inseparable (Guidelines "same data point" exception), and directly matched by the QC-passed V4 precedent (Task2: "11 attendees at $185 each ($2,035.00) instead of 14 ($2,590.00)"). The submission_gate NOT_ATOMIC WARN is a deterministic over-flag human QC accepts; kept with documented rationale.
- **Claim 3 — R[5]+R[6] make-ready update: NON-ISSUE.** Already two separate atomic rubrics; the helper itself judged them acceptable.
- **Claim 4 — R[12] "must not mobilize AND must not be marketed": VALID (fixed).** Two distinct required content items that can fail independently (matches the "storm/city/flight" split pattern, not the coupled-facts exception). Split into make-ready-hold + no-marketing.
- **Claim 5 — R[14] "$1,832 net, not the $0 balance": INVALID (defended).** Value + decoy-contrast; "not $0" is the FAIL condition, not an independent assertion.

**Additional instances found (helper did not flag) and fixed for consistency:** the same make-ready+marketing bundle appeared in R[4] (final response) and R[17] (owner draft). R[4] simplified to the make-ready-hold claim (marketing moved to the deliverables where it belongs); R[17] split into make-ready-cannot-begin + no-marketing.

**Result:** 18 → 20 rubrics, all Outcome. Focused delta re-verification: atomicity PASS, forward-coverage no-gap PASS, OE grounding (OE16/OE17) PASS, L31 preserved/strengthened PASS, no-regression PASS. Deterministic gates re-run: validate --phase all 0 fails, submission_gate 0 fails (1 accepted WARN on R[1]), injection 0 fails. Rubric-quality: 0/20 Major.

**FINAL VERDICT UNCHANGED: PASS** (atomicity revision strengthens the rubric set; no answer/lever/entity/leakage/density impact).

---

## RE-VERIFICATION — Independent fresh-chat re-run (2026-07-24)

FINAL re-invoked in a fresh chat. Deliverables byte-identical to the prior PASS (`7_Rubrics.json` mod 19:45 predates the prior council 19:48; prompt/OE older). Prior PASS **NOT trusted** — every conclusion independently re-derived from source. NOTE: `8a/8b_Verifier_Fails` are now present in the folder (S4 inputs, gathered after the prior FINAL). Per the STOP-gate rule they are **NOT processed at FINAL** — FINAL is the pre-upload gate. No deliverable edits applied at this re-run (task already run on platform; editing artifacts would desync them from the trajectories S4 must analyze).

**Deterministic gates re-run clean:** `phase_ready --phase final` OK; `validate --phase all` 0 fails (prompt 0F/0W/5N, oe 0F/0W/3N, rubrics 0F/18W-adjudicated/5N); `validate --phase injection` 0 fails; `validate --phase submission_gate` 0 fails/1 WARN.

**Operator-side independent checks (python3/grep, not eyeballed):**
- Answer-leakage: net `1832` / gross `1982` absent from prompt; no comma-formatted `1,832`/`1,982` anywhere in `Universe_Split/`; bare `1832`/`1982` hits are all id/timestamp substrings (`…d318324…`, `1781018320000`, `.051982`, `311198205235`). `Fact_Ledger.amounts[]` holds only the `2132.00` decoy — both derived figures are derive-only. CLEAN.
- Drift: 0 em-dashes / 0 cross-universe tokens / 0 Lisa drift / 0 tool-names-in-title across all 3 deliverables. 20/20 Outcome. Decoy `2132.00` intact in QB entities.

**Fresh Final Council (independent, high-rigor, 6 lenses):** re-grounded every identifier + all 3 derived figures from source; re-mapped all 5 levers (L2/L10/L1/L11/L31) prompt→OE→rubric; re-verified per-tool param bindings against `StarPM_Base_Universe/7_Server_Tools_Details.json`. **0 BLOCKER · 0 MAJOR · 4 MINOR · Lens-6 Bucket-1 risk 5% (1/20 ≤ 20%) · injection difficulty ~4.2/5 (≥3.5).**

**4 MINORs (non-blocking; do NOT trigger REVISE; deferred, not applied):**
1. **OE 3 narrative inaccuracy (confirmed by operator):** OE 3 says `get_customer_balance`/`get_aged_receivables` "returns roughly zero." Actually the catch-all customer `proj-2e48c594aab7` carries open invoices 1055 ($2,640) + 1083 ($640) + 1087-796 ($1,240) + CM-2026-044 ($63.75) = **$4,583.75** (before credit memos). No ground-truth / rubric-grade impact (any figure ≠ ~$1,832 fails rubric 1; the $13,208.75 all-status catch-all is already a FAIL value). Suggested S2/S4 wording: "returns the unrelated catch-all AR (~$4,583.75 open / ~$13,208.75 all-status), not the rent arrears." — `6_Oracle_Events.txt:5`.
2. **Rubric 1 FAIL enumeration** could optionally add `$1,982` (gross before credit) and `~$4,583.75` (open-AR catch-all) as enumerated decoys. Already gradeable ("approximately $1,832" excludes both) — L18 optional hardening. — `7_Rubrics.json:6`.
3. **Rubric 2 ($1,982 total + $847/$925/$210 components) NOT_ATOMIC soft-WARN** — re-confirmed a legitimate single-source walk-back the prompt explicitly demands (matches QC-passed V4 precedent); keep as-is. Monitor judge on first run.
4. **Zero process rubrics (20/0)** — standard StarPM V4 outcome-heavy design; Outcome > Process satisfied.

**Per-model density (projection; trajectories not read at FINAL):** Opus ~44-46 → PASS (≥40); Gemini ~38-40 → at/just above the StarPM v4 ≥40 line (borderline PASS, consistent with the Hardness_Plan ~43 and prior council ~42). Watch-item for S4 measured density — not a blocker.

**RE-VERIFICATION VERDICT: PASS** — independent re-run reproduces the prior PASS. 0 BLOCKER, 0 MAJOR; the 4 MINORs are logged as S4/CLOSE watch-items and intentionally not applied (task already run; no gate-stage deliverable edits).
