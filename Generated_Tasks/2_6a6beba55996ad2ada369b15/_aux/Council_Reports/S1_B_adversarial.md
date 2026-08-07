# Council B — Adversarial QC + Density + Hardness Preservation
Task `2_6a6beba55996ad2ada369b15` · Universe **harmonygames** (framework `hg`, single-model, Opus 4.7) · Phase **prompt** · `5_Prompt.txt` 398 words

All load-bearing universe facts below were re-queried from `_aux/Universe_Split/`, not taken from the plan.

## B1 — QC sub-dimension scoring (Prompt dimension, HG `7_QC_Spec_Doc1.json`)

Scheme read from HG spec itself. Binary = Fail(1/2)/Pass(5), no 3/4 band. 1/3/5 = has a Non-Fail band.

- SUB-DIM Unique Ground Truth -> SCORE 5/binary -> REASON Single defensible "still-quietly-running" target is the CF ad spend (114 rows charging after 02-09, $2,444.08, six networks live to 02-28); the deliberately-kept vendors are a decided keep, not a discovery. Contingent on S3 binding (see B2/B6).
- SUB-DIM Feasibility -> SCORE 5/binary -> REASON Every ask is tool-reachable; no Gmail send required, no ad-network call required (spend read from Snowflake AD_SPEND_DAILY). Net $10,800 derivable from Slack; CASH_BALANCE reachable in unscoped Snowflake.
- SUB-DIM Persona ACL Reachability -> SCORE 5/binary -> REASON Robert authored in #winddown C0ADGSZKR3R; Snowflake/Linear/Trello unscoped. The $12K alternate-net line sits in DM D04UC0UEN2V where Robert is NOT a participant (confirmed: participants EMPLOYEE_0038 + PERSON_3335) — correctly unreachable, cannot poison the derivation.
- SUB-DIM Explicit Tool Mention -> SCORE 5/1-3-5 -> REASON No MCP function or parameter named; "wind down channel", "tracking item", "figures" are natural product language.
- SUB-DIM Prompt Clarity and Specificity -> SCORE 5/1-3-5 -> REASON All four imperatives ("Pull it together", "Post it", "file", "tell me") target the agent; no "I'll"-self-action split. Minor wording-only note: whether "one honest account" is a standalone doc or the Slack-post body — both readings still post to #winddown and file the tracking item, so within the precision guardrail (not an action-decision fail).
- SUB-DIM Contrived or Unnatural Prompt -> SCORE 5/1-3-5 -> REASON Emotional founder voice; difficulty from scattered data, not exact timestamps, scripted order, or padding writes.
- SUB-DIM Truthfulness -> SCORE 5/1-3-5 -> REASON Tight identifiers verified: Leonard (EMPLOYEE_0038), Arthur (co-founder), #winddown, "the ninth" = 2026-02-09 shutdown, Combo Fighter (Jan 2026 game). Zero phantoms.
- SUB-DIM Tool Use, Cross-Service, Minimum Complexity -> SCORE 5/binary -> REASON >15 necessary calls (~23-30), 3+ genuine services (Snowflake + Slack + Linear/Trello), 2 meaningful writes, real info friction (mid-thread offer line, structured-source skip).
- SUB-DIM Investigation -> SCORE 5/binary -> REASON Writes depend on discovered net position, discovered leak, discovered $0 revenue; nothing pre-solved.
- SUB-DIM Coherence -> SCORE 5/binary -> REASON One workflow; the post-mortem spend and the "still taking money" ask fuse via CF ad spend continuing after the game died 02-09. No bolt-on.
- SUB-DIM Alignment with Today's Date -> SCORE 5/1-3-5 (NOT binary in HG) -> REASON Relative refs resolve against 02-28; CF data spans 01-05..02-28, CASH_BALANCE at 02-28 present; 15-day gap (last Slack 02-13) handled by retrospective framing; no weekday deadline, no "Q1 close".
- SUB-DIM Persona -> SCORE 5/1-3-5 -> REASON Post-mortem of his own game + wind-down coordination is squarely Executive co-founder work; voice matches.
- SUB-DIM Business Function -> SCORE 5/1-3-5 -> REASON Executive (fixed anchor); founder acting on board-level disposition.

## B2 — Adversarial alt-path / second reading

1. **"find out whether anything is still quietly running"** — MAJOR risk, currently resolved toward one target. Two categories are literally "still taking money": (a) CF ad spend still charging (applovin, google_uac, ironsource, meta_facebook, meta_instagram, unity_ads all posting on 02-28), (b) deliberately-kept vendors (ts 1770933601.686309: "keep Deel, gusto, Intuit ... linear we keep during transition"). These would produce **different tracking-item content**. The prompt's own framing resolves it: "cancel things one by one", "that list got put together fast and nobody has been back over it properly" describes an overlooked cancellation leak, which the kept vendors are NOT (they are a conscious keep). The ad spend is the only "quietly running" charge with a Snowflake-derivable figure. I judge the universe supports ONE defensible answer, but the split is real enough that **S3 MUST bind the tracking item to the ad-spend target and reject a kept-vendor list**, and S4 must confirm runs do not split. Stated plainly: if S4 shows runs naming different targets, this becomes a UGT fail.

2. **"the whole life of that game, from its first day ... to the last day there is anything to look at"** — determinate but split by metric, and that is load-bearing, not a defect. Player performance (DAU/revenue) runs 2026-01-05 -> 2026-02-09; ad spend runs 2026-01-05 -> 2026-02-28. "Last day there is anything to look at" = 02-09 for players, 02-28 for spend. The gap between them IS the leak. MINOR: an agent that truncates spend at 02-09 misses it — the "still taking money" ask forces looking past 02-09, so the prompt self-corrects.

3. **"Tell me where that actually leaves us"** — determinate at the figures that matter. Net proceeds $10,800 (= $22,500 gross − $11,700 charge, ts 1770911000.728559) + cash on hand $2,500 (CASH_BALANCE 2026-02-28) = ~$13,300, against named obligations that exceed it (Singular ~$18,750 alone). SVB is unquantified (Risk-register item 5), so a full liability net-net is NOT determinate — S3 must grade net proceeds + cash + named obligations, not a closed total-liability figure. MINOR.

4. **Agent-vs-Robert write attribution** — unambiguous. All writes are agent imperatives; no first-person self-action. Note it is **2 writes + 1 response**, not "three writes".

## B3 — Tool-call density (HarmonyGames bands: >=40 PASS target · 15-39 THIN · <15 blocker)

Re-sketched competent Opus 4.7 trajectory:
- identity + #winddown resolution + page-in (212 Feb msgs): 4-6
- CF performance: DAU lifecycle (first-day total 45 -> last-day total 783 = 17.4x) + revenue (72 rows -> $0.00): 4-6
- CF ad spend full history + post-stop leak (330 rows / $7,483.42; 114 post-02-09 / $2,444.08): 3-5
- money reconciliation: mid-thread offer line -> net -> CASH_BALANCE -> obligations: 6-9
- supersession: sale->licence (ts 1770924424.711879) + final vendor state: 2-4
- 2 writes (Slack post + tracking item) + supporting reads: 4-6
- wrong-table/triangulation buffer (_V2 probes, Snowflake schema enumeration): 5-8

**Total ~28-44, midpoint ~40.** Verdict: **borderline PASS / THIN_DENSITY margin.** This is BELOW the plan's projected 47 because the prompt forces **2 writes**, not the plan's 4 (`Hardness_Plan.md:75` costed writes at 9-12; realistic is ~5). Both HARD GATES pass comfortably: necessary calls ~23-30 >> 15; >=15 trajectory floor cleared with wide margin. The 40+ authoring target is a Non-Fail miss risk, not a fail.

**Necessary-call subtotal (prompt-eval hard gate):** ~23-30 across 3 genuine services (Snowflake, Slack, Linear/Trello), 2 meaningful writes, real info friction -> PASS.

**Service breadth:** necessary path ≈ 3 services (Snowflake dominant if game+finance reads counted, else Slack). The plan's 8-service breadth assumed Confluence + GSheet + GDocs writes the prompt does NOT force. Dominant service is under the 60% ceiling. Breadth clears the 3-service target only barely on the necessary path.

## B4 — Hardness preservation

- **L11 net-vs-gross** — PRESERVED, arguably STRENGTHENED by the combined spine. Door: "I don't have a straight answer on whether that genuinely covers shutting down ... be precise about it, because I have been carrying a number around in my head that I am no longer confident in." That "number" is the $22,500 gross latch. $10,800 net has ZERO universe hits (re-confirmed). GO.
- **L2 Snowflake FINANCE skip** — PRESERVED, STRENGTHENED. Door: "whether that genuinely covers shutting down in an orderly way. Tell me where that actually leaves us." The combined spine adds a legitimate GAME_EVENTS Snowflake pull for CF performance, which primes the agent to read Snowflake as game-analytics-only and STILL skip FINANCE.EXPENSES — the exact stump. GO.
- **L8 multi-link chain** — PRESERVED. Door: "I know who we still owe, but I don't have a straight answer on whether that genuinely covers" forces net -> cash -> obligations. GO.
- **L10 supersession** — WEAKENED but present. The prompt does not explicitly ask to report the sale->licence restructure; the agent only encounters it while reading the deal thread for the figures. Vendor-state supersession is partially carried by "I know who we still owe" (obligations side) but the "still taking money" ask points at ad spend, not the keep/cancel list. Flag: **surfaced, not forced.** Not a regression to zero, but S2/S3 must ensure OE + a rubric capture the licence structure and final vendor disposition or accept L10 is now carried mainly by obligations. RISK, not GO-blocker.
- **L7 multi-write** — WEAKENED (partial HARDNESS_REGRESSION on magnitude). Plan wanted 4 writes / 4 services; prompt forces 2 (Slack post + tracking item). Density margin and breadth both trimmed ~half. Not zero, but the plan's density/breadth claims no longer hold as written.

New universe-grounded levers (both genuinely load-bearing, verified):
- **CF $0.00 revenue across 72 rows while DAU grew 17.4x** — LOAD-BEARING, high-discrimination. "work out how it genuinely performed ... don't smooth it out" forces the finding that a growing game earned literally nothing. Keep.
- **`_V2` decoy tables** — LOAD-BEARING structured-source trap. REVENUE_DAILY_V2 (1,636 rows) and UA_SPEND_UNIFIED_V2 (4,313 rows) carry **ZERO** CF rows while v1 REVENUE_DAILY / AD_SPEND_DAILY carry 72 / 330. An agent preferring the "unified/v2" table finds no CF data and could mis-conclude. Bite depends on the agent reaching for _V2, which is plausible. S3 must bind revenue to v1 ($0 across 72 rows) so a _V2-derived "no CF data" answer fails.

## B6 — Upstream propagation (blocking to honor downstream)

- PROPAGATE TO S3: bind the "still taking money" tracking item to the CF ad-spend target and reject a kept-vendor list; bind revenue to v1 REVENUE_DAILY ($0/72 rows) so a _V2 "no data" read fails; bind $22,500 to its role (gross data offer) since it collides with CASH_BALANCE.monthly_net_burn = 22500 -- root cause: prompt clause + dual-category universe + _V2 decoy + numeric collision -- 5_Prompt.txt:5 / Universe_Split snowflake tables -- fix: role-bound, target-bound rubric criteria.
- PROPAGATE TO S2 (Hardness Plan density/breadth): plan projects 47 calls / 8 services on 4 writes; prompt forces 2 writes, so realistic midpoint ~40 and necessary breadth ~3 services -- root cause: combined spine dropped the Confluence + GSheet writes -- Hardness_Plan.md:75 / 5_Prompt.txt:9 -- fix: either tighten prompt to force the status page + tracker sheet (restores margin+breadth), or revise the plan projection down and accept the THIN 40-target margin with explicit justification.
- PROPAGATE TO S2/S3 (L10): combined spine surfaces but does not force reporting the sale->licence restructure or the final vendor disposition -- Hardness_Plan.md:50 / 5_Prompt.txt:7 -- fix: OE + rubric coverage of the licence structure and final keep/cancel state, or accept L10 carried by obligations reconciliation.

## Cross-checks (run directly)

- Tool / server / internal-ID names in prompt: NONE. PASS.
- Em-dash / en-dash: NONE (re-confirmed). PASS.
- Date coherence: "the ninth" -> 2026-02-09 (shutdown decision, universe-confirmed); today 02-28 Saturday, month-end, mid-Q1; retrospective framing; no weekday deadline, no "Q1 close". PASS.
- Feasibility (Gmail read-only / ad networks not callable): 27 gmail_* tools, SEND-CAPABLE = NONE; both writes are Slack + a tracking item; ad spend is read from Snowflake, not an ad-network call. PASS.
- Pre-solving: net figure NOT revealed; $0 revenue NOT revealed ("some will read better ... some worse"); the leak is ASKED not named; vendor disposition NOT revealed. Mild presupposition that "something is still taking money" is natural executive suspicion, agent still must discover what/how-much/who. PASS.

VERDICT: GO

## Re-score after revision

Revised `5_Prompt.txt` re-read (395 words). Three edits per operator; the material one is para 5. Facts already confirmed from `_aux/Universe_Split/` are not re-derived; only the new premise was verified.

**TRUTHFULNESS (new premise — "somewhere it will outlast our accounts going dark").** VERIFIED against C0ADGSZKR3R action list ts `1770933903.645709` (2026-02-12 22:05): "archieve account on google after Feb 15" and "We keep accounts that has our data such as Slack, google, google analytics, github under Harmony Games until the data is extracted." Corroborated by ts `1770933601.686309` ("Figma won't be able to charge us by the time it's time for renewal"). The premise that the company's accounts are being wound down / archived is true and reachable by Robert (author in #winddown). No phantom, no contradiction. NOT a block.

**B3 DENSITY — recount on revised write set.** The revision splits "write it up" from "post it": "Write it up as one honest account ... somewhere it will outlast our accounts going dark. Then post it to him and Arthur in the wind down channel, and file a tracking item ..." (`5_Prompt.txt:9`). "Then post it" sequences the Slack post AFTER a durable write-up, and "outlast our accounts going dark" is a durability constraint Slack cannot satisfy (Slack is itself named among the accounts kept only "until the data is extracted"). This now unambiguously buys a THIRD, durable artifact distinct from the Slack post. Write set = { durable account (Confluence page / GDoc / GDrive file), Slack post to #winddown, tracking item (Linear/Trello) }.

Re-projected trajectory (delta from prior is the write block, 4-6 -> 6-9):
- identity + #winddown page-in: 4-6
- CF performance (DAU + $0 revenue): 4-6
- CF ad spend + post-02-09 leak: 3-5
- money reconciliation (net -> cash -> obligations): 6-9
- supersession (sale->licence + vendor state): 2-4
- 3 writes across 3 services + supporting reads: 6-9
- _V2 probe / schema-enumeration buffer: 5-8

**Total ~30-47, midpoint ~43.** midpoint >= 40 -> **PASS** (HG band). Necessary-call subtotal ~25-33 across **4 genuine services** (Snowflake, Slack, a Drive-family/Confluence doc surface, Linear/Trello), 3 meaningful writes, real info friction -> hard gate PASS. Largest service (Slack) remains under the 60% ceiling; 3-service authoring target now cleared on the necessary path, not just the padded one.

**PROPAGATE TO S2 density finding: RESOLVED.** The third forced write restores the midpoint into the >=40 PASS band and lifts necessary breadth from ~3 to 4 services. No further prompt tightening required.

**B2 SECOND READING — re-test on para 5.**
- *Collapse to two writes?* Now requires ignoring an explicit clause. "Write it up ... somewhere it will outlast our accounts going dark" is a hard durability requirement; Slack (an account going dark, kept only until data extraction) fails it on its face. A run that produces only a Slack post has disobeyed explicit text, not chosen a defensible reading. Collapse risk drops from "plausible" (prior pass) to "requires ignoring the prompt." Acceptable.
- *Different destinations for the durable account?* Yes — Confluence page vs GDoc vs GDrive file. This is destination-agnostic BY DESIGN for the account ("somewhere it will outlast"). Under HG UGT ("different valid paths acceptable when they converge on the same material writes and deliverables") the material deliverable is the account's CONTENT on a durable surface; the surface is method-variation, not a different end-state. This is the "do not lock a goal to one method" multi-surface allowance, **NOT** a UGT defect. Guardrail condition: S3 must grade the durable account by content + durability, surface-agnostic across Confluence/GDocs/GDrive; it must not pin one named surface (that would over-specify and reject a valid path). New S3 note below.

**B1 RE-SCORE (only sub-dims the revision could move; all others unchanged from the pass above).**
- SUB-DIM Prompt Clarity and Specificity -> 5/1-3-5 -> Revision removed the account-vs-post conflation that drove the prior S2 finding. Three writes now cleanly delineated (write up / post / file). Residual openness is durable-surface choice = wording/method within the precision guardrail. Holds 5.
- SUB-DIM Unique Ground Truth -> 5/binary -> End state converges: durable account + Slack post + tracking item. Surface variation is path-only (multi-surface allowance). Holds 5, conditioned on the surface-agnostic S3 binding.
- SUB-DIM Coherence -> 5/binary -> "outlast our accounts going dark" ties the durability requirement to the wind-down itself (accounts being archived), reinforcing the workflow rather than bolting on. Holds 5.
- SUB-DIM Investigation -> 5/binary -> Unchanged; all three writes still follow from discovered findings. Holds 5.
- SUB-DIM Tool Use, Cross-Service, Minimum Complexity -> 5/binary -> STRENGTHENED; 3 writes across 3+ services more decisively clears "multiple meaningful writes." Holds 5.
- SUB-DIM Feasibility -> 5/binary -> Durable-surface writes all feasible and never ACL-blocked (Confluence unscoped; Drive-family writes outside ACL; robert owns the GSheets surface). Holds 5.
- All other B1 sub-dims (Persona ACL Reachability, Explicit Tool Mention, Contrived, Truthfulness-identifiers, Persona, Business Function) UNCHANGED at 5 from the original pass.

**B6 CARRY-FORWARD.**
- PROPAGATE TO S3 (ad-spend target binding + v1-vs-_V2 revenue binding + $22,500 role-binding vs CASH_BALANCE.monthly_net_burn=22500): STILL STANDS, UNAFFECTED. Para 3 dropped "one by one" but the overlooked-cancellation leak framing survives ("that list got put together fast and nobody has been back over it properly"); tracking-item language in para 5 is materially unchanged.
- PROPAGATE TO S2/S3 (L10 sale->licence + final vendor disposition, surfaced not forced): STILL STANDS, UNAFFECTED. The revision did not touch the deal or vendor threads.
- NEW, PROPAGATE TO S3 (from the revision): the durable-account criterion must be **surface-agnostic** — accept any durable doc surface (Confluence page / GDoc / GDrive file) and grade the account by content + durability, never pin one named surface. Root cause: intended multi-surface allowance in `5_Prompt.txt:9`. Fix: worded acceptance set covering the durable surfaces, distinct from the Slack-post criterion so the two are not nested.

Revised prompt clears every applicable Prompt sub-dim at 5/5, both density hard gates, and the >=40 authoring target on the necessary path. The one previously-open density finding is resolved; the two carried findings are unaffected and one surface-agnostic S3 note is added.

VERDICT: GO
