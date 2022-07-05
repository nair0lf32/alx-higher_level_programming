#!/usr/bin/python3
"""append writes"""


def append_write(filename="", text=""):
    """append writes to a file"""
    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
