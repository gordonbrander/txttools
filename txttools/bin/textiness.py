#!/usr/bin/env python3
"""
Filter lines of text by "textiness".
"""
import argparse
import sys
import re
import string
from txttools.util.parsertools import add_arguments
from txttools.util.filetools import open_input, open_output

parser = argparse.ArgumentParser(description=__doc__)
parser = add_arguments(parser)
parser.add_argument("-c", "--words", type=argparse.FileType("r"), help="Corpus of common words used to score prosiness. File, one per line.")
parser.add_argument("-w", "--word_threshold", type=int, default=2, help="Word threshold")
parser.add_argument("-p", "--prosiness_threshold", type=float, default=0.8, help="Prosiness threshold")


def count_words(line):
    """
    Count the number of words in a line. We only count words > 1 char.
    """
    return len(tuple(word for word in line.split() if len(word) > 1))


PROSEY = r"[A-Za-z\,\.]"
NONPROSEY = r"[0-9_\@\&\^\%\$\#\<\>\[\]\{\}\*\/\\]"


def report_prosiness(line):
    return (
        len(re.findall(PROSEY, line)),
        len(re.findall(NONPROSEY, line))
    )


def score_prosiness(line):
    prosey, nonprosey = report_prosiness(line)
    if (prosey > 0):
        return (1.0 - (nonprosey / prosey))
    else:
        return 0.0


NONCHARACTERS = r"[^\w\s]"


def to_bag_of_words(line):
    line = line.lower()
    line = re.sub(NONCHARACTERS, "", line)
    return frozenset(line.split())


def is_texty(line, corpus, word_threshold, prosiness_threshold):
    bag = to_bag_of_words(line)
    intersection = bag.intersection(corpus)
    print(bag, intersection)
    return (
        len(intersection) > word_threshold and
        # count_words(line) > word_threshold and
        score_prosiness(line) > prosiness_threshold
    )


def process(lines, corpus, word_threshold, prosiness_threshold):
    for line in lines:
        if is_texty(line, corpus, word_threshold, prosiness_threshold):
            yield line


def main():
    args = parser.parse_args()
    input_file = open_input(args.file)
    output_file = open_output(args.output)

    corpus = frozenset(line.strip() for line in args.words.readlines())

    processed = process(
        input_file,
        corpus,
        word_threshold=args.word_threshold,
        prosiness_threshold=args.prosiness_threshold,
    )
    for line in processed:
        output_file.write(line)


if __name__ == '__main__':
    main()