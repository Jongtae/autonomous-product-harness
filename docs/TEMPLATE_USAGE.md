# GitHub Template Usage

The template path is optimized for **new repositories**.

## One-time repository owner step

On GitHub, enable the repository setting:

**Settings → General → Template repository**

After that, visitors can use **Use this template** to create a clean repository with the APH baseline.

## After creating from the template

1. Rename / describe the repository for the actual product.
2. Replace placeholder values in `TEAM_STATE.toml`.
3. Ask your coding agent to inspect the repository and choose the minimum sufficient APH profile.
4. Remove governance files not needed by the chosen profile rather than carrying unused ceremony.
5. Add product-specific architecture, privacy/security, release, and domain invariants.
6. Run:

```bash
python scripts/check_harness.py
```

7. Commit the initialized state before long-running autonomous work begins.

## Recommended initialization prompt

```text
You are adopting Autonomous Product Harness in this repository.

First inspect the entire repository and existing instructions/CI/docs.
Choose the minimum sufficient autonomy profile from docs/AUTONOMY_PROFILES.md.
Preserve existing conventions and merge rather than overwrite useful project guidance.
Initialize TEAM_STATE.toml from repository reality.
Make Human Gates explicit and minimal.
Install only the governance/eval assets required by the selected profile.
Run the harness checks.
Then continue real product work instead of stopping at setup.
```

## Template philosophy

The template is a **baseline**, not a product architecture.

APH does not prescribe:

- programming language;
- frontend/backend framework;
- cloud provider;
- database;
- LLM provider;
- agent runtime;
- spec methodology;
- issue tracker beyond durable work/evidence requirements.

Projects should compose APH with the implementation systems they already use.
