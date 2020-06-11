"""
Sam Goode
sgooode1@dmacc.edu
6/10/2020
The objection for this program is to create two for loops one that creates and prints out a list of floating numbers
and a second that displays them backwards from 99 to 33
"""


list_float = [1.5, 2.2, 3.4]
for list_float in range(0, 4):
    print(list_float)
# Range is only allowed to print integers and no floats or strings without some import or tweaking a generator.
# The range keyword will give the user back integers instead of the floats in the list

for x in reversed(range(100)):
    print(x)
# Using the reversed key word to accomplish the task being asked
# Added not apparently reversed does not work for an object that is an int and needs to be used on
# This is the error that is displayed 'TypeError: 'int' object is not reversible'


