# Agent Interface Layer

## Goal

Make a website usable by agents without forcing them to screen-scrape the interface.

## Pattern

An agent interface layer exposes structured capabilities directly from the site. Those capabilities should be:

- discoverable
- narrow in scope
- typed or schema-backed
- grounded in the same source of truth as the visible site

## Applied to chudi.dev

`chudi.dev` exposes live WebMCP browser tools for:

- searching posts
- listing posts
- returning author context

This reduces ambiguity for agents and turns the site into a callable system, not just a page surface.
