#!/usr/bin/python3
'''Defines a function is_kind_of_class(obj, a_class)'''


def is_kind_of_class(obj, a_class):
    '''Checksis an object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class

    Returns:
        bool: True if all the above conditions are met, otherwise False
    '''

    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False


if __name__ == "__main__":
    is_kind_of_class(obj, a_class)
