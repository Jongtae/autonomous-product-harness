# Incident and Recovery Contract

Autonomous delivery is incomplete unless the team can detect failure, recover safely, and prevent recurrence.

## Recovery loop

```text
detect
  ↓
classify
  ↓
contain
  ↓
rollback / recover
  ↓
record incident evidence
  ↓
root cause
  ↓
regression protection
  ↓
redeploy
  ↓
verify
```

## Required behavior

For a production-affecting failure:

1. **Detect** from CI, smoke checks, monitoring, security/privacy canaries, or credible user evidence.
2. **Classify** severity and blast radius.
3. **Contain** further rollout or risky automation when appropriate.
4. **Recover quickly** using the last-known-good artifact or another preapproved recovery mechanism.
5. **Record evidence**: timestamps, release SHA, affected surface, symptoms, and actions taken.
6. **Find root cause**, not only the visible symptom.
7. **Add regression protection** with a test, invariant, check, or runbook improvement where practical.
8. **Redeploy** only after normal gates pass.
9. **Verify** both the original incident and adjacent risk.
10. **Update `TEAM_STATE.toml`** and team metrics from measured evidence.

## Recovery authority

A Release Operator may execute a preapproved rollback/redeploy without waiting for routine owner permission when:

- the recovery path is documented;
- the known-good artifact is verified;
- no irreversible data migration is involved; and
- the action does not cross a project-specific Human Gate.

If those conditions are not met, route to the appropriate Human Gate or architecture/security review.

## L4 proof

A recovery drill counts toward autonomy verification only when the team actually exercises detection → recovery → verification. A document describing how rollback *would* work is not proof.

Do not intentionally create unsafe user impact merely to satisfy a recovery metric. Prefer controlled drills or real incidents.
