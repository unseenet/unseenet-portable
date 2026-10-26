#!/usr/bin/env python3
"""The tag of the next bundle release (unseenet-portable#6).

    python tools/next_tag.py            # e.g. v0.6.0, or v0.6.0.post2

A bundle is versioned as the core it carries (``core`` in versions.toml). The first
bundle of a core is ``vX.Y.Z``; every rebuild of it - a newer Tor, newer clients - is a
PEP 440 post-release, ``vX.Y.Z.post1``, ``.post2``, ...: the same Unseenet, built again,
ordered after ``X.Y.Z`` and before ``X.Y.Z+1``. The tags already made are read from git.
"""

from __future__ import annotations

import re
import subprocess
import sys
import tomllib
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
_BASE = re.compile(r"^v?(\d+\.\d+\.\d+)$")


def next_tag(core: str, tags: list[str]) -> str:
    """The next tag for a bundle of ``core`` (``v0.6.0``) given the tags there are."""
    m = _BASE.match(core.strip())
    if m is None:
        raise ValueError(f"versions.toml: core must be a release tag like v0.6.0, not {core!r}")
    base = m.group(1)
    posts = []
    first = False
    for t in tags:
        t = t.strip()
        if t == f"v{base}":
            first = True
        pm = re.fullmatch(rf"v{re.escape(base)}\.post(\d+)", t)
        if pm:
            posts.append(int(pm.group(1)))
    if not first and not posts:
        return f"v{base}"
    return f"v{base}.post{max(posts, default=0) + 1}"


def main() -> None:
    core = tomllib.loads((HERE / "versions.toml").read_text())["release"]["core"]
    tags = subprocess.run(["git", "tag", "-l", "v*"], cwd=HERE, check=True,
                          capture_output=True, text=True).stdout.split()
    print(next_tag(core, tags))


if __name__ == "__main__":
    sys.exit(main())
