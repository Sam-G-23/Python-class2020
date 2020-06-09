"""
This is supposed to test average_scores.py
Sam Goode sgoode1@dmacc.edu 6/4/2020
"""
import unittest
import unittest.mock as mock
from format_output import average_scores as avg
# importing from the other file for this project

class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', average=[85,90,95]):
            self.assertAlmostEqual(avg.average, 90, places=4)
    pass
# So I was not 100% sure if the assert argument was right or not but the test is passing
    def test_average_negative_input(self):
        with self.assertRaises(ValueError):
            avg.average()

if __name__ == '__main__':
    unittest.main()
# I am lost.
# I have no idea what I am doing with this test assert
