"""
This module demonstrates how to:
Parse text files as data with comma separated values.
line into a list of words.

Author: Arnold Murphy
Date: 2025-04-28
"""

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("The result is: ", result)
except ValueError:
    print("You must enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
# End-of-file (EOF)
