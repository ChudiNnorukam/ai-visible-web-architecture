# AI-Visible Web Architecture — Principles

**Scope:** This repo (`ai-visible-web-architecture`). Inherits global
ecosystem principles G1–G17 from `~/.claude/codex/PRINCIPLES.md`. A
local principle that conflicts with a global one MUST cite
`overrides: global-G<n>`; otherwise global wins.

**Status:** `Inferred`. Drafted 2026-05-06 as a 3-principle starter,
seeded from the codex's load-bearing claims and from operator
ratification of the codex-grounded thesis reading. Pending operator
read of this body and re-ratification.

---

## P1 — Evidence-first; never stand a claim on rhetoric

**Rule:** Every load-bearing claim in this repo carries one of three
labels:

- `Verified` — backed by a live public surface OR a runnable check
  (`scripts/audit_live_surfaces.py`,
  `scripts/check_repo_quality.py`).
- `Inferred` — explanatory or recommended pattern beyond what is
  directly observable; reasoned from primary sources.
- `Target` — desired architecture or behavior, not yet observable on
  the live system.

A load-bearing claim missing from
[`proof/verification-matrix.md`](../../proof/verification-matrix.md)
is either a row to add OR a claim to demote. No third option.

**Grounded in:**
[`verification-discipline`](./nodes/verification-discipline.md);
`proof/verification-matrix.md`;
`scripts/audit_live_surfaces.py`;
global G8 (evidence labels).

**Applies to:** README, whitepaper, all architecture chapters, all
diagrams, all blog cross-posts that cite this repo.

**Overrides:** none.

---

## P2 — This repo is the pattern, not the execution

**Rule:** This repository documents the AI-Visible Web Architecture
pattern. It does not BUILD AI visibility for any specific site. The
pattern is verified against [chudi.dev](https://chudi.dev) as the
live case study; the four off-site and audit chapters
(`the-fifteen-check-audit`, `entity-authority-layer`,
`backlink-and-off-page`, `agent-readiness-layer`) are `Inferred`
until adopters exercise them.

When a request looks like execution work for a specific site
("make my site #1", "ship the entity graph", "publish my llms.txt"),
the right home is downstream:

- Site-specific surfaces, content, and entity graph live in the
  adopter's own repo (e.g., `chudi-blog` for chudi.dev).
- Off-site authority work (Wikipedia and Wikidata, `sameAs`
  reciprocity, social profile parity, backlink earning) lives
  outside any code repo, in profile bios, Wikidata claims, and
  content placement.
- Productized audit and measurement lives in citability.dev.

The leveraged action inside this repo is making the pattern itself
cite-worthy as a reference doc, not shipping more sites against it.

**Grounded in:**
[`avr-pattern`](./nodes/avr-pattern.md);
[`entity-and-authority-stack`](./nodes/entity-and-authority-stack.md);
README "Project Thesis and Verified Scope" section;
README "Constraint" section;
global G11 (names describe current state, not aspirational state);
global G5 (preserve existing unless a concrete defect is named).

**Applies to:** chapter-authoring decisions, README scope claims,
how "make X #1 citation source" requests get triaged into this repo
versus downstream.

**Overrides:** explicit operator request to bring an adopter case
in-scope (e.g., adding a second case study repo alongside chudi.dev).

---

## P3 — WebMCP is positioning, not a citation-ranking signal

**Rule:** Treat WebMCP (`navigator.modelContext`) as the agent-action
surface (post-citation commerce and agent-callable tools), NOT as
part of the AI-citation pipeline.

Verified facts about WebMCP as of 2026-05-01 (per
`~/.claude/codex/nodes/webmcp-spec.md`):

- W3C Web Machine Learning Community Group **Draft Report**, NOT
  Standards-Track.
- No documented crawler reads `registerTool` declarations today.
- Chrome 146+ Canary behind `chrome://flags`; Firefox and Safari
  participants joined the CG but are not implementing as of the
  March 19 2026 CG minutes; realistic broad production support is
  2027+.
- The agent-action use case (Stripe ACP-style post-citation
  interaction, agent-driven commerce) is real and worth shipping.
  The "WebMCP boosts citation rate" narrative is not.

When a request frames WebMCP as a path to higher AI-citation rate,
correct the framing and route the work to the agent-readiness
chapter instead. Citation rate is moved by entity authority,
training-data presence, on-site retrieval design, and measurement
(per the 2026-04-16 calibration recorded in
[`entity-and-authority-stack`](./nodes/entity-and-authority-stack.md)),
not by adding browser-side tool registrations.

**Grounded in:**
`~/.claude/codex/nodes/webmcp-spec.md` (global, last_verified
2026-05-01);
[`entity-and-authority-stack`](./nodes/entity-and-authority-stack.md)
(2026-04-16 CONDITIONAL gate finding);
[`architecture/agent-readiness-layer.md`](../../architecture/agent-readiness-layer.md);
[`architecture/agent-interface-layer.md`](../../architecture/agent-interface-layer.md).

**Applies to:** WebMCP claims in README, whitepaper, surface-contract
docs, blog cross-posts, social copy.

**Overrides:** none. The spec status is empirical fact; refresh on
the CG draft schedule.

---

## Conflict resolution

1. Global G1–G17 win over silent local conflicts. A local principle
   conflicting with global MUST cite `overrides: global-G<n>`.
2. P1 (evidence) is the most specific local rule and beats any
   shape-of-content principle when a label is the question.
3. P2 (scope) is the gatekeeper for "should this work happen here at
   all" questions.
4. P3 (WebMCP framing) is a fact-shaped rule, not a tradeoff rule.
   No override.

When this file disagrees with itself OR with the codex node it
cites, flag the conflict to the operator and DO NOT silently pick.
The librarian's priority order
(`PRINCIPLES.md > node bodies > chudi-frame > confidence labels`)
applies.

---

## Refresh policy

Re-verify after:

- Any change to `~/.claude/codex/nodes/webmcp-spec.md` (P3
  fact-base).
- Any chapter ship that exercises one of the four off-site or audit
  chapters against a verifiable surface (P2 scope claim shifts).
- Operator ratification of any of P1–P3 (`Inferred → Verified` flip
  with `ratified: <date>` added).
- Quarterly drift check on the load-bearing facts cited.

Next refresh: 2026-08-01 OR on operator ratification, whichever
sooner.
