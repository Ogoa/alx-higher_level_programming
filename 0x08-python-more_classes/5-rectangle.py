#!/usr/bin/python3
'''Module defining a class Rectangle'''


class Rectangle:
    '''Class representing a rectangle polygon'''

    def __init__(self, width=0, height=0):
        '''Initialises the rectangle's dimensions

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        '''

        self.__width_check(width)
        self.__height_check(height)

        self.__width = width
        self.__height = height

    def __width_check(self, width):
        '''Performs type checks on the width parameter

        Args:
            width (int): Width of the rectangle

        Raises:
            TypeError: if width is not an int object
            An extra check for bool values which would
            pass the check since they are a subtype of int
        '''

        if not isinstance(width, int) or isinstance(width, bool):
            raise TypeError("width must be an integer")

    def __height_check(self, height):
        '''Performs type check on the height parameter

        Args:
            height (int): Height of the rectangle

        Raises:
            TypeError: if height is not an int object
            An extra check for bool values which would pass
            the check since they are a subtype of int
        '''

        if not isinstance(height, int) or isinstance(height, bool):
            raise TypeError("height must be an integer")

    @property
    def width(self):
        '''int: Retrieves value of the width instance variable

        Has a setter function that assigns a value to the variable
        as well as performing checks to ensure the argument passed is
        of the correct type
        '''

        return self.__width

    @width.setter
    def width(self, value):

        self.__width_check(value)

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        '''int: Retrieves value of the height instance variable

        Has a setter function that assigns a value to the variable
        as well as performing checks to ensure the argument passes is
        ot the correct type
        '''

        return (self.__height)

    @height.setter
    def height(self, value):

        self.__height_check(value)

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        '''Evaluates the rectangle area

        Returns:
            int: area of the rectangle
        '''

        return (self.__height * self.__width)

    def perimeter(self):
        '''Evaluates the rectangle perimeter

        Returns:
            int: perimeter
        '''

        if self.__width == 0 or self.__height == 0:
            return 0

        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        '''Returns the string representation of a Rectangle object'''

        if self.__height == 0 or self.__width == 0:
            return ""

        return "\n".join(["#" * self.__width for i in range(self.__height)])

    def __repr__(self):
        '''Returns the official string representation of the
        Rectangle object, which should be able to recreate a new instance
        using the eval() function
        '''

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
