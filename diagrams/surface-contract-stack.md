# Verified Surface Contract Stack

```mermaid
flowchart TB
    C["Verified: Content Layer<br/>pages, posts, topic hubs"]
    M["Verified: Machine-Readable Layer<br/>schema, llms.txt, llms-full.txt, ai.txt, llms.json"]
    A["Verified: Agent Layer<br/>browser-side WebMCP proof surface"]
    D["Verified: Discovery and Consumption Layer<br/>search, retrieval, citation, agent workflows"]

    C --> M --> A --> D
```

- The stack shows how the repo frames `chudi.dev` as more than a page collection.
- The machine-readable layer mediates between visible content and downstream retrieval systems.
- The agent layer builds on the same public authority rather than replacing it.
