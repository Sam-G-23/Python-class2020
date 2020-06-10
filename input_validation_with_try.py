"""
Sam Goode sgoode1@dmacc.edu 6/4/2020
This supposed to take 3 inputs convert to an int and spit out an average score
and on top of that it is supposed to spit out an error if a good input
is given and that input is also an integer and not a str.

I went with the If-else statement per your recommendation I did try doing elif but
I did not know really where to go with it and I felt I was over complicating the code.

Inputs for the user and total to simplify the function below
After opting for your suggestion the code works perfectly
"""


def average():
    try:
        test1 = int(input("Now your first test grade. "))
        if (test1 >= 0) and (test1 <= 100):
            print("Thank you.")
        else:
            print('input not between 0 and 100')
            raise ValueError
    except:
        print('could not convert to int')
        raise ValueError
    try:
        test2 = int(input("Now your second test grade. "))
        if (test2 >= 0) and (test2 <= 100):
            print("Thank you.")
        else:
            print('input not between 0 and 100')
            raise ValueError
    except:
        print('could not convert to int')
        raise ValueError
    try:
        test3 = int(input("Now your third test grade. "))
        if (test3 >= 0) and (test3 <= 100):
            print("Thank you.")
        else:
            print('input not between 0 and 100')
            raise ValueError
    except:
        print('could not convert to int')
        raise ValueError
    final_avg_test = ((test1 + test2 + test3) / 3)
    return final_avg_test
# Calculating average
# I am not really sure what to make of the PEP8 error except throws up.
# All the code seems to be working for the most part I have not noticed anything wrong with it at least.


if __name__ == "__main__":
    name = input("Please input your full name. ")
    print("Congrats,", name, "your average test score is:", average())
# Print out the test score
# Assuming good prompts are given, I know a stretch of the imagination this code should work as intended.
