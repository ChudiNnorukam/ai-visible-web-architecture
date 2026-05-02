---
id: naming-canonical-split
name: Naming Canonical Split (AVR vs AI-Visible Web Architecture vs AI Visibility Readiness)
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
last_verified: 2026-05-02
confidence: inferred
---

## What

The portfolio-wide naming conflict around the acronym "AVR" and the
canonical resolution this repo proposes to adopt.

The acronym AVR canonically expands to **"AI Visibility Readiness"**:
the audit framework hosted at
`github.com/ChudiNnorukam/ai-visibility-readiness` and consumed by
citability.dev as the framework that produces the AVR Score. The
acronym does NOT expand to anything else in this portfolio. In
particular, the score is just "the AVR Score" with no separate
canonical expansion.

| Term | Where it lives | What it means |
|---|---|---|
| **AVR (acronym)** | across the portfolio | "AI Visibility Readiness" (the framework name). Used consistently by chudi.dev (`docs/GLOSSARY.md`, blog posts) and citability.dev (FAQ structured data, `app/page.tsx`). |
| **AI-Visible Web Architecture** | This repo (`ai-visible-web-architecture`) | The reusable 3-layer pattern (info design + identity + agent interface). NOT abbreviated to "AVR" anywhere here. |
| **AI Visibility Readiness Framework** | `github.com/ChudiNnorukam/ai-visibility-readiness` (separate repo) + citability-dev `lib/avr-status.ts` | The 15-check tiered audit (Tier 1 SEO Foundation / Tier 2 AI Infrastructure / Tier 3 Citation Monitoring) with discrete status (AI-READY / INFRASTRUCTURE-READY / FOUNDATION-READY / NOT-READY). Documented in citability-dev's `avr-framework` node. |
| **AVR Score** | citability.dev `public/.well-known/citability.json` + `app/docs/page.tsx` | The framework's 0-100 numeric output, rolling up Visibility, Recommendability, Citability across LLM engines. Takes no separate canonical expansion: it is "the AVR Score" or, when contextually clear, "the score." |
| **VRC** | citability.dev product UI + receipts | The component breakdown (Visibility, Recommendability, Citability) underlying the AVR Score. |
| **Agent Readiness** | citability-dev `agent-readiness-wedge` node | A parallel product wedge separate from AVR. Measures agent-action / agent-commerce readiness (Stripe ACP + Google WebMCP). NOT a sub-component of AVR. |

### What this canon explicitly DOES NOT include

The phrase **"Answer Visibility Ratio"** is repudiated. It was an
LLM-coined backronym that appeared in citability.dev's
`public/.well-known/citability.json` (and propagated to
`app/docs/page.tsx`, `public/llms.txt`, and a small number of blog
posts) as if it were the canonical expansion of "AVR." It is not
operator-authored, contradicts citability.dev's own FAQ structured
data (which states "the score is spelled out as Answer Visibility
Ratio" while elsewhere asserting "AVR is the AI Visibility Readiness
Framework"), and conflicts with the consistent use of AVR =
"AI Visibility Readiness" on chudi.dev and in the public
`ai-visibility-readiness` repo.

A parallel pull request in `citability-dev` removes the phrase from
`.well-known/citability.json`, `app/docs/page.tsx`, the FAQ
structured data on `app/page.tsx`, and `public/llms.txt`. Past
content (blog posts) that uses the phrase is a follow-up sweep, not
in scope for this resolution.

### The canonical resolution (`Inferred`)

1. **"AVR" (the acronym)**: expands to "AI Visibility Readiness" only.
   Used as the framework's name across the portfolio. NOT used to
   refer to the score in isolation.
2. **"AI-Visible Web Architecture"**: the framework name for the
   reusable 3-layer web pattern this repo describes. NOT abbreviated
   to "AVR" in any public surface here, to avoid acronym collision
   with the framework above.
3. **"AI Visibility Readiness Framework"**: the 15-check audit
   methodology. Lives in the separate `ai-visibility-readiness` repo.
   This repo references it but does not redefine it.
4. **"AVR Score"**: citability.dev's product score, a 0-100 number
   rolling up V/R/C. Takes no separate canonical long-form. When
   maximum disambiguation is needed, "the AVR Score (the framework's
   numeric output)" is acceptable; never "AVR Score (Answer
   Visibility Ratio)."
5. **"VRC"**: citability.dev's component axis (Visibility,
   Recommendability, Citability). Used only in citability-dev product
   contexts.
6. **"Agent Readiness"**: the parallel wedge (agent-action +
   agent-commerce + payment-readiness). Documented in this repo's
   future agent-readiness chapter, separate from AVR.

### Why this matters

- AI engines extract definitions from `llms.txt` and `.well-known/`
  surfaces. If the same operator's domain returns one definition and
  a related domain returns another, the engine picks one (often
  inconsistently across queries) and brand semantic precision
  degrades. The "Answer Visibility Ratio" backronym was creating
  exactly this contradiction within citability.dev itself.
- Buyer confusion: a sales conversation that says "AVR is our
  framework" while the dashboard JSON-LD claims "AVR is the score
  (Answer Visibility Ratio)" creates trust friction.
- Backlinks earned by this public reference doc accrue to the
  canonical names ratified here. Asymmetric cost on rename: a
  backlink earned under one canonical name does not transfer cleanly
  to a renamed concept.

### Ratification status

`Inferred`, pending operator-read of this rewritten body in a future
session.

A prior 2026-05-02 ratification (`dc-20260502T070000Z-avr0-push`)
landed this node as `Verified` with the now-repudiated mapping
(treating "Answer Visibility Ratio" as the canonical score
expansion). That ratification was annotated `wrong` in self-ledger
on 2026-05-02 (`dc-20260502T143400Z-avr-rename-annotate`) after the
operator confirmed they did not author "Answer Visibility Ratio" and
a cross-property check showed the term lives only in citability.dev
trust surfaces — contradicting the same site's FAQ.

The corrected mapping in this rewrite is deliberately Inferred, not
re-Verified by the same model that got it wrong yesterday.
Re-ratification only happens after the operator has read this
rewritten body.

### Override path

If operator overrides this resolution (e.g., reinstates "Answer
Visibility Ratio" or picks a different long-form expansion), this
node updates to the new canonical names AND triggers a re-write
pass on:

- This repo's README + whitepaper + new architecture chapters.
- citability-dev's `public/llms.txt`,
  `public/.well-known/citability.json`, `app/docs/page.tsx`,
  `app/page.tsx` FAQ structured data.
- chudi-blog's surfaces if any reference AVR by acronym.

The cost of the override is the same regardless of when it happens,
but the cost of unratified public publication is asymmetric: a
backlink earned under one canonical name does not transfer cleanly
to a renamed concept.

## Where

This node has no code anchors. It is a strategy / governance node
that references external authorities:

- `citability-dev/docs/codex/nodes/avr-naming-authority.md`: the
  upstream resolution. Source of truth for citability product
  taxonomy. Also pending its own ratification.
- `citability-dev/public/llms.txt:1-50`: surface that calls AVR
  the "AI Visibility Readiness Framework." Consistent with this
  resolution after the parallel PR lands.
- `citability-dev/public/.well-known/citability.json:1-100`:
  surface that previously labeled the score "Answer Visibility
  Ratio." Corrected by the parallel PR.
- `citability-dev/app/page.tsx`: FAQ structured data that AI
  engines parse. Corrected by the parallel PR.
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
- "Answer Visibility Ratio" (any reference)

Do NOT route here for purely product-side citability naming questions
(those route to citability-dev's `avr-naming-authority` node directly).

## Refresh policy

Re-verify after:

- Operator reads this rewritten body and ratifies (or overrides) the
  corrected canonical split.
- Parallel citability-dev PR lands, removing "Answer Visibility
  Ratio" from live surfaces.
- Any rename of AVR-related copy in this repo's README, whitepaper,
  or architecture chapters.
- Any change to citability-dev's `avr-naming-authority.md`
  resolution.
- Quarterly check: search this repo's docs for the literal string
  "AVR" and confirm each occurrence resolves to one of the canonical
  meanings without ambiguity. Same for citability-dev.

Next refresh: on operator ratification of this rewritten body, OR
2026-08-01 (whichever sooner).
