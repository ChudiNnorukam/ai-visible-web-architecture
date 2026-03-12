# Verified Identity Graph

```mermaid
flowchart LR
    AUTHOR["Verified: Chudi Nnorukam"]
    SITE["Verified: chudi.dev"]
    ABOUT["Verified: /about"]
    TOPICS["Verified: keyTopics / topic hubs"]
    POSTS["Verified: bestPages / recentPosts"]
    PRODUCTS["Verified: products and portfolio pages"]
    EXT["Verified: external profile links"]

    AUTHOR --> SITE
    AUTHOR --> ABOUT
    SITE --> TOPICS
    SITE --> POSTS
    SITE --> PRODUCTS
    AUTHOR --> EXT
```

- The identity graph shows how the site can be treated as a coherent knowledge node instead of a disconnected archive.
- The node set is derived from public metadata and public pages, not hidden internals.
- This is the minimum shape needed for machine-readable identity and authority concentration.
