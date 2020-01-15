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
from txttools.util.parsertools import add_arguments
from txttools.util.filetools import open_input, open_output

parser = argparse.ArgumentParser(description=__doc__)
parser = add_arguments(parser)
parser.add_argument("-s", "--sep", type=str, default="---",
    help="Separator string")
parser.add_argument("-p", "--prepend_sep", action='store_true',
    help="Prepend separator at beginning as well")

def main():
    args = parser.parse_args()
    input_file = open_input(args.file)
    output_file = open_output(args.output)
    sep = f"\n\n{args.sep}\n\n"

    contents_sep = isep(input_file, sep)

    if args.prepend_sep:
        output_file.write(sep)

    for s in contents_sep:
        output_file.write(s)

if __name__ == '__main__':
    main()