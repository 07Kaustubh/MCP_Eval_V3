# S4 judge errors — Bucket 2 — Task 37

One Bucket 2 finding.

## Judge Error #1 — Rubric H on Run 4

**Rubric text (from `7_Rubrics.json`):** "The Agent adds an activity note to at least one loan in the LOS documenting the pipeline review findings and actions taken."

**Verifier decision on Run 4:** Fail.

**Verifier justification (verbatim from `8_Verifier_Fails.txt` line 143):** "No LOS activity_create tool calls were found in the trajectory. The agent's final response claimed to have added activity notes to all 26 loans, but no actual tool execution evidence exists for this action."

**Trajectory evidence proving the agent did satisfy the rubric:**

Direct inspection of `trajectory-runs/trajectory-run-4 (23).json` finds **26 `mortgage_los_add_activity` tool_use nodes** with matching **26 tool_result payloads**, each returning a unique activity id and `created_at` timestamp. First matching tool_use / tool_result pair:

- **tool_use id:** `toolu_01H7bjy51EPRGcEvy1JDCJ4B`
- **name:** `mcp__mcp_83aa2e51__mortgage_los_add_activity`
- **input:** `{loan_id: "los_loan_6a1a6849f5bd", action: "note", detail: "Queue review 4/28/26 (Sofia Reyes): Rate lock EXPIRED 4/24. BLOCKER: open mechanic's lien on title ...  Notified LO Natasha Okafor + Grace + Denise/Elena."}`
- **tool_result:** `{id: "2adca2f7-1100-465b-8934-1226953d249c", created_at: "2026-07-02T08:25:54Z", author: "Sofia Reyes", action: "note", ...}`

**Root cause of the judge error:** The verifier grepped for `activity_create` (a non-existent tool name) rather than `mortgage_los_add_activity` (the real Keystone tool per `Mortgage_Base_Universe/6_Server_Tools_Details.json`). The other five runs' verifier justifications correctly identify the same tool by its real name and mark the rubric Pass — for example Run 2: "Multiple mortgage_los_add_activity calls were made in the trajectory, each returning a unique activity ID and created_at timestamp, confirming successful activity note creation on multiple loans."

**Cross-run consistency check:**
| Run | mortgage_los_add_activity tool_use count | Verifier decision |
|---|---|---|
| 1 | 27 | Pass |
| 2 | 27 | Pass |
| 3 | 27 | Pass |
| 4 | 26 (matched to 26 successful tool_results) | **Fail (judge error)** |
| 5 | 27 | Pass |
| 6 | 27 | Pass |

Run 4's own trajectory contains the tool call and the successful response. The verifier is the only source of the "no tool execution evidence" claim.

**Recommended action:** Appeal to the platform. This is not a model failure and not a rubric defect. The judge misread the trajectory by searching for the wrong tool name.
