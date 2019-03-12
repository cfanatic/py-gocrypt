#!/usr/bin/env python3

"""
Call gocryptfs with the required arguments taken from a configuration file
"""

import getopt
import subprocess
import sys
import toml

CONFIG_PATH = "/Users/cfanatic/Coding/Python/GoCrypt/misc/config.toml"

def main():
    config = toml.load(CONFIG_PATH)
    try:
        if len(sys.argv) == 1:
            print("Error@main: Not enough input arguments given!")
        else:
            opts, dummy = getopt.getopt(sys.argv[1:], "e:d:p", ["encrypt", "decrypt", "print"])
            for opt, arg in opts:
                if opt in ("-e", "--encrypt"):
                    print("Info@main: Encrypting folder.")
                    subprocess.run(["umount", config[arg]["plain"]])
                elif opt in ("-d", "--decrypt"):
                    print("Info@main: Decrypting folder.")
                    subprocess.run(["gocryptfs", config[arg]["cipher"], config[arg]["plain"]])
                elif opt in ("-p", "--print"):
                    index = 0
                    print("{0:<8} {1:<14} {2:<10} {3:<26}".format("Index", "Key", "Mount", "Path"))
                    print("----------------------------------------------------------------")
                    for key, value in config.items():
                        index += 1
                        mount = subprocess.check_output(["mount"])
                        path = config[key]["plain"].encode()
                        active = "on" if path in mount else "off"
                        print("{0:<8} {1:<14} {2:<10} {3:<26}".format(index, key, active, value["plain"]))
                else:
                    mount = subprocess.check_output(["mount"])
                    path = config[sys.argv[1]]["plain"].encode()
                    arg = sys.argv[1]
                    if path in mount:
                        print("Info@main: Encrypting folder.")
                        subprocess.run(["umount", config[arg]["plain"]])
                    else:
                        print("Info@main: Decrypting folder.")
                        subprocess.run(["gocryptfs", config[arg]["cipher"], config[arg]["plain"]])

    except KeyError as e:
        print("Error@main: '" + e.args[0] + "' is not an encrypted folder!")

if __name__ == "__main__":
    main()
