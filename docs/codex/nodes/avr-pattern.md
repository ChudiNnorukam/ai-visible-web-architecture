---
id: avr-pattern
name: AI-Visible Web Architecture Pattern (the 3-layer model)
domain: pattern-architecture
aliases: [avr-pattern, ai-visible-web-architecture, 3-layer-pattern, three-layer-pattern, retrieval-aware-info-design, the-pattern, the-framework]
code_refs:
  - path: whitepaper/the-ai-visible-personal-website.md
    lines: 1-48
    sha256: bc2b0be4b515aef9a98127c8f6e8719e1fea0dddfa44f515ead4bd636cdee22b
  - path: architecture/conceptual-system-architecture.md
    lines: 1-32
    sha256: c29b8efa7c1c725db8f01035f1449fc74557d1c8b06e3b5aadd88db452f2d0b9
  - path: architecture/verified-surface-architecture.md
    lines: 1-36
    sha256: fc64a8feb17e4ad39509bd027bccbd530b82ca029a5bcc4d8b15758248004597
  - path: architecture/retrieval-and-citation-flow.md
    lines: 1-27
    sha256: 3728dfb3806b51534d8ace3144327d3a74e376316ba0769f65423b5bced9801c
  - path: architecture/agent-interface-layer.md
    lines: 1-26
    sha256: 721ba96b815ef4ec8055e951681a7f3673e315f558c28667cad6cd21fc7e245e
related: [surface-contract, verification-discipline, naming-canonical-split, entity-and-authority-stack]
parent_concepts: []
child_concepts: []
last_verified: 2026-05-02
confidence: inferred
---

## What

The reusable architecture pattern this repository documents. A traditional
personal website is optimized for human browsing alone. The AI-visible web
architecture pattern is optimized for three simultaneous modes off one
authority graph:

1. **Human reading** (the visible site, navigation, narrative).
2. **LLM retrieval and citation** (machine-readable surfaces and answer-shaped
   content for crawlers like GPTBot, ClaudeBot, PerplexityBot, CCBot).
3. **AI agent interaction** (callable tool contracts via WebMCP and related
   surfaces).

The point is not to replace the visible site. It is to let one source of
truth serve all three access patterns so the layers stay coherent. When
they diverge, the public artifact becomes inconsistent and AI systems pick
canonicals that may not match operator intent.

### The three architectural layers

1. **Retrieval-aware information design.** Topic hubs, answer-first intros,
   passage-chunkable structure, deliberate URL hierarchy. Content shape
   matches how retrieval systems segment pages.
2. **Machine-readable identity and discovery.** llms.txt family, ai.txt,
   `.well-known/llms.json`, schema JSON-LD (Person / Organization /
   BlogPosting / Article), sitemap.xml. See `surface-contract`.
3. **Agent-facing interface surfaces.** Documented WebMCP browser tools that
   expose typed capabilities directly from the site so agents do not have
   to screen-scrape.

### What this pattern is NOT

It is not a substitute for entity authority (Wikipedia, Wikidata, KG panel),
backlinks, or topical depth. The pattern handles the on-site half of AI
visibility. The off-site half (training-data presence, referring domains,
citation evidence) is described in the evolution-strategy domain (see
`entity-and-authority-stack`) and is being added to the architecture in a
later chapter.

### Naming context

This repository's framework name is "AI-Visible Web Architecture." It is
NOT the same thing as citability-dev's "AVR Score" (Answer Visibility
Ratio) or the "AI Visibility Readiness Framework" 15-check audit hosted at
`github.com/ChudiNnorukam/ai-visibility-readiness`. See
`naming-canonical-split` for the canonical resolution across surfaces.

## Where

Anchor docs in this repo (the pattern as currently published):

- `whitepaper/the-ai-visible-personal-website.md`: short-form summary of
  the 3-layer pattern, with chudi.dev as the live case study.
- `architecture/conceptual-system-architecture.md`: high-level component
  view.
- `architecture/verified-surface-architecture.md`: verified-only view of
  what the live site exposes today.
- `architecture/retrieval-and-citation-flow.md`: flow doc for how content
  reaches LLM retrieval.
- `architecture/agent-interface-layer.md`: flow doc for the agent surface.

External grounding (other repos in the operator's portfolio):

- `chudi-blog/docs/codex/nodes/llms-surfaces.md`: chudi.dev's actual
  implementation of the surface contract.
- `chudi-blog/docs/codex/nodes/entity-graph.md`: chudi.dev's entity layer
  (Person + Organization + sameAs).
- `citability-dev/docs/codex/nodes/avr-framework.md`: the 15-check audit
  spec this pattern's verification layer aligns with.

## When-to-touch

Route here when the user says any of:

- "the AVR framework", "the architecture", "the 3-layer pattern"
- "what does this repo describe"
- "is the pattern still current"
- "should we add a layer / split a layer"
- "what's the difference between the AVR pattern and citability's AVR"
- "evolve the framework"
- "how does the live site map to the pattern"

Do NOT route here when the request is about a specific surface file
(`llms.txt`, `.well-known/llms.json`): that's `surface-contract`.
Do NOT route here when the request is about audit or evidence claims:
that's `verification-discipline`.

## Refresh policy

Re-verify after:

- Any whitepaper or core architecture doc rewrite.
- Any surface contract change that breaks the 3-layer composition (e.g.,
  retiring WebMCP or replacing the llms.txt family).
- Operator override of the layer count or definitions.
- Quarterly check of whether the pattern has absorbed the planned
  evolution chapters (entity-authority, backlinks, agent-readiness,
  15-check audit). When all four chapters are committed and ratified,
  the pattern grows from 3 layers to 4 (the off-site / authority layer).

Next refresh: 2026-08-01, or sooner on any whitepaper rewrite.
