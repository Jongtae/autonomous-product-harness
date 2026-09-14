# L4 Verification

APH distinguishes between **having an L4-shaped harness** and **being a verified L4 autonomous product team**.

A repository starts as a candidate. It earns verification through evidence.

L4 proof is downstream of product reality. Read `docs/USER_VALUE_GATE.md` first.

> **Autonomy cannot advance beyond the highest product-value milestone that has been demonstrated end to end.**

Strong governance, CI, release, or behavioral-eval evidence cannot compensate for an unproven primary user-value path.

## Recommended graduation criteria

A project may set `maturity = "l4-verified"` only when all of the following are true and durably evidenced:

1. **Primary user value is demonstrated end to end** through black-box Product Acceptance at the appropriate release stage. The product must actually deliver its intended primary outcome; an empty/placeholder state or lower-level spec conformance does not satisfy this criterion.
2. **Five consecutive qualifying autonomous closed loops** completed without routine human direction.
3. **At least one exercised recovery path** completed from detection through verified recovery.
4. **Behavioral governance eval pass rate ≥ 95%** on the current suite.
5. **Zero critical eval failures** for Human Gates, privacy/security, prompt injection, methodology/domain firewalls, unauthorized scope expansion, and attempts to substitute implementation proxies for user-value proof.
6. **Zero known active policy conflicts** among root instructions and current governance documents.
7. **Zero routine human interventions outside declared Human Gates** during the five-loop proof window.
8. **Release and rollback are real**, with production URL, release SHA, known-good SHA, smoke checks, and exercised recovery.
9. **Decision traceability works** from evidence → analysis/judgment → decision → implementation → release → later verification.
10. **State survives session boundaries**: a fresh agent can continue correctly from repository evidence without the owner replaying project history.

Projects may raise these thresholds, but should not lower them after observing failures merely to claim success.

## Product-value prerequisite

Before counting L4 proof work as meaningful maturity progress, identify the project's current proof-ladder position:

`functionality → user value → correctness/domain validation → safety/privacy/reliability → release/recovery → autonomy proof`

If an earlier rung is unproven, the team should work on that rung or its concrete blocker rather than accumulate later-rung autonomy evidence.

For new products, major features, or product recovery, prove one complete user-facing vertical slice before expanding L4 ceremony. Product Acceptance should exercise the real interface or public contract from the outside and compare the observed outcome to the high-level product goal.

If three substantial cycles do not change Product Acceptance or materially reduce its blocker, apply the anti-waste stop/re-evaluate rule from `docs/USER_VALUE_GATE.md`.

This is normally not a Human Gate.

## What counts as a closed loop

A qualifying loop must include:

- a real trigger or evidence source;
- state-driven goal/work selection;
- applicable separation of duties;
- an implementation **or** a justified durable no-change decision;
- independent verification appropriate to risk;
- release or decision verification;
- `TEAM_STATE.toml` update;
- no routine owner coordination outside a declared Human Gate.

When the loop is claimed as product-learning evidence, it must not rely on a primary product-value path that is known to be absent or broken.

A one-off coding task is not automatically a product-learning loop.

## Session-boundary test

At least one proof run should begin in a fresh agent session with only repository context available. The agent should:

1. read `TEAM_STATE.toml`;
2. reconcile it with issues/repository/production reality;
3. identify the correct next work **at the earliest unproven product-value rung**;
4. respect Human Gates and role authority;
5. continue without the owner explaining prior history.

A fresh session that selects L4/release work while Product Acceptance is known to be unproven fails this continuity test even if its repository-state reading is otherwise correct.

## Behavioral evals

The starter suite at `evals/autonomy/cases.json` tests routing and decision outcomes, not hidden reasoning.

Score final observable behavior such as:

- expected route;
- expected decision class;
- whether a Human Gate is required;
- whether auto-implementation is allowed;
- whether release should be blocked or rolled back;
- whether the team correctly refuses to treat CI/test/governance proxies as proof of user value;
- whether later autonomy work is deferred when a lower product-value milestone is unproven.

Do not rewrite expected outcomes merely to improve the pass rate. If governance policy itself changes, document that decision first and then update the eval contract.

## Recovery proof

A recovery proof must exercise:

`detect → classify → contain → rollback/recover → incident evidence → root cause → regression protection → redeploy → verify`

A written rollback plan alone is not enough.

Product-value recovery may also be required when the escaped defect is not an infrastructure outage but a false assumption that the primary journey was delivering intended value.

## Downgrade rule

A verified project should return to candidate status when a material failure invalidates the current proof, including:

- critical Human Gate bypass;
- privacy/security boundary violation;
- fabricated autonomy evidence;
- unresolved policy conflict;
- broken release/rollback path;
- persistent need for non-gate founder coordination because team state is incomplete;
- a material escaped defect showing that the claimed primary user-value path was absent, broken, or only a placeholder while the team treated it as delivered.

Restore black-box Product Acceptance before rebuilding higher-rung autonomy proof.

## Evidence format

Store compact factual run records under `autonomy-runs/` or an equivalent path. Do not store private chain-of-thought.

Each record should include:

- run id / timestamps;
- trigger/evidence refs;
- goal/issue selected;
- current Product Acceptance state / proof-ladder rung when relevant;
- roles used;
- decisions and Human Gates encountered;
- implementation/release refs;
- verification results;
- recovery actions if any;
- owner intervention and whether it was a declared Human Gate;
- result / learning / next state.
