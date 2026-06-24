# Judge Errors (Bucket 2) — Task 26_6a390e724c34487b95645dcc

**Bucket 2 count: 0.**

Every failing rubric was re-read against the run trajectory and the per-task universe records. The judge calls are accurate under strict interpretation. No appeal needed.

Borderline calls that were considered but kept as judge-correct:

- **Run 1 / e35f2189 PASS** — The email body referenced doc_d394765fd5ab with restricted + IRS_TAX_7Y explicitly. Judge correctly recognized both classification and retention.
- **Run 1 / 8f9e0d3c PASS** — The email said "package itself can move to Northstar's managing partner for signature now per your authorization; e-file to follow once the signed authorization is back". Judge read "e-file to follow once signed" as the normal sequence (not a block by accrual housekeeping). Acceptable PASS.
- **Run 6 / b02c9e56 FAIL** — The memo body did reference email_scen_068_northstar_annual_corp_tax_0008 correctly. Judge correctly read the bundled rubric as requiring BOTH the email reference AND the posted JE id+entry_number; with no posted JE in any run, the second half is unfulfillable in Run 6 specifically, and the rubric correctly fails.
- **Run 5 / c79d65bd FAIL** — Agent opened CAO-3116 and embedded follow-up content in the issue description but never called linear_create_comment. Judge correctly applied the rubric's create-then-comment two-step requirement.
