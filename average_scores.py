"""
This supposed to take 3 inputs convert to an int and spit out an average score
Sam Goode sgoode1@dmacc.edu 6/4/2020
"""
# Inputs for the user and total to simplify the function below
test1 = 0
test2 = 0
test3 = 0


def average(test1, test2, test3):
    input("Please input your full name. ")
    test1 = int(input("Now your first test grade. "))
    if (test1 >= 0) and (test1 <= 100):
        try:
            print("Thank you.")
        except:
            print("Invalid input please try again. Try again>")
    test2 = int(input("Now your second test. "))
    if (test2 >= 0) and (test2 <= 100):
        try:
            print("Thank you.")
        except:
            print("Invalid input please try again. Try again>")
    test3 = int(input("Now your second test. "))
    if (test3 >= 0) and (test3 <= 100):
        try:
            print("Thank you.")
        except:
            print("Invalid input please try again. Try again>")
    final_avg_test = (test1 + test2 + test3) / 3
    return average(test1 + test2 + test3)
# Calculating average


if __name__ == "__main__":
    print("Congrats, your average test score is:", average(test1, test2, test3))
# Print out the test score





