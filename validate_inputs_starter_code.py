'''
This module demonstrates how to validate user input using the
pyinputplus library.

Author: Arnold Murphy
Date: 2025-04-28
'''


import pyinputplus as pyip

print("\nEXAMPLE 1")

# uncomment the following line of code and fill in
result = pyip.inputInt("Enter the number of shopping bags you need:", min=0)


# uncomment the following line of code
print("\nYou will use", result, "store bags.")

print("\nEXAMPLE 2")

# uncomment the following line of code and fill in
result = pyip.inputMenu(
   ['red', 'blue', 'green'], lettered=True, numbered=False
)
# uncomment the following line of code
print("\nYou have chosen a", result, "marker.")

print("\nEXAMPLE 3")

# uncomment the following line of code and fill in
result = pyip.inputEmail(
   "Enter your email address:")

# uncomment the following line of code
print("\nThe email you entered:", result)

# End-of-file (EOF)
