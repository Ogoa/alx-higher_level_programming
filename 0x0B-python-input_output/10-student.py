#!/usr/bin/python3
'''Defines a class Student'''


class Student:
    '''Has the public instance attributes:
    first_name
    last_name
    age
    '''

    def __init__(self, first_name, last_name, age):
        '''Initialises a Student object

        Args:
            first_name (str): First name
            last_name (str): Last name
            age (int): age of the student

        Raises:
            TypeError: if first_name or last_name arguments are not strings
            or if age is not an integer
            ValueError: if age is a value less than 0
        '''

        if not isinstance(first_name, str):
            raise TypeError("firstname must be string")

        if not isinstance(last_name, str):
            raise TypeError("lastname must be a string")

        if not isinstance(age, int) or isinstance(age, bool):
            raise TypeError("age must be an integer")

        if age < 0:
            raise ValueError("age must be greater or equal to 0")

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary representation of a Student object
        Args:
                attrs (obj): List of attributes to be retrieved
        '''

        if attrs is None:
            return self.__dict__

        my_obj = {}
        for i in attrs:
            if i in self.__dict__:
                my_obj[i] = self.__dict__[i]

        return my_obj
