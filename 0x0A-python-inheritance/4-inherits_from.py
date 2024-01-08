#!/usr/bin/python3
'''Defines the function inherits_from()'''


def inherits_from(obj, a_class):
    '''Evaluates if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj (obj): The object being evaluated
        a_class (obj): The class @obj is being compared to

    Return:
        bool: True if the condition is satisfied, otherwise false
    '''

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
