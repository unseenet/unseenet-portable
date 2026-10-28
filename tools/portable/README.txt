UNSEENET - portable
===================

Discussion groups the old Usenet way, over Tor. This folder holds everything:
the client, Tor, and - once you start it - your encrypted vault in data/.
Put the whole folder on a USB stick, or anywhere you like.

  Documentation:  https://unseenet.org/
  Source:         https://github.com/unseenet/unseenet


STARTING
--------

Windows   Double-click "Start Unseenet.bat".
          Windows may say "Windows protected your PC": the program is not
          signed. Click "More info", then "Run anyway".

macOS     Double-click "Start Unseenet.command" - not the program in the
          macos-... folder. The first time, macOS blocks it: click Done,
          open System Settings > Privacy & Security, click "Open Anyway"
          by "Start Unseenet.command", and start it again. (macOS 14 and
          older: right-click the file, choose Open, and confirm.)
          If macOS says "Python.framework" is damaged, you started the
          program directly: click Cancel and use the launcher, or run
            xattr -dr com.apple.quarantine /path/to/Unseenet

Linux     In a terminal:   sh /path/to/Unseenet/start-linux.sh

The first time, you choose a passphrase for your vault, a name, and a node to
connect to. Starting Tor takes up to a minute.

You can read at once, but a new key must "ripen" once before it can post: a
calculation of a few minutes to a quarter of an hour or more. It starts by
itself; keep the client open until it is done (Ctrl+P > Key ripening shows
how far it is).


YOUR DATA
---------

Everything you have - your keys, groups, contacts, saved posts and Tor's
state - is in data/, encrypted with your passphrase. Nobody can read it
without the passphrase, and nobody can recover it if you forget it.

  - Back up data/ (it is small). Losing it means losing your identity.
  - The same data/ works with all the programs here, so one stick works on
    Windows, macOS and Linux alike.


WHAT STAYS ON THE COMPUTER
--------------------------

Unseenet writes only inside this folder. But the operating system itself may
record that a program ran: Windows keeps "prefetch" and recent-files lists,
macOS and Linux may keep logs and shell history, and the computer's network
sees that it connects to Tor (not what you do there). Use a computer you
trust; on one you do not, assume it may record what you type.


IF TOR CANNOT CONNECT
---------------------

Some networks - at work, at school, in some countries - block Tor. In the
client press Ctrl+P and choose "Tor bridges": the built-in obfs4 or Snowflake
bridges usually get through.

To check this copy works:   Start Unseenet --self-test
(on Linux: sh start-linux.sh --self-test)


CHECKING YOUR DOWNLOAD
----------------------

Each release lists SHA-256 checksums in SHA256SUMS.txt. Compare:

  Windows:  certutil -hashfile unseenet-....zip SHA256
  macOS:    shasum -a 256 unseenet-....zip
  Linux:    sha256sum unseenet-....zip


WHAT IS INSIDE
--------------

  <platform>/unseenet      the client (unseenet --help for the other modes)
  <platform>/tor/          Tor and its pluggable transports, from the Tor
                           Project's Expert Bundle, signature-checked at build
  LICENSES/                Unseenet (Apache 2.0) and the licences of Tor and
                           the libraries that come with it
  UNSEENET-PORTABLE        tells the programs to keep their data in data/

Unseenet is pre-alpha software. Test nodes may be reset at any time.
