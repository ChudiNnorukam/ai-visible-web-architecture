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
- documented and publicly demonstrated browser-side WebMCP tooling for direct agent queries

## What This Repo Generalizes

- a reusable architecture pattern for AI-visible websites
- a contract for machine-readable discovery surfaces
- an evidence model for separating verified public behavior from system interpretation
- an executable verification loop so claims can be checked instead of trusted

## Vocabulary and Naming

This repo's framework name is **"AI-Visible Web Architecture"**: the
reusable 3-layer pattern (retrieval-aware information design,
machine-readable identity and discovery, agent-facing interface
surfaces).

It is intentionally NOT abbreviated to "AVR" anywhere in this
repository. The acronym "AVR" already refers to several adjacent but
distinct things in the operator's portfolio:

| Term | Where it lives | What it is |
|---|---|---|
| AI-Visible Web Architecture | this repo | the 3-layer pattern (this document) |
| AI Visibility Readiness Framework | [`ChudiNnorukam/ai-visibility-readiness`](https://github.com/ChudiNnorukam/ai-visibility-readiness) | the 15-check tiered audit (Tier 1 SEO Foundation, Tier 2 AI Infrastructure, Tier 3 Citation Monitoring) |
| AVR Score (Answer Visibility Ratio) | [citability.dev](https://citability.dev) | the numeric product score for citation rate |
| VRC | citability.dev | the score's component axes (Visibility, Recommendability, Citability) |
| Agent Readiness | citability.dev (parallel wedge) | preparation for agent-action and agent-commerce surfaces (Stripe ACP + Google WebMCP) |

Status of this naming split: `Verified`, ratified 2026-05-02 in
[`docs/codex/nodes/naming-canonical-split.md`](./docs/codex/nodes/naming-canonical-split.md).
The upstream citability-dev `avr-naming-authority` node is still
pending its own ratification; this repo's resolution stands
independently.

## Case Study Posts

These posts document patterns from this architecture applied to a production system:

- [How I Built a 4,000-Line Production Trading Bot With Claude Code](https://chudi.dev/blog/claude-code-production-trading-bot) — context management, two-gate verification, and Claude Code in a 4,000-line live-money codebase
- [Claude Code Hooks: A Complete Tutorial](https://chudi.dev/blog/claude-code-hooks-tutorial) — the enforcement layer: pre/post-tool hooks for secret scanning, formatting, and destructive-command approval gates

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

### Off-site authority and audit chapters (`Inferred`)

These chapters document the layers the on-site pattern depends on but
does not, by itself, supply. The naming canonical split was ratified
2026-05-02; the chapters themselves remain `Inferred` until adopters
exercise them in practice (most claims are reasoned from primary
sources rather than measured against a verifiable surface).

- [The 15-Check Audit (AI Visibility Readiness)](./architecture/the-fifteen-check-audit.md)
- [Entity Authority Layer](./architecture/entity-authority-layer.md)
- [Backlinks and Off-Page Authority](./architecture/backlink-and-off-page.md)
- [Agent Readiness Layer](./architecture/agent-readiness-layer.md)

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

Dependabot keeps the GitHub Actions dependencies current, and the scheduled live audit now opens or updates an issue automatically if the public proof contract fails.

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
- `docs/codex/`: knowledge codex (nodes, domain taxonomy, INDEX.json) used by the librarian protocol to ground future audit and evolution sessions
- `docs/GLOSSARY.md`: first-pass vocabulary, including terms not yet promoted to codex nodes
- `tools/`: codex maintenance utilities (`codex_verify.py`)

## Knowledge Codex

This repository carries a structured knowledge codex at
[`docs/codex/`](./docs/codex/). It is not user-facing documentation;
it grounds the operator's librarian protocol so each future audit and
evolution session continues from the last instead of restarting at
zero.

To verify the codex locally:

```bash
python3 tools/codex_verify.py --rebuild-index
python3 tools/codex_verify.py --all
```

Drift on a `code_refs` slice is informational, not a CI failure. A
human ratifies semantic shifts before the slice is updated. See
[`docs/codex/nodes/verification-discipline.md`](./docs/codex/nodes/verification-discipline.md)
for the discipline.

## Constraint

This repository is deliberately evidence-first. It distinguishes between what is already implemented on `chudi.dev` and what appears to generalize as a reusable web pattern.

That boundary matters. The goal is technical clarity, not category hype.
