#!/usr/bin/python3
"""reads"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, 'r') as f:
        print(f.read(), end="")
