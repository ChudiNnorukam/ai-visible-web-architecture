# Research and Evidence Rules

This document turns the repository’s capability profile into contribution rules.

Use it whenever you add, revise, or generalize claims about search visibility, machine-readable identity, retrieval, agent interoperability, performance, or verification.

## When Fresh Source Verification Is Required

Re-check sources before writing or changing guidance when the topic is likely to drift:

- search engine documentation and supported structured-data behavior
- Core Web Vitals and performance guidance
- MCP and agent interoperability contracts
- discovery-surface conventions such as `llms.txt`
- GitHub Actions behavior, branch protection rules, or security settings

If the topic could have changed recently, verify it again instead of relying on repo memory.

## Topics That Must Be Treated as Temporally Unstable

These topics are not safe to treat as timeless:

- Google Search support boundaries
- structured-data feature support in search results
- Core Web Vitals scoring guidance
- agent tooling and protocol documentation
- GitHub Actions marketplace behavior and runtime support

For these, prefer current official documentation over older examples or intuition.

## Evidence Labels

Use the repository’s truth labels consistently:

- `Verified`: backed by a live public surface, executable check, or directly inspectable artifact
- `Inferred`: reasoned interpretation based on evidence, but not directly proven from public surfaces
- `Target State`: recommended future operating model or architecture

If a sentence could be mistaken for a verified fact, label it or rephrase it.

## Citation Rules for Repo Prose

- Prefer official docs, standards bodies, and primary-source protocol documentation.
- Cite the source that actually governs the claim, not a nearby commentary source.
- When documenting a search behavior or support claim, favor the product owner’s own docs.
- When documenting vocabulary semantics, use the vocabulary reference.
- When documenting protocol expectations, use the protocol’s own source if it exists.

## When To Add Verification Instead of More Prose

Add or extend a script or workflow when a claim is:

- central to the repo’s trust model
- based on a live public surface that can drift
- simple enough to validate mechanically
- likely to be repeated across docs

Do not add verification when the claim is inherently interpretive and cannot be meaningfully automated.

## Contribution Workflow Rules

Before making an architectural claim:

1. check whether a higher-priority source already governs it
2. determine whether the claim is verified, inferred, or target state
3. update proof or verification material if the claim depends on a live surface
4. update examples when a public contract changes

## Common Failure Patterns

- citing secondary commentary when official docs exist
- implying support where only vocabulary exists
- adding future-state architecture without labeling it
- writing repo prose that cannot be tied to a live surface, a standard, or a clearly marked recommendation
- claiming performance quality without measurement or cited guidance

## Companion Docs

- [Agent Capability Profile](./agent-capability-profile.md)
- [Agent Standards Pack](./agent-standards-pack.md)
- [GitHub Repository Configuration](./github-repository-configuration.md)
