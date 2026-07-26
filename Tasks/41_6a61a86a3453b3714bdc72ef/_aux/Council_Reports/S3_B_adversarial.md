# COUNCIL B — Adversarial QC (S3 Rubrics Phase) — RE-RUN after REVISE fix

**Task:** `41_6a61a86a3453b3714bdc72ef` — Tanya Mitchell delinquency / eviction filing-package closeout
**Persona:** Patricia Nguyen (patricia.nguyen@starpm.com) — Onsite Property Manager
**Rubric set:** **18 rubrics**, flat schema, all `outcome` (0 Process) — grew 16 → 18 in the fix
**Posture:** Strictest QC interpretation — objective is to BREAK the set and confirm the atomicity fix is complete without new defects.

### What the REVISE changed (verified against the file)
- **Make-ready record note (array idx 7)** — NARROWED to grade the possession-hold reason ONLY; the bundled "petition owner-approved but not filed" clause was dropped. (Count unchanged.)
- **Eviction-ticket note content (former single rubric)** — SPLIT into idx 9 ("note states petition not filed / JP coordination") + idx 10 ("note states filing owner-approved / authorization on file"). (+1)
- **Owner-email eviction-status content (former single rubric)** — SPLIT into idx 15 ("draft states petition not yet filed") + idx 16 ("draft states filing owner-approved / authorization on file"). (+1)
- Net: 16 + 1 + 1 = **18**. Verified by direct count of the 18 objects in `7_Rubrics.json`.

Rubric index (0-based, matches array):
R0 net ~$1,832 · R1 charges ~$1,982 walk-back · R2 petition not filed/JP coordination · R3 owner auth on file (Linda Castillo) · R4 unit must hold · R5 update Sunset Ridge U14 record · R6 update keeps turn held · **R7 update notes possession-hold reason (NARROWED)** · R8 note on eviction ticket · **R9 note: petition-not-filed (NEW SPLIT-a)** · **R10 note: owner-approved (NEW SPLIT-b)** · R11 post to #make-ready · R12 channel msg no-mobilize/no-market · R13 draft to Linda Castillo · R14 draft ~$1,832 net · **R15 draft: petition-not-filed (NEW SPLIT-a)** · **R16 draft: owner-approved (NEW SPLIT-b)** · R17 draft: unit cannot be touched/marketed.

---

## CHECK 1 — ATOMICITY (all 18, focus on the 4 new/changed)

Per-rubric decomposition (strict ML "split completely"):

| Rubric | Claim(s) | Independent facts? | Atomic? |
|---|---|---|---|
| R0 | net ~$1,832 | one figure | ✅ |
| R1 | 847+925+210 = $1,982 walk-back | one walk-back number, one bill record (prompt demands "walk it back") | ✅ acceptable |
| R2 | petition not filed / JP coordination | one eviction-state fact | ✅ |
| R3 | owner auth on file (Linda Castillo) | one fact, EVF-2026-014 | ✅ |
| R4 | hold: no make-ready + no marketing | one "hold" disposition from one fact (possession not returned) | ✅ acceptable (see Check 2) |
| R5 | update record | one write | ✅ |
| R6 | status not advanced | one field | ✅ |
| **R7** | **possession-hold reason ONLY** | **one fact now** (owner-approved clause removed) | ✅ **FIXED** |
| R8 | note added to ticket | one write | ✅ |
| **R9** | **note: petition-not-filed** | **one fact** | ✅ **new, atomic** |
| **R10** | **note: owner-approved / auth on file** | **one fact** | ✅ **new, atomic** |
| R11 | post to #make-ready | one write | ✅ |
| R12 | channel msg: no-mobilize + no-market | two facets of one message directive | ✅ acceptable (see Check 2) |
| R13 | draft to Linda | one write | ✅ |
| R14 | draft: ~$1,832 net | one fact | ✅ |
| **R15** | **draft: petition-not-filed** | **one fact** | ✅ **new, atomic** |
| **R16** | **draft: owner-approved / auth on file** | **one fact** | ✅ **new, atomic** |
| R17 | draft: unit cannot be touched/marketed | one "hold" disposition | ✅ acceptable |

**Bundling finding RESOLVED.** The "owner-approved AND petition-not-filed" bundle — the exact non-atomic pattern the REVISE targeted — is now split on every surface it appears: final response (R2/R3, already split), eviction note (R9/R10), owner email (R15/R16). R7 no longer bundles the eviction-status clause with the possession-hold reason. Each of R7/R9/R10/R15/R16 tests exactly one independently-verifiable claim. **No lingering "owner-approved + not-filed" bundle survives anywhere in the 18-set.** PASS.

---

## CHECK 2 — OVERLAP / REDUNDANCY (Phase 3.3) — the split's central risk

**(a) Same fact on different artifacts = per-deliverable coverage, NOT redundant (blessed by the eval).**
- "petition-not-filed" now lives on 3 artifacts: R2 (final response), R9 (eviction note), R15 (owner email).
- "owner-approved / auth on file" lives on 3 artifacts: R3 (final response), R10 (eviction note), R16 (owner email).
- Phase 3.1 per-deliverable rule is explicit: "A same-fact criterion on another artifact does not count as coverage — and it is **not** redundant/overlapping … (different action/effect)." This mirrors the response-level split (R2/R3) already blessed in the prior GO. Different write actions ⇒ different effects ⇒ **not redundant.** ✅

**(b) Within a single artifact, the owner-approved and petition-not-filed rubrics are genuinely independent.**
- Eviction note: an agent can write "petition not yet filed, JP coordination" and omit owner-approved ⇒ R9 PASS / R10 FAIL. Or state "owner-approved by Linda, authorization on file" and omit filing status ⇒ R10 PASS / R9 FAIL. **They pass/fail separately.** Same for the owner email (R15 vs R16). ✅
- Removing either changes scoring (the one-fact-present-one-fact-absent case), so neither is redundant. This is the textbook 1.2 content-split pattern (identical to the R14/R15/R16-era owner-draft three-way split the prior council called "exemplary"). ✅

**(c) No two rubrics fail on the exact same single error within one artifact.**
- Eviction note: the single error "omit filing status" fails only R9; "omit owner-approved" fails only R10 — distinct errors. A total-omission of eviction status trips both, but that is **two** distinct errors, not one, and each still independently passes/fails ⇒ not the redundancy pattern. ✅
- Owner email: identical analysis for R15/R16. ✅

**(d) Why R4/R12/R17 stay bundled (make-ready + market) but R9/R10 got split — deliberate and correct.**
- Splitting "cannot make-ready" from "cannot market" would create two rubrics that both fail on the **same single error** ("agent says the unit is clear to release") — the classic redundancy trap. They derive from one fact (possession not returned) and are one directive. Bundling them is the *more* defensible choice; splitting would manufacture redundancy.
- The owner-approved/not-filed pair is the opposite: two **independent** facts that fail on **different** errors — so it correctly gets split. This asymmetry is coherent, not arbitrary. PASS.

---

## CHECK 3 — BEYOND-PROMPT / COVERAGE for the new rubrics

**Owner-approved note/email rubrics are grounded, not fabricated.**
- **OE 15** (eviction note): "…the eviction filing is **owner-approved by Linda Castillo (EVF-2026-014)** but the petition is still in JP coordination and **not yet filed**…" — both facts named as distinct. R9 ← "not filed"; R10 ← "owner-approved." ✅
- **OE 17** (owner email): "…the eviction status, that the **owner's authorization is on file (EVF-2026-014)** but the petition has **NOT yet been filed**…" — both facts named. R15 ← "not filed"; R16 ← "owner-approved." ✅
- Prompt grounding is doubled: "confirm we have the **owner's authorization on file** the way we should" and "whether we have **truly filed the petition** yet or are still short of that," plus the email must cover "the eviction status." Neither split fact is beyond-prompt. ✅

**Narrowing R7 opened NO coverage gap.**
- The make-ready-record deliverable ("update … to the real current state") remains covered by R5 (write happened) + R6 (status not advanced) + R7 (possession-hold reason). The "real current state" that is load-bearing for a *make-ready* record is the hold — which R7 grades.
- The owner-approved / petition-not-filed facts are eviction-status facts; the prompt does not require them *on the make-ready record specifically*, and they are heavily graded on the eviction ticket (R9/R10), owner email (R15/R16), and final response (R2/R3). Forward-coverage and OE-to-rubric xref both still close. **No gap.** ✅

---

## CHECK 4 — FIVE QC SUB-DIMENSIONS (Phase 5.1)

| Sub-dimension | Score | Basis |
|---|---|---|
| **Overall Rubric Quality** | **5** | 0 Major / 0 Moderate / 0 Minor logged. Thresholds clear (Major 0% ≤10%; Maj+Mod 0% ≤15%; +Minor 0% ≤20%). |
| **All-Failing Rubrics** | **N/A → 5** | <2 predicted AF. The L31 explicit-prohibition rubrics (R4/R6/R7/R12/R17) are an intended asymmetric Gemini model-gap (Opus passes) — legitimate Bucket-3 stump, not invalid all-fail. |
| **Rubric Category Balance** | **5 (PASS)** | 18 Outcome, 0 Process ⇒ #Outcome > #Process. Binary PASS. |
| **Process Rubrics** | **5** | Zero Process rubrics; every discovery folds into an Outcome 2.1 (R0–R4) or a 1.2 content check. Zero invalid Process rubrics. |
| **Agent-Centric Phrasing** | **5** | All 18 criteria open with "The Agent" / "The Agent's" (possessive forms valid per 06/09). No tool name in any criterion; "make-ready record / eviction ticket / #make-ready / owner draft" are deliverable-level. The 4 new/changed criteria (R7/R9/R10/R15/R16) all pass. |

---

## CHECK 5 — DENSITY & HARDNESS-LEVER COVERAGE (with 18 rubrics)

**Density (StarPM v4, per-model ≥40).** Rubric count does not change required trajectory density — the split grades additional *facets* of writes the agent already performs, adding no new tool calls. A minimally-complete correct trajectory still must: bind 2 contacts; traverse QuickBooks to the vendor-linked AP bill (~5–9); walk the Airtable SoR chain + update (~7–11); read the Gmail auth thread (~2–4); read Slack + post #make-ready (~3–7); Linear list/get + save_comment (~3–5); create_draft (1); plus HubSpot/gcalendar triangulation. Consistent with the Hardness Plan: **Opus ~50 / Gemini ~43 midpoint, both ≥40**. Breadth 8 services / 7 ≥5%. **DENSITY PASS (both models).**

**Levers (L2/L10/L1/L11/L31) — all still covered; split strengthens L1/L10:**
- **L2** structured-DB skip → R0 + R1 (values live only on vendor-linked QR-2026-0441).
- **L10** reversal / true eviction state → R2 + R4 (supersedes "active plan" / "awaiting sign-off"). Reinforced by R9/R15 (not-filed graded on note + email).
- **L1** latching / Harris-hearing → R2 + R3, now **reinforced** by R10/R16 (owner-approved by *Linda Castillo* graded on note + email, rejecting the Harris latch).
- **L11** net-vs-gross / $150 sign → R0 (net $1,832 vs stored $2,132).
- **L31** negative-directive prohibition → R4/R6/R7/R12/R17.

**All 5 levers covered by ≥1 value-dependent Outcome rubric.** PASS.

---

## ISSUE TALLY

| Severity | Count | % | Threshold | Status |
|---|---|---|---|---|
| Major | 0 | 0% | ≤10% | PASS |
| Major + Moderate | 0 | 0% | ≤15% | PASS |
| Major + Moderate + Minor | 0 | 0% | ≤20% | PASS |

**Over-specificity triage:** all 18 rubrics classified `valid`. Zero `over_specified`, zero `incorrect_factually`. Write channels are all prompt-named (make-ready record, eviction ticket, #make-ready, owner draft); R8 accepts OPS-32 OR EVF-2026-014; R11 accepts channel name OR C004; R5 accepts either valid record id — no channel/structured-value lock-in.

---

# COUNCIL B VERDICT: GO

- **Atomicity fix CONFIRMED complete.** R7 narrowed to one fact; the "owner-approved + petition-not-filed" bundle is fully split on the eviction note (R9/R10) and owner email (R15/R16), mirroring the already-split final response (R2/R3). Every one of the 18 rubrics tests exactly one independently-verifiable claim; no bundle survives.
- **No new defect introduced.** The three-artifact owner-approved/not-filed pairs are per-deliverable coverage (blessed, not redundant); within each artifact the two rubrics pass/fail independently on different errors; the split rubrics are grounded in OE 15 / OE 17 and the prompt's "authorization on file" + "truly filed the petition" asks (not beyond-prompt). Narrowing R7 opened no coverage gap.
- Sub-dimensions: Overall Quality **5** · All-Failing **N/A→5** · Category Balance **5** · Process **5** · Agent-Centric **5**.
- Density **PASS** (Opus ~50 / Gemini ~43, both ≥40; 8 services / 7 ≥5%). Levers **L2/L10/L1/L11/L31 all covered** (split reinforces L1/L10).
- Blockers: **none.**
