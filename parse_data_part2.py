'''
This module demonstrates how to read a file and parse two different variables
to create two separate files for each tuple.

Author: Arnold Murphy
Date: 2025-04-27
'''

import csv

FILE_PATH = "groceries.csv"

with open(FILE_PATH, "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)
    for row in csv_reader:
        row[1] = int(row[1])
        print(row)

# End-of-file (EOF)
