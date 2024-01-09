#!/usr/bin/python3
'''Defines a class MyInt'''


class MyInt(int):
    '''Definition of a class MyInt
    Inherits from the class int'''

    def __eq__(self, value):
        '''Inverts the return value of the equality operation

        Returns:
            bool: False if the two operands are equivalent, otherwise True
        '''

        return not super().__eq__(value)

    def __ne__(self, value):
        '''Inverts the return value of the inequality operation

        Returns:
            bool: False if the two operands are not equivalent, otherwise True
        '''

        return not super().__ne__(value)
