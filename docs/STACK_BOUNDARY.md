# APH Stack Boundary

APH should behave like an opinionated product-governance starter, not a replacement for mature planning or implementation systems.

## One owner per responsibility

| Responsibility | Default owner | APH behavior |
|---|---|---|
| Product/domain truth | Product repository | Preserve it; never replace it with generic APH policy. |
| Spec → plan → tasks/process composition | GitHub Spec Kit when adopted | Compose with it; do not create a competing spec/task engine. |
| TDD, debugging, task execution, code review, completion verification | Superpowers when available | Invoke/reuse its skills; do not copy or fork their content into APH. |
| User Value Gate / black-box Product Acceptance | APH | Own the contract and proof ordering. |
| Human Gate semantics | APH | Keep gates narrow and owner-only where truly necessary. |
| Blocked-work rerouting | APH | Re-route automatically instead of asking the owner to schedule work. |
| Evidence → analysis → judgment → decision governance | APH | Preserve separation of duties and traceability. |
| Persistent autonomy state / maturity proof | APH | Track state and require falsifiable operational evidence. |
| Runtime/model/subagent orchestration | Coding-agent runtime | Use the runtime's native capability unless concrete recurring pain proves it insufficient. |

The default composition is:

```text
Product/domain rules
        ↓
APH product-governance contract
        ↓
Spec Kit — intent/spec/plan/tasks
        ↓
Superpowers — implementation discipline
        ↓
Codex / Claude Code / other runtime
        ↓
GitHub PR / CI / release evidence
```

This is a responsibility map, not a mandatory dependency chain. APH must continue to support standalone adoption when Spec Kit or Superpowers is absent.

## No-duplication rule

Before adding a new APH command, workflow, skill, scheduler, or template, ask:

1. Is this product-governance or autonomy-verification logic unique to APH?
2. Does Spec Kit already own the durable specification/process layer?
3. Does Superpowers already provide the implementation discipline?
4. Does the active coding runtime already provide the orchestration primitive?

If another layer already owns the capability well, APH should integrate, reference, or adapt it instead of re-implementing it.

Observed product pain is required before APH grows a new execution primitive.

## Goal blocks are not Human Gates

A blocked task does not normally end an autonomous run.

Use this routing contract:

```text
selected work
   ↓
blocked?
   ├─ no → execute
   ├─ dependency block → descend into the prerequisite
   ├─ Product Acceptance/policy failure → choose remediation work
   └─ genuine Human Gate → park only that workstream and continue another meaningful stream
```

Only ask the owner for action when **all meaningful remaining work** is blocked by a genuine Human Gate, or when no meaningful work remains.

Do not ask the owner "what should I do next?" when repository state, issue dependencies, Product Acceptance evidence, or the current goal can determine the next action.

A non-gate owner re-prompt that is required merely to schedule the next task is evidence of an autonomy defect and should be recorded as such when autonomy proof is being measured.

## Human Gate definition

Human Gates should be limited to actions that are materially identity-bound, legally meaningful, financially material, irreversible, methodology-authority-bound, security/privacy-critical, or technically owner-only.

Examples include MFA/CAPTCHA, credential recovery, account-owner terms acceptance, material paid commitments, irreversible production/account changes, and expert/domain authority decisions that cannot be inferred safely.

Routine review, ordinary task selection, dependency resolution, test failure remediation, Product Acceptance failure, and reversible implementation decisions are not Human Gates.

## Product proof ordering

APH owns this ordering:

`functionality → user value → correctness/domain validation → safety/privacy/reliability → release/recovery → autonomy proof`

Later-rung evidence can never substitute for an earlier missing rung. Spec Kit may express the work, Superpowers may execute it, and CI may verify parts of it, but APH decides whether product-value maturity has actually advanced.

## Integration policy

### Spec Kit

Prefer Spec Kit for durable specification, planning, task decomposition, and process composition. APH may add an opinionated preset/bundle layer, but it must not fork Spec Kit's core workflow without a concrete reason.

### Superpowers

Treat Superpowers as an external skill dependency. In runtimes that expose Superpowers skills, prefer the relevant upstream skill for TDD, systematic debugging, subagent-driven development, code review, and verification-before-completion. Do not vendor those skill texts into APH.

### Standalone mode

When neither Spec Kit nor Superpowers is available, APH may provide minimum fallback guidance, but those fallbacks should stay deliberately small and should not evolve into a parallel implementation framework.

## Change test

A proposed APH feature should answer all three questions positively before merge:

1. Does it solve a repeated product-governance/autonomy failure rather than a one-off inconvenience?
2. Is APH the correct responsibility owner?
3. Can the behavior be verified without adding routine owner coordination?

If not, integrate an existing tool or leave the capability in the product repository instead.
