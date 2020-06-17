"""
Program: test_string_functions.py
Author:  Sam Goode
Date: 06/14/2020
This program utilizes that takes parameter arguments and validates the test_score variable.
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    Returns
    :param1 test_name: name of the test
    :param2 test_score: optional test score
    :param3 invalid_message: optional invalid message
    :returns test_name and test_score in a string
    """
    try:
        if test_score < 0 or test_score > 100:
            return invalid_message
        else:
            test_name_and_score = (test_name + ": " + str(test_score))
    except ValueError as err:
        raise ValueError
    else:
        return test_name_and_score


if __name__ == '__main__':
    try:
        print(score_input("stuff", 2))
    except TypeError as err:
        print("Error, encountered")
