# AI-Visible Web Architecture

Public reference architecture for building AI-visible websites, using [chudi.dev](https://chudi.dev) as the live case study.

This repository documents how one public site is designed to work across three access modes at once:

- human reading
- LLM retrieval and citation
- AI agent interaction

## Status

- Maintenance: active
- Trust model: evidence-first
- Primary truth levels:
  - `Verified`: backed by live public surfaces or runnable checks
  - `Inferred` or `Target State`: explanatory or recommended architecture beyond what is directly observable

## What Is Live Today on `chudi.dev`

- `llms.txt`, `llms-full.txt`, `ai.txt`, and `.well-known/llms.json`
- structured identity metadata and topic-based site organization
- answer-oriented content designed for retrieval and citation
- browser-side WebMCP tooling for direct agent queries

## What This Repo Generalizes

- a reusable architecture pattern for AI-visible websites
- a contract for machine-readable discovery surfaces
- an evidence model for separating verified public behavior from system interpretation
- an executable verification loop so claims can be checked instead of trusted

## Start Here

- [Whitepaper](./whitepaper/the-ai-visible-personal-website.md)
- [Live Surfaces](./proof/live-surfaces.md)
- [Live Audit](./proof/live-audit.md)
- [Verification Matrix](./proof/verification-matrix.md)
- [Machine-Readable Interface Contract](./architecture/machine-readable-interface-contract.md)

## Architecture Map

### Verified system views

- [Verified Surface Architecture](./architecture/verified-surface-architecture.md)
- [Machine-Readable Identity Layer](./architecture/machine-readable-identity.md)
- [Retrieval and Citation Flow](./architecture/retrieval-and-citation-flow.md)
- [Agent Interface Layer](./architecture/agent-interface-layer.md)

### Conceptual and target-state views

- [Conceptual System Architecture](./architecture/conceptual-system-architecture.md)
- [Target Operating Model](./architecture/target-operating-model.md)
- [Source-of-Truth Operations](./architecture/source-of-truth-operations.md)

### Diagrams

- [Verified System Context Map](./diagrams/system-context-map.md)
- [Verified Surface Contract Stack](./diagrams/surface-contract-stack.md)
- [Conceptual Content-to-Surface Pipeline](./diagrams/content-to-surface-pipeline.md)
- [Verified Retrieval and Citation Sequence](./diagrams/retrieval-and-citation-sequence.md)
- [Verified Agent Query Sequence](./diagrams/agent-query-sequence.md)
- [Verified Identity Graph](./diagrams/identity-graph.md)
- [Target State Infrastructure and Delivery Topology](./diagrams/infrastructure-and-delivery-topology.md)
- [Theory-to-Implementation Map](./diagrams/theory-to-implementation-map.md)

## Verification

Run the local checks:

```bash
python3 -m py_compile scripts/*.py
python3 scripts/check_repo_quality.py
python3 scripts/audit_live_surfaces.py
```

The live audit verifies that the public surfaces described here still exist and still satisfy the documented contract.

The default branch is protected by the `quality` gate, so repository changes are expected to move through pull requests rather than direct pushes.

## Contributing and Governance

- [Contributing Guide](./CONTRIBUTING.md)
- [Security Policy](./SECURITY.md)
- [Support](./SUPPORT.md)
- [Agent Capability Profile](./operations/agent-capability-profile.md)
- [Agent Standards Pack](./operations/agent-standards-pack.md)
- [Research and Evidence Rules](./operations/research-and-evidence-rules.md)
- [GitHub Repository Configuration](./operations/github-repository-configuration.md)

## Repository Structure

- `architecture/`: architecture layers, contracts, and operating model docs
- `proof/`: verified live surfaces, audit contract, and claim-to-check mapping
- `examples/`: representative local specimens of public machine-readable surfaces
- `diagrams/`: Mermaid architecture and flow diagrams for GitHub rendering
- `operations/`: repository settings and governance guidance that live outside git-tracked code
- `scripts/`: executable verification utilities
- `whitepaper/`: longer-form framing for the overall pattern

## Constraint

This repository is deliberately evidence-first. It distinguishes between what is already implemented on `chudi.dev` and what appears to generalize as a reusable web pattern.

That boundary matters. The goal is technical clarity, not category hype.
