# Role Authority Matrix

APH separates **execution authority** from **judgment authority** so that one agent does not create evidence, interpret it, approve a change, implement it, and declare success by itself.

Use fewer roles for smaller profiles; preserve the same boundaries when roles are combined.

| Role | May do | Must not do | Typical veto / escalation |
|---|---|---|---|
| **Architect** | define technical boundaries, review architecture changes, resolve design tradeoffs | silently expand product scope or weaken privacy/security constraints | veto architecture that violates project invariants |
| **Worker / Implementer** | implement approved issues, add tests, update docs within scope | reinterpret weak feedback as a product mandate; widen accepted scope | escalate missing requirements or architecture conflicts |
| **QA / Release verifier** | reproduce bugs, verify acceptance criteria, run regression/E2E/smoke tests | approve its own implementation as independent review | block release on failed acceptance or regression |
| **Security / Privacy reviewer** | review data flow, secrets, permissions, threat boundaries | trade away defined privacy/security guarantees for convenience | block release and require remediation |
| **Community / Channel Operator** | publish approved experiments, engage communities, collect raw evidence | grade its own campaign or turn comments directly into features | stop outreach on rule/moderation/safety signals |
| **Feedback Analyst** | normalize, cluster, deduplicate, identify underlying problems and alternative explanations | implement changes or declare product direction | mark evidence as weak, biased, contradictory, or source-specific |
| **Product Judge** | preregister hypotheses, evaluate evidence, choose IGNORE / OBSERVE / EXPERIMENT / ACT | treat popularity as truth; bypass methodology/privacy/security firewalls | reject weak evidence, request experiment, route to specialist review |
| **Release Operator** | deploy approved artifacts, execute documented rollback/redeploy | waive failed gates merely to ship | rollback to known-good state when contract requires |

## Core boundary

For material product-learning work:

```text
Operator ≠ Analyst ≠ Judge ≠ Implementer ≠ Release verifier
```

For low-risk projects, one model/session may perform multiple roles sequentially **only if the context explicitly resets the role and preserves independent evidence/review boundaries**. High-risk projects should use distinct agents or isolated contexts.

## High-risk change classes

The following require specialist review even if user feedback is popular:

- privacy/security/data-retention changes;
- authentication/identity changes;
- financial/legal commitments;
- core methodology or domain-rule changes;
- irreversible infrastructure migrations;
- material architecture expansion;
- changes that weaken Human Gates or verification criteria;
- autonomous scope expansion into a different product category.

## Least-authority principle

Give every agent the minimum write/action authority needed for its role. A feedback analyst does not need production deploy permissions. A community operator does not need code write permissions. A worker does not need authority to rewrite the Human Gate policy.
