#!/usr/bin/env python3
"""
Like cat, but combines files with a separator between file contents.

Combined text is printed to stdout.

Example:


"""
import argparse
import sys
from txttools.util.filetools import read

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("files", nargs="+", type=str,
    help="A list of files to concat")
parser.add_argument("-s", "--sep", type=str, default="---",
    help="Separator string")
parser.add_argument("-p", "--prepend_sep", action='store_true',
    help="Prepend separator at beginning as well")
parser.add_argument("-o", "--output", type=str, default="-", help="Output file (- for stdout)")


def ijoin(strings, sep):
    """
    Given an iterable of strings, return an iterable of strings with
    sep in-between.
    """
    i = 0
    for s in strings:
        if i > 0:
            yield sep
        yield s
        i = i + 1


def main():
    args = parser.parse_args()
    output = sys.stdout
    sep = f"\n\n{args.sep}\n\n"

    contents = (read(path) for path in args.files)
    joined = ijoin(contents, sep)

    if args.prepend_sep:
        output.write(sep)

    for s in joined:
        output.write(s)

if __name__ == '__main__':
    main()