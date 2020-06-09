"""
program: coupon_calculations.py
Name: Sam Goode
date: 6/8/2020
prompts user for the price of their order, any cash coupons and percent coupons
then returns to the user the total price after both coupons, shipping, and sales tax are applied to it.
"""


def calculate_price(price, cash_coupon, percent_coupon):
    price = int(input("What is the price of your order? "))
    cash_coupon = int(input("Do you have any cash coupons you would like to use? "))
    new_price = price - cash_coupon
    percent_coupon = int(input("How about any regular coupons? "))
    pre_tax_price = new_price - new_price * (percent_coupon / 100)
    tax = 0.06
# storing variables and manipulating the ones I can
    if pre_tax_price <= 10:
        shipping = 5.95
        print("Your shipping will be","$", 5.95)
    elif 10 < pre_tax_price <= 30:
        shipping = 7.95
        print("Your shipping will be","$", 7.95)
    elif 30 < pre_tax_price < 50:
        shipping = 11.95
        print("Your shipping will be","$", 11.95)
    elif 50 <= pre_tax_price:
        shipping = 0
        print("Congrats! Your shipping is free today.")
# I decided the elif was the perfect statement for this so I could have the machine continually look to see where
# each order was going to fall into shipping wise
    total = round(pre_tax_price + (tax * pre_tax_price)+ shipping, 2)
    print("Your price was, $", price, "but with your cash coupon of $", cash_coupon, "and", percent_coupon, "% off coupon.")
    print("Your new total is $", total, "!")
    return total


if __name__ == '__main__':
    calculate_price('price', 'cash_coupon', 'percent_coupon')
# Overall I believe this could works well perhaps a few things can change but for the most part this does as needed
# assuming good inputs are made of course.
