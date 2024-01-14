#!/usr/bin/python3
'''Defines a unit test for the `square` module'''
import sys
import unittest
sys.path.append("..")
from models.square import Square


class TestSquare(unittest.TestCase):
    '''Defines test cases for the `square` module'''

    def test_correct_instantiation(self):
        '''Ensures that objects are correctly instantiated'''

        s1 = Square(3, 1, 2, 1)
        self.assertEqual((s1.id, s1.width, s1.height, s1.x, s1.y),
                         (1, 3, 3, 1, 2))

    def test_getter_and_setter_methods(self):
        '''Ensures that the getter and setter methods are
        working as expected. The setter methods should validate
        the arguments passed into it and raise type or value
        errors where necessary
        '''

        s2 = Square(5, 3, 2, 2)
        self.assertEqual(s2.size, 5)
        with self.assertRaises(TypeError):
            s2.size = True
            s2.size = "String"
            s2.size = 5 + 6j

        with self.assertRaises(ValueError):
            s2.size = -5
            s2.size = 0


if __name__ == "__main__":
    unittest.main()
