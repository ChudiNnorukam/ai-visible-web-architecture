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
- WebMCP tools for direct agent queries

That combination turns the site into more than a blog. It behaves like a knowledge base, a machine-readable identity node, and an interface layer for agents.

## Design Principle

The same source of truth should support:

- navigation for humans
- extraction for LLMs
- callable context for agents

If those surfaces diverge, the public artifact becomes inconsistent. If they stay aligned, the site becomes easier to trust and easier to cite.
