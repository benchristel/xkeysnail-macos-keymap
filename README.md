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
3. Paste the following into `~/.config/autostart/xkeysnail.desktop` so xkeysnail starts on login. Be sure to replace `/path/to/xkeysnail-macos-keymap/config.py` with the actual path.
   ```
   [Desktop Entry]
   Version=1.0
   Name=xkeysnail
   Comment=remap keyboard input
   Exec=sudo xkeysnail /path/to/xkeysnail-macos-keymap/config.py
   Terminal=false
   Type=Application
   StartupNotify=true
   ```
4. Reboot.

## Security

Since `xkeysnail` runs as `root`, it's possible that `config.py` is also executed as root. Take appropriate precautions to ensure that your `config.py` contains only trusted code. 
