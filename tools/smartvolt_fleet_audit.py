#!/usr/bin/env python3
"""Read-only audit of SmartVoltISA repositories.

Checks repository-level protection prerequisites without modifying GitHub.
Authentication is optional; GITHUB_TOKEN is used when present.
"""

import json
import os
import sys
import urllib.error
import urllib.request

OWNER = "SmartVoltISA"
API = "https://api.github.com"
REQUIRED = ["LICENSE"]
PROTECTION_DOCS = [
    "SECURITY.md",
    "NOTICE",
    "COPYRIGHT.md",
    "SMARTVOLT-PROTECTION-STANDARD.md",
]


def get_json(url):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "SmartVolt-Fleet-Audit/1.0",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def exists(repo, path):
    try:
        get_json(f"{API}/repos/{OWNER}/{repo}/contents/{path}")
        return True
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return False
        raise


def main():
    repos = []
    page = 1
    while True:
        batch = get_json(
            f"{API}/orgs/{OWNER}/repos?per_page=100&page={page}&type=all"
        )
        if not batch:
            break
        repos.extend(r for r in batch if not r.get("archived", False))
        if len(batch) < 100:
            break
        page += 1

    rows = []
    missing_license = []
    incomplete_docs = []

    for repo in sorted(repos, key=lambda r: r["name"].lower()):
        name = repo["name"]
        license_ok = all(exists(name, p) for p in REQUIRED)
        docs = {p: exists(name, p) for p in PROTECTION_DOCS}
        row = {
            "repository": name,
            "license": "OK" if license_ok else "MISSING",
            "protection_docs": [p for p, ok in docs.items() if ok],
            "missing_protection_docs": [p for p, ok in docs.items() if not ok],
        }
        rows.append(row)
        if not license_ok:
            missing_license.append(name)
        if not all(docs.values()):
            incomplete_docs.append(name)

    print(f"SmartVoltISA fleet audit: {len(repos)} active repositories")
    print(f"LICENSE present: {len(repos) - len(missing_license)}/{len(repos)}")
    print(
        "All five protection files present: "
        f"{len(repos) - len(incomplete_docs)}/{len(repos)}"
    )

    if missing_license:
        print("\nMISSING LICENSE:")
        for name in missing_license:
            print(f"- {name}")

    print("\nDetailed report:")
    print(json.dumps(rows, ensure_ascii=False, indent=2))

    # A missing LICENSE is a hard failure; missing extra protection documents
    # is reported separately because the fleet rollout can be staged.
    return 1 if missing_license else 0


if __name__ == "__main__":
    sys.exit(main())
