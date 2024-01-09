#!/usr/bin/python
'''Defines a class BaseGeometry'''


class BaseGeometry:
    '''Definition of the BaseGeometry class'''

    def area(self):
        '''Function that raises an exception'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validates value

        Args:
            name (str): Name of the variable
            value (int): The variable

        Raises:
            TypeError: if @value if less than or equal to 0
            ValueError: if @value is not an integer
        '''

        if not isinstance(name, str):
            raise TypeError("name must be a string")

        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
