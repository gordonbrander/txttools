#!/usr/bin/env python3
"""
Set a new extension on a list of files.

Example:

    txt_ext -e ".md" *.txt
"""
import argparse
from pathlib import Path, PurePath
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("files", nargs="+", type=str,
    help="A list of files to concat")
parser.add_argument("-e", "--ext", type=str,
    help="File extension to use")


def main():
    args = parser.parse_args()

    for pathlike in args.files:
        updated_path = PurePath(pathlike).with_suffix(args.ext)
        Path(pathlike).rename(updated_path)

if __name__ == '__main__':
    main()