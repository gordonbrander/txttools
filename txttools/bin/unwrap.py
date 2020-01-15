#!/usr/bin/env python3
"""
Unwrap text and attemp to split into lines by paragraph using a heuristic.
"""
import argparse
import sys
import re
from txttools.util.parsertools import add_arguments
from txttools.util.filetools import open_input, open_output


parser = argparse.ArgumentParser(description=__doc__)
parser = add_arguments(parser)
parser.add_argument(
    "-e",
    "--paragraph_ending",
    type=str,
    default=".",
    help="Ending characters that may be considered paragraph breaks when found before newlines. "
        "This heuristic is used to unwrap hard-wrapped lines without losing paragraphs. "
        "List characters without spaces. "
        "(. by default)"
)


def _clean_line(line, paragraph_ending):
    line = line.strip()
    if line == "":
        return ""
    elif line.endswith(paragraph_ending):
        return line + "\n"
    else:
        return line + " "


def reformat_lines(lines, paragraph_ending):
    text = "".join(_clean_line(line, paragraph_ending) for line in lines)
    text = text.strip()
    return text.splitlines()


def last(indexed):
    return indexed[-1]


def clean_whitespace(line):
    return re.sub(r"\s+", " ", line)


def reformat_lines_iter(lines, paragraph_ending):
    buf = []
    for line in lines:
        line = clean_whitespace(line).strip()
        # Empty line after text is a paragraph break.
        # Check if the thing before ended on a paragraph ending.
        if line == "" and len(buf) > 0 and last(buf).strip().endswith(paragraph_ending):
            # Join buffer and strip any trailing whitespace.
            yield "".join(buf).strip()
            buf.clear()
        elif line != "":
            buf.append(line + " ")
    # Any left over? Yield it
    if len(buf) > 0:
        yield "".join(buf).strip()


def main():
    args = parser.parse_args()
    input_file = open_input(args.file)
    output_file = open_output(args.output)
    paragraph_ending = tuple(args.paragraph_ending)

    for line in reformat_lines_iter(input_file, paragraph_ending):
        print(line + '\n', file=output_file)


if __name__ == '__main__':
    main()