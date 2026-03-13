# Verification Matrix

This matrix maps the repository's main claims to a live public surface, the local proof document, and the audit check that enforces it.

| Claim | Live surface | Proof doc | Audit enforcement |
| --- | --- | --- | --- |
| `chudi.dev` publishes explicit AI discovery files. | `https://chudi.dev/llms.txt`, `https://chudi.dev/llms-full.txt`, `https://chudi.dev/ai.txt`, `https://chudi.dev/.well-known/llms.json` | [proof/live-surfaces.md](./live-surfaces.md), [proof/llms-and-ai-discovery.md](./llms-and-ai-discovery.md) | `surface contract`, `llms.txt markers`, `ai.txt markers`, `llms.json contract` |
| The live site exposes a machine-readable metadata contract. | `https://chudi.dev/.well-known/llms.json` | [proof/llms-and-ai-discovery.md](./llms-and-ai-discovery.md) | `llms.json contract` |
| The live site has core public sections discoverable through public surfaces. | `https://chudi.dev/sitemap.xml` and key URLs in `llms.txt` | [proof/live-surfaces.md](./live-surfaces.md) | `sitemap coverage`, `llms.txt markers` |
| The live site supports retrieval-oriented navigation. | `https://chudi.dev/start`, `https://chudi.dev/topics`, `https://chudi.dev/about` | [architecture/retrieval-and-citation-flow.md](../architecture/retrieval-and-citation-flow.md) | `surface contract` |
| `chudi.dev` documents and publicly demonstrates an agent interface layer. | `https://chudi.dev/blog/webmcp-sveltekit-implementation` | [proof/webmcp-implementation.md](./webmcp-implementation.md) | `surface contract`, `webmcp proof markers` |
| Repo claims stay tied to executable verification. | local scripts and GitHub Actions | [proof/live-audit.md](./live-audit.md) | `scripts/check_repo_quality.py`, `scripts/audit_live_surfaces.py`, `public-repo-quality` workflow |
