
"""
This module demonstrates how to read a file line by line and split each
line into a list of words.

Author: Arnold Murphy
Date: 2025-04-23
"""

inputFile = open("inputFile.txt", "r", encoding="utf-8")

for line in inputFile:
    line_split = line.split()
    if line_split[2] == "P":
        print(line)
# print(inputFile.read())

inputFile.close()


# End-of-file (EOF)
