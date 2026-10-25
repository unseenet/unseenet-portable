# unseenet-portable

Builds the portable Unseenet clients - **Portable · Terminal** and **Portable · Graphical** - for Linux, Windows and macOS, and the all-in-one USB zip, with Tor inside. No client code: `versions.toml` names the core, terminal and graphical client to build, and the workflows build, self-test and sign them.

Builds run each night when something changed (the `dev` pre-release), by hand, and for releases. A bundle is versioned as the core it carries (`0.6.0`); a rebuild with newer clients is `0.6.0.post1`.

> **Being set up** ([unseenet#549](https://github.com/unseenet/unseenet/issues/549), part of [unseenet#391](https://github.com/unseenet/unseenet/issues/391)). Until it is, the builds people download are still made in [unseenet](https://github.com/unseenet/unseenet/releases) and [unseenet-gui](https://github.com/unseenet/unseenet-gui/releases).

## How it builds

| | |
|---|---|
| [`versions.toml`](versions.toml) | the core and graphical client a release is made from; nightly builds take `main` of each |
| [`.github/workflows/build.yml`](.github/workflows/build.yml) | Tor (signatures checked), the terminal and the graphical build for Linux, Windows and two Macs, each unpacked and self-tested, the USB zips, the checksums; then the `dev` pre-release or the release |

For now each part is built by the build tool in its own repository, checked
out at the version to build; next, those tools move here (#549).

| When | What |
|---|---|
| each night | only if the core's or the graphical client's `main` (or this repository) changed since the `dev` build; replaces `dev`, signed with the CI release key |
| by hand | *Run workflow*: `publish` = `dev` or `artifact`, `force` to build anyway |
| a `v*` tag | the release, from the versions in `versions.toml` |
| a pull request | the builds as artifacts |

Publishing `dev` needs the repository secrets `UNSEENET_RELEASE_KEY` and
`UNSEENET_ANNOUNCE_SEED`; without them the builds are kept as artifacts.

## Part of Unseenet

Unseenet is made in several repositories, each released on its own:

| Repository | What it is |
|---|---|
| [unseenet](https://github.com/unseenet/unseenet) | The protocol (UN-RFCs), the core library, the node and the command-line client |
| [unseenet-tui](https://github.com/unseenet/unseenet-tui) | The terminal client (moving here from unseenet, unseenet#548) |
| [unseenet-gui](https://github.com/unseenet/unseenet-gui) | The graphical client - in a window, booted, or in a browser |
| [unseenet-portable](https://github.com/unseenet/unseenet-portable) | Builds the portable clients, Terminal and Graphical, with Tor inside (unseenet#549) |
| [unseenet-bootable](https://github.com/unseenet/unseenet-bootable) | Builds the bootable images, Terminal and Graphical, and later a node image (unseenet#550) |
| [unseenet-docs](https://github.com/unseenet/unseenet-docs) | The site [unseenet.org](https://unseenet.org), gathering the docs of every repository (unseenet#547) |
| [unseenet-entrance](https://github.com/unseenet/unseenet-entrance) | Web entrances: the graphical client in an ordinary browser |
| [unseenet-gateway](https://github.com/unseenet/unseenet-gateway) | Gateways to other networks: Usenet, Nostr, Matrix |
| [unseenet-bots](https://github.com/unseenet/unseenet-bots) | Bots that keep channels filled with current content |
| [unseenet-helpbot](https://github.com/unseenet/unseenet-helpbot) | The bot that answers questions in `unseenet.help` |
| [unseenet-stats](https://github.com/unseenet/unseenet-stats) | Statistics for the network |
| [unseenet-mcp](https://github.com/unseenet/unseenet-mcp) | An MCP server, so a language model can read and post as you (planning) |
| [unseenet-demo](https://github.com/unseenet/unseenet-demo) | Demo people, feeds and sites, made with the command-line client |

## License

[Apache License 2.0](LICENSE).
