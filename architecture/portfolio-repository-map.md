# AI Visibility Portfolio Repository Map

> Status: `Verified` from public repository metadata, local repository
> inspection, and live public surfaces on 2026-07-11.

## Canonical Ownership

| Repository | Canonical responsibility | Lifecycle |
|---|---|---|
| `ai-visible-web-architecture` | Public architecture, vocabulary, evidence model, cross-property contracts, and implementation-neutral guidance | **Main knowledge repository** |
| `ai-visibility-readiness` | Open-source AVR probes, scoring logic, fixtures, and runnable audit tooling | **Maintained executable specification** |
| `citability-dev` | Private product implementation, customer workflows, receipts, dashboards, and commercial operations | **Maintained product** |

The authoritative human-readable AVR methodology is
`https://chudi.dev/framework`. This repository explains how AVR composes with
the wider web architecture; `ai-visibility-readiness` makes its checks
runnable; `citability-dev` operationalizes it.

## Supporting and Retired Repositories

| Repository | Responsibility | Lifecycle rule |
|---|---|---|
| `seo-geo-control` | Portfolio GSC, freshness, and search-operations control plane | Keep separate; it owns operational state, not architecture |
| `seoauditlite` | Lightweight public AEO audit application with current production deployments | Keep as a separate product; it is not a methodology authority |
| `ai-visibility-readiness-v1-archive` | Historical AVR v1.0 snapshot | Archived |
| `ai-visibility-rd` | Empty private repository with no unique source or documentation | Retired |

Retired repositories are historical evidence, not sources of current
terminology or methodology.

## Architecture Learned From the Live Portfolio

The original three on-site layers remain the foundation, but the live system
now demonstrates four additional operational layers:

1. retrieval-aware information design;
2. machine-readable identity and discovery;
3. agent wayfinding and action surfaces;
4. entity and cross-property authority;
5. calibrated citation measurement and signed receipts;
6. crawler access and content-usage policy;
7. runtime telemetry, drift detection, and verification.

The last four do not all belong inside every website. They are portfolio-level
capabilities that compose with the reusable three-layer website pattern.

## Live Contracts That Supersede Older Claims

- AVR is **AI Visibility Readiness**. VRC means Visibility,
  Recommendability, and Citability. The AVR Score has no separate expansion.
- The current public framework is v1.1.0. Live robots policies already cite
  the v1.2.0 content-intent convention.
- `chudi.dev/entitymap.json` and `citability.dev/entitymap.html` expose the
  cross-property entity graph.
- `citability.dev/.well-known/citability.json` exposes versioned methodology,
  model, verdict, receipt, and Agent Readiness metadata.
- `citability.dev/.well-known/agent-actions` is a live agent-action manifest.
- `ai-train`, `search`, and `ai-input` distinguish permission to access content
  from permission to train on, retrieve, or cite it.
- Retrieval crawlers such as `OAI-SearchBot`, `Perplexity-User`, and
  `Claude-User` are operationally distinct from training crawlers.

## Consolidation Rules

1. Architecture and shared vocabulary land here first.
2. Executable audit behavior stays in `ai-visibility-readiness` and links back
   to the architecture claim it tests.
3. Product-only implementation details stay in `citability-dev`.
4. No other repository may declare a competing canonical expansion, score
   model, or framework version.
5. Live claims graduate from `Inferred` to `Verified` only when a public
   surface and a reproducible check both exist.
