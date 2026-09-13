# Contributing

Thanks for improving Autonomous Product Harness.

APH is intentionally small. Contributions should strengthen **governance, product learning, verification, portability, or adoption** rather than turn the project into another general-purpose agent runtime.

## Good contribution areas

- clearer Human Gate patterns;
- stronger role-authority separation;
- better behavioral governance evals;
- safer migration/adoption logic;
- additional framework adapters that preserve APH semantics;
- incident/recovery verification;
- better template/profile ergonomics;
- real dogfooding evidence and failure cases;
- documentation that reduces ambiguity without adding ceremony.

## Usually out of scope

- bespoke LLM runtimes;
- generic swarm schedulers;
- vector-memory platforms;
- spec-generation systems;
- cloud execution control planes;
- replacing existing coding-agent ecosystems.

Prefer composition and adapters.

## Pull request expectations

A contribution should explain:

- problem being solved;
- affected APH profile(s);
- governance/safety implications;
- tests/evals added or updated;
- migration impact for existing adopters.

Run before submitting:

```bash
python scripts/check_harness.py
```

## Behavioral eval changes

Do not change an expected eval outcome merely because a model failed it.

If the governance contract itself should change:

1. document the policy change;
2. explain why the old expectation was wrong;
3. update the eval fixture;
4. add regression coverage for the newly discovered failure mode.

## Evidence

Real-world failures are especially valuable. When contributing an incident or autonomy-run example, keep records factual and avoid including secrets, personal data, or private chain-of-thought.
