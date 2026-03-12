# Live Audit Contract

This repository claims that `chudi.dev` already exposes public surfaces for discovery, retrieval, and agent interoperability.

Those claims should be runnable, not just readable.

## What the Audit Checks

`scripts/audit_live_surfaces.py` verifies the live site contract:

1. The documented public endpoints return `200`.
2. Each endpoint returns the expected content type for its role.
3. `llms.txt` and `ai.txt` expose the expected discovery and guidance markers.
4. `.well-known/llms.json` exposes the minimum machine-readable contract this repo relies on.
5. `sitemap.xml` includes the core site sections used in repo documentation.

`scripts/check_repo_quality.py` verifies the local repo contract:

1. required governance files are present
2. JSON examples parse cleanly
3. relative Markdown links resolve
4. Markdown files do not contain trailing whitespace

## Why This Exists

The main failure mode for an evidence-first repo is silent drift between:

- what the docs say is live
- what the live site actually exposes
- what readers can reproduce for themselves

The audit closes that gap by turning the public proof into an executable contract.

## Run It

```bash
python3 -m py_compile scripts/*.py
python3 scripts/check_repo_quality.py
python3 scripts/audit_live_surfaces.py
```

To generate a machine-readable audit artifact for CI:

```bash
python3 scripts/audit_live_surfaces.py --json-out artifacts/live-audit.json
```
