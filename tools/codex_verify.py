#!/usr/bin/env python3
"""
codex_verify.py — Read-only drift detector + INDEX.json rebuilder for the
citability-dev knowledge codex (docs/codex/).

The codex is a directory of YAML-fronted markdown nodes. Each node declares
one or more `code_refs`, each pointing at a path + line range in the repo.
This script:

  1. Reads each node's frontmatter.
  2. For each code_ref, computes sha256 of the slice <path>:<lines>.
  3. Compares to the stored sha256.
     - First time (sha256: null)        → write the hash, mark "fresh".
     - Hash matches                     → mark "ok", bump last_verified.
     - Hash differs                     → mark DRIFT, leave the node alone
                                          (human ratifies semantic shifts).
  4. Optionally rebuilds docs/codex/INDEX.json (term → node id map keyed by
     id + every alias).

Exit codes:
  0  — all walked nodes verified clean (or rebuild succeeded)
  1  — one or more nodes had DRIFT (informational; not a crash)
  2  — invocation error (bad path, missing node id, parse failure, etc.)

Usage:
  python3 tools/codex_verify.py --node <id>     # verify one node
  python3 tools/codex_verify.py --all           # verify every node
  python3 tools/codex_verify.py --rebuild-index # regenerate INDEX.json
  python3 tools/codex_verify.py                 # default: --all

Design notes:
  * No external deps. Stdlib only — the verifier must run in any Python 3.9+
    environment without `pip install`. YAML frontmatter is parsed by a small
    hand-rolled reader (we only need the flat-key + simple-list cases that
    the node convention uses).
  * "DRIFT" is informational, not fatal. The point of the codex is that a
    human ratifies semantic changes; the verifier just surfaces them.
  * `last_verified` is only bumped on a clean verify, NOT on first-write.
    First-write writes the hash and sets `last_verified` to today as well —
    they're indistinguishable from the consumer's POV.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# ──────────────────────────────────────────────────────────────────────────────
# Paths
# ──────────────────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
CODEX_DIR = REPO_ROOT / "docs" / "codex"
NODES_DIR = CODEX_DIR / "nodes"
INDEX_PATH = CODEX_DIR / "INDEX.json"
DOMAINS_PATH = CODEX_DIR / "domains.yaml"

# ──────────────────────────────────────────────────────────────────────────────
# Tiny YAML frontmatter parser
# ──────────────────────────────────────────────────────────────────────────────
#
# We deliberately do NOT use PyYAML. The node convention is small enough that
# a 60-line parser covers it and the verifier stays dependency-free.
# Supported shapes:
#
#     key: scalar           # string/int/null/bool
#     key: [a, b, c]        # flow list of scalars
#     key:                  # block list
#       - scalar
#       - scalar
#     key:                  # block list of mappings
#       - subkey: value
#         subkey: value
#
# That's all the schema needs.

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def _coerce_scalar(raw: str) -> Any:
    s = raw.strip()
    if s == "" or s.lower() == "null" or s == "~":
        return None
    if s.lower() == "true":
        return True
    if s.lower() == "false":
        return False
    # Quoted string
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    # Int
    try:
        return int(s)
    except ValueError:
        pass
    return s


def _parse_flow_list(raw: str) -> list:
    inner = raw.strip()
    if not (inner.startswith("[") and inner.endswith("]")):
        raise ValueError(f"expected flow list, got: {raw!r}")
    body = inner[1:-1].strip()
    if not body:
        return []
    return [_coerce_scalar(part) for part in body.split(",")]


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError("no YAML frontmatter found")
    body = m.group(1)
    lines = body.split("\n")

    out: dict = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue

        # Top-level key: ...
        if not line.startswith(" ") and ":" in line:
            key, _, rest = line.partition(":")
            key = key.strip()
            rest_stripped = rest.strip()

            # Inline value
            if rest_stripped:
                if rest_stripped.startswith("["):
                    out[key] = _parse_flow_list(rest_stripped)
                else:
                    out[key] = _coerce_scalar(rest_stripped)
                i += 1
                continue

            # Block list follows
            children: list = []
            i += 1
            while i < len(lines):
                child = lines[i]
                if not child.strip():
                    i += 1
                    continue
                if not child.startswith(" "):
                    break  # back to top-level
                stripped = child.lstrip()
                if stripped.startswith("- "):
                    item_first = stripped[2:]
                    # List of mappings: "- key: value" then more "  key: value"
                    if ":" in item_first and not item_first.startswith("[") and not item_first.startswith('"'):
                        sub_key, _, sub_val = item_first.partition(":")
                        item: dict = {sub_key.strip(): _coerce_scalar(sub_val)}
                        i += 1
                        # Slurp continuation lines (deeper indent, no leading "-")
                        while i < len(lines):
                            cont = lines[i]
                            if not cont.strip():
                                i += 1
                                continue
                            if not cont.startswith("    "):
                                break
                            c_stripped = cont.lstrip()
                            if c_stripped.startswith("- "):
                                break
                            sk, _, sv = c_stripped.partition(":")
                            item[sk.strip()] = _coerce_scalar(sv)
                            i += 1
                        children.append(item)
                    else:
                        children.append(_coerce_scalar(item_first))
                        i += 1
                else:
                    # Indented continuation we don't understand → skip
                    i += 1
            out[key] = children
            continue
        i += 1
    return out


def serialize_frontmatter(data: dict) -> str:
    """Round-trip the small subset we parse. Preserves key order from `data`."""
    out_lines: list[str] = []
    for key, val in data.items():
        if isinstance(val, list) and val and isinstance(val[0], dict):
            out_lines.append(f"{key}:")
            for item in val:
                first = True
                for sk, sv in item.items():
                    prefix = "  - " if first else "    "
                    out_lines.append(f"{prefix}{sk}: {_dump_scalar(sv)}")
                    first = False
        elif isinstance(val, list):
            inner = ", ".join(_dump_scalar(v) for v in val)
            out_lines.append(f"{key}: [{inner}]")
        else:
            out_lines.append(f"{key}: {_dump_scalar(val)}")
    return "\n".join(out_lines)


def _dump_scalar(v: Any) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    s = str(v)
    # Quote if contains characters that would confuse our reader
    if any(c in s for c in [":", "#", "[", "]"]) and not s.startswith('"'):
        return f'"{s}"'
    return s


# ──────────────────────────────────────────────────────────────────────────────
# Node model
# ──────────────────────────────────────────────────────────────────────────────


@dataclass
class CodeRef:
    path: str
    lines: str            # "A-B" or "A"
    sha256: str | None    # hex digest of the slice; null until first verify


@dataclass
class Node:
    id: str
    name: str
    domain: str
    aliases: list[str] = field(default_factory=list)
    code_refs: list[CodeRef] = field(default_factory=list)
    related: list[str] = field(default_factory=list)
    parent_concepts: list[str] = field(default_factory=list)
    child_concepts: list[str] = field(default_factory=list)
    last_verified: str | None = None
    confidence: str = "inferred"
    ratified: str | None = None
    body: str = ""
    file_path: Path = field(default_factory=Path)


def load_node(node_path: Path) -> Node:
    text = node_path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    body = FRONTMATTER_RE.sub("", text, count=1)

    refs = []
    for raw in fm.get("code_refs") or []:
        refs.append(CodeRef(
            path=str(raw.get("path", "")),
            lines=str(raw.get("lines", "")),
            sha256=raw.get("sha256"),
        ))

    return Node(
        id=str(fm.get("id", node_path.stem)),
        name=str(fm.get("name", "")),
        domain=str(fm.get("domain", "")),
        aliases=list(fm.get("aliases") or []),
        code_refs=refs,
        related=list(fm.get("related") or []),
        parent_concepts=list(fm.get("parent_concepts") or []),
        child_concepts=list(fm.get("child_concepts") or []),
        last_verified=fm.get("last_verified"),
        confidence=str(fm.get("confidence") or "inferred"),
        ratified=fm.get("ratified"),
        body=body,
        file_path=node_path,
    )


def write_node(node: Node) -> None:
    fm = {
        "id": node.id,
        "name": node.name,
        "domain": node.domain,
        "aliases": node.aliases,
        "code_refs": [
            {"path": r.path, "lines": r.lines, "sha256": r.sha256}
            for r in node.code_refs
        ],
        "related": node.related,
        "parent_concepts": node.parent_concepts,
        "child_concepts": node.child_concepts,
        "last_verified": node.last_verified,
        "confidence": node.confidence,
    }
    if node.ratified:
        fm["ratified"] = node.ratified
    fm_text = serialize_frontmatter(fm)
    body = node.body.lstrip("\n")
    node.file_path.write_text(f"---\n{fm_text}\n---\n\n{body}", encoding="utf-8")


# ──────────────────────────────────────────────────────────────────────────────
# sha256 over a path:lines slice
# ──────────────────────────────────────────────────────────────────────────────


def _parse_lines(spec: str) -> tuple[int, int]:
    s = str(spec).strip().strip('"').strip("'")
    if "-" in s:
        a, b = s.split("-", 1)
        return int(a), int(b)
    n = int(s)
    return n, n


def hash_slice(repo_root: Path, ref: CodeRef) -> str:
    f = repo_root / ref.path
    if not f.exists():
        raise FileNotFoundError(f"code_ref path missing: {ref.path}")
    start, end = _parse_lines(ref.lines)
    lines = f.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
    # 1-indexed, inclusive
    chunk = "".join(lines[start - 1:end])
    return hashlib.sha256(chunk.encode("utf-8")).hexdigest()


# ──────────────────────────────────────────────────────────────────────────────
# Verify
# ──────────────────────────────────────────────────────────────────────────────


def verify_node(node: Node) -> tuple[str, list[str]]:
    """Return (status, messages). status ∈ {"ok", "drift", "fresh", "missing"}."""
    if not node.code_refs:
        return "ok", [f"{node.id}: no code_refs (concept-only node)"]

    msgs: list[str] = []
    drift = False
    fresh_writes = 0

    for ref in node.code_refs:
        try:
            actual = hash_slice(REPO_ROOT, ref)
        except FileNotFoundError as e:
            msgs.append(f"  MISSING {ref.path}:{ref.lines} — {e}")
            return "missing", msgs

        if ref.sha256 is None:
            ref.sha256 = actual
            fresh_writes += 1
            msgs.append(f"  FRESH   {ref.path}:{ref.lines}  → {actual[:12]}…")
        elif ref.sha256 == actual:
            msgs.append(f"  ok      {ref.path}:{ref.lines}")
        else:
            drift = True
            msgs.append(
                f"  DRIFT   {ref.path}:{ref.lines}\n"
                f"            stored: {ref.sha256[:12]}…\n"
                f"            actual: {actual[:12]}…"
            )

    today = datetime.date.today().isoformat()
    if drift:
        return "drift", msgs

    # Clean verify (or first-write): bump last_verified, persist any fresh hashes.
    node.last_verified = today
    if fresh_writes > 0:
        write_node(node)
        return "fresh", msgs
    write_node(node)
    return "ok", msgs


# ──────────────────────────────────────────────────────────────────────────────
# INDEX.json builder
# ──────────────────────────────────────────────────────────────────────────────


def rebuild_index() -> dict:
    """
    INDEX.json shape:
      {
        "generated_at": "<iso>",
        "node_count": <int>,
        "domains": { "<domain>": ["<id>", ...] },
        "terms":    { "<term>": "<id>" }    # id + every alias collapsed to one map
      }
    """
    nodes = [load_node(p) for p in sorted(NODES_DIR.glob("*.md"))]
    by_domain: dict[str, list[str]] = {}
    terms: dict[str, str] = {}
    collisions: list[str] = []

    for n in nodes:
        by_domain.setdefault(n.domain, []).append(n.id)

        for term in [n.id, *n.aliases]:
            key = term.lower()
            if key in terms and terms[key] != n.id:
                collisions.append(f"{term!r}: {terms[key]} vs {n.id}")
            terms[key] = n.id

    if collisions:
        print("WARN alias collisions (last write wins):", file=sys.stderr)
        for c in collisions:
            print(f"  {c}", file=sys.stderr)

    index = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "node_count": len(nodes),
        "domains": {k: sorted(v) for k, v in sorted(by_domain.items())},
        "terms": dict(sorted(terms.items())),
    }
    INDEX_PATH.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    return index


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────


def find_node_by_id(node_id: str) -> Node | None:
    direct = NODES_DIR / f"{node_id}.md"
    if direct.exists():
        return load_node(direct)
    # Fallback: scan all nodes for matching frontmatter id (handles renamed files).
    for p in NODES_DIR.glob("*.md"):
        n = load_node(p)
        if n.id == node_id:
            return n
    return None


def update_index_for_nodes(node_ids: list[str]) -> dict:
    """Incremental INDEX update: just refresh entries for the named nodes.
    O(k) where k = nodes touched, vs O(N) full rebuild. Falls back to full
    rebuild if INDEX.json doesn't exist or is corrupt."""
    if not INDEX_PATH.exists():
        return rebuild_index()
    try:
        idx = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return rebuild_index()

    by_domain = {k: list(v) for k, v in idx.get("domains", {}).items()}
    terms = dict(idx.get("terms", {}))

    for node_id in node_ids:
        node = find_node_by_id(node_id)
        if node is None:
            # Node was deleted: strip any references
            for d in list(by_domain.keys()):
                if node_id in by_domain[d]:
                    by_domain[d].remove(node_id)
                if not by_domain[d]:
                    del by_domain[d]
            terms = {k: v for k, v in terms.items() if v != node_id}
            continue
        # Strip prior entries for this node from any domain bucket (it may have moved)
        for d in list(by_domain.keys()):
            if node_id in by_domain[d]:
                by_domain[d].remove(node_id)
            if not by_domain[d]:
                del by_domain[d]
        # Strip prior term entries for this node (alias may have changed)
        terms = {k: v for k, v in terms.items() if v != node_id}
        # Insert fresh entries
        by_domain.setdefault(node.domain, []).append(node.id)
        for term in [node.id, *node.aliases]:
            terms[term.lower()] = node.id

    new_idx = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "node_count": sum(len(v) for v in by_domain.values()),
        "domains": {k: sorted(v) for k, v in sorted(by_domain.items())},
        "terms": dict(sorted(terms.items())),
    }
    INDEX_PATH.write_text(json.dumps(new_idx, indent=2) + "\n", encoding="utf-8")
    return new_idx


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify or rebuild the citability-dev knowledge codex.")
    ap.add_argument("--node", help="Verify a single node by id (e.g. v-score)")
    ap.add_argument("--nodes", help="Verify multiple nodes by id (comma-separated). Single subprocess; eliminates per-node Python startup cost. Use this in walks.")
    ap.add_argument("--all", action="store_true", help="Verify every node (default if no flag)")
    ap.add_argument("--rebuild-index", action="store_true", help="(Re)generate docs/codex/INDEX.json (full O(N) walk)")
    ap.add_argument("--update-index", help="Incremental INDEX update for one or more node ids (comma-separated). O(k) instead of O(N).")
    ap.add_argument("--quiet", action="store_true", help="Output only summary line (counts) + drift/missing ids. Cuts harness token cost ~80%% on clean walks.")
    args = ap.parse_args()

    if not CODEX_DIR.exists():
        print(f"codex not found at {CODEX_DIR}", file=sys.stderr)
        return 2

    if args.rebuild_index:
        idx = rebuild_index()
        print(f"INDEX.json: {idx['node_count']} nodes, "
              f"{len(idx['domains'])} domains, {len(idx['terms'])} terms")
        return 0

    if args.update_index:
        ids = [s.strip() for s in args.update_index.split(",") if s.strip()]
        idx = update_index_for_nodes(ids)
        print(f"INDEX.json (incremental, {len(ids)} touched): {idx['node_count']} nodes total")
        return 0

    targets: list[Node]
    if args.nodes:
        ids = [s.strip() for s in args.nodes.split(",") if s.strip()]
        targets = []
        for nid in ids:
            n = find_node_by_id(nid)
            if n is None:
                print(f"unknown node: {nid}", file=sys.stderr)
                return 2
            targets.append(n)
    elif args.node:
        node = find_node_by_id(args.node)
        if node is None:
            print(f"unknown node: {args.node}", file=sys.stderr)
            return 2
        targets = [node]
    else:
        targets = [load_node(p) for p in sorted(NODES_DIR.glob("*.md"))]
        if not targets:
            print(f"no nodes found in {NODES_DIR}", file=sys.stderr)
            return 2

    any_drift = False
    counts = {"ok": 0, "fresh": 0, "drift": 0, "missing": 0}
    drift_ids: list[str] = []
    missing_ids: list[str] = []

    for n in targets:
        status, msgs = verify_node(n)
        counts[status] += 1
        if status == "drift":
            drift_ids.append(n.id)
            any_drift = True
        elif status == "missing":
            missing_ids.append(n.id)
            any_drift = True

        if not args.quiet:
            flag = {
                "ok":      "OK   ",
                "fresh":   "FRESH",
                "drift":   "DRIFT",
                "missing": "MISS ",
            }[status]
            print(f"[{flag}] {n.id}")
            for m in msgs:
                print(m)

    if args.quiet:
        # Compact summary: ok/fresh counts + drift/missing ids only
        summary = f"verified={counts['ok']+counts['fresh']} drift={counts['drift']} missing={counts['missing']}"
        if drift_ids:
            summary += f" drift_ids=[{','.join(drift_ids)}]"
        if missing_ids:
            summary += f" missing_ids=[{','.join(missing_ids)}]"
        print(summary)

    return 1 if any_drift else 0


if __name__ == "__main__":
    sys.exit(main())
