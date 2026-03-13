#!/usr/bin/env python3
"""Audit the live public surfaces that back this repository's claims."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

BASE_URL = "https://chudi.dev"
TIMEOUT_SECONDS = 15
SITEMAP_URL = f"{BASE_URL}/sitemap.xml"
SITEMAP_NAMESPACE = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

TEXT_CONTENT_TYPES = ("text/plain", "text/markdown", "application/octet-stream")
HTML_CONTENT_TYPES = ("text/html",)
JSON_CONTENT_TYPES = ("application/json", "text/json")
XML_CONTENT_TYPES = ("application/xml", "text/xml")

SURFACE_CHECKS = [
    {
        "name": "llms.txt",
        "url": f"{BASE_URL}/llms.txt",
        "expected_types": TEXT_CONTENT_TYPES,
    },
    {
        "name": "llms-full.txt",
        "url": f"{BASE_URL}/llms-full.txt",
        "expected_types": TEXT_CONTENT_TYPES,
    },
    {
        "name": "ai.txt",
        "url": f"{BASE_URL}/ai.txt",
        "expected_types": TEXT_CONTENT_TYPES,
    },
    {
        "name": ".well-known/llms.txt",
        "url": f"{BASE_URL}/.well-known/llms.txt",
        "expected_types": TEXT_CONTENT_TYPES,
    },
    {
        "name": ".well-known/llms.json",
        "url": f"{BASE_URL}/.well-known/llms.json",
        "expected_types": JSON_CONTENT_TYPES,
    },
    {
        "name": "sitemap.xml",
        "url": SITEMAP_URL,
        "expected_types": XML_CONTENT_TYPES,
    },
    {
        "name": "start",
        "url": f"{BASE_URL}/start",
        "expected_types": HTML_CONTENT_TYPES,
    },
    {
        "name": "topics",
        "url": f"{BASE_URL}/topics",
        "expected_types": HTML_CONTENT_TYPES,
    },
    {
        "name": "about",
        "url": f"{BASE_URL}/about",
        "expected_types": HTML_CONTENT_TYPES,
    },
    {
        "name": "webmcp implementation article",
        "url": f"{BASE_URL}/blog/webmcp-sveltekit-implementation",
        "expected_types": HTML_CONTENT_TYPES,
    },
    {
        "name": "llms article",
        "url": f"{BASE_URL}/blog/llms-txt-robots-txt-for-ai-crawlers",
        "expected_types": HTML_CONTENT_TYPES,
    },
]

EXPECTED_LLMSTXT_MARKERS = (
    f"{BASE_URL}/start",
    f"{BASE_URL}/topics",
    f"{BASE_URL}/about",
    f"{BASE_URL}/.well-known/llms.json",
    f"{BASE_URL}/llms-full.txt",
)

EXPECTED_AITXT_MARKERS = (
    "Allow: /",
    f"Contact: {BASE_URL}/about",
    f"See: {BASE_URL}/.well-known/llms.json",
    "Please cite original article URLs",
)

EXPECTED_LLMS_JSON_KEYS = ("site", "author", "endpoints", "policies")
EXPECTED_ENDPOINTS = {
    "llmsTxt": f"{BASE_URL}/llms.txt",
    "llmsWellKnown": f"{BASE_URL}/.well-known/llms.txt",
    "llmsFullTxt": f"{BASE_URL}/llms-full.txt",
    "aiTxt": f"{BASE_URL}/ai.txt",
    "rss": f"{BASE_URL}/rss.xml",
    "sitemap": SITEMAP_URL,
}
EXPECTED_SITEMAP_URLS = (
    BASE_URL + "/",
    f"{BASE_URL}/blog",
    f"{BASE_URL}/about",
    f"{BASE_URL}/resources",
    f"{BASE_URL}/products",
    f"{BASE_URL}/portfolio",
)
EXPECTED_WEBMCP_MARKERS = (
    "navigator.modelContext",
    "searchPosts",
    "listPosts",
    "getAuthorContext",
)

RESULTS: list[dict[str, object]] = []


def record(name: str, ok: bool, details: str, url: str | None = None) -> None:
    status = "PASS" if ok else "FAIL"
    print(f"{status} {name}: {details}")
    entry: dict[str, object] = {"name": name, "ok": ok, "details": details}
    if url:
        entry["url"] = url
    RESULTS.append(entry)


def normalize_content_type(content_type: str | None) -> str:
    if not content_type:
        return ""
    return content_type.split(";", 1)[0].strip().lower()


def fetch(url: str) -> tuple[int, str, bytes]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "ai-visible-web-architecture-audit/1.0",
            "Accept": "*/*",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            status = response.getcode()
            content_type = normalize_content_type(response.headers.get("Content-Type"))
            body = response.read()
    except urllib.error.HTTPError as exc:
        fail(f"{url} returned HTTP {exc.code}")
    except urllib.error.URLError as exc:
        fail(f"{url} was unreachable: {exc.reason}")

    return status, content_type, body


def ensure_surface_contract() -> None:
    for check in SURFACE_CHECKS:
        try:
            status, content_type, _ = fetch(check["url"])
        except SystemExit:
            record(check["name"], False, "endpoint fetch failed", check["url"])
            continue
        expected_types = check["expected_types"]
        ok = status == 200 and content_type in expected_types
        expected = ", ".join(expected_types)
        details = f"{status} {content_type}; expected one of: {expected}"
        record(check["name"], ok, details, check["url"])


def ensure_llms_txt_has_key_markers() -> None:
    _, _, body = fetch(f"{BASE_URL}/llms.txt")
    text = body.decode("utf-8", errors="replace")
    missing = []
    for marker in EXPECTED_LLMSTXT_MARKERS:
        if marker not in text:
            missing.append(marker)
    record(
        "llms.txt markers",
        not missing,
        "all expected markers present" if not missing else f"missing: {', '.join(missing)}",
        f"{BASE_URL}/llms.txt",
    )


def ensure_ai_txt_has_agent_markers() -> None:
    _, _, body = fetch(f"{BASE_URL}/ai.txt")
    text = body.decode("utf-8", errors="replace")
    missing = []
    for marker in EXPECTED_AITXT_MARKERS:
        if marker not in text:
            missing.append(marker)
    record(
        "ai.txt markers",
        not missing,
        "all expected markers present" if not missing else f"missing: {', '.join(missing)}",
        f"{BASE_URL}/ai.txt",
    )


def ensure_llms_json_contract() -> None:
    _, _, body = fetch(f"{BASE_URL}/.well-known/llms.json")
    try:
        payload = json.loads(body)
    except json.JSONDecodeError as exc:
        record(".well-known/llms.json contract", False, f"invalid JSON: {exc}", f"{BASE_URL}/.well-known/llms.json")
        return

    errors = []
    for key in EXPECTED_LLMS_JSON_KEYS:
        if key not in payload:
            errors.append(f"missing top-level key '{key}'")

    site = payload.get("site", {})
    if site.get("url") != BASE_URL:
        errors.append(f"site.url was '{site.get('url')}'")

    endpoints = payload.get("endpoints", {})
    for key, expected in EXPECTED_ENDPOINTS.items():
        if endpoints.get(key) != expected:
            errors.append(f"endpoints.{key} was '{endpoints.get(key)}'")

    policies = payload.get("policies", {})
    if policies.get("attribution") != "required":
        errors.append("policies.attribution was not 'required'")

    record(
        ".well-known/llms.json contract",
        not errors,
        "contract matches expected keys and values" if not errors else "; ".join(errors),
        f"{BASE_URL}/.well-known/llms.json",
    )


def ensure_sitemap_contract() -> None:
    _, _, body = fetch(SITEMAP_URL)
    try:
        root = ET.fromstring(body.decode("utf-8", errors="replace"))
    except ET.ParseError as exc:
        record("sitemap coverage", False, f"invalid XML: {exc}", SITEMAP_URL)
        return

    urls = {node.text for node in root.findall("sm:url/sm:loc", SITEMAP_NAMESPACE) if node.text}
    missing = [url for url in EXPECTED_SITEMAP_URLS if url not in urls]
    detail = f"{len(urls)} URLs indexed"
    if missing:
        detail += f"; missing expected URLs: {', '.join(missing)}"
    record("sitemap coverage", not missing, detail, SITEMAP_URL)


def ensure_webmcp_proof_contract() -> None:
    url = f"{BASE_URL}/blog/webmcp-sveltekit-implementation"
    _, _, body = fetch(url)
    text = body.decode("utf-8", errors="replace")
    missing = [marker for marker in EXPECTED_WEBMCP_MARKERS if marker not in text]
    detail = (
        "proof article contains expected WebMCP markers"
        if not missing
        else f"missing markers: {', '.join(missing)}"
    )
    record("webmcp proof markers", not missing, detail, url)


def write_json_report(path: str) -> None:
    payload = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "baseUrl": BASE_URL,
        "summary": {
            "passed": sum(1 for item in RESULTS if item["ok"]),
            "failed": sum(1 for item in RESULTS if not item["ok"]),
        },
        "checks": RESULTS,
    }
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-out", help="Write a machine-readable audit report to this path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    ensure_surface_contract()
    ensure_llms_txt_has_key_markers()
    ensure_ai_txt_has_agent_markers()
    ensure_llms_json_contract()
    ensure_sitemap_contract()
    ensure_webmcp_proof_contract()
    if args.json_out:
        write_json_report(args.json_out)
    failures = sum(1 for item in RESULTS if not item["ok"])
    if failures:
        print(f"FAIL live audit completed with {failures} failing checks")
        return 1
    print("PASS live audit completed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
