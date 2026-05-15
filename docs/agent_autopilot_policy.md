# Agent Autopilot Policy

Status: active policy draft

This policy defines the maximum safe autonomy level for AI coding agents working on `bugos`.

## Baseline

The repository currently supports offline-first preparation work only. Agents must preserve that design. Autonomy is allowed for local validation, documentation, tests, and small safety-preserving patches. Autonomy is not allowed for real-world security testing, target interaction, scanning, exploit work, payload generation, credential handling, or submission.

## Autonomy Levels

### Level 0: Read-only review

Allowed:

- Inspect repository files.
- Summarize risks.
- Propose changes.

No writes.

### Level 1: Local safe patch

Allowed:

- Documentation-only patches.
- Local fixture corrections.
- Local validation scripts.
- Test additions for already-existing local behavior.

Blocked:

- New dependencies.
- Runtime capability expansion.
- Any network or target-facing behavior.

### Level 2: Draft PR

Allowed:

- Create a branch.
- Commit small reviewable changes.
- Open Draft PR.

Blocked:

- Merge.
- Auto-merge.
- Direct push to `main` unless explicitly authorized for a narrow exception.

### Level 3: Release candidate support

Allowed only with explicit human instruction:

- Changelog update for a concrete release.
- Version bump.
- Release notes.

Blocked:

- Publishing.
- Submission automation.
- Any weakening of safety gates.

## Non-Negotiable Invariants

- `automatic_submission_allowed` remains `false`.
- `decision` remains `BLOCK` or `NEEDS_HUMAN_REVIEW` only.
- No `ALLOW` decision state.
- No scanner, exploit, payload, credential, password-reset, crawler, browser-automation, or target-contact feature.
- No network functionality.
- No merge without explicit user approval.

## Self-Check Before Any Commit

Run, if available:

```bash
python -m pytest -q
python3 scripts/check_safety_invariants.py
```

Validate changed JSON files individually:

```bash
python3 -m json.tool <changed-file.json>
```

If pytest is unavailable, report the exact blocker. Do not install dependencies without explicit authorization.

## Self-Adjustment Rules

When an agent detects uncertainty, missing context, failed tests, or potential safety drift, it must self-adjust by reducing autonomy:

- Level 2 to Level 1 if PR creation is unsafe or unavailable.
- Level 1 to Level 0 if changes risk touching safety boundaries.
- Stop completely if the task would require target interaction, payloads, exploits, scanners, credentials, secrets, or submission.

## No-Change Rule

If no concrete defect exists, the correct outcome is:

`No change recommended.`

Do not create housekeeping PRs for cosmetic improvement.