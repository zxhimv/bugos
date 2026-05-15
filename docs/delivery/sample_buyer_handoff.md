# bugos Sample Buyer Handoff Package

Status: draft for human review

This document implements REV-005 from `docs/revenue_backlog.md`. It is a sample handoff package for prepare-only deliveries. It is not legal advice, not a final contract, not a privacy policy, not a payment request, and not ready for external use without review.

## Delivery Type

Prepare-only delivery package.

## Delivery Summary

The buyer receives structured preparation artifacts based on redacted material. The delivery helps clarify scope blockers, evidence expectations, report structure, and human-review status. It does not include testing, scanning, exploitation, payload generation, credential handling, target interaction, or submission.

## Package Contents

For a Redacted Program Brief Intake Pack, include:

- `program_profile.json`
- `disqualifier_check.md`
- `known_issue_map.md`
- `program_score.json`
- `work_order.json`
- `manual_test_cards.md`
- `evidence_manifest_template.json`
- `report_draft_template.md`
- `final_submission_check.json`
- delivery summary
- redaction checklist
- buyer acceptance checklist

For an Evidence Hygiene and Report Readiness Review, include:

- evidence hygiene notes
- redaction notes
- report-readiness notes
- known-issue or duplicate-risk notes
- final human-review checklist
- delivery summary
- buyer acceptance checklist

## Delivery Checklist

Before delivery, confirm:

- all files are prepare-only
- no real credentials are included
- no tokens, cookies, or session values are included
- no payment, classroom, health, government-ID, or third-party personal data is included
- no exploit steps are included
- no payload strings are included
- no scanner output is included
- no target interaction is claimed
- no submission is claimed
- `automatic_submission_allowed` remains `false`

## Redaction Checklist

The buyer should verify that the delivery does not expose:

- private individual names unless necessary and authorized
- email addresses
- phone numbers
- account identifiers
- tokens or secrets
- session identifiers
- private messages
- payment data
- classroom or student data
- third-party personal data
- unredacted screenshots

## Buyer Review Checklist

The buyer must review:

- whether the supplied source material was authorized
- whether scope assumptions are accurate
- whether blockers are complete
- whether any real-world action is still blocked
- whether evidence handling is safe
- whether a qualified human reviewer is required before next steps
- whether the final decision remains `BLOCK` or `NEEDS_HUMAN_REVIEW`

## Acceptance Criteria

The delivery can be accepted as prepare-only if:

- all expected artifacts are present
- all sensitive data has been redacted or omitted
- no unsafe capability is included or implied
- no automatic submission is included or implied
- no finding, payout, revenue, or acceptance guarantee is made
- the buyer understands that real-world work remains separate and requires authorization

## Rejection Conditions

The buyer should reject or request correction if:

- unredacted sensitive data appears
- the delivery implies authorization for real testing
- the delivery implies target interaction occurred
- the delivery contains payloads, exploit steps, scanner output, or credentials
- the delivery claims guaranteed validity, payout, or income
- `automatic_submission_allowed` is true anywhere

## Buyer Acceptance Statement

`I confirm that I have received a prepare-only delivery package. I understand that it does not include target testing, scanning, exploitation, payload generation, credential handling, password-reset testing, browser automation, crawling, automated submission, legal advice, or any guarantee of valid findings, payout, revenue, or acceptance. I remain responsible for authorization, legal review, privacy review, real-world testing decisions, and any manual submission decision outside bugos.`

## Operator Completion Statement

`This delivery was prepared from redacted material only. It is prepare-only. No target interaction, scanning, exploitation, payload generation, credential handling, password-reset testing, browser automation, crawling, outreach automation, payment automation, or automatic submission was performed.`

## External-Use Warning

This sample handoff must be reviewed for legal, tax, privacy, business, consumer/business, and liability requirements before external use.
