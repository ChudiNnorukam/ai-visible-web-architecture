---
id: entity-and-authority-stack
name: Entity and Authority Stack (the missing layer)
domain: evolution-strategy
aliases:
  - entity-and-authority-stack
  - entity-authority
  - authority-layer
  - the-moat
  - off-page-authority
  - training-data-presence
  - kg-panel
  - wikidata-wikipedia
  - sameAs-graph
related:
  - avr-pattern
  - surface-contract
  - verification-discipline
  - naming-canonical-split
parent_concepts: []
child_concepts: []
code_refs: []
last_verified: null
confidence: inferred
---

## What

The off-site authority layer the AI-Visible Web Architecture pattern is
currently missing. This node names what gets added in the planned
evolution chapters (entity-authority-layer, backlink-and-off-page,
the-fifteen-check-audit, agent-readiness-layer) and explains why each is
load-bearing.

### What the existing pattern already covers (the on-site half)

The 3-layer pattern (`avr-pattern`) covers:

- Retrieval-aware information design (on-site).
- Machine-readable identity and discovery (`surface-contract`,
  on-site).
- Agent-facing interface surfaces (on-site WebMCP).

This is the half of AI visibility under operator direct control.

### What the pattern does NOT yet cover (the off-site half)

LLMs do not assemble citations from on-site signals alone. They draw on:

1. **Training-data presence.** What was in Common Crawl, Wikipedia,
   Wikidata, GitHub READMEs, Reddit, Hacker News, podcast transcripts
   when the model was trained. An unknown brand has weak prior weight
   regardless of on-site optimization. (Source: global
   `entity-authority` node.)

2. **Knowledge Graph + Wikipedia + Wikidata.** Every major LLM was
   trained on Wikipedia. Being the subject of a Wikipedia article is
   "canonical existence" to the model. Wikidata is an easier on-ramp
   (no notability test for organizations).

3. **Schema sameAs + reciprocal social graph.** Person and Organization
   schema with `sameAs` linking to LinkedIn, GitHub, Medium, Dev.to,
   YouTube, Twitter. Each platform mutually links back. Divergence
   invites AI engines to pick a canonical and ignore others. (Source:
   chudi-blog `entity-graph` node.)

4. **Backlinks (referring domains).** Still the strongest off-page
   signal a quarter-century after PageRank. Counts what matters:
   distinct referring domains > raw backlink count, topical relevance >
   raw DR, anchor diversity (branded + URL > exact-match), in-content
   placement > footer. (Source: global `backlink-authority` node.)

5. **Citation evidence (live LLM probing).** What models actually cite
   when asked about your topic. Measured by citability.dev's vScore
   pipeline across N engines. Differentiates "we were not retrieved"
   from "we were retrieved but not cited" (entity-authority gap is
   typically the latter). (Source: citability-dev `v-score` node.)

6. **Agent-action readiness.** A new layer that sits parallel to
   visibility, not under it. Agent commerce (Stripe ACP) + agent action
   surfaces (Google WebMCP) shifted in Apr 2026 from "interesting" to
   "table stakes for the next agent-purchase loop." (Source: global
   `agent-readiness-market-shift` node + citability-dev
   `agent-readiness-wedge` node.)

### Counter-intuitive findings the chapters should surface

From the AI Visibility Readiness Framework v1 sample (citability
`avr-framework` node):

- **Domain Authority does NOT predict AI readiness.** chudi.dev
  (DA approximately 5) scores AI-READY; reddit.com and x.com (DA 99)
  score NOT-READY because they block AI crawlers and serve heavy CSR.
- **Ahrefs.com has approximately 100 percent visibility but
  approximately 5 percent citation rate.** Crawlable is the floor;
  entity authority + answer-first structure are what convert visibility
  into citation.
- **Approximately 85 percent of sites lack AI-readable surfaces.** Most
  public sites fail Tier 2 even when Tier 1 is clean.
- **Audit cost at scale is approximately $3.20 per site.** Driven by
  Tier 3 LLM queries; Tier 1 + Tier 2 are cache-friendly static checks.

### The April 16 2026 finding (operator gate)

This repo's evolution must respect the operator's April 16 2026
CONDITIONAL gate decision: the real moats are backlinks + Bing index
coverage + measurement, NOT more iteration on llms.txt-style on-site
surfaces. Adding more surface-contract chapters without addressing
off-page authority is doing the easy half of the work. The planned
chapters (entity-authority + backlinks + agent-readiness +
AVR audit) are the hard half.

### What chapters this node motivates

The four planned architecture chapters that consume this node:

1. `architecture/the-fifteen-check-audit.md`: Tier 1 / Tier 2 / Tier 3
   discipline + discrete status output.
2. `architecture/entity-authority-layer.md`: Wikipedia / Wikidata /
   sameAs / KG, training-data presence, original-research as
   primary-source signal.
3. `architecture/backlink-and-off-page.md`: referring domains, anchor
   diversity, link velocity, training-data weighting, what does not
   work (PBNs, comment spam).
4. `architecture/agent-readiness-layer.md`: ACP + WebMCP catalyst, the
   6-module readiness audit, positioning relative to AVR measurement.

Each chapter is `target` until shipped and ratified.

## Where

This node has no code anchors. It catalogs what to ADD. References live
in other repos' codexes:

- `~/.claude/codex/nodes/entity-authority.md`: global entity-stack
  reference (Wikipedia, Wikidata, KG, sameAs, podcast circuit, original
  research).
- `~/.claude/codex/nodes/backlink-authority.md`: global referring
  domains, anchor profile, what works and what does not.
- `~/.claude/codex/nodes/agent-readiness-market-shift.md`: global
  catalyst node (Stripe ACP + Google WebMCP, Apr 2026).
- `~/.claude/codex/nodes/cross-link-contract.md`: global 7 rules for
  the operator's surfaces.
- `citability-dev/docs/codex/nodes/avr-framework.md`: AVR check list (CHECKS.md).
- `citability-dev/docs/codex/nodes/agent-readiness-wedge.md`: 6-module
  audit.
- `citability-dev/docs/codex/nodes/entity-authority.md`: citability
  product mirror of the global node.
- `citability-dev/docs/codex/nodes/backlink-authority.md`: citability
  product mirror.
- `chudi-blog/docs/codex/nodes/entity-graph.md`: chudi.dev's actual
  entity-graph implementation.
- `chudi-blog/docs/codex/nodes/llms-surfaces.md`: chudi.dev's surface
  implementation.

External primary sources (for the chapters that get drafted):

- Wikipedia notability for organizations: WP:GNG, WP:ORG.
- schema.org Organization + Person types with sameAs.
- Stripe Agentic Commerce Protocol:
  <https://docs.stripe.com/agentic-commerce/acp>.
- Google WebMCP preview:
  <https://searchengineland.com/google-releases-preview-of-webmcp-how-ai-agents-interact-with-websites-469024>.

## When-to-touch

Route here when the user says:

- "what's missing from the framework"
- "the moat", "off-page", "entity authority"
- "how do LLMs actually pick what to cite"
- "should we add a backlink layer / entity layer / agent-readiness
  layer"
- "what's next for the architecture"
- "why doesn't the pattern address Wikipedia / Wikidata / sameAs"

Do NOT route here for the existing 3-layer pattern (route to
`avr-pattern`) or for surface contract questions (route to
`surface-contract`). This node is for the EVOLUTION direction.

## Refresh policy

Re-verify after:

- Each of the four planned chapters ships (drop the corresponding
  bullet from "What chapters this node motivates").
- Operator override of the priority order (e.g., agent-readiness
  before entity-authority).
- Any change to global `entity-authority`, `backlink-authority`, or
  `agent-readiness-market-shift` nodes.
- Quarterly check that the operator's April 16 2026 CONDITIONAL gate
  finding (backlinks + Bing + measurement as the moat) is still the
  operative read.

Next refresh: on first chapter shipping, OR 2026-08-01.
