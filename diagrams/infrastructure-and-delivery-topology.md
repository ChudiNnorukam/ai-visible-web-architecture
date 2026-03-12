# Target State Infrastructure and Delivery Topology

```mermaid
flowchart LR
    SRC["Inferred: content / metadata source"]
    BUILD["Inferred: app build system"]
    EDGE["Verified / inferred mix: public site delivery edge"]
    PAGE["Verified: public pages"]
    DISC["Verified: discovery files and llms.json"]
    TOOL["Verified / inferred mix: WebMCP browser tools"]
    REPO["Verified: public reference repo"]
    CI["Target State: CI and scheduled audits"]
    MON["Target State: monitoring and drift review"]

    SRC --> BUILD
    BUILD --> EDGE
    EDGE --> PAGE
    EDGE --> DISC
    EDGE --> TOOL
    REPO --> CI
    CI --> MON
    PAGE --> MON
    DISC --> MON
    TOOL --> MON
```

- This is a target-state operating topology rather than a claim about hidden infrastructure details.
- It visualizes the control loop between the live site, the public repo, and the verification system.
- The repo becomes part of the operational system by documenting and checking the contract.
