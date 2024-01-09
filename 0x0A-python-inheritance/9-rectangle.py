#!/usr/bin/python3
'''Defines the class Rectangle'''


class Rectangle(__import__("7-base_geometry").BaseGeometry):
    '''Definition of the class Rectangle'''

    def __init__(self, width, height):
        '''Initialises an instance

        Args:
            width (int): Positive integer
            height (int): Positive integer
        '''

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        '''Evaluates the area of the object

        Returns:
            area (int): Area of the object
        '''

        return (self.__width * self.__height)

    def __str__(self):
        '''Casts a string representation of the object'''

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
