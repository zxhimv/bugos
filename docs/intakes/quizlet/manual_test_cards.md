# Quizlet PREPARE_ONLY Manual Test Cards

Status: PREPARE_ONLY

These cards are planning prompts for a future, separately authorized human workflow. They are not instructions to test Quizlet now.

## Card 1: Authorization And Scope

Purpose: Confirm that current program rules permit any future human-led activity.

Preconditions:

- Authoritative policy has been reviewed by a human.
- In-scope and out-of-scope assets have been recorded locally.
- Account, data, rate-limit, and evidence-handling rules are understood.

Allowed manual observation:

- Read and record policy/scope statements from an authoritative source in a separately authorized workflow.
- Compare local notes against the confirmed scope without interacting with targets from this intake pack.

Evidence to collect:

- Policy snapshot reference.
- Scope confirmation date.
- Reviewer name or initials.
- Explicit notes on allowed and prohibited activity.

Stop conditions:

- Scope is unclear.
- Any activity would require credentials, password resets, automated traffic, exploit work, or payload strings.

Human review checkpoint:

- A human reviewer must confirm that the intake remains PREPARE_ONLY and that automatic_submission_allowed remains false.

## Card 2: Evidence Hygiene

Purpose: Plan how future evidence would be recorded without secrets or personal data.

Preconditions:

- Evidence format is approved by the program.
- Redaction requirements are understood.
- No third-party, student, classroom, payment, or private account data is collected.

Allowed manual observation:

- Review local evidence placeholders and redaction requirements.
- Confirm that any future evidence would be stored only after a separately authorized workflow.

Evidence to collect:

- Redaction checklist.
- Local artifact paths.
- Timestamp placeholders.
- Reviewer notes confirming no sensitive data is stored.

Stop conditions:

- Evidence would expose credentials, tokens, private content, personal data, or unauthorized account state.

Human review checkpoint:

- A human reviewer must verify that evidence placeholders do not contain real target data, secrets, credentials, or personal data.

## Card 3: Duplicate And Known-Issue Review

Purpose: Prevent premature or duplicate reporting.

Preconditions:

- Current known-issue guidance is available from an authoritative source.
- The draft observation is mapped to accepted and excluded categories.

Allowed manual observation:

- Compare local planning notes against authoritative duplicate and known-issue guidance.
- Mark unknown or ambiguous areas as blockers.

Evidence to collect:

- Known-issue source reference.
- Exclusion notes.
- Duplicate-risk notes.
- Reviewer decision trail.

Stop conditions:

- The observation appears excluded, duplicate, low-impact without accepted context, or unverifiable without prohibited actions.

Human review checkpoint:

- A human reviewer must confirm that no report draft advances while duplicate or exclusion status is unresolved.

## Card 4: Report Readiness

Purpose: Decide whether a future report can enter human review.

Preconditions:

- Scope is confirmed.
- Impact is clear.
- Evidence is complete and redacted.
- The final submission check has no policy/scope/evidence blockers in a separately authorized workflow.
- automatic_submission_allowed remains false.

Allowed manual observation:

- Review local report placeholders.
- Verify that summary, impact, scope confirmation, and evidence placeholders are complete and non-sensitive.

Evidence to collect:

- Completed redacted evidence manifest.
- Scope confirmation.
- Known-issue check result.
- Human-review notes.

Stop conditions:

- decision is BLOCK.
- ready is false.
- ready_for_human_review is false.
- automatic_submission_allowed is anything other than false.

Human review checkpoint:

- A human reviewer must confirm that the draft is still template-only until separately authorized human submission review is completed.

## Card 5: Submission Gate

Purpose: Preserve manual control over any future submission.

Preconditions:

- A human explicitly approves any future submission outside this PREPARE_ONLY intake.
- The final check is updated by an authorized reviewer.
- automatic_submission_allowed remains false.

Allowed manual observation:

- Review final_submission_check.json for blocking fields.
- Confirm that no automated submission path exists.

Evidence to collect:

- Human approval record for review readiness.
- Final blocker list.
- Safety-gate confirmation.

Stop conditions:

- Any automated submission path is requested.
- Any safety gate would need to be weakened.
- automatic_submission_allowed would need to become true.

Human review checkpoint:

- A human reviewer must confirm that submission, if ever pursued, is manual only and outside this PREPARE_ONLY intake pack.
