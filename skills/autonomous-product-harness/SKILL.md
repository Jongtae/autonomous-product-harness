---
name: autonomous-product-harness
description: Adopt, audit, or upgrade a repository with the minimum sufficient Autonomous Product Harness profile while preserving existing Spec Kit, Superpowers, runtime, architecture, and project conventions.
---

# Autonomous Product Harness Skill

Use this skill when a user asks to:

- bootstrap a new repository as an autonomous product team;
- adopt APH in an existing repository;
- add a reusable product starter such as `product-web`;
- audit Human Gates, blocked-work behavior, product-value proof, team state, or autonomy claims;
- upgrade from agent-assisted engineering toward autonomous delivery or product learning;
- create a falsifiable L4 graduation path.

## Required mindset

APH is a **thin product-governance and autonomy-verification layer**.

It is not a replacement for the project's coding-agent runtime, GitHub Spec Kit, Superpowers, architecture, CI, or domain-specific product rules.

Always inspect before writing. Prefer composition over duplication.

Read `../../docs/STACK_BOUNDARY.md` and `../../docs/USER_VALUE_GATE.md` when available.

## Workflow

### 1. Inspect the repository and existing stack

Read, when present:

- root agent instructions (`AGENTS.md`, `CODEX.md`, `CLAUDE.md`, etc.);
- README and product/spec docs;
- architecture and privacy/security docs;
- CI/workflows;
- issue/task conventions;
- release/deploy configuration;
- existing decision records;
- current feedback/community integrations;
- Spec Kit state such as `.specify/`, Spec Kit-generated spec/plan/tasks artifacts, presets, extensions, or bundle provenance;
- project/runtime skill configuration that indicates Superpowers or equivalent upstream implementation skills are available.

Determine:

- project type and maturity;
- whether it is a prototype, library, internal tool, or real released product;
- the primary user journey and intended user outcome, when a product exists;
- whether the real user-facing path has black-box Product Acceptance or deployed/release-candidate E2E coverage;
- whether agents only implement work or also deploy/operate/learn from users;
- sensitive data and irreversible actions;
- current Human Gates;
- current production/rollback reality;
- existing agent roles and review boundaries;
- which adjacent tool already owns planning, implementation discipline, and runtime orchestration.

Do not install a duplicate process layer merely because APH has a template for one.

### 2. Compose with existing tools before adding fallback process

Use one owner per responsibility.

#### If Spec Kit is present

Treat Spec Kit as the default source of truth for durable:

- specification;
- planning;
- task decomposition;
- presets/workflows/process composition.

Do not create a competing APH spec/plan/task state machine. Add APH product-governance requirements to the existing Spec Kit process through the smallest compatible mechanism.

#### If Superpowers is available

Use the relevant upstream skill for implementation disciplines such as:

- test-driven development;
- systematic debugging;
- subagent-driven development;
- requesting/receiving code review;
- verification before completion.

Do not copy, paraphrase into a fork, or vendor the upstream Superpowers skill library into APH.

APH Product Acceptance is **above** implementation-level verification: tests can pass while intended user value is still absent.

#### If either is absent

Use a minimum fallback sufficient for the selected APH profile. Standalone APH remains supported, but fallback guidance must stay smaller than a full implementation framework.

### 3. Choose the minimum sufficient profile

Use `references/profiles.md`.

Do not choose L4 merely because the user says “autonomous.”

Typical mapping:

- one-off scripts/libraries → S;
- autonomous issue implementation → M;
- production deployment/recovery → L;
- real-user evidence → independent judgment → delivery → relearning → L4.

### 4. Select an applicable product starter

For a user-facing web product, use `../../starters/product-web/README.md` as the default starting contract unless the repository already has a stricter equivalent.

Do not copy a starter blindly. Adapt:

- the primary user journey;
- the intended outcome;
- realistic input/support boundaries;
- black-box Product Acceptance;
- the milestone sequence.

A product starter is a default, not product truth.

### 5. Reconcile instead of overwrite

For every existing root/governance file:

- preserve product-specific facts and stricter safeguards;
- preserve existing Spec Kit/Superpowers/runtime ownership boundaries;
- never delete privacy/security/release restrictions solely to match APH defaults;
- identify contradictions explicitly;
- prefer one authoritative rule over duplicated conflicting copies.

If a migration is material, leave a short durable migration note or ADR.

### 6. Install only APH-owned governance

Depending on profile, ensure the repository has the relevant equivalents of:

- durable agent operating contract;
- machine-readable team state when the project needs cross-session continuity;
- Human Gates;
- blocked-work rerouting semantics;
- role authority/separation;
- **User Value Gate / black-box Product Acceptance** for user-facing products;
- CI/review/release gates not already owned elsewhere;
- incident/recovery contract;
- evidence-governed product decision policy;
- decision ledger;
- behavioral governance evals;
- L4 verification contract.

Do not add APH-owned versions of planning, debugging, TDD, generic review, or orchestration when an existing layer already owns them well.

### 7. Initialize factual state

Create or reconcile `TEAM_STATE.toml` (or an existing machine-readable equivalent) only when the selected profile benefits from persistent operational state.

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

### 8. Define Human Gates precisely

Human Gates should be materially identity-bound, legally meaningful, financially material, irreversible, methodology-authority-bound, security/privacy-critical, or technically owner-only.

Do not turn routine reversible work into approval gates.

Do not add owner approval merely because automated Product Acceptance is weak; improve the product-value check instead.

A Human Gate parks only the affected workstream unless all meaningful remaining work is blocked by genuine Human Gates.

Routine next-task selection, dependency resolution, Product Acceptance failure, test remediation, and reversible implementation decisions are not Human Gates.

### 9. Reroute blocked work instead of making the owner the scheduler

Use this routing contract:

```text
selected work
   ↓
blocked?
   ├─ no → execute
   ├─ dependency block → descend into the prerequisite
   ├─ Product Acceptance / policy failure → choose remediation work
   └─ genuine Human Gate → park that stream and continue another meaningful stream
```

Do not ask the owner "what should I do next?" when repository state, issue dependencies, Product Acceptance evidence, or the current goal can determine it.

Only request owner action when all meaningful remaining work is blocked by genuine Human Gates, or no meaningful work remains and an owner decision is itself required.

When autonomy proof is active, a non-gate owner re-prompt needed only to schedule the next task counts as an intervention/autonomy defect.

### 10. Define and verify product value

For a user-facing product, identify:

- the primary product goal;
- the shortest complete user-facing vertical slice that proves that goal;
- the current highest demonstrated rung in the proof ladder;
- a black-box Product Acceptance check that fails when intended value is absent.

Use the proof ladder:

`functionality → user value → correctness/domain validation → safety/privacy/reliability → release/recovery → autonomy proof`

For a new product, major feature, or product-recovery phase, use **Vertical Slice First**. Do not allow later-rung work to substitute for missing earlier-rung evidence.

Define progress as meaningful product/release/blocker/evidence state change, not commits, fixture counts, ADR volume, or repeated review.

After three substantial implementation cycles without changing Product Acceptance or materially reducing a concrete blocker, stop that approach and re-evaluate autonomously before producing more artifacts.

### 11. Preserve separation of duties

For material feedback-driven work, enforce:

`Operator != Analyst != Judge != Implementer != Release verifier`

Product Acceptance should be independent of implementation self-review for material user-value milestones when practical.

For smaller projects, roles may share one runtime only when contexts are intentionally separated and independent review is preserved.

### 12. Install / validate behavioral governance evals

When profile is L4, include cases covering at least:

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
- attempts to advance autonomy maturity while the primary product-value path is unproven;
- a blocked task that should reroute rather than ask the owner what to do next.

Score observable route/decision/output, not hidden reasoning.

### 13. Verify the harness

Run the repository's harness checks.

At minimum verify:

- required files parse;
- state schema is coherent;
- no obvious false `l4-verified` claim exists;
- required eval fixtures are valid;
- root instructions do not contain known conflicting policies;
- product-value maturity is not overstated relative to black-box evidence;
- stack ownership does not silently duplicate Spec Kit/Superpowers/runtime responsibilities.

If a Spec Kit bundle scaffold is present and the `specify` CLI is available, validate it with the upstream bundle validator. Do not claim one-command installability without a clean-project install test.

### 14. Continue real work

Do not finish with “setup complete” if the user's goal includes product implementation.

After adoption:

- select the highest-value unblocked product task at the earliest unproven rung;
- use issue-backed delivery for material repository changes: `Issue → change → PR → CI → merge → close when Definition of Done is satisfied`;
- use existing Spec Kit/Superpowers/runtime mechanisms where they own the work;
- implement, test, review, and release according to the selected profile;
- keep durable state current;
- reroute blocked work;
- stop only when all meaningful remaining work is blocked by genuine Human Gates, or no meaningful work remains.

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
- detected process/runtime stack and responsibility owners;
- selected starter, if any;
- primary user journey and current Product Acceptance state when applicable;
- highest demonstrated proof-ladder rung and the next missing rung;
- files/policies added or reconciled;
- duplicated/conflicting process removed or avoided;
- Human Gates identified;
- checks executed and their result;
- current maturity claim;
- next unblocked product action.

Do not expose private chain-of-thought; provide evidence, decisions, and observable results.
