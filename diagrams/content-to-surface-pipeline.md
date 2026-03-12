# Conceptual Content-to-Surface Pipeline

```mermaid
flowchart LR
    SRC["Inferred: content source of truth"]
    BUILD["Inferred: site build and publishing pipeline"]
    PAGE["Verified: public pages"]
    SCHEMA["Verified / inferred mix: structured metadata"]
    DISC["Verified: llms.txt, llms-full.txt, ai.txt, llms.json"]
    TOOL["Verified / inferred mix: WebMCP browser tools"]
    AUDIT["Target State: automated repo and live audits"]

    SRC --> BUILD
    BUILD --> PAGE
    BUILD --> SCHEMA
    BUILD --> DISC
    BUILD --> TOOL
    PAGE --> AUDIT
    DISC --> AUDIT
    TOOL --> AUDIT
```

- The pipeline explains the pattern, not a fully proven private implementation.
- The important rule is shared derivation: pages, metadata, discovery files, and tools should flow from the same facts.
- The audit loop exists to catch divergence after publication.
