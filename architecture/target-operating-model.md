# Target Operating Model

> Evidence boundary: this document is target state. It describes how a production-grade AI-visible website should be operated, not what has been fully proven from the public internet today.

## Goal

Move from "interesting public implementation" to "durable, auditable system".

## Target Capabilities

- one documented contract for all machine-readable surfaces
- automated validation on every repository change
- scheduled verification against live public endpoints
- diagrammed ownership of content, metadata, interfaces, and monitoring
- clear incident and drift response paths when public surfaces diverge

## Operational Standard

A mature AI-visible site should be treated like a small public platform:

- public interfaces are versioned or tightly documented
- verification failures produce visible artifacts
- evidence and architecture documentation stay in sync
- governance and security posture are explicit

## Supporting Docs

- [operations/github-repository-configuration.md](../operations/github-repository-configuration.md)
- [proof/live-audit.md](../proof/live-audit.md)
- [diagrams/infrastructure-and-delivery-topology.md](../diagrams/infrastructure-and-delivery-topology.md)
