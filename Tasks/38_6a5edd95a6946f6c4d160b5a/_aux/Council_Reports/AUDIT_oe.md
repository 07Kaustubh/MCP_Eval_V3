## AUDIT R2 -- Oracle Events Phase
### Task: 38_6a5edd95a6946f6c4d160b5a

**Round:** 2 (post-REVISE re-audit) · **Reviewer:** Strict Veteran QC · **Bar:** 5/5 only, density 50+ design target / 40 absolute floor.

Inputs re-read: `6_Oracle_Events.txt` (31 OEs), `S2_A_grounding_R2.md` (GO), `S2_B_adversarial_R2.md` (GO, midpoint 43 THIN_DENSITY), `Hardness_Plan.md` (projected 50.0 midpoint), `5_Prompt.txt` (4 asks).

---

#### A. Density

Independent recount from the file (strict floor):

| OE | Min calls | Note |
|---|---|---|
| OE3 | 3 | list_bases + list_tables_for_base + search_records |
| OE17 | 2 | get_thread × 2 (a293b24b7f85b0f0 + df187f8cb5c2b3f6) |
| OE1, OE2, OE4-OE16, OE18-OE31 | 1 each | 29 OEs × 1 |

**Lower** = 3 + 2 + (29 × 1) = **34**

Hardness-lever + realistic-exploration inflation (strict-conservative reading of Council B's inflation table):

| Source | Strict Δ | Justification (STRICT) |
|---|---|---|
| L9 Tony dismissal re-verification | +2 | Re-read of Tony Slack post-Alamo + tony.reyes email diff |
| L11 broad bill search before targeting | +2 | search_bills sweep beyond the two named DocNumbers |
| L6 Unit 14 decoy sweep | +3 | 6 decoy MR records + 2 decoy Slack messages force ≥2-3 individual retrievals |
| L8 5-hop chain re-reads | +2 | Re-reads of earlier threads once chain closure surfaces |
| L2 structured-DB skip probes | +2 | Slack/Gmail probes for roof / 208B before Airtable/QB |
| General nav / contact re-verify / Linear team orientation | +4 | Pete Donovan / Gabriella Torres contact lookups; Linear workspace orientation before save_issue |
| **Total** | **+15** | Strict-conservative (below Council B's +18) |

**Upper** = 34 + 15 = **49**
**Midpoint** = (34 + 49) / 2 = **41.5**

Council B computed midpoint **43** using +18 inflation. My strict recount yields **41.5**. Both midpoints clear the 40 floor. Neither meets the 50 design target.

| Metric | Value |
|---|---|
| Lower bound | 34 |
| Upper bound (strict) | 49 |
| Midpoint (strict) | **41.5** |
| Hardness Plan projected | 50.0 |
| 50+ design target | Not met |
| 40+ absolute floor | **Met** |

**Verdict: THIN_DENSITY** (40 ≤ midpoint < 50; NOT a blocker per project rule #11 given explicit Hardness Plan justification carries forward).

---

#### B. Tool Accuracy

Direct-read verification against `6_Oracle_Events.txt`:

| Trap | OE | Observed | Verdict |
|---|---|---|---|
| Gmail draft body param (`body` not `content`) | OE31 L61 | `body: full update covering all three items` | **PASS** |
| Linear team param (`team` not `teamId`) | OE25 L49 | `team: "OPS" or the Operations team identifier` | **PASS** |
| Airtable update param (`tableId`) | OE8 L15 | `tableId: "tblMaintenanceTickets"` | **PASS** |
| Airtable search param (`table` not `tableId`) | OE3 L5, OE10 L19, OE11 L21, OE26 L51, OE27 L53, OE28 L55 | All 6 use `table:` | **PASS** |
| Slack text param (`message` not `payload`/`text`) | OE9 L17 | `message: informing the team...` | **PASS** |
| Slack channel_id | OE9 L17 | `channel_id: "C001"` | **PASS** |
| Gmail draft-only enforcement | OE31 | Draft only; no send tool invoked | **PASS** |
| `get-bill` (hyphen convention) | OE19, OE20 | Both use `get-bill` | **PASS** |

Zero regressions from the R1 fix. R1 blocker (`search_records ... tableId`) fully remediated. All 31 tool names resolve to `7_Server_Tools_Details.json`. All StarPM-specific param traps observed correctly per the StarPM registry entry in AGENTS.md.

**B verdict: PASS.**

---

#### C. Write-Action Completeness

Four write-action OEs; strict Outcome 1.1/1.2 path check:

| OE | Write | Verifiable atoms present | Outcome path |
|---|---|---|---|
| **OE8** | update_records_for_table on rec7f6e5d4c3b2a1e | record_id, compressor-failure field update, supersedes dirty-filter | Outcome 1.1 clear |
| **OE9** | slack_send_message to C001 | channel_id, compressor-failure correction, MT-2026-063 reference | Outcome 1.1 + 1.2 clear |
| **OE25** | save_issue (Linear, new issue) | team=OPS, title, description covering $8,400 single-scope + 2 bills same job + invoice 2026-494 + $640 applied elsewhere + owner-approval thread ref | Outcome 1.1 clear (new-issue path correctly chosen since OE24 confirms no existing Ridgeview roof issue) |
| **OE31** | create_draft to aurora.winona@starpm.com | to[], subject, body integrating all 3 items with correct atoms (compressor failure; $8,400 net w/ pass-through explanation + $640 elsewhere; Las Palmas 4B + payment plan + ESA) | Outcome 1.1 + 1.2 (3-item) clear |

Each write-action has concrete, atomic verifiable content suitable for atomic Outcome rubrics at S3. No process-behavior gaps requiring PROPAGATE TO S3.

**C verdict: PASS.**

---

#### D. Prompt Trace

Strict re-check of 4-ask coverage against `5_Prompt.txt`:

| Ask (from prompt) | OE coverage | Judgement |
|---|---|---|
| **Ask 1** — 208B AC real status + update maintenance record + note in #maintenance | OE3 (find MT-2026-063) → OE4 (Tony Slack) → OE5 (Alamo search) → OE6 (Tony email) → OE7 (Alamo inspection) → OE8 (record update) → OE9 (Slack note) | Complete evidence → decision → 2 writes |
| **Ask 2** — Real Ridgeview owner exposure + update Linear issue | OE10-11 (MT + MR records) → OE12-13 (Robert + Brooke contacts) → OE14-17 (4-thread email chain closure) → OE18-20 (both bills, PrivateNote inspection) → OE21 (AR invoice) → OE22 (QB customer) → OE23 (payment application) → OE24 (list existing) → OE25 (create new issue) | Complete. Prompt says "update the Linear issue"; OE24 confirms no existing Ridgeview roof issue and OE25 correctly creates one — this is the only defensible interpretation given the universe surface. |
| **Ask 3** — Tanya Mitchell current status + confirm unit | OE26 (MR sweep exposing 6 decoys) → OE27 (Las Palmas 4B isolation) → OE28 (DLQ context) → OE29 (Slack unit confirmation) → OE30 (ESA context) | Complete; L6 decoy separation is explicit |
| **Ask 4** — Draft Gmail to Aurora with full update | OE1 (Aurora email verify) → OE31 (create_draft integrating all 3 items) | Complete |

All 4 asks covered end-to-end. No dangling OEs, no orphaned asks.

**D verdict: PASS.**

---

#### E. Overall Assessment

- **R1 blocker resolution:** the 6-OE expansion (OE12, OE13, OE17-split, OE22, OE27, OE28) lifted the density floor from 32 → 34 minimum, targeting L6/L8/L11 lever depth rather than padding. Well-scoped addition.
- **Density:** strict midpoint 41.5 (Council B: 43). Both clear the 40 floor. Neither meets the 50 design target. Per project rule #11 and the explicit AUDIT mandate ("if density midpoint >= 40 ... acceptable given the explicit HARDNESS phase justification -- do NOT REVISE again solely for density"), this is a PASS-with-THIN_DENSITY-note.
- **Hardness lever preservation:** all 5 levers (L2/L6/L8/L9/L11) remain sharply exercised. The +6 OE expansion deepened rather than diluted lever coverage.
- **Tool accuracy:** zero R1 regressions; all StarPM param traps observed.
- **Write-actions:** 4 writes across 3 services (Airtable, Slack, Linear, Gmail) with concrete atoms for atomic Outcome rubrics.
- **Prompt trace:** all 4 asks covered with clean evidence → decision → write chains.
- **Ordering:** reads-before-writes preserved (OE8 after OE7 Alamo confirm; OE25 after OE18-23 billing verify; OE31 terminal).
- **Fix-loop status:** 2 of 3 rounds consumed. No further S2 revise warranted; further OE expansion risks lever dilution.

Nothing further requires REVISE. AUDIT re-fire clears the S2 exit gate.

---

### AUDIT VERDICT: PASS (STRICT)

**THIN_DENSITY note:** Density midpoint (strict recount 41.5; Council B 43) clears the 40 absolute floor but does not reach the 50 design target. This is PASSED forward per project rule #11 on the strength of the explicit Hardness Plan justification: 5 levers (L2 structured-DB skip, L6 near-miss entity, L8 5-hop chain, L9 authority dismissal, L11 net-vs-gross) with total projected midpoint 50.0 lifting real-run counts ~15 calls above the OE floor. Further OE expansion is contraindicated — would risk lever dilution and would not materially improve real-run density. THIN_DENSITY must be carried forward as a known caveat into FINAL (do not re-litigate density in isolation there); if platform trajectories return avg tool calls < 40, task becomes a REDO candidate per REDO runbook, not an S2 defect.
