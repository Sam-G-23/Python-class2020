"""
Program: test_coupon_calculations.py
Author:  Sam Goode
Date: 06/8/2020
This program tests a function prompts user for the price of their order, any cash coupons and percent coupons
then returns to the user the total price after both coupons, shipping, and sales tax are applied to it.
"""
import unittest
import unittest.mock as mock
from topic3 import coupon_calculations as cc

# I dont really understand why but I am getting an error message saying the equation spit out the value for
# the line below the one I am testing at any given attempt
class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(cc.calculate_price(10, 5, 10), 10.72, places=4)
        self.assertAlmostEqual(cc.calculate_price(10, 5, 15), 10.46, places=4)
        self.assertAlmostEqual(cc.calculate_price(10, 5, 20), 10.19, places=4)
        self.assertAlmostEqual(cc.calculate_price(10, 10, 10), 5.95, places=4)
        self.assertAlmostEqual(cc.calculate_price(10, 10, 15), 5.95, places=4)
        self.assertAlmostEqual(cc.calculate_price(10, 10, 20), 5.95, places=4)
# Creating as many test cases as I could think of in the most effective time
    def test_price_under_between_ten_thirty(self):
        self.assertAlmostEqual(cc.calculate_price(15, 5, 10), 15.49, places=4)
        self.assertAlmostEqual(cc.calculate_price(15, 5, 15), 14.96, places=4)
        self.assertAlmostEqual(cc.calculate_price(15, 5, 20), 14.43, places=4)
        self.assertAlmostEqual(cc.calculate_price(20, 10, 10), 14.96, places=4)
        self.assertAlmostEqual(cc.calculate_price(20, 10, 15), 14.96, places=4)
        self.assertAlmostEqual(cc.calculate_price(20, 10, 20), 14.43, places=4)
        self.assertAlmostEqual(cc.calculate_price(25, 5, 10), 27.03, places=4)
        self.assertAlmostEqual(cc.calculate_price(25, 5, 15), 25.97, places=4)
        self.assertAlmostEqual(cc.calculate_price(25, 5, 20), 24.91, places=4)
        self.assertAlmostEqual(cc.calculate_price(30, 10, 10), 27.03, places=4)
        self.assertAlmostEqual(cc.calculate_price(30, 10, 15), 25.97, places=4)
        self.assertAlmostEqual(cc.calculate_price(30, 10, 20), 24.91, places=4)
# The testing gets long here I was not sure how many you were expecting so I am trying for too much
    def test_price_under_between_thirty_fifty(self):
        self.assertAlmostEqual(cc.calculate_price(35, 5, 10), 36.57, places=4)
        self.assertAlmostEqual(cc.calculate_price(35, 5, 15), 34.98, places=4)
        self.assertAlmostEqual(cc.calculate_price(35, 5, 20), 33.39, places=4)
        self.assertAlmostEqual(cc.calculate_price(40, 10, 10), 36.57, places=4)
        self.assertAlmostEqual(cc.calculate_price(40, 10, 15), 34.98, places=4)
        self.assertAlmostEqual(cc.calculate_price(40, 10, 20), 33.39, places=4)
        self.assertAlmostEqual(cc.calculate_price(45, 5, 10), 50.11, places=4)
        self.assertAlmostEqual(cc.calculate_price(45, 5, 15), 47.99, places=4)
        self.assertAlmostEqual(cc.calculate_price(45, 5, 20), 45.87, places=4)
# This is the between thirty and fifty
    def test_price__over_fifty(self):
        self.assertAlmostEqual(cc.calculate_price(50, 10, 10), 50.11, places=4)
        self.assertAlmostEqual(cc.calculate_price(50, 10, 15), 47.99, places=4)
        self.assertAlmostEqual(cc.calculate_price(50, 10, 20), 45.87, places=4)
        self.assertAlmostEqual(cc.calculate_price(55, 10, 10), 54.88, places=4)
        self.assertAlmostEqual(cc.calculate_price(55, 10, 15), 52.50, places=4)
        self.assertAlmostEqual(cc.calculate_price(55, 10, 20), 50.11, places=4)
        self.assertAlmostEqual(cc.calculate_price(60, 5, 10), 64.42, places=4)
        self.assertAlmostEqual(cc.calculate_price(60, 5, 15), 47.99, places=4)
        self.assertAlmostEqual(cc.calculate_price(60, 5, 20), 61.51, places=4)
        self.assertAlmostEqual(cc.calculate_price(65, 10, 10), 64.42, places=4)
        self.assertAlmostEqual(cc.calculate_price(65, 10, 15), 61.51, places=4)
        self.assertAlmostEqual(cc.calculate_price(65, 10, 20), 58.59, places=4)
# finally the over fifty

# The code seems to be working fine I am unsure of what I have wrong I believe it is on this test

if __name__ == '__main__':
    unittest.cc()
# After about a dozen hours I cant seem to find anything of relevance about my described is I can only really turn it in
# Every time I test it on my own it passes. The math is right I triple checked that, the lines are marked w/ correct answer
# I really wish there was more in depth on the unitesting and what exactly is going on here because me on my own is not
# generating the desired results
