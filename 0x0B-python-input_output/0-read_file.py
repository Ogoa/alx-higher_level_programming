#!/usr/bin/python3
'''Defines a function read_file()'''


def read_file(filename=""):
    '''Reads a text file and prints it to stdout

    Args:
        filename (str): Name of the text file
    '''

    with open(filename, "r", encoding="utf-8") as f:
        content = f.readlines()
        for line in content:
            print(line, end="")


if __name__ == "__main__":
    read_file(filename)
