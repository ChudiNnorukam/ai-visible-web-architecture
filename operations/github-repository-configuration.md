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

Apply these rules to `main`:

- require pull request review before merge once there is more than one active contributor
- require status checks to pass before merge
- include `public-repo-quality` as a required check
- block force pushes
- block deletion of `main`

## Security Settings

Enable in GitHub if available:

- secret scanning
- push protection
- dependency graph
- Dependabot alerts

The repository itself is intentionally dependency-light, but the security posture should still be explicit.
