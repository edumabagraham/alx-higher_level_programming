#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """
    A class that defines a rectangle

    Instance attributes
    -------------------
    width: int
    height: int

    Class attributes
    ----------------
    number_of_instances: int
                        the number of instances of the
                        class
    print_symbol:string
                Used as symbol for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializer
        """

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Returns the informal string output of the string
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        else:
            for i in range(self.height):
                for j in range(self.width):
                    string += str(self.print_symbol)
                if i != self.height - 1:
                    string += "\n"
            return string

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        to be able to recreate a new instance by using
        eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes a Rectangle instance.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        Getter

        Return width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter

        Args:
            value: sets to the width if it is an int and is
            greater or equal to 0

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter

        Return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter

        Args:
            value: sets to the height if it is an int and is
            greater or equal to 0

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Method
        Returns the rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Method
        Returns the rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method
        Returns the biggest rectangle based on the area
        If both areas are the same, returns the rect_1
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
