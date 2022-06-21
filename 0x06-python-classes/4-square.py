#!/usr/bin/python3
"""class Square."""


class Square:
    """A square."""

    def __init__(self, size=0):
        """Initializes a new Square.
        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """size Getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return (self.__size ** 2)
