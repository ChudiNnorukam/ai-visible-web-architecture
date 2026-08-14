# Conceptual System Architecture

> Evidence boundary: this document explains the pattern in generalized form. Components marked conceptual may exist in different concrete implementations and should not be read as proof of private internals on `chudi.dev`.

## Purpose

An AI-visible website needs one authority graph that can support:

- page rendering for humans
- retrieval and citation for models
- direct querying for agents

## Conceptual Components

The generalized website architecture has five core subsystems:

1. content source of truth
2. presentation layer for human pages
3. machine-readable export layer
4. agent interface layer
5. verification and operations loop

The live portfolio demonstrates two additional cross-property subsystems that
sit around, rather than inside, an individual website:

6. entity authority and calibrated citation measurement
7. crawler policy, runtime telemetry, and drift detection

The ownership boundary across the architecture, audit tooling, and product
implementation is recorded in
[portfolio-repository-map.md](./portfolio-repository-map.md).

## Design Rule

The same underlying facts should flow into all public surfaces. If the visible site, discovery files, schema, and agent interfaces diverge, the system becomes harder to trust and harder to cite.

## Supporting Docs

- [architecture/machine-readable-interface-contract.md](./machine-readable-interface-contract.md)
- [architecture/source-of-truth-operations.md](./source-of-truth-operations.md)
- [diagrams/content-to-surface-pipeline.md](../diagrams/content-to-surface-pipeline.md)
- [diagrams/theory-to-implementation-map.md](../diagrams/theory-to-implementation-map.md)
