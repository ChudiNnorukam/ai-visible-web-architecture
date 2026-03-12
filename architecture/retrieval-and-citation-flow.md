# Retrieval and Citation Flow

> Evidence boundary: this doc explains the observable retrieval pattern using public site surfaces and does not claim access to private ranking or application internals.

## Goal

Explain how an AI-visible website moves from a user question to an attributable answer.

## Flow

1. A user or agent asks a question.
2. The retrieval system identifies relevant site surfaces.
3. The site exposes clear passages, metadata, and entity context.
4. The model answers with stronger grounding and a clearer citation path.

## Why This Matters

If the only access path is page presentation, AI systems fall back to brittle extraction. Retrieval-aware information design improves answer quality by making authoritative passages easier to find and easier to attribute.

## Applied to chudi.dev

On `chudi.dev`, this flow is supported by:

- topic hubs for orientation
- answer-ready article structures
- `llms.txt` and related discovery files
- consistent author and site identity metadata
