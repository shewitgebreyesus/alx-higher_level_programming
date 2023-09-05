#!/usr/bin/python3
"""
a class Rectangle that defines a rectangle by:
(based on 3-rectangle.py)
"""


class Rectangle:
    """
    a class Rectangle
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width is 0 or self.height is 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        result = ""
        if not self.area():
            return result
        for i in range(self.height):
            result += "#" * self.width
            if i != self.height - 1:
                result += "\n"
        return result

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
