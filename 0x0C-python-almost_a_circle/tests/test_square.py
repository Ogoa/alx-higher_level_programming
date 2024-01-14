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


if __name__ == "__main__":
    unittest.main()
