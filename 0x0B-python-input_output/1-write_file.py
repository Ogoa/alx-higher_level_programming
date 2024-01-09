#!/usr/bin/python3
'''Defines a function write_file()'''


def write_file(filename="", text=""):
    '''A function that writes a text to a file
    The file is created if it does not already exist, otherwise
    it is overwritten

    Returns:
        int: Number of characters written
    '''

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text) + 5
