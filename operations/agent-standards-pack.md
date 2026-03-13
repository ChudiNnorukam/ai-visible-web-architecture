# Agent Standards Pack

This standards pack is the reference set future contributors and agents should consult before making architectural, discoverability, structured-data, interoperability, performance, or verification claims in this repository.

## Source Priority Order

1. Official product documentation and standards bodies
2. Vocabulary and protocol references
3. Primary-source ecosystem documentation
4. Secondary commentary only when needed for context

If a higher-priority source exists for the decision at hand, use it before lower-priority sources.

## Search and Indexing

### 1. Google Search Essentials

- Source: [Google Search Essentials](https://developers.google.com/search/docs/essentials)
- Governs: baseline search eligibility, spam policy, and search best practices
- Consult when: making crawlability, indexing, discoverability, or content-quality claims
- Influences: whether a recommendation is compatible with Google’s stated requirements and guidance
- Prevents: building advanced discovery layers on top of weak search fundamentals
- Refresh note: watch for drift through Google Search documentation updates

### 2. Google Search Technical Requirements

- Source: [Google Search technical requirements](https://developers.google.com/search/docs/essentials/technical)
- Governs: technical conditions for crawling, rendering, indexing, and serving content
- Consult when: discussing HTTP behavior, rendering assumptions, crawl access, or sitemap/index eligibility
- Influences: architectural claims about whether pages and machine-readable surfaces are actually reachable and processable
- Prevents: “smart” architecture that fails basic fetch, render, or crawl requirements
- Refresh note: re-check when making technical SEO recommendations or architecture changes tied to access paths

## Structured Data and Semantic Identity

### 3. Google Article Structured Data Docs

- Source: [Google Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article)
- Governs: supported `Article`-class markup and author markup expectations in Google Search
- Consult when: discussing article schema, authorship, bylines, and visible-to-markup consistency
- Influences: how author entities and article metadata should be represented in search-facing guidance
- Prevents: over-modeling articles in ways that are not aligned with supported search behavior
- Refresh note: re-check whenever article or author markup guidance is discussed

### 4. Google Organization Structured Data Docs

- Source: [Google Organization structured data](https://developers.google.com/search/docs/appearance/structured-data/organization)
- Governs: site or organization identity signals that Google explicitly supports
- Consult when: modeling site identity, homepage entity metadata, or organization/person boundaries
- Influences: recommendations about site-wide identity and homepage-level machine-readable authority signals
- Prevents: treating identity markup as a generic graph exercise instead of a supported search surface
- Refresh note: re-check when changing identity guidance or homepage metadata recommendations

### 5. Schema.org `BlogPosting`

- Source: [Schema.org BlogPosting](https://schema.org/BlogPosting)
- Governs: vocabulary-level semantics for blog post content beyond search-engine-specific interpretation
- Consult when: the repo needs a vocabulary reference independent of any one search engine
- Influences: how machine-readable examples are modeled for broader ecosystem legibility
- Prevents: confusing search-engine support guidance with the full semantic vocabulary
- Refresh note: watch for vocabulary evolution, but use product docs first when behavior in a specific ecosystem matters

## Agent Interoperability

### 6. The `llms.txt` Spec

- Source: [The /llms.txt file](https://llmstxt.org/index.html)
- Governs: the emerging community convention for `llms.txt`
- Consult when: documenting `llms.txt` semantics, format expectations, or discovery role
- Influences: how the repo describes short-form AI discovery surfaces
- Prevents: inventing local `llms.txt` expectations without reference to the current community spec
- Refresh note: treat this as an emerging spec and re-check before making strong interoperability claims

### 7. Anthropic MCP Documentation

- Source: [Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/mcp)
- Governs: the mental model for standardized context and tool interoperability in agent ecosystems
- Consult when: describing MCP-style interfaces, tool exposure, or agent interoperability design
- Influences: how this repo frames callable context, tool contracts, and future-facing agent integration
- Prevents: reducing interoperability to vague “AI agent ready” language without a protocol model
- Refresh note: re-check when discussing transport, tool contracts, or interoperability guarantees

## Performance and Web App Behavior

### 8. W3C Web Application Manifest

- Source: [Web Application Manifest](https://www.w3.org/TR/appmanifest/)
- Governs: installable web app metadata and app-level identity semantics
- Consult when: the site is being discussed as a product-like web application rather than only a publishing surface
- Influences: whether app identity and installability claims are standards-aligned
- Prevents: conflating general site metadata with web application metadata
- Refresh note: standards work can shift; re-check before making app-manifest recommendations

### 9. web.dev on INP

- Source: [Interaction to Next Paint (INP)](https://web.dev/inp/)
- Governs: responsiveness guidance around INP and interaction quality
- Consult when: making performance claims about responsiveness, not just loading
- Influences: what counts as strong runtime interaction quality in future repo guidance
- Prevents: making performance recommendations based only on load-centric metrics
- Refresh note: re-check if Core Web Vitals guidance changes or when performance claims become part of the repo narrative

## Sitemap and Discovery Standards

### 10. Sitemaps Protocol

- Source: [sitemaps.org](https://sitemaps.org/)
- Governs: baseline sitemap structure and protocol expectations
- Consult when: discussing sitemap design, sitemap validation, or discovery surface correctness
- Influences: how sitemap behavior is described in the verification and discovery docs
- Prevents: custom sitemap logic that ignores the standard protocol
- Refresh note: stable reference, but still re-check before changing sitemap-specific guidance

## Monitoring Sources

These are not part of the core ten, but they should stay in the repo’s monitoring loop:

- [Latest Google Search documentation updates](https://developers.google.com/search/updates)
- [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

Use these when a change depends on current Google support boundaries or when a recommendation risks over-optimizing for machine readability at the expense of actual usefulness.
