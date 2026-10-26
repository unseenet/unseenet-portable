# Changelog

All notable changes to unseenet-portable are listed here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow the
[Unseenet conventions](https://github.com/unseenet/.github/blob/main/CONVENTIONS.md#versions).

## [Unreleased]

- **A newer Tor, or newer parts, is released at once** (#6): when
  `tools/tor-version.txt` or `versions.toml` changes on main, `post-release`
  tags the next bundle (`tools/next_tag.py`) and starts the build on it -
  `vX.Y.Z` for a core's first bundle, then `vX.Y.Z.post1`, `.post2`, ...:
  PEP 440 post-releases, the same Unseenet built again. The maintainer signs a
  stable release afterwards as before.

- **The build tools are here** (#6): `tools/build_portable.py` (the terminal
  builds and the Tor handling), `tools/build_graphical.py` (from unseenet-gui),
  the launchers in `tools/portable/`, `tools/tor-version.txt` and Tor Browser's
  key, with their history; they build checkouts given with `--core`/`--gui`.
  The `tor-update` check moves here too, now daily, and opens a pull request
  pinning the newer Tor instead of an issue.
- **`versions` job**: a pull request bumping `versions.toml` when a part makes
  a release (`tools/bump_versions.py`).
