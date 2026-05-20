# bugos v0.1.1

<p align="center">
  <img src="https://raw.githubusercontent.com/zxhimv/bugos/main/assets/bugos-social-preview.png" alt="bugos social preview" width="100%">
</p>

Offline-first Bugcrowd operations helper for authorized bug bounty work.

## Purpose

`bugos` does **not** scan targets, exploit systems, bypass controls, automate attacks, generate payloads, or interact with third-party assets. It only processes local files and helps with:

- redacted Bugcrowd brief intake,
- scope and out-of-scope gating,
- known-issue and duplicate-risk documentation,
- report quality linting,
- evidence manifest hashing,
- final submission readiness checks,
- safe No-Brief / Safe-Lab operation.

## Support this work

If GitHub Sponsors is enabled for this account, use the GitHub Sponsor button for repository-level support.

Sponsorship supports continued work on conservative, offline-first, human-reviewed security workflow tooling. It does not buy vulnerability research, target testing, scanning, exploit work, payload generation, credential handling, report submission, priority access to unsafe capabilities, or guaranteed outcomes.

See `docs/sponsors/sponsorship_overview.md` for the safe sponsorship boundary and draft tier ideas.

## Hard rule

No real target interaction may occur unless a current program brief has been reviewed and the Human Gate has approved scope, out-of-scope rules, known issues, rate limits, test-account permission, disclosure rules, and submission limits.

`bugos` never grants automatic submission approval. A `NEEDS_HUMAN_REVIEW` decision means the local artifacts may be ready for a human to review. It does **not** mean that a report may be submitted without a person checking the brief, scope, evidence, and disclosure rules.

## Install locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -e .[dev]
```

## Run tests

```bash
python -m pytest -q
```

## Demo run

```bash
python -m bugos.cli run-demo --workspace demo_out
```

This generates a synthetic profile, scope decision, evidence manifest, report lint, and final readiness check without any network access. The demo uses only local `demo.example` data and local files.

## Core commands

```bash
bugos validate-brief --brief fixtures/sample_brief.json --out out/validation.json
bugos normalize-brief --brief fixtures/sample_brief.json --out out/program_profile.json
bugos scope-check --profile out/program_profile.json --target https://app.demo.example/account/123 --action "manual BOLA read-only authorization check" --out out/scope_decision.json
bugos lint-report --report fixtures/sample_report_good.md --out out/report_lint.json
bugos build-evidence --evidence-dir fixtures/evidence --out out/evidence_manifest.json
bugos final-check --profile out/program_profile.json --scope-decision out/scope_decision.json --report-lint out/report_lint.json --manifest out/evidence_manifest.json --out out/final_submission_check.json
```

## Exit codes

- `0`: command completed and produced a non-blocking local result.
- `2`: command completed with a conservative block, failed quality gate, missing input, invalid JSON, unsafe path, or another expected user-facing input error.

For expected CLI errors, `bugos` writes a stable JSON error object to `--out` when possible, or to stderr when no output path is available. Error objects use fields such as `ok`, `error`, `errors`, and `warnings`.

## Output principle

The tool prefers conservative `BLOCK` / `NEEDS_HUMAN_REVIEW` decisions over false confidence.

Important final-check fields:

- `decision`: always `NEEDS_HUMAN_REVIEW` or `BLOCK`; there is no automatic submission decision.
- `ready` and `ready_for_human_review`: mean the local artifacts have no current automated blockers and are ready for human review only.
- `automatic_submission_allowed`: always `false`.
- `warnings`: always includes a human-gate reminder before any submission.

## Local path safety

`bugos` constrains CLI reads and writes to the current workspace. It rejects traversal or absolute paths outside that workspace. Evidence symlinks are conservatively blocked and reported as manifest warnings rather than followed.

## Safety boundaries

Allowed:

- local file parsing,
- local hashing,
- local report QA,
- local synthetic fixtures,
- local Codex-assisted implementation inside the repo workspace.

Not allowed:

- network access for tool operation,
- contacting real Bugcrowd targets,
- blind scanning,
- exploit automation,
- payload generation,
- credential attacks,
- bypass attempts,
- accessing real customer data,
- testing assets not explicitly in scope,
- submitting weak or AI-generated slop reports without human review.
