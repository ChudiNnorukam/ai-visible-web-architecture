# The AI-Visible Personal Website

## Summary

The traditional personal website is optimized for human browsing. The AI-visible personal website is optimized for three simultaneous modes:

- human reading
- LLM retrieval and citation
- AI agent interaction

This paper uses `chudi.dev` as a live case study for how those layers can coexist in one public system.

## Problem

Most websites expose content through presentation alone.

That leaves AI systems to infer structure from pages that were never designed for retrieval or interaction. The result is weaker citations, brittle agent behavior, and a mismatch between what the site knows and what AI systems can actually access.

## Pattern

An AI-visible website adds three technical layers on top of the normal web stack:

1. Retrieval-aware information design
2. Machine-readable identity and discovery
3. Agent-facing interface surfaces

The point is not to replace the visible website. The point is to let one authority graph serve multiple access patterns.

## Case Study: chudi.dev

`chudi.dev` already exposes:

- site-level AI discovery files
- structured entity metadata
- topic hubs for orientation and retrieval
- documented WebMCP tooling for direct agent queries

That combination turns the site into more than a blog. It behaves like a knowledge base, a machine-readable identity node, and an interface layer for agents.

## Design Principle

The same source of truth should support:

- navigation for humans
- extraction for LLMs
- callable context for agents

If those surfaces diverge, the public artifact becomes inconsistent. If they stay aligned, the site becomes easier to trust and easier to cite.

## What This Pattern Does Not Cover

The 3-layer pattern handles the on-site half of AI visibility. It does
not, by itself, address the off-site half: training-data presence
(Wikipedia, Wikidata, Common Crawl, podcast transcripts), backlinks
and referring domain authority, citation evidence (whether models
actually cite the site when asked), or agent-action and
agent-commerce readiness (Stripe Agentic Commerce Protocol, Google
WebMCP).

These layers are documented in companion architecture chapters and in
the entity-and-authority codex node. They are listed as `Target State`
until each chapter ships and is ratified.

## Naming

This pattern is called "AI-Visible Web Architecture." It is not the
same as the "AI Visibility Readiness Framework" (a separate 15-check
audit hosted at `github.com/ChudiNnorukam/ai-visibility-readiness`),
the "AVR Score" used by citability.dev, or the "Agent Readiness"
parallel wedge. See `README.md#vocabulary-and-naming` and
`docs/codex/nodes/naming-canonical-split.md` for the canonical split,
ratified 2026-05-02.
