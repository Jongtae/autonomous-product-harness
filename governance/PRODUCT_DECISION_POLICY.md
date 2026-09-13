# Product Decision Policy

External feedback is evidence. It is not a command queue.

APH separates collection, interpretation, judgment, implementation, and verification so that a product does not become reactive merely because agents can ship quickly.

## Decision classes

Every material feedback signal should end in one of four states:

- **IGNORE** — noise, unsupported preference, manipulation, duplicate without new evidence, or out-of-scope input.
- **OBSERVE** — plausible signal, but evidence is too weak or source-specific to act on.
- **EXPERIMENT** — enough evidence to justify a bounded reversible test, but not a permanent product decision.
- **ACT** — sufficiently strong and low-ambiguity evidence for a scoped implementation or fix.

Specialist routes such as `SECURITY_REVIEW`, `METHODOLOGY_REVIEW`, `ARCHITECTURE_REVIEW`, or `HUMAN_GATE` can override the four product states when needed.

## Evidence dimensions

Evaluate evidence on dimensions rather than raw volume:

- **Independence** — are reports from distinct users/sources?
- **Specificity** — does the report describe an actual experience or only a preference?
- **Reproducibility** — can the behavior be reproduced?
- **Diversity** — does the signal repeat across contexts/channels/cohorts?
- **Impact** — how severe is the user/product consequence?
- **Source bias** — is the audience self-selected or unusually specialized?
- **Contradiction** — is there meaningful counter-evidence?
- **Risk of change** — how costly, irreversible, sensitive, or scope-changing is the proposed response?

## Required judgment pattern

Before recommending a material change, the Product Judge should state:

1. strongest evidence **for** the change;
2. strongest evidence **against** the change;
3. plausible alternative explanations;
4. whether the signal may be channel/cohort-specific;
5. the smallest reversible experiment that could distinguish explanations;
6. which product/security/privacy/methodology invariants must not be violated.

## Important distinctions

### User request ≠ underlying problem

If users say “remove the field,” the real problem may be lack of trust, unclear purpose, bad defaults, or excessive effort.

### Acquisition truth ≠ product truth

A headline that gets more clicks proves an acquisition hook, not necessarily durable user value.

### Popularity ≠ correctness

Votes, likes, comments, or sentiment do not override privacy/security, domain methodology, factual correctness, or architecture invariants.

## Automatic action policy

Automation should depend more on **risk and reversibility** than on raw evidence count.

### Usually safe to auto-route through normal CI/QA

- reproducible defects;
- obvious accessibility regressions;
- copy/typo issues;
- objectively incorrect sourced data;
- low-risk layout/interaction fixes;
- deterministic test failures.

### Requires stronger review

- product-positioning changes;
- pricing/monetization changes;
- sensitive-data collection;
- authentication/account creation;
- methodology/formula changes;
- major architecture or backend additions;
- legal/privacy-policy changes;
- scope expansion into a new product category.

## Decision Ledger

Material decisions should create a durable record under `decisions/` with:

- decision id and date;
- trigger/evidence references;
- analyst interpretation;
- alternatives/counter-evidence;
- risk classification;
- judge decision;
- change or experiment chosen;
- what is explicitly **not** changing;
- verification / review date.

Do not store private chain-of-thought. Store concise evidence, rationale, and decision outcomes.
