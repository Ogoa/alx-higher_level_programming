#!/usr/bin/python3
'''Defines a function class_to_json()'''


def class_to_json(obj):
    '''Returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj (obj): Instance of a class
    '''

    return obj.__dict__


if __name__ == "__main__":
    class_to_json(obj)
