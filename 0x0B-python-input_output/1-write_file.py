#!/usr/bin/python3
"""writes"""


def write_file(filename="", text=""):
    """writes to a file"""
    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
