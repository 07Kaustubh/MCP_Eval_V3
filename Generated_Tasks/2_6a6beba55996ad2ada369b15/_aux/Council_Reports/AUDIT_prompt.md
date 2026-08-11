# AUDIT — Phase `prompt` — Strictest Interpretation

Task `2_6a6beba55996ad2ada369b15` · Universe **harmonygames** (`hg`, single-model, Opus 4.7) · `5_Prompt.txt` 395 words · Validator PASS 0/0
Density scored against HarmonyGames' OWN bars (40+ target / >15 necessary / >=15 floor). The V3-family 50-midpoint bar is NOT applied here and would be wrong to apply; noted per the brief.

I re-derived every load-bearing fact from `_aux/Universe_Split/` and the streamed Snowflake blob rather than inheriting it. Findings-only; where a lens found nothing it says so in one line.

## The six attacked thin points

**(a) "whatever is still quietly running" — Unique Ground Truth. PASS.**
Two categories are literally still charging: (i) Combo Fighter ad spend still posting after the 02-09 stop (AD_SPEND_DAILY, ~$2,444.08 through 02-28, confirmed by streaming the 159 MB blob: `combo_fighter` present, Feb 10-28 date suffixes present), and (ii) deliberately-kept vendors (verified line: "During shutdown, let's keep Deel, gusto, Intuit ... linear we keep during transition"). The prompt demands the target be **"named with a figure against it."** I checked whether a kept vendor can satisfy that: in the Feb winddown shard, Deel/gusto/Intuit/Linear carry **no dollar figure** (Deel 8 mentions/0 amounts, gusto 11/only "$1", Intuit 6/0, Linear 2/0), and Snowflake MONTHLY_BURN is categorised (salaries/contractor/aws/legal/tools/other), not per-vendor, so no per-vendor figure is derivable. The ad-spend target alone produces a real figure. That is a universe-grounded disambiguator, independent of and stronger than the councils' "framing" argument. Second disambiguator: "quietly running", "that list got put together fast and nobody has been back over it properly", "surface later" describe an overlooked leak, which the conscious keeps are not. Two independent disambiguators converge on ONE target. This is NOT rationalization (Lens 7): both rest on re-read universe facts. Council A's MINOR and Council B's multi-surface allowance both reach the correct target by a weaker route; the verdict stands but the disambiguation is the figure-requirement, and S3 must bind the tracker to the ad-spend target and reject a kept-vendor list (Council B B6 PROPAGATE already carries this).

**(b) "the whole life of that game ... the last day there is anything to look at" — window split by table. PRODUCTIVE, not defective. PASS.**
Performance (DAU/REVENUE) is fixed 01-05 -> 02-09; ad spend runs to 02-28. "How it performed" therefore has a determinate window (01-05..02-09, revenue $0 across 72 rows). The spend continuation past 02-09 is not a second reading of the same quantity; it is the leak the task is built to surface, and "anything to look at" is deliberately metric-agnostic so an agent that truncates spend at 02-09 misses it. The ask is not indeterminate; the ambiguity is the discovery. PASS.

**(c) "I know roughly what we are getting for the data" — pre-solve check. PASS.**
"roughly" attaches to Robert's own uncertain memory ("a number around in my head that I am no longer confident in"), not to a hint that $22,500 is gross or incomplete. It does not leak that a $11,700 charge must be netted, and $10,800 net stays withheld (see Lens 2). This is the L11 latch door, not a leak.

**(d) "Tell me where that actually leaves us and be precise about it" vs unquantified SVB — MINOR carry-forward, not a prompt defect. PASS.**
"be precise about it" attaches to the coverage verdict. The precise quantities that DO exist are net proceeds ($10,800), cash on hand ($2,500 at 02-28), and the named open obligations (Unity, Singular, Helpshift $1,500). The determinate honest answer ("no, this does not cover an orderly shutdown; and SVB is an additional unquantified obligation") does not require the SVB figure, so the ask is satisfiable and has a single conclusion. SVB is referenced 3x but never quantified (risk-register item 5). The prompt is fine; the exposure is downstream: **S3 must not author a criterion demanding a closed total liability figure** (it would be ungradeable). Flagging as a carry-forward, not a REVISE.

**(e) Coherence / bolt-on — remove-any-sentence test. PASS (binary sub-dim held).**
Unifying spine: Robert assembles the honest picture Leonard hands to angels. Para 2 (performance + spend) and para 3 (the leak) are causally interdependent — the leak IS the spend still charging, discovered in the same data ("while you are in there"). Para 4 (money position) connects through the angel-calls purpose and is folded into a single deliverable by para 5 ("one honest account I can hand to Leonard for those calls"). Para 6 (lead figures) closes back to para 1's angel calls. This is one situation (wind-down of a company whose flagship failed), not two stapled asks. Removing any paragraph removes a component of that one account rather than an unrelated ask. Not a bolt-on.

**(f) Contrived / spec-sheet register (the 5/12 HG miss). PASS.**
The voice is a founder to their assistant: "I don't want the version they get to be the soft one"; "I would rather that be me than a line in a wind down letter"; "don't smooth it out"; "a number I am no longer confident in." Deliverables (para 5) are named as goals and the prompt stops — it does not enumerate their contents, formats, or preservation rules. Para 6 is a natural reply ask, not a specified output shape. 395 words is under the 500 cap and inside the HG register ceiling. Not a spec in costume.

## Lenses

- **Lens 1 (strict QC scoring).** Every applicable Prompt sub-dim scores 5/5 under the strictest defensible HG reading: Unique Ground Truth (a), Coherence (e), Feasibility, Investigation, Truthfulness, Persona, Business Function, Tool Use/Cross-Service/Min-Complexity, Explicit Tool Mention, Prompt Clarity, Contrived (f), Alignment with Today's Date (1-3-5 in HG, not binary). No sub-dim below 5. No NON-FAIL middle band invoked.
- **Lens 2 (answer-leakage).** BLOCKER-clear. My first sweep found 5 raw "10800" hits, which contradicted the plan's "zero" — I ran them down: every hit is a coordinate integer (`X: -0.1080000251531601`) in gdrive/github puzzle-layout files, or an ID string in Snowflake (`SES-1080...`, `INS-0010800`, 13 bare hits, all IDs). **Zero currency-formatted `$10,800` / `10,800` anywhere.** Net figure is not present as money. $0 revenue, cash position, and final vendor disposition are all withheld from the prompt. No single-call reveal.
- **Lens 3 (hardness end-to-end, prompt surfaces only).** L11 door: "a number I am no longer confident in" / "be precise about it". L2 door: "whether that genuinely covers shutting down in an orderly way." L8 door: "I know who we still owe, but I don't have a straight answer on whether that genuinely covers." L10: surfaced (deal thread) not forced — Council B RISK stands, S2/S3 must carry the sale->licence + final vendor state or accept L10 carried by obligations. L7: prompt forces 3 writes (durable account / Slack post / tracking item), below the plan's 4 — Council B already propagated this to S2; density still clears (Lens 4). No lever regressed to zero at the prompt.
- **Lens 4 (density, HG bars).** Independent re-sketch, excluding set_acting_user / ACL-denied / retries: identity+page-in 4-6, CF performance 4-6, ad-spend+leak 3-5, money recon 6-9, supersession 2-4, 3 writes+support 6-9, _V2/triangulation buffer 5-8. Midpoint ~40-43. Against HG: 40+ authoring target = PASS (thin margin), >15 necessary (~25-33) = PASS with room, >=15 floor = PASS, 3+ services (4 on necessary path: Snowflake, Slack, a Drive-family/Confluence doc surface, Linear/Trello) = PASS, Slack under 60%. Not scored against 50.
- **Lens 5 (adversarial veteran).** No tool/server/parameter names, no internal IDs, no em/en-dash (re-confirmed), no "at least N", no single-channel lock-in on a named goal, no "approximately" near exact values. Gmail read-only respected (no send/reply/draft dependency); ad networks not called (spend read from Snowflake). Weekend/month-end/mid-Q1 coherence intact; "the ninth" -> 02-09; no weekday deadline; no "Q1 close". 15-day staleness handled retrospectively.
- **Lens 7 (anti-rationalization).** One place I could have talked myself out of a finding — attack (a) UGT — I instead grounded in re-read facts (kept vendors carry no derivable figure; ad spend does). No "most-likely-interpretation" excuse used to clear a matched pattern.

## Carry-forward to downstream phases (not prompt defects)
1. S3 must bind the "still taking money" tracker to the CF ad-spend target and reject a kept-vendor list (already B6).
2. S3 must not author a closed-total liability criterion; grade net proceeds + cash + named obligations only (SVB unquantified).
3. S3 must bind $22,500 to its role (gross data offer) — it collides with Snowflake CASH_BALANCE.monthly_net_burn = 22500.
4. S2/S3 must carry L10 (sale->licence + final vendor disposition) or explicitly accept L10 as obligations-carried.

## Verdict

No BLOCKER, no sub-dim below 5 under strictest defensible HarmonyGames reading, no bolt-on, no answer leakage, feasibility and date coherence clean, density clears all three HG bars. The four carry-forwards are downstream bindings the councils already flagged, not prompt defects.

VERDICT: PASS (STRICT)
