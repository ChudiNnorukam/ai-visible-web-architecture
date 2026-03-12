# Contributing

Thanks for contributing to `ai-visible-web-architecture`.

This repository documents a live public system and a generalized pattern derived from it. The main contribution rule is simple: keep the boundary between verified evidence and interpretation explicit.

## Before You Open a PR

1. Read [README.md](./README.md), [proof/live-surfaces.md](./proof/live-surfaces.md), and [proof/live-audit.md](./proof/live-audit.md).
2. Confirm whether your change is:
   - `Verified`: grounded in live public surfaces or runnable checks
   - `Inferred`: a reasoned interpretation of the system
   - `Target State`: a recommended future operating model
3. If you add or change a claim about `chudi.dev`, update the proof or verification docs in the same change.

## Contribution Standards

- Prefer small, reviewable pull requests.
- Keep prose concrete and technically defensible.
- Add or update verification when a public claim changes.
- Use Markdown and Mermaid that render cleanly on GitHub.
- Do not commit secrets, tokens, or environment-specific credentials.

## Local Checks

Run these before opening a PR:

```bash
python3 -m py_compile scripts/*.py
python3 scripts/check_repo_quality.py
python3 scripts/audit_live_surfaces.py
```

## Pull Request Expectations

Every PR should explain:

- what changed
- whether the change affects verified, inferred, or target-state content
- how the change was checked

If a change cannot be verified locally, note that explicitly in the PR description.
