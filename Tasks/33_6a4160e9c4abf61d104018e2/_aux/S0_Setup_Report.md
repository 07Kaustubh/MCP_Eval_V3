# S0 Setup Report — Tasks/33_6a4160e9c4abf61d104018e2

## Universe
- **Detected universe:** keystone (Keystone Mortgage Partners — Residential mortgage brokerage)
- **Base path:** `Mortgage_Base_Universe/`
- **Tool catalog:** `Mortgage_Base_Universe/6_Server_Tools_Details.json`
- **Persona briefs:** `Mortgage_Base_Universe/3_Persona_Briefs.md`
- **Universe today:** 2026-06-12 (America/New_York)
- **Last event timestamp seen:** 2026-08-04T21:25:33+00:00
- **Records dated after today:** 8921 — legitimate for future-dated loan items, scheduled closings, and forward-dated CRM events; not a defect signal.

## Persona
- **Name:** Carlos Rivera
- **Role:** Loan Officer (FHA, Conventional)
- **Staff id:** `los_staff_a7fa5b29babd`
- **Email:** carlos.rivera@keystonemortgage.com
- **NMLS:** NC-245891
- **Specialization:** FHA, Conventional (also originated VA and USDA loans in data)
- **Hire date:** 2021-08-01
- **Is active:** true
- **Current pipeline count (per staff record):** 6
- **Assigned-LO loan count in this universe:** 69 (status breakdown — closed: 48, processing: 9, denied: 4, underwriting: 3, conditional_approval: 3, withdrawn: 1, clear_to_close: 1; type breakdown — conventional: 38, fha: 20, va: 9, usda: 2)

## Business function
- **Name:** Loan Operations

## Per-task data
- **sha256 (data_hash):** `ba427e8f9456b845256dcdfdb3f5f15cb199b5a910b07666bb3dbc1fc209672e`
- **Total records:** 31318 across 34 service.table files

### Record counts (service_inventory.md)
| Table | Records |
|---|---|
| contacts.contacts | 889 |
| crm.crm_companies | 17 |
| crm.crm_contacts | 501 |
| crm.crm_deals | 80 |
| crm.crm_engagements | 472 |
| crm.crm_leads | 501 |
| email.emails | 7287 |
| email.mailboxes | 4 |
| email.threads | 2504 |
| mortgage_los.borrowers | 638 |
| mortgage_los.conditions | 32 |
| mortgage_los.document_checklist_items | 8841 |
| mortgage_los.lenders | 8 |
| mortgage_los.loans | 644 |
| mortgage_los.staff | 17 |
| mortgage_los.vendors | 23 |
| quickbooks.accounts | 28 |
| quickbooks.bills | 585 |
| quickbooks.customers | 53 |
| quickbooks.invoices | 73 |
| quickbooks.items | 6 |
| quickbooks.vendors | 16 |
| slack.slack_channels | 26 |
| slack.slack_messages | 573 |
| slack.slack_users | 30 |
| stripe.charges | 1730 |
| stripe.connected_accounts | 11 |
| stripe.customers | 575 |
| stripe.disputes | 16 |
| stripe.fc_accounts | 41 |
| stripe.fc_transactions | 3228 |
| stripe.payment_methods | 660 |
| stripe.refunds | 26 |
| stripe.transfers | 1183 |

## Fact Ledger atom counts
- emails: 1923
- amounts: 4446
- dates: 808
- personas: 1306
- id_slack_channel: 8
- (universe is Keystone — id_je / id_exception / id_recon / id_vendor / id_apinv counts are 0 by design; those atom types belong to Brookfield's GL universe.)

## Notes
- `slack.slack_channels` has 26 rows but only 8 of the canonical Keystone channels (C001 #general, C002 #loan-processing, C003 #closings, C004 #compliance-alerts, C005 #rate-watch, C006 #sales-pipeline, C007 #random, C008 #it-support) should appear in deliverables — the extra rows are DMs / departed-employee channels and must be filtered downstream.
- TRID timing landmine and Marcus Webb departure are the two known Keystone landmines — pass into HARDNESS as candidate stump levers along with persona-scope (`assigned_lo = los_staff_a7fa5b29babd`).
- Carlos's persona brief lists 16 open-thread scenarios; HARDNESS will pick the densest persona × period × scenario intersection.
