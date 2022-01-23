# macOS keyboard shortcuts for Linux, via xkeysnail

## Why?

Perhaps you want to use Mac keyboard shortcuts in Linux. This isn't a simple matter of swapping the `ctrl` and `super` keys, because:

- The terminal uses `ctrl` to send signals to the foreground process—e.g. you want `ctrl-C` to send `SIGINT` as usual.
- Text navigation shortcuts are completely different on Linux—e.g. on Mac `cmd+shift+left` will select to the beginning of the line, whereas Linux uses `shift+home` to accomplish the same thing.

## What?

This repo contains configuration for the key-remapping utility `xkeysnail`, along with installation instructions for elementary OS (and probably other Ubuntu-based systems).

Inspired by [kinto.sh](https://kinto.sh), which I couldn't get to run on elementary OS due to `python-vte` not being available in any repositories that were acceptable to `apt`.

## Installation

1. Clone this repo.
2. Install xkeysnail.
   ```
   sudo apt install python3-pip
   sudo pip3 install xkeysnail
   ```
3. Paste the following into `~/.config/autostart/xkeysnail.desktop` so xkeysnail starts on login. Be sure to replace `/path/to/xkeysnail-macos-keymap/run` with the actual path.
   ```
   [Desktop Entry]
   Name=xkeysnail
   Comment=remap keyboard input
   Exec=sudo /path/to/xkeysnail-macos-keymap/run
   Type=Application
   ```
4. Add a `sudoers` config to allow normal users to sudo the `run` script without entering a password (replace `ben` with your actual username and the example path with the actual one). E.g. on Linux Mint (and probably Ubuntu), you can do:
   ```sh
   sudo su root
   echo "ben ALL=NOPASSWD:/path/to/xkeysnail-macos-keymap/run" >/etc/sudoers.d/xkeysnail
   chmod 440 /etc/sudoers.d/xkeysnail
   ```
5. Log out and log in.

## Security

This is horribly insecure and you shouldn't use it.

The issue is that 1) the `run` script has to be sudo-able without
a password, and 2) `xkeysnail` executes Python files which are probably owned by non-root users. The result is that anyone who can modify these Python files can
execute arbitrary code as root when the user logs in.
