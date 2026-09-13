# APH Profile Selection Reference

Choose the **minimum sufficient** profile.

## S — Agent Ready

Signals:
- small repo or library;
- agent mostly edits code/documents;
- no autonomous production release requirement;
- no real-user product-learning loop.

Install/reconcile:
- durable agent instructions;
- deterministic check/test command;
- clear definition of done.

## M — Autonomous Engineering

Signals:
- agent should select and implement multiple issues/tasks;
- work continues across sessions;
- independent code/QA review matters;
- CI exists or should exist.

Install/reconcile:
- S;
- machine-readable team state;
- issue/task work queue conventions;
- implementer/reviewer boundary;
- CI and durable technical decisions.

## L — Autonomous Delivery

Signals:
- production deployment is part of the mission;
- agents may operate release/rollback flows;
- privacy/security/release boundaries are meaningful;
- a bad release has user impact.

Install/reconcile:
- M;
- Human Gates;
- security/privacy review;
- production/release state;
- known-good artifact/SHA tracking;
- incident and recovery contract;
- smoke/E2E/release gates.

## L4 — Autonomous Product Team

Signals:
- real-user evidence affects product decisions;
- agents should independently analyze feedback and choose what to change;
- product should close the loop from evidence to release to re-observation;
- founder/owner should not be routine product coordinator.

Install/reconcile:
- L;
- channel/community operator contract;
- feedback analyst;
- product judge;
- decision ledger;
- role separation: Operator != Analyst != Judge != Implementer != Release verifier;
- behavioral governance evals;
- autonomy metrics;
- session-boundary continuity;
- falsifiable L4 graduation contract.

## Never infer L4 from these alone

These are not sufficient evidence:
- many subagents;
- long-running sessions;
- automatic pull requests;
- automatic deployments;
- a large prompt or AGENTS.md;
- no human involvement in one coding task.

L4 requires repeated product-level closed loops and recovery/verification evidence.
