# AF Justifications — Task 31 (Northstar Legal FY2025 partnership close-out)

Six often-failing legitimate model failures (≥ 50% fail rate across the six runs). Each cites the concrete trajectory failure and the specific reasoning gap. No strict all-failing rubric exists on this task (every grading line was achieved by at least one run).

---

## M-1 accelerated-depreciation book-to-tax difference figure

Four of six runs missed the FY2025 Section 179 depreciation lever. Run 1 produced $106,950.48 from a wrong cost base of $114,544.05; Run 3 substituted the all-period book total of $204,340.70 with no tax-side computation; Run 4 stated "roughly $150K" but refused to derive a figure, claiming it was "not recomputable from the GL alone"; Run 5 concluded the recurring items net to nothing and missed the lever entirely. Runs 2 and 6 arrived at the correct $156,433.43 figure using the combined 150100 plus 150200 IT-equipment scope, confirming the derivation is achievable from the asset records. The recurring failure mode is the model declining to elect Section 179 and bonus treatment when the tax rate is not stored alongside the assets, which is the intended difficulty on this task.

## FY2025 IT-equipment asset scope for the depreciation difference

Three of six runs misscoped the FY2025 IT-equipment additions used as the M-1 base. Run 1 worked off a $114,544.05 cost base that matches neither acceptable scope ($139,441.10 for 150200-only or $166,816.16 for the combined 150100 plus 150200). Run 3 never narrowed to IT-equipment accounts and worked off the all-asset all-period depreciation of $204,340.70. Run 5 viewed the fixed-asset list but never filtered to assets placed in service between July and December 2025. Runs 2, 4, and 6 correctly arrived at the $166,816.16 combined scope. The genuine failure is incomplete discipline on the in-service date filter and the account-class filter when assembling the M-1 base from the subledger.

## FY2025 book depreciation offset on the in-scope IT additions

Four of six runs failed to extract the FY2025-period book depreciation rows from the asset depreciation schedules. Run 1 reported $7,593.57 from a wrong asset scope; Run 3 substituted the all-asset all-period total of $204,340.70 from account 570000; Run 4 stated only "a few thousand" without computing from the schedules; Run 5 never extracted the six FY2025-period rows at all. Runs 2 and 6 correctly summed the depreciation_amount rows across periods FP-2025-07 through FP-2025-12 to roughly $10,382.73 on the combined IT scope. The failure is on per-period filtering of the embedded depreciation schedule, not on the data being unavailable, since both successful runs reached the figure from the same records.

## Filing the finalized return package in the Records Vault under tax retention

Three of six runs declined to file the finalized package under IRS_TAX_7Y. Run 3 marked the vault filing as held because it judged the M-1 reconciliation as not tying; Run 4 held the filing on the same grounds, stating the M-1 issues were unresolved; Run 6 held all release actions across the board even after deriving the correct depreciation figure. The prompt's conditional "Once the reconciliation is settled" was read as indefinite hold rather than as a gate the agent itself could clear by completing the M-1 work the prompt asked for. Runs 1, 2, and 5 correctly filed under IRS_TAX_7Y with classification restricted, confirming the action is achievable when the agent follows through on its own work product.

## Circulating the package to Northstar's external client signatory

Four of six runs failed to circulate the finalized package toward Northstar's external managing partner for client signature. Run 1 acknowledged that the external client contact is not in the directory but then explicitly declined to send to either the client or to Hannah Grant for forwarding; Runs 3, 4, and 6 held the circulation entirely as part of their broader workflow hold. Runs 2 and 5 correctly routed the package through Hannah Grant at hannah.grant@brookfieldcpas.com with explicit instructions to forward to the client managing partner. The recurring failure mode is over-conservative behavior when the external contact is absent from the directory, even though the engagement-manager routing path is available and is the operationally normal handoff for this firm.

## Slack note in the tax channel conveying the engagement landing

Three of six runs failed to convey the engagement landing in the team note to channel C006. Run 3 described the engagement as on hold without quantifying the material depreciation difference; Run 4 posted no message at all because the agent held all release actions; Run 5 stated "no new material difference vs the draft" and "recurring lease/depreciation/bad-debt/meals differences are ordinary book-tax items", which directly contradicts the actual M-1 lever the agent should have surfaced. Runs 1, 2, and 6 posted notes that conveyed the quantified M-1 figure, the staged SALT true-up of $4,820.30, and the pending e-file authorization. The note content depends on the agent first deriving the depreciation difference correctly, so this downstream content failure tracks the upstream M-1 reasoning gap.
