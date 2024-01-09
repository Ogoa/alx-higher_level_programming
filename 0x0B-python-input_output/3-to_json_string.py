#!/usr/bin/python3
'''Defines a function to_json_string()'''
import json


def to_json_string(my_obj):
    '''Serializes an object to a JSON string

    Returns:
        str: JSON string
    '''

    return json.dumps(my_obj, sort_keys=True)


if __name__ == "__main__":
    to_json_string(my_obj)
