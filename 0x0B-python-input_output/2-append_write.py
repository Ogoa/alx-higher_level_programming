#!/usr/bin/python3
'''Defines a function append_write()'''


def append_write(filename="", text=""):
    '''Appends a string at the end of a text file

    Returns:
        int: The number of characters added
    '''

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)


if __name__ == "__main__":
    append_write(filename, text)
