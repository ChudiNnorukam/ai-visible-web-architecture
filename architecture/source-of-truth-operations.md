# Source-of-Truth Operations

> Evidence boundary: this document is mostly target state. It describes the operating discipline required to keep an AI-visible site consistent across human, machine-readable, and agent-facing surfaces.

## Goal

One authority graph should drive the page layer, discovery layer, and agent layer.

## Operating Model

1. content and identity facts originate in a single source of truth
2. public pages, schema, discovery files, and agent tools derive from the same facts
3. repository docs describe the contract those outputs must satisfy
4. automated checks detect drift between the contract and the live system
5. maintainers update proof docs whenever a public contract changes

## Drift Risks

- page content updates without matching discovery updates
- machine-readable identity changes without proof or example refresh
- agent tools exposing different semantics than the visible site
- documentation claiming behavior no longer observable on the live system

## Repository Control Loop

- examples provide local specimens
- proof docs capture live public evidence
- diagrams explain the system from verified and target-state views
- scripts and workflows enforce the minimum contract

## Supporting Diagram

- [diagrams/infrastructure-and-delivery-topology.md](../diagrams/infrastructure-and-delivery-topology.md)
