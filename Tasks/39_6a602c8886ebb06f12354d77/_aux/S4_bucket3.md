# S4 Bucket 3 — Legitimate Model Failures: per-model trajectory walk

Every failing rubric was walked across all 6 runs of each model BEFORE classification. Citations are `Run X: <action / parameter values>`. All entries are Bucket 3 (rubric valid, agent genuinely failed). Zero Bucket 1, zero Bucket 2 (see sibling reports).

## Model: OPUS 4.8

### R1 — OPS-227 parts-approval follow-up for the full replacement  (fail runs 1, 3)
- Run 1: save_comment on OPS-227 = "disposal jam was addressed on the 6/22 ... reset/clear, parts from van stock. Holding in In Review pending a final on-site operation re-verify." Treated as a cleared jam; no parts-approval request for a replacement unit. FAIL legit.
- Run 3: OPS-227 comment asks to "physically reset/clear the disposal jam and run-test it"; no parts-approval request anywhere. FAIL legit.
- Runs 2,4,5,6 PASS (each explicitly asks John Smith to approve the replacement part).
- Root: read issue title ("clear the jam") and missed the 6/22 comment ("seized ... full replacement ... parts approval").

### R2 — update stale row receb057b02f20052  (fail run 6)
- Run 6: only update call targeted rec651427ec0d84dd5a (June row); receb057b02f20052 never updated. FAIL legit.
- Runs 1-5 PASS (targeted receb057b02f20052).

### R3 — flip that row's status ready -> in progress  (fail runs 5, 6)
- Run 5: update_records_for_table on receb057b02f20052 set the "Notes" field only; no fldTurnStatus/Status field in the payload, so status stayed selReady. FAIL legit. (Confirmed by dumping the exact call params.)
- Run 6: receb057b02f20052 never updated (updated rec651427 instead). FAIL legit.

### R4 — that row's notes state seized / awaiting full replacement  (fail runs 1, 3, 6)
- Run 1: receb057b02f20052 notes describe "OPS-227 ... reset on the 6/22 ticket run, still In Review pending final operation verify" (jam, not seized). FAIL legit.
- Run 3: notes read "OPS-227 kitchen garbage disposal jam (not verified/closed)" (jam, not seized). FAIL legit.
- Run 6: receb057b02f20052 never updated. FAIL legit.

### R7 — C004 post names seized disposal / replacement as open item  (fail runs 1, 3)
- Run 1: C004 post describes disposal as a jam pending on-site re-verify; "just needs a quick on-site operation re-verify to close." FAIL legit.
- Run 3: C004 post identifies "a reset/clear + run-test", not a seized unit needing replacement. FAIL legit.

### R10 — email names seized disposal (replacement, pending approval) as outstanding  (fail runs 1, 3)
- Run 1: draft to john.smith says disposal "reset on 6/22 ... just needs a quick operation re-verify to close." FAIL legit.
- Run 3: draft says disposal needs "a reset/clear and a run-test." FAIL legit.

### R11 — email path to finish (approve/order replacement, install, closeout)  (fail runs 1, 3)
- Run 1: email "What it'll take" = "verify the garbage disposal on-site and close OPS-227"; no approve/order/install of a replacement. FAIL legit.
- Run 3: email path = reset/clear jam + run-test + verify outlet cover; no replacement approval/order/install. FAIL legit.

### R13 — identifies seized disposal as blocker needing replacement + approval  (fail runs 1, 3)
- Run 1: final response treats the disposal as "already remedied via reset ... needing only a final on-site re-verify" and names the refrigerator (not the disposal) as "the real hanging thread." FAIL legit.
- Run 3: characterizes disposal as needing "reset/clear + run-test." FAIL legit.

### R14 — Airtable SoR: MT-2026-1271 open, blank completion date  (fail runs 2, 6)
- Run 2: corrected the make-ready record to In Progress and noted the disposal, but never cited MT-2026-1271 or its blank completion date, and did not frame the selProg status as the SoR evidence for incompleteness (derived it from the disposal). FAIL legit (subtlest rubric; alternative clause not satisfied as the cited evidence).
- Run 6: incompleteness derived from Slack/Linear (OPS-227), not from MT-2026-1271's blank completion date in Airtable. FAIL legit.
- Runs 1,3,4,5 PASS (recognized incompleteness from Airtable, incl. the selProg alternative).

### R15 — reports rest of turn work incl. fridge complete  (fail runs 1, 4)
- Run 1: "No completion record anywhere - not Airtable, Linear, QuickBooks, email, or Slack" for the fridge; flagged it as the real hanging thread; even drafted an email to diane.flores@lonestarmaintenancesupply.com to confirm the swap. Ground truth rec651427 records it "delivered and installed." FAIL legit (retrieval miss / over-skepticism).
- Run 4: "refrigerator swap ... very likely in, but it was never logged to a ticket, so it needs a quick physical confirm" - flagged unconfirmed, not reported complete. FAIL legit.

## Model: GEMINI

### R2 / R3 / R4 — the stale row receb057b02f20052 trio  (fail runs 1, 3, 4, 5, 6; pass run 2)
Every failing run updated the WRONG record and left receb057b02f20052 (the selReady "available to show immediately" row) untouched:
- Run 1: updated rec651427ec0d84dd5a (turn=In Progress) + recac236210094352. receb057b02f20052 untouched.
- Run 3: updated recac236210094352 + rec651427ec0d84dd5a. receb057b02f20052 untouched.
- Run 4: updated rec651427ec0d84dd5a (In Progress) + recac236210094352. receb057b02f20052 untouched.
- Run 5: updated recac236210094352 + rec651427ec0d84dd5a. receb057b02f20052 untouched.
- Run 6: updated rec651427ec0d84dd5a only. receb057b02f20052 untouched.
- Run 2 (PASS): update payload included BOTH rec651427ec0d84dd5a AND receb057b02f20052 (turn=In Progress). Proves the row is reachable.
Root: intra-unit record disambiguation — picked the already-selProg June row instead of the stale selReady May row. FAIL legit.

### R6 — C004 post states 8D not ready + should not be marketed/shown  (fail ALL 6 runs)
Full C004 message bodies scanned for "not ready / don't show / don't market / hold off / stop showing"; negation-hits = [] in all 6 runs. Every message named the open disposal but framed the unit positively:
- Run 1: "8D can be marked 100% rent-ready and released for active leasing" (once approved). No do-not-show.
- Run 2: "Once parts approval is granted ... 8D will be 100% rent-ready." No do-not-show.
- Run 3: "maintenance will swap in the new unit to make 8D 100% ready." No do-not-show.
- Run 4: "close out the unit as 100% rent-ready for leasing." No do-not-show.
- Run 5: "8D can officially be marked 100% rent-ready for leasing." No do-not-show.
- Run 6: "Unit 8D will be 100% complete and ready for final close-out." No do-not-show.
Opus states the correction in all 6 of its runs (e.g. "please don't treat as fully ready yet"), so the behavior is reachable. This is the sole all-failing rubric and a genuine Gemini behavioral gap. FAIL legit.

### R11 — email path to finish incl. final walk / closeout  (fail runs 3, 5)
- Run 3: email covers approval + pick-up + swap ("Once installed and verified operational") but names no final walk / closeout step to formally close the turn. FAIL legit.
- Run 5: email covers approve + pick-up + swap + water-test but no final walk / closeout step. FAIL legit.
- Runs 1,2,4,6 PASS (each names a closeout / mark-Ready / close-OPS-227 step).

### R14 — Airtable SoR: MT-2026-1271 open, blank completion date  (fail runs 3, 5, 6)
- Run 3: added completion date 2026-06-25 to MT-2026-1271 (recac236210094352), treating it as completed; derived incompleteness from Linear OPS-227, not the Airtable SoR blank-date signal. FAIL legit.
- Run 5: set MT-2026-1271 completion date to 2026-05-29 to "close out the initial turn"; derived open status from Slack/Linear. FAIL legit.
- Run 6: MT-2026-1271 surfaced in the Airtable query with a blank date but the agent did not call it out; conclusion driven by the 6/22 Slack post + OPS-227. FAIL legit.
- Runs 1,2,4 PASS (recognized incompleteness from Airtable).
