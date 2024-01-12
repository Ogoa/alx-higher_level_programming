#!/usr/bin/python3
'''Defines the class Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''Inherits from the Base class
    Represents a rectangle polygon
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialises a Rectangle object

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x-axis dimensions
            y (int): y-axis dimensions
            id (int): identification number of the object

        Raises:
            TypeError: if any of the arguments is not of the appropriate type
            ValueError: if either width, height, x or y is less than 0
        '''

        init_args = {"width": width, "height": height, "x": x, "y": y}
        for arg in list(init_args):
            self._check_type(init_args[arg], arg)
            self._check_value(init_args[arg], arg)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def _check_type(self, value, attribute):
        '''Checks if the object type is appropriate

        Args:
            value (int): checks if this is an integer
            attribute (str): object attribute being validated
        Raises:
            TypeError: if @value is not an integer
        '''

        if not type(value) in [int]:
            raise TypeError("{} must be an integer".format(attribute))

    def _check_value(self, value, attribute):
        '''Checks if the object value is appropriate

        Args:
            value (int): checks if this is a positive integer
            for 'width' and 'height', it should be greater than 0
            for 'x' and 'y', it should be greater or equal to 0
            attribute (str): object attribute being checked

        Raises:
            ValueError: if @value does not meet the specified conditions
        '''

        if attribute in ["width", "height"]:
            if value <= 0:
                raise ValueError("{} must be > 0".format(attribute))
        elif attribute in ["x", "y"]:
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))

    @property
    def width(self):
        '''Retrieves the width of the rectangle

        Has a setter that performs type and value checks for data validation
        '''

        return self.__width

    @width.setter
    def width(self, value):

        self._check_type(value, "width")  #: Perform data validation
        self._check_value(value, "width")
        self.__width = value

    @property
    def height(self):
        '''Retrieves the height of the rectangle

        Has a setter that performs type and value checks for data validation
        '''

        return self.__height

    @height.setter
    def height(self, value):

        self._check_type(value, "height")
        self._check_value(value, "height")
        self.__height = value

    @property
    def x(self):
        '''Retrieves the value of x

        Has a setter that performs type and value checks for data validation
        '''

        return self.__x

    @x.setter
    def x(self, value):

        self._check_type(value, "x")
        self._check_value(value, "x")
        self.__x = value

    @property
    def y(self):
        '''Retrieves the value of y

        Has a setter that performs type and value checks for data validation
        '''

        return self.__y

    @y.setter
    def y(self, value):

        self._check_type(value, "y")
        self._check_value(value, "y")
        self.__y = value
