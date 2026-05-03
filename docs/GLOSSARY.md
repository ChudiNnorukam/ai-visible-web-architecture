# Glossary

First-pass vocabulary for `ai-visible-web-architecture`. Terms that have
been promoted to `docs/codex/nodes/<id>.md` are marked with an arrow.
Terms without an arrow are in active use but not yet ratified as nodes.

The librarian protocol promotes a term to a node only when a real
request surfaces it (no speculative authoring). When you find yourself
explaining the same casual term twice in a session, that is the signal
to draft a node for it.

## Promoted terms (have nodes)

- **AI-Visible Web Architecture (the pattern)** → [`avr-pattern`](codex/nodes/avr-pattern.md)
- **Surface Contract (llms.txt family + WebMCP)** → [`surface-contract`](codex/nodes/surface-contract.md)
- **Verification Discipline (evidence labels + live audit)** → [`verification-discipline`](codex/nodes/verification-discipline.md)
- **Naming Canonical Split** → [`naming-canonical-split`](codex/nodes/naming-canonical-split.md)
- **Entity and Authority Stack (the missing layer)** → [`entity-and-authority-stack`](codex/nodes/entity-and-authority-stack.md)

## Active vocabulary (not yet promoted)

The terms below appear in this repo's docs, the operator's other
codexes, or relevant external specs. Each one is a candidate for a node
when a real request surfaces it.

### Architecture and pattern

- **3-layer pattern**: alias of `avr-pattern`.
- **Conceptual system architecture**: the high-level component view
  documented in `architecture/conceptual-system-architecture.md`.
- **Verified surface architecture**: the reduced-scope view of what is
  observable today.
- **Target Operating Model**: the desired-state operating posture
  documented in `architecture/target-operating-model.md`.
- **Source-of-truth operations**: the discipline of one authority graph
  serving multiple access patterns.

### Surface contract specifics

- **llms.txt**: short-form LLM site discovery file.
- **llms-full.txt**: full-content retrieval surface.
- **ai.txt**: agent-facing crawler-policy file.
- **`.well-known/llms.json`**: structured machine-readable metadata.
- **WebMCP**: browser-side agent tool contract surface (Google + MCP
  spec).
- **Schema JSON-LD**: structured data per page (Person, Organization,
  BlogPosting, Article, BreadcrumbList).
- **sameAs graph**: schema field that links the entity across
  platforms (LinkedIn, GitHub, Medium, etc.) for AI engine entity
  resolution.
- **robots.txt AI-crawler allow-list**: explicitly permits GPTBot,
  ClaudeBot, PerplexityBot, CCBot.

### Audit and verification

- **Verification matrix**: the claim-to-proof-to-check table at
  `proof/verification-matrix.md`.
- **Live audit**: `scripts/audit_live_surfaces.py`, the runnable
  check.
- **Repo quality gate**: `scripts/check_repo_quality.py`, the local
  structural gate.
- **Verified / Inferred / Target State**: the three evidence labels
  (matches global G8 portfolio standard).
- **AVR Framework / 15-check audit**: the audit methodology in
  `github.com/ChudiNnorukam/ai-visibility-readiness`. See
  `naming-canonical-split` for the canonical resolution; the actual
  chapter is planned at
  `architecture/the-fifteen-check-audit.md`.

### Authority and entity layer

- **Entity authority**: Wikipedia, Wikidata, KG panel, sameAs graph;
  the training-data layer that LLM citation depends on.
- **Backlink authority**: referring domains, anchor diversity,
  topical relevance; the off-page ranking signal.
- **Topical authority**: depth and breadth of coverage on a single
  topic across the site.
- **Cross-link contract**: the 7 rules governing how the operator's
  public surfaces reference each other (canonical URLs on cross-posts,
  internal linking, LinkedIn behavior, GitHub author credits). See
  `~/.claude/codex/nodes/cross-link-contract.md` (global node).

### Agent commerce and readiness

- **Agent Readiness**: parallel wedge to AVR; measures whether a site
  is prepared for agents to ACT on it (recommend, transact, fulfill).
  See `naming-canonical-split` for the term's relationship to AVR.
- **ACP (Agentic Commerce Protocol)**: Stripe + OpenAI + Meta
  open standard for agentic checkout, cart, delegated payment, OAuth
  delegated authentication, orders, webhooks.
- **WebMCP (Web Model Context Protocol)**: Google's Chrome Canary
  preview that exposes `navigator.modelContext.registerTool()` for
  websites to register structured Tool Contracts.
- **MCP (Model Context Protocol)**: Anthropic-led specification for
  server-side tool contracts; complementary to WebMCP.
- **SPT (Shared Payment Token)**: Stripe scoped one-time-use payment
  credential for agentic checkout.
- **Tool Contract**: typed callable capability exposed to an agent.

### Citability product taxonomy (cross-repo)

These belong to citability-dev primarily; they appear here because the
naming canonical split spans both repos. Source-of-truth nodes live in
`~/Projects/citability-dev/docs/codex/nodes/`.

- **AVR Score**: citability.dev's product score (a 0-100 number
  rolling up V/R/C across LLM engines). The acronym AVR expands to
  "AI Visibility Readiness" (the framework). The score itself takes
  no separate canonical expansion: a prior "Answer Visibility Ratio"
  backronym was repudiated 2026-05-02. See `naming-canonical-split`.
- **VRC (Visibility, Recommendability, Citability)**: the score's
  component axes.
- **vScore**: citability's citation rate measurement.
- **rScore**: citability's readability axis.
- **cScore**: citability's content axis.
