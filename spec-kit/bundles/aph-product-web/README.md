# APH Product Web Foundation — Spec Kit bundle scaffold

This directory is the first **composition scaffold**, not yet a published community bundle and not yet a claim of a one-command complete APH installation.

Spec Kit bundles are a distribution/composition layer over extensions, presets, steps, and workflows. They do not add runtime behavior themselves. This scaffold intentionally keeps that responsibility boundary.

## What this bundle currently provides

`bundle.yml` follows Spec Kit bundle schema `1.0` and pins only a built-in component that APH can rely on without introducing a second implementation framework:

- `agent-context` `1.0.0`

The bundle is integration-agnostic and inherits the target project's active coding-agent integration.

The APH `product-web` governance starter remains in this repository under:

```text
starters/product-web/
```

The portable APH adoption skill remains under:

```text
skills/autonomous-product-harness/
```

Those layers own APH's product-governance contract. The Spec Kit bundle should not duplicate them as a parallel runtime.

## Superpowers integration

Superpowers is an **external implementation-discipline dependency**, not vendored APH code.

When the active runtime already exposes Superpowers, use upstream skills for capabilities such as:

- test-driven development;
- systematic debugging;
- subagent-driven task execution;
- requesting/receiving code review;
- verification before completion.

Do not copy those skill texts into APH.

For teams that want a Spec Kit ↔ Superpowers handoff, the community catalog currently contains `speckit-superpowers-bridge` (v1.2.0 at the time this scaffold was authored). It is community-maintained, not audited or endorsed by Spec Kit maintainers. Review its source and trust boundary before installing it.

Because community component catalogs may be discovery-only by default, this foundation bundle does **not** silently install the bridge. A production-ready APH bundle may add it only after the full install path is verified from a clean Spec Kit project with the required install-allowed catalog configuration.

## Local validation target

With a compatible Spec Kit installation, authoring should eventually be validated with:

```bash
specify bundle validate --path ./spec-kit/bundles/aph-product-web
specify bundle build --path ./spec-kit/bundles/aph-product-web
```

A future issue should add clean-environment install evidence before this bundle is published or advertised as one-command bootstrap.

## Intended end state

The long-term user experience should be Bootstrap-like:

```text
product idea
  → choose APH starter
  → initialize Spec Kit composition
  → use upstream implementation skills
  → prove one vertical slice
  → advance through APH product-value / release / autonomy gates
```

But APH should reach that end state by composing proven primitives, not by rebuilding a planner, debugger, reviewer, or orchestration runtime.
