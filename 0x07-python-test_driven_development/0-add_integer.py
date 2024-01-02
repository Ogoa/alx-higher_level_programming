#!/usr/bin/python3
'''This module implements the add_integer function
This module supplies the function, add_integer().
>>> add_integer(3, 4)
7
'''


def add_integer(a, b=98):
    '''Adds two integers or floats and returns their sum
    If a or b are floats, they are casted to integers
    '''

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
