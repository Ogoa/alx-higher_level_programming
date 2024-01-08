#!/usr/bin/python3
'''Defines a class MyList that inherits from built-in list'''


class MyList(list):
    '''Definition of the class MyList'''

    def print_sorted(self):
        '''Prints the list, but in ascending order'''

        print(sorted(self))

    def append(self, data):
        '''Appends an element to the list

        Args:
            data (int): Data value being appended to the list

        Raises:
            TypeError: if data is not an integer
        '''

        if not isinstance(data, int) or isinstance(data, bool):
            raise TypeError("data must be an int")

        super().append(data)
