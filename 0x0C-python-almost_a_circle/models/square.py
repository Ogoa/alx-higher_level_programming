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
