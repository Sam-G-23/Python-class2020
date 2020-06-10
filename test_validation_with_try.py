"""
This is supposed to test average_scores.py
Sam Goode sgoode1@dmacc.edu 6/4/2020
"""
import unittest
import unittest.mock as mock
from input_validation import input_validation_with_try as avg
# importing from the other file for this project


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            self.assertAlmostEqual(avg.average(), 90, places=4)
# So I was not 100% sure if the assert argument was right or not but the test is passing

    def test_average_negative_input(self):
        with mock.patch('builtins.input', side_effect=[-90, 85, 95]):
            with self.assertRaises(ValueError):
                avg.average()
# Ok after taking your advice, this test worked as intended thank you Professor.
# I have to practice and read a lot more about this and the implications of these tests.

    def test_average_second_negative_input(self):
        with mock.patch('builtins.input', side_effect=[90, -85, 95]):
            with self.assertRaises(ValueError):
                avg.average()
# After several hours working on this I finally got it going with what you suggested.
# I was initially able to get the first two tests working but the third was giving me issues
# I had to rewrite the code in the way you wrote it out to get it all working.

    def test_average_second_negative_input(self):
        with mock.patch('builtins.input', side_effect=[90, 85, -95]):
            with self.assertRaises(ValueError):
                avg.average()
# The last test was pretty simple all I did was copy/paste it onto line 32


if __name__ == '__main__':
    unittest.main()
# I think the hardest part of all of this is that I do not really have a book readily available to review like my
# c++ class. I will need to review all the test references you have provided again to get a better grasp on
# what is going on in the code.
