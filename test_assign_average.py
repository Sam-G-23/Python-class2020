"""
Sam Goode
sgoode1@dmacc.edu
6/25/2020
This program tests the switch_average program
"""


import unittest
import assign_average as aa


class MyTestCase(unittest.TestCase):
    def test_Aa(self):
        self.assertEqual("one", aa.switch_average('A'))
        self.assertEqual("one", aa.switch_average('a'))

    def test_Bb(self):
        self.assertEqual("two", aa.switch_average('B'))
        self.assertEqual("two", aa.switch_average('b'))

    def test_Cc(self):
        self.assertEqual("three", aa.switch_average('C'))
        self.assertEqual("three", aa.switch_average('c'))

    def test_Dd(self):
        self.assertEqual("four", aa.switch_average('D'))
        self.assertEqual("four", aa.switch_average('d'))

    def test_Ee(self):
        self.assertEqual("five", aa.switch_average('E'))
        self.assertEqual("five", aa.switch_average('e'))

    def test_non_key(self):
        self.assertEqual("wrong key", aa.switch_average('R'))


if __name__ == '__main__':
    unittest.main()
