# The AVR Audit (AI Visibility Readiness)

> **The check list is not in this file.** It lives in
> [`CHECKS.md`](https://github.com/ChudiNnorukam/ai-visibility-readiness/blob/main/CHECKS.md),
> generated straight from the audit code, and that is the only place it is
> written down. This chapter explains the audit's shape and how it relates to
> the AI-Visible Web Architecture pattern.
>
> This file used to enumerate fifteen checks by hand. The list was wrong. It
> still listed `llms.txt` as a required check after the framework had removed
> it, and it split the checks six-and-six when the code splits them
> seven-and-five. A restated list drifts; a linked list cannot. The filename is
> kept so existing links still resolve.

## Why a Tiered Audit (Not a Single Composite Score)

A single 0-100 readiness score hides which tier is failing. The checks are
categorically different kinds of claim, and collapsing them into one number
tells an adopter nothing actionable.

The framework refuses the composite. It outputs one of four discrete statuses,
computed by `computeAvrStatus` in citability.dev's `lib/avr-status.ts`:

- **AI-READY**: Tier 1 + Tier 2 all pass; citation score clears its threshold
- **INFRASTRUCTURE-READY**: Tier 1 + Tier 2 all pass; citation score below it
- **FOUNDATION-READY**: Tier 1 passes; one or more Tier 2 gaps
- **NOT-READY**: at least one Tier 1 failure

A status of `FOUNDATION-READY` with a list of Tier-2 fails tells an adopter
exactly what to fix next week. A score of "74 out of 100" does not.

This discipline maps to the same idea as the evidence labels used throughout
this repo (`Verified`, `Inferred`, `Target State`): categorical separation beats
numerical compression when the categories mean different things.

## What Sits in Which Tier

Tier 1 is classical site-level hygiene, the table stakes for any indexable site.
Tier 2 is the LLM-era structural layer. Both are pure HTML and HTTP probes, so
anyone can reproduce them. Tier 3 is citation measurement, which needs live LLM
queries and carries a confidence label instead of a bare number.

Which specific check sits in which tier is decided in code and published in
[`CHECKS.md`](https://github.com/ChudiNnorukam/ai-visibility-readiness/blob/main/CHECKS.md),
along with a fact worth knowing before you read any AVR report: several checks
are measured and shown but carry no tier at all, so they never move the verdict.
CHECKS.md names them.

## VERIFIABLE vs BEST-EFFORT

The labeling discipline is load-bearing. A static HTML check is repeatable and
deterministic. A citation rate across LLMs is a sample, with all the
confidence-interval consequences that implies. Mixing them into one composite
score lies about how confident the audit can be.

Adopters who run the audit should preserve the labeling in their reports.
citability.dev does this by separating the readiness axes (derived from Tier 1 +
Tier 2) from the visibility axis (derived from Tier 3). See citability-dev's
`r-c-score` and `v-score` codex nodes.

## Counter-intuitive Findings (AVR v1 Sample)

Four findings from the framework's first benchmark sweep. They are `Inferred`:
a single v1 sample, not re-measured since, and quoted here because they shaped
the pattern rather than because they are current.

- **Domain Authority does NOT predict AI readiness.** chudi.dev (DA
  approximately 5) scored AI-READY; reddit.com and x.com (DA 99) scored
  NOT-READY because they block AI crawlers and serve heavy
  client-side-rendered pages.
- **Visibility is the floor, not the win.** Ahrefs.com had approximately 100
  percent visibility but approximately 5 percent citation rate. Being crawlable
  is necessary; being cited requires entity authority and answer-first content
  shape.
- **Approximately 85 percent of sampled sites lacked AI-readable surfaces.**
  Most failed Tier 2 even when Tier 1 was clean.
- **Audit cost at scale was approximately $3.20 per site.** Driven almost
  entirely by Tier 3 LLM queries. Tier 1 + Tier 2 are cache-friendly static
  checks.

These findings are why the architecture pattern needs an entity-authority
chapter and a backlink-and-off-page chapter (see
`architecture/entity-authority-layer.md`,
`architecture/backlink-and-off-page.md`). The pattern alone covers the on-site
half; the off-site half is what converts visibility into citation.

## How This Chapter Relates to the Repository's Verification Layer

This repo's `proof/verification-matrix.md` and `scripts/audit_live_surfaces.py`
implement a subset of the audit against the live chudi.dev surfaces: HTTPS and
`sitemap.xml` presence, the machine-readable surface files (`/llms.txt`,
`/llms-full.txt`, `/ai.txt`, `/.well-known/llms.json`), and the AI-crawler
allow-list in `robots.txt` for GPTBot, ClaudeBot, PerplexityBot, and CCBot.

Tier 3 is `Target State` for this repo. Citation measurement is implemented
operationally by citability.dev's audit pipeline, not by this reference repo.

Everything the framework specifies and this repo does not yet enforce is a gap
in `audit_live_surfaces.py`, not in the framework. Rather than restate that gap
list here (which is how the previous version of this file went stale), diff the
surfaces asserted in `proof/verification-matrix.md` against
[`CHECKS.md`](https://github.com/ChudiNnorukam/ai-visibility-readiness/blob/main/CHECKS.md).

## When to Use the Audit vs the Architecture Pattern

- **Pattern alone**: building a new AI-visible site from zero.
  `architecture/conceptual-system-architecture.md` and the surface contract
  chapter are the right starting points.
- **Audit alone**: assessing an existing site's readiness without rebuilding it.
  The checks score the current state; remediation follows from the failures.
- **Pattern + audit**: building or evolving a site and using the audit as the
  success metric. The pattern provides the surfaces; the audit scores them.

## References

- Check list (generated from code):
  [`CHECKS.md`](https://github.com/ChudiNnorukam/ai-visibility-readiness/blob/main/CHECKS.md)
- Methodology and per-check design:
  [`FRAMEWORK.md`](https://github.com/ChudiNnorukam/ai-visibility-readiness/blob/main/FRAMEWORK.md)
- citability.dev `avr-framework` codex node: implementation notes for the audit
  pipeline.
- citability.dev `avr-status-rollup` codex node: the `computeAvrStatus` rollup
  logic and `RECOMMENDATIONS` table.
- citability.dev `r-c-score` and `v-score` codex nodes: the axis decomposition.
- This repo's `docs/codex/nodes/entity-and-authority-stack.md`: the off-site
  layers the audit cannot capture by itself.
