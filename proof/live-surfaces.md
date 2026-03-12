# Live Surfaces on chudi.dev

These are the main public surfaces that support the AI-visible architecture claim.

## Discovery

- `https://chudi.dev/llms.txt`
- `https://chudi.dev/llms-full.txt`
- `https://chudi.dev/ai.txt`
- `https://chudi.dev/.well-known/llms.txt`
- `https://chudi.dev/.well-known/llms.json`

## Site Structure

- `https://chudi.dev/start`
- `https://chudi.dev/topics`
- `https://chudi.dev/about`

## Implementation Proof

- `https://chudi.dev/blog/webmcp-sveltekit-implementation`
- `https://chudi.dev/blog/llms-txt-robots-txt-for-ai-crawlers`

These are not abstract claims. They map directly to live public pages and machine-readable endpoints.

## Verification

This repo includes a runnable audit for these surfaces:

```bash
python3 scripts/audit_live_surfaces.py
```
