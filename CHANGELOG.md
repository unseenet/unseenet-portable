# Changelog

All notable changes to unseenet-portable are listed here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow the
[Unseenet conventions](https://github.com/unseenet/.github/blob/main/CONVENTIONS.md#versions).

## [Unreleased]

## [0.6.8] - 2026-10-31

Unseenet 0.6.8 with the terminal client 0.4.1 and the graphical client 0.5.1: *Share with a
comment*, *Share into a group* and *Send to* open the ordinary compose window, the shared
post as a card under your words, the group or person chosen first with a search. From
0.6.7: link cards keep their picture where the picture's server picks the format
(unseenet#813).

## [0.6.6] - 2026-10-30

Unseenet 0.6.6 with the terminal client 0.4.0 and the graphical client 0.5.0: sharing
(UN-RFC 0060) - share a post into your feed, with a comment of your own, into up to three
groups, or send it to one person. A share is a reference, never a copy: it is read as the
original, comments and reactions go to the original, and when its author withdraws it, it
is gone from every share. Never a count. With Tor 16.0, as 0.6.5.post2 (#21).

## [0.6.5.post1] - 2026-10-30

Unseenet 0.6.5 again, with the terminal client 0.3.1 and the graphical client 0.4.1: a post
with pictures of its own shows them first and its link card as one small line after them
(UN-RFC 0059 section 8) - a NASA picture of the day is the picture again.

## [0.6.5] - 2026-10-30

Unseenet 0.6.5 with the terminal client 0.3.0 and the graphical client 0.4.0: link
previews (UN-RFC 0059) - a post with a link shows a card with the site's icon, domain,
title, description and picture, made once by the poster's client over Tor; small on a chat
line. Ctrl+P: *Link previews* turns them off.

- **A post-release carries its own version** (#6): v0.6.4.post1 was built with the core's
  0.6.4 inside and in its zips' names, so a stick's updater did not see it as newer and
  `sign_release.py` refused it. On a `vX.Y.Z.postN` tag the core's version is now the
  tag's: `unseenet-0.6.4.post1-*.zip`, `UNSEENET-VERSION` 0.6.4.post1. The graphical zips
  keep the graphical client's own version.

- **The graphical builds are signed and announced too** (#3): their checksums are
  in the same `SHA256SUMS.txt` as the terminal builds', so the release key signs
  them and `unseenet.releases` carries them; `SHA256SUMS-graphical.txt` is gone.
  A terminal stick's updater still takes only its own zip.

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
