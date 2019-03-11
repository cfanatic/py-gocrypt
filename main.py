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
    try:
        if len(sys.argv) == 1:
            print("Error@main: Not enough input arguments given!")
        elif len(sys.argv) == 2:
            mount = subprocess.check_output(["mount"])
            path = config[sys.argv[1]]["plain"].encode()
            arg = sys.argv[1]
            if path in mount:
                print("Info@main: Encrypting folder.")
                subprocess.run(["umount", config[arg]["plain"]])
            else:
                print("Info@main: Decrypting folder.")
                subprocess.run(["gocryptfs", config[arg]["cipher"], config[arg]["plain"]])
        else:
            opts, dummy = getopt.getopt(sys.argv[1:], "e:d:i:h", ["encrypt", "decrypt", "info", "help"])
            for opt, arg in opts:
                if opt in ("-e", "--encrypt"):
                    print("Info@main: Encrypting folder.")
                    subprocess.run(["umount", config[arg]["plain"]])
                elif opt in ("-d", "--decrypt"):
                    print("Info@main: Decrypting folder.")
                    subprocess.run(["gocryptfs", config[arg]["cipher"], config[arg]["plain"]])
                elif opt in ("-i", "--info"):
                    mount = subprocess.check_output(["mount"])
                    path = config[arg]["plain"].encode()
                    if path in mount:
                        print("Info@main: '" + arg + "' is mounted.")
                    else:
                        print("Info@main: '" + arg + "' is not mounted.")
                elif opt in ("-h", "--help"):
                    pass
    except KeyError as e:
        print("Error@main: '" + e.args[0] + "' is not an encrypted folder!")

if __name__ == "__main__":
    main()
