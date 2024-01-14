#!/usr/bin/python3
'''Defines a class Square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Defines the class Square
    It inherits from the Rectangle class
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialises the object

        Args:
        size (int): dimensions of the square
        x (int): x-axis dimensions
        y (int): y-axis dimensions
        id (int): identification of the object
        '''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns a string representation of the object'''

        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    @property
    def size(self):
        '''Retrieves the size attribute of the object

        Has a setter that conducts type and value checks to ensure
        the data entered is valid
        '''

        return super().width

    @size.setter
    def size(self, value):

        self._check_type(value, "width")
        self._check_type(value, "width")
        self.width = value
        self.height = value

    def to_dictionary(self):
        '''Returns the dictionary representation of the object'''

        obj_dict = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
            }
        return obj_dict
