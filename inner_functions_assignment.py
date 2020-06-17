"""
Program: test_string_functions.py
Author:  Sam Goode
Date: 06/14/2020
This code is supposed to calculate the area and perimeter of a rectangle/ or square.
"""


def measurements(a_list):
    # inner function calls
    def area(a_list):
        # for square
        if len(a_list) == 1:
            a = a_list[0] * a_list[0]
        # for rectangle
        elif len(a_list) == 2:
            a = a_list[0] * a_list[1]
        # neither square nor rectangle
        else:
            a = -1
        # return the result to caller
        return a
    def perimeter(a_list):
        # for square
        if len(a_list) == 1:
            p = 4 * a_list[0]
        # for rectangle
        elif len(a_list) == 2:
            p = 2 * (a_list[0] + a_list[1])
        # neither square nor rectangle
        else:
            p = -1
        # return the result to caller
        return p

    #continue measurements code; calling inner functions
    a = area(a_list)
    p = perimeter(a_list)
    # building a string with results
    some_string = "Perimeter = " + str(p) + " Area = " + str(a)
    # return the string
    return some_string
    # function definition
