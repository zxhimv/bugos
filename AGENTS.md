# AGENTS.md

Repository: `bugos`

This file defines binding instructions for AI coding agents working in this repository. Follow these instructions before local preferences, inferred improvements, or broad refactoring instincts.

## Project Purpose

`bugos` is an offline-first QA, scope, evidence, and report-preparation helper for authorized Bugcrowd-style work. It is not a scanner, exploit framework, payload generator, target-interaction tool, or submission bot.

## Permanent Safety Invariants

These invariants are mandatory and must not be weakened:

- No network functionality.
- No real target interaction.
- No scanners.
- No exploit execution or exploit-development workflow.
- No payload generation.
- No credential tests, credential retrieval, token handling, or password-reset actions.
- No social-engineering workflows.
- No DoS, stress, load, or rate-limit testing against third-party systems.
- No browser automation or crawling against real targets.
- No automatic submission.
- `automatic_submission_allowed` must remain `false` wherever present.
- Final decisions may only be `BLOCK` or `NEEDS_HUMAN_REVIEW`.
- Human review remains mandatory before any real-world security action or submission.

## Allowed Autonomous Work

Agents may work autonomously only on low-risk local repository tasks:

1. Inspect repository structure and current branch state.
2. Run local tests if the environment already supports them.
3. Validate JSON, Markdown, and local fixtures.
4. Improve documentation only when a concrete defect or ambiguity exists.
5. Add or adjust local-only tests for existing safety behavior.
6. Add small local validation helpers that do not introduce runtime product capabilities.
7. Open Draft PRs for small, reviewable changes when network/push capability is available.

## Prohibited Autonomous Work

Agents must not autonomously:

- Merge pull requests.
- Push directly to `main`, unless the user explicitly accepts a direct-main exception in the current task.
- Add dependencies.
- Add network, scanner, exploit, payload, credential, password-reset, crawling, browser-automation, or submission functionality.
- Contact any Bugcrowd program, target, domain, endpoint, API, account, or external policy page from inside this repo workflow.
- Use real secrets, credentials, tokens, cookies, session data, private user data, classroom data, payment data, or third-party personal data.
- Change safety decisions to an allowed state.
- Create broad architecture, housekeeping, or refactoring PRs without a concrete issue.

## Required Default Workflow

For every non-trivial task:

1. Identify the smallest safe change.
2. Check for existing instructions and relevant files.
3. Keep the diff narrow and reviewable.
4. Run available local tests.
5. Run `python3 scripts/check_safety_invariants.py` if the script exists.
6. Validate changed JSON files with `python3 -m json.tool`.
7. Report exact commands and results.
8. Stop before merge or real-world action.

If the environment lacks Python, pytest, the package, or another local tool, report the blocker. Do not install dependencies unless explicitly authorized.

## Required Final Report

Every agent task must end with:

- Summary
- Changed files
- Tests before change, if run
- Tests after change
- Demo result, if relevant
- Safety gates unchanged/changed
- Security invariants checked
- New risks
- Open points
- PR/commit recommended: yes/no
- Next recommended action

## Hard Stop Conditions

Stop immediately and report if the task appears to require:

- Network or target interaction
- External installation
- Real Bugcrowd target data
- Secrets, credentials, cookies, or tokens
- Payload, exploit, scanner, credential-test, or submission logic
- Changing `automatic_submission_allowed`
- Introducing any allowed final decision state beyond `BLOCK` or `NEEDS_HUMAN_REVIEW`
- Merging without explicit user approval
- Unclear repository state
- Test failures caused by the current patch

## Operating Principle

Prefer no change over unsafe change. Prefer a small Draft PR over a direct write. Prefer `BLOCK` over ambiguous readiness. Preserve the human gate.