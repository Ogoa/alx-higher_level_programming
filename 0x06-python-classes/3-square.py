#!/usr/bin/python3
'''Defines a class Square

Attributes:
    No module-level attributes

'''


class Square:
    '''Defines a square'''

    def __init__(self, size=0):
        '''Class constructor. Initialises instance variables of objects

        Args:
            size (int): The dimension of the square. Must be an integer

        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        '''Calculates the area of the square'''

        return self.__size ** 2
