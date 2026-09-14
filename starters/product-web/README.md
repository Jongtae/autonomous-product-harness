# APH Product Web Starter

Use this starter for a user-facing web product whose value can be demonstrated through one primary browser journey.

The goal is not to prescribe a framework. The goal is to prevent the team from spending large amounts of work on infrastructure, policy, or autonomy proof before a real user can obtain the intended product outcome.

## Default primary journey

Define one concrete journey before broad implementation:

```text
entry
  → required user input/action
  → core product computation/service
  → user-visible result
  → explanation or next meaningful action
```

Replace each placeholder with product-specific behavior. The journey must be executable through the real UI or deployed preview, not only through unit tests or internal APIs.

## Default milestone sequence

1. **Functional Alpha** — one realistic case completes end to end locally.
2. **Value Preview** — a deployed/release-candidate preview delivers the intended user outcome through black-box Product Acceptance.
3. **Correctness Candidate** — domain/calculation/content correctness meets the project's evidence bar.
4. **Release Candidate** — privacy, security, accessibility, reliability, and regression gates pass.
5. **Production** — deployment, smoke, rollback/recovery, and public disclosures are verified.
6. **Autonomy Proof** — only after the earlier product-value milestones are real.

Safety-critical work may happen earlier, but later milestones never count as evidence that an earlier milestone exists.

## Black-box Product Acceptance

The acceptance test must answer:

> Can a user enter through the real product surface, complete the primary journey, and receive the intended product value without hidden setup or owner guidance?

A passing test must verify the **outcome**, not merely page existence, HTTP 200, component rendering, or the absence of exceptions.

Default failure conditions include:

- the primary action does nothing;
- realistic user input is unsupported without a product requirement saying so;
- the flow ends in placeholder, empty, `coming soon`, or `not available yet` output instead of the intended value;
- the result exists only in logs/tests/internal state;
- a user needs the owner to explain the next step;
- the deployed preview behaves differently from the tested local build in a way that removes the value.

## Vertical Slice First

Until the Value Preview passes, default to work that changes one of:

- primary-journey functionality;
- user-visible result/value;
- the concrete blocker preventing the journey;
- black-box Product Acceptance coverage.

Do not expand datasets, agent infrastructure, orchestration, governance artifacts, release drills, community operations, or autonomy-proof ceremony unless that work directly removes the current blocker.

## Human Gate behavior

A failed primary journey is **not** a Human Gate.

When work is blocked:

```text
dependency block → implement/resolve prerequisite
acceptance failure → remediate the product
one Human Gate → park that stream and continue another meaningful stream
all meaningful work blocked by genuine Human Gates → ask the owner for the smallest required action
```

Do not ask the owner to choose the next task when the goal and repository state already determine it.

## Anti-waste default

After three substantial implementation cycles with no change in Product Acceptance and no material reduction of the concrete blocker:

1. stop the current approach;
2. identify the assumption that is not producing state change;
3. change the implementation strategy, acceptance contract, or task decomposition;
4. resume autonomously unless a genuine Human Gate applies.

Do not respond by generating more fixtures, ADRs, reviews, or documentation merely to remain active.

## Suggested composed stack

When available:

```text
Product/domain rules
  + APH User Value / Human Gate / autonomy governance
  + Spec Kit spec → plan → tasks
  + Superpowers implementation disciplines
  + coding-agent runtime
  + GitHub PR / CI / preview
```

Spec Kit and Superpowers are optional external dependencies. APH standalone mode remains valid.

## Starter prompt

A coding agent adopting this starter can be told:

```text
Adopt the APH product-web starter.
Define the primary user journey and black-box Product Acceptance before broad implementation.
Use Vertical Slice First and work at the earliest unproven proof-ladder rung.
If a task is blocked, descend into its prerequisite or reroute to another meaningful unblocked task.
A Human Gate parks only the affected stream.
Do not ask me what to do next when repository state can determine it.
Stop only when all meaningful remaining work is blocked by genuine Human Gates or no meaningful work remains.
```
