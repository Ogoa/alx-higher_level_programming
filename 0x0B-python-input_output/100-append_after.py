#!/usr/bin/python3
'''Defines the function append_after()'''


def append_after(filename="", search_string="", new_string=""):
    '''Inserts a line of text to a file, after each line containing
    a specific string

    Args:
        filename (str): name of the file
        search_string (str): string after which the line of text is to
        be inserted
        new_string (str): string being inserted
    '''

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            if search_string in line:
                line = line.rstrip() + "\n" + new_string
            f.write(line)


if __name__ == "__main__":
    append_after(filename, search_string, new_string)
