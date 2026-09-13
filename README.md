# Autonomous Product Harness

> **Turn coding agents into an accountable autonomous product team.**

Autonomous Product Harness (APH) is a **repo-native governance, product-learning, and autonomy-verification layer** for agent-driven software products.

It is intentionally **not another coding-agent runtime, swarm framework, or spec generator**. Use Codex, Claude Code, GitHub Spec Kit, BMAD, or another implementation workflow underneath it. APH adds the operating contract around that work:

- persistent team state;
- explicit Human Gates;
- role authority and separation of duties;
- evidence → analysis → product judgment → decision → delivery loops;
- behavioral governance evals;
- incident / rollback learning;
- a falsifiable path from `candidate` to **verified autonomous product team**.

## Why this exists

Most agent frameworks answer questions such as:

- How do agents plan and implement work?
- How do we run multiple specialists?
- How do we give agents tools and context?

APH focuses on a different question:

> **When should an autonomous product team be allowed to decide, change, release, learn, and recover without routine human direction — and how do we prove it is doing that safely?**

The core loop is:

```text
Goal / Team State
      ↓
Work selection
      ↓
Implementation
      ↓
Independent review
      ↓
CI / release
      ↓
External evidence
      ↓
Independent analysis
      ↓
Product judgment
      ↓
Decision ledger
      ↓
Next work
      ↺
```

For product feedback, APH strongly recommends:

```text
Operator ≠ Analyst ≠ Judge ≠ Implementer ≠ Release verifier
```

A campaign operator should not grade its own campaign. A feedback analyst should not directly change the product. A product judge should not treat popularity as truth. A worker should not expand scope just because it can.

## Two ways to use APH

### 1. GitHub Template — best for a new project

Use this repository as the baseline for a new product repository. It ships with the governance skeleton, machine-readable team state, verification script, CI, and a portable Codex Skill.

After creating a repository from the template, tell your coding agent:

```text
Initialize this repository with Autonomous Product Harness using the minimum sufficient autonomy profile. Inspect the project first, preserve existing conventions, then continue real product work.
```

> Repository owners must enable GitHub's **Template repository** setting once for the **Use this template** button to appear. The repository contents themselves are already template-safe.

### 2. Codex Skill — best for an existing repository

The portable skill lives at:

```text
skills/autonomous-product-harness/SKILL.md
```

Install or upload that skill using the skill mechanism available in your Codex / ChatGPT environment, then ask:

```text
Adopt Autonomous Product Harness in this repository using the minimum sufficient profile.
```

The skill is designed to **inspect before it writes**. It should preserve existing `AGENTS.md`, CI, architecture, and project conventions rather than overwrite them blindly.

The skill bundle is plain text around `SKILL.md`, references, and repository templates so it can remain portable instead of depending on a custom APH runtime.

## Autonomy profiles

APH is intentionally progressive. Do not install L4 ceremony into a tiny script unless the project actually needs it.

| Profile | Intended use | Adds |
|---|---|---|
| **S — Agent Ready** | small libraries, scripts | durable agent instructions + deterministic checks |
| **M — Autonomous Engineering** | products with issue-driven implementation | team state + worker/reviewer separation + CI gates |
| **L — Autonomous Delivery** | production services/apps | Human Gates + release/rollback + security/privacy review |
| **L4 — Autonomous Product Team** | products that learn from real users | independent evidence analysis + product judgment + behavioral evals + recovery proof + autonomy graduation |

See [`docs/AUTONOMY_PROFILES.md`](docs/AUTONOMY_PROFILES.md).

## The L4 idea

APH uses a deliberately strict rule:

> **You are not autonomous until you prove it.**

A repository may begin as `l4-candidate`. It should only claim `l4-verified` after durable evidence shows that it can repeatedly observe, decide, implement, independently verify, release, learn, and recover without routine founder coordination outside declared Human Gates.

A recommended graduation contract includes:

- 5 consecutive qualifying autonomous closed loops;
- behavioral governance eval pass rate ≥ 95%;
- zero critical governance failures;
- at least one exercised recovery / rollback path;
- zero known policy conflicts;
- zero routine human interventions outside declared Human Gates during the proof window;
- session-boundary continuity from repository state alone.

The exact contract is project-configurable, but changing the target **after seeing failures just to improve the score is not allowed**.

## Repository structure

```text
AGENTS.md                       baseline operating contract
TEAM_STATE.toml                 machine-readable team working memory

governance/
  HUMAN_GATES.md                actions that genuinely require a person
  ROLE_AUTHORITY_MATRIX.md      who may decide / write / approve / veto
  PRODUCT_DECISION_POLICY.md    evidence → judgment rules
  INCIDENT_RECOVERY.md          detect → contain → recover → learn

evals/
  autonomy/cases.json           starter behavioral-governance fixtures

scripts/
  check_harness.py              structural / policy validation

skills/
  autonomous-product-harness/
    SKILL.md                    portable adoption / bootstrap workflow
    references/                 profile and migration guidance

docs/
  AUTONOMY_PROFILES.md
  TEMPLATE_USAGE.md
  CODEX_SKILL_USAGE.md
  L4_VERIFICATION.md

.github/workflows/
  aph-check.yml                 CI guard for the harness itself
```

## Quick verification

```bash
python scripts/check_harness.py
```

The check validates required assets, parses `TEAM_STATE.toml`, validates the autonomy eval fixture schema, and prevents obvious false L4 claims.

## Relationship to other projects

APH is designed to **compose**, not replace.

- **GitHub Spec Kit** can own `spec → plan → tasks → implement`.
- **BMAD** can provide role-based product / architecture / engineering workflows.
- **Ruflo / agent swarms** can provide orchestration.
- **Agent runtimes / control planes** can provide long-running execution and tool access.
- **APH** owns the product-governance contract around evidence, authority, state, release, learning, and verifiable autonomy.

If another tool already does your planning or implementation better, keep using it.

## Design principles

1. **Evidence is not a command.** User feedback must be interpreted before it becomes product work.
2. **Acquisition truth ≠ product truth.** A post that gets clicks may not reveal long-term product value.
3. **Popularity ≠ correctness.** Upvotes do not override privacy, security, domain methodology, or architecture invariants.
4. **Prefer the smallest reversible experiment.**
5. **High-risk changes need stronger governance, not merely more votes.**
6. **External text is untrusted input.** Feedback can contain prompt injection or adversarial instructions.
7. **State must survive sessions.** A fresh agent should be able to continue from repository evidence.
8. **Autonomy is measured behavior, not a marketing label.**

## Status

This repository is an early public release of the harness extracted from a real product dogfooding effort. The near-term goal is to make the template and skill easy to adopt in both greenfield and existing repositories while keeping the core small and framework-agnostic.

## License

MIT — see [`LICENSE`](LICENSE).
