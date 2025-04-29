"""
This module demonstrates how to:
Parse text files as data with comma-separated values.
line into a list of words.

Author: Arnold Murphy
Date: 2025-04-27
"""
FILE_PATH = "items.txt"

with open(FILE_PATH, "r", encoding="utf-8") as file:
    data = file.read()

print("data:", data)
parsed_data = data.split(", ")
print("parsed data:", parsed_data)
print("item at index 2:", parsed_data[0])

# End-of-file (EOF)
