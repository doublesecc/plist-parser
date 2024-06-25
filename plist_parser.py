#!/usr/bin/env python
# Created by Doublesec
# Designed to parse Info.plist files and dump to stdout in JSON format.

import sys
import plistlib
import json
import argparse

script = sys.argv[0]

parser = argparse.ArgumentParser(description="Convert Info.plist to JSON format")

parser.add_argument("-f", "--file", help="Info.plist file path")

args = parser.parse_args()

plist_file = args.file

def main():
    if plist_file is None:
        print("\nMissing file name argument: \"-f\"")
        print("\nUsage: python3 " + script + " -f <Info.plist>") 
        sys.exit()
    else:
        pass
    try:
        with open(plist_file, "rb") as fp:
            plistData = plistlib.load(fp)
            print(json.dumps(plistData, indent=4))
    except Exception as e:
        print(e)
        exit

if __name__ == "__main__":
    main()
