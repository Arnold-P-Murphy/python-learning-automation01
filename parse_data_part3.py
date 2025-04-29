'''
This module demonstrates how to read a file and parse two different variables
to create two separate files for each tuple.

Author: Arnold Murphy
Date: 2025-04-27
'''

import json

FILE_PATH = "groceries.json"

with open(FILE_PATH, "r", encoding="utf-8") as file:
    data = file.read()

parsed_data = json.loads(data)

print("apples quantity:", parsed_data["apples"])

# End-of-file (EOF)
