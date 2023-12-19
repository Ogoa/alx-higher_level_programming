#!/usr/bin/python3
'''A module with the definition of a class Square

Attributes:
    No module-level attributes

'''


class Square:
    '''Defines a square'''

    def __init__(self, size=0):
        '''Initialises the instance variables of an object

        Args:
            size (int): The dimensions of the square. Has\
                    a default value of 0 and must always be an integer

        '''

        if not isinstance(size, int):

            raise TypeError("size must be an integer")
        if size < 0:  #: Raise an exception if size is less than 0
            raise ValueError("size must be >= 0")

        self.__size = size
