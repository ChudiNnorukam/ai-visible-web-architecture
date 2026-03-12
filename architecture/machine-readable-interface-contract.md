# Machine-Readable Interface Contract

> Evidence boundary: this document defines the repository's expected contract for public machine-readable surfaces. Contract items backed by live endpoints are verified; recommended extensions are marked target state.

## Verified Public Interfaces

### `llms.txt`

- role: short-form site discovery and priority navigation
- expected behaviors:
  - exposes key site sections
  - points at richer machine-readable endpoints
  - provides enough context for retrieval systems to orient quickly

### `llms-full.txt`

- role: expanded retrieval context and full-content specimen
- expected behaviors:
  - includes author, topic, permissions, and extended content context
  - provides a denser retrieval surface than `llms.txt`

### `ai.txt`

- role: policy and crawler guidance
- expected behaviors:
  - states broad access expectations
  - points at preferred machine-readable resources
  - communicates citation preference

### `.well-known/llms.json`

- role: structured machine-readable metadata
- expected verified keys:
  - `site`
  - `author`
  - `keyTopics`
  - `bestPages`
  - `endpoints`
  - `policies`
  - `recentPosts`

### WebMCP / browser tools

- role: direct agent interface surface
- verified claim:
  - the site publishes first-party documentation of browser-side WebMCP tooling
- target-state extension:
  - public tool manifests and schemas versioned as explicit machine contracts

## Contract Rule

These interfaces should agree on core identity, preferred endpoints, and attribution requirements. When one changes, the verification layer must be updated in the same repository change.
