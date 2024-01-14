#!/usr/bin/python3
'''Defines a class Base'''
import json


class Base:
    '''A class that will be the base class of all other classes
    defined in modules within this directory
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialises an instance of the class

        Args:
            id (int): identification number of the instance
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        '''Serialises a list of dictionaries into a JSON string

        Returns:
        str: serialise JSON object
        '''

        if list_dictionaries is None or len(list_dictionaries) < 1:
            return json.dumps("[]")
        else:
            return json.dumps(list_dictionaries)
