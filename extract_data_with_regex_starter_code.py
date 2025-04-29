"""
This module demonstrates how to : extract data with regex

Author: Arnold Murphy
Date: 2025-04-27
"""


import re

# uncomment the following line of code and fill in
# phoneNumRegex =
phoneNumRegex = re.compile(r'(\d{3})-\d{3}-\d{4}')
# uncomment the following line of code and fill in
# example =


EXAMPLE = "The number is 123-456-7890."

# uncomment the following line of code and fill in
# result =

result = phoneNumRegex.search(EXAMPLE)

# uncomment the following lines of code and fill in
if result:
    print("Phone number found:", result.group())
    print("Area code:", result.group()[0:3])

# End-of-file (EOF)
