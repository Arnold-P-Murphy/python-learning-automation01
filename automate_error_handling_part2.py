'''
This module demonstrates how to automate error handling in Python.
Author: Arnold Murphy
Date: 2025-04-28
'''


years = [1925, 1943, 1968, 1937, 1975, 1912, 1989, 1954, 1920, 1996]
years.sort()
print(years)
assert years[0] <= years[-1], "First element is greater than last element."


# End-of-file (EOF)
