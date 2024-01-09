#!/usr/bin/python3
'''Defines a function from_json_string()'''
import json


def from_json_string(my_str):
    '''Deserialize a JSON string to a Python dictionary object

    Returns:
        dict: The python object
    '''

    return json.loads(my_str)


if __name__ == "__main__":
    from_json_string(my_str)
