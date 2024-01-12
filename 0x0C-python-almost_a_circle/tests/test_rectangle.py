#!/usr/bin/python3
'''Defines aunit test for the `rectangle` module'''
import unittest
import sys
from io import StringIO
sys.path.append("..")
from models.rectangle import Rectangle
from models.rectangle import Base


class TestRectangle(unittest.TestCase):
    '''Defines test cases for the `rectangle` module'''

    def test_subclass(self):
        '''Ensures that Rectangle is subclasses from the Base class'''

        r1 = Rectangle(5, 6, 0, 1, 1)
        self.assertTrue(isinstance(r1, Base))

    def test_values(self):
        '''Ensures value errors are raised when the wrong argument
        values are passed to either the setter methods or when
        initialising an object
        '''

        with self.assertRaises(ValueError):
            r2 = Rectangle(3, 0, 5, 6, 2)
            r3 = Rectangle(-1, 5, 5, 6, 3)
            r4 = Rectangle(3, 4, -1, 7, 4)
            r5 = Rectangle(3, 4, 3, -1, 5)
            r5.width = 0
            r5.width = -1
            r5.height = 0
            r5.height = -1
            r5.x = -4
            r5.y = -9

    def test_types(self):
        '''Ensures type errors are raised when the wrong argument types
        are passed to either the setter methods or when initialising
        an object
        '''

        with self.assertRaises(TypeError):
            r6 = Rectangle(3, "4", 3, 5, 6)
            r7 = Rectangle(True, 4, 3, 5, 7)
            r8 = Rectangle(3 + 5j, 4, 4, 5, 8)
            r9 = Rectangle("string", 4, 3, 5, 9)
            r10 = Rectangle(7, False, 3, 5, 10)
            r9.width = True
            r9.width = 4 + 8j
            r9.width = "test"
            r9.height = False
            r9.height = 4 + 8j
            r9.height = "test"
            r9.x = "test"
            r9.x = True
            r9.y = "test"
            r9.y = 5 + 5j

    def test_presence_of_attributes(self):
        '''Ensures an instantiated object has all the attributes
        and that they are correctly assigned
        '''

        r11 = Rectangle(7, 8, 3, 5, 11)
        self.assertEqual(len(r11.__dict__), 5)
        self.assertEqual(r11.width, 7)
        self.assertEqual(r11.height, 8)
        self.assertEqual(r11.x, 3)
        self.assertEqual(r11.y, 5)
        self.assertEqual(r11.id, 11)

    def test_area_calculation(self):
        '''Evaluates if the result returned from the area() method
        is an accurate calculation of the objects area
        given the dimensions
        '''

        r12 = Rectangle(3, 4, 1, 1, 12)
        self.assertEqual(r12.area(), 12)
        r12.width = 2
        r12.height = 10
        self.assertEqual(r12.area(), 20)

    def test_display_rectangle(self):
        '''Ensures that a representation of an object is
        printed correctly on stdout using the # character
        '''

        r13 = Rectangle(3, 4, 0, 0, 13)
        r13.display()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "###\n###\n###\n###")

    def setUp(self):
        '''Redirect sys.stdout to capture the printed characters
        '''
        self.old_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        '''Restore sys.stdout'''

        sys.stdout = self.old_stdout


if __name__ == "__main__":
    unittest.main()
