#!/usr/bin/python3
"""Base class"""


class Base:
    """Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class.
        Args:
            id (int): The id of the base class.
        """
        self.id = id

    @property
    def id(self):
        """id getter"""
        return self.__id

    @id.setter
    def id(self, value):
        if value != None:
            self.__id = value
        else:
            type(self).__nb_object += 1
            value = __nb_object
            self.__id = value
