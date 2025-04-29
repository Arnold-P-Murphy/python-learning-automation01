'''
This module demonstrates how to read a file and parse two different variables
to create two separate files for each tuple.

Author: Arnold Murphy
Date: 2025-04-27
'''

import xml.etree.ElementTree as ET

FILE_PATH = "groceries.xml"

tree = ET.parse(FILE_PATH)
root = tree.getroot()

items_over_6 = []
for item in root.findall("grocery_item"):
    name = item.find("name").text
    price = float(item.find("price").text)
    if float(price) > 6.00:
        items_over_6.append(name)
        print(name, price)


for item in root.findall("grocery_item"):
    name = item.find("name").text
    price = item.find("price").text
    print(name, price)

print("Items with a price over $6.00:", items_over_6)
# End-of-file (EOF)
