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

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes a JSON string representation of a list of instances
        that are subtypes of the Base class

        Args:
            list_objs (obj): A list of objects, subclassed form Base
        '''

        filename = str(type(list_objs[0]).__name__) + ".json"

        dict_list = []
        for x in list_objs:
            dict_list.append(x.to_dictionary())

        with open(filename, "w") as f:
            f.write(Base.to_json_string(dict_list))

    def from_json_string(json_string):
        '''Returns a list of the JSON string representation
        of the object
        '''

        if json_string is None or len(json_string) < 1:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set
        Args:
            dictionary (dict): key, value pairs of the aattibutes
        '''

        dummy = None
        if cls.__name__ == "Rectangle":
            dummy = cls(4, 5, 6, 7)
        elif cls.__name__ == "Square":
            dummy = cls(4, 6, 7)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances'''

        filename = str(cls.__name__) + ".json"
        instances = []
        obj_list = []
        contents = ""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                contents = f.read()
                obj_list = cls.from_json_string(contents)
        except FileNotFoundError:
            return []

        for x in obj_list:
            instances.append(cls.create(**x))

        return instances
