#!/usr/bin/python3
'''Defines the class Square'''


class Square(__import__("9-rectangle").Rectangle):
    '''Definition of the class Square
    Inherits from Rectangle'''

    def __init__(self, size):
        '''Initialises an instance of Square

        Args:
            size (int): Dimensions of the square
        '''

        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Evaluates the area of the object

        Returns:
            int: Area of the object
        '''

        return (self.__size ** 2)
