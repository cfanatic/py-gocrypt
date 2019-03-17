# py-gocrypt

Use this tool if you have to manage multiple directories which are encrypted with [**gocryptfs**](https://github.com/rfjakob/gocryptfs) and you prefer to use the terminal over a graphical user interface.

## Requirements

Developed and tested on the following setup:

- macOS 10.13.6
- gocryptfs v1.6.1
- Python 3.7.2

## Installation

Make sure that [**gocryptfs**](https://nuetzlich.net/gocryptfs/quickstart/) is set up correctly.

Open *main.py* and set `CONFIG_PATH` to the full path of `misc/config.toml`.

Create a symbolic link to *main.py*:

`ln -s <path-to-file> /usr/local/bin/gc`

Call `gc` from the terminal to see if the setup is working correctly:

![Summary](https://github.com/cfanatic/py-gocrypt/blob/master/misc/gc_summary.png)

## Usage

In order to decrypt a folder, run `gc <keyword>`:

![Decrypt](https://github.com/cfanatic/py-gocrypt/blob/master/misc/gc_decrypt.png)

Run the same command in order to encrypt a folder.

Each keyword to an encrypted folder is defined in `misc/config.toml`.
