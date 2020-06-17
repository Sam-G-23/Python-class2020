"""
Program: test_string_functions.py
Author:  Sam Goode
Date: 06/14/2020
This program tests the functions of inner_functions_assignment
"""


import unittest
from more_functions import inner_functions_assignment as inn


# given unit test
class MyTestCase(unittest.TestCase):

    def test_measurements_rectangle(self):
        # access measurements function using 'inn' which is for imported python file
        self.assertEqual(inn.measurements([2.1, 3.4]), "Perimeter = 11.0 Area = 7.14")

    def test_measurements_square(self):
        self.assertEqual(inn.measurements([3.5]), "Perimeter = 14.0 Area = 12.25")


if __name__ == '__main__':
    unittest.main()
