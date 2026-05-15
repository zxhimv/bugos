# Synthetic Output Pack Walkthrough

Status: synthetic demo only

This walkthrough demonstrates what a prepare-only `bugos` delivery can look like. It contains no real program, real domain, real target, real company, real account, real vulnerability, credential, payload, exploit, or submission instruction.

## Demo Inputs

Input file:

- `docs/demo/synthetic_program_brief.md`

Input constraints:

- synthetic placeholders only
- no real targets
- no live systems
- no credentials
- no personal data
- no evidence from real testing

## Expected Output Files

A prepare-only intake pack may include:

1. `program_profile.json`
2. `disqualifier_check.md`
3. `known_issue_map.md`
4. `program_score.json`
5. `work_order.json`
6. `manual_test_cards.md`
7. `evidence_manifest_template.json`
8. `report_draft_template.md`
9. `final_submission_check.json`

## Sample Program Profile Summary

- Program: Example Learning Platform Security Program
- Source: synthetic demo brief
- Scope state: placeholder-only, not authoritative
- Testing permission: not granted
- Final state: `BLOCK`
- Human review required: yes
- Automatic submission allowed: false

## Sample Disqualifier Summary

Blocking conditions:

- no authoritative real policy
- no confirmed real scope
- no evidence
- no human review
- no authorization for live testing
- no submission authorization

## Sample Known-Issue Summary

Excluded categories:

- low-impact UI observations without verified security impact
- duplicate or already documented synthetic issue classes
- anything requiring target interaction
- anything requiring payloads, exploitation, credentials, password-reset testing, or automated submission

## Sample Work Order Summary

Allowed work:

- review synthetic brief
- create prepare-only templates
- document blockers
- document human-review requirements

Disallowed work:

- target interaction
- scanning
- exploitation
- payload generation
- credential handling
- password-reset testing
- browser automation
- crawling
- automatic submission

## Sample Manual Test Card Format

Purpose: clarify whether a future separately authorized reviewer has enough scope information.

Preconditions:

- authoritative policy reviewed by a human
- in-scope assets confirmed
- sensitive data handling confirmed

Allowed manual observation:

- review redacted policy text and placeholders only

Evidence to collect:

- redacted policy excerpt reference
- reviewer notes
- blocker list

Stop conditions:

- missing authorization
- unclear scope
- any need for live target interaction
- any need for credentials, payloads, exploitation, or scanning

Human review checkpoint:

- human reviewer confirms whether the workflow remains blocked or may move to a separate authorized process

## Sample Final Submission Check

```json
{
  "status": "PREPARE_ONLY",
  "decision": "BLOCK",
  "ready": false,
  "ready_for_human_review": false,
  "automatic_submission_allowed": false,
  "network_access_used": false,
  "target_contacted": false,
  "scanners_used": false,
  "exploits_used": false,
  "payloads_used": false,
  "submission_performed": false
}
```

## Demo Boundary

This demo is not a bug report, not a security test, not a finding, not a proof of impact, and not a submission-ready artifact. It is a product demonstration of safe preparation structure only.
