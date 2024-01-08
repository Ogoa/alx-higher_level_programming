#!/usr/bin/python3
'''Defines a function that lists the attributes of an object'''


def lookup(obj):
    '''Lists the available attributes and methods if an object

    Args:
        obj (obj): An object

    Returns:
        A list of available attributes and methods
    '''

    return list(dir(obj))
