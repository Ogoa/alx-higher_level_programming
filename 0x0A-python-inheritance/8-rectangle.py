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
