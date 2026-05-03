# The 15-Check Audit (AI Visibility Readiness)

> Evidence boundary: this chapter documents the AI Visibility Readiness
> Framework (15-check tiered audit). The framework specification lives
> in a separate repository,
> [`github.com/ChudiNnorukam/ai-visibility-readiness`](https://github.com/ChudiNnorukam/ai-visibility-readiness).
> citability.dev is one concrete implementation of the same shape. This
> chapter summarizes how the framework relates to the AI-Visible Web
> Architecture pattern and what changes when an adopter wants both the
> pattern and the audit. Chapter status: `Inferred`, pending the
> operator's ratification of the naming canonical split.

## Why a Tiered Audit (Not a Single Composite Score)

A single 0-100 readiness score hides which tier is failing. The 15
checks are categorically different kinds of claim, and collapsing them
into one number tells an adopter nothing actionable.

The framework refuses the composite. It outputs one of four discrete
statuses:

- **AI-READY**: Tier 1 + Tier 2 all pass; Tier 3 citations greater than 0
- **INFRASTRUCTURE-READY**: Tier 1 + Tier 2 all pass; Tier 3 below threshold
- **FOUNDATION-READY**: Tier 1 passes; one or more Tier 2 gaps
- **NOT-READY**: at least one Tier 1 failure

A status of `FOUNDATION-READY` with a list of four Tier-2 fails tells
an adopter exactly what to fix next week. A score of "74 out of 100"
does not.

This discipline maps to the same idea as the evidence labels used
throughout this repo (`Verified`, `Inferred`, `Target State`):
categorical separation beats numerical compression when the categories
mean different things.

## The 15 Checks, in Three Tiers

### Tier 1, SEO Foundation (6 checks, all `[VERIFIABLE]`)

Classical site-level hygiene. Every check is runnable against the raw
HTML or HTTP headers; no LLM calls needed.

1. HTTPS present.
2. `robots.txt` exists and does not blanket-block crawlers.
3. `sitemap.xml` exists.
4. Canonical tag present on each page.
5. `<title>` and `<meta name="description">` present.
6. Heading hierarchy (h1 / h2 / h3) sane.

### Tier 2, AI Infrastructure (6 checks, all `[VERIFIABLE]`)

The LLM-era structural layer. Also purely HTML and HTTP; no LLM calls.

7. `/llms.txt` present (matches the surface contract; see
   `architecture/machine-readable-interface-contract.md`).
8. Answer-first intro on the homepage (passage-retrieval friendly).
9. Structured data (JSON-LD) present on representative pages.
10. Open Graph and Twitter Card tags.
11. AI crawler allow-list in `robots.txt`: GPTBot, ClaudeBot, CCBot,
    PerplexityBot explicitly allowed (or at minimum not blanket-denied).
12. Passage-chunkable content shape (short paragraphs, clear h2 / h3
    structure).

### Tier 3, Citation Monitoring (3 checks, all `[BEST-EFFORT]`)

Where ground-truth gets expensive. These require live LLM queries and
carry confidence tiers (LOW / MODERATE / HIGH) based on sample size.

13. Cited-by-LLM rate across N engines (the citation rate measurement;
    citability.dev calls this `vScore`).
14. Share-of-voice vs named competitors.
15. Brand-name recall ("who are the best Xs?") by LLM.

## VERIFIABLE vs BEST-EFFORT

The labeling discipline is load-bearing. A static HTML check
(`/llms.txt` present) is repeatable and deterministic. A citation rate
across LLMs is a sample, with all the confidence-interval consequences
that implies. Mixing them into one composite score lies about how
confident the audit can be.

Adopters of this pattern who run the audit should preserve the
labeling in their reports. citability.dev does this by separating the
`r/c-score` axes (R for Readiness, C for Chunkability, derived from
Tier 1 + Tier 2) from the `vScore` axis (V for Visibility, derived
from Tier 3). See citability-dev's `r-c-score` and `v-score` codex
nodes.

## Counter-intuitive Findings (AVR v1 Sample)

The framework's first benchmark sweep surfaced four findings worth
reproducing in any pattern-adoption discussion:

- **Domain Authority does NOT predict AI readiness.** chudi.dev (DA
  approximately 5) scores AI-READY; reddit.com and x.com (DA 99) score
  NOT-READY because they block AI crawlers and serve heavy
  client-side-rendered pages.
- **Visibility is the floor, not the win.** Ahrefs.com has
  approximately 100 percent visibility but approximately 5 percent
  citation rate. Being crawlable is necessary; being cited requires
  entity authority and answer-first content shape.
- **Approximately 85 percent of sites lack AI-readable surfaces.**
  Most public sites fail Tier 2 even when Tier 1 is clean.
- **Audit cost at scale is approximately $3.20 per site.** Driven
  almost entirely by Tier 3 LLM queries. Tier 1 + Tier 2 are
  cache-friendly static checks.

These findings are reasons the architecture pattern needs an
entity-authority chapter and a backlink-and-off-page chapter (see
`architecture/entity-authority-layer.md`,
`architecture/backlink-and-off-page.md`). The pattern alone covers the
on-site half; the off-site half is what actually converts visibility
into citation.

## How This Chapter Relates to the Repository's Verification Layer

This repo's `proof/verification-matrix.md` and
`scripts/audit_live_surfaces.py` already implement a subset of the 15
checks against the live chudi.dev surfaces:

- Tier 1: HTTPS, sitemap.xml presence are checked.
- Tier 2: `/llms.txt`, `/llms-full.txt`, `/ai.txt`,
  `/.well-known/llms.json` presence are checked.
- AI-crawler allow-list in `robots.txt` is `Target State`: not yet
  asserted by `audit_live_surfaces.py`. Tracked in
  `architecture/machine-readable-interface-contract.md` companion
  surfaces section.
- Tier 3 checks are `Target State` for this repo. Citation rate
  measurement is implemented operationally by citability.dev's audit
  pipeline, not by this reference repo.

The verification chapter (`proof/verification-matrix.md`) and the
codex node `verification-discipline` describe the audit checks this
repo enforces under CI today and which checks are planned next.

## When to Use the 15-Check Audit vs the Architecture Pattern

- **Pattern alone**: building a new AI-visible site from zero.
  `architecture/conceptual-system-architecture.md` and the surface
  contract chapter are the right starting points.
- **Audit alone**: assessing an existing site's readiness without
  rebuilding it. The 15 checks score the current state; remediation
  follows from the failing checks.
- **Pattern + audit**: building or evolving a site and using the audit
  as the success metric. The pattern provides the surfaces; the audit
  scores them; the chapter closes the loop between architecture and
  measurement.

## Implementation Gaps Still in the Pattern's Verification

These are the checks the framework specifies but this repo does not
yet enforce. Each is `Target State` until added to
`audit_live_surfaces.py`:

- AI-crawler allow-list assertion (Tier 2, check 11).
- JSON-LD presence and shape per page (Tier 2, check 9).
- Open Graph and Twitter Card validation (Tier 2, check 10).
- Passage-chunkable content shape heuristic (Tier 2, check 12).
- Share-of-voice and brand-name recall (Tier 3, checks 14 and 15).
  Out-of-scope for a single-site audit. Adopters with competitor
  context can extend the audit pipeline as needed.

## References

- Framework specification:
  [`github.com/ChudiNnorukam/ai-visibility-readiness`](https://github.com/ChudiNnorukam/ai-visibility-readiness)
  (`FRAMEWORK.md` for the spec, `README.md` for benchmark findings).
- citability.dev `avr-framework` codex node: implementation notes for
  the audit pipeline.
- citability.dev `avr-status-rollup` codex node: the
  `computeAvrStatus` rollup logic and `RECOMMENDATIONS` table.
- citability.dev `r-c-score` and `v-score` codex nodes: the axis
  decomposition.
- This repo's `docs/codex/nodes/entity-and-authority-stack.md`: the
  off-site layers the audit cannot capture by itself.
