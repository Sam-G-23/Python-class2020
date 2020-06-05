import unittest
import unittest.mock as mock
from format_output import average_scores as avg


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', average=[85,90,95]):
            assert avg.average(total=270) == 90


if __name__ == '__main__':
    unittest.main()
