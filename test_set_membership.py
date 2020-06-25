import unittest
from more_fun_with_collections import set_membership


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        test_set = {1, 3, 5, 56, 78}
        test_num = 3
        expected_output = True
        self.assertEqual(expected_output, set_membership.in_set(test_set, test_num))
    def test_in_set_false(self):
        test_set = {1, 3, 5, 56, 78}
        test_num = 7
        expected_output = False
        self.assertEqual(expected_output, set_membership.in_set(test_set, test_num))


if __name__ == '__main__':
    unittest.main()
