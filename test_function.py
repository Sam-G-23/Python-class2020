import unittest
from main import camper_age_input as cai


class FunctionTestCase(unittest.TestCase):
    def test_months(self):
        self.assertEqual(84, cai.months(7))


if __name__ == '__main__':
    unittest.main()
