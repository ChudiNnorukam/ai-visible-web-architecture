# Theory-to-Implementation Map

```mermaid
flowchart TB
    T1["Theory: Retrieval-aware information design"]
    T2["Theory: Machine-readable identity and discovery"]
    T3["Theory: Agent-facing interface layer"]

    I1["Verified: topic hubs, answer-ready writing, proof docs"]
    I2["Verified: llms.txt, llms-full.txt, ai.txt, llms.json"]
    I3["Verified: WebMCP implementation article and public tooling claim"]

    T1 --> I1
    T2 --> I2
    T3 --> I3
```

- This diagram is the bridge between the whitepaper and the live public implementation.
- Each theory layer is mapped to a concrete `chudi.dev` artifact the repo can point at.
- It keeps the repo anchored in evidence while still explaining the larger pattern.
