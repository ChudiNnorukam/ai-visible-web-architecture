# Verified Retrieval and Citation Sequence

```mermaid
sequenceDiagram
    participant U as User
    participant R as Retrieval System
    participant S as "Verified: chudi.dev surfaces"
    participant M as Model

    U->>R: Ask a question
    R->>S: Discover relevant pages and machine-readable context
    S-->>R: Return passages, metadata, and endpoint context
    R->>M: Provide grounded context
    M-->>U: Answer with attribution path
    U->>S: Click through to source
```

- This sequence captures the retrieval behavior the repo argues for.
- The critical property is not just ranking, but grounded answer generation with a credible citation path.
- Public machine-readable surfaces reduce brittle extraction and improve traceability.
