"""
Sam Goode
sgoode1@dmacc.edu
6/18/2020
This code tests the sort and search array.py I am not sure if this type of test works or not.
I have been trying to get it to call the individual functions but to no avail.
"""



from topic4 import sort_and_search_array


def test_sort(lst):
    new_lst = sorted(lst)
    sort_list(lst)
    if lst == new_lst:
        print("Test Passed")
    else: # else test fails
        print("Test Failed")


def test_search(lst,value):
    index = search_list(lst,value)
    if index == -1:
        print(value,"not present in the list")
    else:
        print(value ," present in the list at index: ",index)

l = [8,3,2,4,1]

test_search(l,9)
test_search(l,2)

test_sort(l)
