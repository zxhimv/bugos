# bugos Data Handling Notice

Status: draft for legal/privacy review

This document implements REV-006 from `docs/revenue_backlog.md`. It is a working draft, not a final privacy policy, not legal advice, and not ready for external publication without qualified review.

## Purpose

`bugos` is designed for offline-first preparation and review workflows. It should operate on redacted material only. The goal is to minimize data exposure while preparing scope, evidence, report, and human-review artifacts.

## Data-Minimization Rule

Use the smallest amount of information needed to prepare the requested artifact. Prefer placeholders, summaries, hashes, local references, and redacted excerpts over raw sensitive content.

## Allowed Input

Allowed input should be limited to:

- redacted program briefs
- redacted policy excerpts
- non-sensitive scope notes
- placeholder asset names
- synthetic examples
- non-sensitive report structure notes
- local file names without secrets

## Prohibited Input

Do not provide or store:

- passwords
- API keys
- tokens
- cookies
- session values
- private keys
- recovery codes
- credentials
- payment data
- classroom or student data
- health data
- government identification data
- third-party personal data
- private account content
- unredacted screenshots containing personal data
- live target secrets or confidential customer data

## Redaction Requirements

Before any material is used with `bugos`, redact:

- names of private individuals unless necessary and authorized
- email addresses
- phone numbers
- account identifiers
- IP addresses where not necessary
- tokens and secrets
- session identifiers
- internal URLs where not necessary
- private messages or private account content
- payment, classroom, health, or government-ID information

## Local Storage Expectations

- Keep files local where possible.
- Store only redacted inputs and generated prepare-only outputs.
- Do not commit secrets or sensitive evidence.
- Do not use public repositories for private customer materials.
- Do not include real target data in fixtures or demos.

## Evidence Handling

Evidence manifests should use placeholders unless a separate authorized and reviewed workflow allows otherwise.

Evidence entries should record:

- local path or placeholder reference
- redaction status
- reviewer
- timestamp
- description
- notes

Evidence entries should not contain secrets, credentials, tokens, cookies, private personal data, or unauthorized account content.

## Buyer Responsibilities

The buyer remains responsible for:

- ensuring they are authorized to use the supplied material
- redacting material before delivery
- excluding secrets and personal data
- confirming legal and program-policy requirements
- deciding whether any real-world action is permitted
- deciding whether any report is submitted manually outside `bugos`

## Operator Responsibilities

The operator should:

- reject unredacted sensitive material
- request redacted replacement material where needed
- avoid copying unnecessary data into outputs
- keep `automatic_submission_allowed` false
- avoid target interaction, scanning, exploitation, payload generation, credential handling, and submission
- flag uncertainty as a blocker

## Retention Draft

Suggested default retention before legal review:

- keep only the final redacted delivery package
- delete unneeded working copies
- do not retain secrets or unredacted evidence
- document deletion if sensitive material was received by mistake

## Incident Handling Draft

If prohibited input is received:

1. Stop work.
2. Do not process the material further.
3. Notify the buyer that redacted replacement material is required.
4. Delete or quarantine the prohibited material according to the reviewed retention process.
5. Record that work resumed only after safe replacement material was provided.

## External-Use Warning

This draft must be reviewed for applicable privacy, security, contractual, tax, and business requirements before external use.
