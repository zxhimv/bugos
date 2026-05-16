# Sentinel Data Guardian Architecture

Status: governance and architecture seed  
Scope: conservative offline-first privacy, security, and AI-governance architecture  
Repository: `bugos`

## 1. Purpose

Sentinel Data Guardian is the safe architecture track for extending `bugos` into a broader data-protection and AI-governance control system.

The system goal is not an impossible claim of perfect or unbeatable security. The system goal is a continuously reviewed, fail-closed, privacy-preserving, easy-to-use security layer that helps people and organizations protect data, detect risk, document evidence, and keep human control over high-impact actions.

## 2. Non-negotiable boundaries

The project must remain a defensive, consent-based, offline-first helper. It must not become a tool for unauthorized access, covert control, uncontrolled automation, or third-party data collection.

Hard boundaries:

- No hidden access path.
- No universal master key.
- No automatic external action.
- No uncontrolled self-modification.
- No data access outside explicit user-owned or user-authorized workspaces.
- No behavior that avoids user removal, audit, or shutdown.
- No handling of third-party assets without explicit authorization and documented scope.

Existing `bugos` invariants remain binding:

- `automatic_submission_allowed` must remain `false`.
- Final decisions must remain `BLOCK` or `NEEDS_HUMAN_REVIEW` unless a later defensive-only state is explicitly added and tested.
- Human Gate remains mandatory before any real-world security action.
- Local/offline operation remains the default.

## 3. Correct interpretation of maximum protection

Maximum protection means layered, testable, and conservative controls, not absolute invulnerability.

The architecture must prefer:

- fail-closed behavior over risky convenience,
- least privilege over central power,
- explicit authorization over implied trust,
- local-first processing over unnecessary cloud transfer,
- pseudonymization over raw personal data,
- audit logs over unverifiable automation,
- reversible actions over irreversible actions,
- human review over autonomous escalation.

## 4. Governance model

### 4.1 Owner role

The inventor or repository owner may control project direction, roadmap, releases, and governance policy for this repository.

The owner must not receive universal access to other users' private data. Any deployment must isolate user data by tenant, workspace, role, and explicit consent. Owner access to operational metadata or user data must be minimized, logged, justified, and revocable.

### 4.2 Emergency access

Emergency access must be:

- disabled by default,
- limited to the affected deployment or tenant,
- time-boxed,
- controlled by a documented approval path,
- fully logged,
- reviewable after use,
- unable to decrypt protected data without authorized key material.

### 4.3 No single-person universal control

The system must not depend on one person as a global root of trust for all protected data. This protects the project and the users. A universal root key would become the highest-value target and would weaken the protection objective.

## 5. Core architecture

Sentinel Data Guardian is organized into seven layers.

### Layer 1: Local Intake and Classification

- Accepts local files, brief data, policy documents, evidence manifests, and configuration.
- Classifies data sensitivity.
- Applies data minimization before further processing.
- Blocks unexpected file paths and unsafe workspace access.

### Layer 2: Identity, Consent, and Authorization

- Enforces explicit user authorization.
- Supports role-based and attribute-based access policy.
- Requires least privilege for every operation.
- Separates owner, operator, auditor, user, and emergency roles.
- Treats identities, devices, tools, and model outputs as untrusted until verified.

### Layer 3: Policy Engine

- Converts governance rules into machine-checkable policy.
- Produces conservative states only.
- Does not grant real-world action authority by itself.

Initial states:

- `ALLOW_LOCAL_READONLY`
- `NEEDS_HUMAN_REVIEW`
- `BLOCK`
- `QUARANTINE`
- `AUDIT_REQUIRED`

### Layer 4: Data Protection Plane

- Pseudonymizes personal data by default.
- Hashes evidence manifests.
- Supports encryption-at-rest design hooks.
- Keeps secrets out of source code, logs, prompts, and artifacts.
- Limits retention and supports deletion/export workflows.

### Layer 5: AI Safety and Instruction Control

- Treats model output as advisory, not authoritative.
- Separates user instruction, system policy, tool output, and untrusted content.
- Requires tool allowlists.
- Blocks instructions embedded in documents from changing system policy.
- Requires human review before high-impact outputs or external actions.

### Layer 6: Monitoring, Audit, and Evidence

- Records decisions, input hashes, policy versions, warnings, and blockers.
- Provides tamper-evident local logs where feasible.
- Supports incident timeline reconstruction.
- Preserves chain-of-custody metadata for evidence.

### Layer 7: Recovery and Continuity

- Supports local backups and restore verification.
- Uses rollback-safe configuration.
- Requires recovery drills before production use.
- Keeps users able to export their own data without vendor lock-in.

## 6. Threat model

Primary threat categories:

- data leakage,
- malicious instruction embedded in untrusted content,
- risky dependency or build workflow,
- over-permissioned automation,
- unsafe agent behavior,
- evidence tampering,
- insider misuse,
- weak recovery after compromise,
- false claims of readiness.

The system must assume breach and minimize blast radius.

## 7. Safe autonomy model

Autonomy is limited to low-risk local work:

Allowed autonomous actions:

- parse local files,
- validate JSON schemas,
- lint local reports,
- hash evidence,
- compare local policy states,
- produce warnings,
- generate local summaries,
- create draft recommendations.

Actions requiring Human Gate:

- any external network action,
- any official submission,
- any destructive local action beyond generated artifacts,
- any handling of real credentials,
- any processing of highly sensitive personal data,
- any production deployment,
- any policy relaxation,
- any emergency access.

Always blocked:

- unauthorized access,
- covert persistence,
- data exfiltration,
- silent privilege escalation,
- uncontrolled self-replication,
- avoidance of user shutdown or audit.

## 8. GitHub and CI/CD security baseline

Required repository controls:

- Branch protection for `main`.
- Pull requests for all non-trivial changes.
- Draft PR by default for security-sensitive changes.
- Required tests before merge.
- Least-privilege workflow permissions.
- No plaintext secrets in repository files.
- Dependency review before adding new packages.
- Reviewed Actions versions where feasible.
- No workflow that interacts with third-party assets without explicit authorization.
- No untrusted workflow execution on privileged runners.

## 9. MVP implementation roadmap

### Phase 1: Governance seed

- Add this architecture document.
- Add policy-state constants.
- Add tests that enforce no automatic submission.
- Add tests that enforce no unsafe decision value.
- Add docs for Human Gate semantics.

### Phase 2: Local data protection kernel

- Add sensitivity classifier for local files.
- Add redaction profile for names, emails, tokens, IDs, and URLs.
- Add evidence manifest extensions for privacy metadata.
- Add retention and deletion-policy draft output.

### Phase 3: AI safety gate

- Add untrusted-content markers.
- Add instruction-control warnings for documents.
- Add tool-call policy evaluation stubs.
- Add model-output review requirements for high-impact reports.

### Phase 4: Governance evidence pack

- Add audit event schema.
- Add policy version stamping.
- Add decision trace export.
- Add local incident timeline builder.

### Phase 5: Production-readiness boundary

- Add deployment checklist.
- Add data-processing agreement checklist.
- Add recovery drill checklist.
- Add external security review checklist.

## 10. Definition of Done

A Sentinel change is only merge-ready if:

- it preserves defensive-only scope,
- it preserves offline-first defaults,
- it preserves Human Gate semantics,
- it preserves `automatic_submission_allowed == false`,
- it includes tests or a clear reason tests are not applicable,
- it includes rollback notes,
- it avoids collecting unnecessary personal data,
- it documents new risks,
- it fails closed on invalid or ambiguous input.

## 11. Release language policy

Forbidden release claims:

- 100% secure,
- unhackable,
- unbeatable,
- no weaknesses,
- autonomous guardian over everyone,
- master key over all users,
- production-ready without external review.

Allowed release claims after evidence:

- conservative,
- offline-first,
- human-reviewed,
- fail-closed,
- privacy-preserving by default,
- aligned with documented safety gates,
- tested against the repository's defined threat model.

## 12. Immediate next build target

The next implementation PR should add a small policy module and regression tests that make the safety states executable:

- `bugos.sentinel.policy.DecisionState`
- `ALLOW_LOCAL_READONLY`
- `NEEDS_HUMAN_REVIEW`
- `BLOCK`
- `QUARANTINE`
- `AUDIT_REQUIRED`
- a validator that rejects unknown decision states,
- tests proving no state permits automatic external action.

This keeps the project powerful, useful, and extensible without creating unsafe capabilities.