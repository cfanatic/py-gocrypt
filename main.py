#!/usr/bin/env python3

"""
Call gocryptfs with the required arguments taken from a configuration file
"""

import getopt
import subprocess
import sys
import toml


def main():
    config = toml.load("/Users/cfanatic/Coding/Python/GoCrypt/misc/config.toml")
    if len(sys.argv) == 1:
        print("Error@main: Not enough input arguments given!")
    elif len(sys.argv) == 2:
        mount = subprocess.check_output(["mount"])
        path = config[sys.argv[1]]["plain"].encode()
        arg = sys.argv[1]
        if path in mount:
            print("Encrypting file...")
            subprocess.run(["umount", config[arg]["plain"]])
        else:
            subprocess.run(["gocryptfs", config[arg]["cipher"], config[arg]["plain"]])
    else:
        opts, dummy = getopt.getopt(sys.argv[1:], "e:d:h", ["encrypt", "decrypt", "help"])
        for opt, arg in opts:
            if opt in ("-e", "--encrypt"):
                subprocess.run(["umount", config[arg]["plain"]])
            elif opt in ("-d", "--decrypt"):
                subprocess.run(["gocryptfs", config[arg]["cipher"], config[arg]["plain"]])
            elif opt in ("-h", "--help"):
                pass


if __name__ == "__main__":
    main()
