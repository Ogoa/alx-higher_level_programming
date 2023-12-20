#!/usr/bin/python3
'''Defines a class Square

Attributes:
    No module-level attributes

'''


class Square:
    '''Defines a square'''

    def __init__(self, size=0, position=(0, 0)):
        '''Class constructor. Initialises instance variables of objects

        Args:
            size (int): The dimension of the square. Must be an integer
            position (tuple): Coordinates of the square

        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple) or \
                len(position) != 2 or \
                not isinstance(position[0], int) and not \
                isinstance(position[1], int) or\
                position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    def area(self):
        '''Calculates the area of the square'''

        return self.__size ** 2

    def my_print(self):
        '''Prints the square in stdout'''

        [print() for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for i in range(self.__position[0])]
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print()

    @property
    def size(self):
        '''Retrieves the value of size of a Square instance'''

        return self.__size

    @size.setter
    def size(self, value):
        '''Sets the value of size

        Args:
            value (int): The integer value being assigned to size
        '''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        '''Retrieves the position of a Square instance'''

        return self.__position

    @position.setter
    def position(self, value):
        '''Sets the value of position

        Args:
            value (tuple): The coordinate of the square

        '''

        if not isinstance(value, tuple) or \
                len(value) != 2 or \
                not isinstance(value[0], int) and not \
                isinstance(value[1], int) or\
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")


    def __str__(self):
        '''Converts the square to a string'''

        full_string = []

        full_string.append('\n' * self.__position[1])

        for i in range(self.__size):
            full_string.append(' ' * self.__position[0] + '#' * self.__size)
            if i == self.__size - 1:
                continue
            full_string.append('\n')

        return "".join(full_string)
