---
id: surface-contract
name: Public Surface Contract (llms.txt family + WebMCP)
domain: surface-contract
aliases: [surface-contract, machine-readable-contract, llms-txt, llms-full-txt, ai-txt, well-known-llms-json, webmcp-contract, public-surfaces, the-contract]
code_refs:
  - path: architecture/machine-readable-interface-contract.md
    lines: 1-52
    sha256: afddf41d8a5d20f6240819eba1296a19fbeed6fbd3a0a2c4e8095ae348ac427c
  - path: examples/llms.txt
    lines: 1-18
    sha256: bf888c4674c6c7b2489d7e1e7dd6c0a441b704fa4f39c802d4b3e881c14e1629
  - path: examples/llms.json
    lines: 1-16
    sha256: a18762cd41e45cfd3496782bf70deaf5ee2a6e7d9da41d512456e433c10bc591
  - path: examples/ai.txt
    lines: 1-20
    sha256: 1328f9db62cbc007b8e533fa631406fe30da21349e2574926abc3c3691c09e5e
  - path: proof/llms-and-ai-discovery.md
    lines: 1-15
    sha256: 493434836f10043814848a8fe4ce284f8e3929fcac7aec61210e522f90a61482
related: [avr-pattern, verification-discipline, entity-and-authority-stack]
parent_concepts: [avr-pattern]
child_concepts: []
last_verified: 2026-07-11
confidence: inferred
---

## What

The contract on which public artifacts an AI-visible site exposes and what
each one is for. Adopters of the pattern publish each artifact in a
documented form so retrieval systems and agents can orient without
guessing.

### The verified surfaces (live on chudi.dev today)

| Surface | Role | Verified key contents |
|---|---|---|
| `/llms.txt` | Short-form site discovery and priority navigation | Key sections + pointers to richer endpoints |
| `/llms-full.txt` | Expanded retrieval context with full-content specimens | Author, topics, permissions, dense retrieval surface |
| `/ai.txt` | Policy and crawler guidance | Access expectations, citation preference, preferred resources |
| `/.well-known/llms.json` | Structured machine-readable metadata | `site`, `author`, `keyTopics`, `bestPages`, `endpoints`, `policies`, `recentPosts` |
| WebMCP browser tools | Direct agent interface surface | First-party documented tool definitions |

### Contract rule

These interfaces should agree on core identity, preferred endpoints, and
attribution requirements. When one changes, the verification layer in this
repo (see `verification-discipline`) must be updated in the same pull
request so claims and evidence stay aligned.

### Companion surfaces (not yet in the matrix but increasingly load-bearing)

These belong to the contract per the AI Visibility Readiness
framework but are not yet enforced by this repo's verification layer.
Expected to be added; the current check list is generated at
`CHECKS.md` in the ai-visibility-readiness repo:

- `robots.txt`: must not blanket-block AI crawlers (GPTBot, ClaudeBot,
  PerplexityBot, CCBot). Allow-list is the contract.
- Schema JSON-LD per page: `Person`, `Organization`, `BlogPosting`,
  `Article`, `BreadcrumbList` with consistent `sameAs` graph (see
  `entity-and-authority-stack`).
- Open Graph and Twitter Card tags: for share-surface coherence.
- IndexNow ping endpoint: for fresh-content push to Bing.

### What is target-state, not verified

- Public tool manifests and schemas versioned as explicit machine
  contracts (today the WebMCP surface is documented but not versioned
  as a formal manifest).
- Cross-domain `sameAs` reciprocity audit (LinkedIn, GitHub, Medium,
  Dev.to bidirectional linking).
- AI-crawler allow-list assertion in audit_live_surfaces.py.

## Where

In-repo:

- `architecture/machine-readable-interface-contract.md`: the full
  contract document.
- `examples/llms.txt`, `examples/llms-full.txt`, `examples/ai.txt`,
  `examples/llms.json`, `examples/schema-person.json`,
  `examples/schema-website.json`: representative specimens.
- `proof/llms-and-ai-discovery.md`: proof claim that chudi.dev publishes
  each surface.
- `proof/webmcp-implementation.md`: proof claim for the agent interface
  surface.

External grounding:

- chudi.dev live surfaces: `/llms.txt`, `/llms-full.txt`, `/ai.txt`,
  `/.well-known/llms.json`, `/sitemap.xml`.
- `chudi-blog/docs/codex/nodes/llms-surfaces.md`: chudi.dev's
  implementation node, including the cluster-surface change of
  2026-04-21 (bug-bounty retired, ai-visibility-engineering replaces
  answer-engine-optimization).
- `citability-dev/docs/codex/nodes/llms-txt-standard.md`: the standard
  this repo's contract aligns with.
- `citability-dev/docs/codex/nodes/ai-txt-spec.md`: the ai.txt spec.
- `citability-dev/docs/codex/nodes/agent-action-surface.md`: the
  citability-dev parallel surface for agent actions
  (`.well-known/agent-actions`) that informs the agent-readiness chapter.

## When-to-touch

Route here when the user says:

- "fix the llms.txt", "the contract", "what should llms-full.txt say"
- "ai.txt", "well-known/llms.json", "schema JSON-LD", "WebMCP"
- "is my surface contract complete"
- "what's the canonical machine-readable surface set"
- "can agents discover this site"

Do NOT route here for the higher-level pattern (route to `avr-pattern`)
or for whether the surfaces are passing audit (route to
`verification-discipline`).

## Refresh policy

Re-verify after:

- Any change to `examples/*` specimens.
- Any rename or contract change in
  `architecture/machine-readable-interface-contract.md`.
- Any new surface added to `audit_live_surfaces.py` SURFACE_CHECKS list.
- Quarterly check on whether the live chudi.dev surfaces still match the
  documented contract (drift detection).

Next refresh: 2026-08-01, or sooner on any chudi.dev surface rename.
