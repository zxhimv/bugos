# Revenue Autopilot Stop Check

Status: draft for human review

This document implements REV-010 from `docs/revenue_backlog.md`.

## Purpose

The revenue-autopilot stop check prevents Codex or any other agent from creating arbitrary revenue, housekeeping, or architecture PRs after the safe preparation baseline is complete.

## Local Command

Run:

```bash
python3 scripts/check_revenue_autopilot.py
```

## Expected Outcome After Baseline Completion

When the safe revenue preparation files exist and safety markers are present, the correct autonomous outcome is:

```text
No change recommended unless a concrete reviewed business/legal/privacy gap is identified.
```

## What Counts As A Concrete Gap

A new PR may be justified only if there is a specific reviewed issue such as:

- missing safety wording
- missing redaction boundary
- outdated pricing hypothesis after human review
- legal/privacy reviewer feedback
- broken CI safety check
- missing required artifact for an already approved service package

## What Does Not Justify A PR

Do not create PRs for:

- general polish
- broad housekeeping
- speculative architecture
- more templates without a buyer/use-case signal
- external publication
- outreach automation
- payment automation
- scanner, exploit, payload, credential, or target-interaction capability

## Stop Conditions

Stop immediately if the next step would require:

- external publication
- sending messages
- collecting payment
- issuing invoices
- legal claims
- processing private data
- contacting targets
- testing targets
- scanning
- exploiting
- payload generation
- credential handling
- report submission
- changing `automatic_submission_allowed`

## Required Agent Final Report

When stopping, the agent should report:

- Summary
- Existing baseline files found
- Checks run
- Safety gates unchanged/changed
- New risks
- Open points
- PR/commit recommended: no
- Next recommended action: human review before external use

## Operating Principle

After REV-001 through REV-009 are in place, the default state is not more generation. The default state is review, validation, and controlled external-readiness work by a human.
