# Verification Matrix

This matrix maps the repository's main claims to a live public surface, the local proof document, and the audit check that enforces it.

## Verified claims

| Claim | Live surface | Proof doc | Audit enforcement |
| --- | --- | --- | --- |
| `chudi.dev` publishes explicit AI discovery files. | `https://chudi.dev/llms.txt`, `https://chudi.dev/llms-full.txt`, `https://chudi.dev/ai.txt`, `https://chudi.dev/.well-known/llms.json` | [proof/live-surfaces.md](./live-surfaces.md), [proof/llms-and-ai-discovery.md](./llms-and-ai-discovery.md) | `surface contract`, `llms.txt markers`, `ai.txt markers`, `llms.json contract` |
| The live site exposes a machine-readable metadata contract. | `https://chudi.dev/.well-known/llms.json` | [proof/llms-and-ai-discovery.md](./llms-and-ai-discovery.md) | `llms.json contract` |
| The live site has core public sections discoverable through public surfaces. | `https://chudi.dev/sitemap.xml` and key URLs in `llms.txt` | [proof/live-surfaces.md](./live-surfaces.md) | `sitemap coverage`, `llms.txt markers` |
| The live site supports retrieval-oriented navigation. | `https://chudi.dev/start`, `https://chudi.dev/topics`, `https://chudi.dev/about` | [architecture/retrieval-and-citation-flow.md](../architecture/retrieval-and-citation-flow.md) | `surface contract` |
| `chudi.dev` documents and publicly demonstrates an agent interface layer. | `https://chudi.dev/blog/webmcp-sveltekit-implementation` | [proof/webmcp-implementation.md](./webmcp-implementation.md) | `surface contract`, `webmcp proof markers` |
| Repo claims stay tied to executable verification. | local scripts and GitHub Actions | [proof/live-audit.md](./live-audit.md) | `scripts/check_repo_quality.py`, `scripts/audit_live_surfaces.py`, `public-repo-quality` workflow |

## Target state claims (planned audit checks)

These claims belong to the chapters added in the 2026-05-01 evolution
(15-check audit, entity authority, backlinks and off-page, agent
readiness). Each row is `Target State` until the listed audit check
is implemented in `scripts/audit_live_surfaces.py` and merged.

| Claim | Live surface | Proof / chapter | Audit enforcement (planned) |
| --- | --- | --- | --- |
| `chudi.dev` does not blanket-block AI crawlers. | `https://chudi.dev/robots.txt` | [architecture/the-fifteen-check-audit.md](../architecture/the-fifteen-check-audit.md) Tier 2 check 11 | `robots.txt AI-crawler allow-list` (planned in `audit_live_surfaces.py`) |
| `chudi.dev` exposes Person and Organization JSON-LD with consistent `sameAs` graph. | per-page JSON-LD on `https://chudi.dev/about`, `/blog/*`, plus `/.well-known/llms.json` author block | [architecture/entity-authority-layer.md](../architecture/entity-authority-layer.md) | `schema JSON-LD presence`, `sameAs reciprocity` (planned) |
| `chudi.dev` is verified in Bing Webmaster Tools and pings IndexNow on publish. | `/BingSiteAuth.xml`, IndexNow key file | [architecture/backlink-and-off-page.md](../architecture/backlink-and-off-page.md) | `bing verification`, `indexnow key` (planned) |
| `chudi.dev` exposes a structured agent-action surface. | `/.well-known/agent-actions` (target) | [architecture/agent-readiness-layer.md](../architecture/agent-readiness-layer.md) | `agent-actions manifest`, `Tool Contract presence` (planned) |
| Cross-link contract is enforced on amplifier surfaces. | Medium / Dev.to / Hashnode crossposts pointing back to `chudi.dev` via `<link rel="canonical">` | global codex node `cross-link-contract` (operator's `~/.claude/codex/`) | `cross-link contract` (planned, requires fetching amplifier URLs) |
