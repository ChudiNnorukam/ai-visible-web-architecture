---
id: verification-discipline
name: Verification Discipline (evidence labels + live audit + matrix)
domain: verification-discipline
aliases: [verification-discipline, evidence-first, evidence-labels, verified-inferred-target, live-audit, audit-script, verification-matrix, the-audit, the-proof]
code_refs:
  - path: proof/verification-matrix.md
    lines: 1-29
    sha256: d70f9b5d68b105d60505264a4877f2a6a926d0411f3b7c08e84c26636745a7d1
  - path: proof/live-audit.md
    lines: 1-47
    sha256: 71f2a37257d1a4a3de1a2248bbfa130496301db098493728bcc2a83c1c5fef35
  - path: proof/live-surfaces.md
    lines: 1-32
    sha256: 59f9f5d261a93adb9cd054cb08a786f3c723f817430130592800841d7a1a963a
  - path: scripts/audit_live_surfaces.py
    lines: 1-312
    sha256: de9c4ff82ea33c449526aad3eac2cf049cc5d30056e6d1ebf740d04e24dd9d00
  - path: scripts/check_repo_quality.py
    lines: 1-119
    sha256: 8faba62b9664fad79d91382fd1d70eb5888ec0199dd1a2384211f9afcd7c98c1
related: [avr-pattern, surface-contract, entity-and-authority-stack]
parent_concepts: [avr-pattern]
child_concepts: []
last_verified: 2026-05-02
confidence: inferred
---

## What

The evidence discipline this repository enforces. Every claim in a doc
carries one of three labels (this is the same scheme global G8 mandates
across the operator's portfolio):

- **Verified**: backed by a live public surface or a runnable check.
- **Inferred**: explanatory or recommended pattern beyond what is
  directly observable; reasoned from primary sources.
- **Target State**: desired architecture or behavior, not yet
  observable on the live system.

The discipline is operationalized through three artifacts:

### 1. The verification matrix

`proof/verification-matrix.md` is a flat table mapping each load-bearing
claim to:

- The live public surface that proves it.
- The local proof doc that captures the evidence.
- The audit check that enforces the claim under CI.

If a claim is in the README or whitepaper but missing from the matrix,
the discipline says either add the row OR demote the claim to Inferred /
Target.

### 2. The live audit (audit_live_surfaces.py)

`scripts/audit_live_surfaces.py` is the runnable verification of the
matrix. It hits each public chudi.dev surface (12 checks as of the
2026-05-01 update; robots.txt presence added) and reports pass/fail
with content-type and structural validations. Its
output is a JSON artifact written to `artifacts/live-audit-<date>.json`.
Failures open or update a GitHub issue automatically via the scheduled
workflow.

### 3. The repo quality gate (check_repo_quality.py)

`scripts/check_repo_quality.py` is the local-only structural gate.
Validates internal links, content markers, and that documented
contracts mention the right keys. Runs on every PR via the `quality`
gate and blocks merges on failure.

### What is currently in the matrix (verified rows)

The matrix verifies:

1. chudi.dev publishes explicit AI discovery files (llms.txt, llms-full.txt,
   ai.txt, .well-known/llms.json).
2. The live site exposes a machine-readable metadata contract.
3. The live site has core public sections discoverable through public
   surfaces (sitemap.xml + llms.txt key URLs).
4. The live site supports retrieval-oriented navigation (`/start`,
   `/topics`, `/about`).
5. chudi.dev documents and demonstrates an agent interface layer
   (WebMCP article).
6. Repo claims stay tied to executable verification (local scripts +
   GitHub Actions).

### What the matrix does NOT yet verify (planned)

- AI-crawler allow-list in chudi.dev's robots.txt.
- Schema JSON-LD presence and shape (Person + Organization + sameAs
  parity across surfaces).
- IndexNow ping freshness.
- Bing webmaster verification file presence.
- Cross-link contract enforcement (canonical URLs on Medium / Dev.to /
  Hashnode crossposts pointing back to chudi.dev).
- Entity-graph parity across surfaces (LinkedIn / GitHub / Medium bios
  match the canonical Person schema).

Each unverified row is a candidate for the planned 15-check audit
chapter and the corresponding extension of audit_live_surfaces.py.

## Where

In-repo:

- `proof/verification-matrix.md`: the matrix itself.
- `proof/live-audit.md`: describes what the live audit does and how it
  reports.
- `proof/live-surfaces.md`: proof of which surfaces are public.
- `proof/llms-and-ai-discovery.md`, `proof/webmcp-implementation.md`:
  per-claim proof docs.
- `scripts/audit_live_surfaces.py:1-312`: the live audit runner.
- `scripts/check_repo_quality.py:1-119`: the local quality gate.
- `.github/workflows/`: CI integration (live audit schedule + PR
  quality gate).

External grounding (the discipline mirrors others):

- `citability-dev/docs/codex/nodes/avr-framework.md`: the 15-check
  framework also separates VERIFIABLE checks from BEST-EFFORT checks,
  the same idea expressed differently.
- `citability-dev/PRINCIPLES.md`: "Trust artifact" discipline (don't
  pencil-whip numbers, don't claim a check passed it didn't run).
- `~/.claude/codex/PRINCIPLES.md` G8: "Evidence labels on every claim.
  Never present Inferred as Verified."

## When-to-touch

Route here when the user says:

- "is the audit passing", "what does live-audit do"
- "verification matrix", "the proof", "the evidence"
- "is this Verified or Inferred"
- "add an audit check for X"
- "the script", "audit_live_surfaces", "check_repo_quality"
- "CI is failing on the quality gate"

Do NOT route here for the surface contract definitions themselves
(route to `surface-contract`) or for the higher-level pattern
(route to `avr-pattern`).

## Refresh policy

Re-verify after:

- Any change to `audit_live_surfaces.py` SURFACE_CHECKS list (rows
  added or removed).
- Any change to `verification-matrix.md` (claims added, removed, or
  re-labeled).
- Any change to `.github/workflows/` that touches the quality gate or
  live-audit scheduled job.
- Quarterly check that all rows in the matrix have corresponding live
  surfaces returning 200 (drift detection).

Next refresh: 2026-08-01, or sooner on any audit-script or matrix
change.
