# bugos Core Offer

Status: draft for human review

This document implements REV-001 from `docs/revenue_backlog.md`.

## One-Paragraph Positioning

`bugos` is an offline-first preparation and review workflow for authorized security researchers and teams. It turns redacted program material into structured scope, blocker, evidence, report, and final human-review artifacts. It helps reduce wasted effort and unsafe ambiguity before any manual work begins. It does not scan, exploit, contact targets, handle credentials, run payloads, or submit reports.

## Core Offer Name

Redacted Program Brief Intake Pack

## Core Buyer

The best-fit buyer is an authorized researcher or small security team that already works under a valid program policy and wants cleaner pre-work before manual testing or report preparation.

Secondary buyers:

- independent bug bounty researchers who want scope discipline
- security leads who want consistent intake quality
- small teams that need evidence and report-readiness templates
- operators who want a conservative human-review gate before action

## Included Artifacts

The core offer includes the following prepare-only artifacts:

1. `program_profile.json`
2. `disqualifier_check.md`
3. `known_issue_map.md`
4. `program_score.json`
5. `work_order.json`
6. `manual_test_cards.md`
7. `evidence_manifest_template.json`
8. `report_draft_template.md`
9. `final_submission_check.json`

## Included Work

- Review a redacted program brief or policy excerpt provided by the buyer.
- Extract scope, blockers, and ambiguous areas.
- Identify disqualifiers and known-issue review needs.
- Produce prepare-only manual review cards.
- Provide evidence hygiene and report-readiness templates.
- Preserve a final human-review gate.

## Excluded Work

The offer excludes:

- target interaction
- scanning
- exploitation
- payload generation
- credential testing or handling
- token, cookie, or session handling
- password-reset testing
- social engineering
- DoS, stress, load, or rate-limit testing
- browser automation or crawling
- automatic submission
- legal advice
- guaranteed finding validity
- guaranteed payout or income

## Buyer Prerequisites

The buyer must confirm:

- They are authorized to work with the supplied program material.
- Input has been redacted before delivery.
- No secrets, credentials, tokens, cookies, session data, payment data, classroom data, or third-party personal data are included.
- The buyer remains responsible for real-world authorization, testing decisions, and submission decisions.

## Acceptance Criteria

The core offer is complete when:

- All included artifacts are delivered.
- The final decision remains `BLOCK` or `NEEDS_HUMAN_REVIEW`.
- `automatic_submission_allowed` remains `false`.
- Scope unknowns are explicit.
- Disallowed activity is clearly documented.
- Evidence placeholders contain no real secrets or personal data.
- Report material is clearly marked as template/preparation only.
- Human review remains mandatory before any real-world action.

## Safe CTA

Send a redacted program brief. I will prepare a local-only intake pack that clarifies scope blockers, evidence requirements, report structure, and human-review gates. No testing, scanning, exploitation, credential handling, target contact, or submission is included.

## External-Use Warning

This offer draft must be reviewed before external use for legal, tax, privacy, consumer/business, pricing, and liability implications.
