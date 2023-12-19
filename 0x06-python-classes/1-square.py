#!/usr/bin/python3
'''This module defines a class Square

Attributes:
    No module level attributes

'''


class Square:
    '''Defines a square'''

    def __init__(self, size):
        '''Initialises the instance variables of an object

        Args:
           size (int): The dimensions of the square. It is a private field

        '''
        self.__size = int(size)  #: Assign the value
