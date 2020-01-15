#!/usr/bin/env python3
"""
Clean text.

- Collapse double spaces
"""
import argparse
import sys
import re

from txttools.util.parsertools import add_arguments
from txttools.util.filetools import open_input, open_output


parser = argparse.ArgumentParser(description=__doc__)
parser = add_arguments(parser)


def clean_whitespace(lines):
    for line in lines:
        yield re.sub(r"\s+", " ", line).strip()


def main():
    args = parser.parse_args()
    input_file = open_input(args.file)
    output_file = open_output(args.output)
    
    lines = clean_whitespace(input_file)

    for line in lines:
        print(line, file=output_file)


if __name__ == '__main__':
    main()