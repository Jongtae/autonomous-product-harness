# Human Gates

Human Gates are actions that **genuinely require a person** because they are irreversible, legally meaningful, identity-bound, financially material, or blocked by a system that only the owner can satisfy.

They are not a general permission mechanism for routine product work.

## Default Human Gates

A product should normally stop and ask for a person only when one of these applies:

- CAPTCHA, MFA, email/phone verification, identity verification, account recovery;
- accepting owner-only legal/platform/developer terms;
- signing contracts or representations on behalf of a person or company;
- material spend, purchasing, or irreversible billing commitments beyond an approved budget;
- irreversible destructive production operations without a verified rollback path;
- DNS/domain ownership steps requiring owner credentials;
- security credential enrollment that cannot be delegated safely;
- legal or reputational decisions whose policy is not already defined;
- ambiguous external-community rules where an incorrect action could cause account sanctions;
- explicit project-specific gates added by the owner.

## Not Human Gates by default

Do **not** stop for routine reversible work such as:

- implementation within established architecture;
- creating or updating tests;
- fixing reproducible defects;
- drafting documentation;
- opening normal issues or pull requests;
- low-risk refactors within scope;
- CI retries and safe diagnostics;
- analysis of public feedback;
- routine product decisions already covered by `PRODUCT_DECISION_POLICY.md`;
- normal release actions when release authority and rollback procedures are already defined.

## Minimal blocker rule

If a Human Gate blocks only one workstream:

1. record the exact blocker;
2. state the single action the person must perform;
3. continue every other safe, unblocked workstream;
4. resume the blocked workstream after the gate is cleared.

## Project-specific additions

Projects using APH should add project-specific gates here rather than scattering ad-hoc approval rules across prompts.

## Safety rule

Never invent a Human Gate merely to reduce uncertainty. Never bypass a real Human Gate to improve autonomy metrics.
