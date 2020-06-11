"""
Sam Goode
sgoode1@gmail.com
6/10/2020
This code is designed to take user input, store it in some variable, and output a randomly generated number.
Assuming strings are not used code should work fine.
This program is a nested version of the previous assignment. It does basically the same function, but I am not
sure if this is exactly what is being asked .
"""


def main():
    store_variable = []
    sentinel_value = 99
    while True:
        user_input = input("Please input a number between 1 and 100. Input 99 if you want to stop.")
        try:
            user_input = int(user_input)
        except ValueError:
            print('Not correct format or integer(s).')
            return main()
            break
        while 0 < user_input <= 100:
            print("Thank you. This number is added to the list.")
            store_variable.append(user_input)
            print(store_variable)
            break
        if user_input == 99:
            print('Goodbye.')
            break


# Attempting to make this as realistic as possible and what I imagine a real albeit shorter version of a function
# would be in Python
# I am unsure of a way to ensure both a quality integer is inputted and to ensure that a string is pushed back
# Everything seems to be working. Only issue I am not sure if this is what is being asked.

if __name__ == '__main__':
    print(main())
