def in_set(the_set, num):
    """
    Return true if the num is in the set
    False other wise
    """
    return num in the_set


if __name__ == '__main__':
    print(in_set({1, 3, 5}, 3))
