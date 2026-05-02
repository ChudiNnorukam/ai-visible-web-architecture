# Entity Authority Layer

> Evidence boundary: this chapter documents the off-site authority
> layer the AI-Visible Web Architecture pattern depends on but does
> not, by itself, supply. Most claims here are `Inferred` from primary
> documentation and observed LLM behavior. Adopters should treat the
> tactics as "best evidence today," not "guaranteed lift." Chapter
> status: `Inferred`.

## Why This Layer Exists

LLMs do not assemble citations from on-site signals alone. Two
distinct knowledge sources feed an LLM's response when an adopter's
brand might be cited:

1. **Training data**: what was in Common Crawl, Wikipedia, Wikidata,
   GitHub, Reddit, podcast transcripts, and the model's training
   corpus when the weights were fixed.
2. **Live retrieval**: what a search-augmented model finds at query
   time (Perplexity, ChatGPT Search, Claude with web access, Google
   AI Overviews).

The 3-layer pattern documented elsewhere in this repository optimizes
for live retrieval. This chapter is the layer that addresses the
training-data half. Without it, an unknown brand can be perfectly
crawlable and still lose every recommendation query because the model
has no prior weight on the name.

## The Entity Stack (descending priority)

The relative leverage of each signal, from highest to lowest, based
on observed LLM behavior:

### 1. Wikipedia article

The gold standard. Every major LLM was trained on Wikipedia. Being
the subject of a Wikipedia article means canonical existence to the
model. Bar to entry: notability (WP:GNG): significant coverage in
multiple independent reliable sources.

### 2. Wikidata entry

Structured data backing Wikipedia. Easier on-ramp than Wikipedia
itself: no notability test for organizations. Just verifiable
identity. Gemini and other Knowledge-Graph-aware models draw from
Wikidata heavily.

### 3. Google Knowledge Graph panel

The right-rail box on Google searches for "[brand name]". Triggered
by signals that aggregate from Wikipedia, Wikidata, Crunchbase,
LinkedIn, and authoritative mentions. Owned by Google but visible to
LLMs that index search results.

### 4. Authoritative third-party mentions

Coverage in TechCrunch, NYT, BBC, Forbes, trade publications. Both
for classical rankings AND for training-data presence. A single
substantive mention in a high-authority publication often outweighs
hundreds of low-authority mentions.

### 5. Structured data on the adopter's site

`Organization`, `Person`, `WebSite`, and `sameAs` schema. Explicitly
tells crawlers and LLMs "this is the entity, here are its LinkedIn,
Twitter, and Wikipedia profiles." See the surface contract chapter
for where this lives in the pattern's machine-readable surfaces.

### 6. Social graph

LinkedIn company page, verified Twitter or X handle, GitHub
organization (especially for developer-tool brands), Crunchbase
profile, YouTube channel. Each is a `sameAs` target and each is
indexed by major models. Reciprocal mutual linking matters: every
profile should point at the canonical site, and the canonical site
should list every profile.

### 7. Consistent name and description across the web

LLMs triangulate identity. Varying names and descriptions confuse the
signal. The canonical Person and Organization schema exposed via the
surface contract is the source of truth; profiles, READMEs, bios, and
podcast intros should match it.

## Why This Matters for Citation

Observed behavior: when an LLM is asked "who are the best companies
doing X?", the answer is dominated by brands that were in its
training data. Even if a newer brand publishes better content today,
the model's prior weighting skews older known names. Consequences:

- Wikipedia inclusion is disproportionately valuable for LLM-era
  recommendations.
- Brand salience (branded-search volume) is a strong LLM citation
  signal that shows up indirectly via Common Crawl.
- "Never heard of it" brands rarely win recommendation queries even
  with technically excellent on-site optimization.

Live retrieval partially corrects this: Perplexity, ChatGPT Search,
Claude with web search can find a new brand in the wild. Even so,
training-data-known brands receive heavier weight in the synthesis
step, especially for "best of" queries.

## How to Build Entity Authority

The tactics, ordered by leverage and time horizon:

### Long game (months to years)

1. **Earn a Wikipedia article.** Requires three or more substantive,
   independent sources. Do not edit the article directly; that is a
   conflict of interest under Wikipedia policy.
2. **Get mentioned in training-data-likely sources.** Tech
   publications, academic papers, GitHub READMEs (for developer
   tools), Reddit (for consumer products), Hacker News (for
   developer infrastructure). These feed Common Crawl and the
   specific LLM training corpora.
3. **Podcast circuit.** Podcast transcripts end up in training data
   via transcription sites and human summaries. Three to five
   appearances on relevant podcasts is a disproportionately
   high-leverage entity signal for the time invested.

### Mid game (weeks to months)

4. **Claim a Wikidata entry.** Much easier than Wikipedia. Register,
   create, list verifiable identifiers (website, LinkedIn, GitHub,
   Crunchbase). Often clears in days.
5. **Public original research or tools.** Being the cited source for
   a data point ("per [your site]'s 2026 audit...") is the single
   highest-leverage move for LLM authority. LLMs cite primary-source
   brands.
6. **Consistent name, address, phone, geographic data** for local
   brands. Varying business data across directories confuses entity
   resolution.

### Short game (days to weeks)

7. **Ship `Organization` plus `Person` schema** with `sameAs`
   linking to LinkedIn, Twitter, Wikipedia, Wikidata. Verify the
   reverse: each profile should point back at the canonical site.
8. **Audit social-profile bios.** Each profile's bio should match the
   canonical Person and Organization schema. LinkedIn job title,
   Twitter or X bio, GitHub README, Medium bio, Dev.to bio, YouTube
   channel description, podcast guest one-liners.

## Mapping to E-E-A-T

For adopters who already think in Google's E-E-A-T frame:

- **Experience**: first-person case studies in authoritative
  publications.
- **Expertise**: author Person schema plus LinkedIn plus book or
  paper history.
- **Authoritativeness**: Knowledge Graph panel plus Wikipedia plus
  backlinks from authorities.
- **Trustworthiness**: schema.org, sameAs reciprocity, consistent
  brand data.

The entity-authority layer is the LLM-era analog of E-E-A-T. The
signals overlap; the consumers differ.

## What This Layer Does Not Cover

- **On-site retrieval optimization**: that is the surface contract
  chapter and the agent interface chapter.
- **Backlink and referring domain authority**: an adjacent off-site
  layer covered in `architecture/backlink-and-off-page.md`.
- **Live citation measurement**: covered in
  `architecture/the-fifteen-check-audit.md` Tier 3 and operationally
  in citability.dev's vScore pipeline.

The three off-site chapters are independent layers that compose: an
adopter could rank well in retrieval (entity authority weak), have
strong backlinks but low LLM citation rate (entity authority gap),
or earn citations but lack backlinks (rare; the floors usually
co-fail). Treating them as one undifferentiated "off-page" bucket
hides the diagnostic.

## Verification Hooks (Target State)

The audit checks that would assert entity authority claims under CI
are not yet implemented in this repository's
`scripts/audit_live_surfaces.py`. Planned `Target State` checks:

- Schema JSON-LD presence on representative pages (Person and
  Organization).
- `sameAs` URL list parity across surfaces (the canonical site lists
  N profiles; each profile lists the canonical site).
- Wikipedia article URL or Wikidata entity ID presence in
  `.well-known/llms.json`.
- Knowledge Graph panel presence (signal: a Google search for the
  brand name returns a KG panel entity).

Each check is documented in
`docs/codex/nodes/verification-discipline.md` under "What the matrix
does NOT yet verify" and is a candidate for the next extension of the
audit script.

## References

- This repo's `docs/codex/nodes/entity-and-authority-stack.md`:
  catalog of what this chapter and adjacent chapters add.
- Operator's global codex node `entity-authority`: cross-repo
  reference for the entity stack.
- chudi-blog codex node `entity-graph`: chudi.dev's actual Person and
  Organization schema implementation, including the `sameAs` graph
  and the `aeo:check` build-time validation gate.
- citability-dev codex node `entity-authority`: product-side mirror
  with audit-pipeline implications.
- Wikipedia notability for organizations: WP:GNG, WP:ORG.
- schema.org Organization and Person types with `sameAs`.
- Google Knowledge Graph Search API documentation.
