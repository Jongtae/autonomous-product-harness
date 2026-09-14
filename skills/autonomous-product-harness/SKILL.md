---
name: autonomous-product-harness
description: Adopt, audit, or upgrade a repository with the minimum sufficient Autonomous Product Harness profile, preserving existing project conventions while adding durable state, Human Gates, authority boundaries, product-value verification, evidence-governed product decisions, verification, and L4 graduation rules when appropriate.
---

# Autonomous Product Harness Skill

Use this skill when a user asks to:

- bootstrap a new repository as an autonomous product team;
- adopt APH in an existing repository;
- audit agent governance, Human Gates, team state, product-value proof, or autonomy claims;
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
- the primary user journey and intended user outcome, when a product exists;
- whether the real user-facing path has black-box acceptance or deployed/release-candidate E2E coverage;
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
- **User Value Gate / black-box Product Acceptance** for user-facing products;
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
- Product Acceptance state;
- eval pass rate;
- closed-loop counts;
- recovery-drill counts;
- team metrics.

If evidence is absent, use unknown/not-run/zero rather than guessing.

### 6. Define Human Gates precisely

Human Gates should be identity-bound, legally meaningful, financially material, irreversible, methodology-authority, security/privacy-critical, or technically owner-only.

Do not turn routine reversible work into approval gates.

Do not add owner approval merely because automated Product Acceptance is weak; improve the product-value check instead.

If a gate blocks one workstream, record the minimal blocker and continue other safe work.

### 7. Define and verify product value

For a user-facing product, read `../../docs/USER_VALUE_GATE.md` as the reference contract and adapt it to the target repository.

Identify:

- the primary product goal;
- the shortest complete user-facing vertical slice that proves that goal;
- the current highest demonstrated rung in the proof ladder;
- a black-box Product Acceptance check that can fail when the intended outcome is absent.

Use the proof ladder:

`functionality → user value → correctness/domain validation → safety/privacy/reliability → release/recovery → autonomy proof`

For a new product, major feature, or product-recovery phase, prefer **Vertical Slice First**. Do not allow later-rung work to substitute for missing earlier-rung evidence.

Define progress as meaningful product/release/blocker/evidence state change, not commits, fixture counts, ADR volume, or repeated review.

Add the anti-waste stop rule when appropriate: after three substantial implementation cycles without changing Product Acceptance or materially reducing a concrete blocker, stop that stream and re-evaluate before producing more artifacts.

This re-evaluation is normally autonomous, not a Human Gate.

### 8. Preserve separation of duties

For material feedback-driven work, enforce:

`Operator != Analyst != Judge != Implementer != Release verifier`

Product Acceptance should also be independent of the implementation self-review for material user-value milestones when practical.

For smaller projects, roles may share one model/runtime only when contexts are intentionally separated and independent review is preserved.

### 9. Install / validate behavioral governance evals

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
- unauthorized scope expansion;
- pressure to count implementation proxies as proof of user value;
- attempts to advance autonomy maturity while the primary product-value path is unproven.

Score observable route/decision/output, not hidden reasoning.

### 10. Verify the harness

Run the repository's harness checks.

At minimum verify:

- required files parse;
- state schema is coherent;
- no obvious false `l4-verified` claim exists;
- required eval fixtures are valid;
- root instructions do not contain known conflicting policies;
- product-value maturity is not overstated relative to black-box evidence.

### 11. Continue real work

Do not finish with “setup complete” if the user's goal includes product implementation.

After adoption:

- select the highest-value unblocked product task at the earliest unproven rung of the proof ladder;
- use issue-backed delivery for material repository changes: `Issue → change → PR → CI → merge → close when Definition of Done is satisfied`;
- implement, test, review, and release according to the chosen profile;
- keep team state current;
- stop only at a real Human Gate or an anti-waste re-evaluation point.

Do not advance release, external-feedback, or autonomy-proof work merely because it is available when a lower product-value milestone remains unproven.

## L4 rule

Never claim L4 verification because APH files exist.

Use `references/profiles.md`, `../../docs/USER_VALUE_GATE.md`, and the target repository's verification contract. A normal minimum is:

- a demonstrated primary user-value path at the appropriate release stage;
- 5 consecutive autonomous closed loops;
- behavioral eval pass rate >= 95%;
- zero critical governance failures;
- one exercised recovery path;
- zero known policy conflicts;
- zero routine human interventions outside Human Gates in the proof window;
- fresh-session continuity from repository state.

A later-rung success cannot compensate for an unproven primary product-value path.

## Output expectations

When adopting APH, report concisely:

- selected profile and why;
- primary user journey and current Product Acceptance state when applicable;
- highest demonstrated proof-ladder rung and the next missing rung;
- files/policies added or reconciled;
- conflicts repaired;
- Human Gates identified;
- checks executed and their result;
- current maturity claim;
- next unblocked product action.

Do not expose private chain-of-thought; provide evidence, decisions, and observable results.
