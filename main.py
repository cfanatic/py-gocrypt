#!/usr/bin/env python3

"""
Call gocryptfs from terminal with command line arguments
"""

import getopt
import subprocess
import sys
import toml

# Set the path to the configuration file
CONFIG_PATH = "/Users/cfanatic/Coding/Python/GoCrypt/misc/config.toml"


def decrypt(config, key):
    # Call gocryptfs process
    path_cipher = config[key]["cipher"]
    path_plain = config[key]["plain"]
    subprocess.run(["gocryptfs", path_cipher, path_plain])

def encrypt(config, key):
    # Call unmount process
    path_plain = config[key]["plain"]
    subprocess.run(["umount", path_plain])

def mount():
    # Get all mounted or decrypted folder paths
    return subprocess.check_output(["mount"])

def auto(config, key):
    # Encrypt or decrypt folder automatically
    path = config[key]["plain"].encode()
    if path in mount():
        encrypt(config, key)
    else:
        decrypt(config, key)

def summary(config):
    # Print complete summary
    index = 0
    print("{0:<8} {1:<14} {2:<10} {3:<26}".format("Index", "Key", "Mount", "Path"))
    print("----------------------------------------------------------------")
    for key, value in config.items():
        index += 1
        path = config[key]["plain"]
        active = "on" if path.encode() in mount() else "off"
        print("{0:<8} {1:<14} {2:<10} {3:<26}".format(index, key, active, value["plain"]))

def main():
    config = toml.load(CONFIG_PATH)
    try:
        if len(sys.argv) == 1:
            summary(config)
        else:
            opts, args = getopt.getopt(sys.argv[1:], "d:e:s", ["decrypt", "encrypt", "summary"])
            for opt, key in opts:
                if opt in ("-e", "--encrypt"):
                    encrypt(config, key)
                elif opt in ("-d", "--decrypt"):
                    decrypt(config, key)
                elif opt in ("-s", "--summary"):
                    summary(config)
            for key in args:
                auto(config, key)
    except KeyError as e:
        print("Error@main: '" + e.args[0] + "' is not an encrypted folder!")
    except getopt.GetoptError as e:
        print("Error@main: " + e.args[0] +"!")

if __name__ == "__main__":
    main()
