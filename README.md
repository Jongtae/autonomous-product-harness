# Autonomous Product Harness

> **A Bootstrap-like product-governance starter for autonomous product teams.**

Autonomous Product Harness (APH) is an **opinionated product-governance, product-learning, and autonomy-verification layer** for agent-driven software products.

APH is intentionally thin. It should **compose proven planning and implementation systems instead of rebuilding them**.

The recommended stack is:

```text
Product / domain rules
        ↓
APH — User Value, Human Gates, evidence, autonomy proof
        ↓
GitHub Spec Kit — spec / plan / tasks / process composition
        ↓
Superpowers — TDD / debugging / execution / review / verification
        ↓
Codex / Claude Code / another coding-agent runtime
        ↓
GitHub PR / CI / preview / production evidence
```

Spec Kit and Superpowers are optional. APH still supports standalone adoption, but its fallback process guidance should stay deliberately small.

See [`docs/STACK_BOUNDARY.md`](docs/STACK_BOUNDARY.md) for the ownership contract.

## Why this exists

Coding-agent ecosystems already provide strong primitives for planning, implementation, debugging, review, and orchestration. APH focuses on a different failure mode:

> **A team can execute flawlessly against the wrong proxy.**

A product may have green tests, clean CI, privacy checks, release automation, and even autonomy evals while the primary user still cannot receive the value the product exists to provide.

APH therefore owns the product-level contract around:

- **User Value Gate / black-box Product Acceptance**;
- **Vertical Slice First** ordering;
- narrow, explicit **Human Gates**;
- blocked-work **rerouting instead of routine owner scheduling**;
- role authority and separation of duties;
- evidence → analysis → product judgment → decision → delivery loops;
- durable team state;
- incident / rollback learning;
- falsifiable autonomy verification.

It does **not** aim to own a planner, coding runtime, swarm scheduler, vector memory, TDD methodology, debugger, or generic spec engine.

## User value before autonomy proof

APH uses a strict rule:

> **Autonomy cannot advance beyond the highest product-value milestone that has been demonstrated end to end.**

The default proof ladder is:

```text
functionality
    ↓
user value
    ↓
correctness / domain validation
    ↓
safety / privacy / reliability
    ↓
release / recovery
    ↓
autonomy proof
```

Passing tests, CI, privacy/security checks, release gates, or behavioral evals cannot substitute for an earlier missing rung.

For new products, major features, and product recovery, prove one complete user-facing vertical slice through the real UI or public contract before expanding infrastructure, datasets, governance artifacts, or autonomy ceremony.

Product Acceptance should be black-box and outcome-oriented. If three substantial implementation cycles do not change Product Acceptance or materially reduce its concrete blocker, stop that approach and re-evaluate autonomously instead of generating more activity.

See [`docs/USER_VALUE_GATE.md`](docs/USER_VALUE_GATE.md).

## Goal blocks are not Human Gates

A blocked task normally causes **rerouting**, not a stop.

```text
selected work
   ↓
blocked?
   ├─ no → execute
   ├─ dependency block → descend into the prerequisite
   ├─ Product Acceptance / policy failure → remediate
   └─ genuine Human Gate → park that stream and continue another meaningful stream
```

Only request owner action when all meaningful remaining work is blocked by genuine Human Gates, or no meaningful work remains.

Routine task selection, dependency resolution, test failure remediation, and reversible implementation choices are not Human Gates.

## Bootstrap-style starters

APH starters encode defaults for a **class of product**, not one specific application.

The first starter is [`starters/product-web/`](starters/product-web/). It supplies defaults for a user-facing web product:

```text
entry
→ user input/action
→ core product behavior
→ user-visible result
→ explanation / next meaningful action
```

Its default milestones are:

`Functional Alpha → Value Preview → Correctness Candidate → Release Candidate → Production → Autonomy Proof`

The intention is similar to Bootstrap: avoid re-solving the same basic structure on every project while preserving product-specific design and domain truth.

## Spec Kit composition

GitHub Spec Kit is the preferred owner for durable `spec → plan → tasks` and process composition when a project already uses or chooses it.

APH includes an early local bundle scaffold at:

```text
spec-kit/bundles/aph-product-web/
```

The scaffold follows Spec Kit bundle schema `1.0`, stays integration-agnostic, and is deliberately minimal. It is **not yet advertised as a published one-command community bundle**; clean-project validation and dependency-resolution evidence should come before that claim.

Spec Kit bundles are composition/distribution units, not a new runtime, which matches APH's thin-layer direction.

## Superpowers composition

When the active coding environment exposes [obra/superpowers](https://github.com/obra/superpowers), APH should reuse upstream implementation disciplines rather than copying them.

Typical ownership includes:

- test-driven development;
- systematic debugging;
- subagent-driven development;
- code review workflows;
- verification before completion.

APH keeps product-level acceptance and autonomy governance above those implementation disciplines.

A community `speckit-superpowers-bridge` exists for teams that want a thin handoff between Spec Kit artifacts and Superpowers execution. It is community-maintained and should be reviewed before use; APH does not silently install or vendor it.

## Ways to use APH

### 1. Product starter — best for a new user-facing product

Start from the repository template or adopt the portable skill, then select the smallest applicable starter. For a normal web product, begin with [`starters/product-web/`](starters/product-web/).

A useful first instruction is:

```text
Adopt the APH product-web starter.
Define the primary user journey and black-box Product Acceptance before broad implementation.
Use Vertical Slice First. If work is blocked, descend into its prerequisite or reroute to another meaningful stream.
Stop only when all meaningful remaining work is blocked by genuine Human Gates or no meaningful work remains.
```

### 2. Portable APH Skill — best for an existing repository

The skill lives at:

```text
skills/autonomous-product-harness/SKILL.md
```

Ask the coding agent to:

```text
Adopt Autonomous Product Harness using the minimum sufficient profile. Preserve existing Spec Kit, Superpowers, CI, architecture, and project conventions instead of duplicating them.
```

The skill inspects before writing and composes with existing process layers.

### 3. Standalone template — when Spec Kit / Superpowers are absent

APH still contains enough baseline governance, state, verification, and CI structure to operate independently. Standalone mode is a fallback, not an invitation to grow APH into a competing implementation framework.

## Autonomy profiles

APH is progressive. Do not install L4 ceremony into a tiny script unless the project needs it.

| Profile | Intended use | Adds |
|---|---|---|
| **S — Agent Ready** | small libraries, scripts | durable agent instructions + deterministic checks |
| **M — Autonomous Engineering** | issue-driven implementation | team state + worker/reviewer separation + CI gates |
| **L — Autonomous Delivery** | production services/apps | Human Gates + release/rollback + security/privacy review |
| **L4 — Autonomous Product Team** | products that learn from real users | independent evidence analysis + product judgment + behavioral evals + recovery proof + autonomy graduation |

See [`docs/AUTONOMY_PROFILES.md`](docs/AUTONOMY_PROFILES.md).

## L4 verification

> **You are not autonomous until you prove it.**

A repository may begin as `l4-candidate`. A normal graduation contract includes:

- demonstrated primary user value at the appropriate release stage;
- 5 consecutive qualifying autonomous closed loops;
- behavioral-governance eval pass rate ≥ 95%;
- zero critical governance failures;
- at least one exercised recovery / rollback path;
- zero known policy conflicts;
- zero routine owner interventions outside declared Human Gates during the proof window;
- session-boundary continuity from repository state alone.

See [`docs/L4_VERIFICATION.md`](docs/L4_VERIFICATION.md).

## Repository structure

```text
AGENTS.md                       baseline operating contract
TEAM_STATE.toml                 machine-readable team working memory

governance/
  HUMAN_GATES.md
  ROLE_AUTHORITY_MATRIX.md
  PRODUCT_DECISION_POLICY.md
  INCIDENT_RECOVERY.md

docs/
  USER_VALUE_GATE.md
  STACK_BOUNDARY.md
  AUTONOMY_PROFILES.md
  L4_VERIFICATION.md
  REFERENCE_IMPLEMENTATION_BOUNDARY.md

starters/
  product-web/README.md         first Bootstrap-style product starter

spec-kit/
  bundles/aph-product-web/
    bundle.yml                  local Spec Kit composition scaffold
    README.md

skills/
  autonomous-product-harness/
    SKILL.md                    portable adoption / bootstrap workflow
    references/

evals/
  autonomy/cases.json

scripts/
  check_harness.py

.github/workflows/
  aph-check.yml
```

## Quick verification

```bash
python scripts/check_harness.py
```

The check validates required assets, machine-readable state, the starter/bundle scaffold, and the autonomy eval contract.

## Reference products are not integration showcases

APH can support more tools than any one product should use.

> **Observed pain before framework.**

INYEON is the first major APH dogfood/reference implementation, but it remains product-first. It should adopt Spec Kit, Superpowers bridges, orchestration systems, or other integrations only when they reduce a concrete recurring product-development failure.

## Design principles

1. **User value before autonomy proof.** Implementation proxies cannot substitute for a demonstrated primary user outcome.
2. **Evidence is not a command.** Feedback must be interpreted before it becomes product work.
3. **Goal blocks are not Human Gates.** Reroute unless a person is genuinely required.
4. **Do not make the owner the scheduler.** Repository state should determine routine next work.
5. **One owner per responsibility.** Compose mature tools rather than duplicate them.
6. **Observed pain before framework.** Add APH machinery only for repeated governance/autonomy failures APH actually owns.
7. **Prefer the smallest reversible experiment.**
8. **State must survive sessions.**
9. **Autonomy is measured behavior, not a marketing label.**

## Status

APH is an early public project extracted from real dogfooding. The current direction is to make it a small, reusable product-governance starter that composes with the agent ecosystem instead of competing with it.

## License

MIT — see [`LICENSE`](LICENSE).
