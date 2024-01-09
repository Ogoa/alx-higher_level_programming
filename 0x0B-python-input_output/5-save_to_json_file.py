#!/usr/bin/python3
'''Defines a function save_to_json_file()'''
import json


def save_to_json_file(my_obj, filename):
    '''Writes a serialised JSON string in a text file

    Args:
        my_obj (obj): Python object
        filename (str): Name of the text file
    '''

    with open(filename, "w", encoding="utf-8") as f:
        json_obj = json.dumps(my_obj)
        f.write(json_obj)


if __name__ == "__main__":
    save_to_json_file(my_bj, filename)
