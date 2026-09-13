# Autonomy Profiles

APH should install the **minimum sufficient governance** for the product. More roles and documents do not automatically create more autonomy.

## S — Agent Ready

Use for small libraries, scripts, experiments, and single-developer utilities.

Required:

- durable `AGENTS.md` or equivalent instructions;
- deterministic bootstrap/check/test commands;
- clear definition of done;
- no hidden release claims.

Not required by default:

- persistent product feedback loop;
- Product Judge;
- behavioral product-governance evals;
- recovery-drill graduation.

## M — Autonomous Engineering

Use when agents should move through a queue of implementation work with limited supervision.

Adds:

- `TEAM_STATE.toml`;
- issue/task-driven work selection;
- implementer vs reviewer separation;
- CI gates;
- durable technical decisions;
- retry/escalation policy.

Target behavior:

`state → select work → implement → test → independent review → CI → update state → next work`

## L — Autonomous Delivery

Use for production products where agents may release and operate software.

Adds:

- Human Gates;
- security/privacy review boundaries;
- release state and known-good SHA tracking;
- smoke/E2E/release gates;
- incident and rollback contract;
- release authority rules;
- production evidence and rollback verification.

Target behavior:

`engineering loop → release → smoke → observe → recover when necessary`

## L4 — Autonomous Product Team

Use when the team should **learn from real users** and make bounded product decisions without routine founder direction.

Adds:

- external evidence channels;
- Community/Channel Operator;
- Feedback Analyst;
- Product Judge;
- `Operator != Analyst != Judge != Implementer != Release verifier`;
- Decision Ledger;
- behavioral governance evals;
- autonomy metrics;
- session-boundary continuity;
- closed-loop and recovery proof;
- `l4-candidate → l4-verified` graduation contract.

Target behavior:

`observe → analyze → judge → decide → implement → verify → release → observe again`

## Selection heuristic

Choose the lowest profile that satisfies the real product need.

- “I want Codex to implement issues reliably.” → **M**
- “I want agents to deploy and recover production.” → **L**
- “I want agents to interpret user feedback, decide what to change, release it, and learn again.” → **L4**

## Promotion and downgrade

Profiles may be promoted as the product grows.

A project claiming `L4 verified` should downgrade to candidate status if a material governance failure invalidates its proof window, such as:

- critical Human Gate bypass;
- privacy/security boundary failure;
- fabricated metrics or eval evidence;
- unresolved policy contradictions;
- repeated non-gate owner coordination required because state is insufficient;
- inability to recover safely from production failure.
