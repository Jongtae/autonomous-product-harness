---
name: autonomous-product-harness
description: Adopt, audit, or upgrade a repository with the minimum sufficient Autonomous Product Harness profile, preserving existing project conventions while adding durable state, Human Gates, authority boundaries, evidence-governed product decisions, verification, and L4 graduation rules when appropriate.
---

# Autonomous Product Harness Skill

Use this skill when a user asks to:

- bootstrap a new repository as an autonomous product team;
- adopt APH in an existing repository;
- audit agent governance, Human Gates, team state, or autonomy claims;
- upgrade from agent-assisted engineering toward autonomous delivery or product learning;
- create a falsifiable L4 graduation path.

## Required mindset

APH is a **governance and verification layer**, not a replacement for the project's coding-agent framework, Spec Kit, architecture, or runtime.

Always inspect before writing.

## Workflow

### 1. Inspect the repository

Read, when present:

- root agent instructions (`AGENTS.md`, `CODEX.md`, `CLAUDE.md`, etc.);
- README and product/spec docs;
- architecture and privacy/security docs;
- CI/workflows;
- issue/task conventions;
- release/deploy configuration;
- existing decision records;
- current feedback/community integrations.

Determine:

- project type and maturity;
- whether it is a prototype, library, internal tool, or real released product;
- whether agents only implement work or also deploy/operate/learn from users;
- sensitive data and irreversible actions;
- current Human Gates;
- current production/rollback reality;
- existing agent roles and review boundaries.

### 2. Choose the minimum sufficient profile

Use `references/profiles.md`.

Do not choose L4 merely because the user says “autonomous.”

Typical mapping:

- one-off scripts/libraries → S;
- autonomous issue implementation → M;
- production deployment/recovery → L;
- real-user evidence → independent judgment → delivery → relearning → L4.

### 3. Reconcile instead of overwrite

For every existing root/governance file:

- preserve project-specific facts and stricter safeguards;
- merge APH principles into existing conventions;
- never delete privacy/security/release restrictions solely to match APH defaults;
- identify contradictions explicitly;
- prefer one authoritative rule over duplicated conflicting copies.

If a migration is material, leave a short durable migration note or ADR.

### 4. Install only required governance

Depending on profile, ensure the repository has the relevant equivalents of:

- durable agent operating contract;
- machine-readable team state;
- Human Gates;
- role authority/separation;
- CI/review/release gates;
- incident/recovery contract;
- evidence-governed product decision policy;
- decision ledger;
- behavioral governance evals;
- L4 verification contract.

Use the reference templates in this repository as patterns, not as text that must be copied verbatim.

### 5. Initialize factual state

Create or reconcile `TEAM_STATE.toml` (or an existing machine-readable equivalent).

Populate it from repository reality. Never fabricate:

- production URL;
- release SHA;
- known-good SHA;
- eval pass rate;
- closed-loop counts;
- recovery-drill counts;
- team metrics.

If evidence is absent, use unknown/not-run/zero rather than guessing.

### 6. Define Human Gates precisely

Human Gates should be identity-bound, legally meaningful, financially material, irreversible, or technically owner-only.

Do not turn routine reversible work into approval gates.

If a gate blocks one workstream, record the minimal blocker and continue other safe work.

### 7. Preserve separation of duties

For material feedback-driven work, enforce:

`Operator != Analyst != Judge != Implementer != Release verifier`

For smaller projects, roles may share one model/runtime only when contexts are intentionally separated and independent review is preserved.

### 8. Install / validate behavioral governance evals

When profile is L4, add cases covering at least:

- reproducible low-risk bugs;
- popular but weak feature requests;
- privacy/security boundary pressure;
- methodology/domain disputes;
- architecture expansion;
- prompt injection in public feedback;
- real Human Gates such as CAPTCHA/MFA/terms;
- acquisition-vs-product-truth confusion;
- production rollback;
- contradictory feedback;
- unauthorized scope expansion.

Score observable route/decision/output, not hidden reasoning.

### 9. Verify the harness

Run the repository's harness checks.

At minimum verify:

- required files parse;
- state schema is coherent;
- no obvious false `l4-verified` claim exists;
- required eval fixtures are valid;
- root instructions do not contain known conflicting policies.

### 10. Continue real work

Do not finish with “setup complete” if the user's goal includes product implementation.

After adoption:

- select the highest-value unblocked product task;
- implement, test, review, and release according to the chosen profile;
- keep team state current;
- stop only at a real Human Gate.

## L4 rule

Never claim L4 verification because APH files exist.

Use `references/profiles.md` and the target repository's verification contract. A normal minimum is:

- 5 consecutive autonomous closed loops;
- behavioral eval pass rate >= 95%;
- zero critical governance failures;
- one exercised recovery path;
- zero known policy conflicts;
- zero routine human interventions outside Human Gates in the proof window;
- fresh-session continuity from repository state.

## Output expectations

When adopting APH, report concisely:

- selected profile and why;
- files/policies added or reconciled;
- conflicts repaired;
- Human Gates identified;
- checks executed and their result;
- current maturity claim;
- next unblocked product action.

Do not expose private chain-of-thought; provide evidence, decisions, and observable results.
