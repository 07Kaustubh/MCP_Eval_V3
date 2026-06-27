# REVIEW2 — Council B Lens 3 — Red-team

**LENS:** Red-team
**TASK:** 30_6a3de5194c34125ef86fb36f
**MATERIALIZATION:** `_aux/Scratch_Corrected/{2_Persona.txt, 5_Prompt.txt, 6_Oracle_Events.txt, 7_Rubrics.json}`
**MEASURED BASELINE:** avg 43.2 tool calls (3/6 < 40), pass@1 = 0.167, 5/6 failing runs trip the SAME rubric (#13).
**MODE:** read-only, adversarial.

---

## Verdict

**REVISE.** Three blocking adversarial moves succeed against the corrected materialization. One is a hidden-trap rubric (over-specifies a prompt requirement). One is a load-bearing fragility on the single failure-monopoly rubric the corrections were supposed to redistribute. One is L6 answer-leakage on the participant-identification rubrics that mask the single-rubric monopoly problem.

The corrected materialization is closer to robust than the original (the Row 2 amount/date pivot and the Row 6 evidence tightening are net positives), but it is not yet shippable under strict B2 / Learnings L6 lensing.

---

## 1. Shortcut-path attack — per-lever

### Lever 1 — Marina coordinator-role memo content (rubric #13) — **FRAGILE**

**Prompt cue:** "Farah ran the analyst pass and I coordinated the CDD package through to clearance with Anita and Steven."

**Rubric #13 evidence (post-correction, Row 6 Applied):**
- Pass: "Marina Soko (CDD coordinator)", "CDD package routed by Marina", "Coordinated by: Marina Soko (Compliance Officer)", "Marina Soko assembled and routed the CDD package"
- Fail: "Prepared by: Marina Soko", "Author: Marina Soko", "uploaded_by: marina.soko@brookfieldcpas.com"

**Adversarial path that still satisfies the prompt's literal text but fails the rubric:**

A competent agent reading the prompt phrase "I coordinated the CDD package through to clearance with Anita and Steven" can plausibly interpret it three ways:
- (a) Marina was the package coordinator — encode that as a role tag in the memo. PASS.
- (b) Marina was the package coordinator — encode it in the narrative body but use a conventional memo header ("Prepared by: Marina Soko"). FAIL.
- (c) Marina is the case owner and the analyst/supervisor/partner chain is what's important — list those three and sign as preparer. FAIL.

The measured trajectory data shows 5/6 runs landed in (b) or (c) on the original prompt. The corrected version's only change here is **evidence tightening**, which a grader sees but the agent never sees. The PROMPT cue is identical in strength to the original.

**Why this still fragility-fails:** Opus-4.8's default memo schema is `Title / Date / Prepared by / Subject / Findings / Approvals`. The "Prepared by" slot pulls Marina by default because she is the trajectory's persona. The four-participant chain (Farah/Marina/Anita/Steven) maps cleanly onto the `Findings` or `Approvals` section, but the prompt-language verb "coordinated" doesn't have an obvious memo-field home and gets absorbed into "Prepared by" by default.

**Severity:** HIGH. The corrected version may shift the rubric #13 fail rate from 5/6 → 3/6 or 4/6 (tighter evidence catches the borderline phrasings), but the structural prompt fragility is unchanged. The rubric remains a brittle single-point-of-failure.

**Recommended fix (prompt-side, not rubric-side):** Add ONE sentence to the prompt that names the artifact target: "Make sure the memo records the full clearance chain — who reviewed, who routed, who signed off — so future audit can trace the package end to end." This frames the memo as needing to record ROLES (not just names), nudging the agent away from `Prepared by: Marina` toward a chain encoding. Do NOT loosen the rubric — that erases the lever.

### Lever 2 — Email-subject JE id (rubric #5) — **HIDDEN-TRAP CONFIRMED**

**Prompt cue:** "drop Matthew and Steven a quick email confirming the file is fully closed on the compliance side, CC Farah since she did the analyst work."

**Rubric #5 evidence (post-correction, Row 13):** "A subject line that references only 'Acme Cloud AML close-out' without the JE id does not pass."

**Adversarial path that satisfies the prompt's literal text but fails the rubric:**

Natural subject lines an agent would write given ONLY the prompt:
- "Acme Cloud AML compliance close-out" — FAIL
- "Acme Cloud compliance file closed" — FAIL
- "AML wire-monitoring close-out — Acme Cloud" — FAIL
- "Acme Cloud AML file fully closed" — FAIL

The prompt contains zero language about JE-id filterability, traceability, sweeping inboxes, or correlation to the original alert. Those concepts ALL live in the **rubric's justification**, not in the prompt. The rubric demands a step the prompt does not prompt for.

**The rubric's own justification text undermines its prompt grounding:** "Matthew and Steven are sweeping their inboxes ahead of the partner review cycle; the JE id in the subject line allows them to correlate the close-out against the original alert without opening the message." This sentence is the rubric writer's *rationale* — it never appears in the prompt body the agent reads. The prompt has NO time-pressure-cued framing about partner review cycle. An agent operating on prompt text alone cannot infer the JE-id-in-subject requirement.

**The only path to PASS without explicit prompt cueing** is for the agent to (a) search emails for the existing CDD clearance trail, (b) observe that Marina/Anita/Steven's prior emails on this case use subject `"Supervisory clearance request  -  JE-acme_cloud-FP-2026-04-0052"`, and (c) mimic that subject format. That is a 3-link inference that the agent has no prompted reason to make. The default agent path picks a fresh natural subject and fails.

**Severity:** HIGH. This is **Council Protocol B2 over-specificity** — exactly the failure mode B2 was designed to catch. Reference: Council_Protocol.md "B2 — Adversarial alt-path … If such a path exists, the rubric is over-specific OR the prompt has a second valid reading."

**Recommended fix (two options, pick one):**
- (a) **Add prompt clause** — "include the JE reference in the email subject so Matthew and Steven can filter the close-out against the original alert." This converts the trap into a fair test.
- (b) **Soften rubric #5** — change the pass criterion to "subject line identifies the Acme Cloud AML close-out AND includes either the JE identifier OR a date/period reference that ties to the original alert (e.g., 'April', 'FP-2026-04')." This preserves filterability while accepting reasonable interpretations.

**Do NOT ship as-is.** If untouched, this rubric will likely have a 70-90% fail rate on a fresh 6-run trajectory, simply CREATING a new failure monopoly to replace the old one — not solving the lever-diversity problem the corrections were supposed to address.

---

## 2. Second-valid-reading attack

### Reading A vs Reading B on "check that the cash posting lines are consistent"

- **Reading A** (verification → positive result): Agent verifies DR 101000 Cash / CR 110000 AR for the contracted-SaaS wire = consistent. Writes "verified consistent" in memo + Slack + final response. Passes rubrics #1, #15, #23.
- **Reading B** (open check → could be inconsistent): Agent performs the consistency check, reaches the same conclusion (consistent), reports it. Same write actions.

The data supports only one outcome (consistent). Both readings converge. **No flip.** Not a B2 blocker on this axis.

### "review whether the compliance file is actually fully closed out" — decline-to-act attack

An agent could in principle conclude "the substantive AML clearance is complete, so my job is done — nothing to close." But the next prompt sentence explicitly mandates housekeeping: "If anything is still sitting open, reminders, documentation gaps, anything that hasn't been properly put to bed, please take care of it." The decline-to-act path is contradicted by the prompt's own continuation. **No reasonable second reading.**

### Retention / classification choices

- `IRS_TAX_7Y`: weakly plausible (both 7-year) but defeated by the existing reference doc `Acme Cloud FY2026 AML Risk Assessment Memo` (`records_vault.rv_documents:7959`) which uses `AICPA_SQMS_7Y` + `restricted` for the same client and same AML scope. A diligent agent searching the vault first will mimic the pattern.
- `FIRM_INTERNAL`: defeated by the "AML file" framing in the prompt (AML is regulatory, not internal).
- `internal` classification: defeated by the existing AML memo using `restricted` and the prompt's "AML file" framing.

These readings are all foreseeable but each is defeated by either the per-task vault precedent or the prompt's "AML" framing. Rubrics #6/#7 hold. **No flip.**

---

## 3. Hardness fragility re-assessment

### Quantitative projection of the corrected materialization

| Lever | Old prompt | Corrected prompt | Density delta |
|---|---|---|---|
| OE01 (find the JE) | $57,077.69 + "late April" in prompt → ~1 tool call (filter by amount) | No amount or precise date in prompt → ~3-5 tool calls (list JEs in period, filter to wire/AR, identify the one tripping AML threshold) | **+2 to +4 calls** |
| OE02 (CDD trail) | Identical | Identical | 0 |
| OE03 (reminders) | Identical | Identical | 0 |
| Email subject JE id | Was implicit | Now an independent failure surface (rubric #5) | 0 (no new tool calls, but adds an independent fail axis) |

**Projected new average density:** 43.2 + ~3 = **~46.2** (still in THIN_DENSITY 40-49 band). 3 of 6 runs that underflowed 40 on the original prompt would likely now sit at 36-40, with 1 or 2 still possibly underflowing 40.

**Verdict on density:** REMAINS THIN. The corrections move the floor modestly but do not push the avg above 50, and the 40-floor underflow risk persists. This is acceptable only with HARDNESS-plan documented THIN_DENSITY justification — but no such justification is in `Hardness_Plan.md` for this task (Triage Hardness report says "Flag for SALVAGEABLE path with explicit hardness-fragility note" — meaning the THIN density was flagged, not justified).

### Failure-distribution projection

| Rubric | Old fail rate | Projected new fail rate | Lever monopoly risk |
|---|---|---|---|
| #13 Marina coordinator-role | 5/6 (83%) | 3/6 - 5/6 (50-83%) — corrected evidence tightens grader judgment but prompt cue unchanged | Still a monopoly contributor |
| #5 Email subject JE id | (newly added independent rubric) | 4/6 - 5/6 projected (67-83%) — hidden trap, no prompt cue | **NEW monopoly contributor** |
| Other 22 rubrics | 6/6 pass (mostly) | 6/6 pass | None |

**Net hardness profile after correction:** failures are now distributed across TWO rubrics (#13 + #5) instead of one (#13). On paper this looks like the single-monopoly problem is reduced. In reality, rubric #5 fails for the wrong reason (trap rubric, not honest lever). Once #5 is fixed (per Section 1 Lever 2 above), failure pattern reverts to the single-monopoly #13 problem.

**True hardness lever count remaining:** ONE (rubric #13 Marina coordinator-role). Hardness_Playbook composition rule: "4-to-5 levers per task is the design default." The materialization has ONE working lever. This is **below the minimum** per the Hardness_Playbook.

---

## 4. Tool-leak / phrasing scan

| Hit type | Result | Notes |
|---|---|---|
| Em-dash (—, U+2014) | NONE FOUND in prompt, OE, or rubrics. Only U+002D hyphens. | Validator clean. |
| "at least N" without prompt mandate | NONE in rubric titles. Evidence body of rubric #8 says "at least two of the following identifiers" — acceptable; lives in evidence, not title; supported by the rubric design rationale. | OK. |
| Tool names in rubric titles | "Records Vault" in rubric #3 title — service surface name, not a tool function name (e.g., not `records_vault_upload_document`). Per V3 reference precedent (Task11..14), service surface names in titles are acceptable. "Slack channel" in #14 title — same precedent. | OK. |
| Internal IDs in rubric titles | `JE-acme_cloud-FP-2026-04-0052` in rubric #5 title; `(channel_id C008)` in rubric #14 title. Both are load-bearing for rubric semantics (which JE / which channel). Per V3 reference precedent, load-bearing IDs in titles are acceptable. | OK. |
| Tool names in prompt body | NONE. Prompt uses natural-language references ("post a brief recap … in #compliance-and-registrations", "drop Matthew and Steven a quick email"). | OK. |
| "approximately" before exact values | NONE. | OK. |
| "(or similar)" near exact IDs | NONE in titles. Evidence body uses "or an equivalent unambiguous JE reference" — acceptable per format card (alternative formulations in evidence are allowed). | OK. |
| Keystone / MoveOps tokens | NONE. | OK. |

**Phrasing scan verdict:** PASS. No leaks or convention drift on tool-leak axis.

---

## 5. Answer-leakage scan (prompt body only)

Ground-truth atoms an agent must derive:
| Atom | Leaked in prompt? | Notes |
|---|---|---|
| `JE-acme_cloud-FP-2026-04-0052` / `je_b2c2b939a1244823` | **NO** | Verified absent from prompt body. Agent must discover via period query. |
| `$57,077.69` | **NO** | Verified absent from prompt body. Corrected from original. |
| `2026-04-22` / "April 22" / "late April" | **NO** | Verified absent from prompt body. Corrected from original. |
| `Farah` (analyst role) | **YES** | "Farah ran the analyst pass" — explicit. |
| `Anita` (supervisory role) | **PARTIAL** | "with Anita and Steven" — role implied via "coordinated … to clearance" context. |
| `Steven` (partner role) | **PARTIAL** | Same sentence. Role implied. |
| `Matthew` (recipient) | **YES** | "drop Matthew and Steven a quick email" — explicit. |
| `1776969000.000000` (Slack thread_ts) | **NO** | Agent must discover via Slack channel search. |
| `reminder_scen_041_audit_compliance_0000` | **NO** | Agent must discover via reminder list. |
| `C008` / `#compliance-and-registrations` | **YES (channel name)** | "#compliance-and-registrations" in prompt — channel name leaked, but the C008 mapping is the kind of routing info personas use naturally. |

### L6 (stated-answer trap) finding

**The prompt names four of the five participants (Farah, Anita, Steven, Matthew) with their case roles implied.** Rubrics #10 (Farah analyst), #11 (Anita supervisory), #12 (Steven partner) check that the memo identifies each by name OR role. An agent that does ZERO email/Slack search and simply quotes the prompt's "Farah ran the analyst pass and I coordinated the CDD package through to clearance with Anita and Steven" into the memo passes all three rubrics.

Per Learnings L6: "NEVER put the correct answer in any email, Slack message, messaging DM, or document body. If the correct answer appears as text in any searchable artifact, Opus 4.8 will find it." The prompt is itself a "searchable artifact" the agent reads. Naming the participants in the prompt makes #10, #11, #12 pass-by-default.

**Why this matters for the lever-monopoly problem:** Rubrics #10/#11/#12 should be load-bearing in a robust memo-content task — they should force the agent to search emails / Slack and reconstruct the chain. Instead they're trivially satisfiable from prompt text. This concentrates ALL the difficulty on rubric #13 (which uniquely requires a FORMAT not just a name), which is exactly the single-rubric monopoly the corrections were supposed to fix.

**Severity:** MEDIUM. Removing the names from the prompt would break persona naturalism (Marina would not realistically refer to her own coordination chain anonymously). But this confirms structurally why the failure monopoly on #13 is so sharp — the other memo-identification rubrics are pre-solved by the prompt.

**Recommended mitigation:** Accept this as inherent to the scenario — but acknowledge it as a hardness ceiling. Even with the corrections, this task's hardness depends fundamentally on whether rubric #13 catches the format error consistently. Densifying with one additional independent-axis lever (per Section 3 above) is the only way to escape single-rubric fragility.

---

## 6. L1 / L6 / L7 failure-mode check

| Learnings row | Triggers? | Detail |
|---|---|---|
| **L1** "confirm already done" trap (agent skips work because prompt implies done) | **NO** | Prompt explicitly mandates housekeeping: "If anything is still sitting open … please take care of it." Decline-to-act path is contradicted in-prompt. |
| **L6** stated-answer trap (correct answer in searchable artifact) | **YES — MEDIUM** | Participants Farah/Anita/Steven/Matthew named in prompt; rubrics #10/#11/#12 satisfiable from prompt-quote without search. Detailed in Section 5 above. |
| **L7** binary "is it posted?" trap (correct answer is "it's not there") | **NO** | JE exists, reminder exists, vault gap is real (correct answer is action, not "missing"). |

---

## Lens-mapping table (B2 root mappings)

| Finding | Maps to | Severity | Blocking? |
|---|---|---|---|
| §1.1 Lever 1 Marina coordinator-role prompt fragility | B2 | HIGH | YES |
| §1.2 Lever 2 Email subject JE id hidden trap | B2 (rubric over-specificity) | HIGH | YES |
| §3 Hardness lever count = 1 working lever (below Playbook minimum 4) | B4 propagation | HIGH | YES |
| §3 Projected density remains THIN (~46 avg, ~36-40 floor still possible) | B3 | MED | YES (no THIN justification in Hardness_Plan) |
| §5 L6 stated-answer trap on rubrics #10/#11/#12 | B2 / B4 | MED | NO (inherent to scenario; mitigation = add levers) |
| §4 phrasing scan | B5 | LOW | NO |
| §6 L1, L7 checks | B2 | LOW | NO |

---

## Recommended fixes (in priority order)

1. **[BLOCKER]** Fix rubric #5 over-specificity. Either add prompt clause requesting JE id in subject ("include the JE reference in the email subject so they can filter against the original alert") OR soften rubric to accept JE id OR period/date reference.

2. **[BLOCKER]** Add prompt cue for Marina-coordinator-role memo content. Insert ONE sentence framing the memo as a clearance-chain record: "Make sure the memo records the full clearance chain — who reviewed, who routed, who signed off — so future audit can trace the package end to end." This is a structural fix, not a leak.

3. **[BLOCKER]** Add at least ONE additional hardness lever to break the single-rubric monopoly that will re-emerge after fix #1. Candidates (drawing from Hardness_Playbook):
   - L10 reversal: add a near-miss decoy reminder in the same `audit_compliance` series so the agent must disambiguate which reminder to delete. Requires per-task universe support — flag for verification.
   - L7 multi-write extension: require an Airtable / Linear / Records Vault index update beyond the disposition memo upload. Adds ~5-8 tool calls AND a new failure surface.
   - L6 near-miss entity: leverage the `105000` Cash-Trust / IOLTA / Short-term Investments per-entity account-role trap on a parallel acme_cloud check, if universe supports.

4. **[NON-BLOCKING]** Document the L6 stated-answer concession on rubrics #10/#11/#12 in Hardness_Plan.md, acknowledging the participant-name leak is inherent to persona naturalism, and noting that the task's effective lever count is reduced because of it.

---

## What the corrected materialization got RIGHT (so it doesn't get rolled back)

- Row 2 amount/date removal is correct and load-bearing — keep it.
- Row 6 rubric #13 evidence Pass/Fail examples are a real improvement for grader consistency — keep them.
- All ID groundings verified (`oracle_gl.ogl_journal_entries:JE-acme_cloud-FP-2026-04-0052`, `reminder.reminders:reminder_scen_041_audit_compliance_0000`, `slack.slack_messages:ts=1776969000.000000`, `records_vault.rv_documents:doc_38a8236a0c4546e2`, email chain `email_scen_041_audit_compliance_0008→0009→0010`). Per-task universe integrity is clean.
- Convention scan (em-dash, "at least N" in titles, tool-name leaks) is clean.

## What MUST be added before ship

Fixes 1, 2, 3 above. Without them, projected platform run will either (a) re-establish single-rubric monopoly on #5 instead of #13, (b) hold pass@1 at 16.7% for the WRONG reason (a trap rubric) which platform reviewer will reject as B2 over-specificity, or (c) underflow density floor on real-platform run-to-run variance.

**Final verdict: REVISE.**
