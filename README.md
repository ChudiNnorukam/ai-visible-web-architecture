# AI-Visible Web Architecture

Public reference architecture for building AI-visible websites, using [chudi.dev](https://chudi.dev) as the live case study.

This repository documents how one public site is designed to work across three access modes at once:

- human reading
- LLM retrieval and citation
- AI agent interaction

## Project Thesis and Verified Scope

**Pattern version:** `v1.0.0` (2026-05-06). The 3-layer pattern with
agent wayfinding made explicit in Layer 3. Versioned in
[`docs/codex/nodes/avr-pattern.md`](./docs/codex/nodes/avr-pattern.md)
frontmatter; v2.0.0 will land when the off-site authority chapter
exits `Inferred` and absorbs into the pattern as Layer 4.

This repository documents the architecture pattern that makes a website
maximally cite-worthy by AI search engines and natively callable by AI
agents. It is a reference doc, not the execution.

**The goal** (`Target`): make any website the AI engines' first-pick
citation source, clearly readable and retrievable, trusted, and
natively agentic.

**The verified scope** (`Verified`): the three on-site layers
documented here are exercised by [chudi.dev](https://chudi.dev) as the
live case study. Public EntityMap, crawler-policy, telemetry,
cross-property, citation-receipt, and agent-action surfaces now also exercise
parts of the surrounding operating architecture. The four off-site and audit chapters
([AVR audit](./architecture/the-fifteen-check-audit.md),
[entity authority](./architecture/entity-authority-layer.md),
[backlinks and off-page](./architecture/backlink-and-off-page.md),
[agent readiness](./architecture/agent-readiness-layer.md)) are
assigned claim-level evidence labels: public behavior is `Verified`; causal
ranking claims and unimplemented adopter guidance remain `Inferred`.

**Two corrections to the goal worth surfacing** so adopters do not
over-claim:

1. **WebMCP is positioning, not a citation-ranking signal.** Per the
   [W3C Web Machine Learning CG draft](https://webmachinelearning.github.io/webmcp/),
   `navigator.modelContext` is a Community Group Draft, not a
   Standards-Track document. No documented crawler indexes
   `registerTool` declarations today. Production browser support is
   Chrome 146+ Canary behind a flag; realistic broad availability is
   2027+. WebMCP belongs in the agent-action surface (post-citation
   commerce and interaction), not in the AI-citation pipeline.
2. **The real moats live off-site.** A 2026-04-16 calibration
   (recorded in
   [`entity-and-authority-stack`](./docs/codex/nodes/entity-and-authority-stack.md))
   found that referring domains, Bing index coverage, and citation
   measurement are the load-bearing levers for actually being cited,
   not more iteration on `llms.txt`-style on-site surfaces. The
   on-site work documented here is necessary but not sufficient.

**Where execution actually happens.** Adopters chasing the goal will
do most of the leveraged work outside this repo:

- the adopter's own site content, surfaces, and entity graph (the
  live case study here is chudi.dev);
- the adopter's off-site authority footprint (Wikipedia and Wikidata,
  GitHub, LinkedIn, Medium with reciprocal `sameAs` and canonical
  links);
- a measurement pipeline ([citability.dev](https://citability.dev) is
  one productized audit that consumes the AVR framework).

This repo's own job is to make the **pattern** clearly cite-worthy as
a reference, not to ship the moat for any specific site.

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
repository. Across the operator's portfolio, the acronym "AVR"
canonically expands to **"AI Visibility Readiness"**: the audit
framework hosted at
[`ChudiNnorukam/ai-visibility-readiness`](https://github.com/ChudiNnorukam/ai-visibility-readiness)
and consumed by [citability.dev](https://citability.dev). The
acronym does NOT expand to anything else in this portfolio.

| Term | Where it lives | What it is |
|---|---|---|
| AVR (acronym) | across the portfolio | "AI Visibility Readiness" (the framework name) |
| AI-Visible Web Architecture | this repo | the 3-layer pattern (this document) |
| AI Visibility Readiness Framework | [`ChudiNnorukam/ai-visibility-readiness`](https://github.com/ChudiNnorukam/ai-visibility-readiness) | the tiered audit (Tier 1 SEO Foundation, Tier 2 AI Infrastructure, Tier 3 Citation Monitoring); the check list is generated at [`CHECKS.md`](https://github.com/ChudiNnorukam/ai-visibility-readiness/blob/main/CHECKS.md) |
| AVR Score | [citability.dev](https://citability.dev) | the framework's 0-100 numeric output rolling up V/R/C across LLM engines |
| VRC | citability.dev | the score's component axes (Visibility, Recommendability, Citability) |
| Agent Readiness | citability.dev (parallel wedge) | preparation for agent-action and agent-commerce surfaces (Stripe ACP + Google WebMCP) |

Status of this naming split: `Inferred`, pending re-ratification.
A prior 2026-05-02 ratification mapped the score's name to "Answer
Visibility Ratio"; that mapping was repudiated by the operator
(the phrase originated in an LLM-coined backronym that crept into
[citability.dev's `.well-known/citability.json`](https://citability.dev/.well-known/citability.json)
and contradicts the same site's FAQ). The corrected canonical
mapping above lands `Inferred` until the operator reads the
rewritten
[`docs/codex/nodes/naming-canonical-split.md`](./docs/codex/nodes/naming-canonical-split.md)
node and ratifies. A parallel pull request in `citability-dev`
removes the "Answer Visibility Ratio" expansion from the live trust
surfaces.

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

- [Portfolio Repository Map](./architecture/portfolio-repository-map.md) — canonical ownership, consolidation, and retirement map

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
does not, by itself, supply. They remain `Inferred` until adopters
exercise them in practice (most claims are reasoned from primary
sources rather than measured against a verifiable surface).

- [The AVR Audit (AI Visibility Readiness)](./architecture/the-fifteen-check-audit.md)
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
