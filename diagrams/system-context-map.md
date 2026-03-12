# Verified System Context Map

```mermaid
flowchart LR
    HR["Human Readers"]
    SE["Search Engines"]
    LLM["LLM Retrieval Systems"]
    AG["AI Agents"]
    SITE["Verified: chudi.dev"]
    DISC["Verified: llms.txt / ai.txt / llms-full.txt / llms.json"]
    TOOL["Verified: browser-side WebMCP proof surface"]

    HR --> SITE
    SE --> SITE
    LLM --> DISC
    LLM --> SITE
    AG --> DISC
    AG --> TOOL
    TOOL --> SITE
    DISC --> SITE
```

- This is the public system boundary the repo can defend today.
- Humans, search systems, LLM retrieval systems, and agents all touch the same domain through different surfaces.
- The machine-readable and agent-facing layers are not abstract theory here; they are part of the verified public surface set.
