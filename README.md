<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/unseenet/unseenet/main/assets/logo-dark.svg">
    <img src="https://raw.githubusercontent.com/unseenet/unseenet/main/assets/logo-light.svg" alt="Unseenet" width="360">
  </picture>
</p>

<h1 align="center">unseenet-portable</h1>

<p align="center"><b>Unseenet on a USB stick - for Windows, macOS and Linux.</b><br>
One folder with the client and Tor inside. Nothing to install: unzip it, start it, take it with you.</p>

<p align="center">
  <a href="https://github.com/unseenet/unseenet-portable/releases"><img src="https://img.shields.io/github/v/release/unseenet/unseenet-portable?include_prereleases&label=release" alt="Release"></a>
  <a href="https://github.com/unseenet/unseenet-portable/actions/workflows/build.yml"><img src="https://github.com/unseenet/unseenet-portable/actions/workflows/build.yml/badge.svg" alt="build"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="Apache-2.0"></a>
</p>

> **Pre-alpha.** Nothing is stable yet, and Unseenet has not had a security
> review. Do not rely on it to protect anyone yet.

<p align="center">
  <img src="https://raw.githubusercontent.com/unseenet/unseenet-tui/main/docs/img/demo.gif" alt="Portable · Terminal: the terminal client" width="430">
  <img src="https://raw.githubusercontent.com/unseenet/unseenet-gui/main/docs/img/demo.gif" alt="Portable · Graphical: the graphical client" width="430">
</p>
<p align="center"><sub><b>Portable · Terminal</b> and <b>Portable · Graphical</b> - two clients, one vault</sub></p>

## What it is

The portable builds are the easiest way to use [Unseenet](https://unseenet.org),
a discussion network in the spirit of the old Usenet over Tor onion services.
Each is one folder: the client, **Tor**, and your encrypted vault in `data/`
beside them. Put the folder on a USB stick and you carry your Unseenet with
you - your keys, groups and contacts - and leave nothing behind on the
computer you used.

There are two clients, and they share the stick and the vault:

| | |
|---|---|
| **Portable · Terminal** | [the terminal client](https://github.com/unseenet/unseenet-tui): a newsreader in a terminal window |
| **Portable · Graphical** | [the graphical client](https://github.com/unseenet/unseenet-gui): the same, in a window of its own |

## Get it

From the [releases](https://github.com/unseenet/unseenet-portable/releases) (or the
newest [development build](https://github.com/unseenet/unseenet-portable/releases/tag/dev)):

| File | For |
|------|-----|
| `unseenet-<version>-usb.zip` | **The terminal client for every system** in one folder - for a stick that works on any computer |
| `unseenet-<version>-windows-x86_64.zip`, `-macos-aarch64.zip`, `-macos-x86_64.zip`, `-linux-x86_64.zip` | The terminal client for one system |
| `unseenet-gui-<version>-usb.zip` and per system | The graphical client, the same way |

Check a download against `SHA256SUMS.txt` from the same release
(`sha256sum`, `shasum -a 256` or `certutil -hashfile … SHA256`).

Unzip, copy the `Unseenet` folder to a stick (FAT32 or exFAT works on all
three systems), and start it:

| | Terminal | Graphical |
|---|---|---|
| **Windows** | `Start Unseenet.bat` | `Unseenet Graphical.exe` |
| **macOS** | `Start Unseenet.command` | `Start Unseenet Graphical.command` |
| **Linux** | `sh start-linux.sh` | `sh start-graphical-linux.sh` |

The programs are not signed: Windows asks *More info → Run anyway* the first
time, macOS wants a right-click → *Open*. The first start asks for a
passphrase for your vault, a display name and a node.

**The full guide:** [Portable](https://unseenet.org/portable/) - checking
downloads, the stick, your data, updating.

## How it works

This repository holds no client code. [`versions.toml`](versions.toml) names
the core, the terminal client and the graphical client a release is made
from, and [`.github/workflows/build.yml`](.github/workflows/build.yml) builds
them: Tor (its signatures checked), the terminal and the graphical build for
Linux, Windows and two kinds of Mac, each unpacked and self-tested as a user
would, the USB zips and the checksums - all in the open, on GitHub's runners.

| When | What |
|---|---|
| each night | only if `main` of the core or a client (or this repository) changed since the `dev` build; replaces `dev`, signed with the build repositories' release key and announced in `unseenet.releases`, where sticks learn of it |
| by hand | *Run workflow*: `publish` = `dev` or `artifact`, `force` to build anyway |
| a `v*` tag | the release, from the versions in `versions.toml`, signed afterwards by the maintainer with the project key |
| a pull request | the builds as artifacts |

The images for booting a stick are made from these zips in
[unseenet-bootable](https://github.com/unseenet/unseenet-bootable).

## Develop

The build tools are here: `tools/build_portable.py` (the terminal builds, and
the Tor handling both builds use - the download, the check against Tor
Browser's key in `tools/keys/`, the version pinned in `tools/tor-version.txt`)
and `tools/build_graphical.py`, with the launchers and READMEs in
`tools/portable/`. They build checkouts of the core, unseenet-tui and
unseenet-gui given with `--core` and `--gui`. To try a branch, run the
workflow by hand with `publish: artifact`.

A daily job (`tor-update`) opens a pull request pinning a newer Tor Expert
Bundle when Tor releases one - often a security fix; a daily one (`versions`) opens a pull request when the core,
unseenet-tui or unseenet-gui made a release that `versions.toml` does not
name yet.

## Versions and releases

A bundle is versioned as the core it carries (`0.6.0`); a rebuild with newer
clients is `0.6.0.post1`. When a part is released, the `versions` job
proposes it in `versions.toml` in a pull request; merging it - or a pull request
pinning a newer Tor - tags the next bundle (`post-release`); the
workflow makes the release, and the maintainer signs its `SHA256SUMS.txt`
with the project key (`tools/project/sign_release.py` in unseenet). Notes
are in [CHANGELOG.md](CHANGELOG.md).

## Part of Unseenet

| Repository | What it is |
|---|---|
| [unseenet](https://github.com/unseenet/unseenet) | The protocol (UN-RFCs), the core library, the node and the command-line client |
| [unseenet-tui](https://github.com/unseenet/unseenet-tui) | The terminal client |
| [unseenet-gui](https://github.com/unseenet/unseenet-gui) | The graphical client - in a window, booted, or in a browser |
| [unseenet-portable](https://github.com/unseenet/unseenet-portable) | Builds the portable clients, Terminal and Graphical, with Tor inside |
| [unseenet-bootable](https://github.com/unseenet/unseenet-bootable) | Builds the bootable images, Terminal and Graphical |
| [unseenet-docs](https://github.com/unseenet/unseenet-docs) | The site [unseenet.org](https://unseenet.org) |
| [unseenet-entrance](https://github.com/unseenet/unseenet-entrance) | Web entrances: the graphical client in an ordinary browser |
| [unseenet-gateway](https://github.com/unseenet/unseenet-gateway) | Gateways to other networks: Usenet, Nostr, Matrix |
| [unseenet-bots](https://github.com/unseenet/unseenet-bots) | Bots that keep channels filled with current content |
| [unseenet-helpbot](https://github.com/unseenet/unseenet-helpbot) | The bot that answers questions in `unseenet.help` |
| [unseenet-watchman](https://github.com/unseenet/unseenet-watchman) | Automatic spam reports and content labels that readers may choose to follow |
| [unseenet-stats](https://github.com/unseenet/unseenet-stats) | Statistics for the network |
| [unseenet-mcp](https://github.com/unseenet/unseenet-mcp) | An MCP server, so a language model can read and post as you (planning) |
| [unseenet-demo](https://github.com/unseenet/unseenet-demo) | Demo people, feeds and sites, made with the command-line client |

## License

[Apache License 2.0](LICENSE). The Unseenet logo: CC BY 4.0.
