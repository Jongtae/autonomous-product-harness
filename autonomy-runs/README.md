# Autonomous Run Evidence

Use this directory to record factual evidence for qualifying autonomous product loops.

Suggested filename:

```text
RUN-0001-YYYY-MM-DD.md
```

Template:

```markdown
# RUN-0001

Started: YYYY-MM-DDTHH:MM:SSZ
Ended: YYYY-MM-DDTHH:MM:SSZ
Profile: L4

## Trigger / evidence
- links, issue ids, experiment ids, production signals

## Selected goal / work
- why this was the highest-value unblocked action

## Roles used
- operator / analyst / judge / implementer / verifier as applicable

## Decisions / Human Gates
- decisions taken
- Human Gates encountered
- owner intervention, if any, and whether it was a declared gate

## Implementation / release
- issue / PR / commit / release refs

## Verification
- CI / QA / security / privacy / smoke results

## Recovery
- rollback/recovery actions if applicable

## Result / learning
- observed outcome
- state update
- next action
```

Do not record private chain-of-thought. Store observable evidence, concise rationale, decisions, and results.
