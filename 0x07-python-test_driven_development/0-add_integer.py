#!/usr/bin/python3
"""Does an addition of two numbers"""


def add_integer(a, b=98):
    """Return the sum of a and b.
        Raises:
            TypeError: If a or b is neither
            an int nor a float.
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
