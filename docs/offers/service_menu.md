# bugos Safe Service Menu

Status: draft for human review

This document implements REV-002 from `docs/revenue_backlog.md`. It turns `bugos` into safe, sellable offers. It is not legal, tax, or financial advice. It must be reviewed before external use.

## Positioning

`bugos` is an offline-first preparation and review workflow for authorized security operations. It helps structure redacted program briefs, scope blockers, evidence hygiene, report drafts, and final human-review gates. It does not scan, exploit, contact targets, handle credentials, run payloads, or submit reports.

## Global Boundaries

These boundaries apply to every offer:

- Prepare-only unless separately reviewed by a qualified human.
- Human-review required before any real-world action.
- No automatic submission.
- `automatic_submission_allowed` remains `false`.
- No income, payout, or valid-finding guarantee.
- No legal, tax, or financial advice.
- No secrets, credentials, tokens, cookies, session data, payment data, classroom data, or third-party personal data.

## Offer 1: Redacted Program Brief Intake Pack

### Service Description

Transforms a redacted program brief or policy excerpt into a structured local intake pack. The goal is to clarify scope, blockers, known-issue uncertainty, evidence expectations, and final human-review status before any manual work begins.

### Scope

Included:

- prepare-only program analysis
- scope and uncertainty extraction
- disqualifier review
- known-issue and duplicate-risk mapping
- final readiness gate

Excluded:

- target testing
- scanning
- exploitation
- payload generation
- credential handling
- password-reset testing
- browser automation or crawling
- automated submission
- legal advice

### Buyer Prerequisites

- Buyer provides a redacted program brief or policy excerpt.
- Buyer confirms they are authorized to use the provided material.
- Buyer removes secrets, credentials, tokens, cookies, personal data, and private third-party data before delivery.
- Buyer accepts that the result is preparation only.

### Output Artifacts

- `program_profile.json`
- `disqualifier_check.md`
- `known_issue_map.md`
- `program_score.json`
- `work_order.json`
- `manual_test_cards.md`
- `evidence_manifest_template.json`
- `report_draft_template.md`
- `final_submission_check.json`

### Pricing Draft

- Basic: 49-99 EUR per redacted intake pack.
- Standard: 149-299 EUR with one manual QA pass.
- Team/custom: quote-based.

### Acceptance Criteria

- All expected artifacts delivered.
- `automatic_submission_allowed` remains `false`.
- Final status remains `BLOCK` or `NEEDS_HUMAN_REVIEW`.
- No target, payload, credential, or submission capability is included.

## Offer 2: Evidence Hygiene and Report Readiness Review

### Service Description

Reviews already-authorized, buyer-provided materials for redaction hygiene, report structure, known-issue ambiguity, evidence completeness, and final human-review readiness.

### Scope

Included:

- evidence redaction checklist
- scope confirmation checklist
- duplicate and known-issue review checklist
- report structure review
- final human-review gate

Excluded:

- validating live targets
- creating exploit steps
- writing payload strings
- handling secrets, credentials, tokens, cookies, or session data
- submitting reports
- making validity or payout guarantees

### Buyer Prerequisites

- Buyer already has authorization for the underlying work.
- Buyer provides only redacted evidence or placeholders.
- Buyer confirms no private third-party data is included.
- Buyer accepts that real submission remains manual and outside `bugos`.

### Output Artifacts

- evidence hygiene checklist
- redaction checklist
- report-readiness notes
- known-issue/duplicate-risk notes
- final human-review checklist

### Pricing Draft

- Basic review: 99-199 EUR.
- Standard review: 249-499 EUR.
- Team/custom: quote-based.

### Acceptance Criteria

- Sensitive data issues are flagged.
- Missing scope/evidence areas are explicit.
- Report remains marked as draft/template until human approval.
- No report is submitted automatically.

## Offer 3: Bug Bounty Operations QA Template Pack

### Service Description

Provides reusable prepare-only templates for researchers and teams that want a safer internal intake and report-readiness workflow.

### Scope

Included:

- prepare-only intake templates
- evidence manifest templates
- final submission check templates
- redaction checklist
- human-review workflow
- safety-gate checklist

Excluded:

- automated testing
- target discovery
- scanner configuration
- exploit guidance
- payload guidance
- credential workflows
- submission automation

### Buyer Prerequisites

- Buyer uses the templates only in authorized workflows.
- Buyer performs independent legal and program-policy review.
- Buyer keeps automatic submission disabled.

### Output Artifacts

- reusable template bundle
- short usage guide
- safety checklist
- external-review checklist

### Pricing Draft

- Digital template pack: 29-79 EUR.
- Extended pack with walkthrough: 99-149 EUR.

### Acceptance Criteria

- Templates are clearly marked prepare-only.
- No unsafe capability is implied.
- No income, payout, or finding validity guarantee is made.

## External-Use Checklist

Before using this menu externally:

- Review legal wording.
- Review tax and invoicing requirements.
- Review consumer/business distinction.
- Confirm privacy and data-handling notice.
- Confirm no guarantee claims are made.
- Confirm no unsafe capability is implied.
- Confirm pricing and delivery terms separately.

## Safe CTA Draft

`Send a redacted program brief, and I will prepare a local-only intake pack that clarifies scope blockers, evidence requirements, report structure, and human-review gates. No target testing, scanning, exploit work, payload generation, credential handling, or submission is included.`
