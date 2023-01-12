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

    Methods
    -------
    area: returns the area of the square
    """

    def __init__(self, size=0, position=(0,0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        
        if not (
            type(position) is tuple and
            len(position) == 2 and
            type(position[0]) is int and
            type(position[1]) is int and
            position[0] >= 0 and
            position[1] >= 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if not (
            type(value) is tuple and
            len(value) == 2 and
            type(value[0]) is int and
            type(value[1]) is int and
            value[0] >= 0 and
            value[1] >= 0
            ):
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
