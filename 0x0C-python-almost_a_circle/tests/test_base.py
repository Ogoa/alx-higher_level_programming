#!/usr/bin/python3
'''Defines unit tests for the `base` module'''
import unittest
import sys
sys.path.append("..")
from models.base import Base


class TestBaseClass(unittest.TestCase):
    '''Defines test cases for the base class

    An assumption made is that the argument `id` that is passed into
    the class constructor will always be an integer, therefore,
    a test for the type is not necessary
    '''

    def test_init(self):
        '''Ensures that the dunder init function is working as expected'''

        b1 = Base()
        b2 = Base()
        b3 = Base(9)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 9)
        self.assertEqual(b4.id, 3)


if __name__ == "__main__":
    unittest.main()
