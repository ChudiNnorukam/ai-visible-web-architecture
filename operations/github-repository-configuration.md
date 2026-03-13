# GitHub Repository Configuration

This document captures the repository settings that must be configured in GitHub's UI because they are not stored in the git tree.

## Recommended Repository Metadata

- Description: `Public reference architecture for building AI-visible websites, using chudi.dev as the live case study.`
- Website: `https://chudi.dev`
- Topics:
  - `ai-visible-web`
  - `llms-txt`
  - `webmcp`
  - `machine-readable-identity`
  - `retrieval`
  - `citation`
  - `aeo`
  - `technical-writing`
  - `sveltekit`

## Social Preview

- Preferred asset: `assets/social-preview.svg`
- Fallback export target: 1280x640 PNG generated from the SVG source

## Branch Protection

Active policy for `main`:

- require pull request review before merge
- require status checks to pass before merge
- include `public-repo-quality` as a required check
- require conversation resolution before merge
- enforce the rules for administrators
- block force pushes
- block deletion of `main`

## Emergency Changes

Admin bypass is for emergencies only.

Normal repository maintenance should happen through:

1. a branch
2. a pull request
3. a green `public-repo-quality` run
4. a merge through the PR path

## Security Settings

Enable in GitHub if available:

- secret scanning
- push protection
- dependency graph
- Dependabot alerts

The repository itself is intentionally dependency-light, but the security posture should still be explicit.
