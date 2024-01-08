#!/usr/bin/python3
'''Defines a function is_same_class()'''


def is_same_class(obj, a_class):
    '''Evaluates if an object is exactly an instance ofa specified class

    Args:
        obj (obj): The object being evaluated
        a_class (obj): The class @obj is being checked against

    Returns:
        bool: True if @obj is an instance of @a_class, otherwise False
    '''

    if isinstance(obj, a_class) and a_class is not object:
        return True
    return False


if __name__ == "__main__":
    is_same_class(obj, a_class)
