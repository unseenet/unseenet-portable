# Changelog

All notable changes to unseenet-portable are listed here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow the
[Unseenet conventions](https://github.com/unseenet/.github/blob/main/CONVENTIONS.md#versions).

## [Unreleased]

- **The build tools are here** (#6): `tools/build_portable.py` (the terminal
  builds and the Tor handling), `tools/build_graphical.py` (from unseenet-gui),
  the launchers in `tools/portable/`, `tools/tor-version.txt` and Tor Browser's
  key, with their history; they build checkouts given with `--core`/`--gui`.
  The weekly `tor-update` check moves here too.
- **`versions` job**: a pull request bumping `versions.toml` when a part makes
  a release (`tools/bump_versions.py`).
- A release also attaches its files to the core's release of the same tag
  while old sticks look there, when `UNSEENET_CORE_RELEASE_TOKEN` is set.
