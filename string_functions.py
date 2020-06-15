"""
program: string_functions.py
Sam Goode
sgoode1@dmacc.edu
6/13/2020
The purpose of this program to to calculate a users input so that they can determine their hourly wage
"""


def multiply_string():
    """
    :param string_multiplier: represents the string used to multiply as 'message'
    :param n: represents the number 3
    :return: the mathematical operation as multi
    """
    n = int(input("Please input an integer: "))
    string_multiplier = 'message'
    multi = n * string_multiplier
    return multi


if __name__ == '__main__':
    print(multiply_string())

# Everything seems to be working perfectly with no issues
