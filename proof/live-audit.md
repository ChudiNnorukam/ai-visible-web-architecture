# Live Audit Contract

This repository claims that `chudi.dev` already exposes public surfaces for discovery, retrieval, and agent interoperability.

Those claims should be runnable, not just readable.

## What the Audit Checks

`scripts/audit_live_surfaces.py` verifies four things against the live site:

1. The documented public endpoints return `200`.
2. Each endpoint returns the expected content type for its role.
3. `llms.txt` includes the core discovery links used throughout this repo.
4. `.well-known/llms.json` exposes the minimum machine-readable contract this repo relies on.

## Why This Exists

The main failure mode for an evidence-first repo is silent drift between:

- what the docs say is live
- what the live site actually exposes
- what readers can reproduce for themselves

The audit closes that gap by turning the public proof into an executable contract.

## Run It

```bash
python3 scripts/audit_live_surfaces.py
```
