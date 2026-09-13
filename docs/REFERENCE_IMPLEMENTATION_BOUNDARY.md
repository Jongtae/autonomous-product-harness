# Reference Implementation Boundary

Autonomous Product Harness (APH) is a reusable governance and autonomy-verification layer. A product that dogfoods APH is **not required to install every integration APH supports**.

## Principle

> **The framework may support more than the product uses.**

A dogfood product should adopt only the smallest set of tools that improves its product delivery and autonomous operation. It must not become a showcase or museum of integrations.

APH may provide optional adapters, examples, or guidance for tools such as:

- GitHub Spec Kit for specification/planning workflows;
- Ruflo or other orchestration engines for larger execution topologies;
- AgentOS or other persistent runtimes/control planes for long-running ownership and execution continuity.

Those capabilities are optional. Their existence in APH does not create an adoption obligation for any reference product.

## Product-first adoption rule

Use:

> **Observed pain before framework.**

A product should add an external framework only when a recurring, concrete operational problem has been recorded and the new dependency removes more complexity than it introduces.

Recommended adoption questions:

1. What repeated problem exists today?
2. Why can the current stack not solve it simply?
3. What exact responsibility will the new framework own?
4. Which system remains canonical for product truth, work identity, and release audit?
5. What duplicated state or lifecycle is introduced?
6. Does the integration weaken privacy, security, Human Gates, or role authority?
7. What is the rollback/removal path?
8. How will we know after adoption that complexity actually decreased?

## Authority model

APH remains responsible for governance concepts such as:

- Human Gates;
- role authority/separation;
- evidence-to-decision policy;
- Decision Ledger conventions;
- autonomy verification and graduation criteria.

Optional integrations may own narrower concerns:

- specification/planning;
- orchestration/scheduling;
- persistent execution/runtime state;
- external tool-specific operations.

They must not silently become a second product-governance authority.

## Reference implementations

A reference implementation is valuable when it proves APH can govern a real product under realistic constraints. It is **not** more credible because it enables every adapter.

The preferred relationship is:

`real product pain → reusable APH pattern → optional adapter/support → products adopt only when useful`

Not:

`APH adds integration → reference product installs integration to demonstrate APH`

## INYEON

INYEON is the first major dogfood/reference implementation for APH, but its own repository governance decides its active stack. INYEON may remain on GitHub + Codex native agents + APH governance for as long as that stack is sufficient.

Future Spec Kit, Ruflo, AgentOS, or other integrations should be justified by INYEON's observed friction, not by APH's roadmap.
