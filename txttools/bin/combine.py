#!/usr/bin/env python3
"""
Like cat, but combines files with a separator between file contents.

Combined text is printed to stdout.

Example:


"""
import argparse
import sys
from txttools.util.filetools import read
from txttools.util.util import isep

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("files", nargs="+", type=str,
    help="A list of files to concat")
parser.add_argument("-s", "--sep", type=str, default="---",
    help="Separator string")
parser.add_argument("-p", "--prepend_sep", action='store_true',
    help="Prepend separator at beginning as well")


def main():
    args = parser.parse_args()
    output = sys.stdout
    sep = f"\n\n{args.sep}\n\n"

    contents = (read(path) for path in args.files)
    joined = isep(contents, sep)

    if args.prepend_sep:
        output.write(sep)

    for s in joined:
        output.write(s)

if __name__ == '__main__':
    main()