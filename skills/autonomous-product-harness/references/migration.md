# Existing Repository Migration Guidance

APH adoption should improve governance without destroying working project conventions.

## Inspect before modifying

Identify existing equivalents of:

- root agent instructions;
- state / roadmap / issue queue;
- architecture decisions;
- privacy/security policy;
- CI and release gates;
- incident/rollback docs;
- feedback/research process;
- role definitions;
- evals and test fixtures.

## Merge rules

1. **Do not overwrite a useful `AGENTS.md`.** Add APH principles only where missing and resolve conflicts deliberately.
2. **Prefer one source of truth.** If an existing file already owns Human Gates or release policy, extend it instead of duplicating policy.
3. **Keep stricter rules.** APH defaults are not permission to weaken project-specific privacy/security/legal controls.
4. **Preserve product facts.** Do not replace real architecture/deployment details with generic APH placeholders.
5. **Initialize unknowns honestly.** Use `not-run`, `unknown`, empty values, or zero when evidence does not exist.
6. **Separate cleanup from product changes.** Avoid silently changing product behavior while “installing governance.”
7. **Record material precedence changes.** If a stale instruction is superseded, make that explicit in a durable decision/ADR.

## Conflict examples

### Existing AGENTS says every external post requires owner approval, but current Human Gate policy grants standing authorization

- determine which rule is current and higher-precedence;
- repair the stale rule rather than asking the owner every time;
- add a consistency check if the conflict could recur.

### Existing CI deploys directly from main with no rollback state

- profile S/M may leave deployment outside APH scope;
- profile L/L4 should add known-good release tracking and recovery verification before claiming autonomous delivery.

### Existing product stores sensitive data but no privacy review exists

- do not auto-upgrade to L4 and continue blindly;
- route to security/privacy review and establish data-handling invariants first.

## Completion

Migration is complete only when:

- root instructions and governance no longer contradict each other;
- selected profile requirements are satisfied;
- state reflects reality;
- checks pass;
- any remaining blocker is a real Human Gate or explicit unimplemented issue.
