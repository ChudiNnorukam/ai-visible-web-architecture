# AI-Visible Web Architecture

A public case study in building a website for human readers, LLM retrieval, and AI agent interoperability.

This repository documents the technical pattern behind [chudi.dev](https://chudi.dev): a personal website designed to be readable by people, legible to search and AI systems, and queryable by agents.

## Thesis

Most websites are optimized for browsing.

The next layer of the web also needs to support retrieval, citation, and agent interaction. That requires more than a good UI. It requires machine-readable identity, retrieval-aware information design, and explicit interfaces for AI systems.

`chudi.dev` is a live public working model of that approach.

## What Is Already Live on chudi.dev

- `llms.txt`, `llms-full.txt`, and `ai.txt` discovery surfaces
- Structured data and entity clarity for machine-readable identity
- Topic hubs and answer-ready writing designed for retrieval and citation
- Live WebMCP browser tools that expose callable site context to agents

## What This Repo Does

- Generalizes the architecture pattern beyond one personal site
- Separates the implementation into reusable layers
- Documents live proof from `chudi.dev` without pretending the pattern is already standardized everywhere

## Read First

- [whitepaper/the-ai-visible-personal-website.md](./whitepaper/the-ai-visible-personal-website.md)
- [architecture/retrieval-and-citation-flow.md](./architecture/retrieval-and-citation-flow.md)
- [proof/live-surfaces.md](./proof/live-surfaces.md)
- [proof/live-audit.md](./proof/live-audit.md)

## Structure

- `whitepaper/`: concept paper and framing
- `architecture/`: reusable system breakdowns
- `proof/`: evidence grounded in live surfaces on `chudi.dev`
- `examples/`: representative discovery files and schema snippets
- `diagrams/`: simple source-text diagrams for explanation and reuse
- `scripts/`: executable audits for the live surfaces described here

## Verification

Run the live audit to verify that the documented public surfaces still exist and still satisfy the minimum machine-readable contract:

```bash
python3 scripts/audit_live_surfaces.py
```

## Constraint

This repository is deliberately evidence-first. It distinguishes between:

- what is already implemented on `chudi.dev`
- what appears to generalize as a reusable web pattern

That boundary matters. The goal is technical clarity, not category hype.
