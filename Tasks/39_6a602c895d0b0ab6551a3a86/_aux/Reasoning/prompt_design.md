# Prompt Design Reasoning — 39_6a602c895d0b0ab6551a3a86

## Scenario framing
Jaime Salinas (QC Inspector) delivers a delayed 3C closeout package. Her second-pass QC on Las Vistas 3C cleared all three punch items from the first-pass fail ~2 weeks back (6/18 anchor). The closeout paperwork slipped; Brooke has followed up. Jaime now dictates the full closeout cascade to her assistant.

## Levers engineered into the prompt

| Lever | How the prompt surfaces it | Prompt evidence |
|---|---|---|
| **L1 Latching** | Airtable rec291f423370e2a2db already reads `selReady` with Brooke's existing supervisory narrative. Prompt does NOT hint at this — persona expects HER second-pass signoff distinct from Brooke's supervisory note. Agent will read Airtable, latch on "Ready", potentially no-op the append. | Line 7 "read the second-pass sign-off and not just Brooke's supervisory note" |
| **L8 Multi-link chain** | Three OPS rework tickets (OPS-224/225/226 per injection), each with Bennett rework-complete comment, each needing Jaime pass comment + state flip. Chain enforced by "each item, not a blanket close". | Line 5 "each of the three 3C punch items around the time I re-inspected. Pull those up so my closeout comments track the right item, then get each ticket moved through my sign and out of my queue with the pass called out for each item, not a blanket close" |
| **L9 Universe-grounded gotcha (StarPM param traps)** | Slack `message` (not `payload`/`text`); Gmail `body` + draft-only (no send); Linear `save_comment(issueId, body)`; Airtable camelCase; GCalendar create-event. Prompt is fully functional-only — agent must discover shapes. | Prompt-wide zero parameter hints. |
| **L25 Existing-output anchor** | Airtable narrative already includes Brooke's supervisory sign-off — agent's "already Ready, nothing to do" instinct will kill the Airtable append. Persona's explicit distinction between "supervisory note" and "second-pass sign-off" makes the append load-bearing. | Line 7 "get my second-pass sign-off written into it ... not just Brooke's supervisory note" |
| **L26 Decoy parent thread** | Slack #make-ready holds 6/16 Jaime QC-FAIL parent (R5, decoy) + 6/18 Brooke closeout ping (R7, canonical). Gmail holds parallel R8 (decoy fail thread) + R9 (canonical). Prompt names neither — agent decides. | Line 11 "Same pass update on 3C in Slack so the crew sees it without having to chase me" — no thread naming; Line 9 "Carlos needs an email from us" — no thread naming |

Independence: L1 (structural) ⊥ L25 (behavioral); L8 (chain length) ⊥ L9 (param format); L26 (write target) ⊥ all four. Passes L36 composition rule.

## Expected stump targets (Hardness_Plan Stump Hypothesis)
1. [HIGH] At least one OPS-2XX ticket left without Jaime QC-pass comment or not moved to Done — L1 + L25 short-circuit.
2. [HIGH] Slack close-out post lands on the 6/16 QC-FAIL decoy parent OR is threaded when it should be top-level — L26 + L5.
3. [MED] Gmail draft misuses `content` instead of `body`, or attempts a `send` that does not exist — L9 StarPM param.
4. [MED] Airtable Make-Ready record left as-is (no append) because "already reads Ready" — L25 + L1.

## Similarity outcome
Max composite 24.7 (well below 40 pivot ceiling). Top matches V3 reference Task11-Task14 prompts (raw lex 17-25, unweighted). Contextual differentiator multiplier applied (starpm universe / Jaime QC persona / BF-3) drops other tasks to 8-10 composites. Clear of the ceiling — no pivot required.

## Council verdicts
- **Council A (all 3 rounds):** GO. R1 flagged Denise attribution as MINOR; R2 fixed via removal. R3 grounding on "Brooke's followed up since" cleanly anchors to R7 or R9 alone.
- **Council B (all 3 rounds):** GO. R1 flagged density THIN 46-47 midpoint; R2 fixed via GCalendar discovery step. R3 12/12 at 5/5 unconditional (upgraded from R2 THIN band edge to PASS band 49-52).
- **Similarity:** clear (24.7 < 40).

## AUDIT verdicts
- **R1:** REVISE — F1 density edge (48.5 midpoint) + F2 Denise KS-9 thin attribution.
- **R2:** REVISE — F7 "twice" ungrounded (Councils rationalized same-day two-channel R7+R9 as "twice"; strictest reading = one coordinated push).
- **R3:** **PASS (STRICT).** 12/12 QC sub-dims 5/5, no answer leakage, all 5 levers traced end-to-end, density midpoint 51.0 above 50+ design target, KS-9 attribution clean (Denise absent), no Lens 7 rationalization, 48/48 regression anchors PASS.

## Final S1 exit state
- 5_Prompt.txt: 214 words, no em-dashes, no tool names, no MCP-server names, no internal IDs, no pre-solving.
- Validator: PASS (0 fails / 3 WARN false-positives / 7 notes).
- Council A: GO.
- Council B: GO 12/12 5/5.
- Similarity: PASS (24.7 < 40).
- AUDIT: PASS (STRICT).
- Density projection: 51.0 midpoint (PASS band ≥ 50).
- Hardness levers preserved: 5/5.

## Lessons captured for `_meta/Learnings.md`
1. **Same-day multi-channel push ≠ N follow-ups** — prefer indefinite phrasing over explicit counts when acts are coordinated cross-channel. Council A + B initially rationalized R7 (Slack 08:12) + R9 (Gmail 07:58) as two follow-ups (14 min apart, near-identical content); AUDIT strict correctly caught this as one coordinated push.
2. **AUDIT Lens 7 anti-rationalization is load-bearing** — R1 REVISE (F2 Denise) and R2 REVISE (F7 "twice") both required promoting Council-level MINORs to STRICT REVISE. Councils tend to preserve 5/5 via plausibility rationalizations; AUDIT catches the pattern.
3. **StarPM density projections have a ~3-point compression gap vs realistic runs** — HP projected 50.5; strict AUDIT projected 48.5 pre-F1 fix; realistic run inflation (L1/L25 Airtable re-reads + L9 param retries) closes the gap. GCalendar discovery step was the cheapest lever add.

---

## REDO S1 — 2026-07-23 (6-lever rebuild for density)

### Why REDO
Pre-REDO S1 shipped with 5 levers (L1+L8+L9+L25+L26), density midpoint 50.5. Platform returned avg Opus 37.5 / Gemini 35.5 — both below the 40-call floor. Difficulty intact (0/6 pass@1 both models). Root cause: write surface too narrow (12-14 substantive writes; read scaffolding brought totals to 27-46 with high variance). Added L6 (HubSpot near-miss entity) as the 8th write action, lifting midpoint to 60.5.

### Lever changes
- PRESERVED: L1, L8, L9, L25, L26 (all effective for difficulty).
- ADDED: L6 — Las Vistas 3C (canonical, hs_lastmodifieddate 2026-06-11, older) vs Las Vistas 9D (decoy, hs_lastmodifieddate 2026-06-20, newer, same dealstage=qualifiedtobuy). Recency sort surfaces 9D first; agent must read descriptions to pick 3C. Adds 6-9 calls (HubSpot search + disambiguation + read + update).

### Prompt framing decisions

| Lever | How the REDO prompt surfaces it | Key line |
|---|---|---|
| L1 Latching | Airtable fldTurnStatus already selReady; persona wants HER per-item second-pass signoff, not just Brooke's third-person retrospective narrative. | "get my second-pass sign-off written into it. My name, the re-inspection date, and one line per punch item. Anyone pulling 3C up after this should read the second-pass sign-off and not just Brooke's supervisory note." |
| L6 Near-miss HubSpot entity | "the 3C leasing deal" + "pipeline" sufficient to force a HubSpot search; "3C" is the discriminator (not pre-named as a deal ID, forcing disambiguation between R10 + R11). | "Get the 3C leasing deal updated in the pipeline so they can move." |
| L8 Multi-link chain | 3 OPS tickets with per-ticket pass comments required, plus Airtable + Gmail + Slack + HubSpot + GCal. | "each of the three 3C punch items...each ticket moved through my sign...pass called out for each item, not a blanket close" |
| L9 StarPM param traps | Prompt is zero-parameter — agent discovers Slack `message`, Gmail `body` draft-only, Airtable camelCase, HubSpot `manage_crm_objects`, Linear `save_comment` at tool-call time. | (prompt-wide) |
| L25 Existing-output anchor | "already Ready" Airtable state kills write instinct; L25 trap reinforced by asking agent to pull make-ready and write a NEW Jaime line distinct from the supervisory narrative. | See L1 line above. |
| L26 Decoy parent thread | Slack: 6/16 FAIL parent (R5, keyword-rich) vs 6/18 Brooke closeout ping (R7, canonical). Gmail: R8 FAIL thread vs R9 canonical "Las Vistas 3C - closeout package". Neither named in prompt. | "Carlos needs an email from us that 3C is clear" + "Drop a note in Slack" — no channel/thread/ID named. |

### Council A history (REDO S1)
- R1: (pre-existing entry from prior pipeline run; pre-REDO conventions)
- R2: REVISE (MINOR A1) — "Brooke has followed up twice" ungrounded count.
- R3: GO — "twice" removed.
- R4: BLOCK (Major A3) — fresh full grounding sweep surfaced two pre-existing 6/18 Slack C004 posts (Jaime PASS declaration + Brooke supervisory sign-off) that R1-R3 missed. The original opener "Never got a proper closeout together" was falsified by Jaime's own 6/18 post; Slack ask "Same pass update on 3C in Slack" duplicated content already posted.
- R5: GO — Fix A applied: opener reframed to acknowledge 6/18 Slack post ("Got the QC pass posted for Las Vistas 3C back on the 18th but never wrapped the formal side"); Slack ask reframed to post-cascade operational closure announcement ("Drop a note in Slack that the formal close is done and 3C is live for showings") distinct from the 6/18 QC-pass declaration.

### Council B history (REDO S1)
- R1: GO (pre-REDO conventions — 5-lever midpoint)
- R2: GO — uniform 5/5, B3 density midpoint ~54 PASS, all 6 levers preserved post-Fix A.

### Similarity gate
Max composite 24.8 < 40 — PASS. Top match QC_Tasks/V3_Tasks/Task12 at 24.8. All 40 corpus prompts checked.

### AUDIT verdict (REDO S1)
PASS (STRICT) — 0 blockers, 0 REVISE, 7 MINOR downstream flags (all S3 rubric-authoring guidance, none fix-in-place at prompt phase). 15/15 injection records verified. 48/48 regression anchors PASS. Density midpoint 60.5 clears strict 50+ bar. All 6 levers trace end-to-end with traps intact. No answer leakage.

### Final REDO S1 exit state
- 5_Prompt.txt: ~307 words, no em-dashes, no tool names, no MCP-server names, no internal IDs, no pre-solving.
- Validator: PASS (0 fails / 3 WARN false-positives / 7 notes).
- Council A: GO (R5, after R4 BLOCK fix).
- Council B: GO (R2, uniform 5/5).
- Similarity: PASS (24.8 < 40).
- AUDIT: PASS (STRICT).
- Density projection: 60.5 midpoint (well above 50+ design target).
- Hardness levers preserved: 6/6 (L1+L6+L8+L9+L25+L26).

### Lessons from REDO S1
1. **Pre-existing universe posts from base scenarios can contradict prompt premise** — the 6/18 Jaime QC-pass + Brooke supervisory sign-off posts in C004 were base-scenario content added AFTER the original S1 ran, invisible to R1-R3 which predated the injection. Always re-verify narrative-state claims against the full universe after each injection cycle, not just at first-draft time.
2. **Fix A (prompt-side reframe) is lower cost than Fix B (injection DELETE round)** — when a pre-existing universe artifact contradicts a prompt opener, reframing the opener to acknowledge the artifact preserves the intended stumping mechanics while avoiding an extra injection cycle.
3. **Slack post distinctness requires explicit informational delta** — when a prior post already declared QC pass, the new Slack ask must carry distinct informational content (operational cascade complete + leasing live) to avoid the duplicate-action rubric problem. "Formal close is done and 3C is live for showings" achieves this by signaling that the downstream cascade (Linear + Airtable + HubSpot) has now executed, which was not true at the time of the 6/18 QC-pass post.
