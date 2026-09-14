# User Value Gate

APH must prevent autonomous teams from optimizing delivery proxies while the product's primary user value remains unproven.

Passing tests, CI, security/privacy checks, release gates, or autonomy evals is necessary when applicable, but none of those alone proves that a user can complete the core journey and receive the intended outcome.

## Core rule

> **Autonomy cannot advance beyond the highest product-value milestone that has been demonstrated end to end.**

A later maturity proof cannot compensate for an unproven earlier product milestone.

## Proof ladder

Use the following order unless the project documents a stricter equivalent:

1. **Functionality** — the primary journey executes end to end.
2. **User value** — the journey produces the intended outcome, not a placeholder or empty state.
3. **Correctness / domain validation** — calculations, methodology, and claims meet the project's evidence bar.
4. **Safety / privacy / reliability** — invariants, abuse boundaries, accessibility, and resilience pass.
5. **Release / recovery** — production deployment, smoke, rollback, and recovery are proven.
6. **Autonomy proof** — closed loops, behavioral evals, session continuity, and recovery evidence may advance.

Projects may perform safety work earlier when risk requires it, but they must not count later-rung work as proof that earlier product value exists.

## Vertical Slice First

For a new product, major feature, or product-recovery phase, prove one complete user-facing vertical slice before expanding supporting infrastructure or autonomy machinery.

The slice must exercise the real product path through the real interface or public contract. A synthetic fixture that bypasses the user-facing path is supporting evidence, not Product Acceptance.

Examples:

- form input → calculation → visible result;
- upload → processing → usable output;
- search → selection → intended action;
- create → publish → externally observable artifact.

## Black-box Product Acceptance

A Product Acceptance role/check should evaluate the deployed or release-candidate product from the outside and answer:

> Does the product deliver the primary user outcome defined by the product goal?

It should not grade its own implementation work and should not use commit counts, fixture counts, or internal architecture quality as substitutes for the outcome.

The gate fails when, for example:

- the main CTA produces no useful result;
- an empty/placeholder/disclosure state is counted as delivery of the core value;
- only an unrealistic happy-path input works;
- the implementation satisfies a lower-level spec while contradicting the higher-level product goal;
- unit/integration tests pass but the release candidate cannot complete the core journey.

Automate this as a black-box E2E or contract test wherever practical. Owner review should be milestone-level and exceptional, not the routine verification mechanism.

## Progress definition

Progress means a meaningful change in one or more of:

- user-visible product capability;
- Product Acceptance state;
- release state;
- a concrete blocker;
- real external evidence;
- verified recovery/correctness evidence required for the current milestone.

The following do not count as progress by themselves:

- commits;
- test/fixture count;
- more ADRs or status documents;
- repeated review of an unchanged candidate;
- repeated CI/test execution without changed code or newly identified risk;
- more synthetic data that does not change Product Acceptance;
- autonomy-eval or governance activity that cannot advance because a lower product-value milestone is still unproven.

## Anti-waste stop rule

If **three substantial implementation cycles** complete without either:

1. changing black-box Product Acceptance, or
2. materially reducing a concrete blocker to Product Acceptance,

stop that stream and re-evaluate the goal, acceptance contract, or approach before doing more work.

Do not create preparatory artifacts merely to remain active.

This is normally an autonomous re-evaluation, not a Human Gate.

## Human Gates

Do not solve weak product acceptance by adding routine owner approvals.

Human Gates should remain narrow: identity-bound, legal, financially material, irreversible, security/privacy-critical, methodology-authority, or otherwise genuinely owner-only.

The harness should automate product acceptance and escalate only when a true Human Gate exists.

## Work traceability

For material repository changes, require an issue-backed delivery path:

`Issue → branch/change → tests/review → PR → CI → merge → close when Definition of Done is satisfied`

A PR may deliver one coherent part of a larger issue without closing it when the issue's Definition of Done remains unmet.

Direct-to-main material changes are not the normal operating path.

## L4 implication

A project must not use strong governance/release evidence to outrun weak product evidence.

Before L4 verification can be meaningful, the project must have at least one demonstrated primary user-value path at the appropriate release stage. If a material escaped defect later proves that the supposed primary value was never actually delivered, the autonomy proof should be treated as invalidated until Product Acceptance is restored.
