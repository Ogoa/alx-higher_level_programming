#!/usr/bin/python3
'''Module that implements a function to print a name
Function supplied, say_my_name():
    >>> say_my_name("John", "Smith")
    My name is John Smith
'''


def say_my_name(first_name, last_name=""):
    '''Prints a persons two names with the prefix "My name is"

    Args:
        first_name (str): First name
        last_name (str): Second name
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
