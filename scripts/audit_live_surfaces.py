#!/usr/bin/env python3
"""Audit the live public surfaces that back this repository's claims."""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request

BASE_URL = "https://chudi.dev"
TIMEOUT_SECONDS = 15

TEXT_CONTENT_TYPES = ("text/plain", "text/markdown", "application/octet-stream")
HTML_CONTENT_TYPES = ("text/html",)
JSON_CONTENT_TYPES = ("application/json", "text/json")

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
}


def fail(message: str) -> None:
    print(f"FAIL {message}")
    raise SystemExit(1)


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
        status, content_type, _ = fetch(check["url"])
        if status != 200:
            fail(f"{check['name']} returned HTTP {status}")
        if content_type not in check["expected_types"]:
            expected = ", ".join(check["expected_types"])
            fail(
                f"{check['name']} returned content-type '{content_type}'"
                f" instead of one of: {expected}"
            )
        print(f"PASS {check['name']}: {status} {content_type}")


def ensure_llms_txt_has_key_markers() -> None:
    _, _, body = fetch(f"{BASE_URL}/llms.txt")
    text = body.decode("utf-8", errors="replace")
    for marker in EXPECTED_LLMSTXT_MARKERS:
        if marker not in text:
            fail(f"llms.txt is missing '{marker}'")
    print("PASS llms.txt includes core discovery markers")


def ensure_ai_txt_has_agent_markers() -> None:
    _, _, body = fetch(f"{BASE_URL}/ai.txt")
    text = body.decode("utf-8", errors="replace")
    for marker in EXPECTED_AITXT_MARKERS:
        if marker not in text:
            fail(f"ai.txt is missing '{marker}'")
    print("PASS ai.txt includes agent-facing guidance markers")


def ensure_llms_json_contract() -> None:
    _, _, body = fetch(f"{BASE_URL}/.well-known/llms.json")
    try:
        payload = json.loads(body)
    except json.JSONDecodeError as exc:
        fail(f".well-known/llms.json is not valid JSON: {exc}")

    for key in EXPECTED_LLMS_JSON_KEYS:
        if key not in payload:
            fail(f".well-known/llms.json is missing top-level key '{key}'")

    site = payload.get("site", {})
    if site.get("url") != BASE_URL:
        fail(f".well-known/llms.json site.url is '{site.get('url')}', expected '{BASE_URL}'")

    endpoints = payload.get("endpoints", {})
    for key, expected in EXPECTED_ENDPOINTS.items():
        if endpoints.get(key) != expected:
            fail(
                f".well-known/llms.json endpoints.{key} is '{endpoints.get(key)}',"
                f" expected '{expected}'"
            )

    policies = payload.get("policies", {})
    if policies.get("attribution") != "required":
        fail(".well-known/llms.json policies.attribution must be 'required'")

    print("PASS .well-known/llms.json matches the expected contract")


def main() -> int:
    ensure_surface_contract()
    ensure_llms_txt_has_key_markers()
    ensure_ai_txt_has_agent_markers()
    ensure_llms_json_contract()
    print("PASS live audit completed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
