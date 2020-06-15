"""
Program: test_string_functions.py
Author:  Sam Goode
Date: 06/14/2020
This program tests a function that asks a user how many times they want the string
'message' to be printed out on the screen
"""


import unittest
import unittest.mock as mock
from more_functions import string_functions as str_func


class MyTestCase(unittest.TestCase):

    def test_multiple_strings(self):
        self.assertEqual('messagemessagemessage', str_func.multiply_string())
        self.assertEqual('messagemessagemessagemessagemessagemessagemessage', str_func.multiply_string())


if __name__ == '__main__':
    unittest.main()
