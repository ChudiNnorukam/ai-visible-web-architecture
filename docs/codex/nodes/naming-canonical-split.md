---
id: naming-canonical-split
name: Naming Canonical Split (AI-Visible Web Architecture vs AVR Score vs AI Visibility Readiness)
domain: evolution-strategy
aliases:
  - naming-canonical-split
  - avr-naming
  - naming-conflict
  - framework-vs-score
  - avr-vs-architecture
  - vrc-naming
  - the-naming
related:
  - avr-pattern
  - entity-and-authority-stack
parent_concepts: []
child_concepts: []
code_refs: []
last_verified: null
confidence: inferred
---

## What

The portfolio-wide naming conflict around the acronym "AVR" and the
canonical resolution this repo proposes to adopt. Three referents share
the acronym today:

| Term | Where it lives | What it means |
|---|---|---|
| **AI-Visible Web Architecture** | This repo (`ai-visible-web-architecture`) | The reusable 3-layer pattern (info design + identity + agent interface). Sometimes referred to colloquially as "AVR pattern" or "AVR framework" by the operator. |
| **AI Visibility Readiness Framework** | `github.com/ChudiNnorukam/ai-visibility-readiness` (separate repo) + citability-dev `lib/avr-status.ts` | The 15-check tiered audit (Tier 1 SEO Foundation / Tier 2 AI Infrastructure / Tier 3 Citation Monitoring) with discrete status (AI-READY / INFRASTRUCTURE-READY / FOUNDATION-READY / NOT-READY). Documented in citability-dev's `avr-framework` node. |
| **AVR Score (Answer Visibility Ratio)** | citability.dev `public/.well-known/citability.json` | The numeric score in citability.dev's product summarizing observed visibility, recommendability, citability across LLM engines. |
| **VRC** | citability.dev product UI + receipts | The component breakdown (Visibility, Recommendability, Citability) underlying the AVR Score. |
| **Agent Readiness** | citability-dev `agent-readiness-wedge` node | A parallel product wedge separate from AVR. Measures agent-action / agent-commerce readiness (Stripe ACP + Google WebMCP). NOT a sub-component of AVR. |

### The proposed canonical resolution

Source: citability-dev `avr-naming-authority.md` (2026-04-30, INFERRED,
pending operator ratification). This repo adopts that resolution for the
public reference doc:

1. **"AI-Visible Web Architecture"**: the framework name for the
   reusable 3-layer web pattern this repo describes. NOT abbreviated to
   "AVR" in any public surface here, to avoid acronym collision.
2. **"AI Visibility Readiness Framework"**: the 15-check audit
   methodology. Lives in the separate `ai-visibility-readiness` repo.
   This repo references it but does not redefine it.
3. **"AVR Score"**: citability.dev's product score (Answer Visibility
   Ratio). When this repo cites the score, it uses the full term to
   avoid confusion with framework references.
4. **"VRC"**: citability.dev's component axis (Visibility,
   Recommendability, Citability). Used only in citability-dev product
   contexts.
5. **"Agent Readiness"**: the parallel wedge (agent-action +
   agent-commerce + payment-readiness). Documented in this repo's
   future agent-readiness chapter, separate from AVR.

### Why this matters

- AI engines extract definitions from llms.txt and `.well-known/`
  surfaces. If the same operator's domain returns one definition and a
  related domain returns another, the engine picks one (often
  inconsistently across queries) and brand semantic precision degrades.
- Buyer confusion: a sales conversation that says "AVR is our framework"
  while the dashboard shows "AVR Score: 73" creates trust friction.
- Backlinks earned by this public reference doc accrue to "AI-Visible
  Web Architecture" semantics; if the operator later overrides the
  resolution and renames either side, those backlinks become stale.

### Ratification gate (load-bearing)

This node is `inferred` until the operator ratifies the canonical split.
Per the 2026-05-01 audit red-team outcome, the publication step (git
push / PR open) for this repo's evolution is gated on operator first
ratifying the resolution either:

(a) here in writing (flip this node's `confidence: inferred → verified`
and add `ratified: <date>`), OR

(b) over in citability-dev (ratify
`citability-dev/docs/codex/nodes/avr-naming-authority.md` first; this
repo then defers to that ratification).

Path (a) and (b) are equivalent in outcome. Operator picks the order.

### Override path

If operator overrides the resolution (e.g., "AVR stays the framework
across the board, the score gets renamed"), this node updates to the
new canonical names AND triggers a re-write pass on:

- This repo's README + whitepaper + new architecture chapters.
- citability-dev's `public/llms.txt`, `public/.well-known/citability.json`,
  `app/docs/page.tsx` methodology page.
- chudi-blog's surfaces if any reference AVR by acronym.

The cost of the override is the same regardless of when it happens, but
the cost of unratified public publication is asymmetric: a backlink
earned under one canonical name does not transfer cleanly to a
renamed concept.

## Where

This node has no code anchors. It is a strategy / governance node that
references external authorities:

- `citability-dev/docs/codex/nodes/avr-naming-authority.md`: the
  upstream resolution this node mirrors. Source of truth for citability
  product taxonomy.
- `citability-dev/public/llms.txt:1-50`: surface that calls AVR the
  "AI Visibility Readiness Framework."
- `citability-dev/public/.well-known/citability.json:1-100`: surface
  that defines AVR as "Answer Visibility Ratio."
- `github.com/ChudiNnorukam/ai-visibility-readiness/FRAMEWORK.md`:
  the canonical 15-check spec the framework name refers to.

## When-to-touch

Route here when the user says:

- "what does AVR mean", "AVR vs framework", "naming conflict"
- "are we calling this the framework or the score"
- "AVR pattern vs AVR audit"
- "is this the same as citability's AVR"
- "rename / re-acronym"
- "VRC", "Agent Readiness vs AVR"

Do NOT route here for purely product-side citability naming questions
(those route to citability-dev's `avr-naming-authority` node directly).

## Refresh policy

Re-verify after:

- Operator ratifies (or overrides) the canonical split.
- Any rename of AVR-related copy in this repo's README, whitepaper, or
  architecture chapters.
- Any change to citability-dev's `avr-naming-authority.md` resolution.
- Quarterly check: search this repo's docs for the literal string "AVR"
  and confirm each occurrence resolves to one of the five canonical
  meanings without ambiguity.

Next refresh: on operator ratification, OR 2026-08-01 (whichever
sooner).
