"""
Sam Goode sgoode1@dmacc.edu 6/4/2020
These tests are for testing the mathematical operators
"""
import unittest

class OperatorsTest(unittest.TestCase):
    def test_less_than_or_equal_to_false(self):
        self.assertFalse(3 <= 1)
    def test_less_than_or_equal_to_true(self):
        self.assertTrue(3 <= 5)
    def test_greater_than_or_equal_to_false(self):
        self.assertFalse(5 >= 6)
    def test_greater_than_or_equal_to_true(self):
        self.assertTrue(5 >= 3)
    def test_equal_false(self):
        self.assertFalse(5 == 4)
    def test_equal_true(self):
        self.assertTrue(5 == 5)
    def test_not_equals_false(self):
        self.assertFalse(5 != 5)
    def test_not_equals_True(self):
        self.assertTrue(5 != 4)
    def test_greater_than_false(self):
        self.assertFalse(5 > 6)
    def test_greater_than_true(self):
        self.assertTrue(5 > 3)
    def test_less_than_false(self):
        self.assertFalse(5 < 3)
    def test_less_than_true(self):
        self.assertTrue(3 < 5)
if __name__ == '__main__':
    unittest.main()
# Tested about a dozen times all good, unsure if I should of broken it up or kept it as is.
# Hard to look at is all.
