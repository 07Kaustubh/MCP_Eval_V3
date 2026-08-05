#!/usr/bin/env python3
"""
Universe registry — per-universe constants for multi-universe pipeline support.

Registered universes (see UNIVERSES below for the authoritative list):
- brookfield: CPAs & business advisory firm (v3, current default)
- keystone: Residential mortgage brokerage (v3.1)
- moveops: B2B remote-work relocation services (v2.1)
- starpm: Residential property management (v4)

Every validator + runbook + council prompt should read constants via
`get_universe_constants(detect_universe(task_dir))` rather than hardcoding
universe-specific values.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

UNIVERSES = {
    "brookfield": {
        "name": "Brookfield CPAs & Advisors",
        "framework_version": "v3",
        "domain": "Public accounting / business advisory",
        "base_path": "Brookfield_Base_Universe",
        "docs_path": "Docs",
        "evals_path": "Evals",
        "qc_reference_path": "QC_Tasks/V3_Tasks",
        "tool_catalog": "Brookfield_Base_Universe/8_Server_Tools_Details.json",
        "persona_briefs": "Brookfield_Base_Universe/2_Persona_Briefs.md",
        "business_function_doc": "Brookfield_Base_Universe/3_Task_Categories_Business_Functions.md",
        "universe_one_pager": "Brookfield_Base_Universe/7_Brookfield_Universe_One_pager.md",

        "today": "2026-06-12",
        "today_tz": "US/Eastern",
        "persona_email_domain": "brookfieldcpas.com",
        "business_functions": [
            "Accounting Operations", "Bookkeeping", "Tax", "Compliance & Internal Controls",
            "Audit", "AP / Vendor Operations", "BlackLine Close-Discipline & Variance",
            "Engagement Mgmt & Client Operations", "Executive / Partner Oversight",
            "HR & People Operations",
        ],
        "tight_identifiers": [
            "channel names", "doc IDs", "JE IDs", "vendor names", "company names",
            "account numbers", "dollar amounts", "dates", "fiscal periods", "ticket IDs",
        ],
        "oe_service_map": {
            "reconciliations": "blackline", "exceptions": "blackline", "variance": "blackline",
            "ap_invoices": "sap_subledger", "vendor_master": "sap_subledger",
            "journal_entries": "oracle_gl", "accounts": "oracle_gl", "fiscal_periods": "oracle_gl",
            "retention": "records_vault", "documents": "records_vault",
            "tickets": "linear", "issues": "linear",
            "hr_personnel": "airtable",
            "chat": "slack", "channels": "slack",
            "email_threads": "email",
        },
        "cross_service_pairs": [
            ("email", "sap_subledger"), ("email", "oracle_gl"), ("email", "blackline"),
            ("oracle_gl", "blackline"), ("oracle_gl", "sap_subledger"),
            ("records_vault", "linear"), ("slack", "linear"),
        ],

        "retention_codes": {"AICPA_SQMS_7Y", "IRS_TAX_7Y", "FIRM_INTERNAL", "INDEFINITE"},
        "slack_channels": {f"C{n:03d}" for n in range(1, 11)} | {"C012"},
        "classifications": {"public", "internal", "restricted"},
        "blackline_exception_types": {
            "unrecorded_invoice", "duplicate_entry_detected", "timing_difference_over_sla",
            "subledger_feed_drop", "missing_accrual_variance", "fx_revaluation_drift",
        },
        "npcs": {
            "Owen Mercer", "Brenda Abbas", "Sofia Halabi", "Farah Dlamini",
            "James Randall", "Lucia Ferreira", "Mateo Kovac",
        },
        "services": ["oracle_gl", "sap_subledger", "blackline", "records_vault",
                     "airtable", "linear", "email", "slack", "contacts", "messaging", "reminder"],

        "account_trap_check": True,
        "entity_name_to_id": {
            "brookfield": "brookfield",
            "acme cloud": "acme_cloud", "acme": "acme_cloud",
            "northstar legal": "northstar_legal", "northstar": "northstar_legal",
        },
        "lifecycle_check_kind": "fiscal_period",
        "lifecycle_states_closed": {"closed", "locked"},
        "lifecycle_states_open": {"open", "draft", "active"},

        "tool_param_traps": {
            "email_send_email": {"content_field": "content", "wrong_field": "body"},
            "slack_conversations_add_message": {"content_field": "payload", "wrong_field": "text"},
            "records_vault_upload_document": {"content_field": "content_b64", "wrong_fields": ["file", "data"], "window": 100, "ignorecase": True},
            "linear_create_issue": {"required": "teamId", "wrong": "team", "window": 100},
        },

        "landmines": [
            "Account-number trap: 105000 / 120000 differ per entity (Cash-Trust on Brookfield, IOLTA on Northstar, Short-term Investments on Acme; 120000 absent on Brookfield, Client Cost Advances on Northstar, Deferred Commissions on Acme). Query oracle_gl.ogl_accounts WHERE account_number=N AND entity_id=E before trusting any prose role label.",
            "Email-chain truthfulness: 'X never responded' claims must be proven by (i) parent_id descendant walk from sender's email, (ii) sender-filter across same subject prefix on email.emails. Never trust prose 'no response' claim without the walk.",
            "Persona-scope: 'my X' framing binds to persona's universe assignments (created_by / owner_email / approver_email = persona email). Verify every rubric value is in the persona's scope.",
            "Lifecycle precondition: posting JE to closed period requires either earlier unlock step OR late_post_authorization_id on the post call.",
        ],
    },

    "keystone": {
        "name": "Keystone Mortgage Partners",
        "framework_version": "v3.1",
        "domain": "Residential mortgage brokerage",
        "base_path": "Mortgage_Base_Universe",
        "docs_path": "Docs_keystone",
        "evals_path": "Evals_keystone",
        "qc_reference_path": "QC_Tasks/V3.1_Tasks",
        "tool_catalog": "Mortgage_Base_Universe/6_Server_Tools_Details.json",
        "persona_briefs": "Mortgage_Base_Universe/3_Persona_Briefs.md",
        "business_function_doc": "Mortgage_Base_Universe/5_Task_Categories_Business_Functions.md",
        "universe_one_pager": "Mortgage_Base_Universe/2_Summary.md",

        "today": "2026-04-28",
        "today_tz": "US/Eastern",
        "persona_email_domain": "keystonemortgage.com",
        "business_functions": [
            "Loan Operations", "Compliance", "Sales", "Finance", "Executive", "IT",
        ],
        "business_function_weights": {
            "Loan Operations": 0.30, "Compliance": 0.20, "Sales": 0.20,
            "Finance": 0.15, "Executive": 0.10, "IT": 0.05,
        },
        "tight_identifiers": [
            "channel names", "doc IDs", "loan IDs", "vendor names", "company names",
            "account numbers", "dollar amounts", "dates", "fiscal periods", "ticket IDs",
        ],
        "oe_service_map": {
            "loans": "mortgage_los", "borrowers": "mortgage_los", "conditions": "mortgage_los",
            "document_checklist": "mortgage_los", "disclosures": "mortgage_los",
            "ap_invoices": "quickbooks", "vendor_bills": "quickbooks", "accounts": "quickbooks",
            "payments": "stripe", "charges": "stripe", "transfers": "stripe", "refunds": "stripe",
            "bank_transactions": "stripe", "fc_accounts": "stripe",
            "borrower_documents": "filesystem", "pdfs": "filesystem",
            "leads": "crm", "deals": "crm", "engagements": "crm",
            "chat": "slack", "channels": "slack",
            "email_threads": "email",
        },
        "cross_service_pairs": [
            ("email", "mortgage_los"), ("email", "quickbooks"), ("email", "crm"),
            ("mortgage_los", "crm"), ("mortgage_los", "filesystem"), ("mortgage_los", "stripe"),
            ("quickbooks", "stripe"), ("slack", "mortgage_los"),
        ],

        "retention_codes": set(),
        "slack_channels": {f"C{n:03d}" for n in range(1, 9)},
        "classifications": set(),
        "blackline_exception_types": set(),
        "npcs": {
            "Marcus Webb",
        },
        "services": ["mortgage_los", "stripe", "filesystem", "crm", "quickbooks",
                     "email", "slack", "contacts"],

        "account_trap_check": False,
        "entity_name_to_id": {
            "keystone": "keystone", "keystone mortgage": "keystone",
        },
        "lifecycle_check_kind": "TRID",
        "loan_statuses_open": {
            "application", "conditional_approval", "processing", "underwriting", "clear_to_close",
        },
        "loan_statuses_closed": {"closed", "denied", "withdrawn"},
        "condition_statuses": {"outstanding", "cleared"},
        "trid_windows": {
            "loan_estimate_days_after_app": 3,
            "closing_disclosure_days_before_close": 3,
        },

        "tool_param_traps": {
            "email_send_email": {"content_field": "content", "wrong_field": "body"},
            "slack_conversations_add_message": {"content_field": "payload", "wrong_field": "text"},
            "mortgage_los_add_condition": {"required": "loan_id"},
            "stripe_create_charge": {"content_field": "amount"},
        },

        "landmines": [
            "TRID timing: Loan Estimate must be sent within 3 business days of application; Closing Disclosure must be delivered 3 business days before closing. Query mortgage_los.disclosures for actual sent_date vs application_date / closing_date and verify windows are respected.",
            "Email-chain truthfulness: 'X never responded' claims must be proven by (i) parent_id descendant walk from sender's email, (ii) sender-filter across same subject prefix on email.emails. Never trust prose 'no response' claim without the walk.",
            "Mortgage LOS vs CRM source-of-truth: loan-level data lives in mortgage_los (loans, borrowers, conditions, document_checklist_items). CRM holds the marketing / referral funnel (leads, deals, engagements). When a claim references loan state, never trust CRM as the source — query mortgage_los.",
            "Departed-employee trap: Marcus Webb is on the staff roster but has departed (scenario_7da8f37a — evidence of pre-resignation data exfiltration). Tasks must not ask the agent to interact with him as if active.",
            "Persona-scope: 'my borrowers' / 'my pipeline' binds to persona's loan officer assignments (mortgage_los.loans.loan_officer_email = persona email). Verify every rubric value is in scope.",
        ],
    },

    "moveops": {
        "name": "MoveOps Inc.",
        "framework_version": "v2.1",
        "domain": "B2B remote-work relocation services",
        "base_path": "MoveOps_Base_Universe",
        "docs_path": "Docs_moveops",
        "evals_path": "Evals_moveops",
        "qc_reference_path": "QC_Tasks/V2.1_Tasks",
        "tool_catalog": "MoveOps_Base_Universe/6_Server_Tools_Details.json",
        "persona_briefs": "MoveOps_Base_Universe/2_Persona_Briefs.md",
        "business_function_doc": "MoveOps_Base_Universe/3_Task_Categories_Business_Functions.md",
        "universe_one_pager": "MoveOps_Base_Universe/5_MoveOps_One_Pager.md",

        "today": "2026-04-26",
        "today_tz": "US/Pacific",
        "persona_email_domain": "moveops.com",
        "business_functions": [
            "Operations", "Customer Engagement / Support", "Engineering", "Finance", "Executive",
        ],
        "business_function_weights": {
            "Operations": 0.25, "Customer Engagement / Support": 0.30, "Engineering": 0.20,
            "Finance": 0.15, "Executive": 0.10,
        },
        "tight_identifiers": [
            "channel names", "ticket IDs", "relocation IDs", "vendor names", "company names",
            "dollar amounts", "dates", "coordinator names", "Airtable record IDs", "CRM deal IDs",
        ],
        "oe_service_map": {
            "relocations": "airtable", "stipends": "airtable", "client_accounts": "airtable",
            "vendor_records": "airtable",
            "ap_invoices": "quickbooks", "vendor_bills": "quickbooks", "customers": "quickbooks",
            "accruals": "quickbooks", "vendor_master": "quickbooks",
            "deals": "crm", "engagements": "crm", "leads": "crm",
            "tickets": "linear", "issues": "linear", "linear_projects": "linear",
            "calendar_events": "calendar",
            "chat": "slack", "channels": "slack",
            "email_threads": "email",
            "contacts": "contacts",
        },
        "cross_service_pairs": [
            ("email", "airtable"), ("email", "crm"), ("email", "quickbooks"),
            ("airtable", "quickbooks"), ("airtable", "linear"), ("airtable", "crm"),
            ("slack", "linear"), ("slack", "airtable"), ("slack", "quickbooks"),
            ("crm", "calendar"), ("crm", "airtable"),
        ],

        "retention_codes": set(),
        "slack_channels": {f"C{n:03d}" for n in range(1, 10)},
        "classifications": set(),
        "blackline_exception_types": set(),
        "npcs": {
            "Marcus Webb",
        },
        "services": ["airtable", "calendar", "contacts", "crm", "email", "linear",
                     "public", "quickbooks", "slack"],

        "account_trap_check": False,
        "entity_name_to_id": {
            "moveops": "moveops", "moveops inc": "moveops",
        },
        "lifecycle_check_kind": "PHMSA_hazmat",
        "lifecycle_states_closed": set(),
        "lifecycle_states_open": set(),

        "tool_param_traps": {
            "email_send_email": {"content_field": "content", "wrong_field": "body"},
            "slack_conversations_add_message": {"content_field": "payload", "wrong_field": "text"},
            "linear_create_issue": {"required": "team", "wrong": "teamId"},
            "linear_create_comment": {"required": "issueId", "content_field": "body"},
            "crm_create_engagement": {"required": "engagement_type", "content_field": "body"},
            "airtable_update_records": {"required": "base_id", "also_required": "table_id"},
            "quickbooks_create_customer": {"required": "DisplayName"},
        },

        "landmines": [
            "PHMSA DOT hazmat compliance: hazmat shipments (cryogenic lab equipment, Class 3B lasers, chemical samples) require a signed DOT certificate from the freight carrier. Verbal driver confirmation does NOT count. When a claim references hazmat documentation, verify the Airtable relocation record AND the Swift / Heartland email thread carry the actual signed certificate reference.",
            "Email-chain truthfulness: 'X never responded' claims must be proven by (i) parent_id descendant walk from sender's email, (ii) sender-filter across same subject prefix on email.emails. Never trust prose 'no response' claim without the walk.",
            "Airtable Relocations source-of-truth: relocation state lives in Airtable (tblRelocations01 — status, vendor, coordinator, special handling). CRM holds the deal / engagement funnel. When a claim references relocation state, never trust CRM as the source — query Airtable.",
            "Vendor cross-reference: Heartland Q1 invoice has multiple cancelled / reassigned moves billed in error. Any vendor-payment-dispute task must cross-reference the invoice line items against tblRelocations01 vendor + status, NOT trust the invoice prose.",
            "Marcus Webb identity (MoveOps): Marcus Webb here is a BrightLoop Analytics senior analyst (CLIENT employee), distinct from the KeyStone departed-employee Marcus Webb. Same name, different person, different universe — do NOT carry KeyStone's departed-employee logic over.",
            "ExpenseBot pilot bugs: the stipend auto-categorizer has known policy-config bugs for Vectral and Mosaic (exclusion checks, amount validation, duplicate hash detection). When verifying stipend approval correctness, query Airtable stipend records against the policy + Dmitri's audit findings (linear ticket portfolio).",
            "Persona-scope: 'my clients' / 'my relocations' binds to persona's CRM assignment or Airtable coordinator field (account_manager_email or coordinator_email = persona email). Verify every rubric value is in scope.",
        ],
    },

    "starpm": {
        "name": "Star Property Management",
        "framework_version": "v4",
        "domain": "Residential property management",
        "base_path": "StarPM_Base_Universe",
        "docs_path": "Docs_starpm",
        "evals_path": "Evals_starpm",
        "qc_reference_path": "QC_Tasks/V4_Tasks",
        "tool_catalog": "StarPM_Base_Universe/7_Server_Tools_Details.json",
        "persona_briefs": "StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md",
        "business_function_doc": "StarPM_Base_Universe/3_StarPM_TASK CATEGORIES.md",
        "universe_one_pager": "StarPM_Base_Universe/0_StarPM_One-Pager.md",

        "today": "2026-07-01",
        "today_tz": "America/Chicago",
        "persona_email_domain": "starpm.com",
        "business_functions": [
            "Property Operations", "Portfolio Coord & Owner Relations",
            "QC & Field Services", "Maintenance & Repairs", "Leasing & Applicant Intake",
        ],
        "business_function_weights": {
            "Property Operations": 0.32, "Portfolio Coord & Owner Relations": 0.20,
            "QC & Field Services": 0.10, "Maintenance & Repairs": 0.18,
            "Leasing & Applicant Intake": 0.20,
        },
        "tight_identifiers": [
            "channel names", "unit numbers", "property names", "vendor names", "owner names",
            "invoice numbers", "dollar amounts", "dates", "Airtable record IDs", "Linear issue IDs",
        ],
        "oe_service_map": {
            "make_ready": "airtable", "turns": "airtable", "maintenance_tickets": "airtable",
            "unit_availability": "airtable",
            "rent_invoices": "quickbooks", "vendor_bills": "quickbooks", "journal_entries": "quickbooks",
            "delinquency": "quickbooks", "owner_distributions": "quickbooks", "accounts": "quickbooks",
            "leasing_deals": "hubspot", "applicants": "hubspot", "leasing_funnel": "hubspot",
            "tickets": "linear", "issues": "linear", "linear_projects": "linear",
            "calendar_events": "gcalendar",
            "email_threads": "gmail", "drafts": "gmail",
            "chat": "slack", "channels": "slack",
            "contacts": "contacts",
        },
        "cross_service_pairs": [
            ("gmail", "airtable"), ("gmail", "quickbooks"), ("gmail", "hubspot"),
            ("airtable", "linear"), ("airtable", "quickbooks"),
            ("hubspot", "gmail"), ("slack", "airtable"), ("slack", "linear"),
            ("gcalendar", "gmail"), ("quickbooks", "airtable"),
        ],

        "retention_codes": set(),
        "slack_channels": {f"C{n:03d}" for n in range(1, 9)},
        "classifications": set(),
        "blackline_exception_types": set(),
        "npcs": set(),
        "personas": {
            "brooke.phillips@starpm.com": "Brooke Phillips",
            "lisa.smith@starpm.com": "Lisa Smith",
            "sandra.allen@starpm.com": "Sandra Allen",
            "john.smith@starpm.com": "John Smith",
            "james.bennett@starpm.com": "James Bennett",
            "jaime.salinas@starpm.com": "Jaime Salinas",
            "randy.jones@starpm.com": "Randy Jones",
            "carlos.mendez@starpm.com": "Carlos Mendez",
            "patricia.nguyen@starpm.com": "Patricia Nguyen",
            "kevin.okafor@starpm.com": "Kevin Okafor",
            "elias.navarro@starpm.com": "Elias Navarro",
            "denise.morales@starpm.com": "Denise Morales",
            "teresa.wood@starpm.com": "Teresa Wood",
        },
        "services": ["airtable", "contacts", "gcalendar", "gmail", "hubspot", "linear",
                     "quickbooks", "slack"],

        # Routes per-universe behavior through the registry instead of a `universe ==`
        # branch. The three pre-V4 universes deliberately declare NEITHER flag so their
        # index output stays byte-identical (their tz literal is a preserved mislabel).
        "id_pattern_set": "starpm",
        "index_internal_by_domain": True,
        "index_tz_from_registry": True,
        "account_trap_check": False,
        "entity_name_to_id": {
            "star property management": "starpm", "starpm": "starpm", "star pm": "starpm",
        },
        "lifecycle_check_kind": "TX_rent_eviction",
        "lifecycle_states_closed": set(),
        "lifecycle_states_open": set(),

        "tool_param_traps": {
            "slack_send_message": {"content_field": "message", "wrong_fields": ["payload", "text"], "window": 100, "ignorecase": True},
            "create_draft": {"content_field": "body", "wrong_field": "content", "window": 100, "ignorecase": True},
            "save_issue": {"required": "team", "wrong": "teamId", "window": 100, "ignorecase": True},
            "save_comment": {"required": "issueId", "content_field": "body"},
            "create_records_for_table": {"required": "baseId", "also_required": "tableId"},
            "manage_crm_objects": {"required": "object_type", "also_required": "action"},
            "create_journal_entry": {"content_field": "properties"},
        },

        "landmines": [
            "No account-number trap, no retention codes, no classifications: single entity (starpm), no Records Vault. Files under Data/Files/ are read-only reference PDFs the agent reads directly.",
            "Near-duplicate decoy files: invoice-2026-419 vs invoice-2026-419-287; invoice-BILL-2026-0392 vs invoice-BILL-2026-0392-920; invoice-2026-481 vs 2026-481-makeready; agreement ...tanya-mitchell vs ...tanya-mitchell-2 (plus the separate reasonable-accommodation-lease-addendum); report-laspalmas-8d-qc-inspection vs -2; final-walk-clearance-las-palmas-8d-2026 vs -2; Las Vistas 9D carries two differently-named QC reports. Select the authoritative artifact, never the decoy.",
            "Cross-property Unit 14 ambiguity: 'Unit 14' is not unique (Rio Bend Unit 14, Sunset Ridge Unit 14, Unit 14 Tanya Mitchell Eviction). Disambiguate by property before acting.",
            "Semantic contradiction: Tanya Mitchell appears simultaneously in a fair-housing ESA accommodation track AND a full rent-to-eviction track. A task must not conflate the protected-accommodation posture with the eviction posture.",
            "Source-of-truth: Airtable (tblMakeReady, tblMaintenanceTickets) is the system of record for make-ready and maintenance work orders; Linear is explicitly secondary. HubSpot is the system of record for the leasing / applicant funnel. Never trust Linear for maintenance ground truth.",
            "Name collisions: Tony Reyes (staff) vs Tommy Reyes (tenant); Patricia Nguyen (persona) vs Patricia Lowe (Court Clerk); Kevin Okafor (persona) vs Jerome Okafor (referral partner); Lisa Smith and John Smith (two Smith personas).",
            "TX rent-to-eviction ladder (hardcoded): 5-day grace period, first late-rent notice, payment plan, 3-day pay-or-quit notice, eviction filing packet (rent ledger plus all prior notices plus payment-plan trail plus owner authorization), JP-court coordination with Court Clerk Patricia Lowe. HVAC failures in San Antonio summer are life-safety events.",
            "Persona-scope: 'my property' / 'my turns' binds to the persona's assigned property and Airtable coordinator field. Verify every rubric value is in the persona's scope.",
        ],
    },

    "harmonygames": {
        "name": "Harmony Games",
        "framework_version": "hg",
        "domain": "Mobile game studio (founder-led, remote-first)",
        "base_path": "HarmonyGames_Base_Universe",
        "docs_path": "Docs_harmonygames",
        "evals_path": "Evals_harmonygames",
        # Tool-catalog prefix 6_, SHARED with KeyStone and MoveOps.
        # Brookfield 8_, StarPM 7_, KeyStone/MoveOps/HarmonyGames 6_.
        # The 2026-08 upstream drop renumbered HG 5_ -> 6_, so HarmonyGames no
        # longer carries a distinct prefix; three distinct prefixes remain, not five.
        "tool_catalog": "HarmonyGames_Base_Universe/6_Server_Tools_Details.json",
        "persona_briefs": "HarmonyGames_Base_Universe/2_Persona_Briefs.md",
        "business_function_doc": "HarmonyGames_Base_Universe/3_Task_Categories_Business_Functions.md",
        "universe_one_pager": "HarmonyGames_Base_Universe/0_Universe_One-Pager.md",
        "universe_schema": "HarmonyGames_Base_Universe/7_Universe_Schema.json",
        "persona_acl_roster": "HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json",
        "tool_access_dir": "HarmonyGames_Base_Universe/Tool_Access",
        "qc_reference_path": "QC_Tasks/V5_HG_Buckets",

        # 2026-02-28 is a SATURDAY and the last day of February. Both matter: the universe
        # forbids routine weekday-business comms on a weekend, yet "today" is a weekend day.
        "today": "2026-02-28",
        "today_tz": "America/Chicago",
        "injection_window": ("2026-01-01", "2026-02-28"),
        "persona_email_domain": "harmonygames.co",
        "business_functions": [
            "Engineering & Live-Ops", "Product & Design", "Growth / UA / Marketing",
            "Founders / Exec / Strategy", "Finance / Legal / HR / Ops", "Analytics & Data",
        ],
        "business_function_weights": {
            "Engineering & Live-Ops": 0.25, "Product & Design": 0.20,
            "Growth / UA / Marketing": 0.15, "Founders / Exec / Strategy": 0.15,
            "Finance / Legal / HR / Ops": 0.15, "Analytics & Data": 0.10,
        },
        "tight_identifiers": [
            "channel names", "doc IDs", "issue IDs", "card IDs", "repo names", "PR numbers",
            "company names", "dollar amounts", "dates", "table names", "sheet ranges",
        ],
        "oe_service_map": {
            "issues": "linear", "tickets": "linear",
            "cards": "trello", "boards": "trello",
            "repos": "github", "pull_requests": "github", "commits": "github",
            "queries": "snowflake", "tables": "snowflake", "warehouse": "snowflake",
            "docs": "gdocs", "spreadsheets": "gsheets", "slides": "gslides",
            "files": "gdrive", "calendar_events": "gcal",
            "email_threads": "gmail",
            "chat": "slack", "channels": "slack",
            "wiki": "confluence", "pages": "confluence",
            "contacts": "contacts",
        },
        "cross_service_pairs": [
            ("gmail", "slack"), ("gmail", "gdrive"), ("slack", "linear"), ("slack", "trello"),
            ("github", "linear"), ("snowflake", "gsheets"), ("gdrive", "gdocs"),
            ("confluence", "github"), ("gcal", "gmail"), ("snowflake", "slack"),
        ],

        "retention_codes": set(),
        # 985 channels / 218 users: NOT enumerable, unlike the C001..C0NN sets elsewhere.
        # An empty set here means "do not validate channel IDs against a whitelist".
        "slack_channels": set(),
        "classifications": set(),
        "blackline_exception_types": set(),
        # NPC mailboxes observed in the shipped HG QC corpus (QC_Tasks/V5_HG_Buckets).
        # Harvested from the 10 shipped tasks, NOT from Services_Data, which is un-hydrated.
        # KNOWABLY INCOMPLETE - the real universe has 218 Slack users. This is an allowlist
        # that removes false positives; it is never an authority for absence.
        # "name@harmonygames.co" is excluded on purpose: a template placeholder, not a mailbox.
        "npcs": {
            "benjamin.clark@harmonygames.co",
            "felixyoung@harmonygames.co",
            "graham@harmonygames.co",
            "lauren@harmonygames.co",
            "lucas@harmonygames.co",
            "marcus.lee@harmonygames.co",
            "matthew@harmonygames.co",
            "megan@harmonygames.co",
            "michelle.carter@harmonygames.co",
            "morgan@harmonygames.co",
            "nathan@harmonygames.co",
            "oscar@harmonygames.co",
            "patrick@harmonygames.co",
            "peterlawson@harmonygames.co",
            "rachel@harmonygames.co",
            "ryan@harmonygames.co",
            "scott@harmonygames.co",
            "stevencarter@harmonygames.co",
            "thomas@harmonygames.co",
        },
        # All 17 authoring personas, read verbatim from 4_Persona_ACL_Roster.json.
        # Emails are IRREGULAR by design (arthur_blake -> blake@, julia_lawson -> jlawson@,
        # martin_walsh -> martin.walsh@) so they are transcribed, never derived from names.
        # Previously this held ONE entry, which made the v4_gates F2 persona check truthy
        # but wrong: the other 16 real personas were flagged as unknown-persona defects.
        "personas": {
            "blake@harmonygames.co": "Arthur Blake",
            "brian@harmonygames.co": "Brian Foster",
            "calvin@harmonygames.co": "Calvin Price",
            "claire@harmonygames.co": "Claire Morgan",
            "douglas@harmonygames.co": "Douglas",
            "frederick@harmonygames.co": "Frederick Stone",
            "jlawson@harmonygames.co": "Julia Lawson",
            "leonard@harmonygames.co": "Leonard Hayes",
            "marcus@harmonygames.co": "Marcus Bennett",
            "martin.walsh@harmonygames.co": "Martin Walsh",
            "oliver@harmonygames.co": "Oliver Brooks",
            "owen@harmonygames.co": "Owen Baker",
            "robert@harmonygames.co": "Robert",
            "samuel@harmonygames.co": "Samuel Turner",
            "simon@harmonygames.co": "Simon Walker",
            "victor@harmonygames.co": "Victor Barnes",
            "vincent@harmonygames.co": "Vincent Parker",
        },
        "services": ["confluence", "contacts", "gcal", "gdocs", "gdrive", "github", "gmail",
                     "gsheets", "gslides", "linear", "slack", "snowflake", "trello"],

        # Routes per-universe behavior through the registry instead of a `universe ==`
        # branch. The three pre-V4 universes deliberately declare NEITHER flag so their
        # index output stays byte-identical (their tz literal is a preserved mislabel).
        # 2026-02-28 is itself a Saturday; routine weekend business comms are a violation.
        "weekend_comms_rule": True,
        "id_pattern_set": "harmonygames",
        "index_internal_by_domain": True,
        "index_tz_from_registry": True,
        "account_trap_check": False,
        "entity_name_to_id": {
            "harmony games": "harmonygames", "harmonygames": "harmonygames",
        },
        "lifecycle_check_kind": "persona_acl",
        "lifecycle_states_closed": set(),
        "lifecycle_states_open": set(),
        # Docs_harmonygames/14_Persona_ACL.md (2026-08 drop) settles an ambiguity the
        # superseded 15_Persona_ACL.md carried. That older doc asserted "eight scoped
        # services" three times (:87, :129) while its own matrix marked Contacts "No" in
        # the scoped-reads column, and this registry reconciled toward eight. Upstream has
        # now corrected the prose to match the matrix: :61 enumerates the scoped seven,
        # and :52-53 states the unscoped group "contains exactly Contacts, GitHub,
        # Snowflake, Trello, Linear, and Confluence". Tasks_Template 9_Universe_inject.sql
        # independently confirms "Persona ACL is active for Gmail, Slack, GCal, and
        # Drive-family reads". 7 + 6 = 13. Reads only - :17 "Persona ACL does not govern
        # writes", and :134 forbids making an ACL-based write denial necessary to any
        # prompt, Oracle Event or rubric.
        "acl_scoped_services": ["gmail", "gcal", "gdrive", "gdocs", "gsheets", "gslides",
                                "slack"],
        "acl_unscoped_services": ["contacts", "github", "snowflake", "trello", "linear",
                                  "confluence"],
        "long_horizon_calls": (500, 1000),

        # Verified against HarmonyGames_Base_Universe/Tool_Access/*-tools.json, which
        # Guide:13 makes the capability authority.
        "tool_param_traps": {
            # TWO send tools with DIFFERENT text params. Unique to this universe.
            "slack_send_message": {"content_field": "text", "wrong_fields": ["payload", "message", "content"], "window": 100, "ignorecase": True},
            "slack_conversations_add_message": {"content_field": "payload", "wrong_fields": ["text", "message"], "window": 100, "ignorecase": True},
            "linear_create_issue": {"required": "team", "wrong": "teamId", "window": 100},
            "linear_create_comment": {"required": "issueId", "content_field": "body"},
            # bodyText, NOT body/content - differs from every other universe.
            "gdocs_create_document": {"content_field": "bodyText", "wrong_fields": ["body", "content"], "window": 100, "ignorecase": True},
        },

        "landmines": [
            "Gmail is READ-ONLY. All 27 gmail_* tools are read/label/trash operations; there is NO send, reply, compose or draft tool. 'Email the vendor' is not an available action, and a rubric that requires one is ungradeable. Weaker than StarPM, which at least has create_draft. Snowflake is likewise query/read-only.",
            "Two Slack send tools with DIFFERENT text parameters: slack_send_message uses `text`, slack_conversations_add_message uses `payload`. Both are valid. Never assume one param name across Slack.",
            "gdocs_create_document takes `bodyText`, not `body` or `content`.",
            "linear_create_issue takes `team`, not `teamId` (matches MoveOps, differs from Brookfield).",
            "Weekend rule vs today: routine Slack/Gmail business communication dated on a weekend is a temporal violation, and today (2026-02-28) IS a Saturday and the last day of February. Any 'today'-framed routine-comms ask is a live authoring hazard.",
            "Mid-quarter framing: 2026-02-28 is the second month of Q1/H1, so 'Q1 close' or 'Q1 results are final' is incoherent; Q1 still has a month to run.",
            "Persona emails are IRREGULAR by design (arthur_blake -> blake@, julia_lawson -> jlawson@, martin_walsh -> martin.walsh@). Docs_harmonygames/14_Persona_ACL.md: never construct, normalize or infer an email from a person's name. Resolve via 4_Persona_ACL_Roster.json.",
            "Slack has 985 channels and 218 users, so channel IDs are NOT enumerable against a whitelist the way C001..C0NN are in the other four universes.",
            "Persona ACL: seven services apply persona-scoped read filtering. A read performed under the wrong acting identity is an Excluded execution, not a pass or a fail.",
            "set_acting_user is environment configuration. It is never an Agent action, never Outcome/Process/OE, never complexity-bearing, and must receive no rubric credit.",
            "Explicit no-tool list: Firebase, BigQuery, App Store Connect, Airtable, QuickBooks, Stripe are business topics only, never directly queryable. Zero service overlap with the other four universes.",
        ],
    },
}


def get_universe_constants(universe_name: str) -> dict:
    """Return the constants dict for a universe. Raises KeyError on an unknown name.

    Absence must be loud, never inherited. The previous behaviour silently returned the
    Brookfield entry for any unrecognised string, so a typo in `_aux/Universe.txt`, or a
    universe registered without a matching FRAMEWORKS profile, produced Brookfield's today
    date, Brookfield's Slack whitelist and v3's density target applied to another
    universe's task, with no error at any layer.

    This is the same principle as Hydra's MISSING sentinel (reading an unset config value
    raises rather than resolving) and pydantic-settings' `extra='forbid'` (an unrecognised
    key is a validation error, not a silently dropped one).

    Every call site passes either detect_universe() output or a name already validated
    against list_universes(), so a raise here indicates a real defect rather than user
    input.
    """
    key = (universe_name or "").lower().strip()
    if key not in UNIVERSES:
        raise KeyError(
            f"unknown universe {universe_name!r}; registered: {sorted(UNIVERSES)}. "
            f"Register it in UNIVERSES; do not fall back to another universe's constants."
        )
    return UNIVERSES[key]


_KEYSTONE_SIGNALS = re.compile(
    r"\b(?:mortgage_los|TRID|loan\s+estimate|closing\s+disclosure|Keystone\s+Mortgage|keystonemortgage\.com|borrower|loan\s+officer|underwriting\s+condition|wholesale\s+lender|rate\s+lock|stripe_create_charge|stripe_create_refund|mortgage_los_\w+|filesystem_\w+)\b",
    re.IGNORECASE,
)
_BROOKFIELD_SIGNALS = re.compile(
    r"\b(?:oracle_gl|BlackLine|Records?\s+Vault|Brookfield\s+CPAs?|brookfieldcpas\.com|journal\s+entries|journal\s+entry|trial\s+balance|SAP\s+subledger|fiscal\s+period|northstar_legal|acme_cloud|AICPA_SQMS_7Y|IRS_TAX_7Y|late_post_authorization_id)\b",
    re.IGNORECASE,
)
_MOVEOPS_SIGNALS = re.compile(
    r"\b(?:MoveOps|moveops\.com|Elena\s+Rostova|PHMSA|hazmat|relocation\s+coordinator|stipend\s+platform|UrbanNest|Heartland\s+Movers|Swift\s+Relocations|Atlas\s+Corporate\s+Travel|Vectral\s+Systems|Canopy\s+Health|BrightLoop|Mosaic\s+Robotics|GreenStack\s+Energy|PivotPoint|NorthWind\s+Technologies|StormCloud|airtable_update_records|tblRelocations|tblStipends|ExpenseBot|auto-categorizer)\b",
    re.IGNORECASE,
)
_STARPM_SIGNALS = re.compile(
    r"\b(?:Star\s+Property\s+Management|starpm\.com|hubspot|quickbooks|gcalendar|make-ready|owner-relations|Brooke\s+Phillips|Patricia\s+Nguyen|Teresa\s+Wood)\b",
    re.IGNORECASE,
)

# SCORING signals only. The bare company name and its domain are deliberately NOT here.
# "Harmony Games" is an ordinary company name and Brookfield is an accounting firm with
# clients: a thin Brookfield input reading "Pay the Harmony Games invoice; remit to
# billing@harmonygames.co" scored hg=2 bf=0 and was routed to the wrong universe. A name
# The email DOMAIN is excluded for the same reason: a Brookfield task can legitimately
# cite a client's billing address. Name markers still
# participate in the short-circuit below, but only paired with a structural marker that
# cannot appear in prose about another company.
_HARMONYGAMES_SIGNALS = re.compile(
    r"\b(?:Persona_ACL_Roster|set_acting_user|"
    r"gslides_\w+|gsheets_\w+|gdocs_\w+|gdrive_\w+|gcal_\w+|snowflake_\w+|trello_\w+|"
    r"confluence_\w+)\b|MCP_Eval_V\d+_HarmonyGames",
    re.IGNORECASE,
)


def _write_marker(marker: Path, universe: str) -> None:
    """Best-effort cache write. `_aux/Universe.txt` is an optimization, not the answer.

    QC corpora are often read-only, and a detector that raises PermissionError on a
    read-only fixture cannot be used by read-only auditing tools. Detection is pure;
    only the cache is a side effect, so a failed write is silently tolerated.
    """
    try:
        marker.parent.mkdir(parents=True, exist_ok=True)
        marker.write_text(universe + "\n", encoding="utf-8")
    except OSError:
        pass


def detect_universe(task_dir: Path) -> str:
    """Auto-detect universe from task contents. Writes _aux/Universe.txt and returns the name.

    Highest-signal universe wins. Ties default to brookfield (back-compat).
    """
    task_dir = Path(task_dir)
    marker = task_dir / "_aux" / "Universe.txt"
    if marker.is_file():
        cached = marker.read_text(encoding="utf-8").strip().lower()
        if cached in UNIVERSES:
            return cached

    # Exclusive-marker short-circuit, BEFORE scoring.
    #
    # detect_universe sums raw regex hits over four files, and its highest-yield input is
    # 3_UniverseDataForThisTask.json[:50000]. HarmonyGames' copy of that file is a ~721-byte
    # POINTER, not data, so HarmonyGames is structurally starved of signal in the exact file
    # that dominates scoring for the other four. Combined with the tie-goes-to-brookfield
    # rule below, starvation would silently resolve to the wrong universe.
    #
    # These markers are verified to appear in ZERO bytes of the other four universes'
    # corpora (Validators/test_signal_exclusivity.py), so matching one is decisive and
    # cannot regress an existing universe.
    for candidate in ("1_Business_Function.txt", "2_Persona.txt", "5_Prompt.txt",
                      "3_UniverseDataForThisTask.json"):
        f = task_dir / candidate
        if f.is_file():
            text = f.read_text(encoding="utf-8", errors="ignore")
            # Require TWO DISTINCT markers, not one. A single case-insensitive
            # "Harmony Games" is not proof of universe: Brookfield is an accounting firm
            # with clients, and an ordinary future prompt like "reconcile the Harmony Games
            # invoice against the trust account" would otherwise reroute the whole task and
            # persist the wrong answer to _aux/Universe.txt. Exclusivity was verified against
            # today's corpora; prompts are authored by humans afterwards.
            # Require one NAME marker AND one STRUCTURAL marker, from disjoint families.
            # Exclusivity of the STRUCTURAL family against the other four universes' corpora
            # is asserted by Validators/test_signal_exclusivity.py.
            # Counting two name-family tokens was not independent evidence: `harmonygames`
            # is a substring of `harmonygames.co`, so an ordinary Brookfield prompt naming
            # a client "Harmony Games" and its billing address "@harmonygames.co" produced
            # two distinct tokens and hijacked the universe. A structural marker cannot
            # appear in prose about a third-party company.
            name_hit = re.search(r"harmonygames\.co|harmonygames|Harmony\s+Games",
                                 text, re.IGNORECASE)
            struct_hit = re.search(r"Persona_ACL_Roster|set_acting_user|"
                                   r"MCP_Eval_V\d+_HarmonyGames",
                                   text, re.IGNORECASE)
            if name_hit and struct_hit:
                _write_marker(marker, "harmonygames")
                return "harmonygames"

    scores = {"brookfield": 0, "keystone": 0, "moveops": 0, "starpm": 0, "harmonygames": 0}
    for candidate in ("1_Business_Function.txt", "2_Persona.txt", "5_Prompt.txt"):
        f = task_dir / candidate
        if f.is_file():
            text = f.read_text(encoding="utf-8", errors="ignore")
            scores["keystone"] += len(_KEYSTONE_SIGNALS.findall(text))
            scores["brookfield"] += len(_BROOKFIELD_SIGNALS.findall(text))
            scores["moveops"] += len(_MOVEOPS_SIGNALS.findall(text))
            scores["starpm"] += len(_STARPM_SIGNALS.findall(text))
            scores["harmonygames"] += len(_HARMONYGAMES_SIGNALS.findall(text))

    universe_data = task_dir / "3_UniverseDataForThisTask.json"
    if universe_data.is_file():
        sample = universe_data.read_text(encoding="utf-8", errors="ignore")[:50000]
        scores["keystone"] += len(_KEYSTONE_SIGNALS.findall(sample))
        scores["brookfield"] += len(_BROOKFIELD_SIGNALS.findall(sample))
        scores["moveops"] += len(_MOVEOPS_SIGNALS.findall(sample))
        scores["starpm"] += len(_STARPM_SIGNALS.findall(sample))
        scores["harmonygames"] += len(_HARMONYGAMES_SIGNALS.findall(sample))

    if all(v == 0 for v in scores.values()):
        # ZERO EVIDENCE. Measured across the repo, 40 of 122 task dirs reach this branch,
        # including ones that ship all four scored input files. Returning the default here
        # launders "no idea" into a confident answer, and the answer is then CACHED to
        # _aux/Universe.txt and read unconditionally forever after, so the mistake is
        # sticky and silent.
        #
        # The default is still returned for back-compat (callers expect a universe name,
        # and every existing regression anchor depends on it), but it is NO LONGER
        # PERSISTED: a marker written from zero evidence is indistinguishable from one
        # written from a confident detection, and that is the property that makes the
        # failure permanent. Leaving the cache unwritten means the next call re-derives
        # once real inputs are pasted.
        universe = "brookfield"
        return universe
    else:
        max_score = max(scores.values())
        winners = [u for u, s in scores.items() if s == max_score]
        if "brookfield" in winners:
            universe = "brookfield"
        else:
            universe = sorted(winners)[0]

    _write_marker(marker, universe)
    return universe


def list_universes() -> list:
    return sorted(UNIVERSES.keys())


# Per-framework behavioral profile, keyed by a universe's framework_version.
#
# THIS TABLE IS LOAD-BEARING. Consumers read it via get_framework_profile():
#   parse_trajectories.py  trajectory_layout, verifier_files, density_floor_avg_tool_calls
#   close_task.py          trajectory_layout
#   new_task.py            trajectory_layout
#   phase_ready.py         trajectory_layout
#   validate.py            (profile lookup)
# Verified by Validators/check_capability_registry.py (check C1), which fails if the
# consumer count ever drops to zero.
#
# Paths (docs_path / evals_path / qc_reference_path) deliberately do NOT live here:
# they are per-universe facts owned by UNIVERSES. Duplicating them let the two tables
# silently disagree, which is check C2.
FRAMEWORKS = {
    "v3": {
        "severity_map": {"overly_specific": "moderate", "overly_broad": "minor"},
        "model_under_test": "opus-4.8",
        "trajectory_dispositions": ["pass", "fail"],
        "pass_at_1_ceiling": 0.40,
        "slack_channels_enumerable": True,
        "working_dir_name": "Tasks",
        "acl_gate": False,
        "oe_grammar": ["standard"],
        "injection_difficulty_floor": None,
        "qc_binary_subdim_count": 10,
        "qc_dimension_count": 5,
        "qc_subdim_count": 24,
        "density_prompt_gate_calls": None,
        "density_prompt_gate_services": None,
        "density_target_services": None,
        "density_excluded_calls": [],
        "long_horizon_call_band": None,
        "universe_data_contract": "per_task_json",
        "rubric_balance_rule": "outcome_gt_process",
        # No Negative Criteria dimension in this framework's QC spec, and its vague-exemplar
        # ban covers the title only (validate.py V3_VAGUE_CONNECTOR). See the hg profile.
        "rubric_negative_criteria_gate": False,
        "rubric_vague_exemplar_scope": "title_only",
        "rubric_category_enum": {"outcome", "process"},
        "density_target": 50,
        "density_floor_avg_tool_calls": 40,
        "verifier_models": ["single"],
        "verifier_files": ["8_Verifier_Fails.txt"],
        "trajectory_layout": "flat",
        "extra_phases": [],
    },
    "v3.1": {
        "severity_map": {"overly_specific": "moderate", "overly_broad": "minor"},
        "model_under_test": "opus-4.8",
        "trajectory_dispositions": ["pass", "fail"],
        "pass_at_1_ceiling": 0.40,
        "slack_channels_enumerable": True,
        "working_dir_name": "Tasks",
        "acl_gate": False,
        "oe_grammar": ["standard"],
        "injection_difficulty_floor": None,
        "qc_binary_subdim_count": 10,
        "qc_dimension_count": 5,
        "qc_subdim_count": 24,
        "density_prompt_gate_calls": None,
        "density_prompt_gate_services": None,
        "density_target_services": None,
        "density_excluded_calls": [],
        "long_horizon_call_band": None,
        "universe_data_contract": "per_task_json",
        "rubric_balance_rule": "outcome_gt_process",
        # No Negative Criteria dimension in this framework's QC spec, and its vague-exemplar
        # ban covers the title only (validate.py V3_VAGUE_CONNECTOR). See the hg profile.
        "rubric_negative_criteria_gate": False,
        "rubric_vague_exemplar_scope": "title_only",
        "rubric_category_enum": {"outcome", "process"},
        "density_target": 50,
        "density_floor_avg_tool_calls": 40,
        "verifier_models": ["single"],
        "verifier_files": ["8_Verifier_Fails.txt"],
        "trajectory_layout": "flat",
        "extra_phases": [],
    },
    "v2.1": {
        "severity_map": {"overly_specific": "moderate", "overly_broad": "minor"},
        "model_under_test": "opus-4.8",
        "trajectory_dispositions": ["pass", "fail"],
        "pass_at_1_ceiling": 0.40,
        "slack_channels_enumerable": True,
        "working_dir_name": "Tasks",
        "acl_gate": False,
        "oe_grammar": ["standard"],
        "injection_difficulty_floor": None,
        "qc_binary_subdim_count": 10,
        "qc_dimension_count": 5,
        "qc_subdim_count": 24,
        "density_prompt_gate_calls": None,
        "density_prompt_gate_services": None,
        "density_target_services": None,
        "density_excluded_calls": [],
        "long_horizon_call_band": None,
        "universe_data_contract": "per_task_json",
        "rubric_balance_rule": "outcome_gt_process",
        # No Negative Criteria dimension in this framework's QC spec, and its vague-exemplar
        # ban covers the title only (validate.py V3_VAGUE_CONNECTOR). See the hg profile.
        "rubric_negative_criteria_gate": False,
        "rubric_vague_exemplar_scope": "title_only",
        "rubric_category_enum": {"outcome", "process"},
        "density_target": 50,
        "density_floor_avg_tool_calls": 40,
        "verifier_models": ["single"],
        "verifier_files": ["8_Verifier_Fails.txt"],
        "trajectory_layout": "flat",
        "extra_phases": [],
    },
    "hg": {
        # Severity is the PRE-swap ordering here, the REVERSE of StarPM's post-07/16 swap.
        "severity_map": {"overly_specific": "minor", "overly_broad": "moderate"},
        "model_under_test": "opus-4.7",
        # A read under the wrong acting identity is EXCLUDED: a third disposition that must be
        # subtracted before pass@1 and density are computed, not counted as a pass or a fail.
        "trajectory_dispositions": ["pass", "fail", "excluded"],
        "pass_at_1_ceiling": 0.40,
        "slack_channels_enumerable": False,   # 985 channels / 218 users: no derivable whitelist
        "working_dir_name": "Generated_Tasks",
        "acl_gate": True,
        "oe_grammar": ["standard", "batch"],
        "injection_difficulty_floor": 2.5,    # NOT StarPM's 3.5
        "qc_binary_subdim_count": 18,
        "qc_dimension_count": 7,
        "qc_subdim_count": 38,
        "density_prompt_gate_calls": 15,
        "density_prompt_gate_services": 2,
        "density_target_services": 3,
        # Only tool NAMES belong here, because the consumer matches on tool name.
        # The spec also excludes ACL-denied reads and retries against inaccessible
        # records, but those are ordinary calls (e.g. gmail_list_messages) whose RESULT
        # was a permission error - there is no tool named `acl_denied_reads`. Listing
        # them here would read as consumed while silently never firing, which is worse
        # than leaving them out. They need result inspection, which depends on the
        # `excluded` trajectory disposition; tracked as the trajectory_dispositions work.
        "density_excluded_calls": ["set_acting_user"],
        "long_horizon_call_band": (500, 1000),
        # HarmonyGames' 3_UniverseDataForThisTask.json is a ~721-byte POINTER, not
        # data. Truth is <base_path>/Services_Data/ overlaid by 4_Changelog.json.
        "universe_data_contract": "base_export_plus_changelog",
        # HarmonyGames is NOT "v5". It is v3-shaped SINGLE-model verification PLUS v4's
        # injection + submission_gate phases. A version ordinal would imply a successor
        # relationship to v4 that does not exist, so the key is the universe name.
        # HarmonyGames QC spec replaces the Outcome-majority rule with a flat binary
        # cap: Process <= 40% of the set, and zero Process is explicitly valid.
        "rubric_balance_rule": "process_max_40pct",
        # Negative Criteria (QC dimension 23) and the every-field Vague Exemplar scan
        # exist ONLY in the HarmonyGames spec. Grepping Docs/, Docs_keystone/,
        # Docs_moveops/ and Docs_starpm/ for "negative criteri", "criteria framing" and
        # "vague exemplar" returns nothing, and AGENTS.md rule 25 has each universe follow
        # its own spec, so these gate on the framework rather than running everywhere.
        "rubric_negative_criteria_gate": True,
        "rubric_vague_exemplar_scope": "all_fields",
        # The spec defines a 4-value enum, but a census of all 10 shipped HG tasks
        # (372 criteria, incl. 4 QC-PASSED tasks) found ZERO using it - every artifact
        # uses the lowercase 2-value form. Enforcing the spec enum alone would fail
        # every shipped task on a BINARY sub-dimension. Accept both; see HG-U7.
        "rubric_category_enum": {"outcome", "process",
                                 "Outcome 1.1", "Outcome 1.2", "Outcome 2.1", "Process"},
        "density_target": 40,
        "density_floor_avg_tool_calls": 15,
        "verifier_models": ["single"],
        "verifier_files": ["8_Verifier_Fails.txt"],
        "trajectory_layout": "flat",
        "extra_phases": ["injection", "submission_gate"],
    },
    "v4": {
        "severity_map": {"overly_specific": "moderate", "overly_broad": "minor"},
        "model_under_test": "opus-4.8",
        "trajectory_dispositions": ["pass", "fail"],
        "pass_at_1_ceiling": 0.40,
        "slack_channels_enumerable": True,
        "working_dir_name": "Tasks",
        "acl_gate": False,
        "oe_grammar": ["standard"],
        "injection_difficulty_floor": 3.5,
        "qc_binary_subdim_count": 10,
        "qc_dimension_count": 5,
        "qc_subdim_count": 24,
        "density_prompt_gate_calls": None,
        "density_prompt_gate_services": None,
        "density_target_services": None,
        "density_excluded_calls": [],
        "long_horizon_call_band": None,
        "universe_data_contract": "per_task_json",
        "rubric_balance_rule": "outcome_gt_process",
        # No Negative Criteria dimension in this framework's QC spec, and its vague-exemplar
        # ban covers the title only (validate.py V3_VAGUE_CONNECTOR). See the hg profile.
        "rubric_negative_criteria_gate": False,
        "rubric_vague_exemplar_scope": "title_only",
        "rubric_category_enum": {"outcome", "process"},
        # AGENTS.md: V4 design target is 40+ average tool calls.
        "density_target": 40,
        "density_floor_avg_tool_calls": 15,
        "verifier_models": ["opus", "gemini"],
        "verifier_files": ["8a_Verifier_Fails_Opus.txt", "8b_Verifier_Fails_Gemini.txt"],
        "trajectory_layout": "per_model",
        "extra_phases": ["injection", "submission_gate"],
    },
}


def get_framework_profile(universe_name: str) -> dict:
    """Return the framework profile for a universe's framework_version.

    Resolves the universe (brookfield=v3, keystone=v3.1, moveops=v2.1,
    starpm=v4) to its framework_version and looks that up in FRAMEWORKS.

    Raises KeyError on a universe whose framework_version is not a registered
    profile. That is a registry bug, not user input: every call site passes either
    detect_universe() output or a name already validated against list_universes(),
    so silently substituting another framework's behaviour would hide the defect
    rather than surface it.
    """
    version = get_universe_constants(universe_name).get("framework_version")
    if version not in FRAMEWORKS:
        raise KeyError(
            f"universe {universe_name!r} declares framework_version {version!r}, "
            f"which is not in FRAMEWORKS ({sorted(FRAMEWORKS)}). "
            f"Register the profile; do not fall back to another framework."
        )
    return FRAMEWORKS[version]


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 universes.py <task_dir>")
        print(f"Known universes: {list_universes()}")
        sys.exit(1)
    u = detect_universe(Path(sys.argv[1]))
    consts = get_universe_constants(u)
    print(f"Detected universe: {u}")
    print(f"Name: {consts['name']}")
    print(f"Domain: {consts['domain']}")
    print(f"Base path: {consts['base_path']}")
    print(f"Services: {consts['services']}")
    print(f"Slack channels: {sorted(consts['slack_channels'])}")
    print(f"NPCs: {sorted(consts['npcs'])}")


def canonical_rubric_category(value: str) -> str:
    """Map a stored rubric category to its parent bucket: `outcome` or `process`.

    HarmonyGames stores the guidelines' Outcome sub-categories directly in `category`
    (`Outcome 1.1` write-action result, `Outcome 1.2` action content, `Outcome 2.1` key fact
    in the final response, plus `Process`). Every other universe stores the flat two-value
    form. Both must count into the same two buckets, because the balance rules
    (Outcome-majority, or a Process <= 40% cap) are defined over the parent buckets.

    Single source of truth. `validate.py` and `v4_gates.py` both censused categories with
    their own copy; `validate.py` imports `v4_gates`, so the shared home has to be here.
    """
    v = (value or "").strip().lower()
    if v.startswith("outcome"):
        return "outcome"
    if v.startswith("process"):
        return "process"
    return v
