# Verified Agent Query Sequence

```mermaid
sequenceDiagram
    participant A as Agent
    participant D as "Verified: discovery surfaces"
    participant T as "Verified: WebMCP proof surface"
    participant S as "Verified: chudi.dev"

    A->>D: Inspect llms and AI metadata
    A->>T: Select an agent-capable interface
    T->>S: Query site-backed context
    S-->>T: Return grounded result
    T-->>A: Return callable context
    A-->>A: Synthesize answer or next action
```

- This diagram stays close to what is publicly evidenced: discovery, a documented WebMCP layer, and site-backed results.
- It avoids claiming private tool implementation details that are not visible from the repo.
- The agent layer is useful because it reduces the need for UI scraping.
