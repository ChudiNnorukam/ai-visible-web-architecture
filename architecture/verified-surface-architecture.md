# Verified Surface Architecture

> Evidence boundary: every claim in this document is backed by live public surfaces or repository verification. It does not infer private implementation details.

## Purpose

This is the architecture view you can defend entirely from the public internet and this repo's audit tooling.

## Verified Surface Set

`chudi.dev` currently exposes:

- `llms.txt`
- `llms-full.txt`
- `ai.txt`
- `.well-known/llms.txt`
- `.well-known/llms.json`
- navigational pages such as `/start`, `/topics`, and `/about`
- proof articles about WebMCP and AI discovery implementation

## Verified Architecture Claim

From those surfaces, this repo can verify that `chudi.dev` behaves like:

1. a human-readable website
2. a machine-readable identity and discovery node
3. an agent-facing interface surface

The proof is behavioral rather than internal. The site publishes explicit discovery endpoints, stable identity metadata, and at least one documented and publicly demonstrable agent tooling path.

## Supporting Docs

- [proof/live-surfaces.md](../proof/live-surfaces.md)
- [proof/live-audit.md](../proof/live-audit.md)
- [proof/verification-matrix.md](../proof/verification-matrix.md)
- [diagrams/system-context-map.md](../diagrams/system-context-map.md)
