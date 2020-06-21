"""
Sam Goode
sgoode1@dmacc.edu
6/18/2020
This program is supposed to return the index of an object and
the other function will sort them but I can not seem to get it working.
"""


def sort_list(lst):
    length = len(lst)
    for i in range(length):
        for j in range(0,length-1-i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]


def search_list(lst,value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1
