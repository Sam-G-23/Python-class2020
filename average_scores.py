"""
This supposed to take 3 inputs convert to an int and spit out an average score
Sam Goode sgoode1@dmacc.edu 6/4/2020
"""
last_name = input("What is your last name? ")
first_name = input("What is your first name? ")
age = input("How old are you? ")
test1 = int(input("Enter score for your first test: "))
test2 = int(input("Enter score for your second test: "))
test3 = int(input("Enter score for your third test: "))
total = (test1 + test2 + test3)
# Inputs for the user and total to simplify the function below
def average(total):
    return total / 3
# Calculating average


average_scores = average(total)
print(last_name, ",", first_name, age, "the average score of your tests are:", average(total))
# Print out the test score





