# bugos Buyer Handoff Checklist

Status: draft for human review

This checklist supports REV-001 and REV-002. It is used when delivering prepare-only service outputs to a buyer.

## Delivery Summary

The delivery is prepare-only. It does not authorize or perform testing, scanning, exploitation, payload generation, credential handling, target interaction, or report submission.

## Buyer Input Confirmation

Before delivery, confirm:

- The buyer provided redacted material only.
- The buyer confirmed authorization to use the material.
- No secrets, credentials, tokens, cookies, session data, payment data, classroom data, or third-party personal data were provided.
- No live target interaction was requested or performed.

## Delivered Artifacts

For Redacted Program Brief Intake Pack:

- `program_profile.json`
- `disqualifier_check.md`
- `known_issue_map.md`
- `program_score.json`
- `work_order.json`
- `manual_test_cards.md`
- `evidence_manifest_template.json`
- `report_draft_template.md`
- `final_submission_check.json`

For Evidence Hygiene and Report Readiness Review:

- evidence hygiene checklist
- redaction checklist
- report-readiness notes
- known-issue/duplicate-risk notes
- final human-review checklist

## Required Buyer Review

The buyer must review:

- scope assumptions
- unknowns and blockers
- disallowed activity
- evidence redaction status
- final decision state
- human-review requirements

## Non-Negotiable Gates

- `automatic_submission_allowed` remains `false`.
- No automatic submission is included.
- Real-world testing decisions remain with the buyer.
- Report submission remains manual and outside `bugos`.
- No guarantee is made for valid findings, payouts, revenue, or acceptance.

## Acceptance Statement Draft

`I confirm that this delivery is a prepare-only workflow package. I understand that it does not include target testing, scanning, exploitation, payload generation, credential handling, password-reset testing, automated submission, legal advice, or a guarantee of valid findings or bounty outcomes.`

## External-Use Warning

This checklist must be reviewed for legal, tax, privacy, consumer/business, and liability implications before external use.
