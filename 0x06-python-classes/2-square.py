#!/usr/bin/python3
"""Square related feature module."""


class Square:
    """
    A class used to represent a Square

    ...
    Attributes
    ----------
    Private
    -------
    size: int
    the size of the square
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
