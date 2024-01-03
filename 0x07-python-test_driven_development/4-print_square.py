#!/usr/bin/python3
'''A module implementing a function that prints a square using
the character `#`

Function suplied, print_square():
    >>> print_square(4)
    ####
    ####
    ####
    ####
'''


def print_square(size):
    '''Prints a square using the `#` character

    Args:
        size (int): The dimensions of the square

    Raises:
        TypeError: If size is not an integer or has a value less than 0
        Also, if size is a float and is less than 0
    '''

    if not isinstance(size, int) or (isinstance(size, float) and size < 0)\
            or isinstance(size, bool):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
