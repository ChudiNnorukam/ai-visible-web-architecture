# Backlinks and Off-Page Authority

> Evidence boundary: this chapter documents the off-site link and
> referring-domain layer. Most claims are `Inferred` from public
> primary sources (Google patent disclosures, Search Liaison
> guidance, leaked internal documents) plus observed adopter data.
> The authority of any single tactic in 2026 is degraded relative to
> earlier years: Google has actively reduced the influence of low-
> quality links, and LLMs use links as one signal among many. Chapter
> status: `Inferred`.

## Why This Chapter Belongs in the Pattern

The 3-layer pattern handles on-site information design, surface
contracts, and agent interfaces. None of those layers, by themselves,
move the needle on:

- Classical search rankings, where backlinks remain the strongest
  off-page signal twenty-five years after PageRank.
- LLM citation, where models weight authoritative sites more heavily
  in synthesis even when retrieval is the proximate source of facts.
- Brand training-data presence, which is partially a function of
  whether high-authority sites link to and discuss the brand.

The April 2026 finding from this operator's portfolio is explicit:
real moats are backlinks plus Bing index coverage plus measurement,
not more iteration on `llms.txt`-style on-site surfaces. This chapter
is that finding made architectural.

## What Actually Counts

Counts and attributes ordered by impact, with the failure modes that
defeat each:

### Referring domains (RDs), not total backlinks

100 links from a single domain are roughly worth 1 link. 1 link each
from 100 domains is roughly worth 100 links, with diminishing returns
per additional link from the same domain. Optimize for diversity, not
count.

### Domain authority of the referring site

A link from a household-name publication outweighs a link from a
brand-new low-authority blog by many multiples. Standard tool
proxies: Ahrefs DR, Moz DA, Semrush AS. All are estimates. None is
Google's actual internal score, but they correlate well enough to
guide tactics.

### Topical relevance of the referring site and page

A link from a fintech publication to a fintech page is worth far
more than the same authority-level link from a recipe blog. Google's
"reasonable surfer" model (patent, 2010) discounts off-topic links
on the assumption that real users would not click them.

### Anchor text profile

The clickable text is a ranking signal for the link target. Two
non-obvious rules:

- Exact-match anchors ("best SEO tool" pointing to the best-SEO-tool
  page) are a spam signal past about 3 to 5 percent of total anchor
  profile.
- Natural anchor profiles are dominated by branded anchors, URL
  anchors, and generic anchors ("here," "click"), with occasional
  topical phrases.

### Link placement

In-content body links carry more weight than footer or sitewide
navigation links, again per the reasonable-surfer assumption that
users are more likely to click an in-context link.

### Follow vs nofollow

`rel="nofollow"`, `rel="sponsored"`, and `rel="ugc"` tell Google not
to pass PageRank. Most high-authority sites apply nofollow by default
for outbound links, which is fine: a nofollow link still drives
referral traffic and brand mentions, but does not move classical
rankings directly.

### Link velocity

Unnatural spikes (zero links to 500 links in a week with no news
event) pattern-match to spam. Google's SpamBrain filters these.
Earned-by-news velocity is fine; manufactured velocity is not.

## What Works (in 2026)

1. **Digital PR**: newsworthy original research, data reports,
   calculators, interactive tools. Pitch journalists via HARO,
   Qwoted, or Featured. A single substantive link from a top-tier
   publication can change site trajectory for years.

2. **Linkable assets**: tools, calculators, original studies,
   definitive guides. The asset does the link-building passively by
   being shareable and citable.

3. **Guest posts (carefully)**: write for topically relevant
   high-authority sites; only valuable when the host site has real
   authority AND the link is editorial, not labeled "sponsored."
   SpamBrain detects paid placements at scale.

4. **Broken link building**: find dead links pointing at competitors;
   pitch your replacement. Low volume but high conversion when the
   topical fit is real.

5. **Unlinked brand mentions**: tools find mentions of your brand
   without a link; reach out to add the link. Cheap wins.

6. **Podcast appearances**: most shows link to guest sites in show
   notes. Often mid-authority domains with high topical relevance,
   plus the entity-authority benefit covered in
   `architecture/entity-authority-layer.md`.

## What Does Not Work

These cost time and create exposure to manual actions or spam
filters:

- **Private Blog Networks (PBNs)**: networks of owned sites linking
  to money sites. Detected by IP footprint, Whois patterns, content
  similarity. Penalty class.
- **Link exchanges at scale**: "you link to me, I link to you."
  Detected as reciprocal-link clusters.
- **Forum and blog comment spam**: every comment form's "website"
  field. Detected trivially; nofollow by default.
- **Cheap link packages**: "100 high-DR backlinks for $200" on
  freelance marketplaces. Always PBN or comment spam under the
  hood.

## Time Dynamics

- Links take three to six months to fully count in rankings after
  Google discovers and trusts them. Patience is mandatory; the
  ranking response lag is long enough that adopters often misread
  noise for outcomes.
- Lost links (referring page removes yours) show up two to twelve
  months later as ranking drops. Monitor via Ahrefs "Lost" reports
  or equivalent.

## How LLMs Use Backlinks

LLMs do not directly read the live link graph the way Google does.
They use backlinks indirectly: training data is weighted toward
authoritative sites, and authority correlates strongly with the link
graph that PageRank measures. Practical implications:

- A site with strong links to it is more likely to appear in Common
  Crawl with greater depth and recency, which feeds training data
  more thoroughly.
- A site cited by Wikipedia (a backlink with extreme entity weight)
  is overrepresented in models that train on Wikipedia heavily.
- Live-retrieval LLMs (Perplexity, ChatGPT Search, Claude with web
  access) use rerankers that often inherit authority signals
  correlated with classical SEO ranking. A site that ranks well
  classically is more likely to be retrieved live.

The entity-authority layer and the backlink layer are related but
not identical. Entity authority answers "does the model know this
brand exists?" Backlinks answer "is the model's retrieval system
likely to surface this site at all?"

## Bing Coverage as a Companion Concern

The April 2026 operator finding named "Bing index coverage" alongside
backlinks. The relationship: many LLMs use Bing as their retrieval
back-end (ChatGPT, Copilot, others). A site that is well-indexed in
Bing will be reached by those LLMs even when its Google ranking is
weaker. Adopters should:

- Verify the site in Bing Webmaster Tools.
- Submit `sitemap.xml` to Bing.
- Use IndexNow to push fresh content to Bing within minutes.
- Audit Bing's actual coverage; the public consensus that "Bing has
  10 percent share" understates Bing's importance for LLM-era
  citation.

This is a `Target State` extension to the surface contract. Adding
an IndexNow ping endpoint and Bing verification file presence to the
companion-surfaces section of
`architecture/machine-readable-interface-contract.md` is the
implementation hook.

## Verification Hooks (Target State)

The audit checks that would assert backlink and Bing claims under CI
are not yet in `scripts/audit_live_surfaces.py`. Candidates:

- Bing webmaster verification file presence (`/BingSiteAuth.xml`).
- IndexNow key file presence at the site root.
- Cross-link contract enforcement: scan adopter's amplifier surfaces
  (Medium, Dev.to, Hashnode) for `<link rel="canonical">` pointing
  back to the canonical site. Failures are signal that a cross-post
  is leaking citation authority away from the canonical.

The cross-link contract specifically is documented in the global
codex (`~/.claude/codex/nodes/cross-link-contract.md`) as seven rules
covering canonical URLs, internal linking depth, LinkedIn behavior,
GitHub author credits, and reciprocal site interlinking.

## What This Chapter Does Not Cover

- **On-site internal linking depth**: handled by topical authority
  conventions and content-cluster topology. Briefly: every blog post
  in a pillar should link to two or three sibling posts; pillar
  pages should link to all primary supporting posts.
- **Anchor text optimization for AI engines specifically**: too few
  reproducible findings to ship as architecture. Adopters should
  prioritize anchor diversity over any AI-specific tweak.

## References

- This repo's `docs/codex/nodes/entity-and-authority-stack.md`: the
  off-site catalog this chapter is one of four.
- Operator's global codex node `backlink-authority`: cross-repo
  reference for referring-domain tactics.
- citability-dev codex node `backlink-authority`: product-side
  mirror; audit-pipeline implications for measuring referring-domain
  signal at scale.
- Operator's global codex node `cross-link-contract`: the seven
  rules for the operator's portfolio surfaces.
- Google "reasonable surfer" patent (2010, US7716225B1).
- HARO, Qwoted, Featured: PR pitching directories.
- Bing Webmaster Tools, IndexNow specification.
