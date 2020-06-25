"""
Sam Goode
sgoode1@dmacc.edu
6/25/2020
This program is supposed to output a number grade for each conventional letter grade.
"""

def switch_average(inp):
    grades_dict = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 50 }
    inp = inp.upper()
    res = grades_dict.get(inp, 'Invalid Grade')
    # get function for a dictionary will return value of key provided
    # if the key is not found it will return the second argument in the function.
    return res


print(switch_average('A'))
print(switch_average('a'))
print(switch_average('B'))
print(switch_average('b'))
print(switch_average('C'))
print(switch_average('c'))
print(switch_average('D'))
print(switch_average('d'))
print(switch_average('F'))
print(switch_average('f'))
