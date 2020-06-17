"""
Program: test_string_functions.py
Author:  Sam Goode
Date: 06/14/2020
This program tests the valid input functions program and most of the possible bad inputs that could be given.
"""


import unittest
import unittest.mock as mock
from more_functions import validate_input_in_functions as val_func


class FunctionTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(val_func.score_input("score"), "score: 0")

    def test_score_input_test_score_valid(self):
        self.assertEqual(val_func.score_input("score", 88), "score: 88")

    def test_score_input_test_score_below_range(self):
        self.assertEqual(val_func.score_input("score", -1), "Invalid test score, try again!")

    def test_score_input_test_score_above_range(self):
        self.assertEqual(val_func.score_input("score", 101), "Invalid test score, try again!")

    def test_test_score_non_numeric(self):
        with self.assertRaises(TypeError):
            val_func.score_input("score", "test")

    def test_score_input_invalid_message(self):
        self.assertEqual(val_func.score_input("score", 95, "Bad score input"), "score: 95")


if __name__ == '__main__':
    unittest.main()
