# Agent Readiness Layer

> Evidence boundary: this chapter documents the parallel layer that
> sits alongside (not under) AI visibility. Agent readiness asks
> whether a website is prepared for agents to ACT on it, not just
> read it. Most claims are `Inferred` from primary specifications
> (Stripe ACP, Anthropic MCP, Google WebMCP preview) plus the April
> 2026 catalyst documented in the operator's global codex node
> `agent-readiness-market-shift`. Chapter status: `Inferred`.

## Why a Parallel Layer, Not a Sub-Component

The 3-layer pattern and the entity-authority layer document AI
**visibility**: can systems find, retrieve, and cite the site? Agent
readiness documents AI **action**: can systems act on the site
safely once they have decided to? These are categorically different
questions. Bundling them under one score hides the distinction.

Two market signals shipped in Q2 2026 that made this distinction
load-bearing:

### Signal 1: Stripe agent commerce (April 2026)

Stripe shipped Link wallet access for agents through OAuth-delegated
approval, scoped one-time-use cards, and Shared Payment Tokens. The
Agentic Commerce Protocol (ACP) is co-developed with OpenAI and Meta
and defines an open standard for agentic checkout, cart and feed
exchange, delegated payment, OAuth delegated authentication, orders,
and webhooks.

Shifts agents from "research assistants" (read web, summarize) to
"purchasing actors" (read web, recommend, transact).

### Signal 2: Google WebMCP preview (April 2026)

Chrome Canary exposes `navigator.modelContext.registerTool()` so
websites can register structured Tool Contracts that agents invoke
directly from the browser. The contracts are JSON Schema typed,
client-side, and complementary to MCP (which is server-side). Search
Engine Land and VentureBeat coverage confirms this is the path
Google is signaling for "websites as callable surfaces, not just
crawlable surfaces."

### Why the two together create a category

Without ACP, WebMCP is a developer experiment with no commercial
pressure to adopt. Without WebMCP, ACP is a payment innovation with
no surface for agents to invoke. Together: agents can READ websites
(existing AI search), DECIDE based on Tool Contracts (WebMCP), and
ACT including PAYING (ACP). The full purchasing loop closes. The
adopter surface that prepares a site for that loop is what this
chapter calls "agent readiness."

## What This Layer Does NOT Replace

It does not replace:

- The 3-layer pattern (info design, surface contract, agent
  interface).
- Entity authority work (training-data presence, KG, Wikipedia).
- Backlink and off-page authority work.
- Citation measurement.

It composes on top of them. A site with zero entity authority cannot
get into an agent's recommendation set in the first place; agent
readiness is about what the site exposes once it has earned that
position.

## The Six-Module Audit

Adopted from citability-dev's `agent-readiness-wedge` codex node.
Each module asks one question that an agent (or its operator) needs
answered before they trust the site to act on:

| Module | Question it answers | What gets checked |
|---|---|---|
| AI discovery | Can AI systems identify the brand, offers, pricing, policies? | Visibility and recommendability findings (overlaps with the AVR audit). |
| Citation evidence | Do AI systems cite the site or third-party sources for buyer questions? | Citation receipts and source-gap analysis. |
| Structured commerce data | Are product, offer, pricing, FAQ, policy, organization schema clear? | Schema remediation backlog. |
| Agent actionability | Are forms, routes, tasks exposed in a tool-like way? | WebMCP, OpenAPI, MCP readiness score. |
| Payment readiness | Can future agent flows request scoped payment credentials safely? | ACP and Stripe Link readiness checklist. |
| Test harness | Can an agent simulate search, comparison, cart or request, approval, and receipt flows end-to-end? | Agent-flow simulation scenarios. |

Modules 1 and 2 overlap with the visibility-side AVR audit. Modules
3 through 6 are unique to the agent-readiness layer.

## Positioning Relative to AVR

Two distinct buying moments:

- **AVR** (the AI Visibility Readiness Framework, citability.dev's
  audit): "Can AI systems find, recommend, and cite this site NOW?"
  Measurement.
- **Agent Readiness**: "Can AI agents act on this site SAFELY when
  agentic checkout becomes table stakes?" Preparation.

They share infrastructure (receipts, methodology, evidence tiers)
but target different stages of the buyer's relationship with AI. An
adopter can be AVR-strong and agent-readiness-weak (cited but not
callable), agent-readiness-strong and AVR-weak (callable but rarely
chosen), or both (the goal).

## What Adopters Can Ship Today

For early adopters, the agent-readiness layer is mostly
specification-following. Concrete steps in order of leverage:

### 1. Publish a structured agent-action surface

citability.dev exposes `/.well-known/agent-actions` listing the
WebMCP tools, their JSON Schema, and the actions they support. This
is the minimum-viable agent-readable manifest. The pattern's
existing surface contract chapter is the right home for documenting
this surface formally; today the contract specifies WebMCP browser
tools without a versioned manifest.

### 2. Adopt ACP-compatible commerce schemas

`Product`, `Offer`, `Price`, `Brand`, `FAQPage`, `WebSite`,
`Organization` schema with consistent IDs and `sameAs` links. ACP
agents read these to populate carts and confirm pricing.

### 3. Document scoped payment delegation paths

Even sites that do not yet support ACP can document where scoped
payment would be accepted. Stripe Link's OAuth-delegated approval is
the current standard. Adopters should plan for the integration even
if they do not ship it on day one.

### 4. Build agent simulation scenarios

End-to-end "agent searches my category, compares two options,
recommends mine, requests delegated payment, completes the order,
sends a receipt." These scenarios become regression tests for the
adopter's agent surface. Today they are mostly pen-and-paper. They
are worth writing down as the layer matures.

### 5. Ratify a stable identity for agents to address

Agents need a stable canonical the adopter's brand resolves to. The
entity-authority layer provides this. The agent-readiness layer
consumes it: schema `Organization` plus `sameAs` plus an in-policy
contact path. Without this, an agent has no way to confirm it is
calling the right site.

## What This Layer Does Not Cover

- **Per-agent compatibility detail** (does ChatGPT's agent prefer
  Tool Contract A over schema B?): too volatile to encode in the
  pattern. Track citability.dev's audit pipeline outputs and the
  global codex node `agent-readiness-market-shift` for the current
  state.
- **Agent identity verification on the adopter's side** (how the
  adopter authenticates that the caller is the agent it claims to
  be): work for the agent-action surface chapter and standards
  bodies, not architecture.
- **Liability and legal posture for agentic commerce**: out of scope
  for an architecture pattern; ACP defines the technical contract
  and adopters layer their own legal terms on top.

## Verification Hooks (Target State)

None of the agent-readiness checks are in
`scripts/audit_live_surfaces.py` today. Candidates for the next
extension:

- `/.well-known/agent-actions` presence and JSON Schema validity.
- Schema `Product`, `Offer`, `Brand` presence on commerce pages (if
  applicable).
- ACP webhook endpoint presence and 200-or-401 response shape.
- WebMCP Tool Contract registration presence in adopter's site
  source (heuristic check).

These are documented in
`docs/codex/nodes/verification-discipline.md` under "What the matrix
does NOT yet verify."

## When to Adopt This Layer

The agent-readiness layer is appropriate when:

- The adopter has commerce or transaction surfaces, even thin ones
  (consultation booking, paid downloads, scheduling).
- The adopter is in a category where buyers are likely to use AI
  agents to research and recommend (services, software, consumer
  goods, professional services).
- The adopter has stabilized the visibility-side layers (the
  3-layer pattern plus entity authority plus backlinks). Otherwise
  agent readiness is preparing for traffic that will not arrive.

It is NOT appropriate when:

- The adopter has zero entity authority and zero citation rate. Fix
  the visibility layers first; agents have nothing to call yet.
- The adopter's commerce surfaces are unbuilt. Agent readiness
  cannot manifest payment and order schemas if there is no payment
  or order to schema.
- The adopter is a personal site or portfolio with no transactional
  surface. The visibility layers and the surface contract are
  enough.

## References

- This repo's `docs/codex/nodes/naming-canonical-split.md`:
  positions Agent Readiness as a parallel wedge, not a sub-component
  of AVR.
- This repo's `docs/codex/nodes/entity-and-authority-stack.md`:
  upstream layer the agent-readiness layer depends on.
- Operator's global codex node `agent-readiness-market-shift`: the
  catalyst node, including primary-source URLs for the April 2026
  Stripe ACP and Google WebMCP launches.
- citability-dev codex node `agent-readiness-wedge`: the 6-module
  audit shape and product-positioning rationale.
- citability-dev codex node `agent-action-surface`: implementation
  notes for `/.well-known/agent-actions`.
- Stripe Agentic Commerce Protocol:
  <https://docs.stripe.com/agentic-commerce/acp>.
- Stripe Link wallet for agents:
  <https://stripe.com/blog/giving-agents-the-ability-to-pay>.
- Google WebMCP preview coverage:
  <https://searchengineland.com/google-releases-preview-of-webmcp-how-ai-agents-interact-with-websites-469024>
  and
  <https://venturebeat.com/infrastructure/google-chrome-ships-webmcp-in-early-preview-turning-every-website-into-a>.
- Anthropic Model Context Protocol announcement and specification:
  <https://www.anthropic.com/news/model-context-protocol> and
  <https://modelcontextprotocol.io/specification/2025-03-26>.
