# Revenue Engine Policy

Status: draft guardrail

This document defines how `bugos` may support revenue work without becoming an unsafe autonomous security actor.

## Core Rule

`bugos` may help prepare, package, validate, document, and sell safe local workflows. It must not autonomously perform real-world security testing, target interaction, scanning, exploitation, payload generation, credential handling, password-reset actions, or submission.

## Allowed Revenue Paths

### 1. Local prepare-only intake service

Offer a service that turns a redacted program brief into:

- program profile
- disqualifier check
- known-issue map
- program score
- work order
- manual test cards
- evidence manifest template
- report draft template
- final submission check

Boundary: planning only. No target contact. No vulnerability claim. No submission.

### 2. QA and evidence-readiness package

Offer local review for authorized researchers or internal teams:

- scope clarity review
- evidence hygiene checklist
- redaction checklist
- final human-review gate
- report template quality review

Boundary: no exploit advice, no payloads, no bypass instructions, no scanning instructions.

### 3. Compliance-first report preparation toolkit

Offer `bugos` as an offline workflow tool for teams that already have their own authorized findings and need structured reporting support.

Boundary: the customer must provide authorization and evidence. `bugos` does not verify live targets.

### 4. Documentation and training product

Offer templates, checklists, and training material about safe bug bounty operations:

- scope discipline
- evidence redaction
- duplicate-risk reduction
- final review workflows
- safety gates

Boundary: educational and process-focused only.

## Prohibited Revenue Paths

The following are not allowed:

- Autonomous bounty hunting.
- Target discovery or scanning as a service.
- Exploit development as a service.
- Payload packs.
- Credential testing.
- Account takeover workflows.
- Password-reset testing.
- Automated report submission.
- Guaranteed bounty claims.
- Revenue claims based on unauthorized access.

## Codex Autonomy For Revenue Work

Codex may autonomously prepare:

- landing-page copy
- pricing drafts
- README improvements
- safe demo briefs
- service descriptions
- documentation
- issue templates
- local tests for safety checks
- local validation helpers

Codex must stop before:

- contacting prospects
- sending emails
- creating invoices
- accepting payment
- making financial claims
- making legal guarantees
- interacting with third-party targets
- submitting bug reports
- changing safety gates

## Money-Gate Checklist

Before any revenue-facing material is used externally, human review must confirm:

- No claim that `bugos` autonomously earns bounties.
- No promise of guaranteed income.
- No promise of guaranteed valid findings.
- No target-interaction capability is implied.
- No scanner, exploit, payload, credential, or submission feature is marketed.
- `automatic_submission_allowed` remains false.
- The offer is framed as local preparation, QA, evidence hygiene, and process support.

## Safe Positioning Statement

Use this positioning by default:

`bugos is an offline-first preparation and review tool for authorized security workflows. It helps structure scope, evidence, reports, and human-review gates. It does not scan, exploit, contact targets, handle credentials, or submit reports.`

## Stop Conditions

Stop revenue work if a task requires:

- real program policy scraping without authorization
- target testing
- payloads or exploit instructions
- private customer data without a data-handling plan
- payment setup
- outreach automation
- claims about guaranteed profit or guaranteed bounty outcomes

## Operating Principle

Revenue must come from safe preparation, documentation, QA, and workflow quality—not from autonomous target interaction or automated bounty submission.
