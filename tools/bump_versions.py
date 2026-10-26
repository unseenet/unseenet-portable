#!/usr/bin/env python3
"""Propose the newest releases of the parts in versions.toml (unseenet-portable#6).

    python tools/bump_versions.py            # say what is newer, change nothing
    python tools/bump_versions.py --write    # write versions.toml; GitHub output lines

For each part - core (unseenet/unseenet), tui (unseenet-tui), gui (unseenet-gui) - the
newest release that is not a pre-release (``gh release list``) is compared with the tag
in versions.toml; a newer one is written there, keeping the file's comments. With
``--write`` it prints ``changed=true|false`` and ``summary=...`` for $GITHUB_OUTPUT.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
VERSIONS = HERE / "versions.toml"
REPOS = {"core": "unseenet/unseenet", "tui": "unseenet/unseenet-tui", "gui": "unseenet/unseenet-gui"}
_TAG = re.compile(r"^v?(\d+)\.(\d+)\.(\d+)(?:\.post(\d+))?$")


def key(tag: str) -> tuple | None:
    """A release tag as something to compare: v0.6.0 < v0.6.0.post1 < v0.6.1."""
    m = _TAG.match(tag.strip())
    return None if m is None else tuple(int(x or 0) for x in m.groups())


def newest_release(repo: str) -> str | None:
    out = subprocess.run(["gh", "release", "list", "-R", repo, "--exclude-pre-releases",
                          "--limit", "30", "--json", "tagName"],
                         check=True, capture_output=True, text=True).stdout
    tags = [r["tagName"] for r in json.loads(out) if key(r["tagName"]) is not None]
    return max(tags, key=key) if tags else None


def current(text: str) -> dict[str, str]:
    return {k: v for k, v in re.findall(r'^(core|tui|gui)\s*=\s*"([^"]+)"', text, re.M)}


def bump(text: str, newer: dict[str, str]) -> str:
    for part, tag in newer.items():
        text = re.sub(rf'^({part}\s*=\s*)"[^"]+"', lambda m: f'{m.group(1)}"{tag}"', text,
                      count=1, flags=re.M)
    return text


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--write", action="store_true")
    args = p.parse_args()
    text = VERSIONS.read_text()
    have = current(text)
    newer = {}
    for part, repo in REPOS.items():
        latest = newest_release(repo)
        if latest and (part not in have or key(latest) > (key(have[part]) or ())):
            newer[part] = latest
    summary = ", ".join(f"{p} {have.get(p, '-')} -> {t}" for p, t in newer.items())
    if not args.write:
        print(summary or "versions.toml is up to date")
        return
    if newer:
        VERSIONS.write_text(bump(text, newer))
    print(f"changed={'true' if newer else 'false'}")
    print(f"summary={summary}")


if __name__ == "__main__":
    sys.exit(main())
