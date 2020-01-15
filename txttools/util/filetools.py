"""
Tools for working with files
"""
import sys

def read(file):
    """
    Read contents of file.
    """
    with open(file) as f:
        return f.read()


def open_input(file_path):
    """
    Open input file, accepting "-" as a magic token for "stdin"
    """
    return open(file_path, "r") if file_path != "-" else sys.stdin


def open_output(file_path):
    """
    Open input file, accepting "-" as a magic token for "stdout"
    """
    return open(file_path, "w") if file_path != "-" else sys.stdout