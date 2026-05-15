# bugos v0.1.0

Offline-first Bugcrowd operations helper for authorized bug bounty work.

## Purpose

`bugos` does **not** scan targets, exploit systems, bypass controls, automate attacks, or interact with third-party assets. It only processes local files and helps with:

- redacted Bugcrowd brief intake,
- scope and out-of-scope gating,
- known-issue and duplicate-risk documentation,
- report quality linting,
- evidence manifest hashing,
- final submission readiness checks,
- safe No-Brief / Safe-Lab operation.

## Hard rule

No real target interaction may occur unless a current program brief has been reviewed and the Human Gate has approved scope, out-of-scope rules, known issues, rate limits, test-account permission, disclosure rules, and submission limits.

## Install locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -e .[dev]
```

## Run tests

```bash
pytest
```

## Demo run

```bash
bugos run-demo --workspace demo_out
```

This generates a synthetic profile, scope decision, evidence manifest, report lint, and final readiness check without any network access.

## Core commands

```bash
bugos validate-brief --brief fixtures/sample_brief.json --out out/validation.json
bugos normalize-brief --brief fixtures/sample_brief.json --out out/program_profile.json
bugos scope-check --profile out/program_profile.json --target https://app.demo.example/account/123 --action "manual BOLA read-only authorization check" --out out/scope_decision.json
bugos lint-report --report fixtures/sample_report_good.md --out out/report_lint.json
bugos build-evidence --evidence-dir fixtures/evidence --out out/evidence_manifest.json
bugos final-check --profile out/program_profile.json --scope-decision out/scope_decision.json --report-lint out/report_lint.json --manifest out/evidence_manifest.json --out out/final_submission_check.json
```

## Output principle

The tool prefers conservative `BLOCK` / `NEEDS_HUMAN_REVIEW` decisions over false confidence.

## Safety boundaries

Allowed:

- local file parsing,
- local hashing,
- local report QA,
- local synthetic fixtures,
- local Codex-assisted implementation inside the repo workspace.

Not allowed:

- blind scanning,
- exploit automation,
- credential attacks,
- bypass attempts,
- accessing real customer data,
- testing assets not explicitly in scope,
- submitting weak or AI-generated slop reports.
