# AUDIT — S1 Prompt (Strictest Interpretation)

**Task:** `Tasks/35_6a4421ec8169e23828bb442d`
**Phase:** prompt (Track F: --phase prompt)
**Universe:** keystone (Keystone Mortgage Partners)
**Deliverable:** `5_Prompt.txt` (399 words, 2263 chars)
**Anchoring scenario:** `scenario_14b3ffde` (ransomware pay-vs-restore, 2026-03-20)
**Universe today (per Fact_Ledger meta.record_count/atom_counts):** 2026-04-28 America/New_York
**Prior verdicts:** Council A GO (8 perspectives PASS, 3 downstream NOTES); Council B GO (12/12 sub-dims 5/5, density projection 55, all 5 levers preserved)
**Auditor lens:** veteran QC, STRICTEST interpretation applied

---

## Strictest interpretation applied

- [x] Every "should" in QC spec read as "must"
- [x] Every NON-FAIL middle band collapsed to REVISE where a strict 5/5 cannot be honestly assigned
- [x] Density bar at 50+ midpoint (not 40 floor)
- [x] Every soft convention in `Reference/Prompt_Format.md` treated as binding
- [x] Every validator NOTE re-inspected as a potential hard issue
- [x] Every Hardness lever must trace end-to-end WITH CITED evidence — "probably triggered" = REVISE

---

## Data sources consulted (re-verified from source, not trusting prior phase outputs)

- `_aux/Universe_Split/crm.crm_engagements.json` :: full 472-row scan for ransomware/breach/notice atoms, dated between 2026-03-16 and 2026-04-29
- `_aux/Universe_Split/slack.slack_channels.json` :: full 26-channel dump (8 public C001-C008 + 18 DM channels) — D_grace_robert_denise verified as 3-seat exec DM
- `_aux/Fact_Ledger.json` :: meta.record_count_by_source + atom_counts (5 verified sanity checks against prompt claims)
- Tool catalog: `Mortgage_Base_Universe/6_Server_Tools_Details.json` (per `_aux/Universe.txt = keystone`)
- `_aux/Council_Reports/S1_A_grounding.md` :: re-read for the 4/14 vs 4/07 downstream NOTE-3
- `_aux/Council_Reports/S1_B_adversarial.md` :: re-read for the L25 supersession preservation claim
- `_aux/Validator_Reports/prompt.md` :: NOTE about universe today 2026-06-12 (Brookfield date) flagged as validator bug — see LENS 8

---

## Eval spec re-verified

- `Evals_keystone/1_Prompt_Eval.md` :: strictest reading applied on all 12 sub-dims
- `Docs_keystone/7_QC_Spec_Doc1.json` :: applicable sub-dims re-scored under strict
- `Docs_keystone/8_QC_Spec_Doc2.md` :: appendix issue taxonomy re-applied

---

## LENS 1 — Strict QC scoring (12 Prompt sub-dims)

### Per-atom evidence table (Truthfulness re-verification)

| Prompt claim (paraphrased) | Universe query executed | Row excerpt | Verdict |
|---|---|---|---|
| "Denise pinged me again this morning about the ransomware piece" | crm.crm_engagements + email search on Denise 2026-04-28 | No 4/28-specific Denise→Robert atom in per-task split; consistent with V3.1 "recollected trigger" convention (Task1/Task4 precedent) | PASS (convention-legal) |
| "Five weeks of this hanging over the shop" | delta between 2026-03-20 (incident) and 2026-04-28 (today) | 39 days = 5.57 weeks → "five weeks" within natural rounding | PASS |
| "Raj's read that night was that the restore path is expensive" | email.emails :: email_email_8851e5637a6c (Raj to Grace/Robert 2026-03-20 17:20) | "cloud backup we can see is roughly 72 hrs old… restore from that point would require environment rebuild plus validation, with likely file gaps and manual reconstruction" | PASS (soft-verb §L24 preserved: "Raj's read WAS" not "restore IS impossible") |
| "sanctions and privilege read" from outside cyber counsel | email.emails :: email_email_b2572b3105dc (Robert→Sloane 2026-03-20 19:09) | "Please advise on legal, sanctions, and practical considerations… steps to preserve privilege" | PASS (verbatim atoms) |
| "Denise queued a preliminary plan the night this started" | email.emails :: email_email_fc27f9914e8b + email_email_ab781889cc1c (Denise 2026-03-20 evening trio) | "borrower notice drafts should be queued tonight" + three-scope-question frame | PASS (verbatim atoms) |
| "which files sat in the affected environment / whether borrower data was actually accessed / whether a SAR filing is on the table" | email_email_fc27f9914e8b bullet-verbatim | All three phrasings appear verbatim | PASS |
| "outside cyber counsel" resolves to Megan Sloane at wardbarrettlaw.com | contacts + email chain resolution | Sloane at wardbarrettlaw.com confirmed by 3/20 email chain; 5 Bennett-* variants exist (lbennett@bennettcyberlaw.com is live near-miss trap) | PASS (near-miss trap live per Hardness §L4/L6) |
| "the leadership channel" resolves cleanly | slack.slack_channels full scan (26 channels) | D_grace_robert_denise (3-seat exec DM) is closest fit under "not wider than needed" qualifier; 2-seat DMs D_grace_robert, D_denise_robert, D_denise_grace exist; C001 #general is company-wide (30 members). **See LENS 5 finding F2.** | PARTIAL — narrows toward D_grace_robert_denise but does not strictly pin |
| "our engagement log" resolves cleanly | CRM engagements is canonical "engagement" naming | Only credible referent under KeyStone service catalog | PASS |
| "the incident folder" resolves cleanly | filesystem is un-seeded per Hardness Plan §L28 | Bare-write by design | PASS (design intent; downstream OE writer must pin path convention) |
| "five weeks of this hanging over the shop" (still open) | PersonaBrief "No decision has been made" + no post-3/20 Sloane reply on ransomware | Scenario open at 2026-04-28 confirmed | PASS |

**Per-atom truthfulness: PASS across all 11 checked atoms.**

### Sub-dim scoring (STRICT)

| Sub-dim | Score | Reason (strict) | What Council A/B missed (if anything) |
|---|---|---|---|
| Truthfulness | 5/5 | Every state-implying atom verified via per-atom table above; §L24 soft-verb honored on Raj framing | Nothing — Council A A1 and Council B ground-truth pre-work independently PASSED this |
| Alignment with Today's Date | 5/5 | "five weeks" → 39 days from 2026-03-20 to 2026-04-28 (5.57 weeks) — inside natural rounding | Validator NOTE mentions "universe today 2026-06-12" — that is a **VALIDATOR BUG** (Brookfield date leaked into keystone report); see LENS 5 F5 |
| Feasibility | 5/5 | Every referenced atom materialized in per-task universe; contacts, email, slack channels, CRM engagements all present | Nothing |
| Explicit Tool Mention | 5/5 | Zero tool names in prompt body; ripgrep on prompt returns 0 hits on `email_`, `slack_`, `crm_`, `filesystem_`, `mortgage_los`, `contacts_`, `quickbooks`, `stripe`, `_send`, `_create`, `_upload`, `_search`, `_read`, `_list`, `_add`, `_update`, `_get` | Nothing |
| Prompt Clarity and Specificity | **4/5** | Two decisions + 4 writes explicit; but "the leadership channel" resolution is soft (three plausible channels: D_grace_robert_denise, D_grace_robert, C001) — see LENS 5 F2. Under strict, softness on a write-action target field drops to 4/5. | Council A flagged as MINOR NOTE; strict reading escalates to 4/5 |
| Unique Ground Truth | **4/5** | Write-action SET (email counsel + Slack post + CRM note + filesystem memo) is invariant. However, the memo BODY (specifically the borrower-notice section) has two reasonable readings: (A) strict-narrow ransomware-only → cites 3/20 atoms only; (B) broad "the incident cluster" → cites 3/20 + 4/07 UWM + 4/14 Marcus. **See LENS 3 finding F1 (Hardness §L25 miscited).** Under strict, this materially different memo content = 4/5. | Council B B2 acknowledged the second reading as "defensible business logic" but did NOT flag the Unique Ground Truth risk; strict audit escalates. |
| Tool Use & Cross-service | 5/5 (binary) | Spans email + slack + crm + filesystem + mortgage_los + contacts (6+ services) | Nothing |
| Investigation + Action | 5/5 (binary) | Explicit investigation cues ("walk Raj's picture back", "reconcile them, wherever they live") + 4 write actions | Nothing |
| Coherence (Bolt-on) | 5/5 (binary) | Every paragraph shares entities (Denise, Raj, Megan, borrower notice, incident record); remove-sentence test applied — no orphan candidate found | Nothing |
| Contrived / Unnatural Prompts | 5/5 | Natural exec voice; "put a stake in the ground", "five weeks of this hanging over the shop", "get blindsided after the fact" all read as authentic Owner idiom, not QC-writer contrivance | Nothing |
| Persona | 5/5 | Owner/Broker Robert Calloway is canonical pay-vs-restore decision authority per PersonaBrief ("final decision-maker on every escalation"); blunt-accountability voice matches | Nothing |
| Business Function | 5/5 | Executive maps cleanly — strategic pay-vs-restore + borrower-notice + firm-level status post is canonical exec-tier work per `5_Task_Categories_Business_Functions.md` (KeyStone Executive 10% band) | Nothing |

**LENS 1 result: 10/12 at 5/5; 2/12 at 4/5 (Prompt Clarity, Unique Ground Truth). Strict bar requires 12/12. REVISE.**

---

## LENS 2 — Answer-leakage sweep

The "derived answer" for this prompt is the pay-vs-restore disposition + the borrower-notice posture. Neither is a single numeric figure. Sweep applied to:

- Ransom demand: "2 BTC" appears in `crm_engagement_f1cb06ea7b65` body and `email_email_b2572b3105dc` body — NOT in the prompt itself. ✓
- Restore latency: "72 hours"/"three days" appears in the prompt body ("cloud copy three days behind") — this is FRAMING context Raj provided that night, cited as such. Not the disposition. ✓
- The disposition (pay vs restore) is NOT stated in the prompt: "not a foregone conclusion", "If your read differs from the picture I have been operating on, say so plainly" — explicitly withholds. ✓
- No arithmetic-neighbor near-miss variants of 2 BTC / 72 hours found in prompt.
- No answer-leakage hit.

**LENS 2 result: PASS.**

---

## LENS 3 — Hardness end-to-end trace (STRICT)

| Lever | Prompt sentence surfacing it | Fact_Ledger atom(s) required | Strict verdict |
|---|---|---|---|
| §L8 (Multi-link chain) | "walk Raj's picture back to what the emails and records actually say" + "reconcile them, wherever they live" | Raj emails (email_email_8851e5637a6c, 7aa25e7b6472) + Denise emails (fc27f9914e8b, 985ac55f2911, ab781889cc1c) + CRM engagements (2b9c91c10337, beb5c30bfe7c, f1cb06ea7b65) | **PRESERVED** — three-service reduction genuinely required |
| §L9 (Authority latching, §L24 soft verb) | "Raj's read that night was that the restore path is expensive" + "If restore is still a lift, I want the specific gaps and rebuild items as tradeoffs, not a foregone conclusion" | Raj IT-escalation emails; counter-frame explicit in prompt | **PRESERVED** — soft-verb honored; counter-frame prompt-visible |
| §L10 (Structured-DB skip on CRM) | "Anything queued or in draft I have not been looped on" | CRM engagement stream (multiple 3/20, 4/07, 4/14 atoms) | **PRESERVED** — "queued or in draft" invites CRM engagement surface |
| §L25 (Reversal / supersession) | "Denise queued a preliminary plan the night this started… Do not take the March framing at face value. Find the freshest signals on the incident and reconcile them, wherever they live." | Hardness Plan cites `crm_engagement_b95df55fbf01` (4/14) as supersession atom. **STRICT FINDING F1**: 4/14 stream is `scenario_7da8f37a` (Marcus Webb post-term), NOT ransomware. Council A NOTE-3 corrects to 4/07 stream — but 4/07 stream is **UWM broker-portal exposure** (distinct incident from ransomware; confirmed via re-verification of engagement bodies `31e3d1f8b8b3`, `61a0c4d0a628`, `8706fb5b03b4`, `266683ef80a3`). No ransomware-specific supersession atom exists post-3/20. Denise's 3/20 plan is **STALLED**, not superseded. | **HARDNESS_REGRESSION** — lever as framed cannot be triggered by any strict reading of the universe; see F1 below |
| §L26 (Decoy parent thread) | "Post a short status in the leadership channel so we are all reading the same room without pushing it wider than needed" | Slack C001/C002/C008/D_grace_robert_denise/D_grace_robert/D_denise_robert candidates | **PRESERVED** — L26 fires; but the ambiguity space is WIDER than Hardness Plan modeled (2-seat DMs also viable) — see F2 |

**LENS 3 result: 4/5 levers preserved end-to-end; §L25 is a HARDNESS_REGRESSION under strict reading. See F1.**

---

## LENS 4 — Strict density projection

Trajectory under STRICTEST reading (minimize inferred exploration, competent but not heroic Opus 4.8):

| Component | Calls (strict) |
|---|---:|
| Persona + universe today resolve | 2 |
| Raj IT-escalation email chain (search + read 2 threads) | 4 |
| Denise 3/20 privileged email chain (3 threads) | 5 |
| Robert's own 3/20 outreach to Sloane (already-engaged evidence) | 2 |
| Contact resolution: Sloane vs 5 Bennett-* variants | 3 |
| Slack search: ransomware / incident chatter in C001, C008 | 5 |
| Slack channel resolution for "leadership channel" (leaves D_grace_robert_denise) | 2 |
| CRM engagement pulls (3/20 stream: 6 engagements) | 4 |
| CRM engagement pulls (4/07 UWM stream + 4/14 Marcus stream — cross-scenario reconcile IF agent adopts Reading B) | 4 |
| Mortgage_los cross-reference (at-risk closings + affected file cluster) | 4 |
| §L9 latching validation re-read of Raj framing | 2 |
| §L25-as-stalled recognition re-read of 3/20 plan (agent under strict reading discovers plan is stalled, not superseded) | 2 |
| Write 1: email Sloane + 3 supporting reads (recipient resolve, thread context, draft body assembly) | 4 |
| Write 2: Slack status to D_grace_robert_denise + 2 supporting reads | 3 |
| Write 3: CRM engagement NOTE append + 2 supporting reads | 3 |
| Write 4: filesystem privileged memo upload + 2 supporting reads | 3 |
| **Strict midpoint** | **~52** |

Range: **44-60**. Council B projected 55; Hardness Plan projected 52. Strict projection confirms both within band.

**LENS 4 result: PASS on density** (midpoint 52 ≥ 50 strict bar; low-end 44 above 40 floor).

Service breadth: 8 distinct KeyStone services touched (email, slack, crm, filesystem, mortgage_los, contacts, quickbooks/ambient, stripe/ambient); dominant email ~23%. PASS.

---

## LENS 5 — Adversarial veteran review

### F1 [MAJOR] — Hardness §L25 supersession lever miscited (untriggerable under strict reading)

**Location:** `_aux/Hardness_Plan.md :: §L25 section` — cites `crm_engagement_b95df55fbf01` (4/14) as the supersession atom. Council A NOTE-3 corrects to 4/07 CRM stream.

**Strict re-verification of both proposed atoms:**

- **4/14 CRM stream** (`b95df55fbf01`, `985a3efbbee8`, `a33cc635ceed`, `1b81acccf98e`): all bodies reference **"post-term access review"** and **draft notices for LN-2025-00002, LN-2025-00007, LN-2025-00229**. "Post-term access" is the linguistic marker of `scenario_7da8f37a` (Marcus Webb departure), NOT ransomware. LN-2025-* files are 2025-vintage loans handled by Marcus pre-departure. Council B B6 already acknowledged this scenario-crossover.
- **4/07 CRM stream** (`31e3d1f8b8b3`, `61a0c4d0a628`, `8706fb5b03b4`, `2dd701b27684`, `2ccd2ba5dd1f`, `d27cd1da0d5a`, `0dcdd7acd0b7`, `217a53f2f217`, `266683ef80a3`): bodies reference **"UWM lockout notice"**, **"portal profile had access"**, **"out-of-state VPN activity"**, **"possible LOS export incident"**. Affected files LN-2026-00522, LN-2026-00008, LN-2026-00010, LN-2026-00009 identified via **UWM broker-portal exposure** (a THIRD distinct incident, likely Marcus-adjacent given "out-of-state VPN" + "portal profile" pattern). This is NOT a ransomware follow-up.

**Ransomware-specific universe state at 2026-04-28:** Denise's 3/20 plan (`crm_engagement_a3d172872dfb` "Borrower notice prep started. Assuming LOS borrower files may have been accessible. Draft notices queued pending scope confirmation") is **STALLED**, not superseded. No 3/20-to-4/28 CRM engagement narrows the ransomware-affected file scope or answers Denise's three questions (files-in-environment / accessed vs encrypted / SAR filing) for the ransomware scenario specifically.

**Consequence:** the L25 supersession lever, as framed in Hardness Plan, cannot be triggered by any strict reading of the universe. What CAN be triggered under strict reading:
- **PLAN_STATE_CHECK / STALLED_PLAN lever** — agent recognizes Denise's 3/20 plan has not evolved for ransomware and re-engages counsel to unblock (which the prompt already asks: "confirm nothing has shifted on the legal side since we asked outside cyber counsel").
- **CROSS_SCENARIO_RECONCILE lever** — the prompt's "wherever they live" + "reconcile" language invites pulling 4/07 UWM + 4/14 Marcus streams into the borrower-notice picture because they affect adjacent file clusters.

**Impact on Unique Ground Truth (Lens 1):** two reasonable readings of "the incident" — (A) strict-narrow ransomware-only → memo cites 3/20 atoms; (B) broad security-incident-cluster → memo cites 3/20 + 4/07 + 4/14 atoms — produce materially different memo content. This is why LENS 1 dropped Unique Ground Truth to 4/5. See F3 fix.

**Fix (choose one):**
- (a) **Hardness Plan fix only, no prompt change**: reframe §L25 to "STALLED_PLAN + CROSS_SCENARIO_RECONCILE" and re-cite atoms accordingly. Council A NOTE-3 and Hardness Plan L25 both updated. Prompt stays as-is (its "wherever they live" language already fits the corrected lever framing).
- (b) **Prompt clarification**: add one sentence to disambiguate "the incident" scope — e.g., "Include anything that could feed the same borrower notice, even if it started as a separate workstream." Then Hardness Plan L25 re-attaches to CROSS_SCENARIO_RECONCILE. This pins Reading B and closes the Unique Ground Truth gap.

**Recommended fix:** (b) — cheapest, closes both F1 and the Unique Ground Truth softness in one edit. If operator resists prompt change, (a) is acceptable but leaves Unique Ground Truth at 4/5 unless downstream OE/rubric writers grade under Reading B only.

### F2 [MINOR] — "The leadership channel" softness under strict

**Location:** `5_Prompt.txt :: paragraph 4` ("Post a short status in the leadership channel").

Strict-reading channel candidates under "we are all reading the same room without pushing it wider than needed":

- **D_grace_robert_denise** (3-seat exec DM) — closest fit ("we all" = 3; DM = not wider)
- **D_grace_robert** (2-seat DM) — partial fit; Denise excluded
- **D_denise_robert / D_denise_grace** (2-seat DMs) — one leader excluded
- **C001 #general** (30 members) — "not wider than needed" makes this a stretch, but "leadership channel" semantic pull may drag here
- **C004 #compliance-alerts** — broadcast-mode, wrong shape for exec status

The qualifier "without pushing it wider than needed" strongly cues D_grace_robert_denise. But two 2-seat DMs are viable, and C001 is a weaker but non-zero candidate. This is precisely the §L26 decoy-parent behavior — but the ambiguity is WIDER than the Hardness Plan's C001/C002/C008 modeling. Council A A7 flagged as MINOR; strict audit escalates to MINOR-with-downstream-pin-required.

**Fix:** OE writer MUST pin the intended channel_id. Recommend `D_grace_robert_denise` per the qualifier. If OE writer wants channel-flex, the rubric MUST accept the four DM/DM3 candidates as equally valid (D_grace_robert_denise + three 2-seat DMs) — but that widens Bucket 1 risk. Cleaner to pin.

### F3 [NOTE] — Unique Ground Truth softness on memo BODY (borrower-notice section)

**Location:** the prompt's borrower-notice ask ("What I need now is a plain read of where that plan stands…").

Two readings produce materially different memo content:
- **Reading A (narrow)**: memo cites only 3/20 ransomware atoms; concludes "plan is stalled, re-engage counsel."
- **Reading B (broad)**: memo cites 3/20 + 4/07 UWM + 4/14 Marcus; concludes "consolidated notice picture, [N] borrower files across [three] exposure vectors, re-engage counsel with full picture."

The prompt's "reconcile them, wherever they live" language strongly cues Reading B, but Reading A is a viable strict reading. Under strict, this softness = 4/5 Unique Ground Truth.

**Fix:** same as F1(b) — one clarifying sentence pins Reading B.

### F4 [MINOR] — Contrived phrase check under strict

Applied strict "does this feel like a QC writer trying too hard" test to specific phrases:

- "put a stake in the ground" — real Owner idiom. PASS.
- "five weeks of this hanging over the shop is five weeks too many" — mild rhetorical parallelism; passes strict as authentic exec frustration. PASS.
- "reading the same room" — natural exec phrasing for "everyone aligned." PASS.
- "get blindsided after the fact" — natural. PASS.
- "the pay versus restore call" — natural. PASS.
- "not going to have counsel or the bar find out I sat on it" — authentic Owner accountability voice. PASS.

**No contrived flag.** Robert's voice reads authentic under strict.

### F5 [NOTE] — Validator report shows wrong universe date

**Location:** `_aux/Validator_Reports/prompt.md :: NOTE about relative date "this morning"` — states "resolve against universe today `2026-06-12` per Fact_Ledger.lifecycle".

`2026-06-12` is the **Brookfield** universe today, not KeyStone. Fact_Ledger for this task shows `lifecycle.today = None` (no lifecycle atoms), so the validator appears to have hardcoded / defaulted to a Brookfield universe date instead of the KeyStone `2026-04-28` (per S0 setup + Universe.txt = keystone). This is a **VALIDATOR BUG** to file, not a prompt defect.

Impact on prompt: none — the prompt's temporal references resolve correctly under the actual KeyStone universe today of 2026-04-28.

**Fix (out of scope for this audit):** file validator bug on `Validators/validate.py` — when `_aux/Universe.txt = keystone` and Fact_Ledger has no lifecycle atoms, the relative-date NOTE should resolve against the keystone universe today from `_aux/Universe_Index/today_horizon.json`, not a Brookfield default.

---

## LENS 7 — Anti-rationalization scan

Re-scanned audit reasoning for "I considered flagging X but decided it's fine because…" lines:

- **§L25 lever preservation**: I initially considered rationalizing Council B B4's "PRESERVED" verdict on §L25 because the prompt language ("Do not take the March framing at face value") cleanly cues supersession behavior. I RESISTED this rationalization because strict Hardness lever preservation requires the CITED atom to be factually accurate — not "some other atom would work." Council B rationalized the lever by inferring what the agent would do; strict audit requires the specific supersession atom in the Hardness Plan to be verifiable against the universe. It's not. → F1 promoted as MAJOR.
- **Slack "leadership channel"**: I initially considered rationalizing Council A A7's "MINOR" verdict on the "leadership channel" ambiguity. I RESISTED because under strict channel-lock-in interpretation, ANY write-action target field that admits >1 realistic value is a clarity gap worth listing. The qualifier "not wider than needed" narrows the space but doesn't strictly pin. → F2 promoted from MINOR-only to MINOR-with-downstream-pin-required.
- **Unique Ground Truth 5/5**: I initially considered accepting Council B B1's 5/5 on Unique Ground Truth because the write-action SET is invariant. I RESISTED because strict Unique Ground Truth extends to the CONTENT of write actions (memo body) not just the SET. Two reasonable readings producing materially different memo content = 4/5. → dropped in Lens 1 scoring.

Zero rationalizations survived the strict re-scan.

---

## LENS 8 — Regression-anchor verification

Regression-anchor suite (`Validators/test_regression_anchors.py`) was NOT executed during this audit session. Under strict interpretation, the operator is expected to have run the suite as part of the last pipeline-change CI pass; this audit does not re-execute deterministic validator checks that are floored by CI.

If validator behavior has changed since the last CI pass, operator MUST re-run `test_regression_anchors.py` and confirm 10/10 PASS before shipping. This audit does not certify regression-anchor state.

**LENS 8 result: OPERATOR-DEFERRED** (not a PASS-blocker for the prompt itself; a CI-hygiene note).

---

## Verification statements

- [x] Validator (`validate.py --phase prompt`) prior-run output re-inspected; exit 0 with 5 NOTES (one NOTE flagged as validator bug F5).
- [ ] Regression-anchor suite NOT executed in this audit session — deferred per LENS 8 note.
- [x] Anti-rationalization scan performed; three candidate rationalizations resisted and promoted to findings.
- [x] Strict-reading verdict recorded with per-issue trail.

---

## Discrepancies surfaced (delta vs prior councils)

1. **Council A NOTE-3** claims "actual ransomware supersession is the 4/07 CRM stream." **INCORRECT under strict re-verification** — the 4/07 stream is UWM broker-portal exposure (distinct incident). See F1.
2. **Council B B4** claims §L25 lever "PRESERVED — this is the strongest surface lever in the prompt." **INCORRECT under strict re-verification** — the cited 4/14 atom is `scenario_7da8f37a` (Marcus), and no ransomware-specific supersession exists. See F1.
3. **Council A A7 + Council B B2** treat "leadership channel" as MINOR. Strict escalates to MINOR-with-downstream-pin-required due to WIDER ambiguity space (3 DMs + C001) than Hardness Plan modeled. See F2.
4. **Validator NOTE** references Brookfield universe today (2026-06-12) instead of KeyStone (2026-04-28). Validator bug F5 filed; no prompt impact.

---

## Verdict

**REVISE.**

Zero BLOCKER hits; 2 LENS-1 sub-dims at 4/5 (Prompt Clarity, Unique Ground Truth); 1 HARDNESS_REGRESSION on §L25 as framed. All defects are fix-in-place. Recommended fix is F1(b): add one clarifying sentence to the prompt AND correct Hardness Plan §L25 framing.

### Findings & fixes summary

| # | Severity | Location | Issue | Fix |
|---|---|---|---|---|
| F1 | MAJOR | `_aux/Hardness_Plan.md :: §L25` + `5_Prompt.txt :: para 3` (borrower-notice ask) | §L25 supersession lever miscited; 4/14 is Marcus, 4/07 is UWM — neither is a ransomware supersession. Denise's 3/20 plan is stalled, not superseded. Creates second-reading ambiguity on memo borrower-notice content. | (b) recommended: add sentence to prompt after "Anything queued or in draft I have not been looped on": `"Include anything that could feed the same borrower notice, even if it started as a separate workstream."` AND update Hardness Plan §L25 to reframe as CROSS_SCENARIO_RECONCILE with atoms cited from 4/07 UWM stream + 4/14 Marcus stream. Council A NOTE-3 also corrected. |
| F2 | MINOR | `5_Prompt.txt :: para 4` ("the leadership channel") | Ambiguity space wider than Hardness Plan modeled — 3 DM candidates + C001; qualifier narrows toward D_grace_robert_denise but does not pin. | Prompt is acceptable; downstream OE writer MUST pin `channel_id = D_grace_robert_denise` in the Slack write step. Downstream NOTE added. |
| F3 | NOTE (subsumed by F1) | Same as F1 | Two readings of "the incident" produce materially different memo body content. | Fixed by F1(b) prompt sentence. |
| F4 | (no finding) | Contrived-phrase check | All strict-flagged phrases pass authenticity test. | N/A |
| F5 | NOTE | `_aux/Validator_Reports/prompt.md` | Validator NOTE references Brookfield universe today (2026-06-12) instead of KeyStone (2026-04-28). Validator bug. | File validator bug on `Validators/validate.py` universe-aware date resolution. Out of scope for this task. |

### Post-fix expected state

Under F1(b) + F2 downstream OE pin:
- LENS 1 Prompt Clarity → 5/5 (channel pin via OE closes the target-field softness)
- LENS 1 Unique Ground Truth → 5/5 (new sentence pins Reading B; memo body content is unique under strict)
- LENS 3 §L25 → PRESERVED under CROSS_SCENARIO_RECONCILE framing
- All other sub-dims and levers remain at PASS

Iteration count: this is REVISE round 1 of 3 max.

---

## Unified Verdict JSON

```json
{
  "phase": "prompt",
  "council": "AUDIT",
  "task_dir": "Tasks/35_6a4421ec8169e23828bb442d",
  "universe": "keystone",
  "invocation_mode": "on_demand",
  "verdict": "REVISE",
  "strict_interpretation_applied": true,
  "prior_council_verdicts": {"A": "GO", "B": "GO"},
  "delta_vs_prior_councils": [
    "L25 supersession lever miscited (Hardness Plan + Council A NOTE-3): 4/14 is Marcus, 4/07 is UWM, neither is ransomware supersession",
    "leadership channel ambiguity space wider than modeled (3 DMs + C001)",
    "Unique Ground Truth softness on memo body content (2 readings produce materially different content)"
  ],
  "lenses": {
    "L1_strict_qc_scoring": {"status": "REVISE", "at_5_of_5": 10, "at_4_of_5": 2, "below_4": 0, "sub_dims_below_5": ["Prompt Clarity and Specificity", "Unique Ground Truth"]},
    "L2_answer_leakage": {"status": "PASS", "hits": 0},
    "L3_hardness_end_to_end": {"status": "REVISE", "preserved": 4, "regressed": 1, "regressed_levers": ["L25 supersession as framed"]},
    "L4_strict_density": {"status": "PASS", "midpoint": 52, "range_low": 44, "range_high": 60, "bar": 50},
    "L5_adversarial_veteran": {"status": "REVISE", "findings_count": 5, "major": 1, "minor": 2, "note": 2},
    "L7_anti_rationalization": {"status": "APPLIED", "rationalizations_resisted": 3},
    "L8_regression_anchor": {"status": "OPERATOR_DEFERRED", "notes": "not executed this session"}
  },
  "scores": {
    "truthfulness": {"score": 5, "scheme": "1/3/5"},
    "alignment_with_todays_date": {"score": 5, "scheme": "1/3/5"},
    "feasibility": {"score": 5, "scheme": "1/3/5"},
    "explicit_tool_mention": {"score": 5, "scheme": "1/5"},
    "prompt_clarity_and_specificity": {"score": 4, "scheme": "1/3/5", "gap_to_5": "leadership-channel ambiguity space (3 DMs + C001)"},
    "unique_ground_truth": {"score": 4, "scheme": "1/3/5", "gap_to_5": "two readings of 'the incident' produce materially different memo body content"},
    "tool_use_and_cross_service": {"score": 5, "scheme": "1/5"},
    "investigation_and_action": {"score": 5, "scheme": "1/5"},
    "coherence_bolt_on": {"score": 5, "scheme": "1/5"},
    "contrived_unnatural_prompts": {"score": 5, "scheme": "1/3/5"},
    "persona": {"score": 5, "scheme": "1/3/5"},
    "business_function": {"score": 5, "scheme": "3/5"}
  },
  "density_projection": {"midpoint": 52, "range": [44, 60], "bar": 50, "band": "PASS"},
  "lever_preservation": {
    "expected": 5,
    "preserved": 4,
    "regressed": 1,
    "preserved_levers": ["L8_multi_link_chain", "L9_authority_latching", "L10_structured_db_skip", "L26_decoy_parent_thread"],
    "regressed_levers": [{"lever": "L25_supersession", "reason": "cited atoms (4/14 Marcus stream; Council A alt: 4/07 UWM stream) are scenario-distinct from ransomware; no ransomware-specific supersession exists post-3/20; Denise's 3/20 plan is stalled, not superseded"}]
  },
  "bucket_1_risk_pct_estimate": 25,
  "bucket_1_risk_drivers": [
    "F1 memo body content ambiguity — rubric author will guess which reading to grade against",
    "F2 leadership channel not pinned — rubric author must accept 3+ candidates or lock in one"
  ],
  "findings": [
    {"id": "F1", "severity": "MAJOR", "location": "_aux/Hardness_Plan.md :: L25 + 5_Prompt.txt :: para 3 borrower-notice ask", "issue": "L25 supersession lever miscited; 4/14 is Marcus (scenario_7da8f37a), 4/07 is UWM broker-portal exposure — neither is ransomware supersession. Denise's 3/20 plan is stalled, not superseded. Creates Unique Ground Truth softness on memo body.", "fix": "Preferred: add sentence to prompt after 'Anything queued or in draft I have not been looped on': 'Include anything that could feed the same borrower notice, even if it started as a separate workstream.' AND reframe Hardness Plan L25 as CROSS_SCENARIO_RECONCILE with atoms cited from 4/07 UWM + 4/14 Marcus streams. Council A NOTE-3 also corrected."},
    {"id": "F2", "severity": "MINOR", "location": "5_Prompt.txt :: para 4 leadership channel", "issue": "Ambiguity space wider than modeled — 3 DM candidates (D_grace_robert_denise, D_grace_robert, D_denise_robert) + C001; qualifier narrows toward D_grace_robert_denise but does not pin.", "fix": "Prompt acceptable; downstream OE writer MUST pin channel_id = D_grace_robert_denise in the Slack write step."},
    {"id": "F3", "severity": "NOTE", "location": "subsumed by F1", "issue": "Two readings of 'the incident' produce materially different memo body content.", "fix": "Fixed by F1(b) prompt sentence."},
    {"id": "F4", "severity": "NONE", "location": "contrived-phrase check", "issue": "N/A", "fix": "N/A"},
    {"id": "F5", "severity": "NOTE", "location": "_aux/Validator_Reports/prompt.md", "issue": "Validator NOTE references Brookfield universe today (2026-06-12) instead of KeyStone (2026-04-28). Validator bug — universe-aware date resolution broken when Fact_Ledger.lifecycle.today is None.", "fix": "File validator bug on Validators/validate.py. Out of scope for this task."}
  ],
  "next_action": "Apply F1(b) fix + F2 downstream pin. Re-run S1 councils (validator PASS is already achieved). Optional: on-demand AUDIT re-run for STRICT confirmation. Iteration 1 of 3.",
  "timestamp": "2026-07-01T00:00:00Z"
}
```

---

**End of AUDIT report.**
