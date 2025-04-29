'''
This module demonstrates how to read a file and parse two different variables
to create two separate files for each tuple.

Author: Arnold Murphy
Date: 2025-04-23
'''


# Use 'with' statements and specify encoding for all file operations

# open inputFile.txt with the intention of reading it
with open("inputFile.txt", "r", encoding="utf-8") as inputFile, \
     open("passFile.txt", "w", encoding="utf-8") as passFile, \
     open("failFile.txt", "w", encoding="utf-8") as failFile:

    # loop through each line in inputFile.txt
    for line in inputFile:
        line_split = line.split()
        if line_split[2] == "P":
            # write the line to passFile.txt
            passFile.write(line)
        else:
            # write the line to failFile.txt
            failFile.write(line)

# End-of-file (EOF)
