#!/usr/bin.python3
'''Defines a function load_from_json_file()'''
import json


def load_from_json_file(filename):
    '''Deserializes a JSON string from a file to a Python dictionary

    Args:
        filename (str): Name of the file containing the JSON string
    '''

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
