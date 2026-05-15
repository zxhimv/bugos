# bugos Terms of Use Notes

Status: draft for legal review

This document implements REV-007 from `docs/revenue_backlog.md`. It is not a final terms-of-use document, not legal advice, and not ready for external use without qualified review.

## Purpose

These notes define safe terms boundaries for `bugos` as an offline-first preparation and review workflow. The goal is to support authorized, human-reviewed, prepare-only security operations without enabling unsafe automation or unauthorized activity.

## Permitted Use Summary

A user may use `bugos` to:

- organize redacted program material
- create prepare-only intake artifacts
- document scope uncertainty
- identify disqualifiers and blockers
- prepare evidence hygiene templates
- prepare report draft templates
- structure human-review gates
- use synthetic demo material
- improve local process quality

## Prohibited Use Summary

A user must not use `bugos` to:

- interact with targets without authorization
- scan third-party systems
- exploit systems
- generate or run payloads
- test credentials
- collect credentials, tokens, cookies, or session data
- perform password-reset testing
- conduct social engineering
- conduct DoS, stress, load, or rate-limit testing
- crawl or automate browsers against real targets
- submit reports automatically
- bypass human review
- process unredacted personal or sensitive data
- claim guaranteed findings, payouts, revenue, or acceptance

## Authorization Requirement

Users are responsible for confirming that any real-world security work is authorized by the relevant program, organization, customer, or system owner. `bugos` does not grant authorization and does not verify live scope.

## Human Responsibility Statement

`bugos` produces preparation and review artifacts only. A qualified human remains responsible for all real-world decisions, including whether work is authorized, whether evidence is safe to store, whether a report is accurate, and whether any submission should occur manually outside `bugos`.

## No-Guarantee Statement

No guarantee is made that use of `bugos` will produce valid findings, accepted reports, bounty payouts, revenue, or any specific business outcome.

## No Legal or Tax Advice

`bugos` materials are not legal, tax, financial, or compliance advice. Users should obtain appropriate professional advice before relying on the materials externally.

## Data Handling Statement

Users must provide redacted material only. Users must not provide secrets, credentials, tokens, cookies, session data, payment data, classroom data, government identification data, health data, or third-party personal data.

## Submission Boundary

`automatic_submission_allowed` must remain `false`. `bugos` does not provide automatic submission. Any report submission, if pursued, must be manual, separately authorized, and outside the prepare-only workflow.

## Capability Boundary

`bugos` is not a scanner, exploit framework, payload generator, credential-testing tool, target-interaction tool, browser-automation agent, crawler, or submission bot.

## Customer Material Boundary

If customer material is received, only redacted and authorized material should be processed. If prohibited material is received, work should stop until safe replacement material is provided.

## Draft Acceptance Language

`By using this workflow, I confirm that I will provide redacted, authorized material only; I will not use the workflow for unauthorized testing, scanning, exploitation, payload generation, credential handling, password-reset testing, target interaction, or automated submission; and I understand that all real-world action requires separate human review and authorization.`

## External-Use Warning

These notes must be reviewed and converted into proper terms by a qualified professional before external use.
